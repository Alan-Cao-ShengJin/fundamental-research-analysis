"""Bounded claim checks for publication and reviewer findings.

Checks declared sets, scopes, cash boundaries and arithmetic. It cannot discover omitted material claims,
authenticate source extraction, or decide whether a source population is representative.
"""
import ast
import copy
import json
import math
import operator
from pathlib import Path


def number(value):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError('A finite numeric value is required')
    return value


def arithmetic(expression, values):
    """No eval, code execution, calls, attributes or subscripts."""
    if len(expression) > 2000:
        raise ValueError('Calculation expression is too long')
    binary = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}
    def walk(node):
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Name) and node.id in values:
            return number(values[node.id])
        if isinstance(node, ast.Constant):
            return number(node.value)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            return (-1 if isinstance(node.op, ast.USub) else 1) * walk(node.operand)
        if isinstance(node, ast.BinOp) and type(node.op) in binary:
            return number(binary[type(node.op)](walk(node.left), walk(node.right)))
        raise ValueError('Only named inputs, numeric constants and + - * / are supported')
    tree = ast.parse(expression, mode='eval')
    used = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    if not values or used != set(values):
        raise ValueError('Use each bound input; a replacement constant is not independent verification')
    return number(walk(tree))


def coverage(packet):
    entries = packet.get('claimAssertions', [])
    declared = packet.get('coverage', {}).get('claim-support', {})
    ids = declared.get('assertionIds', [])
    actual = [a.get('id') for a in entries]
    if declared.get('status') == 'not-applicable':
        return (bool(declared.get('reason', '').strip()) and not ids and not entries,
                'Non-applicability needs a reason and no omitted declared claim assertions')
    ok = (declared.get('status') == 'checked' and bool(entries) and len(set(actual)) == len(actual)
          and all(isinstance(i, str) and i for i in actual) and len(set(ids)) == len(ids) and set(ids) == set(actual))
    return ok, 'Cover the material quantified, scope, owner-cash and proposed-review calculations, or state why none apply; completeness remains reviewed'


