---
name: macro-event-analysis
description: Assess macro regimes and events, sector preferences, topical narratives and their effects on company economics and repricing. Use for policy/rate/geopolitical shocks and company market-context analysis; retain investor access and liquidity as supporting checks when material.
metadata:
  version: 2.1.2
---

# Macro event analysis

Choose the mode: **event analysis** uses the framework below; **current regime/company context** follows [market context, narratives and repricing](references/market-regime-and-investor-base.md) without requiring a discrete shock. Assess relevant macro conditions, sector/style preferences, topical association and what is priced in. Narrative reclassification can affect valuation before earnings emerge. This specialist supplies one dimension of the wider investment assessment, with weight determined by [materiality](../research-cycle/references/underwriting-standard.md#integrate-the-analysis-by-materiality), not conversational recency. Keep investor demand detail proportionate, foreground material access/liquidity findings, and avoid a generic outlook or compulsory buyer map.

Start with the event, information cutoff, relevant geography, assets and horizon. Without a specified geography or asset list, use a global major-asset overview and narrow it by materiality. Distinguish announced, effective, proposed, reversed and hypothetical policy. Verify current event details and market observations using available sources; hypothetical shocks remain scenarios.

For a request about sector leadership or rotation, use the [multi-window rotation procedure](references/market-regime-and-investor-base.md#sector-leadership-and-rotation) before handing selected sectors to screening. It compares leadership, breadth and competing explanations across consistent windows; it does not infer net capital flows from returns or make technical confirmation a condition for fundamental value.

## Six-part analysis

1. **Key variables.** Identify the variables that can materially change the result. Give definition, current reading/date, source, relevant threshold and reason it matters. Separate an economic threshold from an analyst's assumed trigger.
2. **Transmission.** Trace shock → policy/business response → growth/inflation/cash flow or discount rate → asset pricing. Mark direction, horizon, lag, feedback and dampening/amplifying mechanisms. Consider how starting valuations and existing expectations alter the effect. Avoid mechanical claims such as every rate cut helping every equity market.
3. **Historical analogues.** Select comparable episodes by mechanism and initial conditions, including contrary outcomes. Define event timestamp, return windows, instruments, currency, price versus total return and a benchmark. Report data availability and material differences; do not invent returns when historical data is absent.
4. **Scenarios.** Describe a central path and plausible alternatives, using observable conditions and time horizons. Define what favourable/adverse means for the named assets. Probability weights are optional subjective assumptions unless calibrated; explain their basis, sum them to one when used and show sensitivity. Distinguish absolute asset direction from performance relative to a benchmark.
5. **Downstream implications.** Explain which companies, operating drivers or valuation assumptions the macro view changes. Portfolio selection, instrument implementation and position sizing belong to the separate portfolio module; retain the evidence and uncertainty for that handoff without assigning weights here.
6. **Invalidation.** State measurable observations that would break a causal link or change a scenario, with the next review action. Separate thesis invalidation, time expiry and a proposed price stop; a stop does not guarantee an execution price or cap loss through gaps.

## Deliverable and routing

Return a sourced Markdown analysis scaled to the request. Use a transmission diagram and historical comparison chart when they clarify supported data; otherwise a table is sufficient. Include both the strongest opposing mechanism and unresolved questions.

For agents, retain stable scenario/variable IDs, dated observations, causal links with lags and confidence, assumption ranges, affected asset/model metric IDs and observable review conditions in a referenced structured record. Use a `hypothesis` [handoff](../research-cycle/references/handoffs.md).

The standalone event deep dive is an optional branch after evidence intake; a proportionate market-context assessment forms part of full company research. Feed relevant conditions into the [company model](../company-model/SKILL.md) through explicit price, volume, cost, FX and funding assumptions, and investor-demand/discount-rate effects into valuation with separate lineage. Recalculate affected outputs before revising a conclusion. Feed proposed observations into the [company follow-up record](../research-cycle/references/company-follow-up.md). Neither analysis nor proposed observations submit an order or activate a watch.
