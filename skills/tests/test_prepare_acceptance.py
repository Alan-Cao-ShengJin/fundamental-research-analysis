"""Acceptance setup isolates the raw fixture and refuses to overwrite a prior run."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

script = Path(__file__).resolve().parents[1] / 'evals/scripts/prepare_acceptance.py'
loader = importlib.util.spec_from_file_location('prepare_acceptance', script)
setup = importlib.util.module_from_spec(loader)
loader.loader.exec_module(setup)


class AcceptanceSetupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'repo'
        for name, text in {
            'CLAUDE.md': 'Production bootstrap',
            'skills/model/SKILL.md': 'Production model guidance',
            'skills/tests/test_answer.py': 'Do not give the author test answers',
            'skills/evals/fixtures/example/pack.md': 'Invented raw evidence',
            'skills/evals/fixtures/example/facts.json': '{"reported":100}',
            'skills/evals/fixtures/answers/example.md': 'Expected answer',
            'research/previous.md': 'Earlier research',
            'MESSAGE_BOARD.md': 'Earlier critique',
            'node_modules/zod/package.json': '{"version":"4.6.7"}',
        }.items():
            path = self.repo / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(text)
        self.destination, self.audit = self.root / 'fresh-author', self.root / 'host-audit'

    def prepare(self, **overrides):
        args = dict(repo=self.repo, pack='example', destination=self.destination, audit=self.audit,
                    request='initiation on Example; evidence in inbox/example/pack.md',
                    evaluation_time='2030-01-15T12:00:00Z')
        return setup.prepare(**dict(args, **overrides))

    def test_only_raw_evidence_and_production_resources_reach_the_author(self):
        result = self.prepare()
        self.assertTrue(result['rawPackUnchanged'])
        for omitted in ('skills/evals', 'skills/tests', 'research', 'MESSAGE_BOARD.md'):
            self.assertFalse((self.destination / omitted).exists())
        self.assertEqual((self.destination / 'inbox/example/pack.md').read_text(), 'Invented raw evidence')
        self.assertTrue((self.destination / 'inbox/example/facts.json').is_file())
        self.assertTrue((self.destination / 'skills/model/SKILL.md').is_file())
        self.assertTrue((self.destination / 'node_modules/zod/package.json').is_file())
        manifest = json.loads((self.audit / 'prepared-manifest.json').read_text())
        self.assertEqual(manifest['maxReviewRounds'], 2)
        self.assertEqual(manifest['request'], (self.audit / 'author-request.txt').read_text().strip())
        self.assertEqual(manifest['evaluation']['now'], '2030-01-15T12:00:00Z')
        self.assertNotEqual(manifest['preparedAt'], manifest['evaluation']['now'])

    def test_existing_run_and_audit_leak_are_refused(self):
        self.destination.mkdir(); sentinel = self.destination / 'keep.txt'; sentinel.write_text('keep')
        with self.assertRaises(FileExistsError):
            self.prepare()
        self.assertEqual(sentinel.read_text(), 'keep')
        with self.assertRaisesRegex(ValueError, 'author must not receive'):
            self.prepare(destination=self.root / 'another', audit=self.root / 'another/answers')

    def test_bad_clock_or_pack_is_refused_before_creating_a_workspace(self):
        with self.assertRaisesRegex(ValueError, 'timezone'):
            self.prepare(evaluation_time='2030-01-15T12:00:00')
        with self.assertRaises(ValueError):
            self.prepare(pack='../../../research')
        self.assertFalse(self.destination.exists())


if __name__ == '__main__':
    unittest.main()
