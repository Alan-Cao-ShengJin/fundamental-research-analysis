"""A frozen draft packet around the existing challenge handoff, plus material financial-claim checks.

This verifies completion, provenance and defined arithmetic, not the truth of evidence or a reviewer's independence.
The host starts a fresh writer/reviewer context; this module does not call an LLM or send anything externally.
"""
from __future__ import annotations
import argparse
import copy
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
import tarfile
from uuid import uuid4

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
                      'Develop business drivers before detailed valuation, beyond the compact header. When describing '
                      'the overall payoff, reconcile price movement and eligible cash on the same dated horizon; '
                      'cash yield is separate from the price-target rating. Compare matched periods before attributing '
                      'a change to peers or a common regime, and qualify causal inferences. Rounded watch levels invite '
                      'reassessment; automatic numeric rating conditions require tested displayed thresholds. '
                      'Do not change the forecast or target just to improve the prose. A brief conclusion keeps the conditions '
                      'the report attaches: alternatives that change the rating, partial answers, management-only evidence. '
                      'Render drafts, not a release.',
              'execution': 'The host launches the fresh context; this packet does not launch an agent.'}
    out = local(study, 'evidence/writing-packet.json')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(packet, indent=2) + '\n', encoding='utf-8')
    return out


class Figures(HTMLParser):
    def __init__(self):
        super().__init__(); self.figures = []; self.current = None; self.skip = 0; self.prose = []; self.span_depth = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('style', 'script'):
            self.skip += 1
        if tag == 'span' and self.current is not None:
            self.span_depth += 1
        if a.get('data-model-claim'):
            if tag != 'span' or self.current is not None:
                raise ValueError('Bound figures must be non-overlapping span elements')
            self.current = dict(a, text='')
            self.span_depth = 1

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
            self.span_depth -= 1
            if self.span_depth == 0:
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
    files.append(record.get('decisionRecord','evidence/decision.json'))
    return list(dict.fromkeys(files + record.get('reviewInputs', [])))


def evaluation_context(study, record):
    """An explicit host fixture clock never replaces actual production/retrieval timestamps."""
    context = record.get('evaluation')
    if context is None:
        for parent in (Path(study).resolve(), *Path(study).resolve().parents):
            config = parent / '.research-evaluation.json'
            if config.is_file():
                context = json.loads(config.read_text(encoding='utf-8'))
                break
    if context is not None:
        if (set(context) != {'mode', 'now', 'reason'} or context['mode'] != 'synthetic-fixture'
                or not str(context['reason']).strip()):
            raise ValueError('Fixture evaluation requires mode=synthetic-fixture, now and a reason')
        datetime.fromisoformat(context['now'].replace('Z', '+00:00'))
    return context


def freeze_inputs(study, files, record, stamp, fingerprint, round_number, evaluation):
    """Copy before handoff. The live builder may subsequently change; reviewed bytes must survive."""
    relative = f'evidence/review-snapshots/round-{round_number:02d}-{uuid4().hex[:12]}'
    root = local(study, relative)
    root.mkdir(parents=True, exist_ok=False)
    hashes = {}
    for rel in files:
        source, destination = local(study, rel), local(root / 'files', rel)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        hashes[rel] = digest(destination)
        if digest(source) != hashes[rel]:
            raise ValueError('Input changed during snapshot: ' + rel)
    # Retain the actual rule bytes as well as their aggregate fingerprint; no extraction is needed to verify it.
    with tarfile.open(root / 'rules.tar', 'w') as archive:
        for source in sorted(SKILLS.rglob('*')):
            if (source.is_file() and source.suffix in ('.md', '.json', '.py', '.mjs')
                    and 'node_modules' not in source.parts and '__pycache__' not in source.parts):
                archive.add(source, arcname=source.relative_to(SKILLS).as_posix(), recursive=False)
    manifest = {'createdAt': stamp, 'reviewedFiles': hashes, 'releaseRecord': record,
                'skillsFingerprint': fingerprint, 'rulesSHA256': digest(root / 'rules.tar'), 'evaluation': evaluation}
    manifest_path = root / 'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    return hashes, {'path': relative, 'manifestSHA256': digest(manifest_path)}


