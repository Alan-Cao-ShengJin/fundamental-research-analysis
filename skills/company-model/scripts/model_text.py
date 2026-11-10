"""Generate live Excel text formulas from model references, not saved narrative numbers.

Only simple numeric TEXT formats are supported. Source interpretation and surrounding
claims remain reviewed. No template code execution, attributes or formatting expressions.
"""
from decimal import Decimal, ROUND_HALF_UP, localcontext
import math
import re
from string import Formatter


def format_number(value, code):
    match = re.fullmatch(r'(#,##)?0(?:\.(0{1,6}))?(%)?', code) if isinstance(code, str) else None
    if not match or type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError('TEXT supports finite numbers with 0, 0.00, #,##0.00 or percentage formats (up to six decimals)')
    decimals = len(match[2] or '')
    with localcontext() as context:
        context.prec = 50
        amount = Decimal(str(value)) * (100 if match[3] else 1)
        amount = amount.quantize(Decimal(1).scaleb(-decimals), rounding=ROUND_HALF_UP)
        if amount == 0: amount = abs(amount)
        return format(amount, (',' if match[1] else '') + f'.{decimals}f') + ('%' if match[3] else '')


def concatenate(a, b):
    def text(value):
        if value == '#N/A': raise ValueError('Error-valued or error-like literal concatenation is outside the supported subset')
        if isinstance(value, str): return value
        if type(value) is bool: return 'TRUE' if value else 'FALSE'
        if type(value) in (int, float) and math.isfinite(value): return str(value) if type(value) is int else format(value, '.15g')
        raise ValueError('Concatenation supports scalar text, logical and finite numeric values')
    return text(a) + text(b)


def formula(template, inputs):
    def literal(value): return '"' + value.replace('"', '""') + '"'
    if not isinstance(template, str) or not isinstance(inputs, dict) or not inputs:
        raise ValueError('A linked explanation needs a template and named model inputs')
    terms, used = [], set()
    for text, field, spec, conversion in Formatter().parse(template):
        if text: terms.append(literal(text))
        if field is None: continue
        if not re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*', field) or field not in inputs or spec or conversion:
            raise ValueError('Use plain named placeholders without template expressions or conversions')
        used.add(field); binding = inputs[field]
        ref, style = binding['model'], binding.get('style', 'number')
        from model_workbook import REF, target
        if not isinstance(ref, str) or not REF.fullmatch(ref) or '!' not in ref or ':' in ref:
            raise ValueError('Use an explicit single model cell reference')
        sheet, address = target(ref, '')
        ref = "'" + sheet.replace("'", "''") + "'!" + address
        if style == 'text':
            terms.append(ref); continue
        decimals = binding.get('decimals', 2)
        if style not in ('number', 'percent', 'multiple') or type(decimals) is not int or not 0 <= decimals <= 6:
            raise ValueError('Use number/percent/multiple and zero to six decimals')
        code = ('#,##0' if binding.get('grouping', False) else '0') + ('.' + '0' * decimals if decimals else '') + ('%' if style == 'percent' else '')
        terms.append(f'TEXT({ref},{literal(code)})')
        if style == 'multiple': terms.append(literal('x'))
    if used != set(inputs):
        raise ValueError('Every bound input must appear in the explanation')
    return '=' + '&'.join(terms)
