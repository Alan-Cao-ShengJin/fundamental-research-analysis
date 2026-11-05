"""Multi-sheet model builder: calculation, scenarios, workbook build and sync check."""
from pathlib import Path
import copy, importlib.util, sys, tempfile, unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'company-model/scripts/model_workbook.py'
spec_ = importlib.util.spec_from_file_location('model_workbook', SCRIPT)
m = importlib.util.module_from_spec(spec_); sys.modules['model_workbook'] = m; spec_.loader.exec_module(m)


def fixture():
    return {'sheets': {
        'Revenue Projection': {'lastColumn': 'E', 'notes': 'F', 'sections': [4], 'cells': {
            'B2': {'value': 'Case'}, 'C2': {'value': 2, 'kind': 'input'},
            'B5': {'value': 'Units'}, 'D5': {'value': 100, 'kind': 'actual'}, 'E5': {'value': '=D5*(1+E6)'},
            'B6': {'value': 'Unit growth'}, 'E6': {'value': '=CHOOSE($C$2,E7,E8,E9)', 'pct': True},
            'E7': {'value': 0.0, 'kind': 'judgment', 'pct': True}, 'E8': {'value': 0.1, 'kind': 'judgment', 'pct': True},
            'E9': {'value': 0.2, 'kind': 'judgment', 'pct': True},
            'B10': {'value': 'Price'}, 'D10': {'value': 2, 'kind': 'actual'}, 'E10': {'value': 2, 'kind': 'input'},
            'B11': {'value': 'Revenue'}, 'D11': {'value': '=D5*D10'}, 'E11': {'value': '=E5*E10', 'bold': True},
            'F11': {'value': 'Units x price; growth from the case selector'}}},
        '3S': {'lastColumn': 'E', 'cells': {
            'B5': {'value': 'Revenue'}, 'D5': {'value': "='Revenue Projection'!D11"}, 'E5': {'value': "='Revenue Projection'!E11"},
            'B6': {'value': 'Costs'}, 'D6': {'value': '=-D5*0.7'}, 'E6': {'value': '=-E5*0.7'},
            'B7': {'value': 'Profit'}, 'D7': {'value': '=SUM(D5:D6)'}, 'E7': {'value': '=SUM(E5:E6)', 'bold': True},
            'B8': {'value': 'Loss flag'}, 'E8': {'value': '=IF(E7<0,1,0)'}}}},
        'scenario': {'cell': 'Revenue Projection!C2', 'cases': ['Bear', 'Base', 'Bull']},
        'outputs': {'profit.next': '3S!E7'}}