def check_snapshot(study, packet):
    root = local(study, packet['snapshot']['path'])
    manifest_path = root / 'manifest.json'
    if digest(manifest_path) != packet['snapshot']['manifestSHA256']:
        raise ValueError('Review snapshot manifest changed')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    if (manifest['reviewedFiles'] != packet['reviewedFiles']
            or manifest['skillsFingerprint'] != packet['skillsFingerprint']
            or manifest['evaluation'] != packet.get('evaluation')):
        raise ValueError('Review snapshot does not match the declared inputs/rules/evaluation')
    for rel, sha in manifest['reviewedFiles'].items():
        if digest(local(root / 'files', rel)) != sha:
            raise ValueError('Archived reviewed input changed: ' + rel)
    if digest(root / 'rules.tar') != manifest['rulesSHA256']:
        raise ValueError('Archived rule bytes changed')


def prepare(study, record, reviewer='unassigned', mode='independent-agent', max_rounds=2, revise=False):
    """After rendering, create a PARTIAL review. Never overwrite an existing review or manufacture a pass."""
    import release_check as rc
    study = Path(study).resolve()
    path = local(study, record.get('review', DEFAULT_PATH))
    from review_attempts import state
    usage = state(study)
    max_rounds = usage['maxRounds'] or max_rounds
    if type(max_rounds) is not int or max_rounds < 1:
        raise ValueError('Review budget must be a positive integer')
    round_number = usage['used'] + 1
    prior_review = None
    if round_number > max_rounds:
        raise ValueError('Review budget exhausted; retain the draft and unresolved findings, do not loop indefinitely')
    if usage['draftVersion'] and (not path.exists() or path != local(study, usage['reviewPath'])):
        raise ValueError('Existing review path is missing or renamed; preserve its actual findings before preparing another draft')
    if path.exists():
        if not revise:
            raise FileExistsError(f'Review exists: {path}; use --revise to archive it and review a changed draft')
        previous = json.loads(path.read_text(encoding='utf-8'))
        archive = path.with_name(f'draft-review.round{previous["round"]}.{digest(path)[:8]}.json')
        shutil.copyfile(path, archive)
        prior_review = {'path': archive.relative_to(study).as_posix(), 'sha256': digest(archive)}
        if previous.get('snapshot'):
            shutil.copyfile(path, local(study, previous['snapshot']['path']) / f'archived-review.{digest(path)[:12]}.json')
    if max_rounds < 1:
        raise ValueError('Review budget must be positive')
    files = inputs(record)
    for folder in ('sources', 'data', 'evidence'):
        base = study / folder
        if base.exists():
            files += [p.relative_to(study).as_posix() for p in sorted(base.rglob('*'))
                      if p.is_file() and p != path and '__pycache__' not in p.parts
                      and 'review-snapshots' not in p.parts
                      and not p.name.startswith('draft-review') and p.name != 'prose-number-inventory.json']
    # Include the producer and bindings, not just its outputs. Explicit reviewInputs covers other build arrangements.
    for folder in ('build', 'deliverables'):
        base = study / folder
        files += [p.relative_to(study).as_posix() for p in sorted(base.glob('*'))
                  if p.is_file() and p.suffix in ('.py', '.json') and p.name != 'release.json']
    files = list(dict.fromkeys(files))
    stamp = datetime.now(timezone.utc).isoformat()
    evaluation = evaluation_context(study, record)
    cutoff = record['cutoff'][:10] + 'T00:00:00+00:00'
    if not evaluation and datetime.fromisoformat(cutoff) > datetime.fromisoformat(stamp):
        raise ValueError('Research cutoff is in the future; use a host-declared synthetic fixture clock, not a false producedAt')
    fingerprint = rc.skills_fingerprint()
    hashes, snapshot = freeze_inputs(study, files, record, stamp, fingerprint, round_number, evaluation)
    # Advisory inventory is not a completion record and is intentionally outside the frozen input hash set.
    inv_path = path.with_name('prose-number-inventory.json')
    inv_path.parent.mkdir(parents=True, exist_ok=True)
    inv_path.write_text(json.dumps(inventory(study, record), indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    # The strict common envelope permits 200 sources. Keep core draft/model references here;
    # all evidence remains frozen in reviewedFiles, and the reviewer adds pivotal source locators.
    sources = [{'id': f'file-{i}', 'location': rel, 'locator': f'SHA256 {hashes[rel]}',
                'publishedAt': None, 'availableAt': None, 'retrievedAt': stamp, 'accessStatus': 'available',
                'synthetic': evaluation is not None} for i, rel in enumerate(inputs(record))]
    h = {'id': 'publication-challenge', 'kind': 'challenge', 'version': 1, 'status': 'partial',
         'notApplicableReason': None, 'mandateId': None, 'mandateVersion': None,
         'scopeIds': [record['security']], 'asOf': record['cutoff'][:10] + 'T00:00:00+00:00',
         'producedAt': stamp, 'summary': 'Draft prepared; substantive review has not run.', 'sources': sources,
         'claims': [], 'dependencies': [], 'checks': [
             {'name': name, 'result': 'not-run', 'blocking': True, 'detail': 'Review the actual draft and underlying evidence.'}
             for name in CHECKS], 'criticalUnknowns': [], 'nextActions': []}
    from review_attempts import prior_requirements
    packet = {'schemaVersion': '1.2', 'draftVersion': usage['draftVersion'] + 1,
              'researchMode': record.get('researchMode', 'unspecified'),
              'reviewPath': path.relative_to(study).as_posix(),
              'priorReview': prior_review, 'priorRequirements': prior_requirements(study, prior_review), 'priorDispositions': [],
              'reviewer': {'id': reviewer, 'mode': mode, 'context': 'fresh'},
              'round': round_number, 'maxRounds': max_rounds, 'reviewedFiles': hashes, 'skillsFingerprint': fingerprint,
              'snapshot': snapshot, 'evaluation': evaluation,
              'valuationBasis': {'status': 'undecided', 'reason': '', 'cases': []},
              'coverage': {**{kind: {'applicability': 'undetermined', 'status': 'undecided', 'reason': '',
                                   'assertionIds': [], 'claimIds': []} for kind in FAMILIES},
                           'claim-support': {'status': 'undecided', 'reason': '', 'assertionIds': []},
                           'comparisons': {'status': 'undecided', 'reason': '', 'assertionIds': []},
                           'incremental-flows': {'status': 'undecided', 'reason': '', 'assertionIds': [], 'candidates': []},
                           'brief-fidelity': {'status': 'undecided', 'items': []},
                           'sensitivity': {'status': 'undecided', 'reason': '', 'sensitivityIds': []}},
              'financialAssertions': [], 'claimAssertions': [], 'handoff': h,
                'task': 'Before reviewing, run publication_review.py begin STUDY --reviewer NAME. Preparation alone is not '
                        'a review attempt; starting consumes one, even if interrupted or failed. '
                        'Check automatic numerical triggers at the displayed precision; rounded watch levels invite '
                      'reassessment and cannot promise a new rating. Financial applicability follows the economic '
                      'claim, not whether a model row was built: applicable but unbound means incomplete verification. '
                      'Read the payoff explanation against price gain and eligible cash receipts on the same horizon, '
                      'with dividends still separate from the rating. Multi-year levels do not establish what drove '
                      'a particular period change; test date-matched alternatives and qualify causal attribution. '
                      'In a full initiation, inspect whether drivers precede detailed valuation beyond the compact header. '
                        'Start a fresh reviewer '
                      'context. Read the exact draft PDFs, brief, calculated model and original '
                      'pivotal evidence. Review the six writing dimensions and financial definitions. Record actual '
                      'findings; do not defend the author or mark unperformed work complete. Read the brief against the report: '
                      'a brief stated more firmly than the report supports is a finding. Comparative claims require '
                      'evidence for both sides on compatible definitions. Record ordinary forecast uncertainty as '
                      'assumption/inference claims with scenarios and revision triggers; criticalUnknowns is reserved '
                      'for unknowns that actually prevent a defensible release. Complete valuationBasis from the '
                      'economic anchor, not a restated headline multiple. Preserve actual production/retrieval times. '
                      'Complete claim-support coverage: quantify set claims over the declared set, distinguish company '
                      'evidence from industry inference, reconcile cash metrics to the owner, and verify new numerical '
                      'corrections proposed by this reviewer as well as author calculations. Use computed results in '
                      'the published wording and findings. Complete comparison and incremental-flow coverage: match '
                      'quantity, period, unit, currency/scale, perimeter and earnings basis before comparing. For material '
                      'overlapping cumulative flows derive the latest non-overlapping period; ratios, per-share values '
                      'and balances need separate bridges. Explain unavailable/noncomparable data rather than inventing it. '
                      'Complete brief-fidelity items for decisive claims and their qualifications. A passing ledger does '
                      'not validate unbound prose or establish that the coverage list is complete.'}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(packet, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    shutil.copyfile(path, local(study, snapshot['path']) / 'prepared-review.json')
    return path


def validate_handoff(handoff, evaluation=None):
    node = os.environ.get('NODE_BINARY') or shutil.which('node')
    if not node:
        raise ValueError('Node.js is required to validate the shared challenge handoff (or set NODE_BINARY)')
    command = [node, str(SKILLS / 'scripts/check-handoff.mjs')]
    if evaluation:
        command += ['--fixture-clock', evaluation['now'], '--fixture-reason', evaluation['reason']]
    result = subprocess.run(command,
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
        if packet.get('schemaVersion') != '1.2':
            raise ValueError('Unsupported publication-review schema')
        h = packet['handoff']
        test('research-mode-declared', packet.get('researchMode') in ('initiation', 'regular-review', 'earnings-update', 'catalyst-update')
             and packet['researchMode'] == record.get('researchMode'), 'Use the routed research mode; it is not a user prompt requirement')
        validate_handoff(h, packet.get('evaluation'))
        test('draft-review-production-time', datetime.fromisoformat(h['producedAt'].replace('Z', '+00:00')) <= datetime.now(timezone.utc),
             'producedAt records actual production, including in a synthetic-clock evaluation')
        test('draft-review-evaluation-current', packet.get('evaluation') == evaluation_context(study, record),
             'The host fixture clock, when present, must remain the declared evaluation context')
        try:
            check_snapshot(study, packet)
            test('draft-review-snapshot', True, 'Complete reviewed inputs and rule bytes retained before handoff')
        except (KeyError, OSError, ValueError) as exc:
            test('draft-review-snapshot', False, str(exc))
        test('draft-review-complete', h['kind'] == 'challenge' and h['status'] == 'complete'
             and any(c['material'] for c in h['claims']) and not h['criticalUnknowns'] and not any(d['changed'] for d in h['dependencies']),
             'A completed challenge needs substantive claims and resolved essential blockers')
        reviewer = packet['reviewer']
        independent = reviewer.get('mode') in ('independent-agent', 'human') and reviewer.get('context') == 'fresh'
        test('draft-review-reader', independent and reviewer.get('id') not in (None, '', 'unassigned'),
             'A named fresh-context agent or human is required; this checks the declaration, not independent identity')
        try:
            from review_attempts import verify, prior_dispositions
            test('draft-review-budget', True, verify(study, packet))
            test('prior-review-dispositions', prior_dispositions(study, packet),
                 'Prior failed checks and essential unknowns need evidence-backed resolution or a justified disagreement')
        except (ValueError, KeyError, OSError) as exc:
            test('draft-review-budget', False, str(exc))
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
            import financial_coverage
            valid,detail=financial_coverage.verify(family,coverage,packet)
            test('financial-coverage:' + family, valid, detail)
        sens = packet['coverage'].get('sensitivity', {})
        ok, detail = sensitivity_coverage(spec, sens)
        test('sensitivity-coverage', ok, detail)
        ok, detail = valuation_basis(spec, record, packet.get('valuationBasis', {}), h, sens.get('sensitivityIds', []))
        test('valuation-economic-basis', ok, detail)
        import claim_checks
        ok, detail = claim_checks.coverage(packet)
        test('claim-support-coverage', ok, detail)
        import comparison_checks
        for key, kinds in (('comparisons', {'comparison'}), ('incremental-flows', {'incremental-flow'})):
            test(key + '-coverage', comparison_checks.coverage(packet, key, kinds),
                 'Bind material comparable/incremental assertions or reasoned non-applicability; the reader checks omissions')
        test('brief-fidelity-coverage', comparison_checks.brief_fidelity(packet),
             'Review decisive brief claims against the report, including denominator, timing, ownership and conditional conclusions')
        for assertion in packet.get('claimAssertions', []):
            try:
                test('claim-assertion:' + assertion['id'], True, claim_checks.evaluate(study, assertion, spec, packet))
            except Exception as exc:
                test('claim-assertion:' + str(assertion.get('id')), False, str(exc))
        # A new formatted span cannot be only self-declared; it needs a source/model assertion.
        declared_displays = {(d['document'],d['id']) for a in packet.get('claimAssertions',[]) for d in a.get('displays',[])}
        for paths in record['renders'].values():
            rel = paths['html'] if isinstance(paths,dict) else paths
            parser = Figures(); parser.feed(local(study,rel).read_text(encoding='utf-8'))
            uncovered = [f['data-model-claim'] for f in parser.figures if 'data-measure-format' in f and (rel,f['data-model-claim']) not in declared_displays]
            test('rendered-measures-covered:'+rel, not uncovered, 'Unbound formatted measures: '+', '.join(uncovered))
        for assertion in assertions:
            try:
                detail = financial_assertion(study, assertion, spec, workbook, record)
                test('financial-assertion:' + assertion['id'], True, detail)
            except Exception as exc:
                test('financial-assertion:' + assertion['id'], False, str(exc))
    except Exception as exc:
        test('draft-review-readable', False, f'{type(exc).__name__}: {exc}')
    return results


def valuation_basis(spec, record, declaration, handoff, sensitivity_ids=()):
    """Check the declared economic anchor, not just P/E times EPS after an algebraic restatement.

    Semantic labels and source relevance remain a reader's responsibility. The cancellation probe is narrow:
    it rejects an inverse-EPS multiple that exactly erases the declared earnings, not ordinary growth adjustments.
    """
    import model_workbook as mw
    if record['method'] != 'P/E':
        ok = (declaration.get('status') == 'not-applicable' and bool(declaration.get('reason', '').strip())
              and not declaration.get('cases'))
        return ok, 'P/E period contract not applicable; other methods retain their own financial-basis review'
    if declaration.get('status') != 'checked':
        return False, 'Declare the primary and scenario P/E economic anchors before publication'
    try:
        cases = declaration['cases']
        if len(cases) != 3 or {c['id'] for c in cases} != {'bear', 'base', 'bull'}:
            raise ValueError('Declare bear, base and bull once each')
        sources = {s['id'] for s in handoff['sources']}
        for case in cases:
            period = record['epsPeriod']
            if case['period'] != period or case['benchmarkPeriod'] != period:
                raise ValueError(f'{case["id"]}: economic anchor and scenario must use the house period {period}; CY comparisons are separate')
            if not case.get('rationale', '').strip() or not case.get('sourceIds') or not set(case['sourceIds']) <= sources:
                raise ValueError('Each anchor needs a rationale and registered source references')
            selected = copy.deepcopy(mw.with_case(spec, case.get('selector')))
            engine = mw.Engine(selected)
            def number(ref):
                sh, address = mw.target(ref, '')
                value = engine.value(sh, address)
                if type(value) not in (int, float) or not math.isfinite(value):
                    raise ValueError('Anchor bindings require finite calculated values')
                return value
            eps, multiple, target = [number(case[k]) for k in ('metricRef', 'multipleRef', 'targetRef')]
            fx = number(case['fxRef']) if case.get('fxRef') else 1
            if eps <= 0 or multiple <= 0 or fx <= 0 or not math.isclose(eps * multiple / fx, target, rel_tol=1e-6, abs_tol=1e-8):
                raise ValueError('Scenario target does not match its declared earnings/multiple/FX basis')
            if case['id'] == 'base':
                for key, binding in (('metricRef', 'forwardEps'), ('multipleRef', 'targetMultiple'), ('targetRef', 'target')):
                    if case[key] != record['bindings'][binding]:
                        raise ValueError('Primary economic basis must match the publication bindings')
                pricing = case.get('sensitivityPricing', [])
                if (len({p['id'] for p in pricing}) != len(pricing)
                        or {p['id'] for p in pricing} != set(sensitivity_ids)):
                    raise ValueError('Map every covered sensitivity to its selected target-pricing period')
                sh, address = mw.target(case['metricRef'], '')
                selected['sheets'][sh]['cells'][address]['value'] = eps * 1.02
                shocked = mw.Engine(selected)
                msh, ma = mw.target(case['multipleRef'], '')
                new_multiple = shocked.value(msh, ma)
                if (not math.isclose(new_multiple, multiple, rel_tol=1e-9)
                        and math.isclose(new_multiple * eps * 1.02, multiple * eps, rel_tol=1e-8)):
                    raise ValueError('Declared forward EPS cancels through an inverse-EPS target multiple; identify the actual economic anchor')
            if any(s.get('period') != period for s in case.get('sensitivityPricing', [])):
                raise ValueError('Published sensitivities must reprice on the same selected earnings period')
        return True, 'Scenario anchors and headline bindings share the declared forward period; no primary inverse-EPS cancellation'
    except (KeyError, TypeError, ValueError, mw.ModelError) as exc:
        return False, str(exc)


def sensitivity_coverage(spec, coverage):
    """Each published model sensitivity maps to a declared full-model recalculation, or the review gives a reason
    (for example, the decisive output is not EPS, or another reviewed method tests it). The reviewer, not this check,
    establishes that every material published sensitivity is listed."""
    import model_workbook as mw
    ids = coverage.get('sensitivityIds', [])
    if coverage.get('status') == 'not-applicable':
        ok = bool(coverage.get('reason', '').strip()) and not ids
        return ok, 'Reasoned non-applicability' if ok else 'Non-applicability needs a reason and no sensitivity IDs'
    if coverage.get('status') != 'checked' or not ids:
        return False, 'Map each published sensitivity to a declared model sensitivity, or give a reasoned non-applicability'
    declared = {d.get('id'): d for d in spec.get('sensitivities', [])}
    missing = [i for i in ids if i not in declared]
    if missing:
        return False, 'Not declared in the model specification: ' + ', '.join(missing)
    failing = [i['sensitivity'] for i in mw.sensitivities({**spec, 'sensitivities': [declared[i] for i in ids]})]
    if failing:
        return False, 'Shown change differs from full-model recalculation: ' + ', '.join(map(str, failing))
    return True, f'{len(ids)} published sensitivities reproduce through the full model'


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
    p.add_argument('action', choices=('writing', 'prepare', 'begin', 'check', 'finalize'))
    p.add_argument('study', type=Path)
    p.add_argument('--reviewer', default='unassigned')
    p.add_argument('--review-mode', choices=('independent-agent', 'human'), default='independent-agent')
    p.add_argument('--revise', action='store_true')
    p.add_argument('--max-rounds', type=int, default=2)
    p.add_argument('--inputs', nargs='+')
    args = p.parse_args()
    if args.action == 'writing':
        print(writing_packet(args.study, args.inputs)); return 0
    record = json.loads((args.study / 'deliverables/release.json').read_text(encoding='utf-8'))
    if args.action == 'begin':
        from review_attempts import begin
        print(begin(args.study, record, reviewer=args.reviewer, mode=args.review_mode)); return 0
    if args.action == 'prepare':
        import report_layout as rl
        record.setdefault('decisionRecord','evidence/decision.json')
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
                from review_attempts import state
                usage = state(args.study)
                if not args.revise or usage['used'] >= usage['maxRounds']:
                    raise ValueError('Existing review needs --revise and remaining correction budget')
            for paths in record['renders'].values():
                if isinstance(paths, dict):
                    expected = local(args.study, paths['pdf'])
                    actual = rl.print_pdf(local(args.study, paths['html']), expected)
                    if actual is not None and Path(actual).resolve() != expected:
                        raise ValueError('Requested PDF is locked; close it and reprint before preparing review: ' + str(expected))
            import release_check as rc
            # The saved record holds the previous draft's bindings and results; recheck them against the revised files.
            record['checks'], fails = rc.run(args.study, record, legacy=True)
            if fails:
                raise ValueError('Revised draft fails integrity checks with the saved bindings; rerun the package adapter '
                                 'with revise=True if bindings changed:\n  ' + '\n  '.join(fails))
            save()
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
