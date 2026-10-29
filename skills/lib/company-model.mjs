import { z } from 'zod';
import { createHash } from 'node:crypto';

// Local deterministic graph helper, not a data feed, complete financial-model
// builder, live worker, or proof that the assumptions describe the business.
export const COMPANY_MODEL_ENGINE_VERSION = '0.1.0';
const id = z.string().min(1).max(160);
const timestamp = z.iso.datetime({ offset: true });
const Unit = z.object({ label: id, scale: z.number().positive().finite(),
  dimensions: z.record(id, z.number().int().min(-8).max(8)), }).strict();
const common = { id, metric: id, periodId: id, unit: Unit,
  classification: z.enum(['reported', 'derived', 'guidance', 'assumption', 'forecast']),
  sourceIds: z.array(id).max(30), rationale: z.string().min(1) };
const Node = z.discriminatedUnion('kind', [
  z.object({ ...common, kind: z.literal('input'), value: z.number().finite().nullable() }).strict(),
  z.object({ ...common, kind: z.literal('calculation'),
    operation: z.enum(['add', 'subtract', 'multiply', 'divide', 'min', 'max']),
    inputs: z.array(id).min(1).max(100) }).strict(),
]);
export const CompanyModelSchema = z.object({
  id, version: z.number().int().positive(), entityId: id, asOf: timestamp,
  synthetic: z.boolean(),
  periods: z.array(z.object({ id, start: z.iso.date(), end: z.iso.date(),
    status: z.enum(['actual', 'forecast']) }).strict()).min(1),
  sources: z.array(z.object({ id, location: id, availableAt: timestamp.nullable(), synthetic: z.boolean() }).strict()),
  nodes: z.array(Node).min(1).max(10000),
  outputs: z.array(id).min(1),
  checks: z.array(z.object({ id, left: id, right: id,
    absoluteTolerance: z.number().finite().nonnegative(), blocking: z.boolean() }).strict()),
}).strict();

const dimensions = value => Object.fromEntries(Object.entries(value).filter(([, power]) => power !== 0).sort(([a], [b]) => a.localeCompare(b)));
const sameDimensions = (a, b) => JSON.stringify(dimensions(a)) === JSON.stringify(dimensions(b));
function combineDimensions(items, divide = false) {
  const out = {};
  for (const [index, item] of items.entries()) for (const [key, power] of Object.entries(item))
    out[key] = (out[key] ?? 0) + power * (divide && index > 0 ? -1 : 1);
  return dimensions(out);
}
function stable(value) {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') return Object.fromEntries(Object.keys(value).sort().map(key => [key, stable(value[key])]));
  return value;
}
export const modelFingerprint = value => createHash('sha256').update(JSON.stringify(stable(CompanyModelSchema.parse(value)))).digest('hex');

export function validateCompanyModel(value) {
  const model = CompanyModelSchema.parse(value);
  for (const [name, items] of [['period', model.periods], ['source', model.sources], ['node', model.nodes], ['check', model.checks]])
    if (new Set(items.map(item => item.id)).size !== items.length) throw new Error(`Duplicate ${name} ID.`);
  const periods = new Map(model.periods.map(p => [p.id, p]));
  const sources = new Map(model.sources.map(s => [s.id, s]));
  const nodes = new Map(model.nodes.map(n => [n.id, n]));
  for (const period of model.periods) if (period.start > period.end) throw new Error(`Reversed period ${period.id}.`);
  for (const source of model.sources) {
    if (source.availableAt && Date.parse(source.availableAt) > Date.parse(model.asOf)) throw new Error(`Future source ${source.id} exceeds model cutoff.`);
    if (!model.synthetic && source.synthetic) throw new Error('Synthetic source cannot support a real model.');
  }
  for (const node of model.nodes) {
    if (!periods.has(node.periodId)) throw new Error(`Unknown period for ${node.id}.`);
    if (node.sourceIds.some(source => !sources.has(source))) throw new Error(`Unknown source for ${node.id}.`);
    if (['reported', 'guidance'].includes(node.classification) && !node.sourceIds.length) throw new Error(`Source required for ${node.id}.`);
    if (node.classification === 'reported' && periods.get(node.periodId).status !== 'actual') throw new Error(`Reported value in forecast period: ${node.id}.`);
    if (node.kind === 'calculation') {
      if (node.inputs.some(input => !nodes.has(input))) throw new Error(`Unknown calculation input for ${node.id}.`);
      if (['subtract', 'divide'].includes(node.operation) && node.inputs.length !== 2) throw new Error(`Two inputs required for ${node.operation}.`);
      const inputs = node.inputs.map(key => nodes.get(key).unit.dimensions);
      const expected = ['multiply', 'divide'].includes(node.operation)
        ? combineDimensions(inputs, node.operation === 'divide') : inputs[0];
      if (!['multiply', 'divide'].includes(node.operation) && inputs.some(unit => !sameDimensions(unit, expected))) throw new Error(`Incompatible input units for ${node.id}.`);
      if (!sameDimensions(expected, node.unit.dimensions)) throw new Error(`Incorrect output units for ${node.id}.`);
    }
  }
  for (const output of model.outputs) if (!nodes.has(output)) throw new Error(`Unknown output ${output}.`);
  for (const check of model.checks) {
    if (!nodes.has(check.left) || !nodes.has(check.right)) throw new Error(`Unknown check reference ${check.id}.`);
    if (!sameDimensions(nodes.get(check.left).unit.dimensions, nodes.get(check.right).unit.dimensions)) throw new Error(`Incompatible check units ${check.id}.`);
  }
  // Validate the entire graph, including nodes that are not exported outputs.
  const visiting = new Set(), done = new Set();
  function visit(key) {
    if (visiting.has(key)) throw new Error(`Circular model dependency at ${key}.`);
    if (done.has(key)) return;
    visiting.add(key);
    const node = nodes.get(key);
    if (node.kind === 'calculation') node.inputs.forEach(visit);
    visiting.delete(key); done.add(key);
  }
  nodes.forEach((_, key) => visit(key));
  return model;
}

