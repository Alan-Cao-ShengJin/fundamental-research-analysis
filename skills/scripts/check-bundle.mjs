import { readFile, readdir, access } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { dirname, resolve, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { z } from 'zod';
import { HandoffSchema, validateHandoff } from '../lib/handoffs.mjs';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const catalog = JSON.parse(await readFile(resolve(root, 'catalog.json'), 'utf8'));
const errors = [], ids = new Set();
const within = (base, target) => { const rel = relative(base, target); return rel === '' || (!rel.startsWith('..' + sep) && rel !== '..' && !rel.includes(':')); };
async function files(directory) {
  const result = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = resolve(directory, entry.name);
    if (entry.isDirectory()) result.push(...await files(path)); else result.push(path);
  }
  return result;
}
for (const skill of catalog.skills) {
  if (skill.id.startsWith('pip-')) errors.push(`Legacy branded skill ID: ${skill.id}`);
  if (ids.has(skill.id)) errors.push(`Duplicate skill ${skill.id}`); ids.add(skill.id);
  const path = resolve(root, skill.path);
  if (!within(root, path)) { errors.push(`Skill path escapes the bundle: ${skill.id}`); continue; }
  const text = (await readFile(path, 'utf8')).replace(/\r\n/g, '\n');
  if (!text.startsWith('---\n') || !/^name: [a-z0-9-]+$/m.test(text) || !/^description: \S.+$/m.test(text)) errors.push(`Invalid entry metadata: ${skill.id}`);
  if (!text.includes(`\nname: ${skill.id}\n`) || dirname(path).split(sep).at(-1) !== skill.id) errors.push(`Entry identity mismatch: ${skill.id}`);
}
if (!ids.has(catalog.entrySkill)) errors.push('Unknown entry skill.');
for (const [mode, workflow] of Object.entries(catalog.companyWorkflows ?? {})) {
  if (!ids.has(workflow.entrySkill) || !catalog.flows[workflow.flow]) errors.push(`Invalid company workflow ${mode}`);
  else if (!catalog.flows[workflow.flow].some(name => catalog.stages[name]?.skill === workflow.entrySkill)) errors.push(`Company workflow ${mode} does not enter its designated skill`);
  for (const [submode, route] of Object.entries(workflow.modes ?? {})) {
    const flow = catalog.flows[route.flow];
    if (!flow || !flow.some(name => catalog.stages[name]?.skill === workflow.entrySkill)) errors.push(`Invalid company workflow mode ${mode}.${submode}`);
    if (route.learningStage && !flow?.includes(route.learningStage)) errors.push(`Missing learning stage in ${mode}.${submode}`);
    if (route.escalateTo && !workflow.modes[route.escalateTo]) errors.push(`Unknown escalation mode in ${mode}.${submode}`);
  }
  if (workflow.routingReference) {
    const path = resolve(root, workflow.routingReference);
    if (!within(root, path)) errors.push(`Routing reference escapes bundle: ${mode}`);
    else try { await access(path); } catch { errors.push(`Missing routing reference: ${mode}`); }
  }
}
for (const [name, stage] of Object.entries(catalog.stages)) {
  if (!ids.has(stage.skill)) errors.push(`Unknown skill for stage ${name}`);
  for (const dep of stage.requiredBefore) if (!catalog.stages[dep]) errors.push(`Unknown dependency ${dep}`);
}
for (const [name, flow] of Object.entries(catalog.flows)) {
  const seen = new Set();
  for (const id of flow) {
    const stage = catalog.stages[id];
    if (!stage || seen.has(id)) { errors.push(`Unknown or repeated stage ${id} in ${name}`); continue; }
    for (const dep of stage.requiredBefore) if (!seen.has(dep)) errors.push(`${name}: ${id} precedes required ${dep}`);
    seen.add(id);
  }
}
const activeRoots = catalog.skills.map(skill => dirname(resolve(root, skill.path)));
const coverage = JSON.parse(await readFile(resolve(root, 'research-cycle/assets/skill-coverage.json'), 'utf8'));
if (Object.keys(coverage.skills).length !== ids.size || [...ids].some(id => !coverage.skills[id])) errors.push('Coverage plan does not account for every skill exactly.');
for (const [mode, flow] of Object.entries(coverage.modes)) {
  if (!catalog.flows[flow]) errors.push(`Unknown coverage flow ${mode}`);
  for (const [id, rule] of Object.entries(coverage.skills)) {
    if (!ids.has(id) || !['required', 'conditional', 'outside-scope'].includes(rule.modes[mode]) || !rule.purpose) errors.push(`Invalid coverage rule ${mode}/${id}`);
    if (rule.modes[mode] === 'conditional' && !rule.trigger) errors.push(`Missing conditional trigger ${mode}/${id}`);
  }
}
let markdownLinks = 0, activeInstructionFiles = 0;
const markdownPaths = (await files(root)).filter(path => path.endsWith('.md'));
if (catalog.sourceArchivesBundled === false) {
  for (const entry of await readdir(dirname(root), { withFileTypes: true })) {
    if (entry.isFile() && entry.name.endsWith('.md')) markdownPaths.push(resolve(dirname(root), entry.name));
  }
}
for (const path of markdownPaths) {
  const text = await readFile(path, 'utf8');
  const activeInstruction = activeRoots.some(base => within(base, path));
  if (activeInstruction) {
    activeInstructionFiles++;
    if (/\p{Script=Han}/u.test(text)) errors.push(`Non-English instruction text: ${relative(root, path)}`);
  }
  for (const match of text.matchAll(/\[[^\]\n]+\]\(([^)\n]+)\)/g)) {
    const target = match[1].replace(/^<|>$/g, '').split('#')[0];
    if (!target || /^[a-z][a-z0-9+.-]*:/i.test(target)) continue;
    const dest = resolve(dirname(path), decodeURIComponent(target));
    // Maintainer docs may link the archive; active instructions stay in the reusable bundle.
    if (!within(dirname(root), dest)) { errors.push(`Link escapes repository: ${relative(root, path)}`); continue; }
    if (activeInstruction && !within(root, dest)) errors.push(`Active instruction links outside bundle: ${relative(root, path)} -> ${target}`);
    try { await access(dest); markdownLinks++; } catch { errors.push(`Broken link ${target} from ${relative(root, path)}`); }
  }
}
const actualSchema = JSON.parse(JSON.stringify(z.toJSONSchema(HandoffSchema)));
const documentedSchema = JSON.parse(await readFile(resolve(root, 'research-cycle/references/handoff.schema.json'), 'utf8'));
if (JSON.stringify(actualSchema) !== JSON.stringify(documentedSchema)) errors.push('Documented handoff schema differs from its implementation.');
validateHandoff(JSON.parse(await readFile(resolve(root, 'research-cycle/references/handoff-example.json'), 'utf8')));
// Standalone exports retain licenses and their own file manifest, not private archives.
const inventory = catalog.sourceArchivesBundled === false ? { files: [] }
  : JSON.parse(await readFile(resolve(root, 'source-inventory.json'), 'utf8'));
