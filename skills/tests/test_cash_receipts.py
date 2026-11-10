import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'company-model/scripts'))
import cash_receipts as receipts


class CashReceiptsTests(unittest.TestCase):
    def data(self):
        return json.loads((ROOT / 'company-model/assets/cash-receipts.example.json').read_text())

    def test_past_interim_is_not_a_future_receipt(self):
        result = receipts.summarize(self.data())
        self.assertAlmostEqual(result['cashPerUnit'], 1.05)
        self.assertAlmostEqual(result['cashYield'], .0525)
        self.assertEqual([r['id'] for r in result['excluded']], ['past-interim'])
        self.assertEqual(result['declaredCashPerUnit'], 0)
        self.assertTrue(result['conditional'])

    def test_ex_date_purchase_is_not_entitled_even_if_payment_is_in_window(self):
        data = self.data(); event = data['distributions'][1]
        event['exDate'] = data['purchaseDate']
        result = receipts.summarize(data)
        self.assertAlmostEqual(result['cashPerUnit'], .45)
        self.assertEqual(result['excluded'][1]['reason'], 'buyer-not-entitled')

    def test_payment_window_is_start_inclusive_end_exclusive(self):
        data = self.data(); data['purchaseDate'] = '2030-11-01'
        event = data['distributions'][1]; event['exDate'] = '2030-11-10'
        event['paymentDate'] = data['window']['start']
        data['distributions'][2]['paymentDate'] = data['window']['end']
        result = receipts.summarize(data)
        self.assertAlmostEqual(result['cashPerUnit'], .6)
        self.assertEqual(result['excluded'][-1]['reason'], 'payment-outside-window')

    def test_unknown_dates_do_not_silently_become_zero_or_complete_yield(self):
        data = self.data(); data['distributions'][1]['paymentDate'] = None
        result = receipts.summarize(data)
        self.assertEqual(result['status'], 'partial')
        self.assertIsNone(result['cashPerUnit']); self.assertIsNone(result['cashYield'])
        self.assertAlmostEqual(result['knownCashPerUnit'], .45)
        data['distributions'][1]['exDate'] = None
        self.assertEqual(receipts.summarize(data)['unresolved'][0]['reason'], 'missing-entitlement-date')

    def test_unusual_rights_require_explicit_sourced_entitlement(self):
        data = self.data(); event = data['distributions'][1]
        event.update(paymentDate='2030-12-01', exDate='2030-12-10')
        with self.assertRaisesRegex(ValueError, 'explicit entitlement'): receipts.summarize(data)
        event.update(entitlementRule='explicit', entitled=True, entitlementRationale='Invented due-bill rights, independently reviewed.')
        self.assertAlmostEqual(receipts.summarize(data)['cashPerUnit'], 1.05)
        event['entitled'] = False
        self.assertAlmostEqual(receipts.summarize(data)['cashPerUnit'], .45)
        event['entitlementRationale'] = ''
        with self.assertRaisesRegex(ValueError, 'rationale'): receipts.summarize(data)

    def test_currency_tax_basis_and_units_must_be_reconciled_before_addition(self):
        for field, value in [('currency', 'EUR'), ('amountBasis', 'net'), ('unit', 'per-unit')]:
            data = self.data(); data['distributions'][1][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'Convert'): receipts.summarize(data)

    def test_duplicate_ids_bad_amounts_and_missing_provenance_fail(self):
        for field, value in [('id', 'past-interim'), ('amountPerUnit', float('nan')), ('amountPerUnit', True),
                             ('amountPerUnit', -1), ('sourceIds', []), ('status', 'proposed'), ('entitlementRule', 'assume')]:
            data = self.data(); data['distributions'][1][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError): receipts.summarize(data)

    def test_dates_price_and_window_are_explicit(self):
        data = self.data(); data['distributions'][1]['exDate'] = '15/05/2031'
        with self.assertRaises(ValueError): receipts.summarize(data)
        data = self.data(); data['referencePrice'] = 0
        with self.assertRaises(ValueError): receipts.summarize(data)
        data = self.data(); data['window']['end'] = data['window']['start']
        with self.assertRaises(ValueError): receipts.summarize(data)
        data = self.data(); data['purchaseDate'] = '2030-12-01'
        with self.assertRaises(ValueError): receipts.summarize(data)

    def test_empty_inventory_is_only_a_declared_no_events_case(self):
        data = self.data(); data['distributions'] = []
        result = receipts.summarize(data)
        self.assertEqual(result['cashPerUnit'], 0)
        self.assertIn('complete event discovery', result['limit'])


if __name__ == '__main__': unittest.main()
