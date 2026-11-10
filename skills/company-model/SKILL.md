---
name: company-model
description: Build and maintain executable company financial models with operating drivers and linked income statements, cash flows and balance sheets. Use for new issuer models, historical updates, forecast revisions, scenarios and forecast evaluation; preserve existing workbook models when requested.
metadata:
  version: 2.5.3
---

# Company model building and updates

Build an executable economic model from the [evidence pack](../evidence-intake/SKILL.md), with linked operating drivers and statements. Every new model meets the [model standard](references/model-standard.md): linked statements and material schedules at the supported cadence, annual roll-ups, component forecasts, evidence, guidance, valuation and scenarios. The [synthetic manufacturer](assets/company-model-example.xlsx) demonstrates depth, local calculation order and linking; adapt its financial rows and schedules to the issuer's economic activities rather than imposing its industrial accounts on every company. Build with [model_workbook.py](scripts/model_workbook.py) and recalculate in Excel under the [workbook contract](references/workbook-profile.md), which also documents compatible alternatives and their verification limits. The Excel workbook and agent interface are both required and mechanically synchronised. A report or total-only EPS forecast does not replace the operating build.

The model is a human-readable argument for the conviction its forecasts warrant. Break material items into their smallest useful forecastable components, substantiate the foundational estimates and aggregate upward. Keep each related calculation chain on one worksheet, with assumptions and their basis beside the figures they drive. Read [foundational builds](references/foundational-builds.md) for the method, the tools and the synthetic example; adapt the business design rather than copying an old issuer workbook.

[Stock initiation](../stock-initiation/SKILL.md) orchestrates a new case; [model revision](../model-revision/SKILL.md) selects the affected work for existing coverage. This specialist supplies the calculations for both; a revision does not rebuild unaffected stages.

Use the clean [model_layout.py](scripts/model_layout.py) primitives for worksheet objects, period rows, headers and text sheets; pass this study's periods, forecast columns and identity rather than copying generic plumbing from an issuer builder. The original synthetic model delegates to these helpers. Driver assumptions, mappings and business-specific schedules remain in the study.

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
- Apply [metric identity](references/metric-identity.md) before converting a pivotal rate, ratio or project appraisal into profit. Use [linked explanations](references/linked-explanations.md) for repeated numerical/rating notes so the human model stays connected to its calculations.
- Treat reported actuals, derived actuals, guidance, broker estimates and analyst assumptions as distinct, and preserve provenance when derived quarters are displayed as hard values. A guide is an input to assess, not a total to reach.
- Keep an observed amount separate from inferred classification, recognition and payment timing; distinguish binding constraints from management targets and our assumed deadlines. Use the [state and timing bridge](references/statement-forecast.md#classification-recognition-and-payment-states) when those choices can change the view.
- Forecast competitor, customer and supplier responses, fund growth through explicit investment and working capital, and carry a supported transition to mature economics into valuation ([competition and capital returns](references/competition-and-capital-returns.md)). Translate material [macro conditions](../macro-event-analysis/references/market-regime-and-investor-base.md) into dated volume, price, cost, currency and financing scenarios; a sector rally does not raise operating forecasts without an economic channel.
- Show break-even inputs, competing cases and room for error ([underwriting standard](../research-cycle/references/underwriting-standard.md)). A downside case that reverses the call does not invalidate the central estimate; reserve blockers for missing essentials.
- Carry the brief's economically meaningful metrics as model rows, with matched definitions and periods. Forward P/E needs positive comparable earnings; P/B needs meaningful book capital. State the invested-capital boundary for ROIC and match its profit exclusions. Use sector-appropriate return and capital measures for banks, insurers and other specialized businesses; show an inapplicable ratio as n/a with a reason, not a forced industrial calculation.
- When distributions matter, build a [dividend schedule](../valuation-thesis/references/valuation-driver-and-dividends.md#dividend-evidence-and-period-alignment) linking earnings-year entitlements to payment years, attributable profit and funded cash capacity.
- Explain differences from fresh consensus and isolate source/vintage differences before judging a broker wrong ([benchmark comparison](references/benchmark-comparison.md)).
- Do not adjust assumptions to reach a target result. Reassess unusual costs, tax, impairments and share-based payments against the applicable accounting and current disclosures.
- Use the [shared financial terminology](../research-brief/references/natural-writing.md#profit-labels-and-valuation-language) in readable outputs.

## Handoff

Return the period/metric map, statement reconciliations, driver map, guidance register, actual/forecast boundary, assumption table with sources and sensitivity, outputs versus comparable consensus, changed cells/records and dependent artifacts, unresolved questions and the next task. Identify the executable model, engine/formula version, fingerprint, scenario/run and frozen forecasts for later evaluation; downstream agents consume these outputs directly. For the workbook, give the path/version, baseline fingerprint and backup, Revenue Build-to-Statements links, cash/financing checks, recalculation evidence and presentation review. [inspect_workbook.py](scripts/inspect_workbook.py) gives a read-only inventory; it does not recalculate.

Claims that a workbook was calculated, preserved or visually verified need actual evidence. A zero balance-sheet check alone does not validate the model or its cash flow. If assumptions move, invalidate dependent valuation, thesis, questions and quoted numbers.
