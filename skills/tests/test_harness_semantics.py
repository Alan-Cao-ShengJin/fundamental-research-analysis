"""Independent counterexamples for financial semantics and safe workflow transitions."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'report-layout/scripts'),str(ROOT/'company-model/scripts')]
import model_workbook as mw
import release_check as rc
import publication_review as pr
import research_rules as rules
import review_attempts as attempts
import decision_record as decisions
import model_review
import presentation_confirmation as confirmation
import test_release_check as fx

class WorksheetSemanticsTests(unittest.TestCase):
    def test_known_worksheet_expectations_not_python_operator_results(self):
        examples={'=ROUND(2.5,0)':3,'=ROUND(-2.5,0)':-3,'=ROUND(2.15,1)':2.2,'=ROUND(-1.475,2)':-1.48,
                  '=-3^2':9,'=2^3^2':64,'=-(3^2)':-9,'=2^(3^2)':512,'=IF("base"="Base",1,0)':1,
                  '=IF("A1"="a1",2,0)':2,'=IF(TRUE,4,5)':4,'=50%*4':2,'=SUM(TRUE,1)':2,'=SUM("2",1)':3,'=IF(TRUE=1,1,0)':0}
        for formula,expected in examples.items():
            with self.subTest(formula=formula): self.assertEqual(mw.Engine({'sheets':{'M':{'cells':{'A1':{'value':formula}}}}}).value('M','A1'),expected)

    def test_sensitivity_mode_must_be_exact(self):
        s={'sheets':{'M':{'cells':{'A1':{'value':100}}}}}
        with self.assertRaisesRegex(mw.ModelError,'mode'): mw.shocked(s,['M!A1'],5,'Add')
        self.assertEqual(mw.shocked(s,['M!A1'],5,'add')['sheets']['M']['cells']['A1']['value'],105)
        self.assertEqual(mw.shocked(s,['M!A1'],.05,'scale')['sheets']['M']['cells']['A1']['value'],105)

    def test_period_identity_and_unambiguous_dates(self):
        self.assertTrue(rc.same_period('FY27E','FY2027E'))
        for a in ('2H27E','Q2 2027E','FY2027A'): self.assertFalse(rc.same_period(a,'FY2027E'))
        self.assertEqual(str(rc.parse_date('2026/11/05')),'2026-11-05')
        self.assertEqual(str(rc.parse_date('HK$79.25 at the 5 Nov 2026 close')),'2026-11-05')
        with self.assertRaises(ValueError): rc.parse_date('05/11/2026')

    def test_target_adapters_reconcile_owner_claim_instead_of_target_alias(self):
        import valuation_methods
        values={'V!A1':100,'V!A2':10,'V!A3':50,'V!A4':20,'V!A5':10,'V!A6':20,'V!A7':1,'V!A8':500,'V!A9':-.0,'V!A10':.5,'V!A11':48}
        spec={'sheets':{'V':{'cells':{ref.split('!')[1]:{'value':value} for ref,value in values.items()}}}}
        b=dict(zip(('enterpriseMetric','targetMultiple','netDebt','nonOperatingValue','minorityValue','shares','fx'),['V!A'+str(i) for i in range(1,8)])); b['target']='V!A11'
        rec={'method':'EV/EBITDA','bindings':b,'_spec':spec}
        self.assertEqual(valuation_methods.target(rec,values.__getitem__),48)
        rec.update(method='NAV',valuationParts=[{'id':'owned-asset','valueRef':'V!A8','ownershipRef':'V!A10','rationale':'Original synthetic 50% owner claim.'}])
        self.assertEqual(valuation_methods.target(rec,values.__getitem__),12.5)
        rec['valuationParts'][0]['valueRef']='V!A11'
        with self.assertRaisesRegex(ValueError,'target'): valuation_methods.target(rec,values.__getitem__)

class HarnessWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.f=fx.ReleaseCheckTests('test_clean_study_passes'); self.f.setUp(); self.addCleanup(self.f.doCleanups)
        self.study=self.f.dir; self.record=fx.record()
    def prepared(self):
        pr.prepare(self.study,self.record); return fx.complete_review(self.study)
    def save(self,p): (self.study/pr.DEFAULT_PATH).write_text(json.dumps(p),encoding='utf-8')
    def failures(self): return [c['name'] for c in pr.check(self.study,self.record,fx.spec(),self.study/self.record['workbook']) if c['result']=='fail']

    def test_model_review_is_required_before_writing_or_publication(self):
        p=self.study/model_review.PATH; value=json.loads(p.read_text()); value['handoff']['status']='partial'; p.write_text(json.dumps(value))
        with self.assertRaisesRegex(ValueError,'model challenge'): pr.prepare(self.study,self.record)
        with self.assertRaisesRegex(ValueError,'model challenge'): pr.writing_packet(self.study,['model/spec.json'])

    def test_model_review_history_cannot_be_reset_by_deleting_the_packet(self):
        path=self.study/model_review.PATH; path.unlink()
        with self.assertRaisesRegex(ValueError,'Missing model review'): model_review.prepare(self.study,'model/spec.json','deliverables/model.xlsx',[],self.record['security'],self.record['cutoff'])

    def test_model_review_cannot_certify_a_different_published_model(self):
        import shutil
        for field,other in (('spec','model/other.json'),('workbook','deliverables/other.xlsx')):
            with self.subTest(field=field):
                shutil.copyfile(self.study/self.record[field],self.study/other)
                changed=dict(self.record,**{field:other})
                with self.assertRaisesRegex(ValueError,'published spec and workbook'):
                    pr.preflight(self.study,changed)
        self.assertIn('complete',model_review.verify(self.study,self.record))
        self.assertEqual(len(model_review.starts(self.study)),1)

    def test_model_review_declared_model_must_be_in_frozen_inputs(self):
        path=self.study/model_review.PATH; p=json.loads(path.read_text())
        del p['inputs'][p['workbook']]; path.write_text(json.dumps(p))
        with self.assertRaisesRegex(ValueError,'freeze its declared'):
            model_review.verify(self.study,self.record)

    def test_writer_receives_the_reviewed_model_even_when_caller_omits_it(self):
        path=pr.writing_packet(self.study,['evidence/decision.json'])
        packet=json.loads(path.read_text())
        for rel in ('model/spec.json','deliverables/model.xlsx',model_review.PATH):
            self.assertEqual(packet['inputs'][rel],rc.sha256(self.study/rel))

    def test_model_review_started_budget_is_retained_across_preparations(self):
        model_review.prepare(self.study,'model/spec.json','deliverables/model.xlsx',[],self.record['security'],self.record['cutoff'])
        model_review.begin(self.study,'second-synthetic-reader')
        path=self.study/model_review.PATH; before=path.read_bytes()
        with self.assertRaisesRegex(ValueError,'budget exhausted'): model_review.prepare(self.study,'model/spec.json','deliverables/model.xlsx',[],self.record['security'],self.record['cutoff'])
        self.assertEqual(path.read_bytes(),before); self.assertEqual(len(model_review.starts(self.study)),2)

    def test_unstarted_model_preparation_neither_spends_a_round_nor_invents_findings(self):
        for _ in range(2):
            path=model_review.prepare(self.study,'model/spec.json','deliverables/model.xlsx',[],self.record['security'],self.record['cutoff'])
        value=json.loads(path.read_text()); self.assertEqual(value['attempt'],2); self.assertEqual(value['priorFindings'],[])
        self.assertEqual(len(model_review.starts(self.study)),1)

    def test_begin_does_not_spend_a_review_on_stale_live_inputs(self):
        pr.prepare(self.study,self.record); self.f.write('deliverables/report.html','Changed')
        with self.assertRaisesRegex(ValueError,'no attempt started'): attempts.begin(self.study,self.record,'reader')
        self.assertEqual(attempts.state(self.study)['used'],0)

    def test_semantically_identical_sync_preserves_reviewed_bytes(self):
        path=self.study/'evidence/decision.json'; path.write_text(json.dumps(json.loads(path.read_text()),separators=(',',':')))
        self.f.write('deliverables/release.json',json.dumps(self.record)); self.prepared(); before=path.read_bytes()
        with patch.object(sys,'argv',['decision_record.py','sync',str(self.study)]),contextlib.redirect_stdout(io.StringIO()): decisions.main()
        self.assertEqual(path.read_bytes(),before); self.assertEqual(self.failures(),[])

    def test_companions_are_frozen_and_drift_blocks(self):
        self.f.write('deliverables/companion.txt','A distributed file'); self.record['deliverables'].append('deliverables/companion.txt')
        p=self.prepared(); self.assertIn('deliverables/companion.txt',p['reviewedFiles'])
        self.f.write('deliverables/companion.txt','Different'); self.assertIn('draft-review-files-current',self.failures())

    def test_unchanged_snapshot_inputs_share_content_objects(self):
        pr.prepare(self.study,self.record)
        objects=self.study/'.review-objects'; before={p.name for p in objects.iterdir()}
        pr.prepare(self.study,self.record,revise=True)
        self.assertEqual({p.name for p in objects.iterdir()},before)

    def test_title_cannot_bypass_initiation_financial_summary(self):
        self.f.write('deliverables/report.html','<title>Research Note</title>'+fx.report_html().replace('data-financial-summary="true"',''))
        self.prepared(); self.assertIn('initiation-financial-summary',self.failures())

    def test_minor_cosmetic_findings_can_be_nonblocking_but_material_ones_block(self):
        p=self.prepared(); c=next(c for c in p['handoff']['checks'] if c['name']=='visual-inspection')
        c.update(result='fail',blocking=False,detail='A cosmetic caption gap; values and readability are intact.'); self.save(p)
        self.assertEqual(self.failures(),[])
        c.update(blocking=True,detail='A clipped minus sign reverses the economic meaning.'); self.save(p)
        self.assertIn('draft-review-required-checks',self.failures())

    def test_confirmation_is_actual_bounded_reader_work_and_cannot_clear_analysis_changes(self):
        p=self.prepared(); c=next(c for c in p['handoff']['checks'] if c['name']=='visual-inspection'); c.update(result='fail',detail='Move caption beside its table.'); self.save(p)
        html=self.study/'deliverables/report.html'; html.write_text('<style>p{margin:1em}</style>'+html.read_text())
        receipt=confirmation.prepare(self.study,self.record)
        self.assertIn('presentation-confirmation',self.failures())
        value=json.loads(receipt.read_text()); value['handoff']['status']='complete'; value['handoff']['summary']='Synthetic reader confirmed the exact content-equivalent presentation correction.'
        for c in value['handoff']['checks']: c.update(result='pass',detail='Synthetic confirmation test double only.')
        receipt.write_text(json.dumps(value)); self.assertEqual(self.failures(),[])
        self.assertEqual(attempts.state(self.study)['used'],1)
        with self.assertRaisesRegex(ValueError,'One confirmation'): confirmation.prepare(self.study,self.record)
        self.f.write('model/spec.json','Changed analytical input')
        self.assertIn('presentation-confirmation',self.failures())

    def test_nonvalue_assertion_does_not_verify_a_printed_value(self):
        import report_layout as layout
        self.f.write('deliverables/report.html',fx.report_html()+layout.bound_measure('bad',.99,'FY2027E','ratio',style='percent'))
        p=self.prepared(); p['claimAssertions']=[{'id':'fake','kind':'evidence-scope','claimId':'fixture','location':'Synthetic scope only',
            'sourceIds':['file-0'],'rationale':'Scope does not check a number.','sourceScopes':{'file-0':'company'},'conclusionScope':'company',
            'displays':[{'document':'deliverables/report.html','id':'bad'}]}]
        p['coverage']['claim-support']={'status':'checked','assertionIds':['fake']}; self.save(p)
        self.assertIn('rendered-measures-covered:deliverables/report.html',self.failures())

    def test_published_yield_and_scenario_fields_cannot_omit_model_bindings(self):
        r=fx.record(); r['bindings'].pop('dividendYield'); r['bindings'].pop('bearTarget')
        checks,fails=rc.run(self.study,r,model_check=fx.passing_check,legacy=True)
        self.assertTrue(any(x.startswith('brief-yield-binding-required') for x in fails))
        self.assertTrue(any(x.startswith('brief-bearTarget-binding-required') for x in fails))

    def test_half_year_eps_heading_is_rejected_by_the_actual_release_period_gate(self):
        from openpyxl import load_workbook
        spec=fx.spec(); spec['sheets']['Statements']['cells']['I5']['value']='2H27E'
        self.f.write('model/spec.json',json.dumps(spec))
        path=self.study/self.record['workbook']; workbook=load_workbook(path); workbook['Statements']['I5']='2H27E'; workbook.save(path)
        _,fails=rc.run(self.study,self.record,model_check=fx.passing_check,legacy=True)
        self.assertTrue(any(x.startswith('forward-eps-column-is-declared-period') for x in fails))

    def test_refused_prepare_preserves_prior_bytes_and_record(self):
        self.prepared(); r=dict(self.record,zipPath='deliverables/old.zip',status='validated')
        path=self.study/'deliverables/release.json'; path.write_text(json.dumps(r)); before=path.read_bytes()
        archive=self.study/'deliverables/old.zip'; archive.write_bytes(b'original')
        with patch.object(sys,'argv',['publication_review.py','prepare',str(self.study)]):
            with self.assertRaises(FileExistsError): pr.main()
        self.assertEqual(archive.read_bytes(),b'original'); self.assertEqual(path.read_bytes(),before)

    def test_session_cutoff_before_utc_midnight_is_valid_in_its_declared_timezone(self):
        from datetime import datetime,timezone
        class Clock(datetime):
            @classmethod
            def now(cls,tz=None): return cls(2026,11,9,18,30,tzinfo=timezone.utc)
        r=dict(self.record,cutoff='2026-11-10',timezone='Asia/Singapore')
        path=self.study/model_review.PATH; p=json.loads(path.read_text()); p['handoff']['asOf']='2026-11-10T00:00:00+08:00'; path.write_text(json.dumps(p))
        with patch.object(pr,'datetime',Clock):
            prepared=pr.prepare(self.study,r)
        value=json.loads(prepared.read_text()); self.assertEqual(value['handoff']['asOf'],'2026-11-10T02:30:00+08:00')

    def test_price_only_writing_can_reuse_a_baseline_without_another_model_reader(self):
        path=self.study/model_review.PATH; path.unlink()
        result=pr.writing_packet(self.study,['model/spec.json'],research_mode='regular-review')
        self.assertTrue(result.is_file())
        with self.assertRaises(FileNotFoundError): pr.writing_packet(self.study,['model/spec.json'],research_mode='regular-review',model_changed=True)

class PinnedRulesTests(unittest.TestCase):
    def test_tests_do_not_change_production_identity_and_archived_code_actually_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/'source/skills'; source.mkdir(parents=True); study=root/'study'; study.mkdir()
            (source/'version.py').write_text('print("PINNED_V1")\n'); (source/'tests').mkdir(); (source/'tests/test.txt').write_text('test')
            with patch.object(rules,'SKILLS',source):
                before=rules.fingerprint(); (source/'tests/test.txt').write_text('test\n'); self.assertEqual(rules.fingerprint(),before)
                rules.pin(study); (source/'version.py').write_text('raise RuntimeError("LIVE_V2_MUST_NOT_RUN")\n')
                with self.assertRaisesRegex(ValueError,'Different pinned'): rules.require_current(study)
                self.assertEqual(rules.run(study,'version.py'),0)
