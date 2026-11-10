"""Dated distributions available to a buyer; no network, investment call or date inference.

Window dates are [start, end). Amounts and price use one currency and unit.
Future dates/amounts remain declared or forecast inputs, never guaranteed receipts.
"""
from datetime import date
import json
import math
from pathlib import Path
import sys


def iso(value):
    if not isinstance(value, str) or len(value) != 10:
        raise ValueError('Use an explicit ISO YYYY-MM-DD date')
    parsed = date.fromisoformat(value)
    if parsed.isoformat() != value:
        raise ValueError('Use an explicit ISO YYYY-MM-DD date')
    return parsed


def number(value, positive=False):
    if type(value) not in (int, float) or not math.isfinite(value) or value < 0 or positive and value == 0:
        raise ValueError('Use a finite nonnegative amount and a positive price')
    return value


def summarize(data):
    start, end = iso(data['window']['start']), iso(data['window']['end'])
    purchase = iso(data['purchaseDate'])
    if not purchase <= start < end:
        raise ValueError('Purchase must be on/before the start of a nonempty receipt window')
    currency, unit, basis = data['currency'], data['unit'], data['amountBasis']
    if not isinstance(currency, str) or not currency.strip() or unit not in ('per-share', 'per-unit') or basis not in ('gross', 'net'):
        raise ValueError('Declare currency, per-share/per-unit and gross/net basis')
    rows, ids = data['distributions'], set()
    if not isinstance(rows, list):
        raise ValueError('Distributions must be a list; an empty list declares no known events')
    included, excluded, unresolved = [], [], []
    declared, forecast = [], []
    for row in rows:
        identity = row['id']
        if not isinstance(identity, str) or not identity.strip() or identity in ids:
            raise ValueError('Distribution IDs must be nonempty and unique')
        ids.add(identity)
        amount = number(row['amountPerUnit'])
        if row.get('currency', currency) != currency or row.get('amountBasis', basis) != basis or row.get('unit', unit) != unit:
            raise ValueError('Convert currencies, units and tax bases explicitly before combining receipts')
        sources = row.get('sourceIds')
        if not isinstance(sources, list) or not sources or any(not isinstance(x, str) or not x.strip() for x in sources):
            raise ValueError('Each distribution needs source/forecast references')
        status = row['status']
        if status not in ('declared', 'forecast'):
            raise ValueError('Use declared or forecast; do not silently treat a proposal as declared')
        ex = iso(row['exDate']) if row.get('exDate') is not None else None
        payment = iso(row['paymentDate']) if row.get('paymentDate') is not None else None
        rule = row.get('entitlementRule', 'ex-date')
        if rule == 'explicit':
            if type(row.get('entitled')) is not bool or not str(row.get('entitlementRationale', '')).strip():
                raise ValueError('Explicit entitlement needs a boolean and sourced rights rationale')
            entitled = row['entitled']
        elif rule == 'ex-date':
            if payment and ex and payment < ex:
                raise ValueError('An unusual payment-before-ex schedule needs explicit entitlement treatment')
            entitled = purchase < ex if ex else None
        else:
            raise ValueError('Unknown entitlement rule')
        event = dict(row, currency=currency, unit=unit, amountBasis=basis)
        if entitled is False:
            excluded.append(dict(event, reason='buyer-not-entitled'))
        elif payment is not None and not start <= payment < end:
            excluded.append(dict(event, reason='payment-outside-window'))
        elif entitled is None or payment is None:
            unresolved.append(dict(event, reason='missing-entitlement-date' if entitled is None else 'missing-payment-date'))
        else:
            included.append(event)
            (declared if status == 'declared' else forecast).append(amount)
    cash = math.fsum(declared + forecast)
    result = {'status': 'partial' if unresolved else 'complete', 'currency': currency, 'unit': unit, 'amountBasis': basis,
              'purchaseDate': data['purchaseDate'], 'window': data['window'],
              'knownCashPerUnit': cash, 'declaredCashPerUnit': math.fsum(declared), 'forecastCashPerUnit': math.fsum(forecast),
              'cashPerUnit': None if unresolved else cash, 'conditional': bool(forecast or unresolved),
              'included': included, 'excluded': excluded, 'unresolved': unresolved,
              'limit': 'Computes declared inputs, not source truth, complete event discovery, guaranteed payment, FX or tax advice.'}
    if 'referencePrice' in data:
        price = number(data['referencePrice'], positive=True)
        result.update(knownCashYield=cash / price, cashYield=None if unresolved else cash / price)
    return result


if __name__ == '__main__':
    print(json.dumps(summarize(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))), indent=2))