class ModelWorkbookTests(unittest.TestCase):
    def test_cases_flow_through_sheets(self):
        r = m.calculate(fixture())
        self.assertAlmostEqual(r['Bear']['outputs']['profit.next'], 60.0)
        self.assertAlmostEqual(r['Base']['outputs']['profit.next'], 66.0)
        self.assertAlmostEqual(r['Bull']['outputs']['profit.next'], 72.0)

    def test_missing_input_and_circular_reference_fail(self):
        s = fixture(); s['sheets']['Revenue Projection']['cells']['E10']['value'] = None
        with self.assertRaisesRegex(m.ModelError, 'Missing input'):m.calculate(s)
        s = fixture(); s['sheets']['3S']['cells']['D6']['value'] = '=D7'
        with self.assertRaisesRegex(m.ModelError, 'Circular'):m.calculate(s)

    def test_build_refuses_overwrite_and_check_needs_recalculated_values(self):
        with tempfile.TemporaryDirectory() as d:
            book = Path(d) / 'model.xlsx'
            m.build(fixture(), book)
            with self.assertRaisesRegex(m.ModelError, 'overwrite'):m.build(fixture(), book)
            report = m.check(fixture(), book)
            self.assertFalse(report['passed'])
            self.assertTrue(any('recalculate' in i.get('reason', '') for i in report['issues']))

    def test_check_detects_formula_drift_against_cached_values(self):
        from openpyxl import load_workbook
        with tempfile.TemporaryDirectory() as d:
            book = Path(d) / 'model.xlsx'
            m.build(fixture(), book)
            values = m.calculate(fixture())['Base']['cells']
            w = load_workbook(book)
            for ref, v in values.items():  # stand in for Excel saving its calculated values
                sheet, address = ref.split('!')
                w[sheet][address].value = v
            w.save(book)
            report = m.check(fixture(), book)
            self.assertFalse(report['passed'])
            self.assertTrue(all(i.get('reason') == 'formula drift' for i in report['issues']))

    def test_tag_column_shifts_physical_addresses_and_formulas(self):
        from openpyxl import load_workbook
        s = fixture()
        s['sheets']['Revenue Projection']['tagColumn'] = 'D'
        s['sheets']['Revenue Projection']['tags'] = {'5': 'AR25'}
        with tempfile.TemporaryDirectory() as d:
            book = Path(d) / 'model.xlsx'
            m.build(s, book)
            w = load_workbook(book)
            rp = w['Revenue Projection']
            self.assertEqual(rp['D5'].value, 'AR25')
            self.assertEqual(rp['E5'].value, 100)
            self.assertEqual(rp['F5'].value, '=E5*(1+F6)')
            self.assertEqual(rp['F6'].value, '=CHOOSE($C$2,F7,F8,F9)')
            self.assertEqual(w['3S']['E5'].value, "='Revenue Projection'!F11")
            self.assertIsNotNone(rp['B11'].comment)
            self.assertIn('CaseSelector', w.defined_names)
            self.assertIn('profit_next', w.defined_names)

    def test_statistics_functions(self):
        s = {'sheets': {'S': {'cells': {'A1': {'value': 2}, 'A2': {'value': 4}, 'A3': {'value': '=IF(A1>5,A1,"")'},
                                        'B1': {'value': '=STDEV(A1:A3)'}, 'B2': {'value': '=COUNT(A1:A3)'},
                                        'B3': {'value': '=SQRT(A2)'}}}}}
        c = m.calculate(s)['Model']['cells']
        self.assertAlmostEqual(c['S!B1'], 2 ** 0.5)
        self.assertEqual(c['S!B2'], 2)
        self.assertEqual(c['S!B3'], 2)


class ModelExampleTests(unittest.TestCase):
    """The synthetic full model in assets is the worked example of the model standard."""

    @classmethod
    def setUpClass(cls):
        path = SCRIPT.parent / 'model_example.py'
        spec_e = importlib.util.spec_from_file_location('model_example', path)
        cls.x = importlib.util.module_from_spec(spec_e)
        spec_e.loader.exec_module(cls.x)
        cls.spec = cls.x.spec()
        cls.result = m.calculate(cls.spec)

    def test_asset_matches_generator(self):
        import json
        asset = json.loads((SCRIPT.parents[1] / 'assets/company-model-example.json').read_text(encoding='utf-8'))
        self.assertEqual(asset, json.loads(json.dumps(self.spec)))

    def test_every_tab_of_the_standard(self):
        self.assertEqual(list(self.spec['sheets']), ['Cover', 'Summary', 'Valuation', 'Valuation Band', 'Scenarios',
                                                     'Revenue Build', 'Statements', 'Data', 'Input Prices', 'Guidance',
                                                     'Questions', 'Checks'])

    def test_checks_hold_in_every_column_and_case(self):
        R3, RR = self.x.S3SHEET.R, self.x.RPSHEET.R
        for case, r in self.result.items():
            for col in self.x.COLS:
                for sheet, rows, key in [('Statements', R3, 'check'), ('Statements', R3, 'cash_chk'),
                                         ('Revenue Build', RR, 'rev_chk'), ('Revenue Build', RR, 'gp_chk')]:
                    v = r['cells'].get(f'{sheet}!{col}{rows[key]}')
                    if v is not None:
                        self.assertAlmostEqual(v, 0, places=6, msg=f'{case} {sheet} {key} {col}')
            self.assertEqual(r['cells'][f'Checks!{self.x.CHECK_CELL}'], 0, msg=f'{case} checks failing')
        eps = [self.result[c]['outputs']['eps.FY2027E'] for c in ('Bear', 'Base', 'Bull')]
        self.assertTrue(eps[0] < eps[1] < eps[2])


if __name__ == '__main__':
    unittest.main()
