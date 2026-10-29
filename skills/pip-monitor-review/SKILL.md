---
name: pip-monitor-review
description: Convert research decisions into explicit watch specifications and scheduled reviews, distinguish active monitoring from plans, and update theses and portfolio decisions from new evidence and outcome attribution.
metadata:
  version: 1.13.0
---

# Monitor, review and learn

Load the decision version, prior assumptions/review and relevant evidence. Include positions, constraints and monitoring acknowledgements when the task concerns an account or an existing watch. Keep actual, simulated and proposed positions separate. Follow the [shared handoff contract](../pip-research-cycle/references/handoffs.md).

## Specify meaningful watches

For earnings-related reviews, maintain the [earnings and peer-event clock](../pip-company-model/references/earnings-clock-and-peer-readthrough.md): issuer release/call/transcript availability, earlier peer calls, intervening updates and next catalysts. Keep confirmed versus estimated dates, timezones, postponements and data freshness separate. Freeze pre-event expectations and schedule a proposed recheck when new information can change the thesis; this does not itself activate a monitor.

Where material, specify [market-context and investor-base triggers](../pip-macro-event-analysis/references/market-regime-and-investor-base.md): macro/sector rotation, documented flow/ownership change, normal and stressed turnover, eligibility/review/effective dates, float/lockup/issuance supply and buyer-capacity changes. Distinguish a rules threshold approached, an announced change and completed buying; record lag/coverage and what reopens valuation versus operating assumptions. These remain planned unless an actual monitoring service acknowledges them.

For each proposed watch, define the underlying decision/thesis, source and exact metric/contract, baseline, threshold/operator/unit, observation cadence, data-freshness limit, expiry/review date, materiality, deduplication/cooldown and the action a change would trigger. Include data/feed/worker health and missing updates, not just market direction.

Examples to adapt: a forecast driver breaches the thesis range; net carry changes enough to invalidate a trade; a hedge ratio/regime changes materially; liquidity deteriorates; a margin/oracle/contract setting changes; a withdrawal deadline approaches; required data becomes stale. A price change need not be a thesis change.

Distinguish **planned**, **active**, **triggered**, **expired**, **disabled** and **health-unknown**. Only a real reviewed monitoring service can return the acknowledgement that makes a watch active. A skill-generated condition, a CLI printout or a saved schedule is not evidence of real-time observation or notification delivery.

When relevant, retain [red-flag issue IDs](../pip-financial-quality/references/financial-red-flags.md) and observable follow-ups such as subsequent collection/payment, new cash restrictions, guarantees/related-party transfers, audit opinion/scope changes, resignations, filing delays, inquiry outcomes, remediation and defaults. Specify which evidence would resolve or worsen the issue and reopen affected model/value claims. Preserve prior unresolved findings across updates; wording changes or a rising share price do not resolve them. These remain proposed watches until acknowledged by a real service.

## Separate observation from reasoning

Reassess [odds versus payoffs](../pip-research-cycle/references/investor-judgment.md#separate-probability-of-success-from-the-payoff-at-the-price) when prices or regimes change. Repeated wins can coexist with deteriorating prospective value after a rally; one loss need not invalidate a sound process. Separate new operating evidence from changed price, valuation, liquidity and loss severity. Preserve the original decision to evaluate the reasoning across outcomes rather than grading it solely by the latest win or miss.

Use deterministic refresh and alert rules for frequent observations. Run research reasoning at the configured cadence or for a supported material event, within the available budget. Distinguish observation from analysis and report coverage or health gaps explicitly.

At a review, check freshness and health first. Refresh affected evidence; classify what changed; update dependencies and recompute the relevant model, strategy costs or portfolio risk. Ask for approval only when the actual mandate/action requires it, not for each ordinary research step.

For companies use the [executable model](../pip-company-model/references/agent-model.md): map observations to semantic driver/period IDs, create a new evidence/model vintage, run affected calculations and refresh dependent valuation/conclusion versions. Retrieve the relevant outputs and lineage rather than requiring a human to reread a workbook or report. An Excel backend is acceptable when supported; machine-consumable state and actual recalculation still matter.

Use [company change tracking](../pip-company-change-tracking/SKILL.md) when a comparable disclosure chain is needed, [macro event analysis](../pip-macro-event-analysis/SKILL.md) for material external shocks. Short-window return explanations can use the historical mode of [valuation and narrative analysis](../pip-valuation-thesis/SKILL.md), keeping attribution uncertainty distinct from an observed model-driver change.

If a dependency fails, record its scope, last successful observation and the next recovery task. Do not conclude a portfolio is safe from silence. Time-sensitive pending approvals/candidates expire or require rechecking when their evidence or mandate changes.

## Learn without hindsight

Use [empirical research and validation](../pip-research-cycle/references/empirical-research-and-validation.md) and [investor judgment](../pip-research-cycle/references/investor-judgment.md) to retain reusable cases, source-specific guidance/delivery patterns and proxy calibration. Include failures and unresolved observations; separate execution from expectation-setting and external shocks. Apply the shared materiality principle when selecting review work, without promoting the latest market narrative over other drivers. Store case facts in versioned research artifacts, not generic skills, and do not imply a library or evaluation service is running merely because a specification exists.

Record the original prediction/assumption, its information cutoff, metric/horizon and what would count as success or failure. At the relevant date compare actual evidence with the original version, not a rewritten thesis. Label unobservable or unresolved outcomes rather than manufacture a score.

Preserve the model/engine/scenario/run that generated each forecast. Match later actuals for period, currency, perimeter, segment and adjusted/reported definition before scoring. Attribute supported forecast and valuation errors to drivers, costs, reinvestment, accounting/data and market assumptions. Keep unidentifiable contributions unresolved. Use this evidence to update the model and research priorities, without treating one outcome as proven predictive performance.

Attribute paper/actual outcomes separately. Distinguish cash flows, realised/unrealised P&L, market/factor exposure, selection, sizing, timing, fees/funding, FX and data/execution problems where the evidence permits. Use a consistent benchmark and capital basis; paper fills do not establish live fill quality.

Update confidence and research priorities in proportion to evidence and sample size. Do not optimise rules on the same evaluation window and call the result independent validation. Retire repeatedly failed hypotheses, record why, and preserve their history.

## Handoff

Return relevant monitoring status/health, material changes, affected artifact versions, decision implications, outcome attribution and the next useful review or investigation. A no-action finding does not imply that continuous monitoring has been activated.
