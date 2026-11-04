import { describe, expect, it } from 'vitest';
import { readFileSync } from 'node:fs';
import { compareForwardPE } from '../valuation-thesis/scripts/compare_forward_pe.mjs';

const fixture = JSON.parse(readFileSync(new URL('../research-brief/assets/calibration-case.json', import.meta.url), 'utf8'));
const input = () => structuredClone(fixture.comparison);

describe('current-forward P/E comparisons', () => {
  it('connects the synthetic operating forecast to EPS before valuing it', () => {
    const x=fixture.operatingInputs;
    const grossProfit=x.forecastUnits*x.pricePerUnit*x.forecastGrossMargin;
    const previousGrossProfit=x.priorUnits*x.pricePerUnit*x.priorGrossMargin;
    const eps=(grossProfit-x.forecastOperatingExpense)*(1-x.taxRate)/x.dilutedShares;
    expect(grossProfit).toBeLessThan(previousGrossProfit);
    expect(eps).toBeCloseTo(fixture.comparison.ourForecast.eps, 12);
  });
  it('distinguishes unchanged own P/E from an earnings downgrade at the broker multiple', () => {
    const r=compareForwardPE(input());
    expect(r.ownForwardPE).toBe(20); expect(r.consensusForwardPE).toBe(16);
    expect(r.targetPrice).toBe(120); expect(r.priceReturn).toBeCloseTo(.20, 12);
    expect(r.unchangedOwnPEPrice).toBe(100);
    expect(r.earningsResetAtConsensusPE.price).toBe(80);
    expect(r.earningsResetAtConsensusPE.direction).toBe('downgrade');
    expect(r.ownForecastBridge.earningsEffect).toBe(0);
    expect(r.ownForecastBridge.multipleEffect).toBe(20);
    expect(r.consensusBridge.earningsEffect).toBe(-20);
    expect(r.consensusBridge.multipleEffect).toBe(40);
    expect(r.consensusBridge.earningsEffect+r.consensusBridge.multipleEffect).toBe(r.targetPrice-r.price);
  });
  it('handles a higher own forecast as an upgrade rather than forcing a downside case', () => {
    const x=input();x.ourForecast.eps=6.25;x.consensusForecast.eps=5;
    const r=compareForwardPE(x);
    expect(r.earningsResetAtConsensusPE.direction).toBe('upgrade');
    expect(r.earningsResetAtConsensusPE.price).toBe(125);
    expect(r.consensusBridge.earningsEffect+r.consensusBridge.multipleEffect).toBeCloseTo(r.targetPrice-r.price,12);
  });
  it('keeps unavailable consensus unknown', () => {
    const x=input();x.consensusForecast=null;const r=compareForwardPE(x);
    expect(r.consensusForwardPE).toBeNull();expect(r.consensusBridge).toBeNull();
    expect(r.earningsResetAtConsensusPE).toBeNull();expect(r.targetPrice).toBe(120);
  });
  it.each(['periodStart','periodEnd','earningsDefinition','shareBasis','currency'])('rejects unmatched %s', field => {
    const x=input();x.consensusForecast.basis[field]=field==='periodStart'?'2028-01-01':field==='periodEnd'?'2028-12-31':field==='currency'?'EUR':'different';
    expect(()=>compareForwardPE(x)).toThrow();
  });
  it.each([0,-1,null,NaN,Infinity])('rejects unusable EPS %s', value => {
    const x=input();x.ourForecast.eps=value;expect(()=>compareForwardPE(x)).toThrow();
  });
  it('rejects missing definitions, impossible dates and a silently added later-period target forecast', () => {
    const x=input();delete x.ourForecast.basis.earningsDefinition;expect(()=>compareForwardPE(x)).toThrow();
    const y=input();y.ourForecast.basis.periodStart='2027-02-30';expect(()=>compareForwardPE(y)).toThrow();
    expect(()=>compareForwardPE({...input(),targetForecast:{eps:6}})).toThrow('Unsupported input');
  });
});
