"""Summarize dated dividend-yield and government-yield observations on a declared basis.

Input JSON: benchmark {currency, tenor, rationale}, dividendCurrency, yieldBasis,
sourceIds, observations [{date,bondDate,dividendYield,governmentYield}]. Optional
targetSpread and sustainableDps produce an explicitly selected conditional price;
the historical mean is not automatically chosen as the target.
"""
from datetime import date
import json
import math
from pathlib import Path
import statistics
import sys

def summarize(data):
    benchmark=data['benchmark']
    if not all(str(benchmark.get(k,'')).strip() for k in ('currency','tenor','rationale')): raise ValueError('Explain benchmark currency, tenor and economic relevance')
    if not data.get('dividendCurrency') or not data.get('yieldBasis') or not data.get('sourceIds'): raise ValueError('Declare dividend currency, yield basis and source references')
    if benchmark['currency']!=data['dividendCurrency'] and not str(data.get('crossCurrencyRationale','')).strip(): raise ValueError('A cross-currency comparison needs an explicit rationale and FX/access limitations')
    rows=data['observations']; dates=[date.fromisoformat(r['date']) for r in rows]
    if len(rows)<2 or len(set(dates))!=len(rows) or dates!=sorted(dates): raise ValueError('Supply at least two distinct chronological observations; sample size does not establish calibration quality')
    spreads=[]; yields=[]; lags=[]
    for r,d in zip(rows,dates):
        bond=date.fromisoformat(r['bondDate'])
        if bond>d: raise ValueError('A benchmark observation cannot come from the future')
        dy,rate=r['dividendYield'],r['governmentYield']
        if any(type(v) not in (int,float) or not math.isfinite(v) for v in (dy,rate)) or dy<0: raise ValueError('Use finite fractional yields and nonnegative dividend yield')
        yields.append(dy); spreads.append(dy-rate); lags.append((d-bond).days)
    result={'observations':len(rows),'start':rows[0]['date'],'end':rows[-1]['date'],'benchmark':benchmark,
            'yieldBasis':data['yieldBasis'],'meanSpread':statistics.mean(spreads),'medianSpread':statistics.median(spreads),
            'sampleSdSpread':statistics.stdev(spreads),'meanAbsoluteYield':statistics.mean(yields),'currentSpread':spreads[-1],
            'maxBondObservationLagDays':max(lags),'sourceIds':data['sourceIds'],
            'limit':'Observed spreads are descriptive. Benchmark choice, rate/regime changes, payout sustainability and timing require economic judgment.'}
    if 'targetSpread' in data:
        required=rows[-1]['governmentYield']+data['targetSpread']; dps=data['sustainableDps']
        if required<=0 or type(dps) not in (int,float) or not math.isfinite(dps) or dps<0: raise ValueError('Conditional capitalization needs positive required yield and nonnegative sustainable DPS')
        result.update(selectedTargetSpread=data['targetSpread'],conditionalRequiredYield=required,conditionalPrice=dps/required)
    return result

if __name__=='__main__': print(json.dumps(summarize(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))),indent=2))
