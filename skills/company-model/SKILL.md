---
name: company-model
description: Build and maintain executable company financial models with operating drivers and linked income statements, cash flows and balance sheets. Use for new issuer models, historical updates, forecast revisions, scenarios and forecast evaluation; preserve existing workbook models when requested.
metadata:
  version: 2.0.0
---

# Company model building and updates

This branch applies to a company underlying, not every tradable market. Work from the [evidence pack](../evidence-intake/SKILL.md) and return a versioned [company-model handoff](../research-cycle/references/handoffs.md). The model is an executable research tool for agents to calculate, query, update, value and evaluate against later actuals. For this workspace, the user also requires a human-auditable Excel model whenever building or numerically revising company forecasts. Deliver a formula-driven `.xlsx` alongside any code/JSON interface; a static export of calculated outputs does not meet this requirement. Preserve existing user workbook edits. A report and a total-only EPS forecast do not substitute for the economic model-building stages.

Read [workbook delivery](references/workbook-profile.md) for the human review contract. Show editable assumptions and sources, operating builds, linked IS/CF/BS, financing, shares/dividends and valuation as applicable. Reconcile the workbook with the versioned agent model and exercise input changes before calling the forecast complete. An evidence-only review with no numerical changes may link the existing valid workbook. Follow a later explicit request for another format or no workbook.

