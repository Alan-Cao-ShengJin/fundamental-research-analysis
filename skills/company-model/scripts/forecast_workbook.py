"""Portable forecast-plan Excel writer and mechanical synchronization check.

build PLAN.json MODEL.xlsx [--compiled MODEL.json]
check PLAN_OR_COMPILED.json MODEL.xlsx

Requires openpyxl. Supports only the forecast_blocks arithmetic grammar, not
arbitrary Excel features. Recalculates saved formulas independently in Python,
writes numeric caches, and verifies every declared input/calculation/output.
Never overwrites a supplied workbook or changes inputs during a sync check.
"""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
import math
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET
from zipfile import ZipFile

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.utils import get_column_letter
from openpyxl.utils.cell import absolute_coordinate
from forecast_blocks import compile_plan, ModelError

SHEET = 'Operating build'
NS = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def specification(value):
    """Recompile executable plans, or validate the basic compiled interface."""
    if 'blocks' in value:
        return compile_plan(value)
    if value.get('schema_version') != 1 or not value.get('rows') or not value.get('periods'):
        raise ModelError('Expected an executable forecast plan or compiled forecast blocks')
    return value


def bindings(spec):
    out = {}
    for row in spec['rows']:
        for cell in row['cells']:
            # Prefix makes names legal even when IDs resemble Excel addresses.
            name = 'm_' + row['id'] + '__' + re.sub(r'[^A-Za-z0-9_]', '_', cell['period'])
            if name.lower() in {n.lower() for n in out}:
                raise ModelError('Colliding workbook binding: ' + name)
            out[name] = (row, cell)
    return out


def numeric(value):
    return type(value) in (int, float) and math.isfinite(value)


def close(a, b):
    return numeric(a) and numeric(b) and math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-8)


def calculate(sheet, addresses):
    """Evaluate the saved Excel formulas, not the compiler's expected values.

    Restricted arithmetic AST; rejects names, functions, external references,
    missing inputs, cycles and zero denominators. No eval or macro execution.
    """
    allowed = set(addresses)
    result, visiting = {}, set()

    def cell(address):
        if address not in allowed:
            raise ModelError('Undeclared workbook precedent: ' + address)
        if address in result:
            return result[address]
        if address in visiting:
            raise ModelError('Workbook circular dependency: ' + address)
        visiting.add(address)
        value = sheet[address].value
        if isinstance(value, str) and value.startswith('='):
            try:
                tree = ast.parse(value[1:], mode='eval').body
            except SyntaxError as exc:
                raise ModelError('Unsupported Excel formula: ' + address) from exc

            def walk(node):
                if isinstance(node, ast.Name) and re.fullmatch('[A-Z]+[1-9][0-9]*', node.id):
                    return cell(node.id)
                if isinstance(node, ast.Constant) and numeric(node.value):
                    return node.value
                if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
                    v = walk(node.operand)
                    return -v if isinstance(node.op, ast.USub) else v
                if isinstance(node, ast.BinOp):
                    a, b = walk(node.left), walk(node.right)
                    if isinstance(node.op, ast.Add): return a+b
                    if isinstance(node.op, ast.Sub): return a-b
                    if isinstance(node.op, ast.Mult): return a*b
                    if isinstance(node.op, ast.Div) and b != 0: return a/b
                raise ModelError('Unsupported or undefined workbook arithmetic: ' + address)

            value = walk(tree)
        if not numeric(value):
            raise ModelError('Missing/non-numeric workbook value: ' + address)
        visiting.remove(address)
        result[address] = value
        return value

    for address in addresses:
        cell(address)
    return result


def cache_values(path, values):
    """Persist results calculated from saved formulas; openpyxl does not calculate."""
    with ZipFile(path) as source:
        entries = [(info, source.read(info.filename)) for info in source.infolist()]
    output = []
    for info, data in entries:
        if info.filename == 'xl/worksheets/sheet1.xml':
            root = ET.fromstring(data)
            for c in root.findall('.//x:sheetData/x:row/x:c', NS):
                if c.find('x:f', NS) is not None:
                    v = c.find('x:v', NS)
                    if v is None:
                        v = ET.SubElement(c, '{'+NS['x']+'}v')
                    v.text = repr(values[c.attrib['r']])
            data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
        output.append((info, data))
    # Temporary file and atomic replace avoid leaving a corrupt package on failure.
    with tempfile.NamedTemporaryFile(dir=path.parent, suffix='.xlsx', delete=False) as handle:
        tmp = Path(handle.name)
    try:
        with ZipFile(tmp, 'w') as destination:
            for info, data in output:
                destination.writestr(info, data)
        tmp.replace(path)
    finally:
        tmp.unlink(missing_ok=True)


