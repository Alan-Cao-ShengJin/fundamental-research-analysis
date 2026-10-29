---
name: pip-theme-screening
description: Screen listed companies exposed to an investment theme and map them by value-chain position, with sourced exposure evidence and a research shortlist. Use for thematic idea generation within a specified or context-supported market universe before company modelling.
metadata:
  version: 1.7.0
---

# Theme screening

Turn a theme into a verifiable candidate universe. A thematic connection identifies research candidates; it does not establish earnings sensitivity, attractive valuation or an investment recommendation.

Distinguish verified economic exposure from credible market/narrative association and promotional stretch. A stock can revalue as a market associates it with a hot topic before material earnings are disclosed. Retain that possible price mechanism as a labeled, dated inference without inventing revenue or upgrading the economic exposure rating. Assess why the association matters now, how widely it is recognized, what the price anticipates and whether attention could persist or fade. Investor-cohort detail remains supporting analysis unless decisive.

## Establish the universe and economic mechanism

Establish the theme, market universe and information cutoff from the request or existing research context. If the universe is unclear and materially changes the result, resolve it before screening. Verify current listing identifiers and exchange suffixes. Distinguish issuers, subsidiaries and similarly named businesses.

Map the value chain into useful primary and secondary segments. Explain who pays, what is purchased, which constraint changes and how the theme could affect volume, price, margin or investment. Include adverse effects, substitutes and bottlenecks rather than assuming every supplier benefits.

## Verify each candidate

Use [market regime and investor-base analysis](../pip-macro-event-analysis/references/market-regime-and-investor-base.md) to locate the theme among global sector/style opportunities. Distinguish economic exposure, current attention/sentiment, positioning and documented flows. Note whether a candidate is crowded, overlooked, constrained or simply unverified, with evidence and alternative explanations. Check practical size/liquidity/access for plausible investor cohorts; theme popularity or low coverage alone does not establish attractive return or future discovery.

Prefer filings, company announcements and attributable exchange Q&A for actual exposure. Research notes and commentary can generate leads; trace their material assertions to evidence and distinguish forecasts from realised business. Record disclosure date, evidence location and relevant business metric. Multiple articles repeating one announcement count as one underlying observation.

Use a 1–5 exposure rating when useful: 1 = peripheral connection; 2 = adjacent business; 3 = established related offering; 4 = material disclosed exposure; 5 = central business with strong disclosed concentration. Ratings describe connection strength, not expected return. Unverified claims receive `unknown`. Company enthusiasm without orders or revenue is not evidence of material contribution.

## Return the shortlist

Provide the requested Markdown table:

| Primary segment | Secondary segment | Company | Ticker/exchange | Exposure rating and basis | Inclusion rationale | Latest development/date | Sources | Evidence gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Explain coverage and exclusions briefly. Rank the next investigations by decision relevance and evidence strength; do not rank expected returns without modelling and valuation. A large universe can be investigated in batches; there is no arbitrary company-count limit.

For agent use, retain stable candidate/entity IDs, source/claim IDs, cutoff, exposure metric/period and the next verification task in a referenced structured dataset. Use a `hypothesis` [handoff](../pip-research-cycle/references/handoffs.md); the table is a view of those records.

## Research route

Use after [evidence intake](../pip-evidence-intake/SKILL.md) and before selecting companies for deep research. Selected companies enter [model construction](../pip-company-model/SKILL.md), financial audit, valuation and challenge through the [research cycle](../pip-research-cycle/SKILL.md). For industry expectations comparisons, use the industry mode of [valuation and narrative analysis](../pip-valuation-thesis/SKILL.md) once comparable company models are available.
