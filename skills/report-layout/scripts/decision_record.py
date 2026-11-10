"""Synchronize and verify reusable decisions against the current calculated model.

This updates derived fields only. It never supplies an investment judgment,
approves a review, infers a source classification or rewrites historical studies.
"""
import argparse
import copy
from datetime import date
import json
import math
from pathlib import Path
import re
from string import Formatter


def pointer_parts(pointer):
    if not isinstance(pointer,str) or not pointer.startswith('/'):
        raise ValueError('Use a non-root JSON pointer')
    return [p.replace('~1','/').replace('~0','~') for p in pointer[1:].split('/')]


def get_at(data, pointer):
    for part in pointer_parts(pointer):
        data = data[int(part)] if isinstance(data,list) else data[part]
    return data


def set_at(data, pointer, value):
    parts = pointer_parts(pointer)
    for part in parts[:-1]:
        data = data[int(part)] if isinstance(data,list) else data[part]
    key = int(parts[-1]) if isinstance(data,list) else parts[-1]
    data[key] = value


def matches(actual, expected):
    if type(expected) in (int,float):
        return type(actual) in (int,float) and math.isfinite(actual) and math.isclose(actual,expected,rel_tol=1e-10,abs_tol=1e-10)
    return actual == expected


def text_from(rule, values):
    from display_bindings import measure
    names = []
    for literal, name, fmt, conversion in Formatter().parse(rule['template']):
        if name is not None:
            if not re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*',name) or fmt or conversion:
                raise ValueError('Bound text uses plain named tokens, without attributes, indexing or format code')
            names.append(name)
    if set(names)!=set(rule['inputs']) or not names:
        raise ValueError('Every bound-text input must appear in its template')
    shown = {name:measure([values[name]],binding.get('style','number'),binding.get('decimals',2),
                         binding.get('transform','identity')) for name,binding in rule['inputs'].items()}
    return rule['template'].format_map(shown)


def derived(study, record, spec, decision):
    import release_check as rc
    from publication_review import local
    vals = rc.cell_values(spec,local(study,record['workbook']),record['bindings'])
    if type(vals['referencePrice']) not in (int,float) or vals['referencePrice']<=0:
        raise ValueError('A decision needs a positive reference price')
    cutoff = date.fromisoformat(record['cutoff'])
    try:
        target_date = cutoff.replace(year=cutoff.year+1)
    except ValueError:
        target_date = cutoff.replace(year=cutoff.year+1,day=28)
    core = {'/schemaVersion':'1.1', '/security':record['security'], '/currency':record['currency'],
            '/cutoff':record['cutoff'], '/researchMode':record['researchMode'],
            '/quote/price':vals['referencePrice'], '/quote/date':record['priceDate'],
            '/rating':vals['rating'], '/targetPrice':vals['target'], '/targetDate':target_date.isoformat(),
            '/priceReturn':vals['target']/vals['referencePrice']-1,
            '/model/spec':record['spec'], '/model/workbook':record['workbook'],
            '/model/specSHA256':rc.sha256(local(study,record['spec'])),
            '/model/workbookSHA256':rc.sha256(local(study,record['workbook']))}
    for field in ('dividendYield','bearTarget','bullTarget'):
        if field in vals:
            core['/'+field] = vals[field]
    extras = {}
    for item in decision.get('bindings',[]):
        pointer_parts(item['pointer'])
        extras[item['pointer']] = rc.cell_values(spec,local(study,record['workbook']),{'v':item['model']})['v']
    for rule in decision.get('boundText',[]):
        pointer_parts(rule['pointer'])
        values = rc.cell_values(spec,local(study,record['workbook']),{k:b['model'] for k,b in rule['inputs'].items()})
        if rule['pointer'] in extras:
            raise ValueError('Duplicate decision pointer: '+rule['pointer'])
        extras[rule['pointer']] = text_from(rule,values)
    pointers = [x['pointer'] for x in decision.get('bindings',[])]+[x['pointer'] for x in decision.get('boundText',[])]
    if len(set(pointers))!=len(pointers):
        raise ValueError('Decision binding pointers must be unique')
    protected = ('/model','/quote','/bindings','/boundText','/triggerCoverage','/triggerTests')
    for p in extras:
        if p in core or any(p==root or p.startswith(root+'/') for root in protected):
            raise ValueError('Extra bindings cannot overwrite decision core or binding definitions')
        if any(q!=p and q.startswith(p+'/') for q in extras):
            raise ValueError('Decision binding pointers cannot overlap')
    from decision_triggers import verify
    verify(decision,spec,record)
    return dict(core,**extras)


def synchronize(study, record, spec, decision=None):
    """Return a refreshed record; caller saves it before preparation/review."""
    out = copy.deepcopy(decision or {})
    out.setdefault('quote',{}); out.setdefault('model',{})
    for pointer,value in derived(study,record,spec,out).items():
        set_at(out,pointer,value)
    return out


def check(study, record, spec):
    from publication_review import local
    rel = record.get('decisionRecord','evidence/decision.json')
    decision = json.loads(local(study,rel).read_text(encoding='utf-8-sig'))
    errors = []
    for pointer, expected in derived(study,record,spec,decision).items():
        try:
            actual = get_at(decision,pointer)
        except (KeyError,IndexError,ValueError,TypeError):
            errors.append('missing '+pointer); continue
        if not matches(actual,expected):
            errors.append(pointer+' is stale or inconsistent with the current model')
    if errors:
        raise ValueError('; '.join(errors))
    return 'Decision identity, dated core, spec/workbook hashes and declared numeric/text bindings agree; unbound judgments remain reviewed'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('sync','check'))
    parser.add_argument('study',type=Path)
    parser.add_argument('--record',default='deliverables/release.json')
    args = parser.parse_args()
    from publication_review import local
    record = json.loads(local(args.study,args.record).read_text(encoding='utf-8-sig'))
    spec = json.loads(local(args.study,record['spec']).read_text(encoding='utf-8-sig'))
    if args.action=='check':
        print(check(args.study,record,spec)); return
    path = local(args.study,record.get('decisionRecord','evidence/decision.json'))
    old = json.loads(path.read_text(encoding='utf-8-sig')) if path.exists() else {}
    out = synchronize(args.study,record,spec,old)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('Derived decision fields refreshed; dependent reviews must be refreshed before release.')


if __name__=='__main__':
    main()
