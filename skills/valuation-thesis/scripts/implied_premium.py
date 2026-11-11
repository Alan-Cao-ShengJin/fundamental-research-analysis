"""Solve the equity return and premium that an index price implies.

Input JSON: index, asOf, level, cashToHolders (dividends plus net buybacks over the past twelve months,
in index points), growth (consensus earnings growth for the next `years`, default 5), riskFree
(10-year government yield; also the long-run growth rate), sourceIds. Rates are fractions: 0.07 for 7%.

    level = sum_{t=1..years} C(1+g)^t/(1+r)^t + [C(1+g)^years (1+rf)/(r-rf)]/(1+r)^years

Output: impliedReturn r and impliedPremium r - rf. The helper does the arithmetic; choosing the index
and retrieving dated inputs belong to the analyst workflow.
"""
import json
import math
from pathlib import Path
import sys


def value(r, cash, growth, risk_free, years):
    flows = [cash * (1 + growth) ** t for t in range(1, years + 1)]
    terminal = flows[-1] * (1 + risk_free) / (r - risk_free)
    return sum(f / (1 + r) ** t for t, f in enumerate(flows, 1)) + terminal / (1 + r) ** years


def solve(data):
    years = data.get('years', 5)
    level, cash, growth, risk_free = (data.get(k) for k in ('level', 'cashToHolders', 'growth', 'riskFree'))
    if any(type(v) not in (int, float) or not math.isfinite(v) for v in (level, cash, growth, risk_free)):
        raise ValueError('level, cashToHolders, growth and riskFree must be finite numbers')
    if type(years) is not int or not 1 <= years <= 10:
        raise ValueError('years must be a whole number from 1 to 10')
    if level <= 0 or cash <= 0:
        raise ValueError('level and cashToHolders must be positive')
    if abs(growth) > 1 or abs(risk_free) > 1:
        raise ValueError('Use fractional rates (0.07 for 7%)')
    if not data.get('index') or not data.get('asOf') or not data.get('sourceIds'):
        raise ValueError('Declare the index, the asOf date and source references')
    low, high = risk_free + 1e-9, risk_free + 1.0
    if value(high, cash, growth, risk_free, years) > level:
        raise ValueError('No implied return below riskFree + 100 points; check the units of level and cashToHolders')
    for _ in range(200):   # value falls as r rises
        mid = (low + high) / 2
        low, high = (mid, high) if value(mid, cash, growth, risk_free, years) > level else (low, mid)
    r = (low + high) / 2
    return {'index': data['index'], 'asOf': data['asOf'], 'impliedReturn': r, 'impliedPremium': r - risk_free,
            'cashYield': cash / level, 'growth': growth, 'riskFree': risk_free, 'years': years, 'sourceIds': data['sourceIds'],
            'limit': 'Implied by the stated price, cash flows and growth; it moves with each and is not a forecast of returns.'}


if __name__ == '__main__':
    print(json.dumps(solve(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8-sig'))), indent=2))
