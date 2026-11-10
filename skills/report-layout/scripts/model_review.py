"""Fresh model/evidence challenge before writing; separate from the publication reader budget."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
from uuid import uuid4

PATH='evidence/model-review.json'
CHECKS=('model-integrity','source-basis','assumption-build','valuation-anchor')

def starts(study):
    directory=Path(study)/'evidence/model-review-starts'
    entries=[json.loads(p.read_text()) for p in sorted(directory.glob('attempt-*.json'))]
    if [r['attempt'] for r in entries]!=list(range(1,len(entries)+1)) or len(entries)>2: raise ValueError('Model review receipt history is incomplete or exceeds its budget')
    return entries

def requirements(packet):
    items={r['id']:r for r in packet.get('priorFindings',[])}
    for c in packet['handoff']['checks']:
        if c['blocking'] and c['result']=='fail': items['check:'+c['name']]={'id':'check:'+c['name'],'finding':c['detail']}
    for i,text in enumerate(packet['handoff']['criticalUnknowns']): items['unknown:'+str(i)]={'id':'unknown:'+str(i),'finding':text}
    return list(items.values())

def prepare(study,spec,workbook,evidence,security,cutoff):
    from publication_review import local,digest,evaluation_context
    from research_rules import pin,require_current
    pin(study); lock=require_current(study); study=Path(study); out=local(study,PATH)
    receipts=starts(study)
    if not out.exists() and (receipts or (study/'evidence/model-reviews').exists()): raise ValueError('Missing model review packet; preserve its prior findings and receipt history')
    if out.exists():
        old=json.loads(out.read_text()); used=len(receipts)
        if old.get('startedAt') and (not receipts or receipts[-1]['id']!=old['id']): raise ValueError('Model review receipt history conflicts with the current packet')
        if used>=2: raise ValueError('Pre-writing model review budget exhausted; retain unresolved findings')
        history=study/'evidence/model-reviews'; history.mkdir(exist_ok=True)
        shutil.copyfile(out,history/(digest(out)+'.json'))
    else: old=None; used=0
    refs=list(dict.fromkeys([spec,workbook,*evidence])); stamp=datetime.now(timezone.utc).isoformat()
    h={'id':'model-challenge','kind':'challenge','version':used+1,'status':'partial','notApplicableReason':None,
       'mandateId':None,'mandateVersion':None,'scopeIds':[security],'asOf':cutoff+'T00:00:00+00:00','producedAt':stamp,
       'summary':'Model checkpoint prepared; no substantive review performed.',
       'sources':[{'id':'input-'+str(i),'location':r,'locator':'SHA256 '+digest(local(study,r)),'publishedAt':None,'availableAt':None,
                   'retrievedAt':stamp,'accessStatus':'available','synthetic':False} for i,r in enumerate(refs)],
       'claims':[],'dependencies':[],'checks':[{'name':name,'result':'not-run','blocking':True,'detail':'Read and test the model and pivotal evidence.'} for name in CHECKS],
       'criticalUnknowns':old['handoff']['criticalUnknowns'] if old else [],'nextActions':[]}
    evaluation=evaluation_context(study,{})
    from publication_review import cutoff_timestamp
    h['asOf']=cutoff_timestamp(cutoff,stamp,os.environ.get('RESEARCH_TIMEZONE','Asia/Singapore'),evaluation)
    if evaluation:
        for source in h['sources']: source['synthetic']=True
    record={'schemaVersion':'1.0','id':uuid4().hex,'attempt':used+1,'maxAttempts':2,'startedAt':None,
        'reviewer':{'id':'unassigned','mode':'independent-agent','context':'fresh'},'inputs':{r:digest(local(study,r)) for r in refs},
        'spec':spec,'workbook':workbook,'rulesFingerprint':lock['productionFingerprint'],'evaluation':evaluation,
        'priorReviewSHA256':digest(out) if out.exists() else None,'handoff':h,
        'task':'Host launches a fresh reader before writing. Before work, run model_review.py begin STUDY --reviewer NAME. Independently search the permitted evidence universe for missing management remarks, covering-broker forecasts and competent outside analysis; obey fixed-pack boundaries and record access limits. Treat outside notes as leads and resolve factual disagreements against the appropriate original source. Reconstruct pivotal source facts, period/unit/ownership definitions, driver forecasts, cash/financing constraints and valuation anchor. Test central-case bias under research-cycle/references/investor-judgment.md and trace material scenario inputs through the model under company-model/references/model-standard.md. For dividend-led valuations or price-implied event weights, apply valuation-thesis/references/valuation-driver-and-dividends.md; unavailable comparables and unidentified probabilities must not be invented. For pivotal rate-to-profit conversions apply company-model/references/metric-identity.md. Distinguish independently supported, discretionary and price-implied valuation parameters; compare revised rationales with their preserved earlier derivation. Check dated cash entitlement where a receipt window is promised, and re-evaluate affected explanations after model changes. Check the strongest alternative. Record real findings and evidence-backed prior dispositions, then recheck corrections; never auto-pass. This is separate from the publication reader budget.'}
    record['priorFindings']=requirements(old) if old else []
    record['resolutions']=[]
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8'); return out

def begin(study,reviewer,mode='independent-agent'):
    from publication_review import local,digest
    path=local(study,PATH); p=json.loads(path.read_text())
    if not reviewer.strip() or reviewer=='unassigned' or mode not in ('human','independent-agent'): raise ValueError('Name a fresh reader')
    if any(digest(local(study,r))!=v for r,v in p['inputs'].items()): raise ValueError('Model checkpoint changed; no review started')
    identity={'id':reviewer,'mode':mode,'context':'fresh'}
    if p['startedAt'] and p['reviewer']!=identity: raise ValueError('Preserve the started model-reader identity')
    receipts=starts(study)
    if p['startedAt']:
        if not receipts or receipts[-1]['id']!=p['id'] or receipts[-1]['reviewer']!=identity: raise ValueError('Started model review has no matching receipt')
        return path
    if len(receipts)>=2 or p['attempt']!=len(receipts)+1: raise ValueError('Model review budget exhausted or attempt history conflicts')
    p.update(reviewer=identity,startedAt=p['startedAt'] or datetime.now(timezone.utc).isoformat())
    directory=local(study,'evidence/model-review-starts'); directory.mkdir(exist_ok=True)
    with (directory/f'attempt-{p["attempt"]:02d}.json').open('x',encoding='utf-8') as out:
        json.dump({'attempt':p['attempt'],'id':p['id'],'reviewer':identity,'startedAt':p['startedAt']},out,indent=2)
    path.write_text(json.dumps(p,indent=2)+'\n',encoding='utf-8'); return path

def verify(study,record=None):
    from publication_review import local,digest,validate_handoff
    from research_rules import require_current
    p=json.loads(local(study,PATH).read_text()); h=p['handoff']
    lock=require_current(study)
    for field in ('spec','workbook'):
        if p.get(field) not in p.get('inputs',{}):
            raise ValueError('Model review must freeze its declared spec and workbook')
        if record and local(study,p[field])!=local(study,record[field]):
            raise ValueError('Model review must cover the published spec and workbook')
    if record and (record['security'] not in h['scopeIds'] or h['asOf'][:10]!=record['cutoff'][:10]): raise ValueError('Model review cutoff/security must match this material research checkpoint')
    if p['rulesFingerprint']!=lock['productionFingerprint']: raise ValueError('Model review uses another rule version')
    if not p.get('startedAt') or p['reviewer']['id']=='unassigned' or p['reviewer']['context']!='fresh' or p['reviewer']['mode'] not in ('human','independent-agent'): raise ValueError('A named fresh model reader must actually start')
    receipts=starts(study)
    if not receipts or receipts[-1]['id']!=p['id'] or receipts[-1]['reviewer']!=p['reviewer'] or receipts[-1]['attempt']!=p['attempt']: raise ValueError('Model review does not match its latest started receipt')
    validate_handoff(h,p.get('evaluation'))
    checks={c['name']:c for c in h['checks']}
    prior=p.get('priorFindings',[]); resolved=p.get('resolutions',[]); sources={s['id'] for s in h['sources']}
    if {x['id'] for x in resolved}!={x['id'] for x in prior} or len(resolved)!=len(prior) or any(not x.get('reason','').strip() or not x.get('sourceIds') or not set(x['sourceIds'])<=sources for x in resolved):
        raise ValueError('Prior model findings need evidence-backed resolutions; do not erase failed work')
    if p.get('priorReviewSHA256'):
        previous=local(study,'evidence/model-reviews/'+p['priorReviewSHA256']+'.json')
        if digest(previous)!=p['priorReviewSHA256']: raise ValueError('Prior model review changed')
        old=json.loads(previous.read_text())
        expected=requirements(old)
        if prior!=expected: raise ValueError('Prior model finding inventory changed')
    if h['status']!='complete' or h['criticalUnknowns'] or any(d['changed'] for d in h['dependencies']) or not any(c['material'] for c in h['claims']) or any(checks.get(k,{}).get('result')!='pass' for k in CHECKS) or any(c['blocking'] and c['result']!='pass' for c in h['checks']): raise ValueError('Pre-writing model challenge is incomplete or has material unresolved findings')
    if any(digest(local(study,r))!=v for r,v in p['inputs'].items()): raise ValueError('Model/evidence changed after pre-writing review; recheck affected conclusions')
    return 'Named pre-writing model challenge complete on current model/evidence bytes; source truth and identity still require trust'

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('action',choices=('prepare','begin','check')); p.add_argument('study',type=Path)
    for name in ('spec','workbook','security','cutoff','reviewer'): p.add_argument('--'+name)
    p.add_argument('--evidence',nargs='*',default=[]); p.add_argument('--mode',default='independent-agent',choices=('independent-agent','human')); a=p.parse_args()
    if a.action=='prepare':
        if not all((a.spec,a.workbook,a.security,a.cutoff)): p.error('prepare requires spec, workbook, security and cutoff')
        print(prepare(a.study,a.spec,a.workbook,a.evidence,a.security,a.cutoff))
    elif a.action=='begin': print(begin(a.study,a.reviewer or '',a.mode))
    else: print(verify(a.study))

if __name__=='__main__': main()
