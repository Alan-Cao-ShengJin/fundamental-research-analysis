"""Rendered figures must match the declared source transformation, not merely a ledger."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'report-layout/scripts'))
from display_bindings import bound_measure,check_displays,measure
from publication_review import Figures


class DisplayBindingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        self.display={'document':'report.html','id':'payout','period':'FY1–2','unit':'ratio',
                      'style':'percent','decimals':0,'transform':'magnitude','order':'ascending'}
        self.values=[-.53,-.51]
        self.packet={'reviewedFiles':{'report.html':'frozen-by-wrapper'}}

    def write(self, text): (self.root/'report.html').write_text(text,encoding='utf-8')
    def render(self):
        d=self.display
        return bound_measure(d['id'],self.values,d['period'],d['unit'],style=d['style'],decimals=d['decimals'],transform=d['transform'],order=d['order'])
    def check(self): return check_displays(self.root,[self.display],self.values,self.packet)

    def test_cash_sign_preserved_while_payout_magnitude_is_explicit(self):
        self.assertEqual(measure([-20]),'-20.00')
        self.assertEqual(measure(self.values,'percent',0,'magnitude','ascending'),'51%–53%')
        self.write(self.render()); self.assertIn('agree',self.check())

    def test_correct_raw_values_cannot_hide_wrong_visible_sign_or_range(self):
        for text in ('-53%–-51%','51%–54%','53%–51%'):
            self.write(self.render().replace('51%–53%',text))
            with self.assertRaisesRegex(ValueError,'Visible'): self.check()

    def test_scope_and_transformation_and_actual_bound_values_must_match(self):
        for old,new in [('data-unit="ratio"','data-unit="currency"'),('data-transform="magnitude"','data-transform="identity"'),
                        ('[-0.53, -0.51]','[-0.54, -0.51]')]:
            self.write(self.render().replace(old,new))
            with self.assertRaises(ValueError): self.check()

    def test_nearby_value_or_another_document_is_not_a_binding(self):
        self.write('<p>51%–53%</p>')
        with self.assertRaisesRegex(ValueError,'No rendered'): self.check()
        self.display['document']='other.html'
        with self.assertRaisesRegex(ValueError,'frozen HTML'): self.check()

    def test_repeated_occurrences_and_nested_style_spans_are_all_checked(self):
        good=self.render().replace('51%–53%','<span class="em">51%</span>–53%')
        self.write(good); self.check()
        self.write(good+self.render().replace('51%–53%','-51%–53%'))
        with self.assertRaisesRegex(ValueError,'Visible'): self.check()

    def test_decimals_negative_zero_and_unsupported_formats(self):
        self.assertEqual(measure([-.00001],'percent',1),'0.0%')
        self.assertEqual(measure([12.25],'multiple',1),'12.2x')
        for args in (([True],),([1,2,3],),([1],'invented'),([1],'number',-1)):
            with self.assertRaises(ValueError): measure(*args)


if __name__=='__main__': unittest.main()
