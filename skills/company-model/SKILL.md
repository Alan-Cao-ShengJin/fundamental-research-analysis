---
name: company-model
description: Build and maintain executable company financial models with operating drivers and linked income statements, cash flows and balance sheets. Use for new issuer models, historical updates, forecast revisions, scenarios and forecast evaluation; preserve existing workbook models when requested.
metadata:
  version: 2.2.0
---

# Company model building and updates

Build an executable economic model from the [evidence pack](../evidence-intake/SKILL.md), with linked operating drivers and statements. Every new model meets the [model standard](references/model-standard.md): quarterly and annual three statements with schedules, a segment-to-unit revenue projection, operating data, guidance, questions, thesis and valuation-band tabs. The [sample model](assets/company-model-example.xlsx) shows that depth in full; start from its structure, not from any other workbook. Build it with [model_workbook.py](scripts/model_workbook.py) and recalculate it in Excel. Comprehensiveness is the point: an AI can build in hours the detail that takes an analyst days. The Excel workbook and the agent interface are both required and mechanically synchronised under the [workbook contract](references/workbook-profile.md). A report or total-only EPS forecast does not replace the operating build.

The model is a human-readable argument for the conviction its forecasts warrant. Break material items into their smallest useful forecastable components, substantiate the foundational estimates and aggregate upward. Keep each related calculation chain on one worksheet, with assumptions and their basis beside the figures they drive. Read [foundational builds](references/foundational-builds.md) for the method, the tools and the synthetic example; adapt the business design rather than copying an old issuer workbook.

[Stock initiation](../stock-initiation/SKILL.md) orchestrates a new case; [model revision](../model-revision/SKILL.md) selects the affected work for existing coverage. This specialist supplies the calculations for both; a revision does not rebuild unaffected stages.

## Sequence

| Stage | Work and output | Read |
| --- | --- | --- |
| 1 | Map the business into forecastable components; establish versioned model state, periods, units, dependencies and a calculation backend; inspect any existing workbook | [Model standard](references/model-standard.md), [model setup](references/model-setup.md), [agent model](references/agent-model.md) |
| 2 | Populate and reconcile historical income statements, balance sheets and cash flows at the supported cadence | [Actuals](references/actuals.md) |
| 3 | Gather component history from filings, calls and external series; reconcile definitions and identify estimated splits | [Drivers and guidance](references/drivers-guidance.md) |
| 4 | Extract dated management guidance and unresolved statements | [Drivers and guidance](references/drivers-guidance.md) |
| 5 | Forecast the foundational pieces into component and segment revenue | [Revenue projection](references/revenue-projection.md) |
| 6 | Build matched costs, unit economics, segment gross profit and the investment needed to deliver the revenue | [Revenue projection](references/revenue-projection.md) |
| 7 | Link into forecast earnings; build operating-expense, tax, share, working-capital, asset, lease, debt and cash schedules | [Statement forecast](references/statement-forecast.md) |
| 8 | Execute and audit the model, implied remaining periods, cash requirements and estimate gaps; retain run/version/checks and sensitivities | [Forecast audit](references/forecast-audit.md) |

Then hand the audited forecast to valuation under the [company sequence](../research-cycle/references/company-sequence.md).

Modes:

- **New model:** complete the sequence. Choose the structure from the business economics, reporting cadence and evidence. Use the [sector references](references/sectors/index.md) for the relevant mechanisms, loading only the cards that apply; a card's example is not a company forecast.
- **Historical update:** follow [actuals](references/actuals.md) and produce a reconciled baseline before forecasting.
- **Operating-driver update:** follow [drivers and guidance](references/drivers-guidance.md).
- **Forecast build/revision:** stages 5 to 8 of the sequence above; incorporate existing quality findings before valuation.
- **Workbook update:** preserve user edits, formulas, period structure and notes. If an inherited model falls short of the [model standard](references/model-standard.md), say where and bring it up to standard in a full update. If no compatible recalculation engine is available, label the workbook uncalculated and do not call it valuation-ready.
- **Existing coverage:** [model revision](../model-revision/SKILL.md) selects regular review or major update.

