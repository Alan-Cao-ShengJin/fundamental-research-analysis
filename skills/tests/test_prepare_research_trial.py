import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT=Path(__file__).resolve().parents[1]/'evals/scripts/prepare_research_trial.py'
spec=importlib.util.spec_from_file_location('real_trial',SCRIPT)
trial=importlib.util.module_from_spec(spec); spec.loader.exec_module(trial)


class PrepareResearchTrialTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name); self.repo=self.root/'repo'; self.repo.mkdir()
        (self.repo/'CLAUDE.md').write_text('Use skills.')
        for directory in ('skills/example','skills/tests','skills/evals/fixtures/answers','research/old'):
            p=self.repo/directory; p.mkdir(parents=True); (p/'keep.txt').write_text(directory)
        (self.repo/'.env.secret').write_text('not copied')
        self.source=self.root/'snapshot'; self.source.mkdir(); (self.source/'filing.txt').write_bytes(b'Original source\r\n')
        self.dest=self.root/'author'; self.audit=self.root/'host'

    def prepare(self): return trial.prepare(self.repo,self.source,self.dest,self.audit,'initiation on XYZ','2026-11-09','XYZ')

    def test_copies_raw_bytes_and_skills_without_answers_prior_work_or_fake_clock(self):
        self.prepare()
        self.assertEqual((self.dest/'inbox/evidence-snapshot/filing.txt').read_bytes(),b'Original source\r\n')
        self.assertTrue((self.dest/'skills/example/keep.txt').is_file())
        for path in ('skills/tests','skills/evals','research','.env.secret','.research-evaluation.json'):
            self.assertFalse((self.dest/path).exists())
        manifest=json.loads((self.audit/'prepared-manifest.json').read_text())
        self.assertEqual(manifest['status'],'prepared-unrun'); self.assertEqual(manifest['maxReviewRounds'],2)
        self.assertFalse((self.dest/'prepared-manifest.json').exists())

    def test_invalid_paths_dates_and_existing_destination_fail_before_writes(self):
        with self.assertRaises(ValueError): trial.prepare(self.repo,self.source,self.dest,self.audit,'request','bad-date','XYZ')
        with self.assertRaises(ValueError): trial.prepare(self.repo,self.source,self.repo/'nested',self.audit,'request','2026-11-09','XYZ')
        with self.assertRaises(ValueError): trial.prepare(self.repo,self.source,self.dest,self.dest/'host','request','2026-11-09','XYZ')
        self.assertFalse(self.dest.exists()); self.dest.mkdir()
        with self.assertRaises(FileExistsError): self.prepare()

    def test_snapshot_cannot_contain_old_research_or_credentials(self):
        (self.source/'research').mkdir()
        with self.assertRaisesRegex(ValueError,'forbidden context'): self.prepare()
        self.assertFalse(self.dest.exists())


if __name__=='__main__': unittest.main()
