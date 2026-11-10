import copy
import importlib.util
from pathlib import Path
import unittest

path=Path(__file__).resolve().parents[1]/'valuation-thesis/scripts/yield_spread.py'
spec=importlib.util.spec_from_file_location('yield_spread',path); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)

class YieldSpreadTests(unittest.TestCase):
    def data(self):
        return {'benchmark':{'currency':'USD','tenor':'10 years','rationale':'Synthetic matched-currency comparison.'},'dividendCurrency':'USD',
                'yieldBasis':'trailing-announced ordinary','sourceIds':['synthetic-observations'],
                'observations':[{'date':f'2030-0{i+1}-28','bondDate':f'2030-0{i+1}-27','dividendYield':dy,'governmentYield':rate}
                                for i,(dy,rate) in enumerate(((.06,.02),(.07,.03),(.08,.04)))]}
    def test_rate_change_is_separated_from_absolute_yield_and_no_target_is_invented(self):
        value=module.summarize(self.data()); self.assertAlmostEqual(value['meanSpread'],.04)
        self.assertAlmostEqual(value['meanAbsoluteYield'],.07); self.assertNotIn('conditionalPrice',value)
        data=self.data(); data.update(targetSpread=.03,sustainableDps=7)
        self.assertAlmostEqual(module.summarize(data)['conditionalPrice'],100)
    def test_future_benchmark_and_unexplained_currency_mismatch_are_rejected(self):
        data=self.data(); data['observations'][0]['bondDate']='2031-01-01'
        with self.assertRaisesRegex(ValueError,'future'): module.summarize(data)
        data=self.data(); data['benchmark']['currency']='EUR'
        with self.assertRaisesRegex(ValueError,'cross-currency'): module.summarize(data)
        data['crossCurrencyRationale']='Explicit synthetic FX comparison, not a matched-currency risk-free spread.'
        self.assertEqual(module.summarize(data)['observations'],3)

if __name__=='__main__': unittest.main()
