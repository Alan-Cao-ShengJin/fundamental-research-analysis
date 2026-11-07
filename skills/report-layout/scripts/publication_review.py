"""A frozen draft packet around the existing challenge handoff, plus material financial-claim checks.

This verifies completion, provenance and defined arithmetic, not the truth of evidence or a reviewer's independence.
The host starts a fresh writer/reviewer context; this module does not call an LLM or send anything externally.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import re

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parents[1]
CHECKS = ('conciseness', 'critical-thinking', 'professional-language', 'sharp-writing',
          'argument-support', 'defensible-view', 'source-and-financial-basis', 'visual-inspection')
FAMILIES = ('cash-coverage', 'normalized-ratio', 'financing')
DEFAULT_PATH = 'evidence/draft-review.json'


def writing_packet(study, paths):
    """Freeze an upstream checkpoint for a host-launched fresh writer. This records work to do, not completed work."""
    if not paths:
        raise ValueError('Provide the model/decision/evidence checkpoint paths with --inputs')
    packet = {'role': 'fresh-writer', 'status': 'prepared',
              'inputs': {rel: digest(local(study, rel)) for rel in paths},
              'read': ['research-brief/SKILL.md', 'research-brief/references/natural-writing.md', 'report-layout/SKILL.md'],
              'task': 'Start in a fresh context. Write from the frozen model and decision/evidence record, with access to '
                      'original pivotal sources. Apply the short writing standard; return discrepancies to analysis. '
                      'Do not change the forecast or target just to improve the prose. Render drafts, not a release.',
              'execution': 'The host launches the fresh context; this packet does not launch an agent.'}
    out = local(study, 'evidence/writing-packet.json')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(packet, indent=2) + '\n', encoding='utf-8')
    return out


class Figures(HTMLParser):
    def __init__(self):
        super().__init__(); self.figures = []; self.current = None; self.skip = 0; self.prose = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('style', 'script'):
            self.skip += 1
        if a.get('data-model-claim'):
            self.current = dict(a, text='')

    def handle_data(self, data):
        if not self.skip:
            if data.strip():
                self.prose.append(data.strip())
            if self.current is not None:
                self.current['text'] += data

    def handle_endtag(self, tag):
        if tag in ('style', 'script'):
            self.skip = max(0, self.skip - 1)
        if tag == 'span' and self.current is not None:
            self.figures.append(self.current); self.current = None


def inventory(study, record):
    """Advisory prose inventory only. An existing model number is never treated as proof of the right metric/period."""
    output = []
    for role, paths in record['renders'].items():
        rel = paths['html'] if isinstance(paths, dict) else paths
        parser = Figures(); parser.feed(local(study, rel).read_text(encoding='utf-8'))
        for text in parser.prose:
            numbers = re.findall(r'[-+]?\d[\d,.]*(?:%|x)?', text)
            if numbers:
                output.append({'document': role, 'text': text, 'numbers': numbers})
    return output


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def local(study, rel):
    p = (Path(study) / rel).resolve()
    if not p.is_relative_to(Path(study).resolve()):
        raise ValueError('Review references must remain inside the study: ' + str(rel))
    return p


def inputs(record):
    files = [record[k] for k in ('spec', 'workbook', 'brief')]
    for value in record.get('renders', {}).values():
        files.extend([value['html'], value['pdf']] if isinstance(value, dict) else [value])
    return list(dict.fromkeys(files))


def prepare(study, record, reviewer='unassigned', mode='independent-agent', max_rounds=2, revise=False):
    """After rendering, create a PARTIAL review. Never overwrite an existing review or manufacture a pass."""
    import release_check as rc
    study = Path(study)
    path = local(study, record.get('review', DEFAULT_PATH))
    round_number = 1
    if path.exists():
        if not revise:
            raise FileExistsError(f'Review exists: {path}; use --revise to archive it and review a changed draft')
        previous = json.loads(path.read_text(encoding='utf-8'))
        round_number, max_rounds = previous['round'] + 1, previous['maxRounds']
        if round_number > max_rounds:
            raise ValueError('Review budget exhausted; retain the draft and unresolved findings, do not loop indefinitely')
        shutil.copyfile(path, path.with_name(f'draft-review.round{previous["round"]}.{digest(path)[:8]}.json'))
    if max_rounds < 1:
        raise ValueError('Review budget must be positive')
    files = inputs(record)
    for folder in ('sources', 'data', 'evidence'):
        base = study / folder
        if base.exists():
            files += [p.relative_to(study).as_posix() for p in sorted(base.rglob('*'))
                      if p.is_file() and p != path and '__pycache__' not in p.parts
                      and not p.name.startswith('draft-review') and p.name != 'prose-number-inventory.json']
    files = list(dict.fromkeys(files))
    hashes = {rel: digest(local(study, rel)) for rel in files}
    # Advisory inventory is not a completion record and is intentionally outside the frozen input hash set.
    inv_path = path.with_name('prose-number-inventory.json')
    inv_path.parent.mkdir(parents=True, exist_ok=True)
    inv_path.write_text(json.dumps(inventory(study, record), indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    stamp = datetime.now(timezone.utc).isoformat()
    # The strict common envelope permits 200 sources. Keep core draft/model references here;
    # all evidence remains frozen in reviewedFiles, and the reviewer adds pivotal source locators.
    sources = [{'id': f'file-{i}', 'location': rel, 'locator': f'SHA256 {hashes[rel]}',
                'publishedAt': None, 'availableAt': None, 'retrievedAt': stamp, 'accessStatus': 'available',
                'synthetic': False} for i, rel in enumerate(inputs(record))]
    h = {'id': 'publication-challenge', 'kind': 'challenge', 'version': 1, 'status': 'partial',
         'notApplicableReason': None, 'mandateId': None, 'mandateVersion': None,
         'scopeIds': [record['security']], 'asOf': record['cutoff'][:10] + 'T00:00:00+00:00',
         'producedAt': stamp, 'summary': 'Draft prepared; substantive review has not run.', 'sources': sources,
         'claims': [], 'dependencies': [], 'checks': [
             {'name': name, 'result': 'not-run', 'blocking': True, 'detail': 'Review the actual draft and underlying evidence.'}
             for name in CHECKS], 'criticalUnknowns': [], 'nextActions': []}
    packet = {'schemaVersion': '1.0', 'reviewer': {'id': reviewer, 'mode': mode, 'context': 'fresh'},
              'round': round_number, 'maxRounds': max_rounds, 'reviewedFiles': hashes, 'skillsFingerprint': rc.skills_fingerprint(),
              'coverage': {kind: {'status': 'undecided', 'reason': '', 'assertionIds': []} for kind in FAMILIES},
              'financialAssertions': [], 'handoff': h,
              'task': 'Start a fresh reviewer context. Read the exact draft PDFs, brief, calculated model and original '
                      'pivotal evidence. Review the six writing dimensions and financial definitions. Record actual '
                      'findings; do not defend the author or mark unperformed work complete.'}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(packet, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return path


def validate_handoff(handoff):
    node = os.environ.get('NODE_BINARY') or shutil.which('node')
    if not node:
        raise ValueError('Node.js is required to validate the shared challenge handoff (or set NODE_BINARY)')
    result = subprocess.run([node, str(SKILLS / 'scripts/check-handoff.mjs')],
                            input=json.dumps(handoff), capture_output=True, text=True)
    if result.returncode:
        raise ValueError('Invalid shared challenge handoff: ' + result.stderr[:1200])


def check(study, record, spec, workbook):
    """Return explicit check results. Passing cannot certify source truth or substantive review quality."""
    import release_check as rc
    results = []
    def test(name, ok, detail):
        results.append({'name': name, 'class': 'review', 'result': 'pass' if ok else 'fail', 'detail': detail})
    try:
        path = local(study, record.get('review', DEFAULT_PATH))
        packet = json.loads(path.read_text(encoding='utf-8-sig'))
        if packet.get('schemaVersion') != '1.0':
            raise ValueError('Unsupported publication-review schema')
        h = packet['handoff']
        validate_handoff(h)
        test('draft-review-complete', h['kind'] == 'challenge' and h['status'] == 'complete'
             and any(c['material'] for c in h['claims']) and not h['criticalUnknowns'] and not any(d['changed'] for d in h['dependencies']),
             'A completed challenge needs substantive claims and resolved essential blockers')
        reviewer = packet['reviewer']
        independent = reviewer.get('mode') in ('independent-agent', 'human') and reviewer.get('context') == 'fresh'
        test('draft-review-reader', independent and reviewer.get('id') not in (None, '', 'unassigned'),
             'A named fresh-context agent or human is required; this checks the declaration, not independent identity')
        test('draft-review-budget', 1 <= packet['round'] <= packet['maxRounds'] and packet['maxRounds'] > 0,
             'Correction rounds are bounded; exhausted unresolved reviews remain drafts')
        test('draft-review-cutoff', h['asOf'][:10] == record['cutoff'][:10] and record['security'] in h['scopeIds'],
             'Review cutoff and security must match the publication')
        checks = {c['name']: c for c in h['checks']}
        test('draft-review-required-checks', all(name in checks and checks[name]['result'] == 'pass' for name in CHECKS)
             and not any(c['blocking'] and c['result'] != 'pass' for c in h['checks']),
             'Six editorial dimensions, source/financial basis and visual inspection must be reviewed; scores do not gate release')
        hashes = packet['reviewedFiles']
        missing = [p for p in inputs(record) if p not in hashes]
        test('draft-review-inputs-covered', not missing, 'Missing reviewed artifacts: ' + ', '.join(missing))
        changed = [p for p, sha in hashes.items() if not local(study, p).is_file() or digest(local(study, p)) != sha]
        test('draft-review-files-current', not changed, 'Changed/missing reviewed files: ' + ', '.join(changed[:10]))
        test('draft-review-skills-current', packet['skillsFingerprint'] == rc.skills_fingerprint(),
             'The review must use the current skill/rule snapshot')
        report_paths = record['renders']['report']
        report_html = local(study, report_paths['html'] if isinstance(report_paths, dict) else report_paths).read_text(encoding='utf-8')
        title = re.search(r'<title>(.*?)</title>', report_html, re.I | re.S)
        if title and 'initiat' in title[1].lower():
            test('initiation-financial-summary', 'data-financial-summary="true"' in report_html,
                 'An initiation needs model-linked summary statements; sector-appropriate rows and available history')
        assertions = packet.get('financialAssertions', [])
        ids = [a['id'] for a in assertions]
        test('financial-assertion-identities', len(set(ids)) == len(ids), 'Financial assertion IDs must be unique')
        for family in FAMILIES:
            coverage = packet['coverage'][family]
            linked = coverage.get('assertionIds', [])
            valid = (coverage.get('status') == 'not-applicable' and bool(coverage.get('reason', '').strip()) and not linked
                     or coverage.get('status') == 'checked' and bool(linked)
                     and all(any(a['id'] == i and a['kind'] == family for a in assertions) for i in linked))
            test('financial-coverage:' + family, valid, 'Declare applicable assertions or a reasoned non-applicability; reviewer verifies coverage')
        for assertion in assertions:
            try:
                detail = financial_assertion(study, assertion, spec, workbook, record)
                test('financial-assertion:' + assertion['id'], True, detail)
            except Exception as exc:
                test('financial-assertion:' + assertion['id'], False, str(exc))
    except Exception as exc:
        test('draft-review-readable', False, f'{type(exc).__name__}: {exc}')
    return results


def financial_assertion(study, a, spec, workbook, record=None):
    """Three demonstrated financial error families. References are logical model cells; raw source facts remain reviewed."""
    import release_check as rc
    def vals(refs):
        out = rc.cell_values(spec, workbook, {str(i): ref for i, ref in enumerate(refs)})
        result = [out[str(i)] for i in range(len(refs))]
        if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in result):
            raise ValueError('Every bound value must be a finite calculated model number')
        return result
    def equal(got, wanted, label):
        if not rc.near(got, wanted, 1e-6, 1e-8):
            raise ValueError(f'{label}: {got} does not reconcile to {wanted}')
    for key in ('id', 'kind', 'period', 'unit', 'rationale'):
        if not isinstance(a.get(key), str) or not a[key].strip():
            raise ValueError('Assertion requires ' + key)
    if a['kind'] == 'cash-coverage':
        before, distributions, available, cover = vals([a[k] for k in ('beforeOutflows', 'distributions', 'availableCash', 'coverage')])
        obligations = vals(a['remainingOutflows']) if a['remainingOutflows'] else []
        if distributions <= 0 or any(v < 0 for v in obligations):
            raise ValueError('Distributions must be positive; remaining required cash outflows use positive amounts')
        equal(available, before - sum(obligations), 'Cash available after remaining obligations')
        equal(cover, available / distributions, 'Shareholder cash coverage')
        if not a.get('accountingTreatment'):
            raise ValueError('Explain which obligations are already deducted to prevent double subtraction')
        required_displays = [a['coverage']]
        period_outputs = required_displays
    elif a['kind'] == 'normalized-ratio':
        base_value, base_income, value, income, ratio = vals([a[k] for k in
            ('baseValue', 'baseIncome', 'normalizedValue', 'normalizedIncome', 'ratio')])
        removed_value = removed_income = 0
        for component in a['removedComponents']:
            v, inc = vals([component['value'], component['income']])
            if not component.get('rationale'):
                raise ValueError('Every removed component needs its asset/income treatment explained')
            removed_value += v; removed_income += inc
        equal(value, base_value - removed_value, 'Normalized asset/claim value')
        equal(income, base_income - removed_income, 'Normalized attributable income')
        if income <= 0:
            raise ValueError('Nonpositive income cannot support a meaningful normalized earnings multiple')
        equal(ratio, value / income, 'Normalized ratio')
        basis = a['basis']
        for key in ('claimBoundary', 'incomeDefinition', 'ownership', 'currency', 'scale', 'leaseTreatment', 'periodConvention'):
            if not basis.get(key):
                raise ValueError('Comparison basis requires ' + key)
        for peer in a.get('peerBases', []):
            if peer != basis:
                raise ValueError('Peer and subject asset/income bases differ; normalize or make the comparison directional')
        required_displays = [a['ratio']]
        period_outputs = required_displays
    elif a['kind'] == 'financing':
        as_of = rc.parse_date(a['asOf'])
        if record is not None and as_of != rc.parse_date(record['cutoff']):
            raise ValueError('Active financing terms must be assessed at the publication cutoff')
        eligible = []
        for term in a['terms']:
            if rc.parse_date(term['publishedAt']) <= as_of and rc.parse_date(term['effectiveFrom']) <= as_of:
                if not local(study, term['source']).is_file() or not term.get('locator'):
                    raise ValueError('Active financing terms need an accessible source and locator')
                eligible.append(term)
        if not eligible:
            raise ValueError('No source-backed financing terms effective at the selected cutoff')
        order = lambda t: (rc.parse_date(t['effectiveFrom']), rc.parse_date(t['publishedAt']))
        term = max(eligible, key=order)
        tied = [t for t in eligible if order(t) == order(term)]
        if len({(t['conversionPrice'], t['principal'], t['contractualFx']) for t in tied}) != 1:
            raise ValueError('Conflicting financing terms need source reconciliation')
        principal, fx, price, shares = vals([a[k] for k in ('principal', 'contractualFx', 'conversionPrice', 'conversionShares')])
        equal(principal, term['principal'], 'Current principal')
        equal(fx, term['contractualFx'], 'Contractual conversion FX')
        equal(price, term['conversionPrice'], 'Current effective conversion price')
        if price <= 0 or principal <= 0 or fx <= 0:
            raise ValueError('Conversion price, principal and contractual FX must be positive')
        equal(shares, principal * fx / price, 'Full conversion shares (same share/money scale)')
        required_displays = [a['conversionPrice'], a['conversionShares']]
        period_outputs = []
        if not {'bear', 'base', 'bull'} <= {s['role'] for s in a['scenarios']}:
            raise ValueError('Assess the financing state for every published bear/base/bull scenario')
        for scenario in a['scenarios']:
            target, base_shares, count, profit, addback, eps = vals([scenario[k] for k in
                ('target', 'baseShares', 'shares', 'profit', 'afterTaxAddback', 'eps')])
            weight = scenario['conversionWeight']
            if base_shares <= 0 or count <= 0:
                raise ValueError('Scenario base and adjusted share counts must be positive')
            if not isinstance(weight, (int, float)) or not 0 <= weight <= 1 or not scenario.get('rationale'):
                raise ValueError('Every scenario needs an explained conversion state and period weight')
            if target >= price and weight == 0 and not scenario.get('nonConversionReason'):
                raise ValueError('In-the-money scenario needs conversion treatment or an explicit non-conversion case')
            equal(count, base_shares + shares * weight, 'Scenario share count')
            equal(eps, (profit + addback) / count, 'Scenario EPS/share-financing bridge')
            required_displays.append(scenario['eps'])
            period_outputs.append(scenario['eps'])
    else:
        raise ValueError('Unknown financial assertion family: ' + a['kind'])
    if record is not None:
        displays = a.get('displays', [])
        if any(ref not in [d['ref'] for d in displays] for ref in required_displays):
            raise ValueError('Bind the material assertion outputs to displayed figures, including scenario EPS')
        figures = []
        for paths in record['renders'].values():
            parser = Figures()
            parser.feed(local(study, paths['html'] if isinstance(paths, dict) else paths).read_text(encoding='utf-8'))
            figures += parser.figures
        for display in displays:
            if display['ref'] in period_outputs and display['period'] != a['period']:
                raise ValueError('Financial output display period differs from its assertion period')
            wanted = vals([display['ref']])[0]
            matches = [f for f in figures if f['data-model-claim'] == display['id']]
            if not matches:
                raise ValueError('No rendered financial binding: ' + display['id'])
            for figure in matches:
                equal(float(figure['data-value']), wanted, 'Rendered bound raw value')
                if figure.get('data-period') != display['period'] or figure.get('data-unit') != display['unit']:
                    raise ValueError('Rendered financial period/unit differs from its declared model binding')
                # Standard financial formatting: commas, parentheses, %, x and currency labels.
                text = figure['text'].strip()
                number = re.search(r'[-+]?\d[\d,]*(?:\.\d+)?', text)
                if not number:
                    raise ValueError('Bound financial figure has no visible numeric value')
                raw = float(number.group().replace(',', ''))
                prefix = text[:number.start()]
                negative = raw < 0 or text.startswith('(') or '-' in prefix or '\u2212' in prefix
                shown = -abs(raw) if negative else raw
                expected = wanted * (100 if '%' in text else 1)
                decimals = len(number.group().rsplit('.', 1)[1]) if '.' in number.group() else 0
                if abs(shown - expected) > .5 * 10 ** -decimals + 1e-8:
                    raise ValueError('Visible figure differs from its raw model binding')
    return 'Bound financial definition and arithmetic reconcile; evidence and rationale still require substantive review'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=('writing', 'prepare', 'check', 'finalize'))
    p.add_argument('study', type=Path)
    p.add_argument('--reviewer', default='unassigned')
    p.add_argument('--revise', action='store_true')
    p.add_argument('--max-rounds', type=int, default=2)
    p.add_argument('--inputs', nargs='+')
    args = p.parse_args()
    if args.action == 'writing':
        print(writing_packet(args.study, args.inputs)); return 0
    record = json.loads((args.study / 'deliverables/release.json').read_text(encoding='utf-8'))
    if args.action == 'prepare':
        import report_layout as rl
        record_path = args.study / 'deliverables/release.json'
        def save():
            tmp = record_path.with_suffix('.json.tmp')
            tmp.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8'); tmp.replace(record_path)
        if record.get('zipPath'):
            zipped = local(args.study, record['zipPath'])
            if zipped.suffix.lower() != '.zip' or not zipped.is_relative_to((args.study / 'deliverables').resolve()):
                raise ValueError('The release ZIP must be inside the study deliverables folder')
            zipped.unlink(missing_ok=True)
        record.pop('fingerprints', None); record['status'] = 'awaiting-review'; save()
        try:
            existing = local(args.study, record.get('review', DEFAULT_PATH))
            if existing.exists():
                previous = json.loads(existing.read_text(encoding='utf-8'))
                if not args.revise or previous['round'] >= previous['maxRounds']:
                    raise ValueError('Existing review needs --revise and remaining correction budget')
            for paths in record['renders'].values():
                if isinstance(paths, dict):
                    expected = local(args.study, paths['pdf'])
                    actual = rl.print_pdf(local(args.study, paths['html']), expected)
                    if actual is not None and Path(actual).resolve() != expected:
                        raise ValueError('Requested PDF is locked; close it and reprint before preparing review: ' + str(expected))
            print(prepare(args.study, record, reviewer=args.reviewer, revise=args.revise, max_rounds=args.max_rounds))
        except Exception as exc:
            record.update(status='failed', error=f'{type(exc).__name__}: {exc}'); save(); raise
    elif args.action == 'check':
        import release_check as rc
        spec = json.loads(local(args.study, record['spec']).read_text(encoding='utf-8-sig'))
        results = check(args.study, record, spec, local(args.study, record['workbook']))
        print(json.dumps(results, indent=2)); return int(any(c['result'] == 'fail' for c in results))
    else:
        import report_layout as rl
        renders = record['renders']
        excluded = {'renders', 'deliverables', 'briefPdf', 'checks', 'fingerprints', 'status', 'scope', 'error', 'zipPath'}
        printed = {renders['report']['pdf'], renders['brief']['pdf']}
        companions = [local(args.study, p) for p in record['deliverables'] if p not in printed]
        rl.package(args.study, local(args.study, record['zipPath']), local(args.study, renders['report']['html']),
                   local(args.study, renders['brief']['html']), companions,
                   **{k: v for k, v in record.items() if k not in excluded})
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
