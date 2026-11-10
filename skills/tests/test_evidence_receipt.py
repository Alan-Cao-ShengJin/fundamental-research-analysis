import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest
path=Path(__file__).resolve().parents[1]/'evidence-intake/scripts/evidence_receipt.py'
spec=importlib.util.spec_from_file_location('evidence_receipt',path); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)

class EvidenceReceiptTests(unittest.TestCase):
    def test_exact_bytes_and_honest_compilation_provenance_without_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/'source.json'; source.write_bytes(b'{"observations": [1, 2]}\r\n'); study=root/'study'
            record=module.retain(study,source,'evidence/source.json','SyntheticProvider','manual-compilation','Original synthetic tool locator')
            self.assertEqual(record['sha256'],hashlib.sha256(source.read_bytes()).hexdigest())
            self.assertFalse(record['authenticityVerified']); self.assertEqual((study/'evidence/source.json').read_bytes(),source.read_bytes())
            with self.assertRaises(FileExistsError): module.retain(study,source,'evidence/source.json','SyntheticProvider','connector-output-file','locator')
            with self.assertRaises(ValueError): module.retain(study,source,'../outside.json','Provider','manual-compilation','locator')

if __name__=='__main__': unittest.main()
