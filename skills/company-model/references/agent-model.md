# Model as an executable investment research tool

The model calculates and evaluates business outcomes over time. Stable economic definitions and executable relationships support machine queries. The workbook and agent interface are equally required and mechanically synchronized under the [workbook contract](workbook-profile.md).

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

The machine model is the cell specification that [model_workbook.py](../scripts/model_workbook.py) builds the workbook from, with its saved outputs file and check report ([model standard](model-standard.md)). Its `outputs` map gives each decision metric a stable semantic ID, such as `eps.FY2027`, that survives an Excel row insertion. Calculated results come from the builder and the recalculated workbook; do not ask a language model to supply calculated answers from memory. For an inherited workbook, a structured index can point to the workbook and a compatible recalculation engine; it need not duplicate every formula in JSON. Analysis-only queries can reuse an existing valid workbook; a newly delivered or revised forecast must also satisfy the human workbook requirement.

## Change propagation and valuation

New filing or operating observation -> reconcile its basis -> identify affected drivers -> revise an evidence-supported assumption or fork a scenario -> recompute revenue/costs -> IS/CF/BS and funding -> audit -> refresh affected valuations -> validate the thesis -> reconsider the conclusion.

Downstream valuations record the model ID/version/fingerprint, scenario, selected metric/period IDs, and their own current price/rate/market inputs. A changed model marks dependent values and conclusions stale; a changed share price can require a valuation refresh without rebuilding the unchanged business forecast. Do not present the old target as current while refresh is pending.

For cash-flow valuation, consume the relevant computed cash-flow bridge. Do not substitute net income for FCFE or FCFF because the data interface is easier. A P/E valuation can consume model EPS directly but still requires cash/financing validation of the business forecast.

## Evaluation after results

Save the forecast before the outcome is available, including its data cutoff, scenario and assumptions. When actuals arrive, first match segment definitions, fiscal period, currency, perimeter, adjusted/reported basis and share treatment. Keep restated-history comparisons separate from what was knowable at the original decision time.

Measure forecast error and its contribution to the valuation error. Separate changes in volume, price/mix, margins, costs, capital spending, working capital, tax, shares, and market valuation assumptions. Flag unsupported components rather than inventing attribution that merely adds up. Revise assumptions or model structure when evidence warrants it; a target miss alone does not prove a specific causal explanation.

This history is for calibration and learning. Do not rewrite the original forecast, optimise on the evaluation window and call it independent validation, or treat one successful forecast as established predictive performance.
