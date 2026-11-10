"""Test the local rating implication of displayed numeric decision triggers.

Source meaning, selection of material triggers, monotonicity outside tested
points and the causal narrative remain reviewed. These are not forecasts.
"""
import copy
import math
import re


def verify(decision, spec, record):
    import model_workbook as mw
    from display_bindings import measure
    import release_check as rc
    coverage=decision.get('triggerCoverage',{})
    tests=decision.get('triggerTests',[])
    if not isinstance(tests,list): raise ValueError('triggerTests must be a list')
    ids=[t.get('id') for t in tests]
    linked=coverage.get('testIds',[])
    if any(not isinstance(i,str) or not i.strip() for i in ids) or len(set(ids))!=len(ids):
        raise ValueError('Trigger tests need unique nonempty IDs')
    if not isinstance(linked,list) or len(set(linked))!=len(linked):
        raise ValueError('Trigger coverage testIds must be a unique list')
    if coverage.get('status')=='not-applicable':
        if tests or linked or not str(coverage.get('reason','')).strip():
            raise ValueError('Trigger non-applicability needs a reason and no omitted declared tests')
        return []
    if coverage.get('status')!='checked' or not tests or set(linked)!=set(ids):
        raise ValueError('Decide trigger coverage and account for every declared trigger test')
    base=mw.Engine(spec)
    results=[]
    for test in tests:
        if not str(test.get('rationale','')).strip(): raise ValueError('Each trigger test needs a rationale')
        b=test['boundary']
        rules=[r for r in decision.get('boundText',[]) if r['pointer']==b['pointer'] and b['token'] in r['inputs']]
        if len(rules)!=1: raise ValueError('Trigger boundary must identify one boundText pointer/token')
        binding=rules[0]['inputs'][b['token']]
        raw=base.value(*mw.target(binding['model'],''))
        style=binding.get('style','number'); decimals=binding.get('decimals',2)
        shown=measure([raw],style,decimals,binding.get('transform','identity'))
        mode=test.get('mode')
        if mode=='watch':
            if 'expectedRating' in test or 'relation' in test:
                raise ValueError('A watch level cannot promise an automatic rating or comparison outcome')
            results.append({'id':test['id'],'mode':'watch','displayed':shown,'automaticRatingVerified':False})
            continue
        if mode!='automatic' or test.get('expectedRating') not in ('Buy','Hold','Sell'):
            raise ValueError('Use an explained watch level or an automatic trigger with expectedRating')
        if binding.get('transform','identity')!='identity':
            raise ValueError('Automatic trigger input and displayed boundary must use the same signed coordinate')
        relation=test.get('relation')
        if relation not in ('>','>=','<','<='):
            raise ValueError('An automatic trigger needs its actual strict/inclusive relation')
        input_ref=test['inputRef']
        input_key=mw.target(input_ref,'')
        if input_key==mw.target(record['bindings']['rating'],''):
            raise ValueError('Test an economic input, not an override of the rating output')
        if input_key not in rc.dependencies(spec,record['bindings']['target']) and input_key not in rc.dependencies(spec,record['bindings']['referencePrice']):
            raise ValueError('Automatic trigger input must influence the target or reference price; a disconnected input proves no decision relevance')
        if input_key[1] not in spec['sheets'].get(input_key[0],{}).get('cells',{}):
            raise ValueError('Trigger inputRef must identify an existing model cell')
        numeric=re.sub(r'[%x,]','',shown)
        boundary=float(numeric)/(100 if style=='percent' else 1)
        quantum=10**(-decimals)/(100 if style=='percent' else 1)
        direction=1 if relation.startswith('>') else -1
        # Test just inside the printed condition, not just the unrounded computed boundary.
        epsilon=max(quantum*1e-6,math.ulp(boundary)*16)
        points=[boundary if '=' in relation else boundary+direction*epsilon,
                boundary+direction*quantum]
        outputs=[]
        for point in points:
            temporary=copy.deepcopy(spec)
            temporary['sheets'][input_key[0]]['cells'][input_key[1]]['value']=point
            engine=mw.Engine(temporary)
            values={k:engine.value(*mw.target(record['bindings'][k],'')) for k in ('referencePrice','target','rating')}
            if (type(values['referencePrice']) not in (int,float) or values['referencePrice']<=0 or
                    type(values['target']) not in (int,float) or not math.isfinite(values['target'])):
                raise ValueError('Trigger probe produced an invalid target or reference price')
            ret=rc.price_return(values['target'],values['referencePrice'])
            actual=rc.rating_for(ret)
            if values['rating']!=actual or actual!=test['expectedRating']:
                raise ValueError(f'Trigger {test["id"]}: printed {relation} {shown}, input {point:.12g} gives '
                                 f'{actual} ({ret:.8%}), not {test["expectedRating"]}; qualify as a watch level or fix precision/meaning')
            outputs.append({'input':point,'rating':actual,'priceReturn':float(ret)})
        results.append({'id':test['id'],'mode':mode,'displayed':shown,'relation':relation,'probes':outputs})
    return results
