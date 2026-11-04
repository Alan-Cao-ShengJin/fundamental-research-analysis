"""Behavior checks for protected decision math and brief content handling."""
from pathlib import Path
import importlib.util,unittest

SCRIPT=Path(__file__).resolve().parents[1]/'research-brief/scripts/render_one_page.py'
spec=importlib.util.spec_from_file_location('brief_renderer',SCRIPT);r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
def fixture():
    return {'schemaVersion':'2.0.0','headline':'A synthetic investment assessment','meta':{'issuer':'Example Company <synthetic>','security':'EXAMPLE ordinary','currency':'USD','asOf':'Example date'},
    'decision':{'rating':'Buy','referencePrice':100,'priceObservation':'Example close','targetPrice':120,'targetDate':'Example horizon','attractiveness':'unattractive','attractivenessReason':'Upside is below 30%, so risk/reward looks less attractive for new money.','dividendYield':.04,'bearTarget':70,'bullTarget':160},
    'sections':[{'id':i,'title':t,'paragraphs':['Synthetic assessment with a stated assumption.'],'sourceIds':['example']} for i,t in [('thesis','Investment case'),('valuation','Valuation'),('risk','What could change')]],
    'financials':{'sectionId':'valuation','caption':'Synthetic units','columns':['Metric','Actual','Forecast'],'rows':[['Value','10','12']]},
    'sources':[{'id':'example','label':'Synthetic source','href':'evidence.html'}],'links':[]}
class BriefTests(unittest.TestCase):
    def test_buy_and_attractiveness_remain_distinct(self):
        document,result=r.render(fixture())
        self.assertEqual(result['rating'],'Buy');self.assertEqual(result['attractiveness'],'unattractive')
        self.assertAlmostEqual(result['priceReturn'],.20);self.assertIn('Buy | Price return +20.0%',document)
        self.assertIn('4.0% dividend yield.',document);self.assertIn('12-month target',document);self.assertNotIn('Example horizon',document)
        self.assertIn('&lt;synthetic&gt;',document);self.assertNotIn('case-basis">',document)
        p=fixture();p['decision'].update(bearBasis='7x EPS of $10',targetBasis='12x EPS of $10',bullBasis='16x EPS of $10');document,_=r.render(p)
        self.assertIn('<span class="case-basis">12x EPS of $10</span>',document)
        p['decision']['keyMetrics']=['10.0x forward P/E','2.0x P/B','4.0% dividend yield','15% ROIC'];document,_=r.render(p);self.assertIn('12-month target; 10.0x forward P/E; 2.0x P/B; 4.0% dividend yield; 15% ROIC.',document)
        p['decision']['keyMetrics']=['2.0x P/B']
        with self.assertRaisesRegex(ValueError,'dividend yield'):r.render(p)
    def test_exact_rating_boundaries_do_not_drift_with_floating_point(self):
        for target in [90,110]:
            p=fixture();p['decision'].update(targetPrice=target,rating='Hold');self.assertEqual(r.validate(p)['rating'],'Hold')
        p=fixture();p['decision'].update(targetPrice=110.01,rating='Hold')
        with self.assertRaisesRegex(ValueError,'Rating'):r.validate(p)
    def test_bull_case_cannot_qualify_base_attractiveness(self):
        p=fixture();p['decision']['attractiveness']='attractive'
        with self.assertRaisesRegex(ValueError,'50%'):r.render(p)
    def test_decent_tier_boundaries_and_entry_prices(self):
        p=fixture();p['decision'].update(targetPrice=130,attractiveness='decent',attractivenessReason='Upside of 30% makes this a decent entry for new money.')
        document,result=r.render(p)
        self.assertEqual(result['newMoney'],'yes');self.assertAlmostEqual(result['priceReturn'],.30);self.assertNotIn('new money',document)
        p['decision']['targetPrice']=129.99
        with self.assertRaisesRegex(ValueError,'30%'):r.render(p)
        p['decision'].update(targetPrice=150)
        with self.assertRaisesRegex(ValueError,'below 50%'):r.render(p)
        p=fixture();document,result=r.render(p)
        self.assertEqual(result['newMoney'],'no');self.assertAlmostEqual(result['entryAttractive'],120/1.5);self.assertNotIn('entry',document.lower())
        p['decision']['newMoney']='yes'
        with self.assertRaisesRegex(ValueError,'below the decent tier'):r.render(p)
    def test_dividend_yield_cannot_lift_the_tier(self):
        p=fixture();p['decision'].update(dividendYield=.40,attractiveness='attractive',attractivenessReason='the return hurdle is met.')
        with self.assertRaisesRegex(ValueError,'50%'):r.render(p)
        p['decision'].update(targetPrice=150)
        document,result=r.render(p)
        self.assertEqual(result['rating'],'Buy');self.assertIn('Buy | Price return +50.0%',document)

    def test_unknown_dividend_is_not_zero_and_old_fields_require_migration(self):
        p=fixture();p['decision']['dividendYield']=None
        document,result=r.render(p)
        self.assertIsNone(result['dividendYield']);self.assertNotIn('Dividend yield',document)
        for old in ('dividendPerShare','dividendsToTargetDate'):
            p=fixture();p['decision'][old]=2
            with self.assertRaisesRegex(ValueError,'dividendYield'):r.render(p)

    def test_empty_selected_content_and_untraceable_citations_are_rejected(self):
        p=fixture();p['sections'][0]['paragraphs']=[]
        with self.assertRaisesRegex(ValueError,'substantive'):r.render(p)
        p=fixture();p['sections'][0]['sourceIds']=['missing']
        with self.assertRaisesRegex(ValueError,'source'):r.render(p)
    def test_brief_without_sources_has_no_footnotes(self):
        p=fixture();p['sources']=[]
        for s in p['sections']:s['sourceIds']=[]
        document,_=r.render(p);self.assertNotIn('Sources:',document);self.assertNotIn('<sup>',document)
    def test_untrusted_text_is_escaped_and_unsafe_links_fail(self):
        p=fixture();p['sections'][0]['paragraphs']=['A <script> claim stays visible text.']
        document,_=r.render(p);self.assertIn('&lt;script&gt;',document);self.assertNotIn('<script>',document)
        p['sources'][0]['href']='javascript:alert(1)'
        with self.assertRaisesRegex(ValueError,'URLs'):r.render(p)
    def test_selective_headings_and_optional_financial_table(self):
        p=fixture();p.pop('financials');p['sections']=p['sections'][:2]
        p['sections'][0]['title']='A company-specific economic question'
        document,result=r.render(p)
        self.assertEqual(result['sectionCount'],2)
        self.assertIn('A company-specific economic question',document)
        self.assertNotIn('<table>',document)
        p['financials']={'sectionId':'absent','caption':'Synthetic units','columns':['Metric','Value'],'rows':[['Value','1']]}
        with self.assertRaisesRegex(ValueError,'sectionId'):r.render(p)

if __name__=='__main__':unittest.main()
