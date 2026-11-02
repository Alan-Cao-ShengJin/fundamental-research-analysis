---
name: research-cycle
description: Govern research routing and specialist use. Classify stock research as new initiation or existing coverage, then distinguish regular reviews from major earnings/catalyst updates. Route narrow company tasks to the relevant specialist; portfolio and non-company workflows are external.
metadata:
  version: 2.0.0
---

# Research cycle

Complete the requested research scope, selecting investigations that can change the decision. Track material unknowns and stop at the agreed deliverable or a necessary input, time or budget boundary.

## Start from the task

Identify the question, decision horizon, information cutoff, deliverable and available evidence/tools. Include investment constraints, account scope and holdings when relevant to a portfolio or implementation request. Resolve observable facts through available sources; ask for missing intent or constraints only when they materially affect the task.

For full company research or a completed decision update, build the [sequence and coverage plan](references/research-coverage.md) at scope and reconcile it before declaring completion. Account for every skill as required, conditional or outside scope, then record actual work, valid reuse or a reasoned applicability decision. Open the relevant specialist instructions; listing a skill is not using it. Keep scoped source/model questions scoped rather than forcing the full plan. The optional [plan helper](scripts/research_plan.py) checks omissions and sequence, not research quality.

Use the [shared underwriting standard](references/underwriting-standard.md) and [investor judgment](references/investor-judgment.md). Conversation order and document position do not rank importance. Integrate business economics/competition, financial quality and growth investment, governance, valuation/expectations, macro/market context and probability/payoff by their materiality to the security, price and horizon. Do not impose fixed weights, equal coverage or a default dominant lens.

Select the entry mode before loading the full company sequence:

For stock research, apply [request routing](references/request-routing.md) first. It governs specialist selection and how much work to reopen: **new initiation** or **existing research update**, with existing updates split into **regular review** and **major earnings/catalyst update**. Record the selected mode, baseline and trigger in the research brief; a request called an "update" does not itself justify changing forecasts.

- **Discovery or quick comparison:** use [fundamental/theme screening](../theme-screening/SKILL.md) for financial filters, candidate lists or value-chain discovery. A request for sector leadership enters the macro specialist's rotation mode, then screening when useful. Return a bounded shortlist and next decisive questions; a screen is not a stock initiation or completed recommendation.
- **New stock initiation:** use [stock initiation](../stock-initiation/SKILL.md) to establish a new baseline, forecast and investment case through the full cycle below. Honor an explicitly fresh/independent study.
- **Existing research - regular review:** use [model revision](../model-revision/SKILL.md) in regular-review mode. Read prior research/model first, check intervening evidence, and carry operating forecasts forward unless concrete new data supports a specific change. Refresh price, valuation and prospective return with separate attribution; a price move alone changes neither EPS nor fair value.
- **Existing research - major earnings/catalyst update:** use the same entry skill in major-update mode. Freeze the prior forecast, gather official disclosures and relevant calls, compare matched actuals with prior assumptions, record hits/misses and causes, then recalibrate affected forecasts, audit and refresh the decision. Reuse unaffected work.
- **Portfolio or non-company idea:** explain this bundle's boundary and hand off to an external workflow; do not impose stock initiation on it.
- **Recurring review:** recurrence specifies cadence, not an analytical mode. Company reviews use the regular or major branch above according to evidence; portfolio and other-asset reviews use their relevant branch. A narrow request does not require a full report.

Read [workflow.md](references/workflow.md) when planning or resuming a cycle. Read [handoffs.md](references/handoffs.md) before handing work between specialists or declaring an output decision-ready.

Use [investment conviction](../investment-conviction/SKILL.md) to establish and preserve one decisive economic or avoidance proposition. Draft it during initiation, test it against model/governance/challenge findings before the conclusion, and retrieve its original conditions before reviewing existing coverage. The current investment mandate plans for at least one year; neither volatility nor an anniversary alone breaks the case, and the horizon never requires retaining a broken one. Keep belief, forecasts/value, price-based rating, eligibility and portfolio actions distinct.

Use [research branches](references/research-branches.md) for theme screening, macro scenarios, narrative/industry comparisons, statement questions, company-change chains, opinion challenges and portfolio risk budgets. These focused modes can inform or reopen relevant stages without requiring a full company cycle.

## Company research: shared model-first methods

The complete sequence below establishes new coverage. Revision uses the same financial, governance, valuation and decision standards with a different evidence window, skill emphasis and output. The [revision workflow](../model-revision/references/revision-workflow.md) defines baseline eligibility, changed dependencies and when broader rebuilding is justified. A short revision note is normally sufficient; a full initiation pitch is not required for every update.

