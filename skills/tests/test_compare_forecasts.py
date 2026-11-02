import importlib.util,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('compare_forecasts',Path(__file__).parents[1]/'company-model/scripts/compare_forecasts.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def snap(values,basis='reported'):
    return {'label':'Synthetic','as_of':'2000-01-01','metrics':[{'id':k,'period':'Y1','unit':'currency million','basis':basis,'scope':'group','value':v,'source':'Invented test fixture'} for k,v in values.items()]}
class CompareTests(unittest.TestCase):
    def test_basis_mismatch_is_excluded(self):
        row=m.compare_snapshots(snap({'profit':10}),snap({'profit':12},'adjusted'))['rows'][0]
        self.assertEqual(row['status'],'definition mismatch');self.assertNotIn('difference',row)
    def test_zero_denominator_is_not_zero_gap(self):
        row=m.compare_snapshots(snap({'profit':10}),snap({'profit':0}))['rows'][0]
        self.assertEqual(row['difference'],10);self.assertIsNone(row['relative_difference'])
    def test_missing_metric_not_zero(self):
        row=m.compare_snapshots(snap({'profit':10}),snap({}))['rows'][0]
        self.assertEqual(row['status'],'missing counterpart')
    def test_bridge_can_expose_an_omission(self):
        r=m.additive_bridge(snap({'profit':20,'gp':30,'cost':10}),snap({'profit':13,'gp':25,'cost':12}),'profit',[{'id':'gp','sign':1},{'id':'cost','sign':-1}],'Y1')
        self.assertTrue(r['reconciled'])
        r=m.additive_bridge(snap({'profit':20,'gp':30,'cost':10}),snap({'profit':13,'gp':25,'cost':12}),'profit',[{'id':'gp','sign':1}],'Y1')
        self.assertFalse(r['reconciled']);self.assertEqual(r['unexplained_residual'],2)
    def test_gp_interaction_shared_and_reversible(self):
        a=m.gross_profit_bridge(120,.25,100,.20);b=m.gross_profit_bridge(100,.20,120,.25)
        self.assertAlmostEqual(a['revenue_effect']+a['margin_effect'],10)
        for k in ['revenue_effect','margin_effect','total_gp_gap']:self.assertAlmostEqual(a[k],-b[k])
    def test_duplicate_rejected(self):
        s=snap({'profit':1});s['metrics']*=2
        with self.assertRaises(ValueError):m.index(s)
    def test_missing_number_rejected(self):
        with self.assertRaises(ValueError):m.index(snap({'profit':None}))
if __name__=='__main__':unittest.main()
