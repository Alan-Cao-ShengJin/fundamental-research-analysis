from pathlib import Path
import sys
import tempfile
import unittest
import zipfile
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'company-model/scripts'))
import model_layout as layout
import model_text
import model_workbook as mw


class ModelTextTests(unittest.TestCase):
    def spec(self):
        sheet=layout.Sheet('Value',last='D')
        for addr,value in {'D6':100,'D7':120,'D8':'=D7/D6-1',
                           'D9':'=IF(D8>0.1,"Buy",IF(D8<-0.1,"Sell","Hold"))'}.items():sheet.put(addr,value)
        sheet.linked_note(10,'Target {target}; return {ret}; call {rating}.',{
            'target':{'model':'Value!D7','decimals':2},
            'ret':{'model':'Value!D8','style':'percent','decimals':1},
            'rating':{'model':'Value!D9','style':'text'}},'G')
        return {'sheets':{'Value':sheet.d}}

    def test_explanation_changes_with_target_and_call_without_retyping(self):
        spec=self.spec()
        self.assertEqual(mw.Engine(spec).value('Value','G10'),'Target 120.00; return 20.0%; call Buy.')
        spec['sheets']['Value']['cells']['D7']['value']=80
        self.assertEqual(mw.Engine(spec).value('Value','G10'),'Target 80.00; return -20.0%; call Sell.')
        self.assertTrue(spec['sheets']['Value']['cells']['G10']['wrap'])
        self.assertEqual(spec['sheets']['Value']['lastColumn'],'G')

    def test_visible_note_does_not_use_legacy_comment_only_column(self):
        sheet=layout.Sheet('M',notes='H')
        with self.assertRaisesRegex(ValueError,'visible'):sheet.linked_note(10,'{x}',{'x':{'model':'M!A1'}},'H')
        sheet.put('D6',100)
        with self.assertRaisesRegex(ValueError,'overwrite'):sheet.linked_note(6,'{x}',{'x':{'model':'M!A1'}},'D')

    def test_concat_precedence_and_text_rounding_match_known_worksheet_results(self):
        expected={'="T"&2+3':'T5','="t"&"x"="TX"':True,'=TEXT(2.675,"0.00")':'2.68',
                  '=TEXT(-0.0001,"0.0%")':'0.0%','=TEXT(1234.5,"#,##0.0")':'1,234.5',
                  '=TEXT(.125,"0.0%")':'12.5%'}
        for formula,value in expected.items():
            with self.subTest(formula=formula):self.assertEqual(mw.Engine({'sheets':{'M':{'cells':{'A1':{'value':formula}}}}}).value('M','A1'),value)

    def test_templates_and_formats_reject_unsupported_expressions(self):
        for template,inputs in [('No input',{'x':{'model':'M!A1'}}),('{x.real}',{'x':{'model':'M!A1'}}),
                                ('{x!r}',{'x':{'model':'M!A1'}}),('{x}',{'x':{'model':'M!A1+M!A2'}})]:
            with self.subTest(template=template),self.assertRaises(ValueError):model_text.formula(template,inputs)
        for code in ('yyyy-mm-dd','0.0000000','0.00;[Red]-0.00'):
            with self.assertRaises(ValueError):model_text.format_number(12,code)
        with self.assertRaisesRegex(ValueError,'supported subset'):model_text.concatenate('#N/A',' call')

    def test_quoted_literals_are_not_model_references(self):
        formula=model_text.formula('Literal "M!A99": {v}x',{'v':{'model':'M!A1','decimals':1}})
        spec={'sheets':{'M':{'cells':{'A1':{'value':2.5},'B1':{'value':formula}}}}}
        self.assertEqual(mw.Engine(spec).value('M','B1'),'Literal "M!A99": 2.5x')

    def test_formula_comparison_preserves_sheet_identity_and_literal_meaning(self):
        self.assertTrue(mw.same_formula("=TEXT('Value'!D7,\"0.00\")",'=text(Value!D7,"0.00")'))
        self.assertTrue(mw.same_formula('= 1 + 2','=1+2'))
        self.assertFalse(mw.same_formula("='Sales'!D7","='Costs'!D7"))
        self.assertFalse(mw.same_formula("='My Sheet'!D7","='MySheet'!D7"))
        self.assertFalse(mw.same_formula('="Buy now"','="Buynow"'))
        self.assertFalse(mw.same_formula('="Buy"','="BUY"'))

    def test_workbook_check_rejects_a_stale_explanation_cache(self):
        # Synthetic cache injection exercises verification; it is not native Excel recalculation.
        spec=self.spec();ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        with tempfile.TemporaryDirectory() as td:
            book=Path(td)/'model.xlsx';mw.build(spec,book)
            values=mw.calculate(spec)['Model']['cells']
            with zipfile.ZipFile(book) as z: content={n:z.read(n) for n in z.namelist()}
            tree=ET.fromstring(content['xl/worksheets/sheet1.xml'])
            for cell in tree.findall('.//m:c',ns):
                if cell.find('m:f',ns) is None:continue
                value=values['Value!'+cell.attrib['r']]
                if isinstance(value,str):cell.set('t','str')
                else:cell.attrib.pop('t',None)
                cached=cell.find('m:v',ns)
                if cached is None:cached=ET.SubElement(cell,'{'+ns['m']+'}v')
                cached.text=str(value)
            content['xl/worksheets/sheet1.xml']=ET.tostring(tree)
            with zipfile.ZipFile(book,'w') as z:
                for n,data in content.items():z.writestr(n,data)
            self.assertTrue(mw.check(spec,book)['passed'])
            tree.find('.//m:c[@r="G10"]/m:v',ns).text='Target 120.00; return 20.0%; call Hold.'
            content['xl/worksheets/sheet1.xml']=ET.tostring(tree)
            with zipfile.ZipFile(book,'w') as z:
                for n,data in content.items():z.writestr(n,data)
            issues=mw.check(spec,book)['issues']
            self.assertTrue(any(i.get('cell')=='Value!G10' for i in issues))


if __name__=='__main__':unittest.main()
