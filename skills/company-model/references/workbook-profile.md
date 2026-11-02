# Workbook import, preservation and delivery

Use this reference for company forecast builds and numerical revisions, workbook imports and updates, or using Excel as the calculation backend. The [agent-model contract](agent-model.md) defines the machine interface; the workbook supplies the user's required human review model. Existing workbook layout and explicit user instructions govern presentation.

## Human review delivery contract

The user's workspace preference requires a formula-driven `.xlsx` whenever building or numerically revising company forecasts. Keep code/JSON for automation when useful, but do not offer it as the sole model deliverable or merely paste its calculated outputs into Excel. An evidence-only review can link the unchanged, valid existing workbook. A later explicit user format choice takes precedence.

Make forecast assumptions editable, visibly distinguish actuals/derived actuals/management claims/analyst estimates, and expose their sources and rationale. Build operating revenue/costs and integrated earnings, balance sheet and cash flow with inspectable formulas and schedules for material investment, financing, shares and distributions. Link the chosen valuation to calculated forecast outputs. Use supported reporting cadence rather than inventing quarterly disclosures.

For revisions, preserve the original workbook/vintage and user edits. Show material old/new assumptions and earnings, cash, funding and valuation effects. Label frozen comparisons as snapshots; changing an active assumption must recompute the live model. Never maintain two unreconciled authoritative models.

Recalculate, scan errors/cycles, inspect formula caches, reconcile material outputs to the versioned agent run, and test representative assumption/case changes and missing-input behavior. Render each new sheet or affected area and inspect readability. Record the engine and any native Excel behavior that was not verified. Include sources, numerical checks and material limitations where the user can find them. A calculation-on-open setting, successful export or zero balance residual alone is insufficient.

## Inspect and preserve

Identify the working model and create a baseline fingerprint and backup. Inventory sheets, formulas, names, charts/images, external links, macros, controls and unsupported extensions. Check for concurrent edits before writing; a file lock alone does not establish that a file is safe to modify.

Choose a writer that supports the workbook's actual features. A file-writing library may preserve formulas without calculating them and may omit unsupported parts. Use an available compatible calculation engine when recalculation is required. Do not execute macros or refresh external sources merely to inspect a workbook.

Map accounts, periods and dependencies by meaning rather than fixed coordinates or sheet names. Review supplied automation for hard-coded inputs and effects before reuse. Preserve existing user edits and notes; compare the current fingerprint with the baseline before applying changes.

## Make the view readable

- Keep each related operating calculation chain together on one worksheet, with relevant history, active assumptions, their basis, intermediate calculations and component totals in a readable local sequence. Put an assumption beside or immediately above/below the figures it drives. A control panel can select cases while leaving the active local inputs visible. Link completed results into other schedules; raw source archives and distinct builds may remain separate. See [foundational builds](foundational-builds.md) for the method and clean example.
- Keep existing valid sheet names and reporting structure. Add components only when needed.
- Label periods, currencies, scales, accounting basis and the actual/forecast boundary.
- Distinguish reported data, derived data, formulas and editable assumptions through explicit classifications and a documented visual legend.
- Write each forecast/assumption explanation and source in a long, visible ordinary cell to the right of the corresponding model row. Include the relevant source date and qualification where needed. Cell comments or Excel Notes do not substitute for that visible explanation. Preserve useful existing annotations during narrow updates.
- Preserve readable existing fonts and styles. For a new view, use restrained formatting, consistent numeric formats and clear section hierarchy.
- Use historical valuation charts only with suitable dated inputs. Identify realised earnings separately from historical forecast vintages and handle nonpositive denominators explicitly.

Treat any template as an unvalidated starting point. Review periods, labels, currencies, formulas, inputs and external dependencies. Resolve material errors rather than hiding them with zero-value fallbacks.

## House theme and reporting detail

Use the clean [model theme](../assets/model-theme.json) for new models and authorised restyling. Preserve a valid existing user layout during a narrow numerical update unless asked to restyle it.

| Element | Convention |
| --- | --- |
| Worksheet gridlines | Off |
| Calculations, including calculated forecast outputs | Black |
| Actual hardcoded data | Dark blue |
| Forecast inputs and explicitly identified forecast judgements | Purple with a pale nude fill |
| Percentages | Italic labels and figures; actual and calculated percentages are light grey, while forecast percentage inputs/judgements retain purple with nude fill |
| Local sums, section subtotals and overall totals | Bold, with a thin separating rule |
| Tables and operating blocks | Consistent thin borders defining sections; restrained header fills |
| Cells | Compact row heights and column widths, enough precision and space for readable figures |
| Alignment | Right-align the model table and figures; left-align explanatory prose in the long cells to its right |

The default palette is black `#000000`, dark blue `#17365D`, purple `#7030A0`, nude `#F2DDD5`, and light grey `#A6A6A6` for actual/calculated percentages. The percentage rule takes precedence over the ordinary actual/calculation colour: percentages are italic, with forecast inputs/judgements retaining purple and nude fill. A formula can encode a forecast judgement, such as an assumed improvement or an unchanged margin. Identify that role explicitly; formula syntax or colour alone does not establish its meaning. Ordinary non-percentage calculated results remain black. Bold component subtotals as well as final output totals, including percentage totals.

Use quarterly operating forecasts where reliable quarterly history and matching drivers are available. Use half-years when quarterly evidence is thin or only interim disclosure supports the build. Annual-only presentation is appropriate when finer detail cannot be supported. Choose cadence by schedule: quarterly earnings data do not imply quarterly balance-sheet or cash-flow disclosures. Keep matching actual/forecast periods aligned, derive quarters only from compatible cumulative flows, and reconcile period totals. Add annual roll-ups where useful, using flow sums, closing balances and recomputed/weighted ratios as appropriate.

## Verify the result

Recalculate with a compatible engine and inspect formulas and outputs, including statement identities, intended links, circular references and error cells. A calculation-on-open flag or unchanged cached values do not prove recalculation occurred.

Compare changed cells/sheets and preservation-sensitive package parts with the baseline. Record unsupported or unverified features. For material presentation changes, render the relevant areas and inspect readability with an available tool.

Retire or replace sheets only within the requested scope after checking references. Deliver the output path, backup/version, calculation status and any unresolved verification gaps.
