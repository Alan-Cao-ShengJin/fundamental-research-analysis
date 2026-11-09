"""Exercise dated NTM through the actual release gate and saved workbook bindings."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_release_check as f


class DatedReleaseTests(unittest.TestCase):
    def setUp(self):
        self.fixture = f.ReleaseCheckTests('test_clean_study_passes')
        self.fixture.setUp(); self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.dir
        self.s = f.spec()
        cells = self.s['sheets']['Statements']['cells']
        for col, period, eps in (('H', '1H FY2027E', 2), ('I', '2H FY2027E', 3.55)):
            cells[col+'5']['value'] = period
            cells[col+'43']['value'] = eps
            cells[col+'44'] = {'value': 100, 'kind': 'input'}
        self.s['sheets']['Valuation']['cells']['D17']['value'] = '=Statements!H43+Statements!I43'
        self.s['sheets']['Valuation']['cells']['D8']['value'] = '=IF(D18/D2-1>0.1,"Buy",IF(D18/D2-1<-0.1,"Sell","Hold"))'
        self.save()
        self.record = f.record(epsPeriod='NTM', fiscalYearEnd=10, ntm={
            'mode': 'dated-periods', 'metric': 'eps-sum', 'allocation': 'uniform-days',
            'rationale': 'Complete half-year forecasts on a constant share basis.',
            'start': '2026-11-01', 'end': '2027-11-01', 'components': [
                {'period': '1H FY2027E', 'start': '2026-11-01', 'end': '2027-05-01',
                 'eps': 'Statements!H43', 'shares': 'Statements!H44', 'header': 'Statements!H5'},
                {'period': '2H FY2027E', 'start': '2027-05-01', 'end': '2027-11-01',
                 'eps': 'Statements!I43', 'shares': 'Statements!I44', 'header': 'Statements!I5'}]},
            bindings=dict(f.record()['bindings'], forwardEps='Valuation!D17', target='Valuation!D18'))

    def save(self):
        from openpyxl import load_workbook
        (self.root / 'model/spec.json').write_text(json.dumps(self.s))
        (self.root / 'deliverables/model.xlsx').unlink()
        f.mw.build(self.s, self.root / 'deliverables/model.xlsx')
        w = load_workbook(self.root / 'deliverables/model.xlsx')
        for ref, value in f.mw.calculate(self.s)['Model']['cells'].items():
            sheet, address = ref.split('!'); w[sheet][address] = value
        w.save(self.root / 'deliverables/model.xlsx')

    def checks(self):
        return f.rc.run(self.root, self.record, model_check=f.passing_check, legacy=True)

    def test_complete_half_year_bridge_passes_without_annual_component_labels(self):
        checks, failures = self.checks()
        self.assertEqual(failures, [])
        self.assertTrue(any(c['name'] == 'ntm-dated-components' and c['result'] == 'pass' for c in checks))

    def test_same_year_wrong_half_header_is_rejected(self):
        self.record['ntm']['components'][0]['period'] = '2H FY2027E'
        self.record['ntm']['components'][1]['period'] = '1H FY2027E'
        self.assertTrue(any(fail.startswith('ntm-dated-components') for fail in self.checks()[1]))

    def test_formula_must_equal_the_dated_bridge(self):
        self.s['sheets']['Valuation']['cells']['D17']['value'] = '=Statements!H43+Statements!I43+0.1'
        self.save()
        self.assertTrue(any(fail.startswith('ntm-bridge-equals-forward-eps') for fail in self.checks()[1]))

    def test_typed_same_value_cannot_replace_a_model_linked_bridge(self):
        self.s['sheets']['Valuation']['cells']['D17']['value'] = 5.55
        self.save()
        self.assertTrue(any(fail.startswith('ntm-dated-lineage') for fail in self.checks()[1]))

    def test_exclusive_end_must_be_the_calendar_anniversary(self):
        self.record['ntm']['end'] = '2027-11-02'
        self.record['ntm']['components'][1]['end'] = '2027-11-02'
        self.assertTrue(any(fail.startswith('ntm-dated-window-exact') for fail in self.checks()[1]))


if __name__ == '__main__':
    unittest.main()
