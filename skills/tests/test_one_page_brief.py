"""Behavior checks for protected decision math and brief content handling."""
from pathlib import Path
import importlib.util,unittest

SCRIPT=Path(__file__).resolve().parents[1]/'research-brief/scripts/render_one_page.py'
spec=importlib.util.spec_from_file_location('brief_renderer',SCRIPT);r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
def fixture():
    return {'schemaVersion':'2.0.0','headline':'A synthetic investment assessment','meta':{'issuer':'Example Company <synthetic>','security':'EXAMPLE ordinary','currency':'USD','asOf':'Example date'},
    'decision':{'rating':'Buy','referencePrice':100,'priceObservation':'Example close','targetPrice':120,'targetDate':'Example horizon','dividendYield':.04,'bearTarget':70,'bullTarget':160},
    'sections':[{'id':i,'title':t,'paragraphs':['Synthetic assessment with a stated assumption.'],'sourceIds':['example']} for i,t in [('thesis','Investment case'),('valuation','Valuation'),('risk','What could change')]],
    'financials':{'sectionId':'valuation','caption':'Synthetic units','columns':['Metric','Actual','Forecast'],'rows':[['Value','10','12']]},
    'sources':[{'id':'example','label':'Synthetic source','href':'evidence.html'}],'links':[]}
class BriefTests(unittest.TestCase):
    def test_buy_brief_shows_price_return_and_dividend_yield(self):
        document,result=r.render(fixture())
        self.assertEqual(result['rating'],'Buy')
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
    def test_dividend_yield_does_not_change_rating_or_price_return(self):
        p=fixture();p['decision'].update(targetPrice=105,rating='Hold',dividendYield=.40)
        document,result=r.render(p)
        self.assertEqual(result['rating'],'Hold');self.assertAlmostEqual(result['priceReturn'],.05);self.assertIn('Hold | Price return +5.0%',document)
    def test_retired_decision_keys_from_older_payloads_are_ignored(self):
        p=fixture();p['decision'].update(attractiveness='decent',attractivenessReason='Older study text.',newMoney='yes')
        document,result=r.render(p)
        self.assertEqual(result,r.render(fixture())[1]);self.assertEqual(document,r.render(fixture())[0])

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
