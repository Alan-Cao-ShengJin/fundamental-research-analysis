"""Validate and compile generic, locally readable forecast blocks. No workbook writes.

python forecast_blocks.py plan.json --output compiled.json
Expressions support names, + - * /, unary minus, and lag(name) for one prior
period. No eval, code execution, implicit zeroes, or automatic source judgments.
"""
from __future__ import annotations
import argparse
import ast
import copy
import json
import math
from pathlib import Path


class ModelError(ValueError):
    pass


def col(number):
    text = ''
    while number:
        number, digit = divmod(number - 1, 26)
        text = chr(65 + digit) + text
    return text


def expression(text):
    try:
        tree = ast.parse(text, mode='eval').body
    except SyntaxError as exc:
        raise ModelError(f'Invalid expression: {text}') from exc
    def check(node):
        if isinstance(node, ast.Name):
            return
        if isinstance(node, ast.Constant) and type(node.value) in (int, float) and math.isfinite(node.value):
            return
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            check(node.left); check(node.right); return
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            check(node.operand); return
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'lag' and len(node.args) == 1 and isinstance(node.args[0], ast.Name) and not node.keywords:
            return
        raise ModelError(f'Unsupported expression element: {ast.dump(node)}')
    check(tree)
    return tree


def references(tree, period):
    if isinstance(tree, ast.Name):
        return [(tree.id, period)]
    if isinstance(tree, ast.Call):
        return [(tree.args[0].id, period - 1)]
    if isinstance(tree, ast.BinOp):
        return references(tree.left, period) + references(tree.right, period)
    if isinstance(tree, ast.UnaryOp):
        return references(tree.operand, period)
    return []


