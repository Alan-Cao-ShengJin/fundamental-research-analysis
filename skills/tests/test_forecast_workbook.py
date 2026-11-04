"""Portable export, independent saved-formula calculation, and drift detection."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from openpyxl import load_workbook

SCRIPTS=Path(__file__).resolve().parents[1]/'company-model/scripts'
sys.path.insert(0,str(SCRIPTS))
import forecast_workbook as workbook
import init_forecast_plan as initializer


class PortableWorkbookTests(unittest.TestCase):
    def test_plan_and_compiled_interface_both_reconcile_all_named_cells(self):
        plan=initializer.make_plan(True)
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'model.xlsx'
            result=workbook.build(plan,path)
            self.assertTrue(result['synchronized']);self.assertEqual(result['namedCellsChecked'],48)
            self.assertTrue(workbook.check(workbook.specification(plan),path)['synchronized'])
            book=load_workbook(path,data_only=True)
            self.assertAlmostEqual(book.active['E29'].value,913);book.close()
            with self.assertRaisesRegex(workbook.ModelError,'exists'):workbook.build(plan,path)

    def test_manual_input_formula_binding_and_machine_changes_fail_sync(self):
        for change in ('input','formula','binding','machine'):
            with self.subTest(change=change),tempfile.TemporaryDirectory() as folder:
                plan=initializer.make_plan(True);path=Path(folder)/'model.xlsx';workbook.build(plan,path)
                book=load_workbook(path)
                if change=='input':book.active['E9']=121
                elif change=='formula':book.active['E12']='=E9*E10+1'
                elif change=='binding':del book.defined_names[next(iter(book.defined_names))]
                else:plan['blocks'][0]['nodes'][0]['values']['P1']=121
                if change!='machine':book.save(path)
                book.close()
                before=path.read_bytes();report=workbook.check(plan,path)
                self.assertFalse(report['synchronized']);self.assertTrue(report['differences'])
                self.assertEqual(before,path.read_bytes()) # checks never rewrite user edits

    def test_perturb_rebuild_changes_outputs_and_preserves_actuals(self):
        plan=initializer.make_plan(True)
        with tempfile.TemporaryDirectory() as folder:
            original=Path(folder)/'original.xlsx';changed=Path(folder)/'changed.xlsx'
            workbook.build(plan,original)
            plan['blocks'][0]['nodes'][0]['values']['P1']=121;workbook.build(plan,changed)
            a=load_workbook(original,data_only=True);b=load_workbook(changed,data_only=True)
            self.assertEqual(a.active['D29'].value,b.active['D29'].value)
            self.assertAlmostEqual(b.active['E29'].value-a.active['E29'].value,47.3)
            a.close();b.close()

    def test_zero_input_is_valid_but_missing_or_undefined_input_cannot_be_exported(self):
        plan=initializer.make_plan(True)
        with tempfile.TemporaryDirectory() as folder:
            plan['blocks'][0]['nodes'][0]['values']['P1']=0
            self.assertTrue(workbook.build(plan,Path(folder)/'zero.xlsx')['synchronized'])
            plan['blocks'][0]['nodes'][0]['values']['P1']=None
            with self.assertRaisesRegex(workbook.ModelError,'missing inputs'):
                workbook.build(plan,Path(folder)/'missing.xlsx')
            self.assertFalse((Path(folder)/'missing.xlsx').exists())

    def test_cache_tampering_and_unsupported_formulas_are_detected(self):
        with tempfile.TemporaryDirectory() as folder:
            plan=initializer.make_plan(True);path=Path(folder)/'model.xlsx';workbook.build(plan,path)
            spec=workbook.specification(plan)
            values={c['address']:c['expected'] for r in spec['rows'] for c in r['cells']}
            values['E27']+=1;workbook.cache_values(path,values)
            self.assertIn('cache',{d['kind'] for d in workbook.check(plan,path)['differences']})
            book=load_workbook(path);book.active['E12']='=WEBSERVICE("https://example.invalid")'
            book.save(path);book.close()
            self.assertFalse(workbook.check(plan,path)['synchronized'])


if __name__=='__main__':unittest.main()
