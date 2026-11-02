"""Research mode coverage, safe reuse and omission/sequence safeguards."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

PATH = Path(__file__).resolve().parents[1] / 'research-cycle/scripts/research_plan.py'
spec = importlib.util.spec_from_file_location('research_plan', PATH)
planner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planner)


def accounted(mode):
    plan = planner.make_plan(mode)
    plan['security'] = 'Synthetic issuer, ordinary shares'
    plan['informationCutoff'] = '2026-11-02T00:00:00Z'
    for group in ('stages', 'skills'):
        for entry in plan[group]:
            if entry.get('requirement') == 'outside-scope':
                continue
            if entry.get('requirement') == 'conditional':
                entry.update(disposition='not-applicable', reason='Synthetic case: trigger assessed and absent.')
            else:
                entry.update(disposition='reused' if mode == 'regular' else 'completed',
                             reason='Synthetic test reference, not actual research.',
                             references=['synthetic://reviewed-artifact'])
    return plan


class CoverageTests(unittest.TestCase):
    def test_new_plans_account_for_every_skill_but_never_start_complete(self):
        catalog, coverage = planner.configuration()
        for mode in coverage['modes']:
            plan = planner.make_plan(mode)
            self.assertEqual({e['id'] for e in plan['skills']}, {s['id'] for s in catalog['skills']})
            self.assertFalse(planner.check_plan(plan)['complete'])

    def test_eligible_reuse_can_complete_regular_review_without_forecast_rebuild(self):
        plan = accounted('regular')
        self.assertTrue(planner.check_plan(plan)['complete'])
        self.assertNotIn('model-revision', [e['id'] for e in plan['stages']])
        self.assertEqual(next(e for e in plan['skills'] if e['id'] == 'company-model')['disposition'], 'reused')

    def test_omitted_governance_or_undecided_conditional_work_prevents_complete_claim(self):
        for mutation in ('omit', 'skip', 'conditional'):
            plan = accounted('initiation')
            if mutation == 'omit':
                plan['skills'] = [e for e in plan['skills'] if e['id'] != 'corporate-governance']
            elif mutation == 'skip':
                next(e for e in plan['skills'] if e['id'] == 'corporate-governance')['disposition'] = 'not-applicable'
            else:
                next(e for e in plan['skills'] if e['id'] == 'management-questions')['disposition'] = 'pending'
            self.assertFalse(planner.check_plan(plan)['complete'])

    def test_required_scope_cannot_be_reclassified_to_avoid_audit(self):
        plan = accounted('major')
        next(e for e in plan['skills'] if e['id'] == 'financial-quality').update(requirement='conditional', disposition='not-applicable')
        self.assertFalse(planner.check_plan(plan)['complete'])

    def test_duplicate_ids_reordered_dependencies_and_stale_method_are_rejected(self):
        for mutation in ('duplicate', 'order', 'version'):
            plan = accounted('major')
            if mutation == 'duplicate':
                plan['skills'].append(copy.deepcopy(plan['skills'][0]))
            elif mutation == 'order':
                plan['stages'][1], plan['stages'][-1] = plan['stages'][-1], plan['stages'][1]
            else:
                plan['catalogVersion'] = 'old-method'
            self.assertFalse(planner.check_plan(plan)['complete'])

    def test_completion_or_reuse_requires_reason_and_artifact_reference(self):
        for field, value in [('reason', ''), ('references', []), ('references', [None])]:
            plan = accounted('regular')
            plan['stages'][0][field] = value
            self.assertFalse(planner.check_plan(plan)['complete'])

    def test_regular_forecast_revision_requires_affected_checks(self):
        plan = accounted('regular')
        plan['targetedForecastRevision']['needed'] = True
        self.assertFalse(planner.check_plan(plan)['complete'])
        plan['targetedForecastRevision'].update(riskReview='synthetic://risk', calculationRun='synthetic://run',
                                               audit='synthetic://audit', refreshedOutputs=['synthetic://valuation'])
        self.assertTrue(planner.check_plan(plan)['complete'])

    def test_malformed_status_does_not_crash_checker(self):
        plan = accounted('regular')
        plan['skills'][0]['disposition'] = []
        self.assertFalse(planner.check_plan(plan)['complete'])


if __name__ == '__main__':
    unittest.main()
