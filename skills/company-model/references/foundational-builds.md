# Build a forecast a human can examine

Use this method when designing an operating forecast or revising its structure.
Preserve the user's valid workbook conventions during narrow updates. The purpose
is to make the reasons for the forecast and the confidence it warrants inspectable.

## Decompose the research problem

Start with the material financial item and ask which distinct activities and
economic mechanisms make it up. Continue until the remaining inputs are the
smallest useful pieces that can reasonably be forecast for this assignment.
These are foundational estimates. They can be quantities, rates, timing,
conversion factors or a directly estimated contribution. They are not necessarily
physical units, disclosed line items or permanently irreducible quantities.

Seek the information that makes a better decomposition possible. Financial
statements may provide totals while earnings-call Q&A supplies the useful split.
Operating trackers, third-party series and suitable comparisons can provide
additional observations. Match definitions, perimeter, units, recognition and
periods. An unofficial management breakdown retains its attribution and
qualification; it does not become a reported actual through insertion in Excel.
Several notes of the same meeting are one evidence origin.

For a material input, keep the observed history, current estimate, source and
availability date, reasoning, uncertainty and next useful evidence. Make the
important explanation visible beside the input; keep longer originals in source
archives. Distinguish observed data, derived actuals, management claims,
third-party estimates and the analyst's judgement. A residual fitted to a total
is conditional on the other assumptions used to derive it.

Investigate important gaps before settling for a broad growth or margin input.
Use a labelled estimate when evidence remains incomplete. The quality of a finer
forecast depends on the support for its components and their combined behaviour.
Do not fabricate detail or treat several correlated guesses as independent
corroboration. Explain what would change the weak foundational estimates.

## Design the local calculation chain

Keep related work together on one worksheet. A useful block presents:

1. Relevant historical observations beside forecast periods, with clear units.
2. The foundational assumptions and the basis for choosing them.
3. Intermediate calculations that explain the economic mechanism.
4. Component forecasts and their subtotal.

This is a logical reading sequence. A result can sit above its supporting detail
when the relationship remains clear; no fixed tab name or universal row order is
required.

