import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1] / 'valuation-thesis/scripts/implied_premium.py'
spec = importlib.util.spec_from_file_location('implied_premium', path); module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)


class ImpliedPremiumTests(unittest.TestCase):
    def data(self, **changes):
        base = {'index': 'Synthetic index', 'asOf': '2030-01-15', 'level': 100, 'cashToHolders': 4, 'growth': 0.04,
                'riskFree': 0.04, 'sourceIds': ['synthetic-index']}
        base.update(changes)
        return base

    def test_constant_growth_matches_the_closed_form(self):
        # With growth equal to the risk-free rate throughout, level = C(1+rf)/(r-rf), so r = rf + C(1+rf)/level.
        result = module.solve(self.data())
        self.assertAlmostEqual(result['impliedReturn'], 0.04 + 4 * 1.04 / 100, places=9)
        self.assertAlmostEqual(result['impliedPremium'], 0.0416, places=9)
        self.assertAlmostEqual(module.value(result['impliedReturn'], 4, 0.04, 0.04, 5), 100, places=6)

    def test_premium_moves_with_price_growth_and_rates(self):
        base = module.solve(self.data())['impliedPremium']
        self.assertGreater(module.solve(self.data(growth=0.08))['impliedPremium'], base)
        self.assertLess(module.solve(self.data(level=125))['impliedPremium'], base)
        self.assertGreater(module.solve(self.data(level=80))['impliedPremium'], base)

    def test_percent_units_and_missing_declarations_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'fractional'): module.solve(self.data(growth=8))
        with self.assertRaisesRegex(ValueError, 'positive'): module.solve(self.data(cashToHolders=0))
        with self.assertRaisesRegex(ValueError, 'finite'): module.solve(self.data(riskFree=float('nan')))
        data = self.data(); del data['sourceIds']
        with self.assertRaisesRegex(ValueError, 'source'): module.solve(data)


if __name__ == '__main__':
    unittest.main()
