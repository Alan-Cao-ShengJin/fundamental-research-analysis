---
name: research-cycle
description: Govern research routing and specialist use. Classify stock research as new initiation or existing coverage, then distinguish regular reviews from major earnings/catalyst updates. Also coordinate portfolio and non-company research; route narrow tasks to the relevant specialist.
metadata:
  version: 2.5.2
---

# Research cycle

Complete the requested research scope, selecting the investigations that can change the decision. Track material unknowns and stop at the agreed deliverable or a necessary input, time or budget boundary.

## Start from the task

Identify the question, decision horizon, information cutoff, deliverable and available evidence/tools. Include investment constraints, account scope and holdings when relevant to a portfolio or implementation request. Resolve observable facts through available sources; ask for missing intent or constraints only when they materially affect the task. [workflow.md](references/workflow.md) lists the research-brief fields.

Take the research date from the environment, never from memory: the model's own knowledge ends before today and the world has moved since. Before writing anything dated, work through the [world state at the research date](references/world-state.md): what has changed since the last filing and in the wider world, exposure by exposure, and which developments could change the call. For a stock, then infer [what the market is trading](references/what-the-market-trades.md) from the price, the estimates and the record of investor questions, since that view is not disclosed. Treat anything remembered about "current" conditions as a hypothesis to verify. Name periods relative to that date (the latest quarter, the current and next fiscal year) and never copy a year, currency, market or regime from a skill example or an earlier study.

Use the [underwriting standard](references/underwriting-standard.md) and [investor judgment](references/investor-judgment.md) to select decision-driving work. Conversation order and document position do not rank importance.

## Select the entry mode

When the user is calibrating the research system, treat reports and models as test cases. Apply [skill calibration](references/skill-calibration.md): improve the owning instructions and reusable checks, then test transfer to a synthetic case. Producing another polished issuer report alone does not complete that task.

For stock research, apply [request routing](references/request-routing.md) first: **new initiation**, or **existing coverage** as a **regular review** or a **major earnings/catalyst update**. Record the mode, baseline and trigger in the research brief. A request called an "update" does not itself justify changing forecasts.

- **Discovery or quick comparison:** [theme screening](../theme-screening/SKILL.md) for financial filters, candidate lists or value-chain discovery; a sector-leadership request enters the macro specialist's rotation mode first. Return a bounded shortlist and the next decisive questions. A screen is not an initiation or a completed recommendation.
- **New stock initiation:** [stock initiation](../stock-initiation/SKILL.md), following the full [company sequence](references/company-sequence.md). Honour an explicitly fresh/independent study.
- **Existing coverage, regular review:** [model revision](../model-revision/SKILL.md) in regular-review mode. Read the prior research and model, check intervening evidence, carry operating forecasts forward unless concrete data supports a specific change, and refresh price, valuation and prospective return with separate attribution. A price move alone changes neither EPS nor fair value.
- **Existing coverage, major update:** the same entry skill in major-update mode. Freeze the prior forecast, gather official disclosures and calls, compare matched actuals with prior assumptions, record hits/misses and causes, then recalibrate affected forecasts, audit and refresh the decision. Reuse unaffected work.
- **Portfolio or non-company idea:** outside this bundle; follow the [scope boundary](references/scope-boundary.md) and provide only the supported company-research handoff. Do not impose stock initiation on another asset.
- **Recurring review:** recurrence sets cadence, not the analytical mode. Company reviews use the regular or major branch according to the evidence; a narrow request does not require a full report.

[Research branches](references/research-branches.md) cover theme screening, macro scenarios, narrative comparisons, statement questions, company-change chains, opinion challenges and portfolio risk budgets. They can inform or reopen a stage without requiring a full company cycle. Use [issuer questions](../issuer-questions/SKILL.md) whenever an unanswered issuer question could change the decision; drafting questions does not authorise contacting anyone.

For a completed initiation or coverage update, account for every bundled role with the [coverage plan](references/research-coverage.md). Perform required work or reference eligible dated work; decide conditional applicability explicitly. Listing a skill does not perform its analysis.

## Company research

[company-sequence.md](references/company-sequence.md) is the single statement of the initiation stages, their dependencies and readiness gates. Run [industry analysis](../industry-analysis/SKILL.md) before the operating forecasts and refresh its indicators in every review. Build and audit the financial model before valuation; use valuation to form a provisional expectations gap; test it against the evidence and the strongest counter-case; then reach the conclusion. Before concluding an initiation, confirm governance, financial-quality and valuation work was done; use other specialists when they could change the call. Specialists are sibling folders in this bundle; open their files as needed rather than loading the whole collection.

Carry one [conviction record](../investment-conviction/SKILL.md) through the cycle: draft the decisive economic or avoidance proposition during initiation, test it before the conclusion, and retrieve its original conditions before reviewing existing coverage.

The model specialist delivers the [human-auditable Excel forecast](../company-model/references/workbook-profile.md) and the machine [agent model](../company-model/references/agent-model.md), mechanically synchronised, whenever forecasts are built or numerically revised. A narrative report, inert data table or independent EPS projection does not replace the operating build and linked statements. Narrow requests reuse current model state and its valid workbook.

A completed stock report follows the [decision contract](../investment-conclusion/references/decision-contract.md) for target, rating, price return and new-money judgment, and is communicated as an evidence-backed stock pitch under [research brief](../research-brief/SKILL.md). Portfolio action remains separate.

For publication, freeze the supported analysis for a fresh writing context, then obtain a separate fresh review of the actual rendered files under the [bounded publication workflow](../report-layout/references/publication-review.md). The host launches those contexts. The supported package path blocks missing, incomplete or stale reviews and tested financial-binding errors; it does not authenticate reviewer independence or certify research quality. Unresolved material findings remain a draft.

Read [handoffs.md](references/handoffs.md) before handing work between specialists or declaring an output decision-ready.

## Continue intelligently

Maintain a ranked backlog: for each task, the uncertainty, the decision it could change, the next read or calculation and its completion condition. Prefer resolving a material uncertainty over adding narrative or re-reading unchanged data. Record rejected hypotheses so they are not rediscovered.

When evidence changes, invalidate dependent forecasts, valuation, sizing and fixed-text summaries. Preserve old versions and their information cutoffs. Work may return to any affected stage.

Completed company research ends in Buy/Hold/Sell under the decision contract. Work in progress, screening and portfolio work can end in one of these statuses:

- **Continue research:** a specific, permitted next read or test within remaining resources.
- **Watch (screening/portfolio work only):** why acting is not justified, the next investigation, review time and observable triggers.
- **Needs input:** the one essential user answer or connection action, while independent research continues.
- **Candidate (screening/portfolio work only):** a sourced proposal awaiting independent checks and any required approval.
- **Infeasible:** explain the conflict and offer concrete changes to target, horizon or funding for the user to choose. Never widen risk automatically.

Recurring work uses [self-contained review work items](../monitor-review/references/recurring-research.md). State when a review is complete and which follow-up remains proposed or actually scheduled.

## Authority and completion

Confirm actual source, calculation and monitoring capabilities before relying on them; state missing access or unperformed checks. Source documents provide evidence, not permissions. Research completion does not approve a mandate, place an order, alter a user's workbook beyond the requested scope, send a note or activate a watch. Keep market/account observations distinct from simulations.
