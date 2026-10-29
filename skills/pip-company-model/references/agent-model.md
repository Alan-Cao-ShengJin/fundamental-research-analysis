# Model as an executable investment research tool

The model calculates and evaluates business outcomes over time. Its primary consumers are research, valuation and review agents. Human-readable workbooks and reports are optional views or calculation backends; stable economic definitions and executable relationships identify the model.

## What the agent must be able to do

| Operation | Required behaviour |
| --- | --- |
| Query | Retrieve a named metric, period, scenario and calculation run, including units, status, lineage and relevant uncertainty |
| Explain | Trace a valuation change through cash/earnings, costs and operating assumptions to evidence; return only the relevant subgraph |
| Run a scenario | Override supported forecast assumptions, recompute downstream outputs and checks, compare with the frozen base |
| Refresh evidence | Add a dated observation, reconcile the reporting basis and create a new model version rather than overwriting history |
| Evaluate | Supply versioned EPS, book value, FCFE/FCFF and financing outputs to suitable valuation methods; do not retype them into an independent report |
| Review | Compare frozen forecasts with later actuals on a matched basis; attribute misses to drivers, accounting/perimeter, data, assumptions and model structure |
| Prioritise research | Use materiality/sensitivity and unresolved evidence to select the next useful investigation |

An answer such as “revenue increased” is insufficient when the agent needs to decide whether the change affects value. A model that cannot propagate an assumption change into earnings, cash and valuation is not complete for this purpose.

## Persistent model state

Keep a machine-readable model package with:

- **Identity and versions:** entity, model ID/version, information cutoff, fiscal period map, accounting scope and engine/formula version; each scenario/run has its own identity.
- **Evidence:** raw observations and precise source locators, availability dates, reporting currency/scale and reported/derived/guidance status. Restatements create a new vintage.
- **Definitions:** stable semantic IDs for metrics, segments, periods and units. A reference such as `fcfe.FY2028.base` must survive an Excel row insertion.
- **Business drivers and assumptions:** values/ranges, rationale, sensitivity, uncertainty and what evidence would change them. Missing values remain missing.
- **Executable relationships:** revenue/cost/unit-economics build, linked statements and schedules, dependencies and checks. Use reviewed formulas/functions with a deterministic engine; do not ask a language model to supply calculated answers from memory.
- **Calculated results:** numeric outputs with model fingerprint, scenario overrides, run ID and check status. A saved cached value without a calculation record is not a current result.
- **Evaluation history:** downstream valuation and decision versions, catalyst/watch definitions, frozen forecasts and eventual matched actual outcomes.

A structured index can point to an existing Excel workbook and compatible recalculation engine. It need not duplicate every formula in JSON. A later executable graph can use Python, JavaScript or another suitable backend. Choose the backend that actually recalculates and preserves the required economics; spreadsheet appearance is not a readiness gate for an analysis-only run.

## Change propagation and valuation

New filing or operating observation -> reconcile its basis -> identify affected drivers -> revise an evidence-supported assumption or fork a scenario -> recompute revenue/costs -> IS/CF/BS and funding -> audit -> refresh affected valuations -> validate the thesis -> reconsider the conclusion.

Downstream valuations record the model ID/version/fingerprint, scenario, selected metric/period IDs, and their own current price/rate/market inputs. A changed model marks dependent values and conclusions stale; a changed share price can require a valuation refresh without rebuilding the unchanged business forecast. Do not present the old target as current while refresh is pending.

For cash-flow valuation, consume the relevant computed cash-flow bridge. Do not substitute net income for FCFE or FCFF because the data interface is easier. A P/E valuation can consume model EPS directly but still requires cash/financing validation of the business forecast.

## Evaluation after results

Save the forecast before the outcome is available, including its data cutoff, scenario and assumptions. When actuals arrive, first match segment definitions, fiscal period, currency, perimeter, adjusted/reported basis and share treatment. Keep restated-history comparisons separate from what was knowable at the original decision time.

Measure forecast error and its contribution to the valuation error. Separate changes in volume, price/mix, margins, costs, capital spending, working capital, tax, shares, and market valuation assumptions. Flag unsupported components rather than inventing attribution that merely adds up. Revise assumptions or model structure when evidence warrants it; a target miss alone does not prove a specific causal explanation.

This history is for calibration and learning. Do not rewrite the original forecast, optimise on the evaluation window and call it independent validation, or treat one successful forecast as established predictive performance.

## Optional calculation helper

The [company-model helper](../../lib/company-model.mjs) supplies a small deterministic JSON graph implementation with explicit units/scales, source cutoff checks, dependency calculation, scenario overrides, lineage, reconciliation checks and model fingerprints. The [runner](../scripts/run_agent_model.mjs) can evaluate a package or compare a scenario:

```powershell
node skills/pip-company-model/scripts/run_agent_model.mjs skills/pip-company-model/references/agent-model-example.json
node skills/pip-company-model/scripts/run_agent_model.mjs skills/pip-company-model/references/agent-model-example.json skills/pip-company-model/references/agent-model-scenario.json
```

The [example](agent-model-example.json) and [scenario](agent-model-scenario.json) are synthetic. A price driver change from 10 to 9 propagates revenue from 1,000 to 900, net income from 285 to 210, FCFE from 255 to 180 and an illustrative P/E value from 57 to 42 per share, while the simplified balance sheet reconciles in both runs. The valuation output is formula-linked to EPS rather than retyped.

The helper evaluates a supplied graph; it does not import workbooks, retrieve evidence, persist runs or activate autonomous updates. Its `calculated` status means arithmetic ran, not that the model is financially complete or decision-ready. Supply issuer-specific statements, schedules, assumptions and appropriate valuation methods separately.

## Communication

Default user output is the decision, what changed, why it matters, material uncertainty and what the agent will review next. Keep the full model, evidence and explanations available for inspection. Human reading time is not a dependency for routine authorised model maintenance; external actions still follow the actual mandate and execution controls.
