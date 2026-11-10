"""Release check: the objective slips it catches, each with a positive and a negative case, and the package path."""
from pathlib import Path
import importlib.util, json, shutil, subprocess, sys, tempfile, unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'report-layout/scripts'
sys.path.insert(0, str(SCRIPTS))
spec_ = importlib.util.spec_from_file_location('release_check', SCRIPTS / 'release_check.py')
rc = importlib.util.module_from_spec(spec_); sys.modules['release_check'] = rc; spec_.loader.exec_module(rc)
import model_workbook as mw  # noqa: E402  (path added by release_check)
import report_layout as rl  # noqa: E402


def spec():
    return {'sheets': {
        'Statements': {'lastColumn': 'I', 'cells': {
            'B5': {'value': 'Period'}, 'H5': {'value': 'FY2026E'}, 'I5': {'value': 'FY2027E'},
            'B43': {'value': 'Recurring EPS'}, 'H43': {'value': 5.0, 'kind': 'input'}, 'I43': {'value': 5.55, 'kind': 'input'}}},
        'Valuation': {'lastColumn': 'D', 'cells': {
            'B2': {'value': 'Price'}, 'D2': {'value': 79.25, 'kind': 'input'},
            'B3': {'value': 'FX'}, 'D3': {'value': 0.85, 'kind': 'input'},
            'B4': {'value': 'EPS FY2027E'}, 'D4': {'value': '=Statements!I43'},
            'B5': {'value': 'Multiple'}, 'D5': {'value': 14.9, 'kind': 'input'},
            'B6': {'value': 'Target'}, 'D6': {'value': '=D5*D4/D3'},
            'B7': {'value': 'Yield'}, 'D7': {'value': 0.0355, 'kind': 'input'},
            'B8': {'value': 'Rating'}, 'D8': {'value': '=IF(D6/D2-1>0.1,"Buy",IF(D6/D2-1<-0.1,"Sell","Hold"))'},
            'B9': {'value': 'Book value per share'}, 'D9': {'value': 40.0, 'kind': 'input'},
            'B10': {'value': 'P/B target'}, 'D10': {'value': '=D11*D9/D3'},
            'B11': {'value': 'P/B multiple'}, 'D11': {'value': 2.0668, 'kind': 'input'},
            'B12': {'value': 'Sum of parts per share'}, 'D12': {'value': 97.26, 'kind': 'input'},
            'B13': {'value': 'DPS'}, 'D13': {'value': 3.0, 'kind': 'input'},
            'B14': {'value': 'Target yield'}, 'D14': {'value': 0.03629, 'kind': 'input'},
            'B15': {'value': 'Yield target'}, 'D15': {'value': '=D13/D14/D3'},
            'B16': {'value': 'EPS FY2026E'}, 'D16': {'value': '=Statements!H43'},
            'B17': {'value': 'NTM EPS'}, 'D17': {'value': '=D16*2/12+D4*10/12'},
            'B18': {'value': 'NTM target'}, 'D18': {'value': '=D5*D17/D3'},
            'B19': {'value': 'FY2028E'}, 'D19': {'value': 6.0, 'kind': 'input'},
            'B20': {'value': 'Typed EPS, same value as the statement'}, 'D20': {'value': 5.55, 'kind': 'input'},
            'D21':{'value':62.9},'D22':{'value':118.4},'D23':{'value':8267.1},'D24':{'value':100}}}},
        'outputs': {'target': 'Valuation!D6'}}


def brief(**over):
    d = {'rating': 'Buy', 'referencePrice': 79.25, 'priceObservation': '5 Nov 2026 close (FactSet)', 'targetPrice': 97.3,
         'targetDate': 'Nov 2027', 'attractiveness': 'unattractive', 'newMoney': 'no', 'bearTarget': 62.9, 'bullTarget': 118.4,
         'keyMetrics': ['12.1x FY27E P/E', '3.6% dividend yield'], 'dividendYield': 0.0355}
    d.update(over)
    return {'schemaVersion': '2.0.0', 'meta': {'issuer': 'Example', 'security': '2020.HK (HKD counter)', 'currency': 'HKD', 'asOf': '6 November 2026'},
            'headline': 'Example headline', 'decision': d,
            'sections': [{'id': 'case', 'title': 'Case', 'sourceIds': [], 'paragraphs': ['We forecast recurring EPS growth of 7%.']}],
            'sources': [], 'links': []}


