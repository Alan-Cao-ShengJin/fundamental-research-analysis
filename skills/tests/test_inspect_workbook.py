"""Check generic, read-only workbook inspection with a synthetic OOXML fixture."""

import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location(
    "inspect_workbook", Path(__file__).resolve().parents[1] / "pip-company-model/scripts/inspect_workbook.py")
inspector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inspector)


class WorkbookInspectionTests(unittest.TestCase):
    def test_any_sheet_is_sampled_and_colours_are_not_financial_classifications(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "synthetic.xlsx"
            with zipfile.ZipFile(path, "w") as package:
                package.writestr("xl/workbook.xml", '''<workbook
                    xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
                    xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
                    <sheets><sheet name="Operating Schedule" sheetId="1" r:id="rId1"/></sheets>
                    </workbook>''')
                package.writestr("xl/_rels/workbook.xml.rels", '''<Relationships
                    xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
                    <Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>''')
                package.writestr("xl/styles.xml", '''<styleSheet
                    xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
                    <fonts count="1"><font><name val="Arial"/><color rgb="FF7030A0"/></font></fonts>
                    <fills count="0"/><cellXfs count="1"><xf fontId="0" fillId="0"/></cellXfs>
                    </styleSheet>''')
                package.writestr("xl/worksheets/sheet1.xml", '''<worksheet
                    xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
                    <sheetData><row r="1"><c r="A1" t="inlineStr"><is><t>Units</t></is></c>
                    <c r="B1"><v>10</v></c><c r="C1"><f>B1*2</f><v>20</v></c>
                    <c r="D1" t="e"><f>1/0</f><v>#DIV/0!</v></c></row></sheetData></worksheet>''')
            before = hashlib.sha256(path.read_bytes()).hexdigest()
            result = inspector.inspect(path)
            sheet = result["sheets"][0]
            self.assertEqual(result["sha256"], before)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), before)
            self.assertEqual(sheet["formula_count"], 2)
            self.assertEqual(sheet["formula_samples"][0]["formula"], "B1*2")
            self.assertEqual(sheet["cached_errors"][0]["cached_error"], "#DIV/0!")
            self.assertEqual(sheet["numeric_input_samples"], [
                {"cell": "B1", "value": "10", "font_color": {"rgb": "FF7030A0"}}])
            self.assertNotIn("assumption_samples", sheet)
            self.assertNotIn("actual_color_cells", sheet)


if __name__ == "__main__":
    unittest.main()
