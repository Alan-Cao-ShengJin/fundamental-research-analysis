"""Create a clean forecast-block scaffold or a wholly synthetic worked example."""
import argparse,json
from pathlib import Path


def make_plan(example=False,cadence='unspecified'):
    periods=[{'id':'P0','label':'P0 actual','kind':'actual'},{'id':'P1','label':'P1 forecast','kind':'forecast'},{'id':'P2','label':'P2 forecast','kind':'forecast'}]
    if cadence!='unspecified':
        unit={'quarter':'quarter','half_year':'half-year','annual':'year'}[cadence]
        for p,label in zip(periods,[f'Prior {unit} actual',f'Next {unit} forecast',f'Following {unit} forecast']):
            p['label']=label;p['frequency']=cadence
    blocks=[]
    for prefix,title,activity,realisation,cost in [('a','Component A',[100,110,120],[10,10.5,11],[6,6.2,6.4]),('b','Component B',[50,55,60],[20,20.5,21],[12,12.5,13])]:
        nodes=[]
        for name,label,unit,vals,why,uncertainty in [
            ('activity','Activity','activity',activity,'Illustrative activity path','Activity could be 10% lower or higher'),
            ('realisation','Value per activity','currency/activity',realisation,'Illustrative realisation path','Realisation could be 5% lower or higher'),
            ('unit_cost','Cost per activity','currency/activity',cost,'Illustrative cost path','Unit cost could be 8% higher')]:
            basis={'default':{'kind':'synthetic' if example else '', 'source':'Invented demonstration data' if example else '', 'rationale':why if example else '', 'uncertainty':uncertainty if example else ''}}
            nodes.append({'id':f'{prefix}_{name}','label':label,'unit':unit,'role':'foundation','values':{p['id']:v if example else None for p,v in zip(periods,vals)},'basis':basis})
        for name,label,formula in [('revenue','Component revenue',f'{prefix}_activity * {prefix}_realisation'),('cost','Component cost',f'{prefix}_activity * {prefix}_unit_cost'),('contribution','Component contribution',f'{prefix}_revenue - {prefix}_cost')]:
            nodes.append({'id':f'{prefix}_{name}','label':label,'unit':'currency','role':'calculation','subtotal':name=='contribution','formula':formula})
        blocks.append({'title':title,'nodes':nodes})
    blocks.append({'title':'Aggregate forecast','nodes':[
        {'id':'total_revenue','label':'Total revenue','unit':'currency','role':'output','formula':'a_revenue + b_revenue'},
        {'id':'total_cost','label':'Total cost','unit':'currency','role':'output','formula':'a_cost + b_cost'},
        {'id':'total_contribution','label':'Total contribution','unit':'currency','role':'output','formula':'a_contribution + b_contribution'},
        {'id':'contribution_margin','label':'Contribution margin','unit':'ratio','role':'output','format':'percent','formula':'total_contribution / total_revenue'}]})
    return {'schema_version':1,'title':'Synthetic forecast build' if example else 'Forecast build scaffold','synthetic':example,'cadence':cadence,'periods':periods,'blocks':blocks,'outputs':['total_revenue','total_cost','total_contribution','contribution_margin'],'scope':'An operating-build demonstration. Choose supported quarterly, half-year or annual periods, replace relative labels with the actual fiscal periods, design the business decomposition and add applicable financial schedules. No issuer data or sector-specific assumptions are included.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output',type=Path);parser.add_argument('--example',action='store_true')
    parser.add_argument('--cadence',choices=['unspecified','quarter','half_year','annual'],default='unspecified')
    args=parser.parse_args()
    if args.output.exists():parser.exit(2,'Destination exists; preserve prior work or choose a new path.\n')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(make_plan(args.example,args.cadence),indent=2),encoding='utf-8')
    print(args.output)
