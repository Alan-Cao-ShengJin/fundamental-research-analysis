"""Definition-aware comparisons and cumulative-to-incremental flow reconciliations.

Definitions are declared, not authenticated. Evidence extraction and omitted material comparisons stay reviewed.
"""
from datetime import date
import math
import operator

FIELDS = ('quantity', 'unit', 'currency', 'scale', 'perimeter', 'basis', 'measure')


def definition(item):
    d = item['definition']
    if any(not isinstance(d.get(k), str) or not d[k].strip() for k in FIELDS):
        raise ValueError('Definitions need quantity, unit, currency, scale, perimeter, basis and measure')
    if d['measure'] not in ('flow', 'ratio', 'per-share', 'stock'):
        raise ValueError('Unknown measurement type')
    if d['measure'] == 'stock':
        point = date.fromisoformat(d['asOf'])
        return d, point, point
    start, end = date.fromisoformat(d['start']), date.fromisoformat(d['end'])
    if start >= end:
        raise ValueError('Measurement periods use a start before an exclusive end')
    return d, start, end


def side(item, read):
    from claim_checks import arithmetic
    value = read(item['value'])
    original = definition(item)
    if 'reconcile' not in item:
        return value, original
    bridge = item['reconcile']
    if not str(bridge.get('rationale', '')).strip() or 'original' in bridge['inputs']:
        raise ValueError('Reconciliation needs a reason and reserves the original input')
    values = {'original': value, **{k: read(v) for k, v in bridge['inputs'].items()}}
    expected, result = arithmetic(bridge['expression'], values), read(bridge['result'])
    if not math.isclose(expected, result, rel_tol=1e-6, abs_tol=1e-8):
        raise ValueError('Comparison reconciliation does not reproduce')
    return result, definition(bridge)


def evaluate(assertion, read):
    if assertion.get('role') not in ('author', 'reviewer'):
        raise ValueError('Identify author or reviewer for a comparable-definition assertion')
    if assertion['kind'] == 'incremental-flow':
        current, (cd, cs, ce) = side(assertion['current'], read)
        prior, (pd, ps, pe) = side(assertion['prior'], read)
        increment = read(assertion['incremental']['value'])
        incd, ins, ine = definition(assertion['incremental'])
        if not all(d['measure'] == 'flow' for d in (cd, pd, incd)):
            raise ValueError('Only additive flows subtract this way; ratios, per-share values and balances need their own bridge')
        if any(cd[k] != d[k] for d in (pd, incd) for k in FIELDS):
            raise ValueError('Cumulative and incremental flows must have matching definitions; reconcile restatements/perimeters first')
        if not (cs == ps and cs < pe < ce and ins == pe and ine == ce):
            raise ValueError('Cumulative flows need a common start and the incremental period must be the remaining non-overlapping interval')
        if not math.isclose(current - prior, increment, rel_tol=1e-6, abs_tol=1e-8):
            raise ValueError('Incremental flow does not equal current cumulative less prior cumulative')
        return f'{assertion["role"]} incremental flow {increment} for [{ins}, {ine}) reconciles'
    left, (ld, ls, le) = side(assertion['left'], read)
    right, (rd, rs, re) = side(assertion['right'], read)
    relation = assertion.get('relation')
    allowed = ('same-period', 'matched-periods', 'cross-section', 'contextual')
    if relation not in allowed:
        raise ValueError('Comparison relation is same-period, matched-periods, cross-section or contextual')
    fields = [k for k in FIELDS if not (relation in ('cross-section', 'contextual') and k == 'perimeter')
              and not (relation == 'contextual' and k == 'basis')]
    if any(ld[k] != rd[k] for k in fields):
        raise ValueError('Comparison definitions differ; bind a reconciliation before asserting the comparison')
    if relation == 'contextual':
        if (assertion.get('interpretation') != 'descriptive-only' or not str(assertion.get('limitations', '')).strip()
                or not str(assertion.get('alignment', '')).strip()):
            raise ValueError('Contextual comparisons need explicit descriptive-only interpretation, alignment and limitations; not a guide-compliance test')
    elif relation == 'same-period':
        if (ls, le) != (rs, re):
            raise ValueError('Comparison periods differ; a remaining period is not a full-year guide')
    elif (not str(assertion.get('alignment', '')).strip()
          or abs((le - ls).days - (re - rs).days) > 7):
        raise ValueError('Matched periods/peers need an alignment rationale and comparable duration; reconcile other differences')
    ops = {'>': operator.gt, '>=': operator.ge, '<': operator.lt, '<=': operator.le, '==': operator.eq}
    if assertion.get('op') not in ops or not ops[assertion['op']](left, right):
        raise ValueError(f'Comparison assertion is false: {left} {assertion.get("op")} {right}')
    return f'{assertion["role"]} comparison {left} {assertion["op"]} {right} reconciles on {relation} definitions'


def coverage(packet, key, kinds):
    entry = packet.get('coverage', {}).get(key, {})
    actual = [a['id'] for a in packet.get('claimAssertions', []) if a.get('kind') in kinds]
    ids = entry.get('assertionIds', [])
    if entry.get('status') == 'not-applicable':
        valid = not actual and not ids and bool(str(entry.get('reason', '')).strip())
    else:
        valid = (entry.get('status') == 'checked' and bool(actual) and len(ids) == len(set(ids))
                 and set(ids) == set(actual))
    if key == 'incremental-flows' and packet.get('researchMode') == 'earnings-update':
        candidates = entry.get('candidates', [])
        sources = {s['id'] for s in packet['handoff']['sources']}
        if not candidates or len({c.get('id') for c in candidates}) != len(candidates):
            return False
        accounted = []
        for c in candidates:
            if (not c.get('id') or type(c.get('material')) is not bool or not c.get('sourceIds')
                    or not set(c['sourceIds']) <= sources or not str(c.get('reason', '')).strip()):
                return False
            if c.get('status') == 'checked':
                if c.get('assertionId') not in actual:
                    return False
                accounted.append(c['assertionId'])
            elif c.get('status') not in ('unavailable', 'not-comparable', 'immaterial') or (c['status'] == 'immaterial' and c['material']):
                return False
        valid = valid and set(accounted) == set(actual)
    return valid


def brief_fidelity(packet):
    entry = packet.get('coverage', {}).get('brief-fidelity', {})
    items = entry.get('items', [])
    claims = {c['id'] for c in packet['handoff']['claims']}
    return (entry.get('status') == 'checked' and bool(items)
            and len({i.get('claimId') for i in items}) == len(items)
            and all(i.get('claimId') in claims and all(isinstance(i.get(k), str) and i[k].strip()
                for k in ('reportLocation', 'briefLocation', 'qualification', 'assessment')) for i in items))
