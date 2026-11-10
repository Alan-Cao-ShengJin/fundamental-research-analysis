"""Method-specific target bridges. Source selection and economic calibration remain reviewed."""
import math


def target(record,read):
    method=record['method']; b=record['bindings']
    def value(name):
        if name not in b: raise ValueError('Valuation method requires binding '+name)
        out=read(b[name])
        if type(out) not in (int,float) or not math.isfinite(out): raise ValueError('Finite numeric valuation binding required: '+name)
        return out
    def positive(name):
        out=value(name)
        if out<=0: raise ValueError('Positive valuation binding required: '+name)
        return out
    fx=value('fx') if 'fx' in b else 1
    if fx<=0: raise ValueError('Valuation FX must be positive')
    if method=='P/E':
        return positive('targetMultiple')*positive('forwardEps')/fx
    if method=='P/B':
        return positive('targetMultiple')*positive('bookValuePerShare')/fx
    if method=='dividend-yield':
        dps=value('dps')
        if dps<0: raise ValueError('Dividend per share must be nonnegative')
        return dps/positive('targetYield')/fx
    if method in ('EV/EBITDA','EV/Sales'):
        shares=value('shares')
        if shares<=0: raise ValueError('Valuation shares must be positive')
        return (positive('targetMultiple')*positive('enterpriseMetric')-value('netDebt')+value('nonOperatingValue')-value('minorityValue'))/shares/fx
    if method in ('SOTP','NAV','residual-income'):
        parts=record.get('valuationParts',[])
        if not parts or len({p['id'] for p in parts})!=len(parts): raise ValueError('Declare unique valuationParts with bound components and rationale')
        import release_check as rc
        import model_workbook as mw
        spec=record['_spec']
        target_ref=b['target']; total=0
        for part in parts:
            ref=part['valueRef']
            if not str(part.get('rationale','')).strip(): raise ValueError('Explain each valuation component and its economic boundary')
            if mw.target(target_ref,'') in rc.dependencies(spec,ref): raise ValueError('Valuation parts cannot consume the target they purportedly verify')
            weight=read(part['ownershipRef']) if part.get('ownershipRef') else 1
            if type(weight) not in (int,float) or not 0<=weight<=1: raise ValueError('Part ownership must lie between zero and one')
            component=read(ref)
            if type(component) not in (int,float) or not math.isfinite(component): raise ValueError('Valuation parts need finite numeric values')
            total+=component*weight
        shares=value('shares')
        if shares<=0: raise ValueError('Valuation shares must be positive')
        return total/shares/fx
    raise ValueError('Unsupported component valuation method')
