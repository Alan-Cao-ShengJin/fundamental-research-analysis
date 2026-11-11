"""Multi-sheet company model: build an Excel workbook from a cell specification,
calculate it independently and check that a recalculated workbook still matches.

build SPEC.json MODEL.xlsx [--outputs OUT.json]
calculate SPEC.json [--outputs OUT.json]
check SPEC.json MODEL.xlsx [--report REPORT.json]

SPEC.json:
{"title": "...", "sheets": {"Statements": {"lastColumn": "K", "notes": "L", "sections": [6, 40],
  "cells": {"B7": {"value": "Revenue"}, "D7": {"value": 1200, "kind": "actual"},
            "G7": {"value": "=F7*(1+G8)"}, "G8": {"value": 0.1, "kind": "input", "pct": true}}}},
 "scenario": {"cell": "Cover!D9", "cases": ["Bear", "Base", "Bull"]},
 "outputs": {"eps.FY2027": "Statements!G44"},
 "sensitivities": [{"id": "s1", "inputs": ["Statements!G8"], "shock": -0.02, "mode": "add",
                    "eps": "Statements!G44", "shown": "Valuation!E60"}]}
Each declared sensitivity is recalculated through the whole model; `check` fails when the EPS change a table
shows differs from that recalculation (see sensitivities()).

Cell kinds: actual (blue), input/judgment (blue on light yellow), calculation (black; green when it
links to another sheet; dark grey italic for ratios; bold black for spec outputs).
Formulas use + - * / ^ and scalar text concatenation (&), simple numeric TEXT formats,
cell and range references across sheets, SUM, MIN, MAX, AVERAGE,
COUNT, STDEV (sample), SQRT, ABS, ROUND, IF with comparisons, NA() and CHOOSE for scenario
selection. The supported numeric subset uses worksheet precedence/rounding and case-insensitive plain text comparison. Range aggregates ignore text/logicals, retain numeric values and reject error values; scalar numeric strings/logicals are handled explicitly. Unsupported formula/type behavior is rejected rather than certified as general Excel compatibility. No eval, macros or external links.
Sheet options: notes (column whose text becomes cell comments on the row label), tagColumn + tags
(a physical column inserted for short source tags; the specification keeps its own addresses),
headerRows and forecastColumns (shaded headers and a rule at the forecast boundary), groupColumns and
groupRows ([first, last, collapsed]), helperColumns ([first, last]: chart-only data, grey and grouped),
unitColumn (centred units, default C), tabColor, zoom, wrap (text sheets), wrapColumns, widths,
printArea (charts are always added to it), fitPages (pages tall; otherwise page breaks avoid splitting
sections). Spec option "home" puts a "Back to Cover" link on every other sheet. Cell options: kind, pct,
bold, format, title, text (formula returning text), flag (green "OK" / red), link ("#'Sheet'!A1"),
merge (last column), wrap, align, date (ISO text written as a real date). Leading spaces in a label
become an indent. Every sheet prints A4 landscape, one page wide.
Defined names exist only for spec outputs and the case selector.
A sheet may list native Excel line or bar charts in the house style (see add_chart):
  "charts": [{"title": "...", "anchor": "P6", "categories": "B30:B149",
              "series": ["F29:F149", "J29:J149"], "width": 24, "height": 12,
              "yMin": 4, "labelEvery": 12, "legend": "r"}]
Each series range starts at its header cell, which names the line. The workbook is the human view; native Excel recalculation is checked
separately with recalc_excel.ps1 before `check`.
"""
from __future__ import annotations
import argparse, ast, copy, hashlib, json, math, re, sys
from functools import lru_cache
from pathlib import Path

REF = re.compile(r"(?:(?:'([^']+)'|([A-Za-z_][A-Za-z_0-9]*))!)?(\$?[A-Z]{1,3}\$?\d+)(?::(\$?[A-Z]{1,3}\$?\d+))?")
NA = '#N/A'   # NA() result: plotted as a gap, ignored by range functions


class ModelError(ValueError):
    pass


def colnum(s):
    n = 0
    for c in s:
        n = n * 26 + ord(c) - 64
    return n


def colname(n):
    s = ''
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def split(address):
    col, row = re.fullmatch('([A-Z]+)([0-9]+)', address.replace('$', '')).groups()
    return col, int(row)


def is_formula(v):
    return isinstance(v, str) and v.startswith('=')


def numeric(v):
    return type(v) in (int, float) or is_formula(v)


def binding(sheet, address):
    return 'm_' + re.sub('[^A-Za-z0-9_]', '_', sheet) + '__' + address


def close(a, b):
    return type(a) in (int, float) and type(b) in (int, float) and math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-6)


def target(ref, here):
    """'Sheet!A1' or 'A1' -> (sheet, address)."""
    sheet, _, address = ref.rpartition('!')
    return (sheet.strip("'") or here), address