const originalSkills = inventory.files.filter(entry => entry.path.endsWith('/SKILL.md')).map(entry => entry.path.split('/').at(-2));
const mappedSkills = new Set(catalog.skills.flatMap(skill => skill.sourceSkills));
for (const name of originalSkills) if (!mappedSkills.has(name)) errors.push(`Original skill has no curated mapping: ${name}`);
for (const name of mappedSkills) if (!originalSkills.includes(name)) errors.push(`Unknown original skill in mapping: ${name}`);
let originalFilesVerified = 0, originalFilesUnavailable = 0;
for (const entry of inventory.files) {
  let bytes;
  try { bytes = await readFile(resolve(dirname(root), entry.path)); } catch { originalFilesUnavailable++; continue; }
  if (createHash('sha256').update(bytes).digest('hex') !== entry.sha256) errors.push(`Original source changed: ${entry.path}`);
  else originalFilesVerified++;
}
let additionalSourcesVerified = 0;
if (catalog.additionalSourceManifest) {
  const manifestPath = resolve(root, catalog.additionalSourceManifest);
  if (!within(root, manifestPath)) errors.push('Additional source manifest escapes bundle.');
  else {
    const additional = JSON.parse(await readFile(manifestPath, 'utf8'));
    const seenSources = new Set();
    const sourceRoot = resolve(dirname(root), additional.sourceRoot ?? 'Claude Skills/new-skills');
    if (!within(dirname(root), sourceRoot)) errors.push('Additional source root escapes repository.');
    for (const entry of additional.files) {
      const sourcePath = resolve(dirname(root), entry.path);
      if (!within(sourceRoot, sourcePath) || seenSources.has(sourcePath)) {
        errors.push(`Invalid or duplicate additional source: ${entry.path}`); continue;
      }
      seenSources.add(sourcePath);
      if (!entry.curatedSkills?.length || entry.curatedSkills.some(id => !ids.has(id))) {
        errors.push(`Missing or unknown curated mapping for ${entry.path}`);
      }
      try {
        const bytes = await readFile(sourcePath);
        if (bytes.length !== entry.bytes || createHash('sha256').update(bytes).digest('hex') !== entry.sha256) {
          errors.push(`Additional original source changed: ${entry.path}`);
        } else additionalSourcesVerified++;
      } catch { errors.push(`Additional original source unavailable: ${entry.path}`); }
    }
    for (const path of (await files(sourceRoot)).filter(path => /\.(md|py)$/.test(path))) {
      if (!seenSources.has(path)) errors.push(`New research source has no mapping: ${relative(dirname(root), path)}`);
    }
  }
}
if (errors.length) { console.error(JSON.stringify({ errors }, null, 2)); process.exitCode = 1; }
else console.log(JSON.stringify({ skills: ids.size, originalSkillsMapped: originalSkills.length, flows: Object.keys(catalog.flows).length, markdownLinks,
  handoffSchema: 'consistent', activeInstructionFiles, originalFilesVerified, originalFilesUnavailable, additionalSourcesVerified,
  note: 'Structural checks, not proof of analyst behaviour or investment performance.' }, null, 2));
