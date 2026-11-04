// Compatibility entry point. The portable Python writer owns all XLSX logic.
// node build_forecast_workbook.mjs PLAN_OR_COMPILED.json OUTPUT.xlsx
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
const [input, output, ...extra] = process.argv.slice(2);
if (!input || !output || extra.length) {
  console.error('Usage: node build_forecast_workbook.mjs PLAN_OR_COMPILED.json OUTPUT.xlsx');
  process.exitCode = 2;
} else {
  const script = fileURLToPath(new URL('./forecast_workbook.py', import.meta.url));
  const run = spawnSync(process.env.PYTHON ?? 'python', ['-B', script, 'build', input, output], { stdio: 'inherit' });
  if (run.error) console.error(run.error.message);
  process.exitCode = run.status ?? 1;
}