class Engine:
    def __init__(self, spec):
        self.spec = spec
        self.visiting = set()

    def cells(self, sheet):
        try:
            return self.spec['sheets'][sheet]['cells']
        except KeyError:
            raise ModelError('Unknown sheet ' + sheet) from None

    @lru_cache(None)
    def value(self, sheet, address):
        key = (sheet, address)
        if key in self.visiting:
            raise ModelError(f'Circular reference at {sheet}!{address}')
        cell = self.cells(sheet).get(address)
        if cell is None or cell.get('value') is None:
            raise ModelError(f'Missing input {sheet}!{address}')
        v = cell['value']
        if not is_formula(v):
            return v
        self.visiting.add(key)
        try:
            refs = {}

            def sub(m):
                name = 'ref_' + str(len(refs))
                refs[name] = (m[1] or m[2] or sheet, m[3].replace('$', ''), m[4].replace('$', '') if m[4] else None)
                return name
            # References inside quoted worksheet strings are literal text, not precedents.
            parts = re.split(r'("(?:[^"]|"")*")', v[1:])
            text = ''.join(part if i % 2 else REF.sub(sub, part) for i, part in enumerate(parts))
            from worksheet_expression import parse
            result = self._walk(parse(text), refs, key)
            if type(result) in (int, float) and not math.isfinite(result):
                raise ModelError(f'Nonfinite result at {sheet}!{address}')
            return result
        except ModelError as exc:
            if str(exc).startswith('Missing input ') and ', needed by ' not in str(exc):
                raise ModelError(f'{exc}, needed by {sheet}!{address}') from None
            raise
        except (ValueError, TypeError, ArithmeticError) as exc:
            raise ModelError(f'{exc} at {sheet}!{address}') from exc
        finally:
            self.visiting.discard(key)

    def _range(self, sheet, start, end):
        c1, r1 = split(start)
        c2, r2 = split(end)
        cells = self.cells(sheet)
        return [self.value(sheet, f'{colname(c)}{r}') for r in range(r1, r2 + 1)
                for c in range(colnum(c1), colnum(c2) + 1) if f'{colname(c)}{r}' in cells]

    def _walk(self, n, refs, key):
        walk = lambda x: self._walk(x, refs, key)
        if isinstance(n, ast.Constant) and type(n.value) in (int, float, str, bool):
            return n.value
        if isinstance(n, ast.Name) and n.id in refs:
            sheet, start, end = refs[n.id]
            return self._range(sheet, start, end) if end else self.value(sheet, start)
        if isinstance(n, ast.BinOp):
            if isinstance(n.op, ast.BitAnd):
                from model_text import concatenate
                return concatenate(walk(n.left), walk(n.right))
            a, b = walk(n.left), walk(n.right)
            if type(a) not in (int, float) or type(b) not in (int, float):
                bad = n.left if type(a) not in (int, float) else n.right
                ref = refs.get(bad.id) if isinstance(bad, ast.Name) else None
                where = f'{ref[0]}!{ref[1]}' if ref and not ref[2] else 'a referenced cell'
                raise ModelError(f'Nonnumeric precedent at {key[0]}!{key[1]}: {where} holds text; a formula must start with "="')
            ops = {ast.Add: lambda: a + b, ast.Sub: lambda: a - b, ast.Mult: lambda: a * b, ast.Pow: lambda: a ** b}
            if isinstance(n.op, ast.Div):
                if b == 0:
                    raise ModelError(f'Division by zero at {key[0]}!{key[1]}')
                return a / b
            if type(n.op) in ops:
                return ops[type(n.op)]()
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.USub, ast.UAdd)):
            x = walk(n.operand)
            return -x if isinstance(n.op, ast.USub) else x
        if isinstance(n, ast.Compare) and len(n.ops) == 1:
            a, b = walk(n.left), walk(n.comparators[0])
            if isinstance(a,str) and isinstance(b,str): a,b=a.casefold(),b.casefold()
            import operator
            comparisons={ast.Lt:operator.lt,ast.LtE:operator.le,ast.Gt:operator.gt,ast.GtE:operator.ge,ast.Eq:operator.eq,ast.NotEq:operator.ne}
            ranks={int:0,float:0,str:1,bool:2}
            if type(a) not in ranks or type(b) not in ranks: raise ModelError('Unsupported worksheet comparison operand')
            if ranks[type(a)]!=ranks[type(b)]: a,b=ranks[type(a)],ranks[type(b)]
            try: return comparisons[type(n.ops[0])](a,b)
            except TypeError as exc: raise ModelError('Unsupported mixed-type worksheet comparison') from exc
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and not n.keywords:
            if n.func.id.upper() == 'TEXT' and len(n.args) == 2:
                from model_text import format_number
                return format_number(walk(n.args[0]), walk(n.args[1]))
            name, args = n.func.id.upper(), n.args
            if name == 'CHOOSE':
                i = walk(args[0])
                if type(i) not in (int, float) or int(i) != i or not 1 <= i < len(args):
                    raise ModelError(f'Invalid CHOOSE index at {key[0]}!{key[1]}')
                return walk(args[int(i)])
            if name == 'NA' and not args:
                return NA
            if name == 'IF' and len(args) == 3:
                condition=walk(args[0])
                if isinstance(condition,str):
                    if condition.upper() not in ('TRUE','FALSE'): raise ModelError('IF condition must be logical or numeric')
                    condition=condition.upper()=='TRUE'
                if type(condition) not in (bool,int,float): raise ModelError('IF condition must be logical or numeric')
                return walk(args[1]) if condition else walk(args[2])
            if name in ('SUM', 'MIN', 'MAX', 'AVERAGE', 'COUNT', 'STDEV'):
                xs = []
                for a in args:
                    v = walk(a)
                    if isinstance(v,list):
                        if NA in v: raise ModelError(f'Error value in {name} range at {key[0]}!{key[1]}')
                        xs.extend(x for x in v if type(x) in (int,float))
                    elif type(v) in (int,float,bool): xs.append(int(v) if isinstance(v,bool) else v)
                    elif isinstance(v,str) and v!=NA:
                        try: xs.append(float(v))
                        except ValueError as exc: raise ModelError('Unsupported nonnumeric scalar argument; use a numeric input or a range') from exc
                    else: raise ModelError(f'Error/unsupported value in {name}')
                if name == 'SUM':
                    return sum(xs)
                if name == 'COUNT':
                    return len(xs)
                if not xs or name == 'STDEV' and len(xs) < 2:
                    raise ModelError(f'Too few values for {name} at {key[0]}!{key[1]}')
                if name == 'STDEV':
                    m = sum(xs) / len(xs)
                    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
                return {'MIN': min, 'MAX': max, 'AVERAGE': lambda v: sum(v) / len(v)}[name](xs)
            if name == 'SQRT' and len(args) == 1:
                x = walk(args[0])
                if type(x) not in (int, float) or x < 0:
                    raise ModelError(f'Invalid SQRT at {key[0]}!{key[1]}')
                return math.sqrt(x)
            if name == 'ABS' and len(args) == 1:
                return abs(walk(args[0]))
            if name == 'ROUND' and len(args) == 2:
                from decimal import Decimal, ROUND_HALF_UP, localcontext
                value,digits=walk(args[0]),walk(args[1])
                if type(value) not in (int,float) or type(digits) not in (int,float):
                    raise ModelError('ROUND requires numeric arguments')
                with localcontext() as context:
                    context.prec=50
                    return float(Decimal(str(value)).quantize(Decimal(1).scaleb(-int(digits)),rounding=ROUND_HALF_UP))
        raise ModelError(f'Unsupported expression at {key[0]}!{key[1]}')


