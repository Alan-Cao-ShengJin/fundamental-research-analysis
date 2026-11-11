"""Pin actual production rules and run them in an isolated import root, without resetting reviews."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tarfile
import tempfile

SKILLS=Path(__file__).resolve().parents[2]
LOCK='evidence/rules-lock.json'

def production_files(root=None):
    root=Path(root or SKILLS)
    return [p for p in sorted(root.rglob('*')) if p.is_file() and not any(x in ('tests','evals','__pycache__','node_modules') for x in p.relative_to(root).parts) and p.suffix not in ('.pyc','.pyo')]

def fingerprint(root=None):
    root=Path(root or SKILLS)
    h=hashlib.sha256()
    for p in production_files(root): h.update(p.relative_to(root).as_posix().encode()); h.update(p.read_bytes())
    return h.hexdigest()

def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def runtime():
    versions={}
    for name in ('openpyxl','et_xmlfile','python-dateutil','PyMuPDF','tzdata'):
        try: versions[name]=importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError: versions[name]=None
    zod=SKILLS.parent/'node_modules/zod/package.json'
    versions['zod']=json.loads(zod.read_text())['version'] if zod.is_file() else None
    node=os.environ.get('NODE_BINARY') or shutil.which('node')
    node_version=subprocess.check_output([node,'--version'],text=True).strip() if node else None
    return {'python':sys.version.split()[0],'node':node_version,'packages':versions}

def runtime_diff(pinned,now):
    """(pinned, current) for each differing entry; the nested packages dict is flattened to packages.NAME."""
    flat=lambda r:{**{k:v for k,v in r.items() if k!='packages'},**{'packages.'+k:v for k,v in (r.get('packages') or {}).items()}}
    pinned,now=flat(pinned),flat(now)
    return {k:(pinned.get(k),now.get(k)) for k in sorted(set(pinned)|set(now)) if pinned.get(k)!=now.get(k)}

def load(study):
    study=Path(study).resolve(); value=json.loads((study/LOCK).read_text(encoding='utf-8'))
    archive=(study/value['archive']).resolve()
    if not archive.is_relative_to(study) or digest(archive)!=value['archiveSHA256']: raise ValueError('Pinned rule archive changed or escapes the study')
    return value

def pin(study):
    study=Path(study).resolve(); path=study/LOCK
    if path.exists(): return load(study)
    if (study/'evidence/review-snapshots').exists(): raise ValueError('Existing review history: use the archived-rule runner; do not silently pin current rules')
    root=study/'evidence/rules-lock'; root.mkdir(parents=True,exist_ok=True); archive=root/'rules.tar'
    with tarfile.open(archive,'w') as output:
        for p in production_files(): output.add(p,arcname=p.relative_to(SKILLS).as_posix(),recursive=False)
    value={'schemaVersion':'1.0','pinnedAt':datetime.now(timezone.utc).isoformat(),'productionFingerprint':fingerprint(),
           'archive':archive.relative_to(study).as_posix(),'archiveSHA256':digest(archive),'runtime':runtime(),
           'scope':'Production instructions, helpers, templates and assets; tests/evals excluded. No source-truth assurance.'}
    path.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8'); return value

def require_current(study):
    if not (Path(study)/LOCK).is_file(): raise ValueError('Pin the study rules before model construction: research_rules.py pin STUDY')
    value=load(study)
    if value['productionFingerprint']!=fingerprint(): raise ValueError('Different pinned rules: use research_rules.py run rather than mixing live rules')
    if value['runtime']!=runtime(): raise ValueError(f'Runtime differs from the pinned dependency receipt: {runtime_diff(value["runtime"],runtime())}; use that environment or explicitly migrate')
    return value

def archived(study):
    study=Path(study).resolve()
    if (study/LOCK).is_file():
        value=load(study); return study/value['archive'],value
    candidates=[]
    for p in (study/'evidence/review-snapshots').glob('*/manifest.json'):
        value=json.loads(p.read_text(encoding='utf-8')); archive=p.parent/'rules.tar'
        if archive.is_file() and digest(archive)==value.get('rulesSHA256'): candidates.append((value['createdAt'],archive,value))
    if not candidates: raise ValueError('No preserved rules exist; do not invent a historical version')
    _,archive,manifest=min(candidates,key=lambda x:x[0])
    return archive,{'legacyArchive':True,'archiveSHA256':digest(archive),'originalRuntimeUnrecorded':True,'productionFingerprint':manifest['skillsFingerprint']}

def run(study,entry,args=()):
    study=Path(study).resolve(); archive,receipt=archived(study)
    if not receipt.get('legacyArchive') and receipt['runtime']!=runtime(): raise ValueError(f'Runtime differs from the pinned dependency receipt: {runtime_diff(receipt["runtime"],runtime())}')
    print(json.dumps({'rulesExecution':{'archiveSHA256':receipt['archiveSHA256'],
          'standard':'preserved-historical-rules' if receipt.get('legacyArchive') else 'study-pinned-production-rules',
          'originalRuntimeRecorded':not receipt.get('originalRuntimeUnrecorded',False)}}),file=sys.stderr)
    with tempfile.TemporaryDirectory(prefix='research-rules-') as scratch:
        root=Path(scratch); skills=root/'skills'; skills.mkdir()
        with tarfile.open(archive) as source:
            for member in source.getmembers():
                name=PurePosixPath(member.name)
                if not member.isfile() or name.is_absolute() or '..' in name.parts or '\\' in member.name: raise ValueError('Archive must contain ordinary relative files')
                dest=skills.joinpath(*name.parts); dest.parent.mkdir(parents=True,exist_ok=True)
                with source.extractfile(member) as src,dest.open('wb') as out: shutil.copyfileobj(src,out)
        zod=SKILLS.parent/'node_modules/zod'
        if zod.is_dir(): shutil.copytree(zod,root/'node_modules/zod')
        (root/'package.json').write_text('{"type":"module"}\n')
        matches=[p for p in skills.rglob(entry) if p.is_file()] if '/' not in entry and '\\' not in entry else []
        script=matches[0] if len(matches)==1 else (study/entry).resolve()
        if len(matches)!=1 and (not script.is_relative_to(study) or not script.is_file()): raise ValueError('Select one archived helper or study-relative builder')
        bootstrap=root/'run_pinned.py'
        bootstrap.write_text('''import importlib.abc, importlib.machinery, pathlib, runpy, sys
root=pathlib.Path(sys.argv[1]); script=sys.argv[2]; args=sys.argv[3:]
paths=sorted({str(p.parent) for p in root.rglob("*.py")})
class Pinned(importlib.abc.MetaPathFinder):
    def find_spec(self,fullname,path=None,target=None):
        if "." not in fullname: return importlib.machinery.PathFinder.find_spec(fullname,paths)
sys.meta_path.insert(0,Pinned()); sys.path[:0]=[str(pathlib.Path(script).parent)]+paths; sys.argv=[script]+args
runpy.run_path(script,run_name="__main__")
''',encoding='utf-8')
        env=dict(os.environ,RESEARCH_PINNED_RUN='1',RESEARCH_SKILLS_ROOT=str(skills))
        return subprocess.run([sys.executable,'-B','-X','utf8',str(bootstrap),str(skills),str(script),*map(str,args)],cwd=study,env=env).returncode

def dispatch(study,entry,args):
    """Return None for current rules; otherwise execute the actual preserved version."""
    if os.environ.get('RESEARCH_PINNED_RUN'): return None
    try: _,value=archived(study)
    except ValueError: return None
    if value.get('legacyArchive') or value['productionFingerprint']!=fingerprint(): return run(study,entry,args)
    return None

def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('action',choices=('pin','run')); parser.add_argument('study',type=Path)
    parser.add_argument('entry',nargs='?'); parser.add_argument('args',nargs=argparse.REMAINDER); a=parser.parse_args()
    if a.action=='pin': print(json.dumps(pin(a.study),indent=2)); return 0
    if not a.entry: raise ValueError('Select an archived helper or builder')
    return run(a.study,a.entry,a.args)

if __name__=='__main__': raise SystemExit(main())
