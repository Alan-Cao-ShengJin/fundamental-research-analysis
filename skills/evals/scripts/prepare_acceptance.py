"""Prepare a new minimal-prompt fixture workspace without answer notes or prior research.

Creates a new directory only; never cleans or overwrites an existing run. The host launches the fresh session.
The audit manifest stays outside the author's workspace. This is context separation, not an OS security boundary.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(repo, pack, destination, audit, request, evaluation_time):
    repo, destination, audit = Path(repo).resolve(), Path(destination).resolve(), Path(audit).resolve()
    fixture = repo / 'skills/evals/fixtures' / pack / 'pack.md'
    if not fixture.is_file() or not fixture.resolve().is_relative_to((repo / 'skills/evals/fixtures').resolve()):
        raise ValueError('Select an existing raw evidence pack, not an answer note')
    if destination.exists():
        raise FileExistsError('Never overwrite an acceptance workspace: ' + str(destination))
    if destination.is_relative_to(repo):
        raise ValueError('Keep the author workspace outside the repository containing answers and critiques')
    if audit.is_relative_to(destination):
        raise ValueError('The author must not receive the grading/audit directory')
    clock = datetime.fromisoformat(evaluation_time.replace('Z', '+00:00'))
    if clock.tzinfo is None:
        raise ValueError('The fixture evaluation clock needs a timezone')
    destination.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(repo / 'CLAUDE.md', destination / 'CLAUDE.md')
    shutil.copytree(repo / 'skills', destination / 'skills',
                    ignore=shutil.ignore_patterns('evals', 'tests', '__pycache__', 'node_modules', '*.pyc'))
    inbox = destination / 'inbox' / pack
    shutil.copytree(fixture.parent, inbox, ignore=shutil.ignore_patterns('answers', '__pycache__', '*.pyc'))
    for name in ('LICENSE', 'NOTICE', 'THIRD_PARTY_NOTICES.md'):
        if (repo / name).is_file():
            shutil.copyfile(repo / name, destination / name)
    # The publication handoff validator needs zod. Reuse installed bytes; no network install or account data.
    zod = repo / 'node_modules/zod'
    if zod.is_dir():
        shutil.copytree(zod, destination / 'node_modules/zod')
    (destination / 'package.json').write_text(json.dumps({'name': 'research-acceptance', 'private': True,
        'type': 'module', 'dependencies': {'zod': json.loads((zod / 'package.json').read_text())['version']} if zod.is_dir() else {}},
        indent=2) + '\n', encoding='utf-8')
    evaluation = {'mode': 'synthetic-fixture', 'now': evaluation_time,
                  'reason': 'Host-declared clock for a fixed invented evidence pack; production timestamps remain actual.'}
    (destination / '.research-evaluation.json').write_text(json.dumps(evaluation, indent=2) + '\n', encoding='utf-8')
    config = destination / '.claude'
    config.mkdir()
    (config / 'settings.json').write_text('{"autoMemoryEnabled": false}\n', encoding='utf-8')
    (destination / '.mcp.json').write_text('{"mcpServers": {}}\n', encoding='utf-8')
    audit.mkdir(parents=True, exist_ok=True)
    manifest = {'preparedAt': datetime.now(timezone.utc).isoformat(), 'workspace': str(destination),
                'request': request, 'maxReviewRounds': 2, 'evaluation': evaluation,
                'separation': 'Fresh directory; answer notes, evaluations, tests, previous research and critiques excluded; not an OS sandbox.',
                'files': {p.relative_to(destination).as_posix(): sha(p) for p in sorted(destination.rglob('*'))
                          if p.is_file() and 'node_modules' not in p.parts}}
    (audit / 'prepared-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    (audit / 'author-request.txt').write_text(request + '\n', encoding='utf-8')
    return {'workspace': str(destination), 'audit': str(audit), 'filesFrozen': len(manifest['files']),
            'rawPackUnchanged': sha(fixture) == sha(inbox / 'pack.md')}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pack', required=True)
    parser.add_argument('--destination', required=True)
    parser.add_argument('--audit', required=True)
    parser.add_argument('--request', required=True)
    parser.add_argument('--evaluation-time', required=True)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[3]
    print(json.dumps(prepare(repo, args.pack, args.destination, args.audit, args.request, args.evaluation_time), indent=2))
