"""Raw synthetic accounting reconciles; targets and discretionary forecasts are not stipulated."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS=Path(__file__).resolve().parents[1]/'evals/scripts'
def module(name):
    loader=importlib.util.spec_from_file_location(name,SCRIPTS/(name+'.py'))
    result=importlib.util.module_from_spec(loader); loader.loader.exec_module(result); return result
fixture=module('build_alder_fixtures')
stager=module('stage_update_acceptance')


class DistributorFactsTests(unittest.TestCase):
    def test_balance_sheets_and_cash_movements_reconcile(self):
        history,q1,h1,balances,cash,pe=fixture.data()
        for name,b in balances.items():
            assets=sum(b[k] for k in ('cash','receivables','inventory','ppe','rou','otherAssets'))
            claims=sum(b[k] for k in ('payables','accruals','debt','leases','parentEquity','minorityEquity'))
            self.assertAlmostEqual(assets,claims,places=8,msg=name)
        for name in ('FY2025','FY2026','1H FY2027'):
            c=cash[name]
            closing=c['openingCash']+c['operating']-c['capex']-c['leasePrincipal']-c['parentDividends']-c['minorityDividends']+c['netBorrowing']
            self.assertAlmostEqual(closing,c['closingCash'],places=8,msg=name)
        self.assertEqual(len(pe),36)

    def test_ownership_one_off_and_access_are_distinct(self):
        history,q1,h1,balances,cash,pe=fixture.data()
        for row in history+[q1,h1]:
            expected=.4*.8*(row['jointGrossProfit']-row['jointOpex'])
            self.assertAlmostEqual(expected,row['minorityProfit'])
            self.assertAlmostEqual(row['eps']*100,row['attributableProfit'])
        reported=sum(row['eps'] for row in history[-2:])
        self.assertAlmostEqual(reported,1.16944)
        self.assertAlmostEqual(reported-13.65*.8/100,1.06024)
        c=cash['FY2026']; group=c['operating']-c['capex']-c['leasePrincipal']
        economic=group-.4*c['jointAfterInvestment']
        available=group-c['jointAfterInvestment']+.6*c['jointDividends']
        self.assertAlmostEqual(group,100.048)
        self.assertAlmostEqual(economic,89.248)
        self.assertAlmostEqual(available,82.648)
        self.assertAlmostEqual(economic-available,6.6)

    def test_cumulative_update_does_not_count_q1_twice(self):
        history,q1,h1,balances,cash,pe=fixture.data()
        self.assertAlmostEqual(h1['eps'],.564)
        self.assertAlmostEqual(cash['1H FY2027']['operating']-cash['1Q FY2027']['operating'],5.32)
        self.assertAlmostEqual(h1['attributableProfit']-q1['attributableProfit'],28.32)
        self.assertAlmostEqual(132.048+22-16,cash['FY2026']['operating'])
        self.assertAlmostEqual(64.72+12-15+22+2+2,cash['1H FY2027']['operating'])


class UpdateStagingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        root=Path(self.temp.name)
        self.study=root/'source/research/example/2030-01-15-initiation'
        (self.study/'deliverables').mkdir(parents=True); (self.study/'evidence').mkdir()
        (self.study/'deliverables/release.json').write_text(json.dumps({'cutoff':'2030-01-15','status':'awaiting-review'}))
        (self.study/'evidence/draft-review.json').write_text(json.dumps({'handoff':{
            'status':'partial','checks':[{'name':'argument-support','result':'fail'}],'criticalUnknowns':[]}}))
        self.destination=root/'update'; self.destination.mkdir()
        (self.destination/'.research-evaluation.json').write_text('{"now":"2030-02-15T12:00:00Z"}')
        self.audit=root/'host-audit'

    def test_valid_model_does_not_make_a_rejected_conclusion_reusable(self):
        with patch.object(stager,'verify_model',return_value={'passed':True,'issues':[]}):
            result=stager.stage(self.study,self.destination,self.audit)
        self.assertFalse(result['conclusionReusable'])
        components=json.loads((Path(result['stagedStudy']).parent/'BASELINE_COMPONENTS.json').read_text())
        self.assertEqual(components['unresolvedReviewChecks'][0]['result'],'fail')
        self.assertTrue((self.audit/'baseline-manifest.json').is_file())
        with self.assertRaises(FileExistsError):
            stager.stage(self.study,self.destination,self.audit)

    def test_unreproducible_model_and_wrong_update_clock_block_staging(self):
        with patch.object(stager,'verify_model',return_value={'passed':False,'issues':['unreproducible']}):
            with self.assertRaisesRegex(ValueError,'does not reproduce'):
                stager.stage(self.study,self.destination,self.audit)
        (self.destination/'.research-evaluation.json').write_text('{"now":"2029-01-01T12:00:00Z"}')
        with self.assertRaisesRegex(ValueError,'predate'):
            stager.stage(self.study,self.destination,self.audit)

    def test_selected_raw_evidence_is_preserved_for_the_update_backend(self):
        evidence=self.study.parents[2]/'inbox/example'; evidence.mkdir(parents=True)
        (evidence/'facts.json').write_text('{"reported":100}')
        with patch.object(stager,'verify_model',return_value={'passed':True,'issues':[]}):
            stager.stage(self.study,self.destination,self.audit,evidence)
        self.assertEqual((self.destination/'inbox/example/facts.json').read_bytes(),(evidence/'facts.json').read_bytes())


if __name__=='__main__':
    unittest.main()
