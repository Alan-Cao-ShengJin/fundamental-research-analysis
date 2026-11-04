"""Multi-sheet company model: build an Excel workbook from a cell specification,
calculate it independently and check that a recalculated workbook still matches.

build SPEC.json MODEL.xlsx [--outputs OUT.json]
calculate SPEC.json [--outputs OUT.json]
check SPEC.json MODEL.xlsx [--report REPORT.json]

SPEC.json:
{"title": "...", "sheets": {"3S": {"lastColumn": "K", "notes": "L", "sections": [6, 40],
  "cells": {"B7": {"value": "Revenue"}, "D7": {"value": 1200, "kind": "actual"},
            "G7": {"value": "=F7*(1+G8)"}, "G8": {"value": 0.1, "kind": "input", "pct": true}}}},
 "scenario": {"cell": "Revenue Projection!C2", "cases": ["Bear", "Base", "Bull"]},
 "outputs": {"eps.FY2027": "3S!G44"}}

Cell kinds: actual (dark blue), input/judgment (purple on nude), calculation (black, default).
Formulas use + - * / ^, cell and range references across sheets, SUM, MIN, MAX, AVERAGE,
COUNT, STDEV (sample), SQRT, ABS, ROUND, IF with comparisons, and CHOOSE for scenario
selection. Range functions ignore text, as Excel does. No eval, macros or external links.
A sheet may list native Excel line charts:
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
INK = {'actual': '17365D', 'input': '7030A0', 'judgment': '7030A0', 'pct': 'A6A6A6', 'calculation': '000000'}
NUDE = 'F2DDD5'


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
            text = REF.sub(sub, v[1:]).replace('^', '**').replace('<>', '!=')
            text = re.sub(r'(?<![<>!=])=(?!=)', '==', text)
            result = self._walk(ast.parse(text, mode='eval').body, refs, key)
            if type(result) in (int, float) and not math.isfinite(result):
                raise ModelError(f'Nonfinite result at {sheet}!{address}')
            return result
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
        if isinstance(n, ast.Constant) and type(n.value) in (int, float, str):
            return n.value
        if isinstance(n, ast.Name) and n.id in refs:
            sheet, start, end = refs[n.id]
            return self._range(sheet, start, end) if end else self.value(sheet, start)
        if isinstance(n, ast.BinOp):
            a, b = walk(n.left), walk(n.right)
            if type(a) not in (int, float) or type(b) not in (int, float):
                raise ModelError(f'Nonnumeric precedent at {key[0]}!{key[1]}')
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
            return {ast.Lt: a < b, ast.LtE: a <= b, ast.Gt: a > b, ast.GtE: a >= b, ast.Eq: a == b, ast.NotEq: a != b}[type(n.ops[0])]
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and not n.keywords:
            name, args = n.func.id.upper(), n.args
            if name == 'CHOOSE':
                i = walk(args[0])
                if type(i) not in (int, float) or int(i) != i or not 1 <= i < len(args):
                    raise ModelError(f'Invalid CHOOSE index at {key[0]}!{key[1]}')
                return walk(args[int(i)])
            if name == 'IF' and len(args) == 3:
                return walk(args[1]) if walk(args[0]) else walk(args[2])
            if name in ('SUM', 'MIN', 'MAX', 'AVERAGE', 'COUNT', 'STDEV'):
                xs = []
                for a in args:
                    v = walk(a)
                    xs.extend(v if isinstance(v, list) else [v])
                xs = [x for x in xs if type(x) in (int, float)]
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
                return round(walk(args[0]), int(walk(args[1])))
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
        outs = {name: values[f'{target(ref, "")[0]}!{target(ref, "")[1]}'] for name, ref in spec.get('outputs', {}).items()}
        result[label or 'Model'] = {'outputs': outs, 'cells': values}
    return result


def build(spec, path):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.workbook.defined_name import DefinedName
    from openpyxl.workbook.properties import CalcProperties
    from openpyxl.worksheet.datavalidation import DataValidation
    path = Path(path)
    if path.exists():
        raise ModelError('Refusing to overwrite ' + str(path) + '; archive it first')
    calculate(spec)  # fail before writing anything
    rule = Side(style='thin', color='DCE3E8')
    w = Workbook()
    w.remove(w.active)
    for name, d in spec['sheets'].items():
        ws = w.create_sheet(name)
        ws.sheet_view.showGridLines = False
        ws.freeze_panes = d.get('freeze', 'D6')
        last = colnum(d.get('lastColumn', 'H'))
        notes = d.get('notes')
        ws.column_dimensions['A'].width = 2
        ws.column_dimensions['B'].width = d.get('labelWidth', 46)
        for c in range(3, last + 1):
            ws.column_dimensions[colname(c)].width = d.get('columnWidth', 12)
        if notes:
            ws.column_dimensions[notes].width = 100
        for address, cell in d['cells'].items():
            v = cell.get('value')
            c = ws[address]
            c.value = v
            kind = cell.get('kind', 'calculation')
            pct = cell.get('pct', False)
            col = split(address)[0]
            if notes and col == notes:
                c.font = Font(name='Arial', size=9, color='536574')
                c.alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
                continue
            if not numeric(v):
                c.font = Font(name='Arial', size=10, bold=cell.get('bold', False), color='142B43')
                c.alignment = Alignment(horizontal='left' if col == 'B' else 'right', vertical='center')
                continue
            editable = kind in ('input', 'judgment')
            ink = INK['input'] if editable else INK['pct'] if pct else INK.get(kind, INK['calculation'])
            c.font = Font(name='Arial', size=10, color=ink, italic=pct, bold=cell.get('bold', False))
            if editable:
                c.fill = PatternFill('solid', fgColor=NUDE)
            c.alignment = Alignment(horizontal='right', vertical='center')
            c.number_format = cell.get('format') or ('0.0%;(0.0%);"-"' if pct else '#,##0.0;(#,##0.0);"-"')
            if cell.get('bold'):
                c.border = Border(top=rule)
            w.defined_names.add(DefinedName(binding(name, address), attr_text=f"'{name}'!${col}${split(address)[1]}"))
        for chart in d.get('charts', []):
            add_chart(ws, chart)
        for r in d.get('sections', []):
            for k in range(2, last + 1):
                c = ws.cell(r, k)
                c.fill = PatternFill('solid', fgColor='EDF0F3')
                c.font = Font(name='Arial', size=10, bold=True, color='142B43')
                c.border = Border(top=rule, bottom=rule)
    sc = spec.get('scenario')
    if sc:
        sheet, address = target(sc['cell'], '')
        dv = DataValidation(type='whole', operator='between', formula1=1, formula2=len(sc['cases']))
        dv.error = 'Choose ' + ', '.join(f'{i} {c}' for i, c in enumerate(sc['cases'], 1))
        w[sheet].add_data_validation(dv)
        dv.add(w[sheet][address])
    w.calculation = CalcProperties(calcId=191029, fullCalcOnLoad=True, forceFullCalc=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    w.save(path)


def add_chart(ws, chart):
    from openpyxl.chart import LineChart, Reference

    def ref(text):
        a, _, b = text.partition(':')
        (c1, r1), (c2, r2) = split(a), split(b or a)
        return Reference(ws, min_col=colnum(c1), min_row=r1, max_col=colnum(c2), max_row=r2)
    c = LineChart()
    c.title = chart.get('title')
    c.width, c.height = chart.get('width', 24), chart.get('height', 12)
    c.legend.position = chart.get('legend', 'r')
    if 'yMin' in chart:
        c.y_axis.scaling.min = chart['yMin']
    c.x_axis.delete = c.y_axis.delete = False   # openpyxl hides axes by default
    c.x_axis.tickLblSkip = chart.get('labelEvery', 12)
    c.y_axis.majorGridlines = None
    for s in chart['series']:
        c.add_data(ref(s), titles_from_data=True)
    for s in c.series:
        s.smooth = False
        s.marker.symbol = 'none'
    c.set_categories(ref(chart['categories']))
    ws.add_chart(c, chart['anchor'])


def same_formula(a, b):
    """Excel drops quotes around sheet names that do not need them."""
    norm = lambda s: re.sub(r"'([A-Za-z_][A-Za-z0-9_]*)'!", r'!', str(s).replace(' ', ''))  # noqa: E731
    return norm(a) == norm(b)


def check(spec, path):
    """Compare formulas, inputs, names and recalculated caches with the specification."""
    from openpyxl import load_workbook
    formulas = load_workbook(path, data_only=False)
    cache = load_workbook(path, data_only=True)
    e = Engine(spec)  # the workbook is saved with the specification's own selector value
    issues, count = [], 0
    for name, d in spec['sheets'].items():
        if name not in formulas.sheetnames:
            issues.append({'sheet': name, 'reason': 'missing sheet'})
            continue
        for address, cell in d['cells'].items():
            v = cell.get('value')
            got = formulas[name][address].value
            if not numeric(v):
                if got != v:
                    issues.append({'cell': f'{name}!{address}', 'reason': 'text drift'})
                continue
            count += 1
            if is_formula(v):
                if not same_formula(got, v):
                    issues.append({'cell': f'{name}!{address}', 'reason': 'formula drift'})
            elif not close(got, v):
                issues.append({'cell': f'{name}!{address}', 'reason': 'input drift'})
            expected, saved = e.value(name, address), cache[name][address].value
            if saved is None and expected == '':
                pass  # Excel stores an empty-text result as a blank cell
            elif saved is None:
                issues.append({'cell': f'{name}!{address}', 'reason': 'no calculated value saved; recalculate in Excel first'})
            elif not (close(expected, saved) if type(expected) in (int, float) else expected == saved):
                issues.append({'cell': f'{name}!{address}', 'expected': expected, 'saved': saved})
            if binding(name, address) not in formulas.defined_names:
                issues.append({'cell': f'{name}!{address}', 'reason': 'missing name'})
    for ws in cache:
        for row in ws.iter_rows():
            for c in row:
                if c.data_type == 'e':
                    issues.append({'cell': f'{ws.title}!{c.coordinate}', 'reason': str(c.value)})
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
