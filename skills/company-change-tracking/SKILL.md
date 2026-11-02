---
name: company-change-tracking
description: Maintain a sourced comparison chain for changes in a listed company's investment drivers, separating realised changes from surprises and linking evidence to affected model assumptions. Use for company updates, inflection-point tracking and recurring thesis reviews.
metadata:
  version: 2.0.0
---

# Company change tracking

Track a specified company/ticker and thesis driver, such as order conversion, capacity utilisation, overseas mix or product pricing. Use the requested time window and sources; otherwise state the review cutoff and coverage. Load the prior evidence ledger, frozen expectations and current model version when available.

## Build the comparison chain

Give each observation a stable record ID. Store the economic observation period/event time separately from disclosure and retrieval times. Link each change to the preceding comparable record ID and source. The initial observation is explicitly `first record`; an absent baseline is `baseline unavailable`, never an invented improvement.

Compare the same metric, period basis, currency, segment, reporting perimeter and adjusted/reported definition. For restatements retain both vintages and bridge them; a correction is not a new operating improvement. Preserve raw observations separately from calculations and interpretation.

Use announcements, filings, attributable meeting notes and authorised private sources where available. State access gaps. A sell-side summary repeating the issuer does not independently confirm the issuer's claim.

## Separate change from surprise

Use the [earnings clock](../company-model/references/earnings-clock-and-peer-readthrough.md) to distinguish latest results, forward expectations, intervening updates and upcoming catalysts. Preserve the pre-event baseline before recording a surprise or changing the model. Earlier-reporting peer evidence can inform the next target period only when available at the cutoff and economically comparable; distinguish a common industry change from share/issuer-specific effects. Label estimated event dates and stale or superseded guidance.

Track material [investor-base and regime changes](../macro-event-analysis/references/market-regime-and-investor-base.md) separately from operating changes: eligibility/rebalance announcements and effective dates, free-float/lockup/issuance changes, documented ownership/flow changes and liquidity/sector rotation. Distinguish newly eligible from newly buying, holdings from live flows and price response from causal proof. Reopen the realization scenario even when the operating forecast is unchanged; preserve former expectations and source lags.

Record previous value, current value, absolute/relative change where meaningful, and whether the change is favourable, adverse, mixed or unchanged for the specified thesis. Increasing costs can be adverse even when the number increases. `In line with expectations` requires a dated expectation baseline available before the observation; without it, surprise is `unknown`.

Keep cause as reported explanation or analyst inference, with evidence and alternatives. A price move is a separate observation; it does not prove a fundamental change or its cause.

## Output and model impact

| Record ID | Disclosure date / observation period | Driver | Direction / surprise | Previous → current | Explanation | Source IDs | Prior record ID | Model/decision impact |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Keep the table backed by append-only, versioned structured records. Each material record identifies the semantic model node/metric and period, prior model version, proposed assumption revision, confidence and unresolved comparability issue. Narrative-only evidence may have no numerical model mapping; retain that limitation rather than inventing a number.

Pass supported changes into [model revision](../model-revision/SKILL.md) when an existing financial model or decision needs updating; the [company model](../company-model/references/agent-model.md) supplies calculations. Change tracking can end with an evidence ledger when no model revision is requested or supported. Preserve the original forecast for later matched forecast-to-actual evaluation. For suspected accounting explanations, invoke [financial quality](../financial-quality/SKILL.md).

Return a `monitor-review` [handoff](../research-cycle/references/handoffs.md) with ledger location, material changes, dependency versions and next tests. Use [monitor review](../monitor-review/SKILL.md) to define cadence and watch status. This skill performs a scoped review; it does not activate continuous monitoring. Short-window return attribution uses the historical mode of [valuation and narrative analysis](../valuation-thesis/SKILL.md).
