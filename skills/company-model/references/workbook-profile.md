# Workbook import, preservation and delivery

Use this reference for company forecast builds and numerical revisions, workbook imports and updates, or using Excel as the calculation backend. The [agent-model contract](agent-model.md) defines the machine interface; the workbook supplies the user's required human review model. Existing workbook layout and explicit user instructions govern presentation.

## Human review delivery contract

Deliver a formula-driven `.xlsx` whenever building or numerically revising company forecasts. Keep code/JSON for automation when useful, but do not offer it as the sole model deliverable or merely paste its calculated outputs into Excel. An evidence-only review can link the unchanged, valid existing workbook. An explicit request for another format takes precedence.

Make forecast assumptions editable, visibly distinguish actuals/derived actuals/management claims/analyst estimates, and expose their sources and rationale. Build operating revenue/costs and integrated earnings, balance sheet and cash flow with inspectable formulas and schedules for material investment, financing, shares and distributions. Link the chosen valuation to calculated forecast outputs. Use supported reporting cadence rather than inventing quarterly disclosures.

For revisions, preserve the original workbook/vintage and user edits. Show material old/new assumptions and earnings, cash, funding and valuation effects. Label frozen comparisons as snapshots; changing an active assumption must recompute the live model. Never maintain two unreconciled authoritative models.

Recalculate, scan errors/cycles, inspect formula caches, reconcile material outputs to the versioned agent run, and test representative assumption/case changes and missing-input behavior. Render each new sheet or affected area and inspect readability. Record the engine and any native Excel behavior that was not verified. Include sources, numerical checks and material limitations where the user can find them. A calculation-on-open setting, successful export or zero balance residual alone is insufficient.

## Portable build and mechanical sync

Generate the machine interface and Excel from the same specification or mechanically compare **every named input and output** against the recalculated workbook. Fail on any difference; do not silently choose one representation. Model, source and run versions remain part of the research package.

For a company model, write one cell specification and use [model_workbook.py](../scripts/model_workbook.py): `build` writes the styled multi-sheet workbook (named cells only for outputs and the case selector), `calculate` runs every case independently, and `check` compares every cell's formula, input and saved value with the specification after [recalc_excel.ps1](../scripts/recalc_excel.ps1) has recalculated the workbook in Excel. A workbook that has not been recalculated fails the check. A formula cannot reference an empty cell directly; roll periods up with `SUM(first:last)`, which skips blanks. If the human model is edited, deliberately reconcile those edits into a new machine-model version, then rebuild and check the pair. Do not overwrite user edits to make the check pass.

The scripts need openpyxl. Install [requirements.txt](../requirements.txt) into the interpreter actually used (or a virtual environment); a user-site install is not visible under `python -I`.

For an existing workbook the builder did not write, use an actual compatible engine and equivalent complete named bindings; a manual spot-check or calculation-on-open setting does not establish sync.

## Inspect and preserve

Identify the working model and create a baseline fingerprint and backup. Inventory sheets, formulas, names, charts/images, external links, macros, controls and unsupported extensions. Check for concurrent edits before writing; a file lock alone does not establish that a file is safe to modify.

Choose a writer that supports the workbook's actual features. A file-writing library may preserve formulas without calculating them and may omit unsupported parts. Use an available compatible calculation engine when recalculation is required. Do not execute macros or refresh external sources merely to inspect a workbook.

Map accounts, periods and dependencies by meaning rather than fixed coordinates or sheet names. Review supplied automation for hard-coded inputs and effects before reuse. Preserve existing user edits and notes; compare the current fingerprint with the baseline before applying changes.

## Make the view readable

- Keep each related operating calculation chain together on one worksheet, with relevant history, active assumptions, their basis, intermediate calculations and component totals in a readable local sequence. Put an assumption beside or immediately above/below the figures it drives. A control panel can select cases while leaving the active local inputs visible. Link completed results into other schedules; raw source archives and distinct builds may remain separate. See [foundational builds](foundational-builds.md) for the method and clean example.
- Keep existing valid sheet names and reporting structure. Add components only when needed.
- Label periods, currencies, scales, accounting basis and the actual/forecast boundary.
- Distinguish reported data, derived data, formulas and editable assumptions through explicit classifications and a documented visual legend.
- Give every assumption and hardcoded figure a short visible source tag beside its units ("AR25", "3Q26 call", "Est."). Keep decision-driving assumptions, qualifications and their concise rationale visible beside the calculation; a wrapped explanation cell can use [linked text](linked-explanations.md) for live figures. Longer source detail may sit in a row-label comment, but do not hide the logic needed to check the forecast there. Cite sources a reader can follow, never pipeline file paths. Preserve useful existing annotations during narrow updates.
- Preserve readable existing fonts and styles. For a new view, use restrained formatting, consistent numeric formats and clear section hierarchy.
- Use historical valuation charts only with suitable dated inputs. Identify realised earnings separately from historical forecast vintages and handle nonpositive denominators explicitly.

Treat any template as an unvalidated starting point. Review periods, labels, currencies, formulas, inputs and external dependencies. Resolve material errors rather than hiding them with zero-value fallbacks.

