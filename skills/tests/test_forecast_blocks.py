"""Exercise forecast propagation, missing inputs, unsafe formulas and read-only tracing."""
import copy,hashlib,importlib.util,json,tempfile,unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/'company-model'
def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py')
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result
compiler=module('forecast_blocks');initializer=module('init_forecast_plan');tracer=module('trace_model')
def result(compiled,nid,pid):
    return next(c['expected'] for r in compiled['rows'] if r['id']==nid for c in r['cells'] if c['period']==pid)


class ForecastBlocksTests(unittest.TestCase):
    def test_component_forecasts_aggregate_and_input_change_preserves_other_periods(self):
        plan=initializer.make_plan(True);base=compiler.compile_plan(plan)
        self.assertEqual(base['findings'],[])
        self.assertAlmostEqual(result(base,'total_revenue','P1'),2282.5)
        self.assertAlmostEqual(result(base,'total_contribution','P1'),913)
        change=compiler.perturb(plan,'a_activity','P1',121)
        self.assertAlmostEqual(result(change,'total_revenue','P1')-result(base,'total_revenue','P1'),115.5)
        self.assertAlmostEqual(result(change,'total_contribution','P1')-result(base,'total_contribution','P1'),47.3)
        for row in base['rows']:
            for pid in ('P0','P2'):
                self.assertEqual(result(base,row['id'],pid),result(change,row['id'],pid))

    def test_missing_inputs_remain_unavailable_and_evidence_gaps_are_reported(self):
        compiled=compiler.compile_plan(initializer.make_plan(False))
        self.assertIsNone(result(compiled,'total_revenue','P1'))
        self.assertIn('missing_value',{f['code'] for f in compiled['findings']})
        self.assertIn('missing_basis',{f['code'] for f in compiled['findings']})
        formula=next(c['formula'] for r in compiled['rows'] if r['id']=='a_revenue' for c in r['cells'] if c['period']=='P1')
        self.assertEqual(formula,'=(E9*E10)') # readable arithmetic; export validates missing inputs

    def test_row_level_basis_is_inherited_and_period_overrides_remain_local(self):
        plan=initializer.make_plan(True)
        n=plan['blocks'][0]['nodes'][0]
        n['basis']={'default':{'source':'Synthetic historical source','rationale':'Synthetic calibrated activity'},
                    'periods':{'P2':{'rationale':'Alternative late-period estimate'}}}
        built=compiler.compile_plan(plan)
        self.assertFalse(any(f['code']=='missing_basis' and f['node']==n['id'] for f in built['findings']))
        cells=next(row['cells'] for row in built['rows'] if row['id']==n['id'])
        self.assertEqual(cells[1]['basis']['rationale'],'Synthetic calibrated activity')
        self.assertEqual(cells[2]['basis']['rationale'],'Alternative late-period estimate')

    def test_lagged_roll_forward_uses_prior_period_without_a_false_cycle(self):
        plan=initializer.make_plan(True)
        plan['blocks'][0]['nodes'][0]={'id':'a_activity','label':'Activity','unit':'activity','role':'calculation','values':{'P0':100},'formula':'lag(a_activity) * 1.1'}
        compiled=compiler.compile_plan(plan)
        self.assertAlmostEqual(result(compiled,'a_activity','P2'),121)
        cell=next(c for r in compiled['rows'] if r['id']=='a_activity' for c in r['cells'] if c['period']=='P2')
        self.assertIn('E9',cell['formula'])

    def test_cycles_unknown_precedents_and_executable_expressions_are_rejected(self):
        for formula in ('a_revenue + 1','unknown_node * 2',"__import__('os').system('anything')"):
            plan=initializer.make_plan(True)
            plan['blocks'][0]['nodes'][3]['formula']=formula
            with self.assertRaises(compiler.ModelError):compiler.compile_plan(plan)

    def test_zero_denominators_and_unused_inputs_are_visible(self):
        plan=initializer.make_plan(True)
        for block in plan['blocks'][:2]:block['nodes'][0]['values']['P1']=0
        plan['blocks'][0]['nodes'].append({'id':'unused','label':'Unused input','unit':'ratio','role':'foundation','values':{'P0':1,'P1':2,'P2':3}})
        compiled=compiler.compile_plan(plan)
        self.assertIsNone(result(compiled,'contribution_margin','P1'))
        codes={f['code'] for f in compiled['findings']}
        self.assertIn('zero_denominator',codes);self.assertIn('unused_foundation',codes)

    def test_historical_perturbations_are_not_allowed(self):
        with self.assertRaises(compiler.ModelError):compiler.perturb(initializer.make_plan(True),'a_activity','P0',120)

    def test_saved_example_reconciles_every_value_and_preserves_local_formula_links(self):
        from openpyxl import load_workbook
        compiled=compiler.compile_plan(initializer.make_plan(True))
        path=ROOT/'assets/forecast-blocks-example.xlsx'
        formulas=load_workbook(path,data_only=False);values=load_workbook(path,data_only=True)
        for row in compiled['rows']:
            for cell in row['cells']:
                self.assertAlmostEqual(values.active[cell['address']].value,cell['expected'])
                if cell['formula']:
                    self.assertEqual(formulas.active[cell['address']].value,cell['formula'])
                    self.assertNotIn('!',cell['formula'])
        formulas.close();values.close()

    def test_tracer_preserves_source_and_exposes_depth_limits(self):
        path=ROOT/'assets/forecast-blocks-example.xlsx'
        before=hashlib.sha256(path.read_bytes()).hexdigest()
        full=tracer.trace(path,['Operating build!E14'])
        self.assertIn('Operating build!E9',full['nodes'])
        self.assertTrue(all(p['same_sheet'] for n in full['nodes'].values() for p in n['precedents']))
        limited=tracer.trace(path,['Operating build!E14'],max_depth=0)
        self.assertTrue(limited['unresolved'])
        self.assertEqual(before,hashlib.sha256(path.read_bytes()).hexdigest())

    def test_house_theme_distinguishes_actuals_forecast_inputs_and_calculations(self):
        from openpyxl import load_workbook
        path=ROOT/'assets/forecast-blocks-example.xlsx'
        book=load_workbook(path,data_only=False);sheet=book.active
        rgb=lambda cell:sheet[cell].font.color.rgb[-6:]
        self.assertFalse(sheet.sheet_view.showGridLines)
        self.assertEqual(rgb('D9'),'17365D')
        self.assertEqual(rgb('E9'),'7030A0')
        self.assertEqual(sheet['E9'].fill.fgColor.rgb[-6:],'F2DDD5')
        self.assertEqual(rgb('E12'),'000000')
        self.assertTrue(sheet['E14'].font.bold)
        self.assertTrue(sheet['E27'].font.bold)
        self.assertEqual(sheet['E12'].alignment.horizontal,'right')
        self.assertEqual(sheet['B9'].border.left.style,'thin')
        self.assertEqual(sheet['E14'].border.top.style,'thin')
        self.assertIn('Source:',sheet['H9'].value)
        self.assertIn('Reason:',sheet['H9'].value)
        self.assertTrue(all(c.comment is None for row in sheet for c in row))
        self.assertLessEqual(sheet.row_dimensions[12].height,20)
        for address in ('D30','E30','F30'):
            self.assertTrue(sheet[address].font.italic)
            self.assertEqual(rgb(address),'A6A6A6')
            self.assertTrue(sheet[address].font.bold)
        self.assertTrue(sheet['B30'].font.italic)
        book.close()

    def test_supported_cadence_choices_preserve_values_and_expose_period_frequency(self):
        baseline=compiler.compile_plan(initializer.make_plan(True))
        for cadence in ('quarter','half_year','annual'):
            plan=initializer.make_plan(True,cadence)
            self.assertTrue(all(p['frequency']==cadence for p in plan['periods']))
            built=compiler.compile_plan(plan)
            self.assertEqual(built['cadence'],cadence)
            self.assertEqual(result(built,'total_contribution','P1'),result(baseline,'total_contribution','P1'))


if __name__=='__main__':unittest.main()
