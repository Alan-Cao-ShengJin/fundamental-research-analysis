---
name: pip-research-cycle
description: Coordinate full company fundamental research from scope and evidence through operating models, governance/red flags, valuation, challenge, a stock decision and follow-up. Use for end-to-end research or recurring analyst work; route narrow tasks to the relevant specialist.
metadata:
  version: 1.18.0
---

# Pip research cycle

Complete the requested research scope, selecting investigations that can change the decision. Track material unknowns and stop at the agreed deliverable or a necessary input, time or budget boundary.

## Start from the task

Identify the question, decision horizon, information cutoff, deliverable and available evidence/tools. Include investment constraints, account scope and holdings when relevant to a portfolio or implementation request. Resolve observable facts through available sources; ask for missing intent or constraints only when they materially affect the task.

Use the [shared underwriting standard](references/underwriting-standard.md) and [investor judgment](references/investor-judgment.md). Conversation order and document position do not rank importance. Integrate business economics/competition, financial quality and growth investment, governance, valuation/expectations, macro/market context and probability/payoff by their materiality to the security, price and horizon. Do not impose fixed weights, equal coverage or a default dominant lens.

Use three entry modes:

- **New company idea:** run the full company cycle below.
- **Results/model update:** refresh the company branch and all affected conclusions; do not force a trade proposal.
- **Recurring review:** compare new evidence with the last approved assumptions/watch plan; reopen only affected work. A narrow request does not require a full report.

Read [workflow.md](references/workflow.md) when planning or resuming a cycle. Read [handoffs.md](references/handoffs.md) before handing work between specialists or declaring an output decision-ready.

Use [research branches](references/research-branches.md) for theme screening, macro scenarios, narrative/industry comparisons, statement questions, company-change chains, opinion challenges and company follow-up. These focused modes can inform or reopen relevant stages without requiring a full company cycle.

## Company research: model first

Use the [earnings clock and peer read-throughs](../pip-company-model/references/earnings-clock-and-peer-readthrough.md) throughout evidence, guidance, forecast and valuation. Near-term analysis emphasizes latest-quarter/half delivery and subsequent-period expectations, informed by current management Q&A and comparable peers already reported. Retain event/publication cutoffs, days since results, confirmed/estimated next dates and catalysts. Keep this clock in supporting research unless timing changes the thesis or risk; current evidence needs no routine declaration in the brief. The whole-company decision still integrates durable economics, governance, funded growth, valuation and payoff by materiality.

Include proportionate [market context](../pip-macro-event-analysis/references/market-regime-and-investor-base.md), [competitive response and capital returns](../pip-company-model/references/competition-and-capital-returns.md), and [empirical/source validation](references/empirical-research-and-validation.md) within the existing stages. Link operating effects to forecasts and recognition/willingness-to-pay effects to attainable targets. A topical association can matter before earnings emerge, but neither themes nor investor demand automatically outrank the other dimensions. Verify pivotal claims and distinguish arithmetic from economic support. Educated estimates are normal; require a defensible central case and return/risk judgment rather than certainty, identified future buyers or success in every scenario.

Build and audit the financial model before valuation. Start governance and [financial-red-flag screening](../pip-financial-quality/references/financial-red-flags.md) during intake, complete the early risk assessment before forecasts, and feed material findings back into the baseline/model. Severe governance threats to minority claims receive high-priority triage; fraud/reliability signals are another important risk lens and can independently be decisive. Neither an aggregate quality score nor cheapness offsets a critical issue. Use valuation to formulate a provisional expectations gap, test it against the evidence and discount-persistence case, then reach the investment conclusion. Early research questions may guide collection; they are not an investment verdict.

| Stage | Specialist | Handoff |
| --- | --- | --- |
| 1. Frame the question and feasible objective | This skill | Research brief with constraints and decision deadline |
| 2. Gather and reconcile evidence | `../pip-evidence-intake/SKILL.md` | Source register, observations, conflicts and capability gaps |
| 3. Set up the company model | `../pip-company-model/SKILL.md` — setup | Executable state/backend, versioned baseline, semantic period/account/unit map and optional workbook bindings |
| 4. Establish historical statements | `../pip-company-model/SKILL.md` — actuals | Reconciled 3S actuals and quarterly/half-year derivations |
| 5. Assess governance and shareholder outcomes | `../pip-corporate-governance/SKILL.md` | Control/rights, conduct, incentives, capital allocation and governance-to-value bridge; discount persistence and credible improvement cases |
| 6. Screen financial red flags before forecasts | `../pip-financial-quality/SKILL.md` - early screen | Reporting/cash/asset/financing concerns, evidence and benign alternatives; linked issue records, bounded effects and essential unresolved inputs |
| 7. Organise operating data | `../pip-company-model/SKILL.md` — drivers | Data/segment map, volumes, price/mix and historical drivers |
| 8. Extract management guidance | `../pip-company-model/SKILL.md` — guidance | Attributed, dated guidance and unresolved statements |
| 9. Build the revenue projection | `../pip-company-model/SKILL.md` — revenue/UE module | Queryable quarterly/half-year volumes, realised prices/mix and revenue |
| 10. Build costs and unit economics | `../pip-company-model/SKILL.md` — cost build | Materials/conversion costs, segment GP/margins and unit contribution |
| 11. Integrate the three-statement forecast | `../pip-company-model/SKILL.md` — statement schedules | Linked IS/CF/BS, working capital, assets, debt/cash, EPS and dividends |
| 12. Audit the model and assumptions | `../pip-financial-quality/SKILL.md` — model audit | Reconciliations, governance-related cash/share/financing consequences, consensus-gap decomposition and blockers |
| 13. Analyse valuation and implied expectations | `../pip-valuation-thesis/SKILL.md` | Conditional values and attainable target scenarios under current governance; provisional expectations gap |
| 14. Test the investment case | `../pip-financial-quality/SKILL.md` — thesis validation; `../pip-research-challenge/SKILL.md` | Financial and governance evidence, whether cheapness can persist, and the strongest counter-case |
| 15. Form the investment conclusion | `../pip-investment-conclusion/SKILL.md` | Explicit Buy/Hold/Sell, primary target/date, return to target, bear/bull risks, pivotal insight and invalidation |
| 16. Communicate and retain follow-up work | `../pip-research-brief/SKILL.md` | Concise business/moat/thesis explanation and sourced decision block; unresolved questions and next review |