## House theme and reporting detail

Use this theme for new models and authorised restyling. Preserve a valid existing user layout during a narrow numerical update unless asked to restyle it.

| Element | Convention |
| --- | --- |
| Worksheet gridlines | Off; zoom 85% on calculation sheets, 100% on output sheets |
| Tabs | Outputs navy `#1B2A41`, calculations grey `#BFC7D0`, inputs and data light blue `#BDD7EE`; title-case names without abbreviations |
| Navigation | Hyperlinked sheet index on the Cover; "Back to Cover" at the top right of every other sheet |
| Font | Arial: body 9pt, headers 10pt bold, sheet title 12pt bold navy |
| Hardcoded historicals | Blue `#0000FF` |
| Forecast assumptions, estimated splits and scenario levers | Blue on light yellow `#FFF2CC` |
| Formulas | Black |
| Formulas that link to another sheet | Green `#008000` |
| Memo ratios (growth, margins, shares of revenue) | Dark grey `#595959` italic |
| Key outputs (rating, target, EPS, price return) | Bold black 10pt, never grey or italic; they take precedence over the input, link and ratio styles |
| Section headers | Bold uppercase navy on `#E7EBF0` across the used width |
| Totals and subtotals | Bold with a thin top rule on the number cells |
| Forecast columns | Header cells `#F2F2F2` and a medium rule down the left of the first forecast column; row 4 the basis (8pt grey), row 5 the period (bold, centred) |
| Columns | Spacer 2; labels 46 (40 on output sheets, widened up to 60 rather than clipped); units 8, centred; source tag 11, 8pt grey, indented; periods 11; a spacer of 2 between annual and quarterly blocks |
| Rows | Data rows 15 high, no wrap; text-heavy tables wrap, top-aligned, with rows sized to fit; sub-items indented with the cell indent |
| Grouping | Quarterly columns; each schedule's detail rows, leaving its header and total visible; chart-only helper data grouped and greyed; `#N/A` chart gaps never visible |
| Notes | Visible source tag and pivotal rationale beside the calculation; longer source detail may use row-label comments |
| Charts | Palette navy `#1B2A41`, teal `#1F6F78`, slate `#6E7F96`, light teal `#8DBCC1`, greys `#9AA3AE`, `#B9C1CB`; takeaway title 11pt bold; legend at the bottom; light grey horizontal gridlines only; no border; forecasts hatched (bars) or dashed (lines); clipped data noted on the chart; anchored inside the print area, aligned to column edges, off every table |
| Print | A4 landscape, one page wide, centred, 0.5-inch margins; title rows (rows 1-5 and columns A-D on time-series sheets, rows 1-3 elsewhere) repeated; print area includes every chart and excludes helper data; breaks between sections; footer with file, sheet, page N of M and date |

Number formats, one per unit: reporting currency in millions `#,##0.0;(#,##0.0);"–"`; per share `0.00;(0.00);"–"`; % `0.0%;(0.0%);"–"` (`0.00%` for ratios under 1%); change in points `0.0" pt"`; multiples `0.0"x"`; days `0`; FX `0.0000`; counts `#,##0`; dates `d mmm yyyy` as real dates. Negatives always in parentheses; the writer adds the parenthesised section to any format that lacks one. Use one currency label throughout. The writer formats a row from its column C unit only for the labels in `UNIT_FORMATS`; a per-share row gets two decimals only under `RMB`, `US$`, `HKD` or `per share`, so use `per share` or set `format` for other currencies. A formula can encode a forecast judgement, such as an assumed improvement; give the judgement its own input cell rather than writing it into the formula. Defined names exist only for the specification's outputs and the case selector; the specification itself is the map of every cell.

Use quarterly operating forecasts where reliable quarterly history and matching drivers are available. Use half-years when quarterly evidence is thin or only interim disclosure supports the build. Annual-only presentation is appropriate when finer detail cannot be supported. Choose cadence by schedule: quarterly earnings data do not imply quarterly balance-sheet or cash-flow disclosures. Keep matching actual/forecast periods aligned, derive quarters only from compatible cumulative flows, and reconcile period totals. Add annual roll-ups where useful, using flow sums, closing balances and recomputed/weighted ratios as appropriate.

## Verify the result

Recalculate with a compatible engine and inspect formulas and outputs, including statement identities, intended links, circular references and error cells. A calculation-on-open flag or unchanged cached values do not prove recalculation occurred.

Compare changed cells/sheets and preservation-sensitive package parts with the baseline. Record unsupported or unverified features. For material presentation changes, export each sheet to PDF from Excel and look at every page: page count against the one-page targets, clipped or cut-off text, visible `#N/A`, charts outside the print area or over a table, legend overlap, wrapped titles and minus-sign negatives. The PDF is only for inspection; the deliverable stays the workbook. A formatting pass must leave every computed value unchanged.

Retire or replace sheets only within the requested scope after checking references. Deliver the output path, backup/version, calculation status and any unresolved verification gaps.
