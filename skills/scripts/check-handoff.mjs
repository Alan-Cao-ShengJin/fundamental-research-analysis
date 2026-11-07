import { readFileSync } from 'node:fs';
import { validateHandoff } from '../lib/handoffs.mjs';

try {
  validateHandoff(JSON.parse(readFileSync(0, 'utf8')));
  process.stdout.write(JSON.stringify({ valid: true }));
} catch (error) {
  process.stderr.write(String(error.message));
  process.exitCode = 1;
}
