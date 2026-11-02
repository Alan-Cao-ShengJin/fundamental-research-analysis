"""Generate and check explicit research coverage. No research or automatic readiness judgment."""
import argparse
import json
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]
SPEC = Path(__file__).resolve().parents[1] / 'assets/skill-coverage.json'
DISPOSITIONS = {'pending', 'deferred', 'completed', 'reused', 'not-applicable'}


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def configuration(root=SKILLS_ROOT):
    catalog = read(root / 'catalog.json')
    spec = read(root / 'research-cycle/assets/skill-coverage.json')
    ids = {s['id'] for s in catalog['skills']}
    if set(spec['skills']) != ids:
        raise ValueError('Coverage specification must account for every catalog skill exactly.')
    for mode, flow in spec['modes'].items():
        if flow not in catalog['flows']:
            raise ValueError(f'Unknown flow for {mode}')
        for rule in spec['skills'].values():
            if rule['modes'].get(mode) not in {'required', 'conditional', 'outside-scope'}:
                raise ValueError(f'Missing requirement for {mode}')
    return catalog, spec


def make_plan(mode, root=SKILLS_ROOT):
    catalog, spec = configuration(root)
    if mode not in spec['modes']:
        raise ValueError(f'Unknown research mode: {mode}')
    flow = spec['modes'][mode]
    skills = []
    for sid, rule in spec['skills'].items():
        requirement = rule['modes'][mode]
        skills.append({'id': sid, 'requirement': requirement, 'purpose': rule['purpose'],
                       'trigger': rule.get('trigger'),
                       'disposition': 'not-applicable' if requirement == 'outside-scope' else 'pending',
                       'reason': rule['purpose'] if requirement == 'outside-scope' else None,
                       'references': []})
    return {'planVersion': '1.0.0', 'catalogVersion': catalog['version'], 'mode': mode,
            'security': None, 'informationCutoff': None, 'flow': flow,
            'stages': [{'id': stage, 'skill': catalog['stages'][stage]['skill'],
                        'disposition': 'pending', 'reason': None, 'references': []}
                       for stage in catalog['flows'][flow]],
            'skills': skills,
            'targetedForecastRevision': {'needed': False, 'riskReview': None,
                                        'calculationRun': None, 'audit': None, 'refreshedOutputs': []}}


def check_plan(plan, root=SKILLS_ROOT):
    catalog, spec = configuration(root)
    issues = []
    if not isinstance(plan, dict):
        return {'complete': False, 'issues': ['Plan must be an object.']}
    mode = plan.get('mode')
    if mode not in spec['modes']:
        return {'complete': False, 'issues': ['Unknown research mode.']}
    expected = make_plan(mode, root)
    for field in ('planVersion', 'catalogVersion', 'flow'):
        if plan.get(field) != expected[field]:
            issues.append(f'Mismatch: {field}; reconcile the plan with current methods.')
    for field in ('security', 'informationCutoff'):
        if not isinstance(plan.get(field), str) or not plan[field].strip():
            issues.append(f'Missing {field}.')
    for group in ('stages', 'skills'):
        entries = plan.get(group)
        if not isinstance(entries, list) or any(not isinstance(e, dict) for e in entries):
            issues.append(f'{group} must be a list of records.')
            continue
        wanted = {e['id']: e for e in expected[group]}
        actual = [e.get('id') for e in entries]
        if len(actual) != len(set(str(s) for s in actual)) or set(str(s) for s in actual) != set(wanted):
            issues.append(f'{group}: missing, unknown or duplicate IDs.')
        if group == 'stages' and actual != [e['id'] for e in expected[group]]:
            issues.append('Stages must retain dependency order.')
        for entry in entries:
            sid = entry.get('id')
            if not isinstance(sid, str) or sid not in wanted:
                continue
            rule = wanted[sid]
            requirement = rule.get('requirement', 'required')
            if group == 'skills' and entry.get('requirement') != requirement:
                issues.append(f'{sid}: requirement was changed.')
            if group == 'stages' and entry.get('skill') != rule['skill']:
                issues.append(f'{sid}: stage owner was changed.')
            disposition = entry.get('disposition')
            if not isinstance(disposition, str) or disposition not in DISPOSITIONS or disposition in {'pending', 'deferred'}:
                issues.append(f'{group}/{sid}: work or applicability decision remains incomplete.')
            if not isinstance(disposition, str):
                disposition = 'invalid'
            if disposition == 'not-applicable' and requirement == 'required':
                issues.append(f'{group}/{sid}: required work cannot be skipped.')
            if requirement == 'outside-scope' and disposition != 'not-applicable':
                issues.append(f'{sid}: use a separate route for the requested extension.')
            if not isinstance(entry.get('reason'), str) or not entry['reason'].strip():
                issues.append(f'{group}/{sid}: missing reason.')
            refs = entry.get('references')
            if disposition in {'completed', 'reused'} and (not isinstance(refs, list) or not refs
                    or any(not isinstance(r, str) or not r.strip() for r in refs)):
                issues.append(f'{group}/{sid}: completed/reused work needs artifact references.')
    revision = plan.get('targetedForecastRevision')
    if not isinstance(revision, dict) or type(revision.get('needed')) is not bool:
        issues.append('Declare whether a targeted forecast revision was needed.')
    elif revision['needed']:
        for field in ('riskReview', 'calculationRun', 'audit'):
            if not isinstance(revision.get(field), str) or not revision[field].strip():
                issues.append(f'Targeted forecast revision needs {field}.')
        if not isinstance(revision.get('refreshedOutputs'), list) or not revision['refreshedOutputs']:
            issues.append('Targeted forecast revision needs refreshed dependent outputs.')
    return {'complete': not issues, 'issues': issues,
            'limit': 'Coverage accounting only; no verification of sources, artifact validity or economic judgment.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=['initiation', 'regular', 'major'])
    parser.add_argument('--out', type=Path)
    parser.add_argument('--validate', type=Path)
    args = parser.parse_args()
    if args.validate:
        if args.mode or args.out:
            parser.error('--validate cannot be combined with plan creation.')
        result = check_plan(read(args.validate))
        print(json.dumps(result, indent=2))
        return 0 if result['complete'] else 1
    if not args.mode or not args.out:
        parser.error('Creation requires --mode and --out.')
    plan = make_plan(args.mode)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x', encoding='utf-8') as handle:
        json.dump(plan, handle, indent=2)
        handle.write('\n')
    print(f'Created incomplete {args.mode} plan: {args.out}')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as exc:
        raise SystemExit(str(exc))
