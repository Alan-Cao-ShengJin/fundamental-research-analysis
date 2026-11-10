"""Retain connector-output bytes or an explicitly labeled manual compilation.

A hash records integrity, not provider authentication. No provider request is made.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

def retain(study,source,destination,provider,origin,locator):
    study=Path(study).resolve(); source=Path(source).resolve(); output=(study/destination).resolve()
    if origin not in ('connector-output-file','manual-compilation'): raise ValueError('Declare the actual origin')
    if not output.is_relative_to(study) or output==source: raise ValueError('Choose a new study-relative retained evidence file')
    receipt=output.with_suffix(output.suffix+'.receipt.json')
    if output.exists() or receipt.exists(): raise FileExistsError('Preserve previous evidence; choose a versioned destination')
    if not provider.strip() or not locator.strip(): raise ValueError('Record provider and source/tool locator')
    data=source.read_bytes(); output.parent.mkdir(parents=True,exist_ok=True); output.write_bytes(data)
    record={'provider':provider,'origin':origin,'locator':locator,'retainedAt':datetime.now(timezone.utc).isoformat(),
            'file':output.relative_to(study).as_posix(),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'authenticityVerified':False,
            'limit':'Integrity receipt only. Connector-output files are not independently authenticated; manual compilations are not raw provider responses.'}
    receipt.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8'); return record

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('study'); p.add_argument('source'); p.add_argument('destination')
    p.add_argument('--provider',required=True); p.add_argument('--origin',required=True,choices=('connector-output-file','manual-compilation')); p.add_argument('--locator',required=True); a=p.parse_args()
    print(json.dumps(retain(a.study,a.source,a.destination,a.provider,a.origin,a.locator),indent=2))
