---
name: monitor-review
description: Convert research decisions into explicit watch specifications and scheduled reviews, distinguish active monitoring from plans, and update theses and portfolio decisions from new evidence and outcome attribution.
metadata:
  version: 2.1.0
---

# Monitor, review and learn

Load the decision version, prior assumptions/review and relevant evidence. Include positions, constraints and monitoring acknowledgements when the task concerns an account or an existing watch. Keep actual, simulated and proposed positions separate. Follow the [shared handoff contract](../research-cycle/references/handoffs.md).

Use [investment conviction](../investment-conviction/SKILL.md) to preserve the decisive proposition and active exclusions across reviews.

Use [durable recurring research](references/recurring-research.md) when retaining a work item or preparing a recurring review. Make the instruction self-contained for a fresh session, with baseline locations/versions, exact work, outputs, freshness/failure rules, cadence/timezone when authorized and delivery conditions. Keep the canonical task separate from dated runs; verify actual scheduling and delivery state rather than treating a saved file as an active job.

## Specify meaningful watches

For earnings-related reviews, maintain the [earnings and peer-event clock](../company-model/references/earnings-clock-and-peer-readthrough.md): issuer release/call/transcript availability, earlier peer calls, intervening updates and next catalysts. Keep confirmed versus estimated dates, timezones, postponements and data freshness separate. Freeze pre-event expectations and schedule a proposed recheck when new information can change the thesis; this does not itself activate a monitor.

Where material, specify [market-context and investor-base triggers](../macro-event-analysis/references/market-regime-and-investor-base.md): macro/sector rotation, documented flow/ownership change, normal and stressed turnover, eligibility/review/effective dates, float/lockup/issuance supply and buyer-capacity changes. Distinguish a rules threshold approached, an announced change and completed buying; record lag/coverage and what reopens valuation versus operating assumptions.

For each watch, state the metric, threshold, source, review date and what a change would affect. Check data health before interpreting silence.

Examples to adapt: a forecast driver breaches the thesis range; net carry changes enough to invalidate a trade; a hedge ratio/regime changes materially; liquidity deteriorates; a margin/oracle/contract setting changes; a withdrawal deadline approaches; required data becomes stale. A price change need not be a thesis change.

A saved condition or schedule is a plan. Call it active only after the actual monitoring service acknowledges activation; retain that acknowledgement with the watch.

When relevant, retain [red-flag issue IDs](../financial-quality/references/financial-red-flags.md) and observable follow-ups such as subsequent collection/payment, new cash restrictions, guarantees/related-party transfers, audit opinion/scope changes, resignations, filing delays, inquiry outcomes, remediation and defaults. Specify which evidence would resolve or worsen the issue and reopen affected model/value claims. Preserve prior unresolved findings across updates; wording changes or a rising share price do not resolve them.

## Separate observation from reasoning

Reassess [odds versus payoffs](../research-cycle/references/investor-judgment.md#separate-probability-of-success-from-the-payoff-at-the-price) when prices or regimes change. Repeated wins can coexist with deteriorating prospective value after a rally; one loss need not invalidate a sound process. Separate new operating evidence from changed price, valuation, liquidity and loss severity. Preserve the original decision to evaluate the reasoning across outcomes rather than grading it solely by the latest win or miss.

Use deterministic refresh and alert rules for frequent observations. Run research reasoning at the configured cadence or for a supported material event, within the available budget. Distinguish observation from analysis and report coverage or health gaps explicitly.

At a review, check freshness and health first. Refresh affected evidence; classify what changed; update dependencies and recompute the relevant model, strategy costs or portfolio risk. Ask for approval only when the actual mandate/action requires it, not for each ordinary research step.

For companies apply [request routing](../research-cycle/references/request-routing.md) first. A regular review retains operating forecasts unless concrete data supports change; refresh valuation/return using the existing valid model. Major earnings/catalyst evidence requires frozen forecast evaluation and recalibration of affected drivers. When modeling changes, use the [executable model](../company-model/references/agent-model.md): map observations to semantic driver/period IDs, create a new model vintage, run affected calculations and refresh dependent valuation/conclusion versions. Retain a review/evidence vintage without manufacturing a new forecast vintage for a price-only review. Retrieve outputs and lineage alongside the human-auditable model; an Excel backend is acceptable when supported and actually recalculated.

Use [company change tracking](../company-change-tracking/SKILL.md) when a comparable disclosure chain is needed, [macro event analysis](../macro-event-analysis/SKILL.md) for material external shocks, and [risk budgets (external workflow)](../research-cycle/references/scope-boundary.md) for supported portfolio covariance reviews. Short-window return explanations can use the historical mode of [valuation and narrative analysis](../valuation-thesis/SKILL.md), keeping attribution uncertainty distinct from an observed model-driver change.

If a dependency fails, record its scope, last successful observation and the next recovery task. Do not conclude a portfolio is safe from silence. Time-sensitive pending approvals/candidates expire or require rechecking when their evidence or mandate changes.

## Learn without hindsight

Use [empirical research and validation](../research-cycle/references/empirical-research-and-validation.md) and [investor judgment](../research-cycle/references/investor-judgment.md) to retain reusable cases, source-specific guidance/delivery patterns and proxy calibration. Include failures and unresolved observations; separate execution from expectation-setting and external shocks. Apply the shared materiality principle when selecting review work, without promoting the latest market narrative over other drivers. Store case facts in versioned research artifacts, not generic skills, and do not imply a library or evaluation service is running merely because a specification exists.

Record the original prediction/assumption, its information cutoff, metric/horizon and what would count as success or failure. At the relevant date compare actual evidence with the original version, not a rewritten thesis. Label unobservable or unresolved outcomes rather than manufacture a score.

Preserve the model/engine/scenario/run that generated each forecast. Match later actuals for period, currency, perimeter, segment and adjusted/reported definition before scoring. Attribute supported forecast and valuation errors to drivers, costs, reinvestment, accounting/data and market assumptions. Keep unidentifiable contributions unresolved. Use this evidence to update the model and research priorities, without treating one outcome as proven predictive performance.

Attribute paper/actual outcomes separately. Distinguish cash flows, realised/unrealised P&L, market/factor exposure, selection, sizing, timing, fees/funding, FX and data/execution problems where the evidence permits. Use a consistent benchmark and capital basis; paper fills do not establish live fill quality.

Update confidence and research priorities in proportion to evidence and sample size. Do not optimise rules on the same evaluation window and call the result independent validation. Retire repeatedly failed hypotheses, record why, and preserve their history.

## Handoff

Return relevant monitoring status/health, material changes, affected artifact versions, decision implications, outcome attribution and the next useful review or investigation.
