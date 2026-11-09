"""Shared numeric presentation and verification; source/metric selection stays reviewed."""
import html
import json
import math


def measure(values, style='number', decimals=2, transform='identity', order='input'):
    if (not isinstance(values, (list, tuple)) or not 1 <= len(values) <= 2 or
            any(type(v) not in (int,float) or not math.isfinite(v) for v in values)):
        raise ValueError('A measure needs one finite value or two range endpoints')
    if type(decimals) is not int or not 0 <= decimals <= 6:
        raise ValueError('Use zero to six display decimals')
    if style not in ('number','percent','multiple') or transform not in ('identity','negate','magnitude') or order not in ('input','ascending'):
        raise ValueError('Unsupported measure format, transform or ordering')
    converted = [v if transform=='identity' else -v if transform=='negate' else abs(v) for v in values]
    if order == 'ascending':
        converted.sort()
    suffix = {'number':'','percent':'%','multiple':'x'}[style]
    factor = 100 if style=='percent' else 1
    # Suppress a displayed negative zero, not a materially negative value.
    shown = [f'{(0 if round(v*factor,decimals)==0 else v*factor):,.{decimals}f}{suffix}' for v in converted]
    return '–'.join(shown)


def bound_measure(claim_id, values, period, unit, *, style='number', decimals=2, transform='identity', order='input'):
    if not all(isinstance(s,str) and s.strip() for s in (claim_id,period,unit)):
        raise ValueError('A rendered measure needs ID, period and unit')
    values = list(values) if isinstance(values,(tuple,list)) else [values]
    text = measure(values,style,decimals,transform,order)
    attrs = {'data-model-claim':claim_id, 'data-values':json.dumps(values), 'data-period':period, 'data-unit':unit,
             'data-measure-format':style,'data-decimals':str(decimals),'data-transform':transform,'data-order':order}
    return '<span '+ ' '.join(f'{k}="{html.escape(v,quote=True)}"' for k,v in attrs.items())+'>'+html.escape(text)+'</span>'


def check_displays(study, displays, values, packet):
    """Check every occurrence in each named frozen HTML document, not a nearby number."""
    from publication_review import Figures, local
    if not displays:
        raise ValueError('A published measure needs at least one display binding')
    for display in displays:
        path = display['document']
        if path not in packet['reviewedFiles'] or not path.lower().endswith(('.html','.htm')):
            raise ValueError('Bind an explicit frozen HTML document')
        expected = measure(values,display.get('style','number'),display.get('decimals',2),
                           display.get('transform','identity'),display.get('order','input'))
        parser = Figures(); parser.feed(local(study,path).read_text(encoding='utf-8'))
        matches = [f for f in parser.figures if f['data-model-claim']==display['id']]
        if not matches:
            raise ValueError('No rendered measure: '+display['id'])
        for f in matches:
            if f.get('data-period')!=display['period'] or f.get('data-unit')!=display['unit']:
                raise ValueError('Rendered measure period/unit differs from its declaration')
            raw = json.loads(f.get('data-values','null'))
            if (not isinstance(raw,list) or len(raw)!=len(values) or
                    any(type(x) not in (int,float) or not math.isfinite(x) or not math.isclose(x,y,rel_tol=1e-12,abs_tol=1e-12)
                        for x,y in zip(raw,values))):
                raise ValueError('Rendered raw measure differs from its bound inputs')
            for attr,key,default in [('data-measure-format','style','number'),('data-decimals','decimals',2),
                                      ('data-transform','transform','identity'),('data-order','order','input')]:
                if f.get(attr)!=str(display.get(key,default)):
                    raise ValueError('Rendered measure transformation differs from its declaration')
            if f['text'].strip()!=expected:
                raise ValueError('Visible measure differs from its bound calculation: expected '+expected)
    return 'Declared values, transformations, range ordering and rendered text agree'
