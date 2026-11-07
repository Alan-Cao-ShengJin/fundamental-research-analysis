"""Release check for a study's deliverables: objective tests of rules already set, each tied to a failure that has happened.

Run from the build path through report_layout.package(), which validates the rendered HTML, prints the PDFs from those
exact files, writes deliverables/release.json (the run record: inputs, checks, file hashes, provenance) and makes the
zip only when every check passes. To verify an existing release later:

    python -B -X utf8 release_check.py <study folder>

which reruns the checks and compares every file with the hashes saved at release. Checks are classed `integrity`
(numbers, periods, dates, bindings, files) or `wording` (the regression list of phrasing that has reached a report).
A current release also requires a completed fresh-reader declaration bound to the actual draft files and applicable
financial assertions. This checks completion, provenance and defined arithmetic, not source truth or reviewer identity.
Use --legacy only for explicitly labeled historical integrity inspection, not for current publication.
"""
from __future__ import annotations
import hashlib, html as html_lib, json, re, subprocess, sys
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parents[1]
for p in (SKILLS / 'company-model' / 'scripts', SKILLS / 'research-brief' / 'scripts'):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

RATING = {'Buy', 'Hold', 'Sell'}
METHODS = ('P/E', 'P/B', 'SOTP', 'dividend-yield')
# Wording that has reached a report before. A regression list for deliverables, not a style judge; "fair value" is the
# house rule that the multiple is a reasonable target, never fair value.
BANNED_PHRASES = ('nobody publishes', 'nobody will tell', 'read it from the price', 'fair value', 'we do not roll',
                  'internal run', 'checklist finding')
BYLINE = re.compile(r'\b(prepared by|analyst:|author:|contact:)', re.I)
EMAIL = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]*\w')
SCOPE = ('Checked: calculation caches, target basis and period, rating and tier, the decision block in the brief payload '
         'and in the rendered report and brief, observation and retrieval ages, currency and security, one-page brief, '
         'file hashes and print provenance, and the wording regression list. Current publication additionally checks '
         'completed review declarations bound to current files and skills, and applicable declared financial assertions '
         'and displayed bindings. Legacy inspection explicitly omits the review requirement. Not certified: source '
         'truth or extraction, review quality or independent identity, unbound prose figures, undeclared financial '
         'claims, share class/scale beyond declared bindings, contributor vintages, last exchange session or visual '
         'quality. Those require substantive review.')


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse_date(text):
    """A date from ISO text or free text such as '5 Nov 2026 close (FactSet)'."""
    if isinstance(text, date):
        return text
    s = str(text)
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', s)
    if m:
        return date(int(m[1]), int(m[2]), int(m[3]))
    from dateutil import parser
    return parser.parse(s, fuzzy=True, dayfirst=True).date()


def fiscal_year_of(d, fiscal_year_end=12):
    """Fiscal years are named by the calendar year they end in."""
    return d.year if d.month <= fiscal_year_end else d.year + 1


def third_quarter_end(fy, fiscal_year_end=12):
    q3_month = (fiscal_year_end - 3 - 1) % 12 + 1
    q3_year = fy if q3_month < fiscal_year_end else fy - 1
    nxt = date(q3_year + (q3_month == 12), q3_month % 12 + 1, 1)
    return nxt - timedelta(days=1)


def forward_period(cutoff, fiscal_year_end=12, third_quarter_covered=False):
    """The fiscal year whose EPS carries the target under the house rule: the current fiscal year, or the next one once
    the cutoff is past the third fiscal quarter AND results or a dated operating update covering that quarter have been
    published. Quarter end alone does not switch the year."""
    cutoff = parse_date(cutoff)
    fy = fiscal_year_of(cutoff, fiscal_year_end)
    past_q3 = cutoff > third_quarter_end(fy, fiscal_year_end)
    return f'FY{fy + 1 if past_q3 and third_quarter_covered else fy}E'


def ntm_weights(start, fiscal_year_end=12):
    """Share of the twelve months from `start` falling in each fiscal year, by whole months."""
    start = parse_date(start)
    out = {}
    for i in range(12):
        m = (start.month - 1 + i) % 12 + 1
        y = start.year + (start.month - 1 + i) // 12
        fy = fiscal_year_of(date(y, m, 1), fiscal_year_end)
        out[f'FY{fy}E'] = out.get(f'FY{fy}E', 0) + 1 / 12
    return out