## Principles

- Carry known governance and financial-quality findings into model inputs. The governance assessment and red-flag screen run at initiation or when new evidence raises an issue; reuse valid prior findings otherwise. Map [governance findings](../corporate-governance/SKILL.md) into supported cash-access, related-party, dilution, compensation and financing assumptions. Do not bury value diversion in Other; keep an unquantifiable rights issue explicit for valuation rather than inventing a cash-flow haircut.
- Anchor near-term forecasts on the latest reported period, its call and peers already reported ([earnings clock](references/earnings-clock-and-peer-readthrough.md)). History supplies seasonality, cycle context and calibration. Carry the component build through the year [the market is trading](../research-cycle/references/what-the-market-trades.md#2-which-period-the-market-trades) when that is beyond the forward year. For a fast-growing line, build from the latest run rate and the capacity ramp with seasonality, channel inventory and demand tested, then set the result against management's plan and its guidance record; forecast above or below the plan when the evidence supports it.
- Choose drivers that explain the economics: units/price/mix, capacity/utilisation, users/monetisation or another suitable decomposition. Reconcile segment totals and cash requirements; do not impose a volume model where it misleads.
- Treat reported actuals, derived actuals, guidance, broker estimates and analyst assumptions as distinct, and preserve provenance when derived quarters are displayed as hard values. A guide is an input to assess, not a total to reach.
- Forecast competitor, customer and supplier responses, fund growth through explicit investment and working capital, and carry a supported transition to mature economics into valuation ([competition and capital returns](references/competition-and-capital-returns.md)). Translate material [macro conditions](../macro-event-analysis/references/market-regime-and-investor-base.md) into dated volume, price, cost, currency and financing scenarios; a sector rally does not raise operating forecasts without an economic channel.
- Show break-even inputs, competing cases and room for error ([underwriting standard](../research-cycle/references/underwriting-standard.md)). A downside case that reverses the call does not invalidate the central estimate; reserve blockers for missing essentials.
- Carry the brief's key metrics as model rows: our forward P/E (price over our NTM EPS), P/B on the latest book value, dividend yield, and next-year ROIC (after-tax operating profit over average equity plus debt; an operating version excluding cash and supplier financing can sit beside it).
- When distributions matter, build a [dividend schedule](../valuation-thesis/references/valuation-driver-and-dividends.md#dividend-evidence-and-period-alignment) linking earnings-year entitlements to payment years, attributable profit and funded cash capacity.
- Explain differences from fresh consensus and isolate source/vintage differences before judging a broker wrong ([benchmark comparison](references/benchmark-comparison.md)).
- Do not adjust assumptions to reach a target result. Reassess unusual costs, tax, impairments and share-based payments against the applicable accounting and current disclosures.
- Use the [shared financial terminology](../research-brief/references/natural-writing.md#profit-labels-and-valuation-language) in readable outputs.

## Handoff

Return the period/metric map, statement reconciliations, driver map, guidance register, actual/forecast boundary, assumption table with sources and sensitivity, outputs versus comparable consensus, changed cells/records and dependent artifacts, unresolved questions and the next task. Identify the executable model, engine/formula version, fingerprint, scenario/run and frozen forecasts for later evaluation; downstream agents consume these outputs directly. For the workbook, give the path/version, baseline fingerprint and backup, Revenue Build-to-Statements links, cash/financing checks, recalculation evidence and presentation review. [inspect_workbook.py](scripts/inspect_workbook.py) gives a read-only inventory; it does not recalculate.

Claims that a workbook was calculated, preserved or visually verified need actual evidence. A zero balance-sheet check alone does not validate the model or its cash flow. If assumptions move, invalidate dependent valuation, thesis, questions and quoted numbers.