def compile_plan(plan):
    if plan.get('schema_version') != 1:
        raise ModelError('Expected schema_version 1')
    periods = plan.get('periods', [])
    if not periods or len({p['id'] for p in periods}) != len(periods):
        raise ModelError('Periods must be nonempty and unique')
    if any(p.get('kind') not in ('actual', 'forecast') for p in periods):
        raise ModelError('Every period needs actual or forecast kind')
    period_ids = {p['id'] for p in periods}
    nodes = {}; placement = {}; sections = []; row = 8
    for block in plan.get('blocks', []):
        sections.append({'row': row, 'title': block['title']}); row += 1
        for node in block.get('nodes', []):
            nid = node.get('id', '')
            if not nid.isidentifier() or nid in nodes or nid == 'lag':
                raise ModelError(f'Invalid, duplicate or reserved node ID: {nid}')
            if node.get('role') not in ('foundation', 'calculation', 'output'):
                raise ModelError(f'Unknown role for {nid}')
            if not node.get('label') or not node.get('unit'):
                raise ModelError(f'Missing label/unit for {nid}')
            if not set(node.get('values', {})) <= period_ids:
                raise ModelError(f'Unknown period value in {nid}')
            if node['role'] == 'foundation' and node.get('formula'):
                raise ModelError(f'Foundation {nid} must be an independent input; use a calculation row for formulas')
            nodes[nid] = node; placement[nid] = row; row += 1
        row += 2
    if not nodes:
        raise ModelError('At least one forecast block is required')
    outputs = plan.get('outputs', [])
    if not outputs or any(n not in nodes for n in outputs):
        raise ModelError('Outputs must identify existing nodes')
    findings = []; trees = {}; values = {}; states = {}; dependency_map = {}
    def add(code, nid, period, message):
        findings.append({'code': code, 'node': nid, 'period': period, 'message': message})
    for nid, node in nodes.items():
        if node.get('formula'):
            trees[nid] = expression(node['formula'])
        for i, p in enumerate(periods):
            explicit = p['id'] in node.get('values', {})
            if explicit:
                if node['values'][p['id']] is None:
                    add('missing_value', nid, p['id'], 'Input is missing; it will remain unavailable, not zero')
                if node['role'] != 'foundation' and p['kind'] == 'forecast':
                    add('forecast_override', nid, p['id'], 'A derived forecast is overridden. Explain its basis and downstream dependencies.')
                if node['role'] == 'foundation' or p['kind'] == 'forecast':
                    basis = node.get('basis', {}).get(p['id'], {})
                    for field in ('kind', 'source', 'rationale'):
                        if not basis.get(field):
                            add('missing_basis', nid, p['id'], f'Missing {field} beside independent input')
                    if basis.get('kind') and basis['kind'] != 'synthetic' and not basis.get('source_date'):
                        add('missing_source_date', nid, p['id'], 'Record the evidence availability date and check the research cutoff')
                    if p['kind'] == 'forecast' and not basis.get('uncertainty'):
                        add('missing_uncertainty', nid, p['id'], 'State the range, alternative or uncertainty in the foundational estimate')
            deps = [] if explicit else references(trees[nid], i) if nid in trees else []
            if not explicit and nid not in trees:
                add('missing_value', nid, p['id'], 'Input is missing; it will remain unavailable, not zero')
            for dep, di in deps:
                if dep not in nodes or di < 0:
                    raise ModelError(f'{nid}/{p["id"]}: unknown or unavailable precedent {dep}')
            dependency_map[(nid, i)] = deps
    def get(nid, i):
        key = (nid, i)
        if states.get(key) == 'visiting':
            raise ModelError(f'Circular dependency at {nid}/{periods[i]["id"]}')
        if key in values:
            return values[key]
        states[key] = 'visiting'; node = nodes[nid]; pid = periods[i]['id']
        if pid in node.get('values', {}):
            result = node['values'][pid]
            if result is not None and (type(result) not in (int, float) or not math.isfinite(result)):
                raise ModelError(f'Nonfinite/nonnumeric input at {nid}/{pid}')
        elif nid in trees:
            def calculate(t):
                if isinstance(t, ast.Constant):return t.value
                if isinstance(t, ast.Name):return get(t.id, i)
                if isinstance(t, ast.Call):return get(t.args[0].id, i-1)
                if isinstance(t, ast.UnaryOp):
                    v = calculate(t.operand)
                    return None if v is None else -v if isinstance(t.op, ast.USub) else v
                left, right = calculate(t.left), calculate(t.right)
                if left is None or right is None:return None
                if isinstance(t.op, ast.Add):return left + right
                if isinstance(t.op, ast.Sub):return left - right
                if isinstance(t.op, ast.Mult):return left * right
                if right == 0:
                    add('zero_denominator', nid, pid, 'Division by zero leaves this result unavailable')
                    return None
                return left / right
            result = calculate(trees[nid])
        else:result = None
        if result is not None and not math.isfinite(result):
            raise ModelError(f'Nonfinite calculation at {nid}/{pid}')
        values[key] = result; states[key] = 'done'; return result
    for nid in nodes:
        for i in range(len(periods)):get(nid, i)
    used = set()
    def walk(key):
        if key in used:return
        used.add(key)
        for dep in dependency_map[key]:walk(dep)
    for output in outputs:
        for i, p in enumerate(periods):
            if p['kind'] == 'forecast':walk((output, i))
    for nid, node in nodes.items():
        if node['role'] == 'foundation' and not any((nid, i) in used for i,p in enumerate(periods) if p['kind']=='forecast'):
            add('unused_foundation', nid, None, 'Input does not reach a selected forecast output')
    def excel(t, i):
        if isinstance(t, ast.Name):return f'{col(4+i)}{placement[t.id]}'
        if isinstance(t, ast.Constant):return str(t.value)
        if isinstance(t, ast.Call):return f'{col(3+i)}{placement[t.args[0].id]}'
        if isinstance(t, ast.UnaryOp):return ('-' if isinstance(t.op, ast.USub) else '+')+excel(t.operand,i)
        op={ast.Add:'+',ast.Sub:'-',ast.Mult:'*',ast.Div:'/'}[type(t.op)]
        return '('+excel(t.left,i)+op+excel(t.right,i)+')'
    compiled=[]
    for nid,node in nodes.items():
        cells=[]
        for i,p in enumerate(periods):
            explicit=p['id'] in node.get('values',{})
            deps=dependency_map[(nid,i)]
            formula=None
            if not explicit and nid in trees:
                refs=list(dict.fromkeys(f'{col(4+di)}{placement[dep]}' for dep,di in deps))
                body=excel(trees[nid],i)
                # Missing inputs propagate as #N/A in Excel; they never masquerade as zero.
                checks=','.join(refs)
                formula=f'=IF(COUNT({checks})={len(refs)},{body},NA())' if refs else '='+body
            basis=node.get('basis',{}).get(p['id'],{})
            cells.append({'period':p['id'],'address':f'{col(4+i)}{placement[nid]}','input':explicit,'value':node.get('values',{}).get(p['id']) if explicit else None,'formula':formula,'expected':values[(nid,i)],'basis':basis})
        compiled.append({'id':nid,'row':placement[nid],'label':node['label'],'unit':node['unit'],'role':node['role'],'subtotal':bool(node.get('subtotal')),'assumption':bool(node.get('assumption')),'format':node.get('format','number'),'cells':cells})
    default_theme=json.loads((Path(__file__).resolve().parents[1]/'assets/model-theme.json').read_text(encoding='utf-8'))
    return {'schema_version':1,'title':plan.get('title','Forecast build'),'synthetic':bool(plan.get('synthetic')),'cadence':plan.get('cadence','unspecified'),'theme':copy.deepcopy(plan.get('theme',default_theme)),'periods':periods,'sections':sections,'rows':compiled,'outputs':outputs,'findings':findings,'dependencies':{f'{n}/{periods[i]["id"]}':[f'{d}/{periods[di]["id"]}' for d,di in deps] for (n,i),deps in dependency_map.items()},'limits':'Checks cover declared structure and arithmetic. Evidence truth, economic fit, completeness, dimensional compatibility and predictive quality require analyst review.'}


def perturb(plan, node_id, period_id, value):
    changed=copy.deepcopy(plan)
    target=next((n for b in changed['blocks'] for n in b['nodes'] if n['id']==node_id),None)
    if target is None or target['role']!='foundation' or period_id not in target.get('values',{}):
        raise ModelError('Perturb a declared foundational input, not a derived result')
    if next(p for p in changed['periods'] if p['id']==period_id)['kind']!='forecast':
        raise ModelError('Perturbation must preserve historical inputs')
    target['values'][period_id]=value
    return compile_plan(changed)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan',type=Path);parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--set',nargs=3,metavar=('NODE','PERIOD','VALUE'))
    args=parser.parse_args();plan=json.loads(args.plan.read_text(encoding='utf-8'))
    try:
        result=perturb(plan,args.set[0],args.set[1],float(args.set[2])) if args.set else compile_plan(plan)
    except (ModelError,KeyError,TypeError,ValueError) as exc:
        parser.exit(2,f'Invalid forecast plan: {exc}\n')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'output':str(args.output),'rows':len(result['rows']),'review_findings':len(result['findings'])}))


if __name__=='__main__':main()