def period_year(label):
    m = re.search(r'(\d{4}|\d{2})(?!\d)', str(label))
    if not m:
        return None
    y = int(m[1])
    return y if y > 99 else 2000 + y


def rating_for(price_return):
    r = Decimal(str(price_return))
    return 'Buy' if r > Decimal('0.10') else 'Sell' if r < Decimal('-0.10') else 'Hold'


def text_of(path):
    path = Path(path)
    if path.suffix.lower() == '.pdf':
        import fitz
        return '\n'.join(page.get_text() for page in fitz.open(str(path)))
    raw = path.read_text(encoding='utf-8', errors='replace')
    if path.suffix.lower() in ('.html', '.htm'):
        raw = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', raw, flags=re.S | re.I)
        raw = html_lib.unescape(re.sub(r'<[^>]+>', ' ', raw))
    return raw


def page_count(pdf_path):
    import fitz
    return len(fitz.open(str(pdf_path)))


def _num(s):
    s = html_lib.unescape(str(s))
    m = re.search(r'-?[\d,]*\.?\d+', s.replace('−', '-'))
    return float(m[0].replace(',', '')) if m else None


def rendered_decision(html):
    """Rating, reference price and target as displayed in a rendered report (rating_box) or brief (template)."""
    m = re.search(r'<div class="rbox"><div class="rating"[^>]*>(Buy|Hold|Sell)</div><table class="kv"><tr><td>[^<]*</td><td>([^<]+)</td></tr>'
                  r'<tr><td>12-month target</td><td><b>([^<]+)</b>', html, re.S)
    if m:
        return {'rating': m[1], 'price': _num(m[2]), 'target': _num(m[3]), 'kind': 'report'}
    r = re.search(r'<span class="rating">(Buy|Hold|Sell) \|', html)
    p = re.search(r'<small>Reference price</small><strong[^>]*>([^<]+)</strong>', html)
    t = re.search(r'<small>Price target</small><strong[^>]*>([^<]+)</strong>', html)
    if r and p and t:
        return {'rating': r[1], 'price': _num(p[1]), 'target': _num(t[1]), 'kind': 'brief'}
    return None


def git_state(root):
    try:
        head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(['git', 'status', '--porcelain'], cwd=root, capture_output=True, text=True, check=True).stdout.strip() != ''
        return {'commit': head, 'dirty': dirty}
    except Exception:  # noqa: BLE001 - no git is a fact to record, not a failure
        return {'commit': None, 'dirty': None}


def skills_fingerprint():
    h = hashlib.sha256()
    for p in sorted(SKILLS.rglob('*')):
        if p.is_file() and p.suffix in ('.md', '.json', '.py', '.mjs') and 'node_modules' not in p.parts and '__pycache__' not in p.parts:
            h.update(p.relative_to(SKILLS).as_posix().encode()); h.update(p.read_bytes())
    return h.hexdigest()


def cell_values(spec, workbook, bindings):
    """Cached workbook values at logical addresses ('Sheet!D37', the specification's own convention)."""
    import model_workbook as mw
    from openpyxl import load_workbook
    layout, book, out = mw.Layout(spec), load_workbook(workbook, data_only=True), {}
    for name, ref in bindings.items():
        sheet, address = mw.target(ref, '')
        out[name] = book[sheet][layout.addr(sheet, address)].value
    return out


def spec_value(spec, ref):
    """The specification's formula or literal at a logical address. The model-calculated check proves the workbook
    carries the same formula, so lineage is read here rather than from the saved file."""
    import model_workbook as mw
    sheet, address = mw.target(ref, '')
    return spec['sheets'].get(sheet, {}).get('cells', {}).get(address, {}).get('value')


def references(formula, sheet, address):
    """Whether a formula text refers to Sheet!A1 (quoted or not, with or without $)."""
    if not isinstance(formula, str) or not formula.startswith('='):
        return False
    body = re.sub(r'\$', '', formula)
    col, row = re.fullmatch(r'([A-Z]+)(\d+)', address).groups()
    return re.search(rf"(?:'{re.escape(sheet)}'|{re.escape(sheet)})!{col}{row}(?!\d)", body) is not None


