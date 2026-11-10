"""Invalid valuation denominators must fail, not silently become defaults."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'report-layout/scripts'))
import valuation_methods as vm
import test_release_check as fx


class ValuationInputTests(unittest.TestCase):
    def case(self,method,**over):
        values=dict(fx=2,targetMultiple=10,forwardEps=3,bookValuePerShare=8,dps=1,targetYield=.05,
                    enterpriseMetric=20,shares=10,netDebt=5,nonOperatingValue=2,minorityValue=1)
        values.update(over)
        return {'method':method,'bindings':{k:k for k in values}},values

    def test_valid_methods_and_omitted_same_currency_fx(self):
        for method,expected in (('P/E',15),('P/B',40),('dividend-yield',10),('EV/EBITDA',9.8),('EV/Sales',9.8)):
            with self.subTest(method=method):
                record,values=self.case(method)
                self.assertAlmostEqual(vm.target(record,values.__getitem__),expected)
                del record['bindings']['fx']
                self.assertAlmostEqual(vm.target(record,values.__getitem__),2*expected)

    def test_supplied_bad_fx_is_never_replaced_with_unity(self):
        for method in ('P/E','P/B','dividend-yield','EV/EBITDA','EV/Sales'):
            for bad in (0,-1,None,True,float('nan'),float('inf')):
                with self.subTest(method=method,bad=bad):
                    record,values=self.case(method,fx=bad)
                    with self.assertRaises(ValueError): vm.target(record,values.__getitem__)

    def test_zero_dividend_is_valid_but_invalid_yield_is_not(self):
        record,values=self.case('dividend-yield',dps=0)
        self.assertEqual(vm.target(record,values.__getitem__),0)
        for bad in (0,-.05,None,True,float('nan'),float('inf')):
            record,values=self.case('dividend-yield',targetYield=bad)
            with self.assertRaises(ValueError): vm.target(record,values.__getitem__)

    def test_nonpositive_multiple_or_denominator_does_not_create_valid_value(self):
        for method,metric in (('P/E','forwardEps'),('P/B','bookValuePerShare'),('EV/EBITDA','enterpriseMetric')):
            for changes in ({metric:0},{metric:-5,'targetMultiple':-10},{'targetMultiple':0}):
                with self.subTest(method=method,changes=changes):
                    record,values=self.case(method,**changes)
                    with self.assertRaises(ValueError): vm.target(record,values.__getitem__)

    def test_release_gate_rejects_invalid_inputs_even_if_fallback_arithmetic_would_match(self):
        f=fx.ReleaseCheckTests('test_clean_study_passes'); f.setUp(); self.addCleanup(f.doCleanups)
        # In these isolated fixtures caches are stipulated; the model integrity check
        # has its own tests. Verify the actual publication method gate independently.
        for method,cell,expected in (('P/E','D3','target-is-multiple-times-forward-eps'),
                                     ('dividend-yield','D14','target-is-dps-over-yield')):
            with self.subTest(method=method):
                s=fx.spec(); s['sheets']['Valuation']['cells'][cell]['value']=0
                f.write('model/spec.json',json.dumps(s))
                bindings=dict(fx.record()['bindings'],dps='Valuation!D13',targetYield='Valuation!D14')
                checks,_=fx.rc.run(f.dir,fx.record(method=method,bindings=bindings),model_check=fx.passing_check,legacy=True)
                result=next(c for c in checks if c['name']==expected)
                self.assertEqual(result['result'],'fail')
                self.assertIn('positive',result['detail'].lower())


if __name__=='__main__': unittest.main()