def with_case(spec, case):
    if case is None or not spec.get('scenario'):
        return spec
    s = copy.deepcopy(spec)
    sheet, address = target(spec['scenario']['cell'], '')
    s['sheets'][sheet]['cells'][address]['value'] = case
    return s


def calculate(spec):
    """Every numeric cell for each case; outputs by name."""
    cases = spec.get('scenario', {}).get('cases') or [None]
    result = {}
    for i, label in enumerate(cases, start=1):
        s = with_case(spec, i if label else None)
        e = Engine(s)
        values = {f'{sh}!{a}': e.value(sh, a) for sh, d in s['sheets'].items() for a, c in d['cells'].items() if numeric(c.get('value'))}
        outs = {}
        for name, ref in spec.get('outputs', {}).items():
            cell = '{}!{}'.format(*target(ref, ''))
            if cell not in values:
                raise ModelError(f'Output {name} points at {cell}, which has no calculated value')
            outs[name] = values[cell]
        result[label or 'Model'] = {'outputs': outs, 'cells': values}
    return result


STYLE = {'actual': '0000FF', 'input': '0000FF', 'judgment': '0000FF', 'calculation': '000000', 'link': '008000',
         'ratio': '595959', 'label': '000000', 'title': '1B2A41', 'muted': '595959'}
INPUT_FILL = 'FFF2CC'
SECTION_FILL = 'E7EBF0'
FORECAST_FILL = 'F2F2F2'
RULE = 'BFC7D0'
BODY, HEAD, TITLE = 9, 10, 12          # font sizes: body; headers and key outputs; sheet title
CHART_COLORS = ['1B2A41', '1F6F78', '6E7F96', '8DBCC1', '9AA3AE', 'B9C1CB']
UNIT_FORMATS = {   # number format by the row's unit label (column C) when a cell has no explicit format
    'RMB m': '#,##0.0;(#,##0.0);"–"', 'US$m': '#,##0.0;(#,##0.0);"–"', 'm': '#,##0.0;(#,##0.0);"–"',
    'RMB': '0.00;(0.00);"–"', 'US$': '0.00;(0.00);"–"', 'HKD': '0.00;(0.00);"–"', 'per share': '0.00;(0.00);"–"',
    '%': '0.0%;(0.0%);"–"', 'pt': '0.0" pt";(0.0" pt");"–"', 'x': '0.0"x";(0.0"x");"–"', 'days': '0;(0);"–"',
    'rate': '0.0000', 'units': '#,##0;(#,##0);"–"', 'people': '#,##0;(#,##0);"–"'}
DEFAULT_FORMAT = '#,##0.0;(#,##0.0);"–"'
PCT_FORMAT = '0.0%;(0.0%);"–"'
DATE_FORMAT = 'd mmm yyyy'
PAGE_PX = (1027, 688)   # printable A4 landscape area inside the margins, in pixels at 96 dpi


def with_negatives(fmt):
    """Negatives in parentheses whenever a format gives no negative section of its own."""
    if ';' in fmt or fmt in ('General', '@') or 'yy' in fmt or not re.search('[0#]', fmt):
        return fmt
    return f'{fmt};({fmt})'


def shown_text(v):
    """Leading spaces in a label become a cell indent: (text, indent level)."""
    s = v.lstrip(' ')
    return s, (len(v) - len(s) + 1) // 2


def text_lines(text, width, chars=1.45):
    """Lines a wrapped Arial text needs in a column of this width (Excel character units): greedy word wrap at about
    `chars` characters per width unit (1.45 for 9pt body text, 1.1 for 10pt bold headers)."""
    per = max(1.0, width * chars)
    lines = 0
    for part in str(text).split('\n'):
        n, used = 1, 0
        for word in part.split(' '):
            need = len(word) + (1 if used else 0)
            if used and used + need > per:
                n, used = n + 1, len(word)
            else:
                used += need
        lines += n + int(used > per)
    return lines


class Layout:
    """Logical (specification) addresses to physical workbook addresses. A sheet with 'tagColumn' gets one physical column
    inserted there for short source tags; every logical column at or right of it moves one to the right."""

    def __init__(self, spec):
        self.tag = {name: colnum(d['tagColumn']) for name, d in spec['sheets'].items() if d.get('tagColumn')}

    def col(self, sheet, col):
        n = colnum(col.replace('$', ''))
        return colname(n + 1) if sheet in self.tag and n >= self.tag[sheet] else colname(n)

    def addr(self, sheet, address):
        c, r = split(address)
        return f'{self.col(sheet, c)}{r}'

    def formula(self, sheet, text):
        """Rewrite every reference (outside quoted strings) to physical columns."""
        if not is_formula(text) or not self.tag:
            return text

        def sub(m):
            target_sheet = m[1] or m[2] or sheet
            def one(a):
                dollar_c = a.startswith('$')
                c, rest = re.fullmatch(r'\$?([A-Z]{1,3})(\$?\d+)', a).groups()
                return ('$' if dollar_c else '') + self.col(target_sheet, c) + rest
            prefix = m[0][:m.start(3) - m.start(0)]
            out = prefix + one(m[3])
            return out + (':' + one(m[4]) if m[4] else '')
        parts = re.split(r'("[^"]*")', text)
        return ''.join(p if p.startswith('"') else REF.sub(sub, p) for p in parts)

    def range(self, sheet, text):
        a, _, b = text.partition(':')
        return self.addr(sheet, a) + (':' + self.addr(sheet, b) if b else '')


def defined_name(key):
    n = re.sub(r'[^A-Za-z0-9_]', '_', key)
    return n if re.match(r'[A-Za-z_]', n) else '_' + n


