"""Local review-attempt receipts, separate from immutable draft versions.

This detects ordinary resets/overwrites; it cannot authenticate a person or resist rewriting all local evidence.
"""
import json
from pathlib import Path


def state(study):
    from publication_review import local, digest, check_snapshot
    root = local(study, 'evidence/review-snapshots')
    drafts = []
    for path in root.glob('*/prepared-review.json'):
        packet = json.loads(path.read_text(encoding='utf-8'))
        if packet.get('schemaVersion') != '1.1':
            raise ValueError('Legacy review history needs explicit migration; keep its original outcome and budget')
        drafts.append(packet)
    budgets = {p['maxRounds'] for p in drafts}
    paths = {p['reviewPath'] for p in drafts}
    versions = [p['draftVersion'] for p in drafts]
    if len(budgets) > 1 or len(paths) > 1 or len(versions) != len(set(versions)):
        raise ValueError('Draft history has conflicting budgets or duplicate versions')
    receipts = []
    for path in root.glob('*/review-start.json'):
        receipt = json.loads(path.read_text(encoding='utf-8'))
        prepared = path.with_name('prepared-review.json')
        if digest(prepared) != receipt['preparedSHA256']:
            raise ValueError('Prepared review changed after its attempt started')
        packet = json.loads(prepared.read_text(encoding='utf-8'))
        check_snapshot(study, packet)
        if (receipt['snapshot'] != packet['snapshot'] or receipt['draftVersion'] != packet['draftVersion']
                or receipt['maxRounds'] != packet['maxRounds'] or receipt['attempt'] != packet['round']):
            raise ValueError('Review-start receipt conflicts with its frozen draft')
        receipts.append(receipt)
    attempts = sorted(r['attempt'] for r in receipts)
    if attempts != list(range(1, len(attempts) + 1)):
        raise ValueError('Review attempt history is duplicated or incomplete')
    return {'used': len(receipts), 'maxRounds': next(iter(budgets), None),
            'reviewPath': next(iter(paths), None),
            'draftVersion': max(versions, default=0), 'receipts': receipts}


def begin(study, record, reviewer=None, mode='independent-agent'):
    from datetime import datetime, timezone
    from publication_review import local, digest, check_snapshot, DEFAULT_PATH
    path = local(study, record.get('review', DEFAULT_PATH))
    packet = json.loads(path.read_text(encoding='utf-8'))
    if packet.get('schemaVersion') != '1.1':
        raise ValueError('Prepare a current review packet before starting an attempt')
    check_snapshot(study, packet)
    prepared = json.loads((local(study, packet['snapshot']['path']) / 'prepared-review.json').read_text(encoding='utf-8'))
    fixed_context(packet, prepared)
    identity = {'id': reviewer or packet['reviewer']['id'], 'mode': mode, 'context': 'fresh'}
    if identity['id'] in (None, '', 'unassigned') or mode not in ('human', 'independent-agent'):
        raise ValueError('Starting review needs a named fresh reader')
    usage = state(study)
    receipt_path = local(study, packet['snapshot']['path']) / 'review-start.json'
    if receipt_path.exists():
        receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
        if receipt['reviewer'] != identity:
            raise ValueError('This draft already has a started review; do not replace the reader identity')
        return receipt_path
    if usage['used'] >= packet['maxRounds']:
        raise ValueError('Review budget exhausted; retain the unresolved draft')
    if packet['round'] != usage['used'] + 1:
        raise ValueError('Review attempt number does not follow preserved history')
    receipt = {'attempt': packet['round'], 'draftVersion': packet['draftVersion'], 'maxRounds': packet['maxRounds'],
               'reviewer': identity, 'startedAt': datetime.now(timezone.utc).isoformat(),
               'snapshot': packet['snapshot'], 'preparedSHA256': digest(receipt_path.with_name('prepared-review.json'))}
    with receipt_path.open('x', encoding='utf-8') as out:
        out.write(json.dumps(receipt, indent=2) + '\n')
    packet['reviewer'] = identity
    path.write_text(json.dumps(packet, indent=2) + '\n', encoding='utf-8')
    return receipt_path


def verify(study, packet):
    from publication_review import local
    usage = state(study)
    path = local(study, packet['snapshot']['path']) / 'review-start.json'
    receipt = json.loads(path.read_text(encoding='utf-8'))
    prepared = json.loads(path.with_name('prepared-review.json').read_text(encoding='utf-8'))
    fixed_context(packet, prepared)
    if (receipt['reviewer'] != packet['reviewer'] or receipt['attempt'] != packet['round']
            or receipt['draftVersion'] != packet['draftVersion'] or receipt['maxRounds'] != packet['maxRounds']
            or receipt['attempt'] != usage['used'] or not 1 <= usage['used'] <= packet['maxRounds']):
        raise ValueError('Current review does not match the latest preserved attempt and budget')
    return f'{usage["used"]} started review attempts; draft version {packet["draftVersion"]}'


def fixed_context(packet, prepared):
    fixed = ('schemaVersion', 'researchMode', 'reviewPath', 'draftVersion', 'round', 'maxRounds', 'snapshot',
             'reviewedFiles', 'skillsFingerprint', 'evaluation', 'priorReview', 'priorRequirements')
    if any(packet.get(key) != prepared.get(key) for key in fixed):
        raise ValueError('Fixed review context changed after preparation')


def prior_requirements(study, prior):
    from publication_review import local, digest
    requirements, seen = [], set()
    while prior:
        path = local(study, prior['path'])
        if path in seen or digest(path) != prior['sha256']:
            raise ValueError('Prior review findings changed or history is cyclic')
        seen.add(path)
        previous = json.loads(path.read_text(encoding='utf-8'))
        prefix = f'draft-{previous["draftVersion"]}/'
        requirements += [{'id': prefix+c['name'], 'finding': c['detail'], 'reviewPath': prior['path']}
            for c in previous['handoff']['checks'] if c['blocking'] and c['result'] == 'fail']
        requirements += [{'id': prefix+f'unknown-{i}', 'finding': text, 'reviewPath': prior['path']}
            for i, text in enumerate(previous['handoff']['criticalUnknowns'])]
        prior = previous.get('priorReview')
    return requirements


def prior_dispositions(study, packet):
    dispositions = packet.get('priorDispositions', [])
    requirements = prior_requirements(study, packet.get('priorReview'))
    if packet.get('priorRequirements', []) != requirements:
        raise ValueError('Prior blocking-finding inventory changed')
    needed = {r['id'] for r in requirements}
    sources = {s['id'] for s in packet['handoff']['sources']}
    return (len(dispositions) == len(needed) and {d.get('id') for d in dispositions} == needed
            and all(d.get('status') in ('resolved', 'disagreed') and str(d.get('reason', '')).strip()
                    and d.get('sourceIds') and set(d['sourceIds']) <= sources for d in dispositions))
