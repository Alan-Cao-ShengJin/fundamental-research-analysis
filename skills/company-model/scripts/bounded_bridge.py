"""Feasibility of one affine earnings/value bridge over independent closed ranges.

No optimizer dependency. A witness disproves necessity within the declared box;
it does not identify anybody's actual assumptions. Nonlinear or coupled drivers
require a different domain/model test, not this helper.
"""
import argparse
import json
import math
from pathlib import Path


def finite(value):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError('Use finite numeric inputs, not booleans')
    return value


def solve(offset, target, drivers):
    """Drivers: unique id, coefficient, low, high. Units are caller-defined."""
    finite(offset); finite(target)
    if not drivers or len(drivers) > 200:
        raise ValueError('Provide one to 200 independent bounded drivers')
    ids = [d['id'] for d in drivers]
    if any(not isinstance(i, str) or not i.strip() for i in ids) or len(set(ids)) != len(ids):
        raise ValueError('Driver IDs must be nonempty and unique')
    lower, upper = {}, {}
    for d in drivers:
        c, lo, hi = [finite(d[k]) for k in ('coefficient', 'low', 'high')]
        if lo > hi:
            raise ValueError('A driver low cannot exceed its high')
        lower[d['id']], upper[d['id']] = (lo, hi) if c >= 0 else (hi, lo)
    def evaluate(point):
        return finite(offset + sum(d['coefficient'] * point[d['id']] for d in drivers))
    low, high = evaluate(lower), evaluate(upper)
    tolerance = 1e-10 * max(1, abs(low), abs(high), abs(target))
    feasible = low-tolerance <= target <= high+tolerance
    witness = None
    if feasible:
        weight = 0 if high == low else max(0, min(1, (target-low)/(high-low)))
        witness = {i:lower[i]+weight*(upper[i]-lower[i]) for i in ids}
    return {'feasible':feasible, 'minimum':low, 'maximum':high, 'witness':witness,
            'reproduced':evaluate(witness) if witness is not None else None,
            'limits':'One affine equality over independent ranges; domain completeness, economic feasibility and source definitions remain reviewed.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding='utf-8-sig'))
    print(json.dumps(solve(payload['offset'],payload['target'],payload['drivers']),indent=2))


if __name__ == '__main__':
    main()
