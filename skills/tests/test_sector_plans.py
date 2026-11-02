"""Economic arithmetic and propagation, not keyword/template-presence tests."""
import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'company-model'
def module(name):
    s=importlib.util.spec_from_file_location(name,ROOT/'scripts'/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
plans=module('sector_plan');compiler=module('forecast_blocks')
def value(compiled,key):return next(c['expected'] for row in compiled['rows'] if row['id']==key for c in row['cells'] if c['period']=='P1')
class SectorPlansTests(unittest.TestCase):
    def test_every_example_reconciles_to_independent_expected_arithmetic(self):
        for slug,case in plans.cases().items():
            with self.subTest(slug=slug):
                computed=compiler.compile_plan(plans.make_plan(slug,True))
                self.assertEqual(computed['findings'],[])
                for key,expected in case['expected'].items():self.assertAlmostEqual(value(computed,key),expected,places=6)
    def test_blank_is_missing_evidence_and_data_not_zero(self):
        for slug in plans.cases():
            with self.subTest(slug=slug):
                computed=compiler.compile_plan(plans.make_plan(slug))
                self.assertIn('missing_value',{f['code'] for f in computed['findings']})
                self.assertTrue(all(c['expected'] is None for r in computed['rows'] for c in r['cells']))
    def test_airline_yield_and_rask_paths_agree_after_load_change(self):
        p=plans.make_plan('transport',True);changed=compiler.perturb(p,'load_factor','P1',.5)
        self.assertAlmostEqual(value(changed,'passenger_revenue'),5000000)
        self.assertAlmostEqual(value(changed,'passenger_revenue'),value(changed,'rask_revenue_check'))
    def test_bank_gross_chargeoffs_and_recoveries_affect_allowance_once(self):
        p=plans.make_plan('banks',True);changed=compiler.perturb(p,'recoveries','P1',3)
        self.assertAlmostEqual(value(changed,'allowance_close'),22)
        changed=compiler.perturb(p,'period_fraction','P1',.5)
        self.assertAlmostEqual(value(changed,'nii'),16.5)
    def test_dividend_coverage_below_one_means_shortfall(self):
        p=plans.make_plan('telecom',True)
        row=next(r for r in compiler.compile_plan(p)['rows'] if r['id']=='dividend_coverage')
        self.assertEqual(row['unit'],'times')
        self.assertNotEqual(row['format'],'percent')
        changed=compiler.perturb(p,'spectrum_cash','P1',14000)
        self.assertAlmostEqual(value(changed,'cash_available'),7000)
        self.assertAlmostEqual(value(changed,'dividend_coverage'),.7)
    def test_production_is_not_automatically_sales(self):
        p=plans.make_plan('metals-mining',True);base=compiler.compile_plan(p);changed=compiler.perturb(p,'recovery','P1',.7)
        self.assertLess(value(changed,'payable_production'),value(base,'payable_production'))
        self.assertEqual(value(changed,'revenue'),value(base,'revenue'))
        self.assertLess(value(changed,'metal_stock_close'),0) # flag implausible sales, do not fabricate extra production
    def test_committed_trial_cost_not_discounted_by_success_twice(self):
        p=plans.make_plan('pharma',True);changed=compiler.perturb(p,'success_probability','P1',0)
        self.assertAlmostEqual(value(changed,'asset_rnpv_proxy'),-10)
    def test_no_variable_contribution_is_not_a_finite_breakeven(self):
        p=plans.make_plan('autos-ev',True);changed=compiler.perturb(p,'variable_unit_cost','P1',20)
        self.assertIsNone(value(changed,'breakeven_units'))
        self.assertIn('zero_denominator',{f['code'] for f in changed['findings']})
    def test_unknown_sector_does_not_silently_choose_one(self):
        with self.assertRaises(ValueError):plans.make_plan('../unreviewed')
if __name__=='__main__':unittest.main()
