import json
from pathlib import Path
import unittest


class MetricIdentityExampleTests(unittest.TestCase):
    def test_equal_irr_does_not_identify_annual_accounting_profit(self):
        source=Path(__file__).resolve().parents[1]/'company-model/assets/metric-identity.example.json'
        data=json.loads(source.read_text());rate=data['equityIrr'];depreciation=data['initialInvestment']/data['lifeYears']
        profits=[]
        for case in data['cases']:
            self.assertAlmostEqual(sum(v/(1+rate)**i for i,v in enumerate(case['cashFlows'])),0)
            profit=[v-depreciation for v in case['cashFlows'][1:]]
            self.assertEqual(profit,case['accountingProfit']);profits.append(profit)
        self.assertNotEqual(profits[0],profits[1])
        self.assertNotIn([10,10],profits)


if __name__=='__main__':unittest.main()
