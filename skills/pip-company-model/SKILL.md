---
name: pip-company-model
description: Build and maintain executable company financial models with operating drivers and linked income statements, cash flows and balance sheets. Use for new issuer models, historical updates, forecast revisions, scenarios and forecast evaluation; preserve existing workbook models when requested.
metadata:
  version: 1.12.0
---

# Company model building and updates

This branch applies to a company underlying, not every tradable market. Work from the [evidence pack](../pip-evidence-intake/SKILL.md) and return a versioned [company-model handoff](../pip-research-cycle/references/handoffs.md). The model is an executable research tool for agents to calculate, query, update, value and evaluate against later actuals. A human-readable workbook or report is a view, not the completion criterion. Preserve an existing requested workbook; do not require Excel delivery for every full research task. A report and a total-only EPS forecast do not substitute for the economic model-building stages.

Read [agent-model.md](references/agent-model.md) for semantic metrics, scenario runs, evidence-driven changes, valuation dependencies, forecast evaluation and the optional deterministic calculation helper.

For full research and earnings updates, read [earnings timing and peer read-throughs](references/earnings-clock-and-peer-readthrough.md). Within near-term performance analysis, emphasize the latest reported quarter/half and the subsequent-period outlook; history supplies calibration, seasonality and cycle context. Compare latest management wording/Q&A, intervening updates and relevant earlier-reporting peers without copying peer results or assuming a fiscal calendar. Keep timing discipline within the shared materiality framework.

Before forecasts, consume the initial [governance assessment](../pip-corporate-governance/SKILL.md) and [financial-red-flag screen](../pip-financial-quality/references/financial-red-flags.md). Carry reported versus usable cash, suspect assets/claims, restrictions, related-party exposures and bounded losses into explicit inputs/scenarios. Do not build a Buy case on an unbounded material reporting contradiction or conceal it with a balancing plug. The later model audit revisits the same issue IDs; a preliminary screen is not assurance that the accounts are true.

## Complete model-building sequence

| Stage | Work and output | Read when doing this stage |
| --- | --- | --- |
| 1 | Establish versioned executable model state, periods, units, metric/dependency maps and a calculation backend; inspect/import existing workbooks when relevant | [Agent model](references/agent-model.md), [model setup](references/model-setup.md) |
| 2 | Populate and reconcile historical income statements, balance sheets and cash flows at the supported cadence | [Historical actuals](references/actuals.md) |
| 3 | Assemble the Data/price/segment history and reconcile definitions | [Drivers and guidance](references/drivers-guidance.md) |
| 4 | Extract dated management guidance and unresolved statements | [Drivers and guidance](references/drivers-guidance.md) |
| 5 | Build a queryable quarterly/half-year revenue and cost module, including volumes, price/mix, margins and unit economics; RP/UE tabs can expose it | [Revenue projection](references/revenue-projection.md) |
| 6 | Link the projection into forecast earnings and build operating-expense, tax, share, working-capital, asset, lease, debt and cash schedules | [Statement forecasts](references/statement-forecast.md) |
| 7 | Execute and audit the model, statement links, implied remaining periods, cash requirements and estimate gaps; retain run/version/check results and scenario sensitivities | [Forecast audit](references/forecast-audit.md), [agent model](references/agent-model.md) |

Then hand the audited forecast to valuation -> thesis validation/challenge -> investment conclusion -> brief. The final investment conclusion is downstream of the modelling work. Management questions can branch from any material unresolved assumption.

## Select the requested mode

- **Historical update:** inspect the current model and source periods; follow [actuals.md](references/actuals.md). Produce a reconciled historical baseline before forecasting.
- **Operating-driver update:** follow [drivers-guidance.md](references/drivers-guidance.md) for tracker and transcript analysis.
- **New model:** complete the sequence above using an available deterministic calculation backend and semantic input/output map. Choose the structure from the business economics, reporting cadence and available evidence.
- **Forecast build/revision:** use the separate revenue/cost and statement-forecast references above, then [forecast-audit.md](references/forecast-audit.md). Incorporate existing quality findings before valuation.
- **Workbook update:** preserve existing user edits, formulas, period structure and notes. Use a supported writer. If a compatible recalculation engine is unavailable, continue independent analysis but label the workbook uncalculated and do not assert it is complete or valuation-ready.
- **Agent review:** ingest new evidence into a new model version, recompute affected outputs and valuations, compare frozen forecasts with matched actuals, and retain attribution/next investigations. A saved watch or specification does not mean an automatic update service is running.

