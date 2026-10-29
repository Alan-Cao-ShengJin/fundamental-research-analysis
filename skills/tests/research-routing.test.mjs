import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

const catalog = JSON.parse(readFileSync(new URL('../catalog.json', import.meta.url), 'utf8'));

function dependencies(stage, visited = new Set()) {
  for (const name of catalog.stages[stage].requiredBefore) {
    if (!visited.has(name)) { visited.add(name); dependencies(name, visited); }
  }
  return visited;
}

describe('company research risk dependencies', () => {
  it('requires early governance and financial screening before forecasts in every full company route', () => {
    for (const flow of Object.values(catalog.flows).filter(flow => flow.includes('company-forecast'))) {
      for (const risk of ['corporate-governance', 'financial-red-flags']) {
        expect(flow).toContain(risk);
        expect(flow.indexOf(risk)).toBeLessThan(flow.indexOf('revenue-projection'));
        expect(dependencies('revenue-projection').has(risk)).toBe(true);
        expect(dependencies('conclusion').has(risk)).toBe(true);
      }
    }
  });

  it('keeps one financial-quality skill across three passes with the audit upstream of valuation', () => {
    for (const stage of ['financial-red-flags', 'model-audit', 'thesis-validation']) {
      expect(catalog.stages[stage].skill).toBe('pip-financial-quality');
      expect(catalog.stages[stage].output).toBe('financial-quality');
    }
    expect(dependencies('model-audit').has('financial-red-flags')).toBe(true);
    expect(dependencies('valuation').has('model-audit')).toBe(true);
    expect(dependencies('thesis-validation').has('valuation')).toBe(true);
  });

  it('permits a filing-based red-flag review without full forecasting or a stock call', () => {
    const flow = catalog.flows['financial-red-flag-review'];
    expect(flow).toContain('financial-red-flags');
    expect(dependencies('financial-red-flags').has('evidence')).toBe(true);
    for (const stage of ['company-model-setup', 'company-forecast', 'valuation', 'conclusion']) {
      expect(flow).not.toContain(stage);
      expect(dependencies('financial-red-flags').has(stage)).toBe(false);
    }
  });
});
