"""Create a blank local-chain scaffold or an explicitly synthetic sector example.
Uses the existing forecast_blocks.py compiler; does not classify issuers,
fetch evidence, choose forecasts, infer KPI completeness or write a workbook.
"""
import argparse,json
from pathlib import Path

ASSET=Path(__file__).resolve().parents[1]/'assets/sector-examples.json'
def cases():return json.loads(ASSET.read_text(encoding='utf-8'))['cases']

def make_plan(sector,example=False):
    all_cases=cases()
    if sector not in all_cases:raise ValueError('Unknown sector; choose an explicit supported activity: '+sector)
    data=all_cases[sector];nodes=[]
    for item in data['inputs']:
        nodes.append({'id':item['id'],'label':item['label'],'unit':item['unit'],'role':'foundation',
          'values':{'P1':item['value'] if example else None},
          'basis':{'P1':{'kind':'synthetic' if example else '',
             'source':'Independently invented arithmetic demonstration; no issuer or broker data' if example else '',
             'rationale':'Demonstrate this local mechanism only; replace with dated source evidence and an assessed forecast' if example else '',
             'uncertainty':'Not an empirical assumption range' if example else '',
             'next_evidence':'Gather the activity-specific source history and operating evidence described in the sector reference'}}})
    outputs=list(data['expected'])
    for item in data['calculations']:
        nodes.append({**item,'role':'output' if item['id'] in outputs else 'calculation',
                      **({'format':'percent'} if item['unit']=='ratio' else {})})
    return {'schema_version':1,'title':('Synthetic example | ' if example else 'Blank operating scaffold | ')+sector,
       'synthetic':example,'cadence':'unspecified','sector':sector,
       'periods':[{'id':'P1','label':'Illustrative period' if example else 'Replace with supported fiscal period','kind':'forecast'}],
       'blocks':[{'title':'Local economic chain | '+sector,'nodes':nodes}],
       'outputs':outputs,'scope':data['scope']+' This is not a complete company model. Add reconciled history, material business components, supported timing, financial statements/capital and valuation through the existing workflow.',
       'applicability_reason':'Demonstration only' if example else '',
       'limits':'Formulas calculate selected relationships; they do not verify source definitions, applicability, dimensions, forecasts, regulation or investment quality.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--list',action='store_true');p.add_argument('--sector');p.add_argument('--example',action='store_true');p.add_argument('--out',type=Path);a=p.parse_args()
    if a.list:print('\n'.join(sorted(cases())));return
    if not a.sector or not a.out:p.error('--sector and --out are required unless listing')
    if a.out.exists():p.error('Destination exists; choose a new path to preserve prior edits')
    try:plan=make_plan(a.sector,a.example)
    except ValueError as exc:p.error(str(exc))
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(plan,indent=2),encoding='utf-8');print(str(a.out))
if __name__=='__main__':main()
