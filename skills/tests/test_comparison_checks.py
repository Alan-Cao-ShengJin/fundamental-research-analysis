"""Comparable-period and incremental-flow counterexamples across businesses and reviewer roles."""
import copy
from datetime import date
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'report-layout/scripts'))
import comparison_checks as cc


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.values = {'restMargin': .28, 'guide': .27, 'restRevenue': 300, 'knownProfit': 24, 'fullRevenue': 400,
            'annualMargin': .27, 'halfCash': 90, 'quarterCash': 83, 'incrementalCash': 7}

    def item(self, key, start='2028-01-01', end='2029-01-01', measure='ratio', **over):
        return {'value': key, 'definition': dict(quantity='gross margin', unit='fraction', currency='none', scale='1',
            perimeter='parent operating unit', basis='recurring', measure=measure, start=start, end=end, **over)}

    def assertion(self, role='author'):
        return {'kind': 'comparison', 'role': role, 'relation': 'same-period', 'op': '>',
            'left': self.item('restMargin', start='2028-04-01'), 'right': self.item('guide')}

    def test_remaining_period_above_full_year_guide_is_invalid_even_for_reviewer(self):
        for role in ('author', 'reviewer'):
            with self.assertRaisesRegex(ValueError, 'periods differ'):
                cc.evaluate(self.assertion(role), self.values.__getitem__)

    def test_bound_period_reconciliation_allows_valid_annual_comparison(self):
        a = self.assertion()
        a['left']['reconcile'] = {'inputs': {'restRevenue': 'restRevenue', 'knownProfit': 'knownProfit', 'fullRevenue': 'fullRevenue'},
            'expression': '(original * restRevenue + knownProfit) / fullRevenue', 'result': 'annualMargin',
            'definition': self.item('annualMargin')['definition'], 'rationale': 'Weight remaining and known gross profit by actual revenue.'}
        a['op'] = '=='
        self.assertIn('reconciles', cc.evaluate(a, self.values.__getitem__))
        self.values['annualMargin'] = .28
        with self.assertRaisesRegex(ValueError, 'reconciliation'): cc.evaluate(a, self.values.__getitem__)

    def test_matching_comparison_and_different_year_comparison_can_pass(self):
        a = self.assertion(); a['left'] = self.item('restMargin')
        self.assertIn('reconciles', cc.evaluate(a, self.values.__getitem__))
        a['right'] = self.item('guide', start='2027-01-01', end='2028-01-01')
        a.update(relation='matched-periods', alignment='Same complete fiscal year and recurring basis; leap-day difference is immaterial.')
        self.assertIn('reconciles', cc.evaluate(a, self.values.__getitem__))
        a['right']['definition']['perimeter'] = 'different group including minority interests'
        with self.assertRaisesRegex(ValueError, 'definitions differ'): cc.evaluate(a, self.values.__getitem__)
        a.update(relation='cross-section', alignment='Selected peer group, same recurring measure and fiscal-year duration.')
        self.assertIn('reconciles', cc.evaluate(a, self.values.__getitem__))

    def test_units_basis_and_false_ordering_fail(self):
        for key in ('unit', 'currency', 'scale', 'basis', 'quantity'):
            a = self.assertion(); a['left'] = self.item('restMargin'); a['right']['definition'][key] = 'different'
            with self.assertRaises(ValueError): cc.evaluate(a, self.values.__getitem__)
        a = self.assertion(); a['left'] = self.item('restMargin'); a['op'] = '<'
        with self.assertRaisesRegex(ValueError, 'false'): cc.evaluate(a, self.values.__getitem__)

    def test_descriptive_context_is_allowed_without_pretending_guide_compliance(self):
        a = self.assertion(); a.update(relation='contextual', interpretation='descriptive-only',
            alignment='Quarter margin shown beside annual history, explicitly different periods.',
            limitations='Context only; does not establish a breach of the full-year guide.')
        self.assertIn('contextual', cc.evaluate(a, self.values.__getitem__))
        del a['limitations']
        with self.assertRaisesRegex(ValueError, 'descriptive-only'): cc.evaluate(a, self.values.__getitem__)

    def flow(self):
        def f(key, start, end):
            item = self.item(key, start, end, measure='flow')
            item['definition'].update(quantity='operating cash flow', unit='currency', currency='USD', scale='millions', basis='reported')
            return item
        return {'kind': 'incremental-flow', 'role': 'author',
            'current': f('halfCash', '2028-01-01', '2028-07-01'),
            'prior': f('quarterCash', '2028-01-01', '2028-04-01'),
            'incremental': f('incrementalCash', '2028-04-01', '2028-07-01')}

    def test_cumulative_subtraction_derives_latest_nonoverlapping_flow(self):
        self.assertIn('7', cc.evaluate(self.flow(), self.values.__getitem__))
        self.values['incrementalCash'] = 173
        with self.assertRaisesRegex(ValueError, 'does not equal'): cc.evaluate(self.flow(), self.values.__getitem__)

    def test_ratios_eps_balances_changed_perimeters_and_nonoverlapping_cumulatives_fail(self):
        for measure in ('ratio', 'per-share', 'stock'):
            a = self.flow()
            for k in ('current', 'prior', 'incremental'):
                a[k]['definition'].update(measure=measure, asOf='2028-07-01')
            with self.assertRaisesRegex(ValueError, 'Only additive'): cc.evaluate(a, self.values.__getitem__)
        a = self.flow(); a['prior']['definition']['basis'] = 'pre-restatement'
        with self.assertRaisesRegex(ValueError, 'matching definitions'): cc.evaluate(a, self.values.__getitem__)
        a = self.flow(); a['prior']['definition']['start'] = '2027-10-01'
        with self.assertRaisesRegex(ValueError, 'common start'): cc.evaluate(a, self.values.__getitem__)

    def test_coverage_cannot_hide_declared_items_but_reasoned_unavailability_is_allowed(self):
        packet = {'coverage': {'incremental-flows': {'status': 'not-applicable', 'reason': 'Only a closing balance was supplied.', 'assertionIds': []}}}
        self.assertTrue(cc.coverage(packet, 'incremental-flows', {'incremental-flow'}))
        packet['claimAssertions'] = [dict(self.flow(), id='q2')]
        self.assertFalse(cc.coverage(packet, 'incremental-flows', {'incremental-flow'}))
        packet['coverage']['incremental-flows'] = {'status': 'checked', 'assertionIds': ['q2']}
        self.assertTrue(cc.coverage(packet, 'incremental-flows', {'incremental-flow'}))

    def test_earnings_update_requires_sourced_candidate_dispositions(self):
        packet = {'researchMode': 'earnings-update', 'handoff': {'sources': [{'id': 'filing'}]},
            'coverage': {'incremental-flows': {'status': 'not-applicable', 'reason': 'No compatible earlier flow.', 'assertionIds': [], 'candidates': []}}}
        check = lambda: cc.coverage(packet, 'incremental-flows', {'incremental-flow'})
        self.assertFalse(check())
        candidate = {'id': 'profit', 'material': True, 'sourceIds': ['filing'], 'status': 'unavailable',
                     'reason': 'Only an annual flow is available; the earlier document contains balance-sheet stocks.'}
        packet['coverage']['incremental-flows']['candidates'] = [candidate]
        self.assertTrue(check())
        candidate['status'] = 'immaterial'
        self.assertFalse(check())
        candidate.update(status='checked', assertionId='missing')
        self.assertFalse(check())
        packet['claimAssertions'] = [dict(self.flow(), id='flow')]
        packet['coverage']['incremental-flows'].update(status='checked', assertionIds=['flow'])
        candidate['assertionId'] = 'flow'
        self.assertTrue(check())
        candidate['sourceIds'] = ['invented']
        self.assertFalse(check())


if __name__ == '__main__':
    unittest.main()
