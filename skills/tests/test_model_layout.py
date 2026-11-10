from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'company-model/scripts'))
import model_layout as layout
import model_workbook as mw

class ModelLayoutTests(unittest.TestCase):
    def test_half_year_driver_chain_is_generic_and_live(self):
        sheet=layout.Sheet('Operations',last='F',notes='H'); sheet.reserve('volume price sales')
        layout.header(sheet,'Operating forecast','units',company='Original synthetic example',periods={'D':'1H2030A','F':'2H2030E'})
        layout.period_row(sheet,'volume','Units','units',{'D':10,'F':12},['D','F'],['F'],note='Synthetic unit assumptions beside the chain.')
        layout.period_row(sheet,'price','Price','currency',{'D':3,'F':4},['D','F'],['F'])
        r=layout.period_row(sheet,'sales','Sales','currency',lambda c,r:f'={c}{sheet.R["volume"]}*{c}{sheet.R["price"]}',['D','F'],['F'],bold=True)
        engine=mw.Engine({'sheets':{'Operations':sheet.d}})
        self.assertEqual(engine.value('Operations',f'F{r}'),48)
        self.assertEqual(sheet.d['cells']['D6']['kind'],'actual'); self.assertEqual(sheet.d['cells']['F6']['kind'],'input')
        self.assertEqual(sheet.d['cells']['F5']['value'],'2H2030E')

if __name__=='__main__': unittest.main()
