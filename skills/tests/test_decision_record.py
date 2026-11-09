"""Check actual artifact lineage and bound trigger text independently of reviewer approval."""
import copy
import json
from pathlib import Path
import sys
import unittest

sys.path[:0]=[str(Path(__file__).resolve().parent),str(Path(__file__).resolve().parents[1]/'report-layout/scripts')]
import test_release_check as f
import decision_record as dr
import publication_review as pr


class DecisionRecordTests(unittest.TestCase):
    def setUp(self):
        self.fixture=f.ReleaseCheckTests('test_clean_study_passes'); self.fixture.setUp(); self.addCleanup(self.fixture.doCleanups)
        self.root=self.fixture.dir; self.record=f.record(decisionRecord='evidence/decision.json'); self.spec=f.spec()
        self.decision=dr.synchronize(self.root,self.record,self.spec,{
            'invalidation':{'toSell':''},
            'boundText':[{'pointer':'/invalidation/toSell','template':'Test margin below {margin}.',
                          'inputs':{'margin':{'model':'Valuation!D7','style':'percent','decimals':2}}}],
            'valuationBasis':{'multiple':None},'bindings':[{'pointer':'/valuationBasis/multiple','model':'Valuation!D5'}]})
        self.write()

    def write(self): self.fixture.write('evidence/decision.json',json.dumps(self.decision))
    def check(self): return dr.check(self.root,self.record,self.spec)

    def test_current_decision_and_trigger_text_match_calculated_model(self):
        self.assertIn('agree',self.check())
        self.assertEqual(self.decision['invalidation']['toSell'],'Test margin below 3.55%.')
        self.assertIn('evidence/decision.json',pr.inputs(self.record))

    def test_stale_hash_and_old_trigger_fail_even_when_target_is_unchanged(self):
        for pointer,value in [('/model/workbookSHA256','old'),('/model/specSHA256','old'),
                              ('/invalidation/toSell','Test margin below 2.80%.'),('/valuationBasis/multiple',12),
                              ('/currency','USD'),('/targetDate','2028-11-06')]:
            saved=copy.deepcopy(self.decision)
            dr.set_at(self.decision,pointer,value); self.write()
            with self.assertRaisesRegex(ValueError,'stale'): self.check()
            self.decision=saved
        self.write()

    def test_workbook_or_spec_replacement_invalidates_record(self):
        path=self.root/self.record['workbook']; path.write_bytes(path.read_bytes()+b'changed')
        with self.assertRaisesRegex(ValueError,'workbookSHA256'): self.check()

    def test_same_outputs_do_not_excuse_a_changed_spec_fingerprint(self):
        path=self.root/self.record['spec']; path.write_bytes(path.read_bytes()+b'\n')
        with self.assertRaisesRegex(ValueError,'specSHA256'): self.check()

    def test_missing_decision_blocks_current_release_but_legacy_stays_explicit(self):
        (self.root/'evidence/decision.json').unlink()
        rec=f.record()
        checks,failed=f.rc.run(self.root,rec,model_check=f.passing_check)
        self.assertTrue(any(s.startswith('decision-record-current') for s in failed))
        self.assertFalse(any(s.startswith('decision-record-current') for s in f.rc.run(self.root,rec,model_check=f.passing_check,legacy=True)[1]))

    def test_refresh_changes_derived_values_without_approving_review_or_overwriting_judgment(self):
        self.decision['judgment']='Conditional central case; review source classification.'
        self.decision['invalidation']['toSell']='Old trigger'
        out=dr.synchronize(self.root,self.record,self.spec,self.decision)
        self.assertEqual(out['judgment'],self.decision['judgment'])
        self.assertEqual(out['invalidation']['toSell'],'Test margin below 3.55%.')
        self.assertFalse((self.root/pr.DEFAULT_PATH).exists())

    def test_duplicate_protected_and_executable_text_bindings_rejected(self):
        for mutate in (lambda d:d['bindings'].append(d['bindings'][0]),
                       lambda d:d['bindings'][0].update(pointer='/targetPrice'),
                       lambda d:d['boundText'][0].update(template='{margin.real}'),
                       lambda d:d['boundText'][0].update(template='{margin:.2f}')):
            case=copy.deepcopy(self.decision); mutate(case)
            with self.assertRaises(ValueError): dr.synchronize(self.root,self.record,self.spec,case)


if __name__=='__main__': unittest.main()