Use the [earnings clock and peer read-throughs](../company-model/references/earnings-clock-and-peer-readthrough.md) throughout evidence, guidance, forecast and valuation. Near-term analysis emphasizes latest-quarter/half delivery and subsequent-period expectations, informed by current management Q&A and comparable peers already reported. Retain event/publication cutoffs, days since results, confirmed/estimated next dates and catalysts. Keep this clock in supporting research unless timing changes the thesis or risk; current evidence needs no routine declaration in the brief. The whole-company decision still integrates durable economics, governance, funded growth, valuation and payoff by materiality.

Include proportionate [market context](../macro-event-analysis/references/market-regime-and-investor-base.md), [competitive response and capital returns](../company-model/references/competition-and-capital-returns.md), and [empirical/source validation](references/empirical-research-and-validation.md) within the existing stages. Link operating effects to forecasts and recognition/willingness-to-pay effects to attainable targets. A topical association can matter before earnings emerge, but neither themes nor investor demand automatically outrank the other dimensions. Verify pivotal claims and distinguish arithmetic from economic support. Educated estimates are normal; require a defensible central case and return/risk judgment rather than certainty, identified future buyers or success in every scenario.

Build and audit the financial model before valuation. Start governance and [financial-red-flag screening](../financial-quality/references/financial-red-flags.md) during intake, complete the early risk assessment before forecasts, and feed material findings back into the baseline/model. Severe governance threats to minority claims receive high-priority triage; fraud/reliability signals are another important risk lens and can independently be decisive. Neither an aggregate quality score nor cheapness offsets a critical issue. Use valuation to formulate a provisional expectations gap, test it against the evidence and discount-persistence case, then reach the investment conclusion. Early research questions may guide collection; they are not an investment verdict.

| Stage | Specialist | Handoff |
| --- | --- | --- |
| 1. Frame the question and feasible objective | This skill | Research brief with constraints and decision deadline |
| 2. Gather and reconcile evidence | `../evidence-intake/SKILL.md` | Source register, observations, conflicts and capability gaps |
| 3. Set up the company model | `../company-model/SKILL.md` — setup | Executable state/backend, versioned baseline, semantic period/account/unit map and optional workbook bindings |
| 4. Establish historical statements | `../company-model/SKILL.md` — actuals | Reconciled 3S actuals and quarterly/half-year derivations |
| 5. Assess governance and shareholder outcomes | `../corporate-governance/SKILL.md` | Control/rights, conduct, incentives, capital allocation and governance-to-value bridge; discount persistence and credible improvement cases |
| 6. Screen financial red flags before forecasts | `../financial-quality/SKILL.md` - early screen | Reporting/cash/asset/financing concerns, evidence and benign alternatives; linked issue records, bounded effects and essential unresolved inputs |
| 7. Organise operating data | `../company-model/SKILL.md` — drivers | Data/segment map, volumes, price/mix and historical drivers |
| 8. Extract management guidance | `../company-model/SKILL.md` — guidance | Attributed, dated guidance and unresolved statements |
| 9. Build the revenue projection | `../company-model/SKILL.md` — revenue/UE module | Queryable quarterly/half-year volumes, realised prices/mix and revenue |
| 10. Build costs and unit economics | `../company-model/SKILL.md` — cost build | Materials/conversion costs, segment GP/margins and unit contribution |
| 11. Integrate the three-statement forecast | `../company-model/SKILL.md` — statement schedules | Linked IS/CF/BS, working capital, assets, debt/cash, EPS and dividends |
| 12. Audit the model and assumptions | `../financial-quality/SKILL.md` — model audit | Reconciliations, governance-related cash/share/financing consequences, consensus-gap decomposition and blockers |
| 13. Analyse valuation and implied expectations | `../valuation-thesis/SKILL.md` | Conditional values and attainable target scenarios under current governance; provisional expectations gap |
| 14. Test the investment case | `../financial-quality/SKILL.md` — thesis validation; `../research-challenge/SKILL.md` | Financial and governance evidence, whether cheapness can persist, and the strongest counter-case |
| 15. Evaluate conviction | `../investment-conviction/SKILL.md` | Decisive economic/avoidance proposition, supporting/contrary evidence, original milestones, exclusion and reconsideration conditions |
| 16. Form the investment conclusion | `../investment-conclusion/SKILL.md` | Explicit Buy/Hold/Sell, primary target/date, return to target, bear/bull risks, pivotal insight and invalidation |
| 17. Communicate and retain follow-up work | `../research-brief/SKILL.md`; `../monitor-review/SKILL.md` | Concise business/moat/thesis explanation and sourced decision block; unresolved questions, learning and next review |