def column_of(ref):
    return re.sub(r'\d+$', '', ref.rsplit('!', 1)[-1].replace('$', ''))


def near(a, b, rel=0.005, abs_=0.0):
    return isinstance(a, (int, float)) and isinstance(b, (int, float)) and abs(a - b) <= max(abs(b) * rel, abs_)


def run(study, record, model_check=None, legacy=False):
    """Return (checks, fails) for a study folder and its release record. Fails name the cell, field or file."""
    study = Path(study)
    checks, fails = [], []

    def check(name, ok, detail, cls='integrity'):
        checks.append({'name': name, 'class': cls, 'result': 'pass' if ok else 'fail', 'detail': detail})
        if not ok:
            fails.append(f'{name}: {detail}')

    # 0. An existing release: every file must still be the one that was checked.
    saved = (record.get('fingerprints') or {}).get('files') or {}
    for rel, h in saved.items():
        p = study / rel
        now = sha256(p) if p.exists() else None
        check(f'files-match-release-record:{Path(rel).name}', now == h, 'unchanged since release' if now == h else
              'missing since release' if now is None else 'content differs from the released file; rebuild and re-release')

    spec = json.loads((study / record['spec']).read_text(encoding='utf-8-sig'))
    workbook = study / record['workbook']
    if model_check is None:
        import model_workbook as mw
        model_check = mw.check
    report = model_check(spec, workbook)
    check('model-calculated', report['passed'],
          'specification, formulas and Excel-calculated values agree' if report['passed']
          else 'first issues: ' + json.dumps(report['issues'][:3], ensure_ascii=False))

    b = record['bindings']
    v = cell_values(spec, workbook, b)
    fx = v.get('fx') or 1.0
    price, target = v.get('referencePrice'), v.get('target')
    cutoff = parse_date(record['cutoff'])
    fye = record.get('fiscalYearEnd', 12)
    method = record.get('method')
    check('valuation-method-declared', method in METHODS, f'method {method!r}; allowed {METHODS}')

    # 1. The earnings period behind the target, tied to the cells that carry it.
    if method == 'P/E':
        expect = (v.get('targetMultiple') or 0) * (v.get('forwardEps') or 0) / fx
        check('target-is-multiple-times-forward-eps', near(target, expect),
              f'target {target} against multiple {v.get("targetMultiple")} x EPS {v.get("forwardEps")} / fx {fx} = {expect}')
        declared = str(record.get('epsPeriod', ''))
        if declared.upper().startswith('NTM'):
            n = record.get('ntm') or {}
            try:
                start, end = parse_date(n['start']), parse_date(n['end'])
                comps = n['components']
            except (KeyError, TypeError, ValueError):
                check('ntm-window-declared', False, 'NTM needs ntm.start, ntm.end and ntm.components [{period, weight, eps}]')
            else:
                span_ok = abs((end - (start + timedelta(days=365))).days) <= 3 and abs((start - cutoff).days) <= 31
                check('ntm-window-is-twelve-months-from-cutoff', span_ok,
                      f'window {start} to {end}; must start within a month of the cutoff {cutoff} and run twelve months; no roll to the target date')
                periods = [str(c.get('period')) for c in comps]
                weights = [c.get('weight') for c in comps]
                finite = all(isinstance(w, (int, float)) and w == w and 0 <= w <= 1 for w in weights)
                check('ntm-components-well-formed', finite and len(set(periods)) == len(periods) and all(c.get('eps') and c.get('header') for c in comps),
                      f'periods {periods}, weights {weights}; each component needs a distinct period, a finite weight in [0, 1], an eps cell and a header cell')
                want = ntm_weights(start, fye)
                got = dict(zip(periods, weights))
                weights_ok = finite and abs(sum(weights) - 1) <= 0.005 and set(got) == set(want) and all(abs(got[k] - w) <= 0.005 for k, w in want.items())
                check('ntm-weights-follow-fiscal-calendar', weights_ok,
                      f'declared { {k: round(w, 4) for k, w in got.items()} }; whole-month weights from the fiscal calendar are { {k: round(w, 4) for k, w in want.items()} } (tolerance 0.005, below one month)')
                heads = cell_values(spec, workbook, {f'h{i}': c['header'] for i, c in enumerate(comps) if c.get('header')})
                cells = [str(c.get('eps')) for c in comps]
                tied = len(set(cells)) == len(cells) and all(
                    period_year(heads.get(f'h{i}')) == period_year(c['period']) and column_of(c['header']) == column_of(c['eps']) and c['header'].split('!')[0] == c['eps'].split('!')[0]
                    for i, c in enumerate(comps) if c.get('header'))
                check('ntm-components-bound-to-their-periods', tied,
                      'each component EPS cell sits under a header naming its period, and no cell serves two periods' if tied else
                      f'headers {[heads.get(f"h{i}") for i in range(len(comps))]} for periods {periods}; cells {cells}')
                eps = cell_values(spec, workbook, {c['period']: c['eps'] for c in comps})
                bridge = sum((c['weight'] or 0) * (eps.get(c['period']) or 0) for c in comps)
                check('ntm-bridge-equals-forward-eps', near(v.get('forwardEps'), bridge, 0.005),
                      f'weighted components {bridge} against the bound forward EPS {v.get("forwardEps")} (annual interpolation, an approximation)')
        else:
            fy = fiscal_year_of(cutoff, fye)
            lp = record.get('latestPublished') or {}
            covered = bool(lp.get('coversThirdQuarter'))
            if covered:
                # The evidence must cover the current fiscal year's third quarter: its period names this fiscal year and it
                # was published after that quarter ended and on or before the cutoff. A prior year's quarter does not count.
                try:
                    pub = parse_date(lp['date'])
                    kind, period = str(lp['kind']), str(lp['period'])
                    q3_end = third_quarter_end(fy, fye)
                    ok = period_year(period) == fy and q3_end < pub <= cutoff and bool(kind.strip())
                    why = f'{kind} for {period} dated {pub}: must name FY{fy}, be published after the third quarter ended ({q3_end}) and on or before the cutoff {cutoff}'
                except (KeyError, ValueError, TypeError) as exc:
                    ok, why = False, f'latestPublished needs period, kind and date ({type(exc).__name__}: {exc})'
                check('third-quarter-evidence-covers-current-year', ok, why)
                covered = ok
            rule = forward_period(cutoff, fye, covered)
            check('forward-eps-period', period_year(declared) == period_year(rule),
                  f'declared {declared!r}; house rule at cutoff {cutoff} (year end month {fye}, third quarter covered: {covered}) gives {rule} or NTM; no roll to the target date')
            missing = [k for k in ('forwardEps', 'forwardEpsHeader', 'forwardEpsSource') if k not in b]
            check('required-period-bindings-present', not missing, 'forwardEps, forwardEpsHeader and forwardEpsSource are bound' if not missing else f'missing bindings {missing}')
            if not missing:
                header = str(v.get('forwardEpsHeader') or '')
                same_col = column_of(b['forwardEpsHeader']) == column_of(b['forwardEpsSource']) and b['forwardEpsHeader'].split('!')[0] == b['forwardEpsSource'].split('!')[0]
                check('forward-eps-column-is-declared-period', period_year(header) == period_year(declared) and same_col,
                      f'header {header!r} at {b["forwardEpsHeader"]} must name {declared!r} and sit in the column of the source {b["forwardEpsSource"]}')
                formula = spec_value(spec, b['forwardEps'])
                src_sheet, src_addr = b['forwardEpsSource'].replace("'", '').rsplit('!', 1)
                consumes = b['forwardEps'].replace("'", '') == b['forwardEpsSource'].replace("'", '') or references(formula, src_sheet, src_addr)
                check('valuation-eps-consumes-statement-output', consumes and near(v.get('forwardEps'), v.get('forwardEpsSource'), 1e-6),
                      f'valuation EPS at {b["forwardEps"]} is {formula!r} = {v.get("forwardEps")}; must reference {b["forwardEpsSource"]} = {v.get("forwardEpsSource")}')
    elif method == 'P/B':
        expect = (v.get('targetMultiple') or 0) * (v.get('bookValuePerShare') or 0) / fx
        check('target-is-multiple-times-book', near(target, expect), f'target {target} against multiple x book / fx = {expect}')
    elif method == 'SOTP':
        check('target-is-sum-of-parts', near(target, v.get('sumOfPartsPerShare')), f'target {target} against parts per share {v.get("sumOfPartsPerShare")}')
    elif method == 'dividend-yield':
        expect = (v.get('dps') or 0) / (v.get('targetYield') or 1) / fx
        check('target-is-dps-over-yield', near(target, expect), f'target {target} against DPS / target yield / fx = {expect}')

    # 2. Rating and tier from the unrounded return; the brief payload.
    brief = json.loads((study / record['brief']).read_text(encoding='utf-8'))
    d, meta = brief['decision'], brief['meta']
    if isinstance(price, (int, float)) and isinstance(target, (int, float)) and price:
        ret = target / price - 1
        want = rating_for(ret)
        check('rating-from-unrounded-return', d.get('rating') == want and (v.get('rating') in (None, want)),
              f'price return {ret:.4%} gives {want}; brief says {d.get("rating")!r}, workbook says {v.get("rating")!r}')
        check('tier-on-price-return-only', not any(k in d for k in ('dividendPerShare', 'dividendsToTargetDate')) and
              (d.get('attractiveness') != 'attractive' or ret >= 0.5) and (d.get('attractiveness') != 'decent' or 0.3 <= ret < 0.5),
              f'tier {d.get("attractiveness")!r} on price return {ret:.1%}; dividend yield stays separate')
    check('rating-present', d.get('rating') in RATING, f'rating {d.get("rating")!r}')
    try:
        import render_one_page
        render_one_page.validate(brief)
        check('brief-payload-valid', True, 'render_one_page.validate passed')
    except (ValueError, KeyError, TypeError) as exc:
        check('brief-payload-valid', False, str(exc))
    check('brief-price-matches-model', near(d.get('referencePrice'), price, 0.0005, 0.006), f'brief {d.get("referencePrice")} vs workbook {price}')
    check('brief-target-matches-model', near(d.get('targetPrice'), target, 0.0005, 0.051), f'brief {d.get("targetPrice")} vs workbook {target}')
    if 'dividendYield' in b:
        check('brief-yield-matches-model', near(d.get('dividendYield'), v.get('dividendYield'), 0.0, 0.0006), f'brief {d.get("dividendYield")} vs workbook {v.get("dividendYield")}')
    for key in ('bearTarget', 'bullTarget'):
        if key in b:
            check(f'brief-{key}-matches-model', near(d.get(key), v.get(key), 0.0005, 0.051), f'brief {d.get(key)} vs workbook {v.get(key)}')

    # 3. The decision block as rendered, in the report and the brief HTML the PDFs are printed from.
    for label, paths in (record.get('renders') or {}).items():
        html_rel = paths['html'] if isinstance(paths, dict) else paths
        html = (study / html_rel).read_text(encoding='utf-8', errors='replace')
        got = rendered_decision(html)
        if not got:
            check(f'rendered-decision-found:{label}', False, f'no rating box or decision strip recognised in {html_rel}')
            continue
        ok = got['rating'] == d.get('rating') and near(got['price'], price, 0.0005, 0.006) and near(got['target'], target, 0.0005, 0.051)
        check(f'rendered-decision-matches-model:{label}', ok,
              f'{got["kind"]} shows {got["rating"]} at {got["price"]} with target {got["target"]}; model {d.get("rating")} at {price} with target {target}')

    # 4. Ages at the cutoff. Retrieval and observation ages only: not estimate vintages or the last exchange session.
    price_date = parse_date(record['priceDate'])
    check('price-observation-age', cutoff - timedelta(days=7) <= price_date <= cutoff,
          f'price observed {price_date} for cutoff {cutoff}: on or before the cutoff and within seven days; this is an age check, not a session lookup')
    observed = parse_date(d.get('priceObservation', ''))
    check('brief-price-date-matches-record', observed == price_date, f'brief says {observed}, record says {price_date}')
    if record.get('consensusDate'):
        cd = parse_date(record['consensusDate'])
        check('consensus-retrieval-age', cutoff - timedelta(days=7) <= cd <= cutoff,
              f'consensus retrieved {cd} for cutoff {cutoff}: a retrieval-age check; contributor estimate dates are not validated')
    check('brief-as-of-is-cutoff', parse_date(meta.get('asOf', '')) == cutoff, f'brief asOf {meta.get("asOf")!r} vs cutoff {cutoff}')
    check('currency-agrees', meta.get('currency') == record.get('currency'), f'brief {meta.get("currency")!r} vs record {record.get("currency")!r}')
    check('security-agrees', str(record.get('security', '')) in str(meta.get('security', '')), f'brief {meta.get("security")!r} vs record {record.get("security")!r}')

    # 5. The printed brief and the wording regression list.
    if record.get('briefPdf') and (study / record['briefPdf']).exists():
        try:
            n = page_count(study / record['briefPdf'])
            check('brief-is-one-page', n == 1, f'{n} page(s)')
        except Exception as exc:  # noqa: BLE001 - an unreadable PDF is a failed check, not a crash
            check('brief-is-one-page', False, f'unreadable PDF: {type(exc).__name__}: {exc}')
    allowed = {c.lower() for c in record.get('contacts', [])}
    banned = [p.lower() for p in BANNED_PHRASES] + [p.lower() for p in record.get('bannedText', [])]
    for rel in record.get('deliverables', []):
        path = study / rel
        if path.suffix.lower() not in ('.pdf', '.html', '.htm') or not path.exists():
            continue
        try:
            text = text_of(path)
        except Exception as exc:  # noqa: BLE001
            check(f'authorship-clean:{path.name}', False, f'unreadable file: {type(exc).__name__}: {exc}')
            continue
        low = text.lower()
        hits = [p for p in banned if p in low]
        emails = [e for e in EMAIL.findall(text) if e.lower() not in allowed]
        bylines = [] if record.get('byline') else BYLINE.findall(text)
        check(f'authorship-clean:{path.name}', not (emails or bylines),
              'no unapproved email address or byline marker' if not (emails or bylines) else f'emails {emails[:3]}; byline markers {bylines[:3]}')
        check(f'wording-clean:{path.name}', not hits, 'none of the banned phrases' if not hits else f'banned {hits}', cls='wording')
    if legacy:
        check('legacy-review-scope', True, 'Historical integrity verification only; no current publication-review assurance', cls='scope')
    else:
        import publication_review as pr
        for result in pr.check(study, record, spec, workbook):
            checks.append(result)
            if result['result'] != 'pass':
                fails.append(result['name'] + ': ' + result['detail'])
    return checks, fails