Place an editable assumption beside or immediately above/below the numbers it
drives. Keep a visible source beside the calculation. A small operating scaffold
can show its full explanation in an ordinary cell to the right; the full company
workbook uses the compact source tags and row-label comments in the
[workbook profile](workbook-profile.md#house-theme-and-reporting-detail).
Changing an assumption should leave its active value and consequences in view,
with the supporting reasoning easy to retrieve.
Forecast inputs can live in their owning operating block. A shared case selector
or control panel can select them without hiding the active local assumptions.
Do not create separate assumptions and calculation tabs for a small local chain.

Calculate each component once, aggregate the pieces into the larger forecast,
and link completed results onward into statements and other schedules. Raw data
archives, distinct operating builds and full financial schedules can have their
own worksheets. Cross-sheet reuse is useful; forcing a reviewer to switch tabs
repeatedly to understand one local calculation is avoidable.

Choose one independent lever for each causal step. A price derived from an
assumed revenue total is an implication, rather than independent price evidence.
If both unit cost and margin are estimated, reconcile them and identify which
drives the active forecast. Trace investment, timing, financing and ownership
consequences where applicable. A coherent scenario changes related quantities
on a defensible business story; an input sensitivity measures exposure only.

## Review the conviction the model warrants

Apply the [workbook profile](workbook-profile.md#house-theme-and-reporting-detail) for the house theme, local assumption explanations and supported reporting cadence.

Ask another analyst to identify the main assumptions, explain their bases, change
an important one and describe the resulting component and aggregate changes.
Inspect the worksheet at normal zoom and verify that the local chain and its
notes are readable. A numerical dependency map cannot establish that usability.

Check that the build can explain the important historical changes and the
forecast transition. Reconcile totals independently, examine implied operating
requirements and test representative input changes through the full model.
Investigate consequential weak inputs using their sensitivity and uncertainty.
Do not average source-quality labels into a forecast-confidence score.

Keep separate conclusions about arithmetic, economic plausibility, source
support, human usability and subsequent forecast calibration. Passing one does
not establish the others. Compare frozen forecasts with matched actuals and
attribute misses to changed evidence, assumptions and model structure.

## Generic tools and clean assets

The following resources use neutral labels and invented numbers. They contain
no issuer data or sector assumptions.

- [Sample company model](../assets/company-model-example.xlsx), built from
  [its specification](../assets/company-model-example.json) by
  [model_example.py](../scripts/model_example.py): the full multi-sheet model
  the [model standard](model-standard.md) requires, with invented figures. Start
  every company model from this structure.
- [Blank build plan](../assets/forecast-blocks-template.json): edit the periods,
  block definitions, foundations, formulas and selected outputs for the task.
  Null inputs and blank evidence fields intentionally mark unfinished work.
- [Synthetic worked plan](../assets/forecast-blocks-example.json) and
  [editable Excel example](../assets/forecast-blocks-example.xlsx): demonstrate
  two local component builds aggregating to a total on the same worksheet.
  They are an operating-build example, not a completed issuer model or a claim
  that every business should use those equations.
- [Plan initializer](../scripts/init_forecast_plan.py): create a fresh scaffold
  without copying a prior company's workbook.
- [Compiler and reviewer](../scripts/forecast_blocks.py): check declared inputs,
  missing bases, dependencies, cycles, missing values and unused foundations;
  calculate the plan and compile local Excel formulas. Its findings direct
  analyst review, without certifying the evidence or economics.
- [Company model builder](../scripts/model_workbook.py) and [Excel recalculation](../scripts/recalc_excel.ps1): build the full multi-sheet model required by the [model standard](model-standard.md) from one cell specification, calculate every case independently, recalculate in Excel and check that the two agree.
- [Portable workbook writer and sync checker](../scripts/forecast_workbook.py), for a single-sheet annual operating scaffold only; it cannot hold a company model's statements: build formulas and named bindings from the same executable plan, recalculate its restricted arithmetic, and fail if any declared input/output, formula or saved value differs. See [portable build and sync](workbook-profile.md#portable-build-and-mechanical-sync).
- [Read-only cell tracer](../scripts/trace_model.py): trace selected cells in an
  existing workbook, including saved formula caches, local/cross-sheet precedents,
  nearby row labels and cell notes. It does not recalculate or infer whether a
  hardcoded leaf is a fact, an assumption, a technical constant or an override.

### Use the tools

From the repository root, choose new output paths to preserve existing work:

```powershell
python skills/company-model/scripts/model_workbook.py build output/model_spec.json output/model.xlsx --outputs output/outputs.json
powershell -NoProfile -ExecutionPolicy Bypass -File skills/company-model/scripts/recalc_excel.ps1 -Workbook output/model.xlsx -Selector "Cover!C9" -Cases 3 -Outputs "Statements!K50" -Report output/excel.json
python skills/company-model/scripts/model_workbook.py check output/model_spec.json output/model.xlsx --report output/model-sync.json
```

For a single-sheet scaffold:

```powershell
python skills/company-model/scripts/init_forecast_plan.py output/plan.json
python skills/company-model/scripts/forecast_blocks.py output/plan.json --output output/compiled.json
python skills/company-model/scripts/forecast_workbook.py build output/plan.json output/model.xlsx --compiled output/compiled.json
python skills/company-model/scripts/forecast_workbook.py check output/plan.json output/model.xlsx
```

The compiler uses the Python standard library; the portable writer/checker and tracer use the dependencies in [requirements.txt](../requirements.txt), without a proprietary runtime. The portable evaluator recalculates only the documented arithmetic grammar; it is not a general Excel engine. Existing complex workbooks require a compatible engine and the [preservation workflow](workbook-profile.md). No helper refreshes external data or runs macros.

For a numerical sensitivity, set a forecast foundation in a separate run:

```powershell
python skills/company-model/scripts/forecast_blocks.py output/plan.json --set input_id forecast_period 12 --output output/sensitivity.json
python skills/company-model/scripts/trace_model.py output/existing.xlsx --cell "Operating build!F15" --output output/trace.json
```

Expressions support named rows, `+`, `-`, `*`, `/`, parentheses, unary signs and
`lag(row_id)` for one prior period. They are parsed, never executed as Python.
Declare an independent input under `values` by period. Put its basis once in `basis.default` (source for actuals, rationale for forecasts), with optional `basis.periods` overrides; a distinct source or assumption merits a distinct basis, not boilerplate for every cell. A `formula` supplies
calculated periods; a historical value can anchor the first period of a
roll-forward. An explicit forecast value on a calculated row is reported as an
override needing explanation. Formulas can encode assumptions too; explain their
economic rule locally.

The helpers do not infer dimensions, fiscal calendars, recognition rules,
business completeness or source truth. They support a documented business design,
not automatic template fitting. Missing inputs stay unavailable; the workbook
adapter refuses to export an incomplete calculated build. The blank JSON plan
is intentionally not calculation-ready. For a full company forecast, add the
appropriate linked statements, funding, ownership and valuation schedules under
the existing skill requirements. The model may use another suitable backend.