For a full company cycle, complete setup, historical statements, operating data, guidance assessment, projections, statement forecasts and audit before valuation. Historical reconciliation is part of model construction; targeted validation of a valuation thesis is a later pass. A focused update can reuse current upstream work.

## Modelling principles

Translate material [macro/regime conditions](../pip-macro-event-analysis/references/market-regime-and-investor-base.md) into dated volume, price, cost, currency and financing scenarios. Keep business-economics effects separate from investor attention, investability and willingness to pay. A sector rally or expected index inclusion does not justify raising operating forecasts without an economic channel; pass market-demand and multiple implications to valuation with their own evidence.

For full company forecasts, read [competition, capital returns and advantage duration](references/competition-and-capital-returns.md). Forecast material competitor/customer/supplier responses, fund growth through explicit investment and working capital, and assess marginal rather than only historical returns. Carry a supported transition from exceptional to mature economics into valuation. Sparse data permit labeled economic estimates; they do not justify treating growth as costless or exceptional margins as perpetual.

Use the [underwriting standard](../pip-research-cycle/references/underwriting-standard.md) and [investor judgment](../pip-research-cycle/references/investor-judgment.md) for assumption calibration and economic readiness. Test sell-in versus sell-through, organic versus acquired growth, selected versus full cohorts and proxy mappings where relevant. Combine available observations with industry economics, historical base rates and source-specific delivery patterns to make reasoned estimates. Show break-even inputs, competing cases and room for error; a downside case reversing the call does not by itself invalidate the central estimate. Reserve blockers for missing essentials that prevent meaningful modeling.

Map metrics by meaning and reporting basis before identifying cells. Treat reported actuals, derived actuals, management guidance, broker estimates and analyst assumptions as distinct. Preserve provenance when displaying derived quarters as hard values.

Choose business drivers that explain the company's economics: units/price/mix, capacity/utilisation, users/monetisation or another suitable decomposition. Reconcile segment totals and cash requirements; do not impose a volume model on a business where it is misleading.

Forecast from a reconciled baseline with explicit assumptions, constraints and scenarios. A guide is an input to assess, not a total that must be reached. Explain differences versus fresh consensus and isolate source/vintage differences before judging a broker wrong.

Map [governance findings](../pip-corporate-governance/SKILL.md) into supported cash-access, related-party, dilution, compensation, reinvestment and financing assumptions. Preserve issue/source IDs and exposure ranges; do not bury value diversion in Other or assume every unit of consolidated cash belongs to outside common shareholders. Keep a qualitative rights/discount issue explicit when it cannot be credibly quantified, and pass it to valuation rather than inventing a cash-flow haircut.

Do not adjust assumptions solely to reach a target result. Reassess unusual costs, tax, impairments and share-based payments using applicable accounting, current evidence and company disclosures.

## Handoff

Provide the period/metric map; statement reconciliations; operating-driver map; guidance register; actual/forecast boundary; assumption table with sources and sensitivity; current outputs versus comparable consensus; changed cells/records and dependent artifacts; unresolved questions and next task.

The primary handoff identifies the executable model, backend/formula version, model fingerprint, scenario/run, semantic outputs and lineage, missing/failed checks, downstream valuation dependencies and frozen forecasts for later evaluation. Downstream agents should consume these calculated outputs directly. Do not require a human to read or approve routine authorised calculations to advance the research.

For a workbook deliverable include the model path/version, baseline fingerprint, output and backup, explicit projection-to-3S links, cash/financing checks, recalculation evidence and presentation review. Use [inspect_workbook.py](scripts/inspect_workbook.py) for read-only OOXML inventory when useful; it does not recalculate or verify formula correctness.

Assertions that a workbook was calculated, preserved or visually verified require actual evidence of those checks. A zero balance-sheet check alone does not validate the model or its cash flow. If assumptions move, invalidate dependent valuation, thesis, questions and quoted numbers in briefs.
