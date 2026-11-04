"""Compare explicitly normalised forecast snapshots; never guesses workbook mappings.

python compare_forecasts.py left.json right.json --out comparison.json
Positive gaps mean left above right. Sources are retained, not verified here.
"""
import argparse,json,math
from pathlib import Path

def number(value):
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value):
        raise ValueError('Expected a finite numeric observation, not missing data or an error')
    return value

def index(snapshot):
    if not snapshot.get('as_of') or not snapshot.get('label'):raise ValueError('Snapshot needs label and as_of')
    out={}
    for row in snapshot['metrics']:
        for field in ['id','period','unit','basis','scope','source']:
            if not row.get(field):raise ValueError('Missing mapping field: '+field)
        key=(row['id'],row['period'])
        if key in out:raise ValueError('Duplicate metric/period '+str(key))
        number(row['value']);out[key]=row
    return out

def compare_snapshots(left,right):
    a,b=index(left),index(right);rows=[]
    for key in sorted(a.keys()|b.keys()):
        x,y=a.get(key),b.get(key)
        if x is None or y is None:
            rows.append({'id':key[0],'period':key[1],'status':'missing counterpart'});continue
        mismatch=[f for f in ['unit','basis','scope'] if x[f]!=y[f]]
        row={'id':key[0],'period':key[1],'left':x,'right':y,'status':'definition mismatch' if mismatch else 'comparable','mismatch':mismatch}
        if not mismatch:
            row['difference']=x['value']-y['value']
            row['relative_difference']=row['difference']/abs(y['value']) if y['value']!=0 else None
        rows.append(row)
    return {'left_label':left['label'],'right_label':right['label'],'left_as_of':left['as_of'],'right_as_of':right['as_of'],'direction':'left minus right; a forecast gap is not a realised error','rows':rows}

def gross_profit_bridge(left_revenue,left_margin,right_revenue,right_margin):
    """Symmetric exact decomposition: revenue and margin effects share interaction.
    Revenue includes price/mix/units; never describe its effect as volume alone.
    Call only after establishing the same component perimeter and period.
    """
    lr,lm,rr,rm=map(number,[left_revenue,left_margin,right_revenue,right_margin])
    revenue=(lr-rr)*(lm+rm)/2
    margin=(lm-rm)*(lr+rr)/2
    total=lr*lm-rr*rm
    if abs(total-revenue-margin)>1e-9*max(1,abs(total)):raise ArithmeticError('Bridge does not close')
    return {'revenue_effect':revenue,'margin_effect':margin,'total_gp_gap':total,'interaction_convention':'half to each effect; revenue is not physical volume'}

def additive_bridge(left,right,total_id,components,period,tolerance=1e-6):
    """Reconcile total gap to signed component gaps; do not hide residuals.
    components: [{id, sign}], where the underlying metrics use consistent signs.
    """
    a,b=index(left),index(right);result=[]
    def gap(metric):
        x,y=a[(metric,period)],b[(metric,period)]
        if any(x[f]!=y[f] for f in ['unit','basis','scope']):raise ValueError('Noncomparable bridge metric '+metric)
        return x['value']-y['value']
    for item in components:result.append({'id':item['id'],'effect':gap(item['id'])*number(item['sign'])})
    total=gap(total_id);residual=total-sum(r['effect'] for r in result)
    return {'total_id':total_id,'period':period,'components':result,'total_gap':total,'unexplained_residual':residual,'reconciled':abs(residual)<=tolerance,'scope':'Accounting attribution, not causal proof or an isolated counterfactual'}

def main():
    p=argparse.ArgumentParser();p.add_argument('left',type=Path);p.add_argument('right',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    result=compare_snapshots(json.loads(a.left.read_text(encoding="utf-8-sig")),json.loads(a.right.read_text(encoding="utf-8-sig")))
    a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'out':str(a.out),'comparable':sum(r['status']=='comparable' for r in result['rows']),'excluded':sum(r['status']!='comparable' for r in result['rows'])}))

if __name__=='__main__':main()