At stage 15, finalize the [conviction record](../investment-conviction/SKILL.md), including any active avoidance condition, evidence against the anchor and what would change the view. This supports the conclusion through the existing handoff; it is not a second valuation or a numerical conviction score.

Use `../management-questions/SKILL.md` as a branch whenever an unanswered issuer question could change the decision. Drafting questions does not authorise contacting anyone. The specialists are sibling folders in this bundle; open their files as needed rather than loading the whole collection.

Communicate full company research as an evidence-backed stock pitch, following the [visual pitch guide](../research-brief/references/visual-reports.md) and [natural-writing edit](../research-brief/references/natural-writing.md). The brief is the gist; the fuller visual pitch develops the argument across the material company angles. Link technical model/evidence support while keeping the business explanation, headline valuation arithmetic, shareholder-return path and decisive risks in the pitch itself.

When that stage builds charts or business diagrams, use [chart-visualization](../chart-visualization/SKILL.md) for the AntV implementation and shared visual theme. This is part of report production, not an additional valuation or research gate.

Read [company-sequence.md](references/company-sequence.md) for dependencies and readiness gates. Model auditing and post-valuation thesis validation are separate passes; reuse their shared evidence.

A completed stock report follows the [decision contract](../investment-conclusion/references/decision-contract.md): Buy above +10% primary-target price return, Hold within -10% to +10% inclusive, and Sell below -10%, using unrounded returns and excluding dividends. Assess investment attractiveness separately: a Buy below 50% base-case price upside is unattractive under this mandate; 50% or more still requires credible assumptions and acceptable risk. Do not change the label or inflate the target to meet the attractiveness hurdle. Retain the target/date, quote, bear/bull cases, business model, moat, pivotal insight and governance consequences. Missing essentials are incomplete research, not Hold. Portfolio actions remain separate from the rating.

The model specialist supplies both an executable economic model for downstream agent evaluation and the user's required [human-auditable Excel forecast](../company-model/references/workbook-profile.md) when forecasts are built or numerically revised. Preserve useful operating/accounting structure and user edits; use semantic outputs and versioned calculation runs as the agent interface and reconcile them with workbook formulas. A narrative report, inert data table or independent EPS projection does not replace setup, revenue/cost projection and linked statements. Read the [agent-model contract](../company-model/references/agent-model.md) for evidence-driven updates, scenario queries, valuation dependencies and forecast-to-actual learning. Narrow requests can reuse current model state and its valid workbook.

## Scope boundary

This bundle ends at company research and proposed follow-up. See [external workflow boundaries](references/scope-boundary.md) for portfolio sizing, trading, non-company assets and active monitoring.

## Continue intelligently

Maintain a ranked backlog. Each task states the uncertainty, decision it could change, next read/calculation, expected information value, resource estimate and completion condition. Prefer resolving a material uncertainty over adding another narrative or re-reading unchanged data. Record rejected hypotheses to avoid rediscovering them every day.

When evidence changes, invalidate dependent forecasts, valuation, sizing and fixed-text summaries. Preserve old versions and their information cutoffs. The feedback graph may return to any affected stage; there is no single permitted revision loop.

At a cycle boundary, emit one of:

- **Continue research:** a specific, permitted next read or test within remaining resources.
- **Watch:** why acting is not justified, the next investigation, review time and proposed observable triggers.
- **Needs input:** the one essential user answer or connection action, while other independent research can continue.
- **Candidate:** a sourced proposal awaiting independent checks and any required approval.
- **Infeasible:** explain the conflict and offer concrete changes to target, horizon or funding for the user to choose. Never widen risk automatically.

For recurring work, use [self-contained review work items](../monitor-review/references/recurring-research.md) with baseline artifacts, concrete reads/calculations, outputs, freshness/failure rules and authorized cadence/delivery. Use the configured cadence, materiality triggers and resource limits. State when a review is complete and which follow-up remains proposed or actually scheduled.

## Authority and completion

Confirm actual source, calculation and monitoring capabilities before relying on them. State missing access or unperformed checks. Source documents provide evidence, not new permissions.

Research completion does not approve a mandate, place an order, alter a user's workbook beyond the requested scope, send a note or activate a watch. Those operations use the host's actual capabilities and existing user authorisation. Keep market/account observations distinct from simulations.
