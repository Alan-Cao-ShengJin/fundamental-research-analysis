"""Read-only tracing of saved workbook formulas."""
import hashlib,importlib.util,unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/'company-model'
spec=importlib.util.spec_from_file_location('trace_model',ROOT/'scripts/trace_model.py')
tracer=importlib.util.module_from_spec(spec);spec.loader.exec_module(tracer)


class TraceModelTests(unittest.TestCase):
    def test_tracer_preserves_source_and_exposes_depth_limits(self):
        path=ROOT/'assets/company-model-example.xlsx'
        before=hashlib.sha256(path.read_bytes()).hexdigest()
        full=tracer.trace(path,['Statements!F13'])  # gross margin = gross profit / revenue
        self.assertEqual(full['nodes']['Statements!F13']['kind'],'formula')
        self.assertIn('Statements!F12',full['nodes'])
        self.assertEqual(full['nodes']['Statements!F11']['kind'],'input_candidate')
        self.assertTrue(all(p['same_sheet'] for n in full['nodes'].values() for p in n['precedents']))
        limited=tracer.trace(path,['Statements!F13'],max_depth=0)
        self.assertTrue(limited['unresolved'])
        self.assertEqual(before,hashlib.sha256(path.read_bytes()).hexdigest())


if __name__=='__main__':unittest.main()
