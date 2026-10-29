# Workbook import, preservation and delivery

Use this reference when importing or updating a workbook, using it as a calculation backend, or delivering a workbook view. The [agent-model contract](agent-model.md) defines the computational interface; existing workbook layout and explicit user instructions govern the view.

## Inspect and preserve

Identify the working model and create a baseline fingerprint and backup. Inventory sheets, formulas, names, charts/images, external links, macros, controls and unsupported extensions. Check for concurrent edits before writing; a file lock alone does not establish that a file is safe to modify.

Choose a writer that supports the workbook's actual features. A file-writing library may preserve formulas without calculating them and may omit unsupported parts. Use an available compatible calculation engine when recalculation is required. Do not execute macros or refresh external sources merely to inspect a workbook.

Map accounts, periods and dependencies by meaning rather than fixed coordinates or sheet names. Review supplied automation for hard-coded inputs and effects before reuse. Preserve existing user edits and notes; compare the current fingerprint with the baseline before applying changes.

## Make the view readable

- Keep existing valid sheet names and reporting structure. Add components only when needed.
- Label periods, currencies, scales, accounting basis and the actual/forecast boundary.
- Distinguish reported data, derived data, formulas and editable assumptions through explicit classifications and a documented visual legend.
- Keep material assumption sources and rationales accessible in a visible notes field, linked register or source comment.
- Preserve readable existing fonts and styles. For a new view, use restrained formatting, consistent numeric formats and clear section hierarchy.
- Use historical valuation charts only with suitable dated inputs. Identify realised earnings separately from historical forecast vintages and handle nonpositive denominators explicitly.

Treat any template as an unvalidated starting point. Review periods, labels, currencies, formulas, inputs and external dependencies. Resolve material errors rather than hiding them with zero-value fallbacks.

## Verify the result

Recalculate with a compatible engine and inspect formulas and outputs, including statement identities, intended links, circular references and error cells. A calculation-on-open flag or unchanged cached values do not prove recalculation occurred.

Compare changed cells/sheets and preservation-sensitive package parts with the baseline. Record unsupported or unverified features. For material presentation changes, render the relevant areas and inspect readability with an available tool.

Retire or replace sheets only within the requested scope after checking references. Deliver the output path, backup/version, calculation status and any unresolved verification gaps.