def basis_text(row):
    groups = {}
    for cell in row['cells']:
        for field, title in [('source','Source'),('source_date','As of'),('rationale','Reason'),('uncertainty','Uncertainty')]:
            value = cell.get('basis', {}).get(field)
            if value:
                groups.setdefault((title, str(value)), []).append(cell['period'])
    return '. '.join(f'{title}{"" if len(periods)==len(row["cells"]) else " ("+"/".join(periods)+")"}: {value}' for (title,value),periods in groups.items())


def build(value, destination):
    spec = specification(value)
    path = Path(destination)
    if path.exists():
        raise ModelError('Destination exists; preserve the prior workbook and use a new path')
    mapped = bindings(spec)
    if any(not numeric(c.get('expected')) for _,c in mapped.values()):
        raise ModelError('Resolve missing inputs/undefined arithmetic before exporting a calculated workbook')
    book = Workbook(); sheet = book.active; sheet.title = SHEET
    theme = spec['theme']; colors = theme['colors']; layout = theme['layout']
    color = lambda key: colors[key].lstrip('#')
    side = Side(style=layout['border_style'], color=color('border'))
    last = max(row['row'] for row in spec['rows']); end_col = 3+len(spec['periods']); note_col = end_col+2
    sheet.sheet_view.showGridLines = layout['gridlines']; sheet.freeze_panes = 'D8'
    widths = {1:3, 2:layout['label_width'], 3:layout['unit_width'], end_col+1:3, note_col:layout['explanation_width']}
    for column in range(4,end_col+1): widths[column]=layout['period_width']
    for column,width in widths.items():sheet.column_dimensions[get_column_letter(column)].width=width
    for row in sheet.iter_rows(min_row=1,max_row=last,max_col=note_col):
        for c in row:
            c.font=Font(name=theme['font']['name'],size=theme['font']['size'],color=color('calculation'))
            c.alignment=Alignment(horizontal=layout['alignment'],vertical='center')
        sheet.row_dimensions[row[0].row].height=layout['row_height']
    def text(address,value):
        c=sheet[address]; c.value=value; c.data_type='s';return c
    text('B2',spec['title']).font=Font(name=theme['font']['name'],size=17,bold=True)
    sheet['B2'].alignment=Alignment(horizontal='left')
    text('B4','Synthetic example; no company forecasts' if spec['synthetic'] else 'Forecast build')
    text('B5','Blue: actual inputs. Blue/yellow: forecast assumptions. Black: calculations. Italic grey: memo ratios. Bold: totals.')
    sheet['B4'].alignment=sheet['B5'].alignment=Alignment(horizontal='left')
    text('B7','Metric');text('C7','Unit');text(f'{get_column_letter(note_col)}7','Basis and uncertainty')
    for i,p in enumerate(spec['periods'],4):text(f'{get_column_letter(i)}7',p['label'])
    for r in [7]+[s['row'] for s in spec['sections']]:
        for row in sheet.iter_rows(min_row=r,max_row=r,min_col=2,max_col=end_col):
            for c in row:
                c.fill=PatternFill('solid',fgColor=color('section_fill'));f=copy.copy(c.font);f.bold=True;c.font=f
                c.border=Border(bottom=side)
    for i,section in enumerate(spec['sections']):
        text('B'+str(section['row']),section['title'])
        end=min(last,spec['sections'][i+1]['row']-3 if i+1<len(spec['sections']) else last)
        for r in range(section['row'],end+1):
            sheet.cell(r,2).border=Border(left=side,top=side if r==section['row'] else None,bottom=side if r==end else sheet.cell(r,2).border.bottom)
            sheet.cell(r,end_col).border=Border(right=side,top=side if r==section['row'] else None,bottom=side if r==end else sheet.cell(r,end_col).border.bottom)
    for row in spec['rows']:
        r=row['row'];text('B'+str(r),row['label']);text('C'+str(r),row['unit'])
        percentage=row['format']=='percent';total=row['role']=='output' or row['subtotal']
        for c in row['cells']:
            cell=sheet[c['address']];cell.value=c['formula'] or c['value']
            forecast=next(p['kind']=='forecast' for p in spec['periods'] if p['id']==c['period'])
            assumption=forecast and (c['input'] or row['assumption'])
            ink='forecast_input' if assumption else 'percentage' if percentage else 'actual_input' if c['input'] else 'calculation'
            cell.font=Font(name=theme['font']['name'],size=theme['font']['size'],color=color(ink),bold=total,italic=percentage)
            if assumption:cell.fill=PatternFill('solid',fgColor=color('forecast_fill'))
            cell.number_format='0.0%;(0.0%);"-"' if percentage else '#,##0.0;(#,##0.0);"-"'
        for column in range(2,end_col+1):
            cell=sheet.cell(r,column);f=copy.copy(cell.font);f.bold=total;f.italic=percentage
            if column<4 and percentage:f.color=color('percentage')
            cell.font=f
            if total:
                b=copy.copy(cell.border);b.top=side;cell.border=b
        note=basis_text(row)
        if note:
            c=text(f'{get_column_letter(note_col)}{r}',note);c.alignment=Alignment(horizontal='left',vertical='center',wrap_text=True)
            c.font=Font(name=theme['font']['name'],size=9,color=color('explanation'))
            sheet.row_dimensions[r].height=max(layout['row_height'],math.ceil(len(note)/(layout['explanation_width']*1.15))*13+4)
    for name,(_,cell) in mapped.items():
        book.defined_names.add(DefinedName(name,attr_text=f"'{SHEET}'!{absolute_coordinate(cell['address'])}"))
    path.parent.mkdir(parents=True,exist_ok=True);book.save(path);book.close()
    saved=load_workbook(path,data_only=False)
    try:values=calculate(saved[SHEET],[c['address'] for _,c in mapped.values()])
    finally:saved.close()
    cache_values(path,values)
    report=check(spec,path)
    if not report['synchronized']:raise ModelError('Export failed synchronization: '+json.dumps(report['differences']))
    return report


