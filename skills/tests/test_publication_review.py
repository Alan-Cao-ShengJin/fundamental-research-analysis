"""Real release-boundary and financial-definition regressions; no LLM quality scores are asserted."""
import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'report-layout/scripts'))
import publication_review as pr
import report_layout as rl
import test_release_check as fixtures
rc, complete_review, record, spec = fixtures.rc, fixtures.complete_review, fixtures.record, fixtures.spec


class PublicationReviewTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.ReleaseCheckTests('test_clean_study_passes')
        self.f.setUp(); self.addCleanup(self.f.doCleanups)
        self.dir, self.rec = self.f.dir, record()

    def prepared(self, complete=True):
        pr.prepare(self.dir, self.rec)
        if complete:
            return complete_review(self.dir)
        return json.loads((self.dir / pr.DEFAULT_PATH).read_text())

    def write_packet(self, packet):
        (self.dir / pr.DEFAULT_PATH).write_text(json.dumps(packet), encoding='utf-8')

    def failures(self):
        return [c['name'] for c in pr.check(self.dir, self.rec, spec(), self.dir / self.rec['workbook']) if c['result'] == 'fail']

    def test_no_review_and_unperformed_review_block(self):
        self.assertIn('draft-review-readable', self.failures())
        self.prepared(False)
        self.assertIn('draft-review-complete', self.failures())
        self.assertIn('draft-review-required-checks', self.failures())

    def test_completed_fresh_review_passes_but_stale_draft_does_not(self):
        self.prepared(); self.assertEqual(self.failures(), [])
        self.f.write('deliverables/report.html', 'Changed investment argument')
        self.assertIn('draft-review-files-current', self.failures())

    def test_formatted_prose_span_needs_a_source_or_calculation_binding(self):
        html=fixtures.report_html()+rl.bound_measure('unbound',.12,'FY2031E','ratio',style='percent')
        self.f.write('deliverables/report.html',html)
        self.prepared()
        self.assertIn('rendered-measures-covered:deliverables/report.html',self.failures())

    def test_decision_is_automatically_frozen_and_cannot_change_after_review(self):
        p=self.prepared()
        self.assertIn('evidence/decision.json',p['reviewedFiles'])
        self.f.write('evidence/decision.json','{"changed":"trigger"}')
        self.assertIn('draft-review-files-current',self.failures())

    def test_general_bound_prose_passes_the_full_review_check_and_wrong_text_fails(self):
        html=fixtures.report_html()+rl.bound_measure('yield',.0355,'FY2027E','ratio',style='percent',decimals=1)
        self.f.write('deliverables/report.html',html)
        p=self.prepared()
        p['claimAssertions']=[{'id':'yield-display','kind':'rendered-measure','claimId':'fixture',
            'location':'Report yield paragraph','sourceIds':['file-0'],'rationale':'Synthetic model ratio on the declared period.',
            'values':[{'model':'Valuation!D7'}], 'displays':[{'document':'deliverables/report.html','id':'yield',
                'period':'FY2027E','unit':'ratio','style':'percent','decimals':1}]}]
        p['coverage']['claim-support']={'status':'checked','assertionIds':['yield-display']}
        self.write_packet(p)
        self.assertEqual(self.failures(),[])
        tampered=html.replace('data-order="input">','data-order="input">-')
        self.assertNotEqual(tampered,html)
        self.f.write('deliverables/report.html',tampered)
        failures=self.failures()
        self.assertIn('claim-assertion:yield-display',failures)
        self.assertIn('draft-review-files-current',failures)

    def test_changed_model_and_omitted_dependencies_do_not_silently_pass(self):
        p = self.prepared()
        del p['reviewedFiles'][self.rec['spec']]
        self.write_packet(p)
        self.assertIn('draft-review-inputs-covered', self.failures())
        self.f.write('deliverables/model.xlsx', 'changed bytes')
        self.assertIn('draft-review-files-current', self.failures())

    def test_self_review_or_unresolved_blocker_is_not_independent_completion(self):
        p = self.prepared(); p['reviewer']['mode'] = 'self'; self.write_packet(p)
        self.assertIn('draft-review-reader', self.failures())
        p['reviewer']['mode'] = 'human'
        p['handoff']['criticalUnknowns'] = ['Known material source contradiction remains unresolved']
        self.write_packet(p)
        self.assertIn('draft-review-complete', self.failures())

    def test_coverage_must_be_decided_and_rounds_are_bounded(self):
        p = self.prepared(False)
        self.assertIn('financial-coverage:cash-coverage', self.failures())
        pr.prepare(self.dir, self.rec, revise=True)
        self.assertTrue(list((self.dir / 'evidence').glob('draft-review.round1.*.json')))
        p2 = json.loads((self.dir / pr.DEFAULT_PATH).read_text())
        self.assertEqual((p2['round'], p2['draftVersion']), (1, 2))
        complete_review(self.dir)
        pr.prepare(self.dir, self.rec, revise=True)
        complete_review(self.dir)
        with self.assertRaisesRegex(ValueError, 'budget exhausted'):
            pr.prepare(self.dir, self.rec, revise=True)

    def test_review_snapshots_preserve_overwritten_inputs_builder_and_rules(self):
        (self.dir / 'build').mkdir()
        self.f.write('build/build_report.py', '# first builder')
        p = self.prepared(False)
        root = self.dir / p['snapshot']['path']
        original = (root / 'files/deliverables/report.html').read_bytes()
        self.f.write('deliverables/report.html', 'second draft')
        self.f.write('build/build_report.py', '# changed builder')
        pr.prepare(self.dir, self.rec, revise=True)
        self.assertEqual((root / 'files/deliverables/report.html').read_bytes(), original)
        self.assertEqual((root / 'files/build/build_report.py').read_text(), '# first builder')
        self.assertTrue((root / 'rules.tar').is_file())
        self.assertTrue(list(root.glob('archived-review.*.json')))
        p2 = json.loads((self.dir / pr.DEFAULT_PATH).read_text())
        self.assertFalse(any('review-snapshots' in name for name in p2['reviewedFiles']))
        pr.check_snapshot(self.dir, p)
        (root / 'files/deliverables/report.html').write_text('tampered archive')
        with self.assertRaisesRegex(ValueError, 'Archived reviewed input changed'):
            pr.check_snapshot(self.dir, p)

    def test_started_failed_or_interrupted_reviews_count_even_if_findings_are_cleared(self):
        from review_attempts import begin
        p = self.prepared(False)
        begin(self.dir, self.rec, reviewer='reader-one')
        self.assertIn('draft-review-complete', self.failures())
        with self.assertRaisesRegex(ValueError, 'review path'):
            pr.prepare(self.dir, dict(self.rec, review='evidence/renamed-review.json'))
        pr.prepare(self.dir, self.rec, revise=True)
        p2 = json.loads((self.dir / pr.DEFAULT_PATH).read_text())
        self.assertEqual((p2['round'], p2['draftVersion']), (2, 2))
        begin(self.dir, self.rec, reviewer='reader-two')
        # Editing the current declaration or changing its filename cannot erase the two frozen start receipts.
        p2['round'], p2['maxRounds'] = 1, 99
        self.write_packet(p2)
        self.assertIn('draft-review-budget', self.failures())
        with self.assertRaisesRegex(ValueError, 'budget exhausted'):
            pr.prepare(self.dir, dict(self.rec, review='evidence/renamed-review.json'))

    def test_begin_is_required_idempotent_and_bound_to_the_reader_and_frozen_draft(self):
        from review_attempts import begin, state
        self.prepared(False)
        with self.assertRaisesRegex(ValueError, 'named'): begin(self.dir, self.rec)
        first = begin(self.dir, self.rec, reviewer='fresh-reader')
        self.assertEqual(begin(self.dir, self.rec, reviewer='fresh-reader'), first)
        self.assertEqual(state(self.dir)['used'], 1)
        with self.assertRaisesRegex(ValueError, 'replace'): begin(self.dir, self.rec, reviewer='different-reader')
        first.with_name('prepared-review.json').write_text('{}')
        with self.assertRaises(ValueError): state(self.dir)

    def test_comparison_incremental_and_brief_coverage_are_required_not_inferred_from_arithmetic(self):
        p = self.prepared()
        for name in ('comparisons', 'incremental-flows', 'brief-fidelity'):
            old = p['coverage'].pop(name)
            self.write_packet(p)
            self.assertIn(name + '-coverage', self.failures())
            p['coverage'][name] = old
        self.write_packet(p)
        self.assertEqual(self.failures(), [])

    def test_completed_declaration_without_start_receipt_cannot_publish(self):
        self.prepared(False)
        with patch('review_attempts.begin'):
            complete_review(self.dir)
        self.assertIn('draft-review-budget', self.failures())

    def test_prior_failed_checks_and_unknowns_need_dispositions_not_erasure(self):
        packet = self.prepared()
        packet['handoff']['checks'][0]['result'] = 'fail'
        packet['handoff']['criticalUnknowns'] = ['A material cash boundary remains unsupported.']
        self.write_packet(packet)
        pr.prepare(self.dir, self.rec, revise=True)
        pr.prepare(self.dir, self.rec, revise=True)  # unreviewed re-render must not erase the earlier failed review
        current = complete_review(self.dir)
        self.assertEqual((current['round'], current['draftVersion']), (2, 3))
        self.assertIn('prior-review-dispositions', self.failures())
        current['priorDispositions'] = [
            {'id': 'draft-1/'+packet['handoff']['checks'][0]['name'], 'status': 'resolved', 'reason': 'Checked revised fixture.', 'sourceIds': ['file-0']},
            {'id': 'draft-1/unknown-0', 'status': 'disagreed', 'reason': 'Synthetic fixture has no ownership exposure; checked the actual model.', 'sourceIds': ['file-0']}]
        self.write_packet(current)
        self.assertEqual(self.failures(), [])

    def test_future_fixture_cutoff_preserves_actual_production_time(self):
        now = datetime.now(timezone.utc)
        future = (now + timedelta(days=3)).date().isoformat()
        self.rec['cutoff'] = future
        with self.assertRaisesRegex(ValueError, 'future'):
            pr.prepare(self.dir, self.rec)
        self.rec['evaluation'] = {'mode': 'synthetic-fixture', 'now': future + 'T12:00:00Z', 'reason': 'Fixed synthetic pack date'}
        p = self.prepared(False)
        self.assertLess(datetime.fromisoformat(p['handoff']['producedAt']), datetime.fromisoformat(p['handoff']['asOf']))
        self.assertTrue(all(s['synthetic'] for s in p['handoff']['sources']))
        pr.validate_handoff(p['handoff'], p['evaluation'])
        with self.assertRaisesRegex(ValueError, 'cutoff'):
            pr.validate_handoff(p['handoff'])
        p['handoff']['sources'][0]['synthetic'] = False
        with self.assertRaisesRegex(ValueError, 'synthetic-only'):
            pr.validate_handoff(p['handoff'], p['evaluation'])

    def test_uncertain_assumption_passes_but_reclassifying_as_essential_blocks(self):
        p = self.prepared()
        p['handoff']['claims'].append({'id': 'ramp', 'text': 'The product ramp is uncertain and adverse outcomes are modeled.',
            'material': True, 'basis': 'assumption', 'sourceIds': [], 'calculation': None,
            'rationale': 'Central case from qualified capacity; scenario and dated revision trigger retained.'})
        self.write_packet(p)
        self.assertEqual(self.failures(), [])
        p['handoff']['criticalUnknowns'] = ['An unresolved essential ownership boundary prevents a defensible target.']
        self.write_packet(p)
        self.assertIn('draft-review-complete', self.failures())

    def test_economic_anchor_rejects_cy_restatement_and_accepts_supported_adjustments(self):
        p = self.prepared()
        basis = p['valuationBasis']
        assess = lambda s, b=basis: pr.valuation_basis(s, self.rec, b, p['handoff'])
        self.assertTrue(assess(spec())[0])
        for case in basis['cases']:
            case['benchmarkPeriod'] = 'CY2027'
        self.assertFalse(assess(spec())[0])
        for case in basis['cases']:
            case['benchmarkPeriod'] = self.rec['epsPeriod']
        changed = copy.deepcopy(spec())
        cells = changed['sheets']['Valuation']['cells']
        cells['D5']['value'] = '=20*D19/D4'  # CY or another earnings period disguised as a forward multiple
        ok, detail = assess(changed)
        self.assertFalse(ok)
        self.assertIn('cancels', detail)
        cells['D5']['value'] = '=14.9*(D4/5.55)^0.5'  # supported growth/quality adjustments need not be constant
        self.assertTrue(assess(changed)[0])
        pb = dict(self.rec, method='P/B')
        self.assertTrue(pr.valuation_basis(changed, pb,
            {'status': 'not-applicable', 'reason': 'Capital value is the anchor, not EPS.', 'cases': []}, p['handoff'])[0])
        self.assertFalse(pr.valuation_basis(changed, self.rec,
            {'status': 'not-applicable', 'reason': 'Skip period checks', 'cases': []}, p['handoff'])[0])
        basis['cases'][1]['sensitivityPricing'] = [{'id': 'pricing', 'period': 'CY2027'}]
        self.assertFalse(pr.valuation_basis(spec(), self.rec, basis, p['handoff'], ['pricing'])[0])

    def test_sensitivity_coverage_maps_to_reproducing_model_checks_or_a_reason(self):
        cells = {'D2': {'value': 100, 'kind': 'input'}, 'D3': {'value': 0.2, 'kind': 'input'},
                 'D4': {'value': 10, 'kind': 'input'}, 'D5': {'value': -0.05, 'kind': 'input'},
                 'D6': {'value': '=D2*D3*0.75/D4'},
                 'D7': {'value': '=D2*D5*0.75/D4'}, 'D8': {'value': '=D2*D5/D4'}}
        model = {'sheets': {'M': {'cells': cells}}, 'sensitivities': [
            {'id': 'margin', 'inputs': ['M!D3'], 'shock': 'M!D5', 'eps': 'M!D6', 'shown': 'M!D7'},
            {'id': 'pre-tax', 'inputs': ['M!D3'], 'shock': 'M!D5', 'eps': 'M!D6', 'shown': 'M!D8'}]}
        cover = lambda **c: pr.sensitivity_coverage(model, c)[0]  # noqa: E731
        self.assertFalse(cover(status='undecided'))
        self.assertFalse(cover(status='checked', sensitivityIds=[]))
        self.assertFalse(cover(status='checked', sensitivityIds=['volume']))          # published but never declared
        self.assertFalse(cover(status='checked', sensitivityIds=['margin', 'pre-tax']))  # one row skips tax
        self.assertTrue(cover(status='checked', sensitivityIds=['margin']))
        self.assertTrue(cover(status='not-applicable', reason='The decisive output is net asset value, not EPS.'))
        self.assertFalse(cover(status='not-applicable', reason=' '))
        packet = self.prepared()
        packet['coverage']['sensitivity'] = {'status': 'undecided', 'reason': '', 'sensitivityIds': []}
        self.write_packet(packet)
        self.assertIn('sensitivity-coverage', self.failures())

    def test_inventory_is_advisory_and_excludes_styles(self):
        self.f.write('deliverables/report.html', '<style>p {width:999px}</style><p>Annual productivity 0.8%; input 0.5%.</p>')
        items = pr.inventory(self.dir, self.rec)
        self.assertTrue(any('0.8%' in i['numbers'] for i in items))
        self.assertFalse(any('999' in i['numbers'] for i in items))

    def test_claim_support_disposition_is_required_at_publication(self):
        packet = self.prepared()
        packet['coverage']['claim-support'] = {'status': 'undecided', 'assertionIds': []}
        self.write_packet(packet)
        self.assertIn('claim-support-coverage', self.failures())
        packet['coverage']['claim-support'] = {'status': 'checked', 'assertionIds': ['missing-assertion']}
        self.write_packet(packet)
        self.assertIn('claim-support-coverage', self.failures())

    def test_failed_revision_invalidates_old_publication_before_printing(self):
        self.prepared()
        rec = dict(self.rec, zipPath='deliverables/old.zip', status='validated', fingerprints={'old': 'hash'})
        rec['renders'] = {role: {'html': path, 'pdf': path.replace('.html', '.pdf')}
                          for role, path in rec['renders'].items()}
        (self.dir / 'deliverables/release.json').write_text(json.dumps(rec))
        zipped = self.dir / 'deliverables/old.zip'; zipped.write_bytes(b'old')
        def failed_print(*args):
            current = json.loads((self.dir / 'deliverables/release.json').read_text())
            self.assertEqual(current['status'], 'awaiting-review')
            self.assertNotIn('fingerprints', current)
            self.assertFalse(zipped.exists())
            raise RuntimeError('synthetic printer failure')
        with patch.object(sys, 'argv', ['publication_review.py', 'prepare', str(self.dir), '--revise']), \
             patch.object(rl, 'print_pdf', failed_print):
            with self.assertRaisesRegex(RuntimeError, 'printer failure'):
                pr.main()
        current = json.loads((self.dir / 'deliverables/release.json').read_text())
        self.assertEqual(current['status'], 'failed')

    def test_large_evidence_manifest_does_not_overflow_common_handoff_sources(self):
        folder = self.dir / 'sources'; folder.mkdir()
        for i in range(205):
            (folder / f'{i}.txt').write_text('Synthetic evidence file')
        p = self.prepared()
        self.assertGreater(len(p['reviewedFiles']), 200)
        self.assertLess(len(p['handoff']['sources']), 200)
        self.assertEqual(self.failures(), [])

    def test_exhausted_revision_budget_does_not_leave_a_stale_release_zip(self):
        self.prepared(); pr.prepare(self.dir, self.rec, revise=True)
        complete_review(self.dir)
        rec = dict(self.rec, zipPath='deliverables/old.zip', status='validated', fingerprints={'old': 'hash'})
        record_path = self.dir / 'deliverables/release.json'; record_path.write_text(json.dumps(rec))
        zipped = self.dir / 'deliverables/old.zip'; zipped.write_bytes(b'old')
        self.f.write('deliverables/report.html', 'Changed draft requiring another review')
        with patch.object(sys, 'argv', ['publication_review.py', 'prepare', str(self.dir), '--revise']):
            with self.assertRaisesRegex(ValueError, 'correction budget'):
                pr.main()
        self.assertFalse(zipped.exists())
        current = json.loads(record_path.read_text())
        self.assertEqual(current['status'], 'failed')
        self.assertNotIn('fingerprints', current)


class FinancialAssertionTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)
        self.values = {}

    def evaluate(self, assertion, record=None):
        def cells(s, w, bindings):
            return {key: self.values[ref] for key, ref in bindings.items()}
        with patch.object(rc, 'cell_values', cells):
            return pr.financial_assertion(self.dir, assertion, {}, None, record)

    def cash(self):
        self.values = {'S!A1': 120, 'S!A2': 30, 'S!A3': 80, 'S!A4': 90, 'S!A5': 1.125}
        return {'id': 'cash', 'kind': 'cash-coverage', 'period': 'FY2027E', 'unit': 'x', 'rationale': 'Required cash obligations',
                'beforeOutflows': 'S!A1', 'remainingOutflows': ['S!A2'], 'distributions': 'S!A3',
                'availableCash': 'S!A4', 'coverage': 'S!A5', 'accountingTreatment': 'Lease cash is outside operating cash flow'}

    def test_prelease_coverage_fails_and_already_deducted_cash_is_not_subtracted_twice(self):
        a = self.cash(); self.evaluate(a)
        self.values['S!A5'] = 1.5
        with self.assertRaisesRegex(ValueError, 'Shareholder cash coverage'):
            self.evaluate(a)
        a['remainingOutflows'] = []; self.values.update({'S!A1': 90, 'S!A5': 1.125})
        a['accountingTreatment'] = 'Lease payments already deducted inside operating cash flow'
        self.evaluate(a)

    def test_actual_visible_number_and_period_are_bound(self):
        a = self.cash()
        a['displays'] = [{'id': 'coverage', 'ref': 'S!A5', 'period': 'FY2027E', 'unit': 'x'}]
        rec = {'renders': {'report': 'report.html'}}
        path = self.dir / 'report.html'
        path.write_text(rl.bound_value('coverage', 1.125, 'FY2027E', 'x', lambda x: f'{x:.2f}x'))
        self.evaluate(a, rec)
        path.write_text(path.read_text().replace('>1.12x<', '>1.50x<'))
        with self.assertRaisesRegex(ValueError, 'Visible figure'):
            self.evaluate(a, rec)
        path.write_text(rl.bound_value('coverage', 1.125, '1H2027E', 'x'))
        with self.assertRaisesRegex(ValueError, 'period/unit'):
            self.evaluate(a, rec)

    def test_consistent_render_metadata_cannot_override_the_assertion_output_period(self):
        a = self.cash()
        a['displays'] = [{'id': 'coverage', 'ref': 'S!A5', 'period': 'FY2026A', 'unit': 'x'}]
        (self.dir / 'report.html').write_text(rl.bound_value('coverage', 1.125, 'FY2026A', 'x'))
        with self.assertRaisesRegex(ValueError, 'assertion period'):
            self.evaluate(a, {'renders': {'report': 'report.html'}})

    def test_negative_cash_outputs_accept_house_currency_signs_but_not_reversed_signs(self):
        a = self.cash()
        self.values.update({'S!A1': 3, 'S!A4': -27, 'S!A5': -27/80})
        a['displays'] = [dict(id='coverage', ref='S!A5', period='FY2027E', unit='x'),
                         dict(id='available', ref='S!A4', period='FY2027E', unit='USD million')]
        path = self.dir / 'report.html'; rec = {'renders': {'report': 'report.html'}}
        cover = rl.bound_value('coverage', -27/80, 'FY2027E', 'x')
        for shown in ('-US$27', 'US$-27', '(US$27)', '\u2212US$27'):
            path.write_text(cover + rl.bound_value('available', -27, 'FY2027E', 'USD million', lambda x: shown), encoding='utf-8')
            self.evaluate(a, rec)
        path.write_text(cover + rl.bound_value('available', -27, 'FY2027E', 'USD million', lambda x: 'US$27'), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Visible figure'):
            self.evaluate(a, rec)

    def test_cash_stripped_income_and_unmatched_peer_bases_fail(self):
        self.values = {'V!A1': 100, 'V!A2': 10, 'V!A3': 20, 'V!A4': 1, 'V!A5': 80, 'V!A6': 9, 'V!A7': 80 / 9}
        basis = dict(claimBoundary='operating', incomeDefinition='after-tax', ownership='attributable', currency='USD',
                     scale='million', leaseTreatment='expensed', periodConvention='current FY2027E')
        a = dict(id='core', kind='normalized-ratio', period='FY2027E', unit='x', rationale='Matched operating claims',
                 baseValue='V!A1', baseIncome='V!A2', normalizedValue='V!A5', normalizedIncome='V!A6', ratio='V!A7',
                 removedComponents=[dict(value='V!A3', income='V!A4', rationale='Remove surplus cash and related after-tax income')],
                 basis=basis, peerBases=[copy.deepcopy(basis)])
        self.evaluate(a)
        self.values['V!A6'] = 10
        with self.assertRaisesRegex(ValueError, 'Normalized attributable income'):
            self.evaluate(a)
        self.values['V!A6'] = 9; a['peerBases'][0]['claimBoundary'] = 'whole-equity'
        with self.assertRaisesRegex(ValueError, 'bases differ'):
            self.evaluate(a)

    def financing(self):
        (self.dir / 'terms.txt').write_text('Synthetic amendment to conversion terms.')
        self.values = dict(P=1000, F=2, CP=50, CS=40, T=60, B=1000,
                           S=1040, NI=2000, ADD=20)
        self.values['EPS'] = 2020/self.values['S']
        term = dict(source='terms.txt', locator='Synthetic stipulated term', publishedAt='2026-08-26',
                    effectiveFrom='2026-09-10', conversionPrice=50, principal=1000, contractualFx=2)
        scenario = dict(target='T', baseShares='B', shares='S', profit='NI', afterTaxAddback='ADD', eps='EPS',
                        conversionWeight=1, rationale='Full if-converted scenario for the chosen earnings basis')
        return dict(id='cb', kind='financing', period='FY2027E', unit='million shares', rationale='Scenario financing bridge',
                    asOf='2026-11-07', terms=[dict(term, conversionPrice=55, effectiveFrom='2026-01-01'), term],
                    principal='P', contractualFx='F', conversionPrice='CP', conversionShares='CS',
                    scenarios=[dict(scenario, role=role) for role in ('bear', 'base', 'bull')])

    def test_effective_amendment_and_scenario_dilution(self):
        a = self.financing(); self.evaluate(a)
        self.values['CP'] = 55
        with self.assertRaisesRegex(ValueError, 'effective conversion price'):
            self.evaluate(a)
        self.values['CP'] = 50; self.values['S'] = 1000
        with self.assertRaisesRegex(ValueError, 'Scenario share count'):
            self.evaluate(a)

    def test_nonconversion_is_possible_but_needs_a_consistent_explained_state(self):
        a = self.financing()
        for s in a['scenarios']:
            s.update(conversionWeight=0, nonConversionReason='Explicit holder non-exercise case, not automatic conversion')
        self.values.update(S=1000, ADD=0, EPS=2)
        self.evaluate(a)
        del a['scenarios'][2]['nonConversionReason']
        with self.assertRaisesRegex(ValueError, 'non-conversion'):
            self.evaluate(a)


if __name__ == '__main__':
    unittest.main()
