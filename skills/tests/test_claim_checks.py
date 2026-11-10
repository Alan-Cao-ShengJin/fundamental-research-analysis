"""Financial and inference counterexamples; no model output is graded for bullishness."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'report-layout/scripts'))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'company-model/scripts'))
import claim_checks as cc


class ClaimChecksTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = {'ids': ['short', 'medium', 'long'], 'returns': [.04, .07, .20], 'multiple': 15.3, 'eps': 1.2861}
        (self.root / 'inputs.json').write_text(json.dumps(self.data))
        self.packet = {'reviewedFiles': {'inputs.json': 'hash-checked-by-publication-wrapper'},
            'handoff': {'sources': [{'id': 'source'}], 'claims': [
                {'id': 'claim', 'basis': 'reported', 'rationale': None}]}}
        values = [100, 20, 10, 70, 1000, .10, .07, 0, 35, 2]
        self.spec = {'sheets': {'M': {'cells': {f'A{i}': {'value': value} for i, value in enumerate(values, 1)}}}}
        self.base = {'id': 'test', 'claimId': 'claim', 'location': 'Report paragraph or reviewer finding',
                     'sourceIds': ['source'], 'rationale': 'Synthetic evidence for this assertion.'}

    def file(self, pointer):
        return {'file': 'inputs.json', 'pointer': pointer}

    def check(self, assertion):
        return cc.evaluate(self.root, dict(self.base, **assertion), self.spec, self.packet)

    def set_claim(self):
        return {'kind': 'quantified-set', 'scope': 'universe', 'universeDefinition': 'All three supplied alternatives',
                'universeIds': self.file('/ids'), 'quantifier': 'all', 'predicate': {'op': '>', 'threshold': .1},
                'members': [{'id': name, 'value': self.file(f'/returns/{i}')} for i, name in enumerate(self.data['ids'])]}

    def cash(self):
        return {'kind': 'cash-boundary', 'numerator': {'model': 'M!A4'}, 'denominator': {'model': 'M!A5'},
                'ratio': {'model': 'M!A7'}, 'nonControllingInterests': 'present',
                'numeratorBoundary': 'parent-economic', 'denominatorBoundary': 'parent-equity',
                'interpretation': 'owner-return', 'reconciliation': {
                    'baseCash': {'model': 'M!A1'}, 'nonOwnerEconomicCash': {'model': 'M!A2'},
                    'unavailableCash': {'model': 'M!A3'}, 'rightsBasis': 'Economic partner share and separately restricted parent cash.'}}

    def test_universal_claim_fails_when_only_some_observations_support_it(self):
        with self.assertRaisesRegex(ValueError, '1 of 3'):
            self.check(self.set_claim())
        case = self.set_claim(); case['quantifier'] = 'any'
        self.assertIn('1 of 3', self.check(case))

    def test_true_listed_subset_is_allowed_without_claiming_the_universe(self):
        case = self.set_claim(); case['scope'] = 'listed'; case['members'] = case['members'][2:]
        self.assertIn('1 of 1', self.check(case))
        case['scope'] = 'universe'
        with self.assertRaisesRegex(ValueError, 'complete input set'):
            self.check(case)

    def test_empty_and_duplicate_sets_do_not_vacuously_pass(self):
        for members in ([], [self.set_claim()['members'][0]] * 2):
            case = self.set_claim(); case['members'] = members
            with self.assertRaises(ValueError):
                self.check(case)

    def test_no_negative_observations_is_a_valid_none_claim(self):
        case = self.set_claim(); case.update(quantifier='none', predicate={'op': '<', 'threshold': 0})
        self.assertIn('0 of 3', self.check(case))

    def test_company_results_cannot_be_reported_as_an_industry_fact(self):
        case = {'kind': 'evidence-scope', 'sourceScopes': {'source': 'company'}, 'conclusionScope': 'industry'}
        with self.assertRaisesRegex(ValueError, 'reasoned inference'):
            self.check(case)
        self.packet['handoff']['claims'][0].update(basis='inference', rationale='A hypothesis supported by the company evidence.')
        case['limitations'] = 'One issuer is not the whole industry; category data are unavailable.'
        self.assertIn('reconciled', self.check(case))

    def test_actual_industry_evidence_supports_a_reported_industry_claim(self):
        self.assertIn('reconciled', self.check({'kind': 'evidence-scope',
            'sourceScopes': {'source': 'industry'}, 'conclusionScope': 'industry'}))
        with self.assertRaises(ValueError):
            self.check({'kind': 'evidence-scope', 'sourceScopes': {'unknown-source': 'industry'}, 'conclusionScope': 'industry'})

    def test_owner_cash_removes_economic_non_owner_share_and_access_limits(self):
        self.assertIn('reconcile', self.check(self.cash()))
        case = self.cash(); case.update(numerator={'model': 'M!A1'}, ratio={'model': 'M!A6'}, numeratorBoundary='consolidated')
        with self.assertRaisesRegex(ValueError, 'not parent-owner cash'):
            self.check(case)

    def test_explicit_consolidated_proxy_is_not_forced_into_owner_cash(self):
        case = self.cash(); case.update(numerator={'model': 'M!A1'}, ratio={'model': 'M!A6'},
            numeratorBoundary='consolidated', interpretation='consolidated-proxy',
            limitations='Group cash before partner claims over parent equity: a labeled proxy, not owner yield.')
        self.assertIn('reconcile', self.check(case))
        del case['limitations']
        with self.assertRaisesRegex(ValueError, 'limitation'):
            self.check(case)

    def test_wholly_owned_cash_does_not_get_an_automatic_haircut(self):
        case = self.cash(); case.update(numerator={'model': 'M!A1'}, ratio={'model': 'M!A6'},
            nonControllingInterests='none', numeratorBoundary='consolidated')
        del case['reconciliation']
        self.assertIn('reconcile', self.check(case))

    def test_distribution_cover_is_not_presented_as_an_owner_cash_yield(self):
        case = self.cash(); case.update(interpretation='distribution-coverage',
            denominator={'model':'M!A9'},ratio={'model':'M!A10'},
            denominatorBoundary='parent-distributions', limitations='Coverage assumes the disclosed parent access rights hold.')
        self.assertIn('reconcile', self.check(case))
        case['denominatorBoundary']='parent-equity'
        with self.assertRaisesRegex(ValueError,'distributions'):
            self.check(case)

    def test_wrong_owner_bridge_and_wrong_ratio_fail(self):
        case = self.cash(); case['reconciliation']['nonOwnerEconomicCash'] = {'model': 'M!A8'}
        with self.assertRaisesRegex(ValueError, 'Reconcile'):
            self.check(case)
        case = self.cash(); case['ratio'] = {'model': 'M!A6'}
        with self.assertRaisesRegex(ValueError, 'does not reproduce'):
            self.check(case)

    def test_reviewer_replacement_arithmetic_is_checked_and_display_rounding_allowed(self):
        case = {'kind': 'calculation', 'role': 'reviewer', 'inputs': {'multiple': self.file('/multiple'), 'eps': self.file('/eps')},
                'expression': 'multiple * eps', 'shown': 19.4, 'decimals': 2}
        with self.assertRaisesRegex(ValueError, 'does not reproduce'):
            self.check(case)
        case['shown'] = 19.68
        self.assertIn('reviewer calculation reproduces', self.check(case))
        case['inputs']['multiple'] = {'modelFormula': '=AVERAGE(M!A1:A2)'}
        case['shown'] = round(60 * 1.2861, 2)
        self.assertIn('reproduces', self.check(case))

    def test_unfrozen_data_and_code_execution_are_rejected(self):
        case = {'kind': 'calculation', 'role': 'author', 'inputs': {'eps': self.file('/eps')},
                'expression': '__import__("os").getcwd()', 'shown': 0}
        with self.assertRaises(ValueError):
            self.check(case)
        case.update(expression='eps'); self.packet['reviewedFiles'] = {}
        with self.assertRaisesRegex(ValueError, 'frozen'):
            self.check(case)

    def test_replacement_constant_cannot_pose_as_a_verified_calculation(self):
        case={'kind':'calculation','role':'reviewer','inputs':{'x':self.file('/eps')},'expression':'19.4','shown':19.4}
        with self.assertRaisesRegex(ValueError,'bound input'):
            self.check(case)
        case.update(expression='x'); case['inputs']['x']={'modelFormula':'=19.4'}
        with self.assertRaisesRegex(ValueError,'consume model inputs'):
            self.check(case)

    def test_feasible_counterexample_rejects_claim_that_target_is_impossible(self):
        case={'kind':'bounded-bridge','offset':{'model':'M!A8'},'target':{'model':'M!A6'},
              'drivers':[{'id':'driver','coefficient':.1,'low':{'model':'M!A8'},'high':{'model':'M!A10'}}],
              'domainRationale':'Independent linear driver in matched units; no additional constraints in this synthetic example.',
              'expectedFeasible':False}
        with self.assertRaisesRegex(ValueError,'contradicts'): self.check(case)
        case['expectedFeasible']=True
        self.assertIn('witness',self.check(case))

    def test_correct_calculation_ledger_cannot_approve_wrong_rendered_figure(self):
        from display_bindings import bound_measure
        expected=self.data['multiple']*self.data['eps']
        display={'document':'report.html','id':'target','period':'FY1','unit':'currency','decimals':2}
        case={'kind':'calculation','role':'author','inputs':{'m':self.file('/multiple'),'eps':self.file('/eps')},
              'expression':'m*eps','shown':round(expected,2),'decimals':2,'displays':[display]}
        self.packet['reviewedFiles']['report.html']='frozen-by-wrapper'
        html=bound_measure('target',expected,'FY1','currency')
        (self.root/'report.html').write_text(html,encoding='utf-8')
        self.assertIn('reproduces',self.check(case))
        (self.root/'report.html').write_text(html.replace('19.68','18.68'),encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'Visible'): self.check(case)

    def test_sourced_rendered_range_checks_transform_and_both_endpoints(self):
        from display_bindings import bound_measure
        self.packet['reviewedFiles']['report.html']='frozen-by-wrapper'
        display={'document':'report.html','id':'range','period':'FY1-2','unit':'ratio','style':'percent','decimals':0,'order':'ascending'}
        case={'kind':'rendered-measure','values':[{'model':'M!A6'},{'model':'M!A7'}],'displays':[display]}
        html=bound_measure('range',[.1,.07],'FY1-2','ratio',style='percent',decimals=0,order='ascending')
        (self.root/'report.html').write_text(html,encoding='utf-8'); self.assertIn('agree',self.check(case))
        (self.root/'report.html').write_text(html.replace('7%–10%','-7%–-10%'),encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'Visible'): self.check(case)

    def test_applicability_does_not_allow_hiding_declared_assertions(self):
        packet = {'coverage': {'claim-support': {'status': 'not-applicable', 'reason': 'No such numerical or scope claims.', 'assertionIds': []}},
                  'claimAssertions': []}
        self.assertTrue(cc.coverage(packet)[0])
        packet['claimAssertions'] = [dict(self.base, **self.set_claim())]
        self.assertFalse(cc.coverage(packet)[0])
        packet['coverage']['claim-support'] = {'status': 'checked', 'assertionIds': ['test']}
        self.assertTrue(cc.coverage(packet)[0])
        packet['coverage']['claim-support']['assertionIds'] = []
        self.assertFalse(cc.coverage(packet)[0])

    def test_cash_yield_does_not_equal_combined_payoff_when_the_price_changes(self):
        # Synthetic prices 100 -> 70, with 20 of eligible cash, yield -10% combined, not +20%.
        case={'kind':'calculation','role':'author','inputs':{'initial':{'model':'M!A1'},'ending':{'model':'M!A4'},'receipts':{'model':'M!A2'}},
              'expression':'(ending + receipts) / initial - 1','shown':.20,'decimals':4}
        with self.assertRaisesRegex(ValueError,'does not reproduce'): self.check(case)
        case['shown']=-.1
        self.assertIn('reproduces',self.check(case))


if __name__ == '__main__':
    unittest.main()
