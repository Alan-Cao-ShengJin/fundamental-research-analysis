"""One bounded confirmation of presentation-only corrections by the original reader.

Retains the substantive review and attempt. It cannot clear changed numbers,
model/evidence/decision inputs, or analytical findings, even if the rating is unchanged.
"""
from datetime import datetime, timezone
import json
from pathlib import Path
import re

PATH='evidence/draft-confirmation.json'
EDITORIAL={'conciseness','professional-language','sharp-writing','visual-inspection'}

def meaning(path):
    path=Path(path)
    if path.suffix=='.json': return json.loads(path.read_text(encoding='utf-8-sig'))
    if path.suffix=='.pdf':
        import fitz
        parts=[]
        with fitz.open(path) as doc:
            for page in doc:
                parts.append(page.get_text(clip=fitz.Rect(0,18*72/25.4,page.rect.width,page.rect.height-18*72/25.4)))
        text=' '.join(parts)
    elif path.suffix in ('.html','.htm'):
        from brief_consistency import Visible
        p=Visible(); p.feed(path.read_text(encoding='utf-8')); text=' '.join(p.text)
    else: raise ValueError('Presentation confirmation cannot change this file type')
    return re.findall(r'\w+|[^\w\s]',text)

def changes(study,record,packet):
    from publication_review import local,digest
    allowed={record['brief']}
    for value in record['renders'].values(): allowed.update(value.values() if isinstance(value,dict) else [value])
    old=local(study,packet['snapshot']['path'])/'files'; changed={}
    for rel,value in packet['reviewedFiles'].items():
        current=local(study,rel)
        if digest(current)==value: continue
        if rel not in allowed or meaning(old/rel)!=meaning(current): raise ValueError('Correction changes analytical inputs or visible content; a substantive review is required: '+rel)
        changed[rel]=digest(current)
    if not changed: raise ValueError('No presentation correction to confirm')
    return changed

def prepare(study,record):
    from publication_review import local,digest,check_snapshot,DEFAULT_PATH
    from research_rules import require_current
    from review_attempts import verify as verify_attempt
    require_current(study); path=local(study,PATH)
    if path.exists(): raise ValueError('One confirmation per reviewed draft; preserve it rather than looping')
    original=local(study,record.get('review',DEFAULT_PATH)); p=json.loads(original.read_text(encoding='utf-8-sig'))
    check_snapshot(study,p); verify_attempt(study,p)
    failed={c['name'] for c in p['handoff']['checks'] if c['result']!='pass'}
    if p['handoff']['status']!='complete' or p['handoff']['criticalUnknowns'] or not failed or not failed<=EDITORIAL:
        raise ValueError('Only completed analytical reviews with presentation findings qualify')
    changed=changes(study,record,p)
    h=dict(p['handoff'],id='presentation-confirmation',status='partial',producedAt=datetime.now(timezone.utc).isoformat(),
           summary='Presentation corrections prepared for actual confirmation by the original reader.',claims=[],criticalUnknowns=[],
           checks=[{'name':name,'result':'not-run','blocking':True,'detail':'Inspect the corrected print and unchanged meaning.'} for name in sorted(failed)])
    result={'schemaVersion':'1.0','originalReviewSHA256':digest(original),'draftVersion':p['draftVersion'],'attempt':p['round'],
            'reviewer':p['reviewer'],'changedFiles':changed,'resolvedChecks':sorted(failed),'handoff':h,
            'task':'The original reader inspects exact corrected PDFs and the diff, confirms no analytical/visible-text change and records actual findings. This is one confirmation of an existing attempt, not a new independent review or permission for further revisions.'}
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8'); return path

def verify(study,record,packet):
    from publication_review import local,digest,validate_handoff,DEFAULT_PATH
    receipt=json.loads(local(study,PATH).read_text(encoding='utf-8-sig')); h=receipt['handoff']
    original=local(study,record.get('review',DEFAULT_PATH))
    if receipt['originalReviewSHA256']!=digest(original) or receipt['reviewer']!=packet['reviewer'] or receipt['draftVersion']!=packet['draftVersion'] or receipt['attempt']!=packet['round']:
        raise ValueError('Confirmation does not match the original review, reader and attempt')
    if changes(study,record,packet)!=receipt['changedFiles']: raise ValueError('Corrected files changed after confirmation preparation')
    expected={c['name'] for c in packet['handoff']['checks'] if c['result']!='pass'}
    if not expected or not expected<=EDITORIAL or set(receipt['resolvedChecks'])!=expected: raise ValueError('Confirmation cannot clear analytical findings')
    validate_handoff(h,packet.get('evaluation'))
    checked={c['name'] for c in h['checks'] if c['result']=='pass'}
    if h['status']!='complete' or h['criticalUnknowns'] or checked!=expected or any(c['blocking'] and c['result']!='pass' for c in h['checks']): raise ValueError('Actual presentation confirmation is incomplete')
    return receipt
