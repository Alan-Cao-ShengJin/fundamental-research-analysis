"""Independent feasibility witnesses and rejection of overclaimed component necessity."""
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'company-model/scripts'))
from bounded_bridge import solve


class BoundedBridgeTests(unittest.TestCase):
    def test_target_has_multiple_component_routes_and_interior_witness(self):
        drivers=[{'id':'sales','coefficient':.3,'low':100,'high':120},
                 {'id':'cost','coefficient':-1,'low':10,'high':15}]
        result=solve(2,24,drivers)
        self.assertTrue(result['feasible'])
        self.assertAlmostEqual(2+.3*result['witness']['sales']-result['witness']['cost'],24)
        self.assertEqual((result['minimum'],result['maximum']),(17,28))
        # Constraining sales below its maximum still permits the same profit.
        drivers[0]['high']=110
        self.assertTrue(solve(2,24,drivers)['feasible'])

    def test_outside_range_is_infeasible_without_inventing_a_witness(self):
        result=solve(0,20,[{'id':'x','coefficient':2,'low':1,'high':5}])
        self.assertFalse(result['feasible']); self.assertIsNone(result['witness'])

    def test_zero_negative_coefficients_and_fixed_ranges(self):
        drivers=[{'id':'x','coefficient':-2,'low':3,'high':3}, {'id':'y','coefficient':0,'low':1,'high':10}]
        self.assertTrue(solve(10,4,drivers)['feasible'])
        self.assertFalse(solve(10,5,drivers)['feasible'])

    def test_malformed_and_nonfinite_inputs_rejected(self):
        good={'id':'x','coefficient':1,'low':0,'high':2}
        for drivers in ([],[good,good],[dict(good,low=3)],[dict(good,high=math.inf)],[dict(good,coefficient=True)]):
            with self.assertRaises(ValueError): solve(0,1,drivers)


if __name__=='__main__': unittest.main()
