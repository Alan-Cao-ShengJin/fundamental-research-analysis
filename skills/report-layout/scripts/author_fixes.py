"""Author fixes after the single fresh review: no second read.

The reader reviews once. For each failed blocking check the author records either `fixed` (what changed) or
`minor` (why it does not move the target, rating or a decisive claim), reprints, and finalizes the fixed files.
Nonblocking (minor) findings need no entry. This records the author's own work; it is not a review.
"""
from datetime import datetime, timezone
import json

PATH = 'evidence/author-fixes.json'


def _failed(packet):
    return sorted(c['name'] for c in packet['handoff']['checks'] if c['blocking'] and c['result'] != 'pass')


def _changed(study, packet):
    from publication_review import local, digest
    return {rel: digest(local(study, rel)) for rel, value in packet['reviewedFiles'].items()
            if local(study, rel).is_file() and digest(local(study, rel)) != value}


def require_completed_review(study, record):
    """Read-only eligibility check, also used before printing or replacing artifacts."""
    from publication_review import local, check_snapshot, DEFAULT_PATH
    from review_attempts import verify as verify_attempt
    review = local(study, record.get('review', DEFAULT_PATH))
    p = json.loads(review.read_text(encoding='utf-8-sig'))
    if p['handoff']['status'] != 'complete' or p['handoff']['criticalUnknowns']:
        raise ValueError('Author fixes follow a completed review without critical unknowns')
    check_snapshot(study, p); verify_attempt(study, p)
    return review, p


def prepare(study, record):
    """After the reprint, write the receipt the author completes. Repeating it refreshes the changed-file list."""
    from publication_review import local, digest
    review, p = require_completed_review(study, record)
    path = local(study, PATH)
    notes = {}
    if path.exists():
        old = json.loads(path.read_text(encoding='utf-8-sig'))
        if old.get('reviewSHA256') == digest(review):
            notes = {f['check']: f for f in old.get('findings', [])}
    findings = [notes.get(name, {'check': name, 'status': '', 'note': ''}) for name in _failed(p)]
    receipt = {'schemaVersion': '1.0', 'reviewSHA256': digest(review), 'reviewer': p['reviewer'],
               'draftVersion': p['draftVersion'], 'preparedAt': datetime.now(timezone.utc).isoformat(),
               'changedFiles': _changed(study, p), 'findings': findings,
               'task': 'For each failed blocking check set status "fixed" with what changed, or "minor" with why it does '
                       'not move the target, rating or a decisive claim. No second read follows.'}
    path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return path


def verify(study, record, packet):
    from publication_review import local, digest, DEFAULT_PATH
    receipt = json.loads(local(study, PATH).read_text(encoding='utf-8-sig'))
    if receipt['reviewSHA256'] != digest(local(study, record.get('review', DEFAULT_PATH))) or receipt['reviewer'] != packet['reviewer']:
        raise ValueError('Author fixes do not match the completed review')
    if packet['handoff']['status'] != 'complete' or packet['handoff']['criticalUnknowns']:
        raise ValueError('Author fixes follow a completed review without critical unknowns')
    entries = {f.get('check'): f for f in receipt['findings']}
    if set(entries) != set(_failed(packet)):
        raise ValueError('Record one entry for each failed blocking check')
    if any(f.get('status') not in ('fixed', 'minor') or not str(f.get('note', '')).strip() for f in entries.values()):
        raise ValueError('Each failed check needs status fixed or minor with a note')
    if _changed(study, packet) != receipt['changedFiles']:
        raise ValueError('Files changed after the author-fix receipt; rerun the fix print')
    return receipt