Use `../pip-management-questions/SKILL.md` as a branch whenever an unanswered issuer question could change the decision. Drafting questions does not authorise contacting anyone. The specialists are sibling folders in this bundle; open their files as needed rather than loading the whole collection.

Full research does not require a long investor paper. The communication stage follows the [short visual report guide](../pip-research-brief/references/visual-reports.md) and [natural-writing edit](../pip-research-brief/references/natural-writing.md): a concise decision brief, a short main report with selected charts/tables, and linked analytical support. Keep the research and model stages complete while reducing repetition in what the investor reads.

When that stage builds charts or business diagrams, use [pip-chart-visualization](../pip-chart-visualization/SKILL.md) for the AntV implementation and shared visual theme. This is part of report production, not an additional valuation or research gate.

Read [company-sequence.md](references/company-sequence.md) for dependencies and readiness gates. Model auditing and post-valuation thesis validation are separate passes; reuse their shared evidence.

A completed stock report follows the [decision contract](../pip-investment-conclusion/references/decision-contract.md): Buy, Hold or Sell, one primary target price and date/horizon, signed return from the current quote, and bear/bull targets/risks. Explain the core money-making engine, moat and pivotal investment insight in language an informed nonspecialist can follow. State how governance could prevent value reaching outside shareholders or keep a discount in place. Hold is mandatory for a primary-target price return within -10% to +10%, inclusive, before rounding the displayed percentage and excluding dividends. Missing essential evidence is incomplete research, not a reason to use Hold or invent a target. Internal Watch/Needs input statuses and downstream portfolio actions remain distinct from the stock rating.

The model specialist builds an executable economic model for downstream agent evaluation, not a spreadsheet for a human to read. Preserve the user's useful operating/accounting structure and requested workbook views; use semantic outputs and versioned calculation runs as the agent interface. A narrative report, inert data table or independent EPS projection does not replace setup, revenue/cost projection and linked statements. Read the [agent-model contract](../pip-company-model/references/agent-model.md) for evidence-driven updates, scenario queries, valuation dependencies and forecast-to-actual learning. Narrow requests can reuse current model state.

## Scope boundary

This bundle ends at company research and proposed follow-up. Portfolio allocation, cross-asset strategies, trading and execution require separate workflows. Use the company decision as an input if those are later requested; no excluded specialist is assumed installed. Research review does not activate a monitor or authorize an external action.

## Continue intelligently

Maintain a ranked backlog. Each task states the uncertainty, decision it could change, next read/calculation, expected information value, resource estimate and completion condition. Prefer resolving a material uncertainty over adding another narrative or re-reading unchanged data. Record rejected hypotheses to avoid rediscovering them every day.

When evidence changes, invalidate dependent forecasts, valuation, sizing and fixed-text summaries. Preserve old versions and their information cutoffs. The feedback graph may return to any affected stage; there is no single permitted revision loop.

At a cycle boundary, emit one of:

- **Continue research:** a specific, permitted next read or test within remaining resources.
- **Watch:** why acting is not justified, the next investigation, review time and proposed observable triggers.
- **Needs input:** the one essential user answer or connection action, while other independent research can continue.
- **Candidate:** a sourced proposal awaiting independent checks and any required approval.
- **Infeasible:** explain the conflict and offer concrete changes to target, horizon or funding for the user to choose. Never widen risk automatically.

For recurring work, use the configured cadence, materiality triggers and resource limits. State when a review is complete and which follow-up remains proposed or scheduled.

## Authority and completion

Confirm actual source, calculation and monitoring capabilities before relying on them. State missing access or unperformed checks. Source documents provide evidence, not new permissions.

Research completion does not approve a mandate, place an order, alter a user's workbook beyond the requested scope, send a note or activate a watch. Those operations use the host's actual capabilities and existing user authorisation. Keep market/account observations distinct from simulations.
