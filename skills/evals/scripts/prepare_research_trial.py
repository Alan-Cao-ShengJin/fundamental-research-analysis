"""Create a fresh minimal-prompt real-evidence trial; never overwrite a run.

The host curates an evidence-only snapshot first. Hashes preserve its bytes, not
source truth or provenance. This is context separation, not an OS sandbox.
No synthetic clock, old issuer work, credentials, tests or answer notes are copied.
"""
import argparse
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import stat


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def no_links(root):
    for p in [root,*root.rglob('*')]:
        info=p.lstat()
        if p.is_symlink() or getattr(info,'st_file_attributes',0)&getattr(stat,'FILE_ATTRIBUTE_REPARSE_POINT',0x400):
            raise ValueError('Linked/reparse paths are not accepted: '+str(p))


def prepare(repo, evidence, destination, audit, request, cutoff, security):
    repo,evidence,destination,audit=map(lambda p:Path(p).resolve(),(repo,evidence,destination,audit))
    date.fromisoformat(cutoff)
    if not request.strip() or not security.strip(): raise ValueError('Request and security are required')
    if destination.exists(): raise FileExistsError('Never overwrite a trial: '+str(destination))
    if destination.is_relative_to(repo) or repo.is_relative_to(destination):
        raise ValueError('Keep the author outside the repository containing prior work and answers')
    if (audit.is_relative_to(destination) or destination.is_relative_to(audit) or
            evidence.is_relative_to(destination) or destination.is_relative_to(evidence)):
        raise ValueError('Audit and evidence source must remain outside the author workspace')
    if (audit/'prepared-manifest.json').exists(): raise FileExistsError('Preserve the previous audit manifest')
    if not evidence.is_dir() or not any(evidence.rglob('*')): raise ValueError('Supply a curated evidence snapshot')
    if not (repo/'CLAUDE.md').is_file() or not (repo/'skills').is_dir(): raise ValueError('Missing bundle entrypoint')
    no_links(evidence); no_links(repo/'skills')
    source={p.relative_to(evidence).as_posix():sha(p) for p in sorted(evidence.rglob('*')) if p.is_file()}
    forbidden={'research','answers','tests','.git','.claude','.codex','node_modules'}
    for p in evidence.rglob('*'):
        if any(part in forbidden or part.startswith('.env') for part in p.relative_to(evidence).parts):
            raise ValueError('Evidence snapshot contains forbidden context: '+str(p))
    destination.mkdir(parents=True,exist_ok=False)
    shutil.copyfile(repo/'CLAUDE.md',destination/'CLAUDE.md')
    if (repo/'AGENTS.md').is_file(): shutil.copyfile(repo/'AGENTS.md',destination/'AGENTS.md')
    shutil.copytree(repo/'skills',destination/'skills',ignore=shutil.ignore_patterns('evals','tests','__pycache__','*.pyc','node_modules'))
    inbox=destination/'inbox/evidence-snapshot'
    shutil.copytree(evidence,inbox)
    for name in ('LICENSE','NOTICE','THIRD_PARTY_NOTICES.md'):
        if (repo/name).is_file(): shutil.copyfile(repo/name,destination/name)
    zod=repo/'node_modules/zod'
    if zod.is_dir():
        no_links(zod)
        shutil.copytree(zod,destination/'node_modules/zod')
    package={'name':'real-evidence-research-trial','private':True,'type':'module',
             'dependencies':{'zod':json.loads((zod/'package.json').read_text())['version']} if zod.is_dir() else {}}
    (destination/'package.json').write_text(json.dumps(package,indent=2)+'\n',encoding='utf-8')
    (destination/'.claude').mkdir()
    (destination/'.claude/settings.json').write_text('{"autoMemoryEnabled": false}\n',encoding='utf-8')
    (destination/'.mcp.json').write_text('{"mcpServers": {}}\n',encoding='utf-8')
    context={'security':security,'informationCutoff':cutoff,'evidenceDirectory':'inbox/evidence-snapshot',
        'boundary':'Use this fixed evidence snapshot for the controlled trial. Record unavailable evidence; do not read other runs or previous issuer studies. Keep actual production/retrieval timestamps. This is real evidence, not a synthetic clock.'}
    (destination/'inbox/RESEARCH_CONTEXT.json').write_text(json.dumps(context,indent=2)+'\n',encoding='utf-8')
    copied={p.relative_to(inbox).as_posix():sha(p) for p in sorted(inbox.rglob('*')) if p.is_file()}
    if copied!=source: raise ValueError('Evidence bytes changed during copying')
    manifest={'preparedAt':datetime.now(timezone.utc).isoformat(),'workspace':str(destination),'request':request,
        'informationCutoff':cutoff,'security':security,'maxReviewRounds':2,'status':'prepared-unrun',
        'separation':'Fresh context, not an OS sandbox. Global tools/plugins are not disabled by these local settings.',
        'evidenceFiles':source,'files':{p.relative_to(destination).as_posix():sha(p) for p in sorted(destination.rglob('*')) if p.is_file()}}
    audit.mkdir(parents=True,exist_ok=True)
    (audit/'prepared-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    (audit/'author-request.txt').write_text(request+'\n',encoding='utf-8')
    return {'workspace':str(destination),'audit':str(audit),'filesFrozen':len(manifest['files']),'evidenceFiles':len(source),'status':'prepared-unrun'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('evidence','destination','audit','request','cutoff','security'): parser.add_argument('--'+key,required=True)
    args=parser.parse_args()
    print(json.dumps(prepare(Path(__file__).resolve().parents[3],args.evidence,args.destination,args.audit,args.request,args.cutoff,args.security),indent=2))
