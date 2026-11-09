"""Dated NTM bridges. Dates are ISO and intervals are [start, end), including irregular fiscal periods.

Uniform daily allocation is an explicit approximation, not a forecast of intra-period seasonality.
Input dates, accounting definitions and representativeness still require source review.
"""
from datetime import date
import math
import re


def interval(item):
    start, end = date.fromisoformat(item['start']), date.fromisoformat(item['end'])
    if start >= end:
        raise ValueError('Period start must precede its exclusive end')
    return start, end


def finite(value):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError('Dated NTM bindings must be finite numbers')
    return value


def label(value):
    return re.sub(r'[^A-Z0-9]', '', str(value).upper())


def calculate(declaration, read):
    """read(ref) returns a calculated workbook value. Returns EPS and auditable overlap details."""
    start, end = interval(declaration)
    if declaration.get('allocation') != 'uniform-days' or not str(declaration.get('rationale', '')).strip():
        raise ValueError('Declare uniform-days allocation and justify the forecast profile; it remains an approximation')
    basis = declaration.get('metric')
    if basis not in ('eps-sum', 'profit-over-shares'):
        raise ValueError('Dated NTM metric is eps-sum or profit-over-shares')
    components = declaration['components']
    if (not components or any(not isinstance(c['period'], str) or not c['period'].strip() for c in components)
            or len({c['period'] for c in components}) != len(components)):
        raise ValueError('Dated components need distinct period labels')
    spans, details, used = [], [], set()
    profit, eps, weighted_shares = 0.0, 0.0, 0.0
    counts = []
    for c in components:
        cs, ce = interval(c)
        lo, hi = max(start, cs), min(end, ce)
        if lo >= hi:
            raise ValueError('Every dated component must intersect the NTM window')
        fraction = (hi - lo).days / (ce - cs).days
        if 'weight' in c and (not math.isclose(finite(c['weight']), fraction, abs_tol=1e-8)):
            raise ValueError('Component weight differs from its dated overlap')
        ref = c['eps'] if basis == 'eps-sum' else c['profit']
        canonical = ref.replace('$', '').replace("'", '')
        if canonical in used:
            raise ValueError('One earnings cell cannot serve two dated periods')
        used.add(canonical)
        header = c['header']
        if (label(read(header)) != label(c['period']) or header.split('!')[0] != ref.split('!')[0]
                or re.sub(r'\d', '', header.split('!')[1]) != re.sub(r'\d', '', ref.split('!')[1])):
            raise ValueError('Each dated earnings cell needs its own matching period header in the same column')
        shares = finite(read(c['shares']))
        if shares <= 0:
            raise ValueError('Period weighted-average shares must be positive')
        counts.append(shares)
        amount = finite(read(ref))
        if basis == 'eps-sum':
            eps += amount * fraction
        else:
            profit += amount * fraction
            weighted_shares += shares * (hi - lo).days / (end - start).days
        spans.append((lo, hi))
        details.append({'period': c['period'], 'overlapStart': lo.isoformat(), 'overlapEnd': hi.isoformat(),
                        'fractionOfComponent': fraction, 'amount': amount, 'shares': shares})
    cursor = start
    for lo, hi in sorted(spans):
        if lo != cursor:
            raise ValueError('Dated NTM components have a gap or overlap')
        cursor = hi
    if cursor != end:
        raise ValueError('Dated NTM components do not cover the whole window')
    if basis == 'eps-sum' and any(not math.isclose(n, counts[0], rel_tol=1e-9) for n in counts):
        raise ValueError('EPS addition requires constant comparable shares; use profit-over-shares when shares change')
    return {'eps': eps if basis == 'eps-sum' else profit / weighted_shares,
            'profit': profit if basis == 'profit-over-shares' else None,
            'weightedShares': weighted_shares if basis == 'profit-over-shares' else counts[0],
            'components': details}