def fingerprints(study, record):
    study = Path(study)
    files = [record['workbook'], record['spec'], record['brief']] + list(record.get('deliverables', []))
    for paths in (record.get('renders') or {}).values():
        files += [paths['html'], paths['pdf']] if isinstance(paths, dict) else [paths]
    review = record.get('review', 'evidence/draft-review.json')
    if (study / review).is_file():
        files.append(review)
    out = {rel: sha256(study / rel) for rel in dict.fromkeys(files) if (study / rel).exists()}
    return {'files': out, 'skills': skills_fingerprint(), 'git': git_state(SKILLS.parent)}


def main(argv=None):
    args = argv or sys.argv[1:]
    legacy = '--legacy' in args
    study = Path(next(a for a in args if a != '--legacy'))
    try:
        record = json.loads((study / 'deliverables' / 'release.json').read_text(encoding='utf-8'))
        checks, fails = run(study, record, legacy=legacy)
        out = {'status': 'failed' if fails else 'legacy-verified' if legacy else 'validated', 'scope': SCOPE, 'checks': checks}
    except Exception as exc:  # noqa: BLE001 - a crash is a failed verification, reported as such
        out = {'status': 'failed', 'error': f'{type(exc).__name__}: {exc}', 'checks': []}
        fails = [out['error']]
    print(json.dumps(out, indent=1, ensure_ascii=False))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