def evaluate(study, assertion, spec, packet):
    import model_workbook as mw
    from publication_review import local
    for key in ('id', 'claimId', 'location', 'rationale'):
        if not isinstance(assertion.get(key), str) or not assertion[key].strip():
            raise ValueError('Claim assertion requires ' + key)
    claims = {c['id']: c for c in packet['handoff']['claims']}
    if assertion['claimId'] not in claims:
        raise ValueError('Assertion must identify a recorded claim or reviewer finding')
    registered = {s['id'] for s in packet['handoff']['sources']}
    if not assertion.get('sourceIds') or not set(assertion['sourceIds']) <= registered:
        raise ValueError('Claim assertion requires registered source references')
    engine = mw.Engine(mw.with_case(spec, assertion.get('selector')))

    def read(binding, numeric=True):
        if not isinstance(binding, dict):
            raise ValueError('Use a model, modelFormula or frozen file/pointer binding')
        if set(binding) == {'model'}:
            result = engine.value(*mw.target(binding['model'], ''))
        elif set(binding) == {'modelFormula'}:
            if not str(binding['modelFormula']).startswith('='):
                raise ValueError('A model formula begins with =')
            if not mw.REF.search(binding['modelFormula']):
                raise ValueError('A model formula must consume model inputs')
            temporary = copy.deepcopy(mw.with_case(spec, assertion.get('selector')))
            if '__ClaimCheck__' in temporary['sheets']:
                raise ValueError('Reserved claim-check sheet name is already in use')
            temporary['sheets']['__ClaimCheck__'] = {'cells': {'A1': {'value': binding['modelFormula']}}}
            result = mw.Engine(temporary).value('__ClaimCheck__', 'A1')
        elif set(binding) == {'file', 'pointer'}:
            if binding['file'] not in packet['reviewedFiles']:
                raise ValueError('Claim data must be among the frozen review inputs')
            result = json.loads(local(study, binding['file']).read_text(encoding='utf-8-sig'))
            pointer = binding['pointer']
            if pointer and not pointer.startswith('/'):
                raise ValueError('Use an explicit JSON pointer')
            for part in pointer.split('/')[1:]:
                part = part.replace('~1', '/').replace('~0', '~')
                result = result[int(part)] if isinstance(result, list) else result[part]
        else:
            raise ValueError('Unsupported or ambiguous input binding')
        return number(result) if numeric else result

    kind = assertion['kind']
    if kind == 'bounded-bridge':
        from bounded_bridge import solve
        if not assertion.get('domainRationale','').strip():
            raise ValueError('Explain independent ranges, matched units and omitted constraints')
        drivers = [{'id':d['id'],'coefficient':number(d['coefficient']), 'low':read(d['low']), 'high':read(d['high'])}
                   for d in assertion['drivers']]
        result = solve(read(assertion['offset']),read(assertion['target']),drivers)
        if type(assertion.get('expectedFeasible')) is not bool or result['feasible']!=assertion['expectedFeasible']:
            raise ValueError('Bounded bridge feasibility contradicts the claim: '+json.dumps(result))
        return json.dumps(result)
    if kind == 'rendered-measure':
        from display_bindings import check_displays
        return check_displays(study,assertion['displays'],[read(b) for b in assertion['values']],packet)
    if kind in ('comparison', 'incremental-flow'):
        from comparison_checks import evaluate as compare
        return compare(assertion, read)
    if kind == 'quantified-set':
        members = assertion['members']
        ids = [m['id'] for m in members]
        if not ids or len(set(ids)) != len(ids):
            raise ValueError('A quantified set needs nonempty, unique members')
        scope = assertion['scope']
        if scope == 'universe':
            universe = read(assertion['universeIds'], numeric=False)
            if (not isinstance(universe, list) or len(set(universe)) != len(universe)
                    or set(universe) != set(ids) or not assertion.get('universeDefinition', '').strip()):
                raise ValueError('A universe claim must cover its explicitly defined complete input set')
        elif scope != 'listed':
            raise ValueError('Set scope is listed or universe, not an implicit entire market')
        ops = {'>': operator.gt, '>=': operator.ge, '<': operator.lt, '<=': operator.le, '==': operator.eq}
        predicate = assertion['predicate']
        compare, threshold = ops[predicate['op']], number(predicate['threshold'])
        hits = sum(compare(read(m['value']), threshold) for m in members)
        supported = {'all': hits == len(ids), 'any': hits > 0, 'none': hits == 0}
        if assertion['quantifier'] not in supported or not supported[assertion['quantifier']]:
            raise ValueError(f'Quantified claim is false: {hits} of {len(ids)} members satisfy the predicate')
        return f'{hits} of {len(ids)} comparisons in the declared {scope} set satisfy {predicate["op"]} {threshold}'
    if kind == 'evidence-scope':
        scopes = assertion['sourceScopes']
        allowed = {'unit', 'company', 'sample', 'industry'}
        if set(scopes) != set(assertion['sourceIds']) or not set(scopes.values()) <= allowed:
            raise ValueError('Give a supported population scope for each cited source')
        conclusion = assertion['conclusionScope']
        if conclusion not in allowed:
            raise ValueError('Unknown conclusion population')
        extrapolates = conclusion == 'industry' and 'industry' not in scopes.values()
        extrapolates |= conclusion == 'company' and set(scopes.values()) == {'unit'}
        claim = claims[assertion['claimId']]
        if extrapolates and not (claim['basis'] in ('inference', 'assumption') and claim.get('rationale')
                                 and assertion.get('limitations', '').strip()):
            raise ValueError('Broader population conclusions need a reasoned inference and explicit limits, not a reported fact')
        return 'Declared evidence/conclusion scopes reconciled; representativeness and published qualification require the reader'
    if kind == 'cash-boundary':
        numerator, denominator, shown = [read(assertion[k]) for k in ('numerator', 'denominator', 'ratio')]
        if denominator <= 0 or not math.isclose(numerator / denominator, shown, rel_tol=1e-6, abs_tol=1e-8):
            raise ValueError('Cash ratio does not reproduce from its declared numerator and denominator')
        nci = assertion['nonControllingInterests']
        if nci not in ('none', 'present', 'unknown'):
            raise ValueError('Declare whether non-owner interests exist')
        if assertion['numeratorBoundary'] not in ('consolidated', 'parent-economic', 'parent-available') or assertion['denominatorBoundary'] not in ('parent-equity', 'group-capital', 'parent-distributions'):
            raise ValueError('Use explicit supported cash and capital boundaries')
        interpretation = assertion['interpretation']
        if interpretation not in ('owner-return', 'consolidated-proxy', 'distribution-coverage'):
            raise ValueError('Declare the interpretation of the cash metric')
        if interpretation == 'owner-return':
            if assertion['denominatorBoundary'] != 'parent-equity':
                raise ValueError('An owner cash yield needs the matching equity boundary')
            if nci != 'none':
                if assertion['numeratorBoundary'] != 'parent-economic':
                    raise ValueError('Consolidated cash is not parent-owner cash where other owners exist')
                bridge = assertion.get('reconciliation', {})
                base, non_owner, unavailable = [read(bridge[k]) for k in ('baseCash', 'nonOwnerEconomicCash', 'unavailableCash')]
                if not bridge.get('rightsBasis', '').strip() or not math.isclose(base - non_owner - unavailable, numerator, rel_tol=1e-6, abs_tol=1e-8):
                    raise ValueError('Reconcile economic ownership and access; partner dividends alone do not establish owner cash')
        elif not assertion.get('limitations', '').strip():
            raise ValueError('A consolidated proxy or distribution-coverage measure needs its boundary/access limitation')
        if interpretation == 'distribution-coverage' and assertion['denominatorBoundary'] != 'parent-distributions':
            raise ValueError('Distribution coverage uses distributions, not equity market value')
        return 'Cash arithmetic and declared ownership/access bridge reconcile; source rights and business-specific measure remain reviewed'
    if kind == 'calculation':
        if assertion['role'] not in ('author', 'reviewer'):
            raise ValueError('Identify whether this is an author or reviewer calculation')
        values = {name: read(binding) for name, binding in assertion['inputs'].items()}
        expected = arithmetic(assertion['expression'], values)
        decimals = assertion.get('decimals', 6)
        if type(decimals) is not int or not 0 <= decimals <= 6:
            raise ValueError('Declare zero to six display decimals')
        if round(expected, decimals) != round(number(assertion['shown']), decimals):
            raise ValueError(f'Calculation shown {assertion["shown"]} does not reproduce: {expected}')
        if assertion.get('displays'):
            from display_bindings import check_displays
            check_displays(study,assertion['displays'],[expected],packet)
        return f'{assertion["role"]} calculation reproduces: {round(expected, decimals)}'
    raise ValueError('Unsupported claim assertion kind: ' + str(kind))
