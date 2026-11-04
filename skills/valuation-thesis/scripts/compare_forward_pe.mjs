/** Fixed-current-earnings P/E comparison. Arithmetic, not valuation calibration.
 * CLI: node compare_forward_pe.mjs input.json
 */
import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const fields = ['currency', 'periodStart', 'periodEnd', 'earningsDefinition', 'shareBasis'];
function positive(value, label) {
  if (typeof value !== 'number' || !Number.isFinite(value) || value <= 0) {
    throw new Error(`${label} must be a finite positive number; this helper requires positive EPS`);
  }
  return value;
}
function forecast(value, label, currency) {
  positive(value?.eps, `${label}.eps`);
  for (const key of fields) {
    if (typeof value?.basis?.[key] !== 'string' || !value.basis[key].trim()) {
      throw new Error(`${label}.basis.${key} must be explicit`);
    }
  }
  for (const key of ['periodStart', 'periodEnd']) {
    const date = value.basis[key];
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date) || !Number.isFinite(Date.parse(date)) ||
        new Date(date).toISOString().slice(0, 10) !== date) throw new Error(`${label}: invalid ${key}`);
  }
  if (value.basis.periodEnd < value.basis.periodStart) throw new Error(`${label}: reversed period`);
  if (value.basis.currency !== currency) throw new Error(`${label}: price and EPS currency mismatch`);
}

export function compareForwardPE(input) {
  const allowed = new Set(['price', 'currency', 'targetPE', 'ourForecast', 'consensusForecast']);
  for (const key of Object.keys(input)) if (!allowed.has(key)) throw new Error(`Unsupported input: ${key}`);
  const price = positive(input.price, 'price');
  const targetPE = positive(input.targetPE, 'targetPE');
  if (!/^[A-Z]{3}$/.test(input.currency ?? '')) throw new Error('Explicit three-letter currency required');
  forecast(input.ourForecast, 'ourForecast', input.currency);
  const ours = input.ourForecast.eps;
  const ownForwardPE = price / ours;
  const targetPrice = ours * targetPE;
  let consensusForwardPE = null, earningsResetAtConsensusPE = null, consensusBridge = null;
  if (input.consensusForecast != null) {
    forecast(input.consensusForecast, 'consensusForecast', input.currency);
    for (const key of fields) {
      if (input.ourForecast.basis[key] !== input.consensusForecast.basis[key]) {
        throw new Error(`Forecast basis mismatch: ${key}; reconcile before comparison`);
      }
    }
    const consensus = input.consensusForecast.eps;
    consensusForwardPE = price / consensus;
    const resetPrice = ours * consensusForwardPE;
    earningsResetAtConsensusPE = {
      direction: ours < consensus ? 'downgrade' : ours > consensus ? 'upgrade' : 'unchanged',
      price: resetPrice, priceReturn: resetPrice / price - 1,
      assumption: 'Replace consensus EPS with our EPS while retaining the consensus-based P/E',
    };
    consensusBridge = {
      earningsEffect: (ours - consensus) * consensusForwardPE,
      multipleEffect: ours * (targetPE - consensusForwardPE),
      totalPriceChange: targetPrice - price,
    };
  }
  const result = {
    price, currency: input.currency, basis: { ...input.ourForecast.basis },
    ourEPS: ours, consensusEPS: input.consensusForecast?.eps ?? null,
    ownForwardPE, consensusForwardPE, targetPE, targetPrice, priceReturn: targetPrice / price - 1,
    unchangedOwnPEPrice: ownForwardPE * ours,
    ownForecastBridge: { earningsEffect: 0, multipleEffect: targetPrice - price, totalPriceChange: targetPrice - price },
    earningsResetAtConsensusPE, consensusBridge,
  };
  function finiteNumbers(value) {
    if (typeof value === 'number' && !Number.isFinite(value)) throw new Error('Calculation overflow');
    if (value && typeof value === 'object') for (const child of Object.values(value)) finiteNumbers(child);
  }
  finiteNumbers(result);
  return result;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    if (process.argv.length !== 3) throw new Error('Usage: node compare_forward_pe.mjs input.json');
    const input = JSON.parse((await readFile(process.argv[2], 'utf8')).replace(/^\uFEFF/, ''));
    console.log(JSON.stringify(compareForwardPE(input), null, 2));
  } catch (error) {
    console.error(error.message); process.exitCode = 1;
  }
}
