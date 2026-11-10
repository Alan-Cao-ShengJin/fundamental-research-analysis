"""Economic non-applicability is different from an applicable claim missing its implementation."""
import copy
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'report-layout/scripts'))
from financial_coverage import verify


class FinancialCoverageTests(unittest.TestCase):
    def setUp(self):
        self.packet={'handoff':{'claims':[{'id':'cash-claim'}]},'financialAssertions':[{'id':'cash-test','kind':'cash-coverage'}]}
        self.valid={'applicability':'applicable','status':'checked','assertionIds':['cash-test'],'claimIds':['cash-claim']}

    def test_applicable_verified_claim_passes(self): self.assertTrue(verify('cash-coverage',self.valid,self.packet)[0])

    def test_applicable_but_unbound_is_not_non_applicable(self):
        bad=dict(self.valid,status='not-applicable',assertionIds=[],reason='No coverage row was built.')
        self.assertFalse(verify('cash-coverage',bad,self.packet)[0])
        bad['applicability']='not-applicable'
        self.assertFalse(verify('cash-coverage',bad,self.packet)[0])

    def test_genuine_non_applicability_passes_without_manufacturing_a_model(self):
        entry={'applicability':'not-applicable','status':'not-applicable','reason':'No convertible instrument or published conversion claim.',
               'claimIds':[],'assertionIds':[]}
        self.assertTrue(verify('financing',entry,self.packet)[0])
        entry['reason']=''
        self.assertFalse(verify('financing',entry,self.packet)[0])

    def test_unverified_omitted_duplicate_or_unknown_claim_links_fail(self):
        for edit in (dict(status='not-verified'),dict(assertionIds=[]),dict(assertionIds=['cash-test']*2),
                     dict(claimIds=[]),dict(claimIds=['not-registered']),dict(applicability='undetermined')):
            self.assertFalse(verify('cash-coverage',dict(self.valid,**edit),self.packet)[0])


if __name__=='__main__': unittest.main()
