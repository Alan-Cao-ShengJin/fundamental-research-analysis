"""Copy a checked, explicitly selected study into a prepared update workspace without publishing its conclusion."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import shutil
import sys


def verify_model(study, record):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'company-model/scripts'))
    import model_workbook as mw
    spec_path, workbook = [(study / record[k]).resolve() for k in ('spec','workbook')]
    if not all(p.is_relative_to(study) for p in (spec_path,workbook)):
        raise ValueError('Baseline model paths must remain within the selected study')
    return mw.check(json.loads(spec_path.read_text(encoding='utf-8')),workbook)


def stage(study, destination, audit, evidence=None):
    study, destination, audit = [Path(p).resolve() for p in (study,destination,audit)]
    record = json.loads((study/'deliverables/release.json').read_text(encoding='utf-8'))
    clock = json.loads((destination/'.research-evaluation.json').read_text(encoding='utf-8'))
    if datetime.fromisoformat(record['cutoff'][:10]) > datetime.fromisoformat(clock['now'][:10]):
        raise ValueError('The update clock cannot predate its baseline')
    if audit.is_relative_to(destination):
        raise ValueError('Keep host grading/audit records outside the author workspace')
    target = destination/'research'/study.parent.name/study.name
    if target.is_relative_to(study):
        raise ValueError('The update destination cannot be nested inside its baseline')
    if target.exists():
        raise FileExistsError('A baseline is already staged; never overwrite an acceptance run')
    evidence_target = None
    if evidence is not None:
        evidence = Path(evidence).resolve()
        source_inbox = study.parents[2]/'inbox'
        if not evidence.is_dir() or not evidence.is_relative_to(source_inbox.resolve()):
            raise ValueError('Select raw baseline evidence from its author workspace inbox')
        if not all(p.resolve().is_relative_to(evidence) for p in evidence.rglob('*')):
            raise ValueError('Baseline evidence links must remain within the selected raw directory')
        evidence_target = destination/'inbox'/evidence.name
        if evidence_target.exists():
            raise FileExistsError('Refuse to overwrite update evidence')
    if not all(p.resolve().is_relative_to(study) for p in study.rglob('*')):
        raise ValueError('A baseline link resolves outside the selected study')
    check = verify_model(study,record)
    if not check['passed']:
        raise ValueError('Baseline model does not reproduce: '+json.dumps(check['issues'][:5]))
    review_path = (study/record.get('review','evidence/draft-review.json')).resolve()
    if not review_path.is_relative_to(study):
        raise ValueError('Baseline review must remain within the selected study')
    review = json.loads(review_path.read_text(encoding='utf-8')) if review_path.is_file() else None
    unresolved = [] if review is None else [c for c in review['handoff']['checks'] if c['result'] != 'pass']
    unknowns = [] if review is None else review['handoff']['criticalUnknowns']
    reusable = bool(record.get('status') == 'validated' and review and review['handoff']['status'] == 'complete'
                    and not unresolved and not unknowns)
    shutil.copytree(study,target,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    if evidence_target:
        shutil.copytree(evidence,evidence_target)
    relative = target.relative_to(destination).as_posix()
    components = {'study':relative,'baselineCutoff':record['cutoff'],'modelArithmetic':check,
                  'sourcePublicationStatus':record.get('status'),'conclusionReusable':reusable,
                  'baselineEvidence':evidence_target.relative_to(destination).as_posix() if evidence_target else None,
                  'unresolvedReviewChecks':unresolved,'criticalUnknowns':unknowns,
                  'note':'Checked model/evidence components are supplied. Preserve their vintages and open findings; an unreleased conclusion is not an accepted investment baseline.'}
    (target.parent/'BASELINE_COMPONENTS.json').write_text(json.dumps(components,indent=2)+'\n',encoding='utf-8')
    audit.mkdir(parents=True,exist_ok=True)
    hashes = {p.relative_to(destination).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(target.rglob('*')) if p.is_file()}
    if evidence_target:
        hashes.update({p.relative_to(destination).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in sorted(evidence_target.rglob('*')) if p.is_file()})
    (audit/'baseline-manifest.json').write_text(json.dumps({'components':components,'files':hashes},indent=2)+'\n',encoding='utf-8')
    return {'stagedStudy':str(target),'modelPassed':True,'conclusionReusable':reusable,'files':len(hashes)}


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--study',required=True); p.add_argument('--destination',required=True); p.add_argument('--audit',required=True)
    p.add_argument('--evidence',help='Optional raw baseline inbox directory needed by the executable backend')
    args=p.parse_args()
    print(json.dumps(stage(args.study,args.destination,args.audit,args.evidence),indent=2))
