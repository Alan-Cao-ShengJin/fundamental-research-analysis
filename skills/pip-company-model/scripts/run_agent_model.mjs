import { readFile, writeFile } from 'node:fs/promises';
import { evaluateCompanyModel, compareModelScenario } from '../../lib/company-model.mjs';

const [path, scenarioPath, outputPath] = process.argv.slice(2);
if (!path) throw new Error('Usage: node run_agent_model.mjs model.json [scenario.json] [output.json]');
const model = JSON.parse(await readFile(path, 'utf8'));
const result = scenarioPath ? compareModelScenario(model, JSON.parse(await readFile(scenarioPath, 'utf8'))) : evaluateCompanyModel(model);
const text = JSON.stringify(result, null, 2) + '\n';
if (outputPath) await writeFile(outputPath, text); else process.stdout.write(text);
