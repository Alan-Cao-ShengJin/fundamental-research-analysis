"""Grade a brief.json from the fiscal-calendar pack against the expected arithmetic. Judgment is graded by reading.

python -B -X utf8 grade_fiscal_calendar.py <brief.json> [epsPeriod]
"""
import json, re, sys
from pathlib import Path

brief = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
period = sys.argv[2] if len(sys.argv) > 2 else ' '.join(str(brief['decision'].get(k, '')) for k in ('targetBasis',))
d = brief['decision']
results = []
def grade(name, ok, detail):
    results.append((name, ok, detail)); print(('PASS ' if ok else 'FAIL ') + name + ': ' + detail)
target = float(d['targetPrice'])
grade('target', abs(target - 36.0) <= 0.10 or abs(target - 37.5) <= 0.10, f'{target} (expected 36.00 on FY2027E or 37.50 on NTM; 40.50 is the target-date roll)')
grade('period', bool(re.search(r'FY ?20?27|NTM', period, re.I)) and not re.search(r'FY ?20?28', period, re.I), f'{period!r}')
grade('price-reference', abs(float(d['referencePrice']) - 30.0) < 0.01 and re.search(r'6 Nov|2026-11-06|Nov(ember)? 6', str(d.get('priceObservation', ''))) is not None,
      f'{d["referencePrice"]} at {d.get("priceObservation")!r}')
grade('rating', d.get('rating') == 'Buy', str(d.get('rating')))
grade('tier', str(d.get('attractiveness', '')).lower() == 'unattractive' and d.get('newMoney', 'no') == 'no', f'{d.get("attractiveness")} / new money {d.get("newMoney")}')
grade('dividend-separate', not any(k in d for k in ('dividendPerShare', 'dividendsToTargetDate')) and 0.030 <= float(d.get('dividendYield') or 0) <= 0.037,
      f'dividendYield {d.get("dividendYield")}')
sys.exit(0 if all(ok for _, ok, _ in results) else 1)