def _is_link(sheet, v):
    """A formula that refers to another sheet."""
    return is_formula(v) and any((m[1] or m[2]) and (m[1] or m[2]) != sheet for m in REF.finditer(v))


def _col_px(ws, k):
    w = ws.column_dimensions[colname(k)].width
    return int((w if w is not None else 8.43) * 7 + 5)


def _row_px(ws, r):
    h = ws.row_dimensions[r].height
    return (h if h is not None else 15) * 4 / 3


def chart_extent(ws, chart, L, sheet):
    """Last physical column and row a chart covers."""
    if chart.get('range'):
        c, r = split(L.range(sheet, chart['range']).partition(':')[2])
        return colnum(c), r
    c, r = split(L.addr(sheet, chart['anchor']))
    k, need = colnum(c), chart.get('width', 24) / 2.54 * 96
    while need > 0:
        need -= _col_px(ws, k)
        k += 1
    need = chart.get('height', 12) / 2.54 * 96
    while need > 0:
        need -= _row_px(ws, r)
        r += 1
    return k - 1, r - 1


def page_breaks(ws, sections, first, last, last_col, titles):
    """Manual row breaks so that no section starts in the last rows of a page or splits when it would fit on the next."""
    from openpyxl.worksheet.pagebreak import Break
    scale = min(1.0, PAGE_PX[0] / sum(_col_px(ws, k) for k in range(1, last_col + 1)))
    cap = PAGE_PX[1] / scale * 0.97 - sum(_row_px(ws, r) for r in range(1, titles + 1))
    starts = sorted(s for s in sections if first <= s <= last)
    ends = {s: (starts[i + 1] - 1 if i + 1 < len(starts) else last) for i, s in enumerate(starts)}
    used = 0
    for r in range(first, last + 1):
        h = _row_px(ws, r)
        if r in ends:
            block = sum(_row_px(ws, x) for x in range(r, ends[r] + 1))
            lead = sum(_row_px(ws, x) for x in range(r, min(r + 3, ends[r]) + 1))
            if used and (used + block > cap and block <= cap or used + lead > cap):
                ws.row_breaks.append(Break(id=r - 1))
                used = 0
        used += h
        if used > cap:
            used = h


