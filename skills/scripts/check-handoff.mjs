import { readFileSync } from 'node:fs';
import { validateHandoff } from '../lib/handoffs.mjs';

try {
  const args = process.argv.slice(2);
  if (args.length && (args.length !== 4 || args[0] !== '--fixture-clock' || args[2] !== '--fixture-reason')) {
    throw new Error('Expected --fixture-clock ISO_TIMESTAMP --fixture-reason REASON, or no clock override.');
  }
  const options = args.length ? { fixtureClock: { mode: 'synthetic-fixture', now: args[1], reason: args[3] } } : {};
  validateHandoff(JSON.parse(readFileSync(0, 'utf8')), options);
  process.stdout.write(JSON.stringify({ valid: true }));
} catch (error) {
  process.stderr.write(String(error.message));
  process.exitCode = 1;
}
