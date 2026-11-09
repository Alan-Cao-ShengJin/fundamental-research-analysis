"""Calendar-year mapping of fiscal quarters by end date, including 52/53-week years."""
import importlib.util, sys, unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / 'company-model/scripts'
sys.path.insert(0, str(SCRIPTS))
spec_ = importlib.util.spec_from_file_location('calendarize', SCRIPTS / 'calendarize.py')
cz = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(cz)
import model_workbook as mw  # noqa: E402


class CalendarizeTests(unittest.TestCase):
    def test_week_based_quarter_ending_in_january_belongs_to_the_prior_year(self):
        ends = {'V': '2026-12-26', 'W': '2027-03-27', 'X': '2027-07-03', 'Y': '2027-10-02', 'Z': '2028-01-01',
                'AA': '2028-04-01'}
        self.assertEqual(cz.calendar_quarter('2028-01-01'), (2027, 4))
        self.assertEqual(cz.calendar_years(ends), {2027: ['W', 'X', 'Y', 'Z']})   # 2026 and 2028 are incomplete

    def test_calendar_eps_is_profit_over_average_shares_not_summed_eps(self):
        cells = {}
        for col, profit, shares in [('W', 100, 10), ('X', 120, 10), ('Y', 140, 12), ('Z', 160, 12)]:
            cells.update({f'{col}2': {'value': profit, 'kind': 'input'}, f'{col}3': {'value': shares, 'kind': 'input'},
                          f'{col}4': {'value': f'={col}2/{col}3'}})
        cells['B6'] = {'value': cz.eps_formula('S', ['W', 'X', 'Y', 'Z'], 2, 3, days=[91, 91, 91, 91])}
        e = mw.Engine({'sheets': {'S': {'cells': cells}}})
        self.assertAlmostEqual(e.value('S', 'B6'), 520 / 11)
        self.assertNotAlmostEqual(e.value('S', 'B6'), sum(e.value('S', f'{c}4') for c in 'WXYZ'))

    def test_a_14_week_quarter_carries_its_time_weight_in_the_share_denominator(self):
        ends = {'P': '2026-12-26', 'W': '2027-03-27', 'X': '2027-06-26', 'Y': '2027-09-25', 'Z': '2028-01-01'}
        days = cz.quarter_days(ends)
        self.assertEqual([days[c] for c in 'WXYZ'], [91, 91, 91, 98])
        cells = {}
        for col, shares in zip('WXYZ', [10, 10, 10, 100]):
            cells.update({f'{col}2': {'value': 100, 'kind': 'input'}, f'{col}3': {'value': shares, 'kind': 'input'}})
        cells['B6'] = {'value': cz.eps_formula('S', list('WXYZ'), 2, 3, days=[days[c] for c in 'WXYZ'])}
        cells['B7'] = {'value': cz.eps_formula('S', list('WXYZ'), 2, 3, days=None)}   # labelled approximation
        e = mw.Engine({'sheets': {'S': {'cells': cells}}})
        self.assertAlmostEqual(e.value('S', 'B6'), 11.8436, places=4)
        self.assertAlmostEqual(e.value('S', 'B7'), 12.3077, places=4)
        with self.assertRaises(TypeError):
            cz.eps_formula('S', list('WXYZ'), 2, 3)          # the weighting choice must be explicit

    def test_two_fiscal_quarters_in_one_calendar_quarter_and_offset_months_are_refused(self):
        with self.assertRaisesRegex(ValueError, 'both map'):
            cz.calendar_years({'A': '2027-03-27', 'B': '2027-04-03'})
        with self.assertRaisesRegex(ValueError, 'map this period by its months'):
            cz.calendar_quarter('2027-05-15')


if __name__ == '__main__':
    unittest.main()
