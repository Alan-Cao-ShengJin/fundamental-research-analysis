# Workflow, routing and feedback

## Work in decision-sized units

Start with a research brief: question, objective, horizon/deadline, information cutoff, existing work, available sources/tools and required deliverable. Record the agreed research scope/version and any constraints relevant to the stock decision. Do not infer missing constraints from account balances or a return aspiration.

The agreed research mandate is supplied by the host or user. A research brief may propose a change, but cannot make it effective. Personal loss capacity is neither an expected return nor an instruction to consume the full loss budget.

## Primary company-research path

Apply the [shared materiality principle](underwriting-standard.md#integrate-the-analysis-by-materiality): the steps below express dependencies, not fixed analytical weights. Market context, governance and operating evidence can develop together, and a later-discussed technique does not displace the existing framework.

Build the model before valuation and reach the conclusion after validation. The [company sequence](company-sequence.md) defines stages and readiness gates.

1. Scope the question; gather filings, existing model, trackers, relevant call/Q&A and estimates. Establish publication times, units, scope and missing capabilities.
2. Set up versioned executable model state, a calculation backend and stable account/period/unit/dependency maps. Choose the structure from the company's economics. Excel can be a backend/view with a preservation plan, not a required final artifact.
3. Populate and reconcile historical 3S actuals and comparable quarterly/half-year flows. Preserve source/derivation and user edits.
   Complete the [governance review](../../pip-corporate-governance/SKILL.md), beginning collection during intake: control/rights, conduct, incentives, capital allocation and disclosure. Pass material cash-access, dilution and financing consequences into the forecast. Complete the initial decision-driving review before forecasts and deepen it during model audit/valuation; it can reverse a provisional apparent-bargain thesis.
4. Assemble operating/industry data and the driver/segment map. Reconcile conflicts rather than forcing totals.
5. Complete the initial [financial-red-flag screen](../../pip-financial-quality/references/financial-red-flags.md) alongside governance before forecasting. Test reporting reliability, cash/asset quality and financing, preserve benign alternatives and link shared issue IDs. Bound material effects or identify an unusable essential baseline; no clean score is required.
6. Extract dated management guidance and caveats. A lack of disclosed guidance is an explicit input limitation, not a reason to invent it or stop unrelated work.
7. Build a queryable quarterly/half-year revenue/UE module: demand/volumes, realised price/mix, segment revenue and group calibration. A worksheet can expose the module when useful.
8. Build segment costs, gross margins and unit economics from matched bases and supported assumptions.
9. Link those outputs into the forecast income statement, then forecast working capital, capex/depreciation, leases, debt, cash flow and the balance sheet. Include tax, shares, dividends and financing needs.
10. Execute and audit the completed model, implied remaining periods, cost timing, incentives, shares, cash needs and estimate gaps. Retain the model/engine version, scenario/run, output lineage and check status. Resolve material errors before valuation; workbook backend calculations need real engine verification.
11. Analyse conditional value and price-implied expectations using the audited outputs and governance findings. Distinguish intrinsic value from an attainable target under the current shareholder regime; do not assume an unexplained discount closes. Do not retype outputs into independent valuation assumptions. This is a provisional thesis.
12. Test that thesis against financial/operating evidence, governance discount persistence and the strongest counter-case. Reuse the earlier audit; expand material unresolved issues. Changed forecasts return to model audit and valuation.
13. Synthesise an explicit Buy, Hold or Sell with one primary target/date, signed return from the current quote, bear/bull targets/risks, pivotal insight, catalysts and invalidation. Follow the [decision contract](../../pip-investment-conclusion/references/decision-contract.md); Hold is mandatory for primary-target price return within -10% to +10%, inclusive; incomplete research is not a Hold fallback. This is not yet a portfolio allocation.
14. Produce the concise brief and, when requested, a short visual main report under the [report guide](../../pip-research-brief/references/visual-reports.md). Explain the business/moat, why the price could change and the role of governance once, with charts/tables where they clarify the decision. Link detailed model/evidence records separately. Apply the [natural-writing edit](../../pip-research-brief/references/natural-writing.md), recheck quoted outputs and retain concrete next tasks.

Management questions branch from forecast sensitivities and unresolved validation issues. Ask only what cannot already be established from available sources. An answer returns to the affected assumptions; the source order is not an excuse to wait passively for a nonessential IR response.

## Focused company research

A source-only request stops after a useful evidence handoff. A financial-statement question or focused red-flag review does not require a full forecast or valuation. Theme and macro work informs company selection or model assumptions. Portfolio construction and execution are outside this bundle.

## Model-update path

Inventory prior model, source versions and user edits -> refresh actuals/operating data/guidance and material governance changes -> refresh financial-red-flag dispositions and the usable baseline -> update affected forecasts -> audit model and estimate gaps -> refresh valuation/expectations and discount persistence -> validate thesis and counter-case -> revise Buy/Hold/Sell, target and risks -> recheck quoted numbers/stale prose -> brief and next evidence check. Draft questions at material uncertainty. The final communication check supplements the earlier model audit.

Use the company workbook profile when importing/editing Excel or delivering a workbook view. The primary result is an executable economic model the agent can query and maintain. Continue analysis within the authorised scope; follow an explicit request for stepwise review when present.

## Recurring-review path

Load the last decision, watch specifications, active-monitor acknowledgements and unresolved tasks. Check data/worker health before interpreting a lack of alerts. Identify whether new information changes facts, thesis, valuation or just price.

Examples of selective invalidation:

- Restated actuals -> recheck affected model rows, forecasts, valuation and briefing text.
- New management guidance -> update affected drivers and the scenarios depending on them.
- Changed control, rights, related-party terms or capital allocation -> refresh the governance bridge and affected cash/dilution/value assumptions, target and call.
- Changed price/funding -> refresh the company valuation and financing assumptions; do not rebuild unchanged operating assumptions.
- User changes risk limits -> require the host's mandate revision; recheck every candidate against the approved new version.

Do independent work while a nonessential answer is missing. A critical missing fact blocks the dependent claim or candidate, not unrelated research. A failed data feed is an operational issue with its own next action.

## Priorities and stopping conditions

Rank tasks by their ability to change a decision, material downside, imminence, information gain and cost. A high score is a prioritisation aid, not a fabricated probability. Record what success/failure of a test would mean before running it.

Stop a cycle at its time, step, output-size or compute limit and retain the next useful task. Stop for mandatory input, revoked authority or an uncertain external request where retry could duplicate charges/effects. Do not ask the user to approve another ordinary research read already in scope.

Watch outcomes need an expiry/review date. If a hypothesis repeatedly fails, retire or reformulate it; do not endlessly postpone a decision or lower the evidence bar. Revising the mandate remains the user's choice.