def build(spec, path):
    from openpyxl import Workbook
    from openpyxl.comments import Comment
    from openpyxl.formatting.rule import FormulaRule
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.workbook.defined_name import DefinedName
    from openpyxl.workbook.properties import CalcProperties
    from openpyxl.worksheet.datavalidation import DataValidation
    from openpyxl.worksheet.hyperlink import Hyperlink
    from openpyxl.worksheet.page import PageMargins
    import datetime
    path = Path(path)
    if path.exists():
        raise ModelError('Refusing to overwrite ' + str(path) + ': move the existing workbook into an archive folder beside it under a name that records the review attempt, then build, recalculate and check again')
    calculate(spec)  # fail before writing anything
    engine = Engine(spec)   # text that formulas return, for wrapped row heights
    L = Layout(spec)
    thin = Side(style='thin', color=RULE)
    edge = Side(style='medium', color='7F8C99')
    outputs = {target(ref, '') for ref in spec.get('outputs', {}).values()}
    font = spec.get('font', 'Arial')
    home = spec.get('home')
    w = Workbook()
    w.remove(w.active)
    for name, d in spec['sheets'].items():
        ws = w.create_sheet(name)
        P = lambda a: L.addr(name, a)  # noqa: E731
        ws.sheet_view.showGridLines = False
        ws.sheet_view.zoomScale = d.get('zoom', 100)
        ws.freeze_panes = P(d.get('freeze', 'D6'))
        if d.get('tabColor'):
            ws.sheet_properties.tabColor = d['tabColor']
        notes = d.get('notes')
        wrap = d.get('wrap', False)
        wrap_cols = {L.col(name, c) for c in d.get('wrapColumns', [])}
        unit_col = d.get('unitColumn', 'C')   # None: the sheet has no units column
        key_bold = d.get('keyBold', False)     # output sheets: bold figures are key outputs
        top_align = wrap or bool(wrap_cols)    # text-heavy sheets: every cell top-aligned
        last = colnum(L.col(name, d.get('lastColumn', 'H')))
        ws.column_dimensions['A'].width = 2
        sections = set(d.get('sections', []))
        labels = [(shown_text(c['value']), c.get('bold')) for a, c in d['cells'].items()
                  if a[0] == 'B' and a[1:].isdigit() and int(a[1:]) > 3 and int(a[1:]) not in sections
                  and isinstance(c.get('value'), str) and not is_formula(c['value']) and not c.get('merge')
                  and not wrap and not c.get('wrap')]
        fit = max([len(s) / (1.3 if b else 1.45) + 2 * i + 1 for (s, i), b in labels] or [0])
        ws.column_dimensions['B'].width = min(60, max(d.get('labelWidth', 46), math.ceil(fit)))   # labels never clipped
        for c in range(3, last + 1):
            ws.column_dimensions[colname(c)].width = d.get('columnWidth', 11)
        if unit_col:
            ws.column_dimensions[L.col(name, unit_col)].width = d.get('unitWidth', 8)
        for col, width in d.get('widths', {}).items():
            ws.column_dimensions[L.col(name, col)].width = width
        if name in L.tag:
            ws.column_dimensions[colname(L.tag[name])].width = 11
        width_of = lambda k: ws.column_dimensions[colname(k)].width or 8.43  # noqa: E731
        units = {split(a)[1]: c['value'] for a, c in d['cells'].items()
                 if unit_col and split(a)[0] == unit_col and isinstance(c.get('value'), str)}
        top = d.get('headerRows', [])
        helper = [colnum(L.col(name, x)) for x in d['helperColumns']] if d.get('helperColumns') else None
        rows, heights = set(), {}
        for address, cell in d['cells'].items():
            v = cell.get('value')
            col, row = split(address)
            rows.add(row)
            if notes and col == notes:
                if v:
                    label = ws[f'B{row}']
                    cm = Comment(str(v), 'Note')
                    cm.width, cm.height = 420, max(60, 16 * (len(str(v)) // 70 + 2))
                    label.comment = cm
                continue
            c = ws[P(address)]
            k = c.column
            span = [k]
            if cell.get('merge'):
                span = list(range(k, colnum(L.col(name, cell['merge'])) + 1))
                ws.merge_cells(start_row=row, start_column=k, end_row=row, end_column=span[-1])
            link = cell.get('link')
            if link and link.startswith('#'):
                c.hyperlink = Hyperlink(ref=c.coordinate, location=link[1:])
            elif link:
                c.hyperlink = link
            kind = cell.get('kind', 'calculation')
            pct = cell.get('pct', False)
            key = (name, address) in outputs or key_bold and cell.get('bold') and numeric(v) and not cell.get('text')
            bold = cell.get('bold', False) or key
            if cell.get('date'):   # ISO text in the specification, a real date in the workbook
                c.value = datetime.date.fromisoformat(v)
                c.number_format = DATE_FORMAT
                c.font = Font(name=font, size=BODY, color=STYLE['actual' if kind == 'actual' else 'label'], bold=bold)
                c.alignment = Alignment(horizontal='right', vertical='center')
                continue
            if not numeric(v) or cell.get('text'):   # text, or a formula that returns text
                indent = 0
                if is_formula(v):
                    c.value = L.formula(name, v)
                else:
                    c.value, indent = shown_text(v) if isinstance(v, str) else (v, 0)
                in_head = row in top and col != 'B'
                heading = (in_head or bold and col not in ('A', 'B') and not cell.get('text')) and row > 3
                wraps = row > 3 and (wrap or c.column_letter in wrap_cols or heading or cell.get('wrap')) and not cell.get('nowrap')
                size, ink, b = BODY, STYLE['label'], bold
                if cell.get('title'):
                    size, ink = TITLE, STYLE['title']
                elif heading:
                    size, b = HEAD, True
                if in_head and row != max(top):
                    size, ink, b = 8, STYLE['muted'], False
                c.font = Font(name=font, size=size, bold=b, color=ink, underline='single' if link else None)
                if heading or in_head:
                    h = 'center'
                elif col in ('A', 'B') or row <= 3 or wraps or cell.get('text') or d.get('textAlign') == 'left':
                    h = 'left'
                elif col == unit_col:
                    h = 'center'
                else:
                    h = 'right'
                c.alignment = Alignment(horizontal=cell.get('align') or h, indent=indent, wrap_text=wraps,
                                        vertical='top' if (wraps or top_align and row > 3) and not heading else 'center')
                if heading and not in_head:
                    c.border = Border(bottom=thin)
                if wraps:
                    text = v if not is_formula(v) else engine.value(name, address)
                    lines = text_lines(text, sum(width_of(x) for x in span) - 1, 1.1 if heading else 1.45)
                    if lines > 1:
                        heights[row] = max(heights.get(row, 15), 12 * lines + 3)
                continue
            c.value = L.formula(name, v) if is_formula(v) else v
            editable = kind in ('input', 'judgment')
            if key:
                ink = STYLE['calculation']
            elif editable or kind == 'actual':
                ink = STYLE[kind]
            elif _is_link(name, v):
                ink = STYLE['link']
            elif cell.get('bold'):
                ink = STYLE['calculation']
            elif helper and helper[0] <= k <= helper[1]:
                ink = STYLE['muted']
            elif pct:
                ink = STYLE['ratio']
            else:
                ink = STYLE['calculation']
            c.font = Font(name=font, size=HEAD if key else BODY, color=ink, italic=ink == STYLE['ratio'], bold=bold)
            if editable and not key:
                c.fill = PatternFill('solid', fgColor=INPUT_FILL)
            c.alignment = Alignment(horizontal='right', vertical='top' if top_align and row > 3 else 'center')
            unit = units.get(row)
            c.number_format = with_negatives(cell.get('format') or (PCT_FORMAT if pct else UNIT_FORMATS.get(unit, DEFAULT_FORMAT)))
            if cell.get('bold') and top and not key:   # totals on time-series sheets
                c.border = Border(top=thin)
        for row, tag in d.get('tags', {}).items():
            c = ws.cell(int(row), L.tag[name])
            c.value = tag
            c.font = Font(name=font, size=8, color=STYLE['muted'])
            c.alignment = Alignment(horizontal='left', vertical='center', indent=1)
        fc_cols = [colnum(L.col(name, x)) for x in d.get('forecastColumns', [])]
        body = [r for r in rows if r > max(top or [0])]
        for k in fc_cols:
            for r in top:
                ws.cell(r, k).fill = PatternFill('solid', fgColor=FORECAST_FILL)
        if top:
            for k in range(2, last + 1):
                ws.cell(max(top), k).border = Border(bottom=thin)
        for k in fc_cols:
            if k - 1 not in fc_cols:
                for r in range(min(top or [1]), max(body or [1]) + 1):
                    cell = ws.cell(r, k)
                    cell.border = Border(left=edge, top=cell.border.top, bottom=cell.border.bottom)
        covered = []   # (first column, first row, last row) of charts that fill a range of this sheet
        for ch in d.get('charts', []):
            if ch.get('range'):
                a, _, b = L.range(name, ch['range']).partition(':')
                covered.append((colnum(split(a)[0]), split(a)[1], split(b)[1]))
        for r in d.get('sections', []):
            stop = min([k for k, r1, r2 in covered if r1 <= r <= r2] + [last + 1]) - 1   # the band ends at a chart
            for k in range(2, stop + 1):
                c = ws.cell(r, k)
                c.fill = PatternFill('solid', fgColor=SECTION_FILL)
                c.font = Font(name=font, size=HEAD, bold=True, color=STYLE['title'])
                c.alignment = Alignment(horizontal='left', vertical='center')
        for r in range(1, max(rows or [1]) + 1):
            if r in heights:
                ws.row_dimensions[r].height = heights[r]
            elif not wrap or r <= max(top or [5]):
                ws.row_dimensions[r].height = 18 if r == 1 else 15
        for g in d.get('groupColumns', []) + ([d['helperColumns']] if helper else []):
            ws.column_dimensions.group(L.col(name, g[0]), L.col(name, g[1]), outline_level=1,
                                       hidden=len(g) > 2 and bool(g[2]))
        for g in d.get('groupRows', []):
            for r in range(g[0], g[1] + 1):
                ws.row_dimensions[r].outlineLevel = 1
                ws.row_dimensions[r].hidden = len(g) > 2 and bool(g[2])
        for address, cell in d['cells'].items():
            if cell.get('flag'):   # status text: green when it contains "OK", red otherwise
                a = P(address)
                ws.conditional_formatting.add(a, FormulaRule(formula=[f'ISNUMBER(SEARCH("OK",{a}))'],
                                                             font=Font(name=font, bold=True, color='2E7D4F')))
                ws.conditional_formatting.add(a, FormulaRule(formula=[f'NOT(ISNUMBER(SEARCH("OK",{a})))'],
                                                             font=Font(name=font, bold=True, color='C00000')))
        na = [split(P(a)) for a, c in d['cells'].items() if is_formula(c.get('value')) and 'NA()' in c['value'].upper()]
        if na:   # chart gaps: #N/A stays in the cell but shows and prints in the fill colour
            c1, c2 = min(colnum(x) for x, _ in na), max(colnum(x) for x, _ in na)
            r1, r2 = min(r for _, r in na), max(r for _, r in na)
            ws.conditional_formatting.add(f'{colname(c1)}{r1}:{colname(c2)}{r2}',
                                          FormulaRule(formula=[f'ISNA({colname(c1)}{r1})'], font=Font(color='FFFFFF')))
        last_row = max(rows or [1])
        ws.page_setup.orientation = 'landscape'
        ws.page_setup.paperSize = ws.PAPERSIZE_A4
        ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, d.get('fitPages', 0)
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.page_margins = PageMargins(left=0.5, right=0.5, top=0.5, bottom=0.6, header=0.3, footer=0.3)
        ws.print_options.horizontalCentered = True
        titles = max(top or [d.get('titleRows', 3)])
        ws.print_title_rows = f'1:{titles}'
        if name in L.tag:
            ws.print_title_cols = f'A:{colname(L.tag[name])}'
        if d.get('printArea'):
            b = L.range(name, d['printArea']).partition(':')[2]
            pc, pr = colnum(split(b)[0]), split(b)[1]
        else:
            pc, pr = last, last_row
        for chart in d.get('charts', []):   # the print area always takes in the sheet's charts
            ec, er = chart_extent(ws, chart, L, name)
            pc, pr = max(pc, ec), max(pr, er)
        ws.print_area = f'A1:{colname(pc)}{pr}'
        if home and name != home:
            c = ws.cell(1, pc)
            c.value = 'Back to Cover'
            c.hyperlink = Hyperlink(ref=c.coordinate, location=f"'{home}'!A1")
            c.font = Font(name=font, size=BODY, color=STYLE['title'], underline='single')
            c.alignment = Alignment(horizontal='right', vertical='center')
        if not d.get('fitPages'):
            page_breaks(ws, d.get('sections', []), titles + 1, pr, pc, titles)
        ws.oddFooter.left.text = '&F'
        ws.oddFooter.center.text = '&A'
        ws.oddFooter.right.text = 'Page &P of &N | &D'
        for part in (ws.oddFooter.left, ws.oddFooter.center, ws.oddFooter.right):
            part.size, part.font = 8, font
    for name, d in spec['sheets'].items():   # charts last, so they can use data on any sheet
        for chart in d.get('charts', []):
            add_chart(w[name], chart, L, name, w)
    sc = spec.get('scenario')
    if sc:
        sheet, address = target(sc['cell'], '')
        dv = DataValidation(type='whole', operator='between', formula1=1, formula2=len(sc['cases']))
        dv.error = 'Choose ' + ', '.join(f'{i} {c}' for i, c in enumerate(sc['cases'], 1))
        dv.prompt = dv.error
        w[sheet].add_data_validation(dv)
        dv.add(w[sheet][L.addr(sheet, address)])
        col, row = split(L.addr(sheet, address))
        w.defined_names.add(DefinedName('CaseSelector', attr_text=f"'{sheet}'!${col}${row}"))
    for key, ref in spec.get('outputs', {}).items():
        sheet, address = target(ref, '')
        col, row = split(L.addr(sheet, address))
        w.defined_names.add(DefinedName(defined_name(key), attr_text=f"'{sheet}'!${col}${row}"))
    w.calculation = CalcProperties(calcId=191029, fullCalcOnLoad=True, forceFullCalc=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    w.save(path)


def _rich(lines, rot=None):
    """Chart text: lines of (text, size, bold, colour); one line with text None gives axis or legend text properties."""
    from openpyxl.chart.text import RichText
    from openpyxl.drawing.text import CharacterProperties, Font as DrawingFont, Paragraph, ParagraphProperties, \
        RegularTextRun, RichTextProperties

    def props(size, bold, color):
        return CharacterProperties(sz=size * 100, b=bold, solidFill=color, latin=DrawingFont(typeface='Arial'))
    if lines[0][0] is None:
        _, size, bold, color = lines[0]
        return RichText(bodyPr=RichTextProperties(rot=rot, vert='horz'),
                        p=[Paragraph(pPr=ParagraphProperties(defRPr=props(size, bold, color)), endParaRPr=props(size, bold, color))])
    return RichText(p=[Paragraph(pPr=ParagraphProperties(defRPr=props(s, b, col)), r=[RegularTextRun(rPr=props(s, b, col), t=t)])
                       for t, s, b, col in lines])


def add_chart(ws, chart, L=None, sheet=None, book=None):
    """Native Excel chart in the house style. kind 'line' (default) or 'bar' (stacked when 'stacked'); per-series 'colors'
    (default: house palette) and 'dash' ('solid', 'dash', 'sysDot'); yMin/yMax/yMajor/yFormat; 'note' (a grey second
    title line, e.g. for data the axis clips); 'forecastFrom' (category index from which bars are hatched and lines
    dashed); 'range' (cells the chart fills, so it aligns with column edges) or 'anchor' + width/height in cm; legend
    at the bottom; blanks and #N/A plot as gaps; data in hidden (grouped) cells still plots."""
    from openpyxl.chart import BarChart, LineChart, Reference
    from openpyxl.chart.axis import ChartLines
    from openpyxl.chart.marker import DataPoint
    from openpyxl.chart.shapes import GraphicalProperties
    from openpyxl.chart.text import Text
    from openpyxl.chart.title import Title
    from openpyxl.drawing.fill import ColorChoice, PatternFillProperties
    from openpyxl.drawing.line import LineProperties
    from openpyxl.drawing.spreadsheet_drawing import AnchorMarker, TwoCellAnchor

    def ref(text):
        src, here = ws, sheet
        if '!' in text:   # data on another sheet
            here, _, text = text.rpartition('!')
            here = here.strip("'")
            src = book[here]
        text = L.range(here, text) if L else text
        a, _, b = text.partition(':')
        (c1, r1), (c2, r2) = split(a), split(b or a)
        return Reference(src, min_col=colnum(c1), min_row=r1, max_col=colnum(c2), max_row=r2)
    kind = chart.get('kind', 'line')
    c = BarChart() if kind == 'bar' else LineChart()
    if kind == 'bar':
        c.type = 'col'
        if chart.get('stacked'):
            c.grouping, c.overlap = 'stacked', 100
        c.gapWidth = 60
    if chart.get('title'):
        lines = [(chart['title'], 11, True, '1B2A41')] + ([(chart['note'], 8, False, '595959')] if chart.get('note') else [])
        c.title = Title(tx=Text(rich=_rich(lines)), overlay=False)
    c.width, c.height = chart.get('width', 24), chart.get('height', 12)
    c.legend.position = chart.get('legend', 'b')
    c.legend.overlay = False   # keep the legend beside the plot, not over the data or axis labels
    c.legend.txPr = _rich([(None, 8, False, '595959')])
    if 'yMin' in chart:
        c.y_axis.scaling.min = chart['yMin']
    if 'yMax' in chart:
        c.y_axis.scaling.max = chart['yMax']
    if 'yMajor' in chart:
        c.y_axis.majorUnit = chart['yMajor']
    c.y_axis.number_format = chart.get('yFormat', '#,##0')
    c.x_axis.delete = c.y_axis.delete = False   # openpyxl hides axes by default
    c.x_axis.tickLblSkip = chart.get('labelEvery', 1)
    c.x_axis.tickMarkSkip = chart.get('labelEvery', 1)
    c.x_axis.txPr = _rich([(None, 8, False, '595959')], rot=0)
    c.y_axis.txPr = _rich([(None, 8, False, '595959')])
    c.y_axis.majorGridlines = ChartLines(spPr=GraphicalProperties(ln=LineProperties(solidFill='E1E5EA', w=6350)))
    c.y_axis.spPr = GraphicalProperties(ln=LineProperties(noFill=True))
    c.graphical_properties = GraphicalProperties(ln=LineProperties(noFill=True))   # no chart border
    c.display_blanks = 'gap'
    c.visible_cells_only = False
    for s in chart['series']:
        c.add_data(ref(s), titles_from_data=True, from_rows=chart.get('byRow', False))
    colors, dashes = chart.get('colors') or CHART_COLORS, chart.get('dash', [])
    cats = ref(chart['categories'])
    n = (cats.max_row - cats.min_row + 1) * (cats.max_col - cats.min_col + 1)
    split_at = chart.get('forecastFrom', n)
    for i, s in enumerate(c.series):
        color = colors[i % len(colors)]
        if kind == 'bar':
            s.graphicalProperties = GraphicalProperties(solidFill=color)
            s.graphicalProperties.line.solidFill = color
            for p in range(split_at, n):   # forecast bars hatched in the series colour
                hatch = PatternFillProperties(prst='wdUpDiag', fgClr=ColorChoice(srgbClr=color), bgClr=ColorChoice(srgbClr='FFFFFF'))
                s.dPt.append(DataPoint(idx=p, invertIfNegative=False,
                                       spPr=GraphicalProperties(pattFill=hatch, ln=LineProperties(solidFill=color))))
            continue
        s.smooth = False
        s.marker.symbol = 'none'
        width = 19050 if i == 0 else 12700
        s.graphicalProperties.line = LineProperties(solidFill=color, w=width, prstDash=dashes[i] if i < len(dashes) else 'solid')
        for p in range(split_at, n):
            s.dPt.append(DataPoint(idx=p, spPr=GraphicalProperties(ln=LineProperties(solidFill=color, w=width, prstDash='dash'))))
    c.set_categories(cats)
    if L and chart.get('range'):
        a, _, b = L.range(sheet, chart['range']).partition(':')
        (c1, r1), (c2, r2) = split(a), split(b)
        c.anchor = TwoCellAnchor(editAs='oneCell', _from=AnchorMarker(col=colnum(c1) - 1, row=r1 - 1),
                                 to=AnchorMarker(col=colnum(c2), row=r2))
        ws.add_chart(c)
    else:
        ws.add_chart(c, L.addr(sheet, chart['anchor']) if L else chart['anchor'])


def same_formula(a, b):
    """Ignore harmless syntax normalization, preserving sheet identity and literal text."""
    def norm(value):
        parts=re.split(r'''("(?:[^"]|"")*"|'(?:[^']|'')*'!)''',str(value))
        result=[]
        for part in parts:
            if part.startswith('"'):
                result.append(part)  # spaces and case inside output text are meaningful
            elif part.startswith("'") and part.endswith("'!"):
                name=part[1:-2]
                result.append((name+'!' if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*',name) else part).upper())
            else:
                result.append(re.sub(r'\s+','',part).upper())
        return ''.join(result)
    return norm(a)==norm(b)


def shocked(spec, inputs, shock, mode):
    """A copy of the specification with each input cell moved by the shock: 'add' adds it, 'scale' multiplies by 1+shock."""
    if mode not in ('add','scale'): raise ModelError('Sensitivity mode must be add or scale')
    s = copy.deepcopy(spec)
    for ref in inputs:
        sheet, address = target(ref, '')
        cell = s['sheets'][sheet]['cells'].get(address)
        if cell is None or not numeric(cell.get('value')):
            raise ModelError(f'Sensitivity input {ref} is not a numeric cell')
        v = cell['value']
        if is_formula(v):
            cell['value'] = f'=({v[1:]})+{shock!r}' if mode == 'add' else f'=({v[1:]})*(1+{shock!r})'
        else:
            cell['value'] = v + shock if mode == 'add' else v * (1 + shock)
    return s


def recalculated(spec, d, base=None):
    """(EPS, EPS change) for one declared sensitivity, recalculated through the whole model."""
    base = base or Engine(spec)
    shock = d['shock']
    if isinstance(shock, str):
        shock = base.value(*target(shock, ''))
    eps = base.value(*target(d['eps'], ''))
    moved = Engine(shocked(spec, d['inputs'], shock, d.get('mode', 'add'))).value(*target(d['eps'], ''))
    return eps, moved - eps


def sensitivities(spec):
    """Recalculate the whole model for each declared sensitivity and compare the EPS change it shows.

    spec["sensitivities"] = [{"id": "s1", "inputs": ["Revenue Build!J20"], "shock": "Valuation!D60" or 0.05,
                              "mode": "add" or "scale", "eps": "Statements!J45", "shown": "Valuation!E60"}]
    A shortcut formula or a stale snapshot passes only when it reproduces the model's own tax, ownership, financing and
    share mechanics; the tolerance is 5% of the recalculated change or 0.1% of EPS, whichever is larger."""
    issues, base = [], Engine(spec)
    for d in spec.get('sensitivities', []):
        sid = d.get('id', '?')
        try:
            eps, delta = recalculated(spec, d, base)
            shown = base.value(*target(d['shown'], ''))
        except (KeyError, TypeError) as exc:
            issues.append({'sensitivity': sid, 'reason': f'declaration needs inputs, shock, eps and shown ({exc})'})
            continue
        if abs(shown - delta) > max(0.05 * abs(delta), 0.001 * abs(eps), 1e-9):
            issues.append({'sensitivity': sid, 'reason': 'shown EPS change differs from full-model recalculation',
                           'shown': shown, 'recalculated': delta, 'eps': eps})
    return issues


def check(spec, path):
    """Compare formulas, inputs, output names and recalculated caches with the specification."""
    from openpyxl import load_workbook
    formulas = load_workbook(path, data_only=False)
    cache = load_workbook(path, data_only=True)
    e = Engine(spec)  # the workbook is saved with the specification's own selector value
    L = Layout(spec)
    issues, count, na_cells = [], 0, set()
    for name, d in spec['sheets'].items():
        if name not in formulas.sheetnames:
            issues.append({'sheet': name, 'reason': 'missing sheet'})
            continue
        notes = d.get('notes')
        for address, cell in d['cells'].items():
            v = cell.get('value')
            if notes and split(address)[0] == notes:
                continue
            phys = L.addr(name, address)
            got = formulas[name][phys].value
            if not numeric(v):
                want = v
                if cell.get('date'):
                    got = got.date().isoformat() if hasattr(got, 'date') else got
                elif isinstance(v, str) and not is_formula(v):
                    want = shown_text(v)[0]
                if got != want and not (got is None and want == ''):   # Excel stores empty text as a blank cell
                    issues.append({'cell': f'{name}!{address}', 'reason': 'text drift'})
                continue
            count += 1
            if is_formula(v):
                if not same_formula(got, L.formula(name, v)):
                    issues.append({'cell': f'{name}!{address}', 'reason': 'formula drift'})
            elif not close(got, v):
                issues.append({'cell': f'{name}!{address}', 'reason': 'input drift'})
            expected, saved = e.value(name, address), cache[name][phys].value
            if expected == NA:
                na_cells.add(f'{name}!{phys}')
            if saved is None and expected == '':
                pass  # Excel stores an empty-text result as a blank cell
            elif saved is None:
                issues.append({'cell': f'{name}!{address}', 'reason': 'no calculated value saved; recalculate in Excel first'})
            elif not (close(expected, saved) if type(expected) in (int, float) else expected == saved):
                issues.append({'cell': f'{name}!{address}', 'expected': expected, 'saved': saved})
    names = set(formulas.defined_names.keys()) if hasattr(formulas.defined_names, 'keys') else \
        {n.name for n in formulas.defined_names.definedName}
    for key in spec.get('outputs', {}):
        if defined_name(key) not in names:
            issues.append({'name': defined_name(key), 'reason': 'missing output name'})
    for ws in cache:
        for row in ws.iter_rows():
            for c in row:
                if c.data_type == 'e' and f'{ws.title}!{c.coordinate}' not in na_cells:
                    issues.append({'cell': f'{ws.title}!{c.coordinate}', 'reason': str(c.value)})
    issues += sensitivities(spec)
    return {'passed': not issues, 'numericCellsChecked': count, 'issues': issues[:200],
            'workbookSHA256': hashlib.sha256(Path(path).read_bytes()).hexdigest()}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    p.add_argument('command', choices=['build', 'calculate', 'check'])
    p.add_argument('spec', type=Path)
    p.add_argument('workbook', type=Path, nargs='?')
    p.add_argument('--outputs', type=Path)
    p.add_argument('--report', type=Path)
    a = p.parse_args(argv)
    spec = json.loads(a.spec.read_text(encoding='utf-8-sig'))
    try:
        if a.command == 'check':
            report = check(spec, a.workbook)
            if a.report:
                a.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
            print(json.dumps({k: v for k, v in report.items() if k != 'issues'} | {'issues': len(report['issues'])}))
            return 0 if report['passed'] else 1
        if a.command == 'build':
            build(spec, a.workbook)
        result = calculate(spec)
        outs = {case: r['outputs'] for case, r in result.items()}
        if a.outputs:
            a.outputs.write_text(json.dumps(outs, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        print(json.dumps(outs, ensure_ascii=False))
        return 0
    except ModelError as err:
        print('Model error: ' + str(err), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
