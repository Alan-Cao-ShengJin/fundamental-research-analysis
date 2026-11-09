"""Accounting-coherence tests for a held-out bank source pack, not a prescribed investment call."""
import json
from pathlib import Path
import unittest


class CedarFixtureTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((Path(__file__).resolve().parents[1] / 'evals/fixtures/cedar-bank/facts.json').read_text())

    def test_all_income_and_balance_sheets_reconcile(self):
        for r in self.data['reported']:
            self.assertAlmostEqual(r['interestIncome']-r['interestExpense'], r['netInterestIncome'])
            self.assertAlmostEqual(r['netInterestIncome']+r['fees']-r['operatingCosts']-r['impairment'], r['preTax'])
            self.assertAlmostEqual(r['preTax']-r['tax'], r['attributableProfit'])
            self.assertAlmostEqual(r['attributableProfit']/r['weightedShares'], r['eps'])
        for b in self.data['balanceSheets'].values():
            self.assertAlmostEqual(b['assets'], b['deposits']+b['wholesaleFunding']+b['otherLiabilities']+b['equity'])
            self.assertAlmostEqual(b['netLoans'], b['grossLoans']-b['allowance'])
            self.assertAlmostEqual(b['cet1'], b['tangibleEquity']-b['otherPrudentialDeductions'])

    def test_cash_and_equity_movement_bridges_reconcile(self):
        for r in self.data['cashFlows'].values():
            self.assertAlmostEqual(r['opening']+r['operating']+r['investing']+r['dividends']+r['repurchases'], r['closing'])
        for r in self.data['equityBridges'].values():
            self.assertAlmostEqual(r['opening']+r['profit']-r['dividends']-r['repurchases']+r['oci'], r['closing'])

    def test_incremental_flows_and_changed_share_eps_are_distinct(self):
        periods = {r['period']: r for r in self.data['reported']}
        h, n = periods['1H2026'], periods['9M2026']
        profit = n['attributableProfit']-h['attributableProfit']
        self.assertAlmostEqual(profit, 13.2)
        self.assertNotAlmostEqual(n['eps']-h['eps'], profit/190)
        self.assertAlmostEqual(self.data['cashFlows']['9M2026']['operating']-self.data['cashFlows']['1H2026']['operating'], -25)


if __name__ == '__main__':
    unittest.main()