def record(**over):
    r = {'cutoff': '2026-11-06', 'researchMode': 'initiation', 'fiscalYearEnd': 12, 'priceDate': '2026-11-05', 'consensusDate': '2026-11-06', 'security': '2020.HK',
         'currency': 'HKD', 'method': 'P/E', 'epsPeriod': 'FY2027E',
         'latestPublished': {'period': '3Q26', 'kind': 'operating update', 'date': '2026-10-21', 'coversThirdQuarter': True},
         'spec': 'model/spec.json', 'workbook': 'deliverables/model.xlsx', 'brief': 'deliverables/brief.json',
         'deliverables': ['deliverables/report.html'], 'renders': {'report': 'deliverables/report.html', 'brief': 'deliverables/brief.html'},
         'bindings': {'referencePrice': 'Valuation!D2', 'fx': 'Valuation!D3', 'forwardEps': 'Valuation!D4', 'targetMultiple': 'Valuation!D5',
                      'target': 'Valuation!D6', 'dividendYield': 'Valuation!D7', 'rating': 'Valuation!D8',
                      'bearTarget':'Valuation!D21','bullTarget':'Valuation!D22',
                      'forwardEpsSource': 'Statements!I43', 'forwardEpsHeader': 'Statements!I5'}}
    r.update(over)
    return r


def report_html(rating='Buy', price='HK$79.25', target='HK$97.3'):
    return (f'<html><body><div data-financial-summary="true"></div><div class="rbox"><div class="rating" style="color:#2E7D4F">{rating}</div><table class="kv">'
            f'<tr><td>Price, 5 Nov 2026</td><td>{price}</td></tr><tr><td>12-month target</td><td><b>{target}</b></td></tr>'
            f'<tr><td>Price return</td><td><b>+22.8%</b></td></tr></table></div><p>We forecast 7% growth. Internal use only.</p></body></html>')


def brief_html(rating='Buy', price='HK$79.25', target='HK$97.3'):
    import render_one_page
    p,t=float(price.replace('HK$','')),float(target.replace('HK$',''))
    call=rc.rating_for(rc.price_return(t,p))
    payload=brief(rating=call,referencePrice=p,targetPrice=t)
    return render_one_page.render(payload)[0].replace(call+' |',rating+' |')


def passing_check(s, path):
    return {'passed': True, 'issues': [], 'workbookSHA256': rc.sha256(path)}


def complete_review(study):
    """A synthetic reviewer test double, not an automated judgment or a production completion shortcut."""
    path = Path(study) / 'evidence/draft-review.json'
    packet = json.loads(path.read_text(encoding='utf-8'))
    packet['reviewer'] = {'id': 'synthetic-test-reviewer', 'mode': 'independent-agent', 'context': 'fresh'}
    packet['handoff']['status'] = 'complete'
    packet['handoff']['summary'] = 'Synthetic fixture reviewed for this isolated regression.'
    packet['handoff']['claims'] = [{'id': 'fixture', 'text': 'The fixture assumes its stated target.', 'material': True,
        'basis': 'assumption', 'sourceIds': [], 'calculation': None, 'rationale': 'Stipulated synthetic fixture, not investment evidence.'}]
    for check in packet['handoff']['checks']:
        check.update(result='pass', detail='Synthetic reviewer test double: isolated fixture verified.')
    for kind in packet['coverage']:
        packet['coverage'][kind] = {'status': 'not-applicable', 'reason': 'This isolated fixture has no such financial claim.', 'assertionIds': []}
    for kind in ('cash-coverage','normalized-ratio','financing'):
        packet['coverage'][kind].update(applicability='not-applicable',claimIds=[])
    frozen = json.loads((Path(study) / packet['snapshot']['path'] / 'manifest.json').read_text())['releaseRecord']
    if frozen['method'] == 'P/E':
        b = frozen['bindings']
        packet['valuationBasis'] = {'status': 'checked', 'reason': '', 'cases': [
            {'id': name, 'period': frozen['epsPeriod'], 'benchmarkPeriod': frozen['epsPeriod'],
             'metricRef': b['forwardEps'], 'multipleRef': b['targetMultiple'], 'targetRef': b['target'], 'fxRef': b.get('fx'),
             'sourceIds': [packet['handoff']['sources'][0]['id']], 'rationale': 'Stipulated same-period synthetic fixture.'}
            for name in ('bear', 'base', 'bull')]}
    else:
        packet['valuationBasis'] = {'status': 'not-applicable', 'reason': 'The primary method does not use P/E.', 'cases': []}
    packet['coverage']['brief-fidelity'] = {'status': 'checked', 'items': [{
        'claimId': 'fixture', 'reportLocation': 'Synthetic report decision', 'briefLocation': 'Synthetic brief decision',
        'qualification': 'Stipulated same-period target only; this is not a real research review.',
        'assessment': 'Both decision blocks agree on the fixture assumptions.'}]}
    from review_attempts import begin
    begin(study, frozen, reviewer=packet['reviewer']['id'])
    path.write_text(json.dumps(packet), encoding='utf-8')
    return packet