For new model views, apply the [house theme](references/workbook-profile.md#house-theme-and-reporting-detail): gridlines off, bordered sections, black calculations, dark-blue actual inputs, purple forecast assumptions with a nude fill, bold local/final totals and compact right-aligned cells. Write assumption explanations and sources in visible long cells to the right. Use quarters where supported by the data, or halves when quarterly evidence is thin; choose cadence per schedule.

Percentage labels and figures are italic. Actual/calculated percentages use light grey; forecast percentage inputs/judgements retain purple with nude fill. This percentage convention overrides the ordinary actual/calculation colour.

For new forecasts and changes to model structure, read [foundational builds](references/foundational-builds.md). The model is a human-readable argument for the conviction its forecasts warrant. Break material financial items into their smallest useful forecastable components, substantiate the foundational estimates, and aggregate upward. Seek useful breakdowns in filings, management calls and third-party observations, keeping their evidence status distinct. Keep each related calculation chain on one worksheet, with assumptions and their basis beside the figures they drive. Reuse completed results across schedules. Judge source support, economic explanation, coherent behaviour and human usability separately from arithmetic checks. That reference supplies generic scripts, a blank plan and a wholly synthetic editable Excel example; adapt the business design rather than copying an old issuer workbook.

Read [agent-model.md](references/agent-model.md) for semantic metrics, scenario runs, evidence-driven changes, valuation dependencies, forecast evaluation and the optional deterministic calculation helper.

For sector-specific business analysis, evidence planning and model design, use the [activity-based sector references](references/sectors/index.md). Select material economic mechanisms rather than a sector-label template; load only the relevant cards. They provide operating chains, accounting/cash traps and independent synthetic examples across twenty activities. Apply the shared foundational-build method and existing specialist responsibilities; a sector card or calculated example is not a completed company forecast.

[Stock initiation](../stock-initiation/SKILL.md) orchestrates a new investment case; [model revision](../model-revision/SKILL.md) selects affected work, baseline preservation and attribution for existing coverage. This specialist supplies shared calculations for both. The complete construction sequence below does not require rebuilding unaffected stages on every revision.

Define net profit attributable to shareholders as the listed company's earnings after excluding non-controlling interests. Use that name, or attributable net profit after defining it, in readable outputs. Do not label it parent profit or confuse it with the parent company's standalone profit. Keep reported, adjusted and operating profit and cash flow separate. Stable internal metric IDs may remain if their definitions and displayed labels are clear.

When distributions matter, build a [dividend schedule](../valuation-thesis/references/valuation-driver-and-dividends.md#dividend-evidence-and-period-alignment): reconcile adopted policy and earnings-year interim/final entitlements with actual payment years. Link forecast payouts to attributable profit and funded cash capacity, retain policy conditions/expiry, and distinguish annual forward DPS from receipts within the target horizon. Test additional payout against recurring cash after investment, competing capital uses and constraints.

For full research and earnings updates, read [earnings timing and peer read-throughs](references/earnings-clock-and-peer-readthrough.md). Within near-term performance analysis, emphasize the latest reported quarter/half and the subsequent-period outlook; history supplies calibration, seasonality and cycle context. Compare latest management wording/Q&A, intervening updates and relevant earlier-reporting peers without copying peer results or assuming a fiscal calendar. Keep timing discipline within the shared materiality framework.

Before forecasts, consume the initial [governance assessment](../corporate-governance/SKILL.md) and [financial-red-flag screen](../financial-quality/references/financial-red-flags.md). Carry reported versus usable cash, suspect assets/claims, restrictions, related-party exposures and bounded losses into explicit inputs/scenarios. Do not build a Buy case on an unbounded material reporting contradiction or conceal it with a balancing plug. The later model audit revisits the same issue IDs; a preliminary screen is not assurance that the accounts are true.

## Complete model-building sequence

| Stage | Work and output | Read when doing this stage |
| --- | --- | --- |
| 1 | Map the business into forecastable components and foundational inputs; establish versioned model state, periods, units, dependencies and a calculation backend; inspect existing workbooks when relevant | [Foundational builds](references/foundational-builds.md), [agent model](references/agent-model.md), [model setup](references/model-setup.md) |
| 2 | Populate and reconcile historical income statements, balance sheets and cash flows at the supported cadence | [Historical actuals](references/actuals.md) |
| 3 | Gather component history from filings, management-call detail and suitable external series; reconcile definitions and identify estimated splits | [Drivers and guidance](references/drivers-guidance.md) |
| 4 | Extract dated management guidance and unresolved statements | [Drivers and guidance](references/drivers-guidance.md) |
| 5 | Forecast the foundational pieces and build them into component and segment totals in locally readable operating blocks, at the supported cadence | [Revenue projection](references/revenue-projection.md), [foundational builds](references/foundational-builds.md) |
| 6 | Build matched component costs, unit economics, segment gross profit/margins and the investment needed to deliver the revenue forecast | [Revenue and cost projection](references/revenue-projection.md), [foundational builds](references/foundational-builds.md) |
| 7 | Link operating projections into forecast earnings and build operating-expense, tax, share, working-capital, asset, lease, debt and cash schedules | [Statement forecasts](references/statement-forecast.md) |
| 8 | Execute and audit the model, statement links, implied remaining periods, cash requirements and estimate gaps; retain run/version/check results and scenario sensitivities | [Forecast audit](references/forecast-audit.md), [agent model](references/agent-model.md) |

Then hand the audited forecast to valuation -> thesis validation/challenge -> conviction assessment -> investment conclusion -> brief and follow-up under the [research coordinator](../research-cycle/SKILL.md). The final investment conclusion is downstream of the modelling work. Management questions can branch from any material unresolved assumption.

## Select the requested mode

- **Historical update:** inspect the current model and source periods; follow [actuals.md](references/actuals.md). Produce a reconciled historical baseline before forecasting.
- **Operating-driver update:** follow [drivers-guidance.md](references/drivers-guidance.md) for tracker and transcript analysis.
- **New model:** complete the sequence above using an available deterministic calculation backend and semantic input/output map. Choose the structure from the business economics, reporting cadence and available evidence.
- **Forecast build/revision:** use the separate revenue/cost and statement-forecast references above, then [forecast-audit.md](references/forecast-audit.md). Incorporate existing quality findings before valuation.
- **Workbook update:** preserve existing user edits, formulas, period structure and notes. Use a supported writer. If a compatible recalculation engine is unavailable, continue independent analysis but label the workbook uncalculated and do not assert it is complete or valuation-ready.
- **Agent review:** ingest new evidence into a new model version, recompute affected outputs and valuations, compare frozen forecasts with matched actuals, and retain attribution/next investigations. A saved watch or specification does not mean an automatic update service is running.

For a full company cycle, complete setup, historical statements, operating data, guidance assessment, projections, statement forecasts and audit before valuation. Historical reconciliation is part of model construction; targeted validation of a valuation thesis is a later pass. A focused update can reuse current upstream work.

## Modelling principles

Translate material [macro/regime conditions](../macro-event-analysis/references/market-regime-and-investor-base.md) into dated volume, price, cost, currency and financing scenarios. Keep business-economics effects separate from investor attention, investability and willingness to pay. A sector rally or expected index inclusion does not justify raising operating forecasts without an economic channel; pass market-demand and multiple implications to valuation with their own evidence.

For full company forecasts, read [competition, capital returns and advantage duration](references/competition-and-capital-returns.md). Forecast material competitor/customer/supplier responses, fund growth through explicit investment and working capital, and assess marginal rather than only historical returns. Carry a supported transition from exceptional to mature economics into valuation. Sparse data permit labeled economic estimates; they do not justify treating growth as costless or exceptional margins as perpetual.

Use the [underwriting standard](../research-cycle/references/underwriting-standard.md) and [investor judgment](../research-cycle/references/investor-judgment.md) for assumption calibration and economic readiness. Test sell-in versus sell-through, organic versus acquired growth, selected versus full cohorts and proxy mappings where relevant. Combine available observations with industry economics, historical base rates and source-specific delivery patterns to make reasoned estimates. Show break-even inputs, competing cases and room for error; a downside case reversing the call does not by itself invalidate the central estimate. Reserve blockers for missing essentials that prevent meaningful modeling.

Map metrics by meaning and reporting basis before identifying cells. Treat reported actuals, derived actuals, management guidance, broker estimates and analyst assumptions as distinct. Preserve provenance when displaying derived quarters as hard values.

Choose business drivers that explain the company's economics: units/price/mix, capacity/utilisation, users/monetisation or another suitable decomposition. Reconcile segment totals and cash requirements; do not impose a volume model on a business where it is misleading.

Forecast from a reconciled baseline with explicit assumptions, constraints and scenarios. A guide is an input to assess, not a total that must be reached. Explain differences versus fresh consensus and isolate source/vintage differences before judging a broker wrong.

When comparing forecasts or testing a rebuilt model against another analyst, read [benchmark comparison](references/benchmark-comparison.md). Map periods and definitions per schedule, reconcile component bets and the earnings gap, and examine whether historical mix and cost leverage remain supported. Use the generic comparison helper for arithmetic; a broker gap is not a realised forecasting error.

Map [governance findings](../corporate-governance/SKILL.md) into supported cash-access, related-party, dilution, compensation, reinvestment and financing assumptions. Preserve issue/source IDs and exposure ranges; do not bury value diversion in Other or assume every unit of consolidated cash belongs to outside common shareholders. Keep a qualitative rights/discount issue explicit when it cannot be credibly quantified, and pass it to valuation rather than inventing a cash-flow haircut.

Do not adjust assumptions solely to reach a target result. Reassess unusual costs, tax, impairments and share-based payments using applicable accounting, current evidence and company disclosures.

## Handoff

Provide the period/metric map; statement reconciliations; operating-driver map; guidance register; actual/forecast boundary; assumption table with sources and sensitivity; current outputs versus comparable consensus; changed cells/records and dependent artifacts; unresolved questions and next task.

The primary handoff identifies the executable model, backend/formula version, model fingerprint, scenario/run, semantic outputs and lineage, missing/failed checks, downstream valuation dependencies and frozen forecasts for later evaluation. Downstream agents should consume these calculated outputs directly. Do not require a human to read or approve routine authorised calculations to advance the research.

For the workbook deliverable include the model path/version, baseline fingerprint, output and backup, explicit projection-to-3S links, cash/financing checks, recalculation evidence and presentation review. Use [inspect_workbook.py](scripts/inspect_workbook.py) for read-only OOXML inventory when useful; it does not recalculate or verify formula correctness.

Assertions that a workbook was calculated, preserved or visually verified require actual evidence of those checks. A zero balance-sheet check alone does not validate the model or its cash flow. If assumptions move, invalidate dependent valuation, thesis, questions and quoted numbers in briefs.
