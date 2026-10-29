import { describe, it, expect } from 'vitest';
import { readFileSync } from 'node:fs';
import { evaluateCompanyModel, compareModelScenario, evaluationMatchesModel } from '../lib/company-model.mjs';
const load = () => JSON.parse(readFileSync(new URL('../pip-company-model/references/agent-model-example.json', import.meta.url), 'utf8'));

describe('executable company model', () => {
  it('links operating drivers, cash flow, balance sheet and valuation without retyped outputs', () => {
    const result = evaluateCompanyModel(load());
    expect(result.outputs.revenue.value).toBe(1000);
    expect(result.outputs['net.income'].value).toBe(285);
    expect(result.outputs.fcfe.value).toBe(255);
    expect(result.outputs['closing.cash'].value).toBe(275);
    expect(result.outputs['illustrative.value'].value).toBe(57);
    expect(result.checks[0].result).toBe('pass');
    expect(result.outputs['illustrative.value'].inputIds).toContain('price');
    expect(result.outputs['illustrative.value'].sourceIds).toContain('fixture');
  });
  it('reruns the downstream economics when a driver changes and preserves the base model', () => {
    const model = load(), before = structuredClone(model);
    const result = compareModelScenario(model, { scenarioId: 'lower-price', overrides: { price: 9 } });
    expect(result.scenario.outputs['net.income'].value).toBe(210);
    expect(result.scenario.outputs.fcfe.value).toBe(180);
    expect(result.scenario.outputs['illustrative.value'].value).toBe(42);
    expect(result.changes['illustrative.value'].delta).toBe(-15);
    expect(result.scenario.checks[0].result).toBe('pass');
    expect(model).toEqual(before);
  });
  it('converts compatible scales and rejects dimensionally invalid formulas', () => {
    const model = load();
    model.nodes.find(n => n.id === 'revenue').unit.scale = 1000;
    expect(evaluateCompanyModel(model).outputs['net.income'].value).toBe(285);
    model.nodes.find(n => n.id === 'cash.cogs').unit.dimensions = { product: 1 };
    expect(() => evaluateCompanyModel(model)).toThrow(/units/);
  });
  it('exposes missing driver inputs rather than silently turning them into zero', () => {
    const model = load(); model.nodes.find(n => n.id === 'price').value = null;
    const result = evaluateCompanyModel(model);
    expect(result.calculationStatus).toBe('partial');
    expect(result.outputs['illustrative.value'].value).toBeNull();
    expect(result.checks[0].result).toBe('not-run');
  });
  it('rejects circular formulas, zero denominators and overrides of reported facts', () => {
    const model = load(); model.nodes.find(n => n.id === 'cash.profit').inputs[0] = 'ebit';
    expect(() => evaluateCompanyModel(model)).toThrow(/Circular/);
    expect(() => evaluateCompanyModel(load(), { overrides: { shares: 0 } })).toThrow(/Zero denominator/);
    expect(() => evaluateCompanyModel(load(), { overrides: { 'opening.cash': 999 } })).toThrow(/cannot override/);
  });
  it('rejects future source availability and detects stale model-dependent evaluations', () => {
    const model = load(), result = evaluateCompanyModel(model);
    expect(evaluationMatchesModel(result, model)).toBe(true);
    expect(evaluationMatchesModel({ ...result, engineVersion: 'old-engine' }, model)).toBe(false);
    model.nodes.find(n => n.id === 'price').value = 11;
    expect(evaluationMatchesModel(result, model)).toBe(false);
    model.sources[0].availableAt = '2026-10-29T12:00:00+08:00';
    expect(() => evaluateCompanyModel(model)).toThrow(/Future source/);
  });
  it('does not report calculated success when a blocking economic identity fails', () => {
    const model = load(); model.nodes.find(n => n.id === 'opening.equity').value = 1;
    const result = evaluateCompanyModel(model);
    expect(result.calculationStatus).toBe('checks-failed');
    expect(result.checks[0].result).toBe('fail');
  });
});