def check(value, workbook):
    spec=specification(value);mapped=bindings(spec);path=Path(workbook)
    formulas=load_workbook(path,data_only=False);cached=load_workbook(path,data_only=True)
    differences=[]
    try:
        if SHEET not in formulas.sheetnames:raise ModelError('Missing declared worksheet')
        sheet=formulas[SHEET]
        addresses=[c['address'] for _,c in mapped.values()]
        try:calculated=calculate(sheet,addresses)
        except ModelError as error:
            calculated={};differences.append({'kind':'calculation','detail':str(error)})
        actual_names={n for n in formulas.defined_names if n.startswith('m_')}
        if actual_names!=set(mapped):differences.append({'kind':'binding_set','missing':sorted(set(mapped)-actual_names),'extra':sorted(actual_names-set(mapped))})
        for name,(row,c) in mapped.items():
            address=c['address'];actual=sheet[address].value;name_obj=formulas.defined_names.get(name)
            if name_obj is None or list(name_obj.destinations)!=[(SHEET, absolute_coordinate(address))]:
                differences.append({'name':name,'kind':'binding'})
            if sheet[f'B{row["row"]}'].value!=row['label'] or sheet[f'C{row["row"]}'].value!=row['unit']:
                differences.append({'name':name,'kind':'label_or_unit'})
            p=next(p for p in spec['periods'] if p['id']==c['period'])
            column=re.match('[A-Z]+',address)[0]
            if sheet[column+'7'].value!=p['label']:differences.append({'name':name,'kind':'period'})
            if c['formula']:
                if actual!=c['formula']:differences.append({'name':name,'kind':'formula','expected':c['formula'],'actual':actual})
            elif not close(actual,c['value']):differences.append({'name':name,'kind':'input','expected':c['value'],'actual':actual})
            for kind,v in [('calculated',calculated.get(address)),('cache',cached[SHEET][address].value)]:
                if not close(v,c['expected']):differences.append({'name':name,'kind':kind,'expected':c['expected'],'actual':v})
    finally:formulas.close();cached.close()
    return {'synchronized':not differences,'namedCellsChecked':len(mapped),'differences':differences,
            'workbookSha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'engine':'portable arithmetic AST evaluator; numeric XLSX caches verified',
            'limits':'Only forecast_blocks arithmetic is supported. No native Excel/LibreOffice verification, external links, macros or arbitrary Excel formulas. Evidence quality and forecast economics require analyst review.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['build','check']);parser.add_argument('model',type=Path);parser.add_argument('workbook',type=Path)
    parser.add_argument('--compiled',type=Path,help='Save the compiled machine interface from the same executable plan')
    args=parser.parse_args()
    try:
        value=json.loads(args.model.read_text(encoding='utf-8-sig'))
        report=build(value,args.workbook) if args.action=='build' else check(value,args.workbook)
        if args.compiled:
            if args.action!='build':raise ModelError('--compiled is a build option')
            args.compiled.parent.mkdir(parents=True,exist_ok=True)
            args.compiled.write_text(json.dumps(specification(value),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(report,ensure_ascii=False,indent=2))
        return 0 if report['synchronized'] else 1
    except (ModelError,OSError,ValueError,KeyError,TypeError) as error:
        parser.exit(2,f'Forecast workbook error: {error}\n')


if __name__=='__main__':raise SystemExit(main())
