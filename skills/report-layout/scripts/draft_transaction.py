"""Render and check in staging before replacing canonical draft PDFs."""
import copy
from pathlib import Path
import os
import shutil
import tempfile

def render(study,record,fix=False):
    import publication_review as pr
    import report_layout as rl
    import release_check as rc
    study=Path(study).resolve(); out=study/'deliverables'
    with tempfile.TemporaryDirectory(prefix='.draft-stage-',dir=out) as scratch:
        stage=Path(scratch); candidate=copy.deepcopy(record); replacements=[]
        for role,paths in record['renders'].items():
            html=paths['html'] if isinstance(paths,dict) else paths
            final=pr.local(study,paths['pdf'] if isinstance(paths,dict) else str(Path(html).with_suffix('.pdf')))
            temporary=stage/(role+'.pdf')
            produced=rl.print_pdf(pr.local(study,html),temporary)
            if produced is not None and Path(produced).resolve()!=temporary: raise ValueError('Printer did not produce the requested staged PDF')
            replacements.append((temporary,final))
            candidate['renders'][role]={'html':html,'pdf':temporary.relative_to(study).as_posix()}
        pdf_map={final.relative_to(study).as_posix():temporary.relative_to(study).as_posix() for temporary,final in replacements}
        candidate['deliverables']=[pdf_map.get(p,p) for p in record['deliverables']]
        candidate['briefPdf']=candidate['renders']['brief']['pdf']
        candidate.pop('fingerprints',None)
        checks,fails=rc.run(study,candidate,legacy=True)
        if fails: raise ValueError('Staged draft fails integrity checks with current bindings:\n  '+'\n  '.join(fails))
        # Ensure eligibility is still true before replacing any reviewed output. A fix print follows the single review.
        if not fix: pr.preflight(study,record,revise=pr.local(study,record.get('review',pr.DEFAULT_PATH)).exists())
        backups={}
        for _,final in replacements:
            if final.exists():
                with final.open('rb+') as handle: pass
                backup=stage/('backup-'+final.name); shutil.copyfile(final,backup); backups[final]=backup
        committed=[]
        try:
            for temporary,final in replacements: os.replace(temporary,final); committed.append(final)
        except Exception:
            for final in reversed(committed):
                if final in backups: os.replace(backups[final],final)
                else: final.unlink(missing_ok=True)
            raise
        return checks