export function evaluateCompanyModel(value, { scenarioId = 'base', overrides = {} } = {}) {
  const model = validateCompanyModel(value), nodes = new Map(model.nodes.map(n => [n.id, n]));
  for (const [key, number] of Object.entries(overrides)) {
    const node = nodes.get(key);
    if (!node || node.kind !== 'input' || !['assumption', 'forecast'].includes(node.classification)) throw new Error(`Scenario cannot override ${key}.`);
    if (typeof number !== 'number' || !Number.isFinite(number)) throw new Error(`Finite scenario value required for ${key}.`);
  }
  const values = new Map(), lineage = new Map();
  function calculate(key) {
    if (values.has(key)) return values.get(key);
    const node = nodes.get(key);
    let result;
    if (node.kind === 'input') {
      result = Object.hasOwn(overrides, key) ? overrides[key] : node.value;
      lineage.set(key, [key]);
    } else {
      const raw = node.inputs.map(calculate);
      lineage.set(key, [...new Set(node.inputs.flatMap(input => lineage.get(input)))]);
      if (raw.some(number => number === null)) result = null;
      else {
        const inputs = raw.map((number, index) => number * nodes.get(node.inputs[index]).unit.scale);
        switch (node.operation) {
          case 'add': result = inputs.reduce((a, b) => a + b, 0); break;
          case 'subtract': result = inputs[0] - inputs[1]; break;
          case 'multiply': result = inputs.reduce((a, b) => a * b, 1); break;
          case 'divide':
            if (inputs[1] === 0) throw new Error(`Zero denominator at ${key}.`);
            result = inputs[0] / inputs[1]; break;
          case 'min': result = Math.min(...inputs); break;
          case 'max': result = Math.max(...inputs); break;
        }
        result /= node.unit.scale;
        if (!Number.isFinite(result)) throw new Error(`Nonfinite result at ${key}.`);
      }
    }
    values.set(key, result); return result;
  }
  nodes.forEach((_, key) => calculate(key));
  const checks = model.checks.map(check => {
    const left = calculate(check.left), right = calculate(check.right);
    const delta = left === null || right === null ? null : left - right * nodes.get(check.right).unit.scale / nodes.get(check.left).unit.scale;
    return { id: check.id, blocking: check.blocking, result: delta === null ? 'not-run' : Math.abs(delta) <= check.absoluteTolerance ? 'pass' : 'fail', delta };
  });
  const outputs = Object.fromEntries(model.outputs.map(key => [key, {
    value: calculate(key), unit: nodes.get(key).unit, inputIds: lineage.get(key),
    sourceIds: [...new Set(lineage.get(key).flatMap(input => nodes.get(input).sourceIds))],
  }]));
  const warnings = model.sources.filter(source => source.availableAt === null).map(source => `Unknown source availability: ${source.id}`);
  const fingerprint = modelFingerprint(model);
  const runId = createHash('sha256').update(JSON.stringify(stable({ modelFingerprint: fingerprint, engineVersion: COMPANY_MODEL_ENGINE_VERSION, scenarioId, overrides }))).digest('hex');
  return { modelId: model.id, modelVersion: model.version, modelFingerprint: fingerprint, engineVersion: COMPANY_MODEL_ENGINE_VERSION, runId, asOf: model.asOf,
    scenarioId, synthetic: model.synthetic, overrides: { ...overrides }, outputs, checks, warnings,
    calculationStatus: Object.values(outputs).some(output => output.value === null) ? 'partial' : checks.some(check => check.blocking && check.result !== 'pass') ? 'checks-failed' : 'calculated',
    meaning: 'Arithmetic and lineage only; not financial completeness, source truth, valuation readiness, a running agent or trading approval.' };
}

export function compareModelScenario(value, options) {
  const baseline = evaluateCompanyModel(value), scenario = evaluateCompanyModel(value, options);
  const changes = Object.fromEntries(Object.keys(baseline.outputs).filter(key => baseline.outputs[key].value !== scenario.outputs[key].value).map(key => {
    const before = baseline.outputs[key].value, after = scenario.outputs[key].value;
    return [key, { before, after, delta: before === null || after === null ? null : after - before, unit: baseline.outputs[key].unit }];
  }));
  return { baseline, scenario, changes };
}

export function evaluationMatchesModel(evaluation, value) {
  const model = validateCompanyModel(value);
  return evaluation.modelId === model.id && evaluation.modelVersion === model.version && evaluation.modelFingerprint === modelFingerprint(model)
    && evaluation.engineVersion === COMPANY_MODEL_ENGINE_VERSION;
}
