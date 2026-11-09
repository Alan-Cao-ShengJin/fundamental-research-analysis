"""Dated bridges test actual coverage and equity arithmetic, not a preferred rating."""
import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'report-layout/scripts'))
import dated_ntm as dn
import release_check as rc


class DatedNtmTests(unittest.TestCase):
    def setUp(self):
        self.values = {'S!B5': '2Q FY2027E', 'S!C5': '2H FY2027E', 'S!D5': '1H FY2028E',
            'S!B8': .30, 'S!C8': .57, 'S!D8': .64,
            'S!B9': 100, 'S!C9': 100, 'S!D9': 100, 'S!B7': 30, 'S!C7': 57, 'S!D7': 64}
        self.n = {'mode': 'dated-periods', 'start': '2026-12-01', 'end': '2027-12-01',
            'allocation': 'uniform-days', 'metric': 'eps-sum',
            'rationale': 'The supported forecast profile is allocated uniformly within its quarter/half.',
            'components': [dict(period=p, start=s, end=e, eps=f'S!{c}8', profit=f'S!{c}7', shares=f'S!{c}9', header=f'S!{c}5')
                for c, p, s, e in [('B', '2Q FY2027E', '2026-10-01', '2027-01-01'),
                    ('C', '2H FY2027E', '2027-01-01', '2027-07-01'), ('D', '1H FY2028E', '2027-07-01', '2028-01-01')]]}

    def calc(self):
        return dn.calculate(self.n, self.values.__getitem__)

    def test_mixed_period_fractions_need_not_sum_to_one_and_can_change_rating(self):
        result = self.calc()
        self.assertAlmostEqual(result['eps'], .30*31/92 + .57 + .64*153/184)
        self.assertGreater(sum(c['fractionOfComponent'] for c in result['components']), 2)
        self.assertEqual(rc.rating_for(result['eps']*16.95/22.5-1), 'Hold')
        annual = 1.15*7/12 + 1.22*5/12
        self.assertEqual(rc.rating_for(annual*16.95/22.5-1), 'Sell')

    def test_gaps_overlaps_empty_irrelevant_and_duplicate_periods_fail(self):
        for change in ('gap', 'overlap', 'irrelevant', 'empty', 'duplicate'):
            with self.subTest(change=change):
                original = copy.deepcopy(self.n)
                if change == 'gap': self.n['components'][1]['start'] = '2027-01-02'
                if change == 'overlap': self.n['components'][1]['start'] = '2026-12-31'
                if change == 'irrelevant': self.n['components'][0]['end'] = '2026-11-30'
                if change == 'empty': self.n['components'] = []
                if change == 'duplicate': self.n['components'][1]['period'] = self.n['components'][0]['period']
                with self.assertRaises(ValueError): self.calc()
                self.n = original

    def test_wrong_weight_header_and_duplicate_cell_fail(self):
        self.n['components'][0]['weight'] = .5
        with self.assertRaisesRegex(ValueError, 'overlap'): self.calc()
        del self.n['components'][0]['weight']
        self.values['S!B5'] = '1H FY2027E'
        with self.assertRaisesRegex(ValueError, 'header'): self.calc()
        self.values['S!B5'] = '2Q FY2027E'
        self.n['components'][1]['eps'] = 'S!B8'
        with self.assertRaisesRegex(ValueError, 'two dated periods'): self.calc()

    def test_changed_shares_use_profit_over_time_weighted_shares(self):
        self.values['S!C9'], self.values['S!D9'] = 110, 120
        with self.assertRaisesRegex(ValueError, 'constant'): self.calc()
        self.n['metric'] = 'profit-over-shares'
        r = self.calc()
        profit = 30*31/92 + 57 + 64*153/184
        shares = (100*31 + 110*181 + 120*153)/365
        self.assertAlmostEqual(r['eps'], profit/shares)
        self.assertAlmostEqual(r['weightedShares'], shares)

    def test_leap_year_and_irregular_periods_use_actual_days(self):
        self.n.update(start='2027-12-30', end='2028-12-30')
        self.n['components'] = [dict(period='FY2028E', start='2027-12-27', end='2029-01-01',
            eps='S!B8', shares='S!B9', header='S!B5')]
        self.values['S!B5'] = 'FY2028E'
        self.assertAlmostEqual(self.calc()['eps'], .3 * 366/371)

    def test_unknown_allocation_nonfinite_and_nonpositive_shares_fail(self):
        self.n['allocation'] = 'guess'
        with self.assertRaises(ValueError): self.calc()
        self.n['allocation'] = 'uniform-days'
        self.values['S!B8'] = float('inf')
        with self.assertRaises(ValueError): self.calc()
        self.values['S!B8'], self.values['S!B9'] = .3, 0
        with self.assertRaises(ValueError): self.calc()


if __name__ == '__main__':
    unittest.main()