class ReleaseCheckTests(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp()); self.addCleanup(shutil.rmtree, self.dir, True)
        (self.dir / 'model').mkdir(); (self.dir / 'deliverables').mkdir()
        (self.dir / 'model/spec.json').write_text(json.dumps(spec()), encoding='utf-8')
        mw.build(spec(), self.dir / 'deliverables/model.xlsx')
        from openpyxl import load_workbook
        w = load_workbook(self.dir / 'deliverables/model.xlsx')
        self.values = mw.calculate(spec())['Model']['cells']
        for ref, v in self.values.items():  # stand in for Excel's saved results
            sheet, address = ref.split('!'); w[sheet][address].value = v
        w.save(self.dir / 'deliverables/model.xlsx')
        self.write_brief(brief())
        self.write('deliverables/report.html', report_html())
        self.write('deliverables/brief.html', brief_html())
        # A current publication also needs the reusable decision checkpoint.
        import decision_record
        (self.dir / 'evidence').mkdir(exist_ok=True)
        self.write('evidence/decision.json',json.dumps(decision_record.synchronize(self.dir,record(),spec(),{
            'triggerCoverage':{'status':'not-applicable','reason':'This isolated fixture publishes no numerical rating triggers.','testIds':[]},
            'triggerTests':[]})))
        # Explicit synthetic reviewer double for the pre-writing checkpoint; never production approval.
        import model_review
        path=model_review.prepare(self.dir,'model/spec.json','deliverables/model.xlsx',[],record()['security'],record()['cutoff'])
        model_review.begin(self.dir,'synthetic-model-reader')
        packet=json.loads(path.read_text()); h=packet['handoff']; h['status']='complete'
        h['summary']='Synthetic pre-writing review for an isolated regression.'
        h['claims']=[{'id':'model-fixture','text':'Original synthetic assumptions are stipulated.','material':True,'basis':'assumption',
                      'sourceIds':[],'calculation':None,'rationale':'Synthetic test double only.'}]
        for c in h['checks']: c.update(result='pass',detail='Synthetic test fixture only.')
        path.write_text(json.dumps(packet),encoding='utf-8')

    def write(self, rel, text):
        (self.dir / rel).write_text(text, encoding='utf-8')

    def write_brief(self, payload):
        self.write('deliverables/brief.json', json.dumps(payload))

    def fails(self, rec=None):
        # These cases isolate the original integrity checks. Review/freshness policy has dedicated regressions.
        return rc.run(self.dir, rec or record(), model_check=passing_check, legacy=True)[1]

    def assert_fails(self, prefix, rec=None):
        f = self.fails(rec)
        self.assertTrue(any(x.startswith(prefix) for x in f), f'{prefix} not among {f}')

    # ---- the earnings period
    def test_forward_period_switches_only_after_third_quarter_evidence(self):
        self.assertEqual(rc.forward_period('2026-11-06', 12, True), 'FY2027E')    # past Q3 and covered: next year
        self.assertEqual(rc.forward_period('2026-11-06', 12, False), 'FY2026E')   # past Q3 end, nothing published: current year
        self.assertEqual(rc.forward_period('2026-07-15', 12, True), 'FY2026E')    # inside the year
        self.assertEqual(rc.forward_period('2026-11-06', 6, True), 'FY2027E')     # June year end: FY2027 Q3 ends Mar 2027
        self.assertEqual(rc.forward_period('2027-04-10', 6, True), 'FY2028E')
        self.assertEqual(rc.forward_period('2026-11-06', 3, True), 'FY2027E')     # March year end: Q3 ends Dec 2026

    def test_clean_study_passes(self):
        self.assertEqual(self.fails(), [])

    def test_target_rolled_to_the_target_date_fails(self):
        self.assert_fails('forward-eps-period', record(epsPeriod='FY2028E'))

    def test_next_year_needs_third_quarter_evidence_for_the_current_year(self):
        self.assert_fails('forward-eps-period', record(latestPublished={'period': '1H26', 'kind': 'results', 'date': '2026-08-26', 'coversThirdQuarter': False}))
        self.assert_fails('third-quarter-evidence-covers-current-year', record(latestPublished={'period': '3Q26', 'kind': 'results', 'date': '2026-11-20', 'coversThirdQuarter': True}))   # after the cutoff
        self.assert_fails('third-quarter-evidence-covers-current-year', record(latestPublished={'period': '3Q2025', 'kind': 'results', 'date': '2025-10-21', 'coversThirdQuarter': True}))  # last year's quarter
        self.assert_fails('third-quarter-evidence-covers-current-year', record(latestPublished={'period': '3Q26', 'kind': 'results', 'date': '2026-09-15', 'coversThirdQuarter': True}))   # before the quarter ended
        self.assert_fails('third-quarter-evidence-covers-current-year', record(latestPublished={'coversThirdQuarter': True}))                                                             # partial declaration

    def test_annual_period_bindings_are_mandatory_and_carry_lineage(self):
        b = dict(record()['bindings'], forwardEpsHeader='Valuation!B19')   # a cell reading FY2028E, in another column
        self.assert_fails('forward-eps-column-is-declared-period', record(bindings=b))
        b = dict(record()['bindings'], forwardEpsSource='Statements!H43')  # header column I, source column H
        self.assert_fails('forward-eps-column-is-declared-period', record(bindings=b))
        self.assert_fails('valuation-eps-consumes-statement-output', record(bindings=b))
        b = dict(record()['bindings'], forwardEps='Valuation!D20')         # same value, typed in, no reference to the statement
        self.assert_fails('valuation-eps-consumes-statement-output', record(bindings=b))
        for key in ('forwardEpsHeader', 'forwardEpsSource'):
            b = dict(record()['bindings']); b.pop(key)
            self.assert_fails('required-period-bindings-present', record(bindings=b))

    def ntm_record(self, **over):
        n = {'start': '2026-11-06', 'end': '2027-11-05', 'components': [{'period': 'FY2026E', 'weight': 2 / 12, 'eps': 'Statements!H43', 'header': 'Statements!H5'},
                                                                       {'period': 'FY2027E', 'weight': 10 / 12, 'eps': 'Statements!I43', 'header': 'Statements!I5'}]}
        n.update(over)
        b = dict(record()['bindings'], forwardEps='Valuation!D17', target='Valuation!D18'); b.pop('forwardEpsHeader'); b.pop('forwardEpsSource')
        t = round(self.values['Valuation!D18'], 1)
        self.write_brief(brief(targetPrice=t)); self.write('deliverables/report.html', report_html(target=f'HK${t}')); self.write('deliverables/brief.html', brief_html(target=f'HK${t}'))
        return record(epsPeriod='NTM', ntm=n, bindings=b)

    def test_ntm_bridge_passes_when_window_weights_and_components_agree(self):
        self.assertEqual(self.fails(self.ntm_record()), [])

    def test_ntm_rolled_window_wrong_end_or_wrong_weights_fail(self):
        self.assert_fails('ntm-window-is-twelve-months-from-cutoff', self.ntm_record(start='2027-11-06', end='2028-11-05'))
        self.assert_fails('ntm-window-is-twelve-months-from-cutoff', self.ntm_record(end='2028-11-05'))
        comp = lambda w1, w2, e1='Statements!H43', e2='Statements!I43', h1='Statements!H5', h2='Statements!I5': [  # noqa: E731
            {'period': 'FY2026E', 'weight': w1, 'eps': e1, 'header': h1}, {'period': 'FY2027E', 'weight': w2, 'eps': e2, 'header': h2}]
        self.assert_fails('ntm-weights-follow-fiscal-calendar', self.ntm_record(components=comp(0.5, 0.5)))
        self.assert_fails('ntm-weights-follow-fiscal-calendar', self.ntm_record(components=comp(3 / 12, 9 / 12)))    # one month out
        self.assert_fails('ntm-components-bound-to-their-periods', self.ntm_record(components=comp(2 / 12, 10 / 12, e1='Statements!I43')))   # one cell, two labels
        self.assert_fails('ntm-components-bound-to-their-periods', self.ntm_record(components=comp(2 / 12, 10 / 12, h1='Statements!I5')))    # header names the wrong year
        self.assert_fails('ntm-components-well-formed', self.ntm_record(components=[{'period': 'FY2026E', 'weight': 2 / 12, 'eps': 'Statements!H43', 'header': 'Statements!H5'},
                                                                                   {'period': 'FY2026E', 'weight': 10 / 12, 'eps': 'Statements!I43', 'header': 'Statements!I5'}]))
        self.assert_fails('ntm-components-well-formed', self.ntm_record(components=comp(-2 / 12, 14 / 12)))
        self.assert_fails('ntm-bridge-equals-forward-eps', self.ntm_record(components=comp(2 / 12, 10 / 12, e1='Valuation!D19', h1='Valuation!B19')))
        self.assert_fails('ntm-window-declared', record(epsPeriod='NTM'))

    # ---- the other valuation methods
    def test_price_to_book_sum_of_parts_and_dividend_yield_branches(self):
        base = record()['bindings']
        pb = dict(base, target='Valuation!D10', targetMultiple='Valuation!D11', bookValuePerShare='Valuation!D9')
        self.assertEqual(self.fails(record(method='P/B', bindings=pb)), [])
        self.assert_fails('target-is-multiple-times-book', record(method='P/B', bindings=dict(pb, targetMultiple='Valuation!D5')))
        sotp = dict(base, target='Valuation!D12', shares='Valuation!D24')
        parts=[{'id':'business','valueRef':'Valuation!D23','rationale':'Original synthetic aggregate owner value.'}]
        self.assertEqual(self.fails(record(method='SOTP', bindings=sotp,valuationParts=parts)), [])
        self.assert_fails('target-is-method-bridge', record(method='SOTP', bindings=sotp,valuationParts=[dict(parts[0],valueRef='Valuation!D12')]))
        dy = dict(base, target='Valuation!D15', dps='Valuation!D13', targetYield='Valuation!D14')
        self.assertEqual(self.fails(record(method='dividend-yield', bindings=dy)), [])
        self.assert_fails('target-is-dps-over-yield', record(method='dividend-yield', bindings=dict(dy, dps='Valuation!D9')))
        self.assert_fails('valuation-method-declared', record(method='DCF'))

    # ---- decision block, dates, identity
    def test_stale_brief_target_fails(self):
        self.write_brief(brief(targetPrice=95.0)); self.assert_fails('brief-target-matches-model')

    def test_rendered_decision_block_must_match_the_model(self):
        self.write('deliverables/report.html', report_html(target='HK$999.00', rating='Sell')); self.assert_fails('rendered-decision-matches-model:report')
        self.write('deliverables/report.html', report_html())
        self.write('deliverables/brief.html', brief_html(price='HK$70.00')); self.assert_fails('rendered-decision-matches-model:brief')
        self.write('deliverables/brief.html', '<html><body>no decision block</body></html>'); self.assert_fails('rendered-decision-found:brief')

    def test_rating_must_follow_the_unrounded_return(self):
        self.write_brief(brief(rating='Hold')); self.assert_fails('rating-from-unrounded-return')

    def test_dividend_inside_the_tier_fails(self):
        self.write_brief(brief(attractiveness='decent'))   # 22.8% price return is below the decent tier
        f = self.fails(); self.assertTrue(any(x.startswith('tier-on-price-return-only') or x.startswith('brief-payload-valid') for x in f), f)

    def test_price_and_consensus_ages(self):
        self.assert_fails('price-observation-age', record(priceDate='2026-11-07'))
        self.assert_fails('price-observation-age', record(priceDate='2026-10-20'))
        self.assert_fails('consensus-retrieval-age', record(consensusDate='2026-10-01'))
        self.write_brief(brief(priceObservation='6 Nov 2026 close'))   # a Monday cutoff accepts Friday's close
        f = self.fails(record(cutoff='2026-11-09', priceDate='2026-11-06'))
        self.assertFalse(any(x.startswith('price-observation-age') or x.startswith('brief-price-date') for x in f), f)

    # ---- authorship and wording
    def test_unapproved_email_and_byline_fail_but_approved_contact_passes(self):
        self.write('deliverables/report.html', report_html() + '<p>Prepared by someone@example.com. Nobody publishes what buyers think.</p>')
        f = self.fails()
        self.assertTrue(any(x.startswith('authorship-clean') and 'someone@example.com' in x for x in f), f)
        self.assertTrue(any(x.startswith('wording-clean') and 'nobody publishes' in x for x in f), f)
        self.write('deliverables/report.html', report_html() + '<p>Prepared by approved@example.com.</p>')
        self.assertEqual(self.fails(record(contacts=['approved@example.com'], byline='approved')), [])
        self.assert_fails('authorship-clean', record(byline='approved'))   # byline allowed, the email is not listed

    def test_corrupt_pdf_is_a_failed_check_not_a_crash(self):
        self.write('deliverables/brief.pdf', '%PDF-1.4 not a real pdf')
        f = self.fails(record(briefPdf='deliverables/brief.pdf', deliverables=['deliverables/report.html', 'deliverables/brief.pdf']))
        self.assertTrue(any(x.startswith('brief-is-one-page') and 'unreadable' in x for x in f), f)
        self.assertTrue(any(x.startswith('authorship-clean:brief.pdf') and 'unreadable' in x for x in f), f)
        r = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(SCRIPTS / 'release_check.py'), str(self.dir / 'missing')], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1); self.assertEqual(json.loads(r.stdout)['status'], 'failed')

    def test_uncalculated_workbook_fails(self):
        f = rc.run(self.dir, record(), model_check=lambda s, p: {'passed': False, 'issues': [{'cell': 'Valuation!D6', 'reason': 'no calculated value saved'}]})[1]
        self.assertTrue(any(x.startswith('model-calculated') for x in f), f)

    # ---- package: print, bind, zip, and failure handling
    def package(self, **over):
        rec = {k: v for k, v in record(**over).items() if k not in ('deliverables', 'renders')}
        args = (self.dir, self.dir / 'deliverables/pkg.zip', self.dir / 'deliverables/report.html', self.dir / 'deliverables/brief.html',
                [self.dir / 'deliverables/model.xlsx'])
        try:
            return rl.package(*args, **rec)
        except SystemExit:
            saved = json.loads((self.dir / 'deliverables/release.json').read_text())
            if saved['status'] != 'awaiting-review':
                raise
            # Synthetic test double for an actual completed fresh review; never used by production packaging.
            complete_review(self.dir)
            return rl.package(*args, **rec)

    def test_revision_rechecks_with_current_bindings_not_the_saved_record(self):
        import publication_review as pr
        from unittest.mock import patch
        saved = (rl.print_pdf, rc.page_count, rc.text_of, rc.run)
        rl.print_pdf = lambda h, p: (Path(p).write_bytes(b'%PDF-fake ' + Path(h).read_bytes()), Path(p))[1]
        rc.page_count = lambda p: 1
        rc.text_of = lambda p: Path(p).read_text(encoding='utf-8', errors='replace')
        rc.run = lambda study, rec, model_check=None, **kw: saved[3](study, rec, model_check=passing_check, **kw)
        try:
            rec = {k: v for k, v in record().items() if k not in ('deliverables', 'renders')}
            args = (self.dir, self.dir / 'deliverables/pkg.zip', self.dir / 'deliverables/report.html',
                    self.dir / 'deliverables/brief.html', [self.dir / 'deliverables/model.xlsx'])
            with self.assertRaises(SystemExit): rl.package(*args, **rec)          # round 1 draft
            path = self.dir / 'deliverables/release.json'
            stale = json.loads(path.read_text(encoding='utf-8'))
            stale['bindings']['forwardEpsSource'] = 'Statements!H43'          # a binding left from an earlier draft
            path.write_text(json.dumps(stale), encoding='utf-8')
            with patch.object(sys, 'argv', ['publication_review.py', 'prepare', str(self.dir), '--revise']):
                with self.assertRaisesRegex(ValueError, 'integrity checks'):
                    pr.main()
            self.assertEqual(json.loads(path.read_text(encoding='utf-8'))['status'], 'failed')
            with self.assertRaises(SystemExit) as cm: rl.package(*args, revise=True, **rec)   # adapter, current bindings
            self.assertIn('Draft PDFs ready', str(cm.exception))
            current = json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(current['status'], 'awaiting-review')
            self.assertEqual(current['bindings']['forwardEpsSource'], 'Statements!I43')
            self.assertTrue(current['checks'])
            packet = json.loads((self.dir / pr.DEFAULT_PATH).read_text(encoding='utf-8'))
            self.assertEqual((packet['round'], packet['draftVersion']), (1, 2))
            with self.assertRaises(SystemExit): rl.package(*args, revise=True, **rec)  # another draft, still no review started
            self.assertEqual(json.loads(path.read_text(encoding='utf-8'))['status'], 'awaiting-review')
        finally:
            rl.print_pdf, rc.page_count, rc.text_of, rc.run = saved

    def test_package_prints_binds_and_fails_safely(self):
        saved = (rl.print_pdf, rc.page_count, rc.text_of, rc.run)
        rl.print_pdf = lambda h, p: (Path(p).write_bytes(b'%PDF-fake ' + Path(h).read_bytes()), Path(p))[1]   # no Chrome in tests
        rc.page_count = lambda p: 1
        rc.text_of = lambda p: Path(p).read_text(encoding='utf-8', errors='replace')
        rc.run = lambda study, rec, model_check=None, **kw: saved[3](study, rec, model_check=passing_check, **kw)
        try:
            out = self.package()
            self.assertEqual(out['status'], 'validated')
            self.assertTrue((self.dir / 'deliverables/pkg.zip').exists())
            files = out['fingerprints']['files']
            self.assertIn('deliverables/report.pdf', files); self.assertIn('deliverables/report.html', files); self.assertIn('deliverables/model.xlsx', files)
            self.assertEqual(out['renders']['brief'], {'html': 'deliverables/brief.html', 'pdf': 'deliverables/brief.pdf'})
            # an existing release: a changed PDF (or a prior PDF beside current HTML) no longer matches the record
            reviewed_pdf = (self.dir / 'deliverables/report.pdf').read_bytes()
            (self.dir / 'deliverables/report.pdf').write_bytes(b'%PDF-prior')
            f = rc.run(self.dir, json.loads((self.dir / 'deliverables/release.json').read_text(encoding='utf-8')))[1]
            self.assertTrue(any(x.startswith('files-match-release-record:report.pdf') for x in f), f)
            (self.dir / 'deliverables/report.pdf').write_bytes(reviewed_pdf)
            # a failing check after an earlier success: no zip, failed record
            self.write_brief(brief(targetPrice=95.0))
            with self.assertRaises(SystemExit): self.package()
            self.assertFalse((self.dir / 'deliverables/pkg.zip').exists())
            self.assertEqual(json.loads((self.dir / 'deliverables/release.json').read_text(encoding='utf-8'))['status'], 'failed')
            # an exception after an earlier success: still no zip, failed record naming the error
            self.write_brief(brief()); self.package(); self.assertTrue((self.dir / 'deliverables/pkg.zip').exists())
            (self.dir / 'deliverables/brief.json').unlink()
            with self.assertRaises(SystemExit) as cm: self.package()
            self.assertIn('FileNotFoundError', str(cm.exception))
            self.assertFalse((self.dir / 'deliverables/pkg.zip').exists())
            rec = json.loads((self.dir / 'deliverables/release.json').read_text(encoding='utf-8'))
            self.assertEqual(rec['status'], 'failed'); self.assertIn('FileNotFoundError', rec['error'])
            # a zip-write failure after an earlier success: no zip, no partial, failed record naming OSError
            (self.dir / 'deliverables/brief.moved.json').rename(self.dir / 'deliverables/brief.json') if (self.dir / 'deliverables/brief.moved.json').exists() else self.write_brief(brief())
            self.package(); self.assertTrue((self.dir / 'deliverables/pkg.zip').exists())
            import zipfile
            real = zipfile.ZipFile
            def broken(*a, **k): raise OSError('disk full')
            zipfile.ZipFile = broken
            try:
                with self.assertRaises(SystemExit) as cm: self.package()
            finally:
                zipfile.ZipFile = real
            self.assertIn('OSError', str(cm.exception))
            self.assertFalse((self.dir / 'deliverables/pkg.zip').exists()); self.assertFalse((self.dir / 'deliverables/pkg.partial.zip').exists())
            rec = json.loads((self.dir / 'deliverables/release.json').read_text(encoding='utf-8'))
            self.assertEqual(rec['status'], 'failed'); self.assertIn('OSError', rec['error'])
        finally:
            rl.print_pdf, rc.page_count, rc.text_of, rc.run = saved


if __name__ == '__main__':
    unittest.main()
