---
name: pip-valuation-thesis
description: Analyse company value, price-implied expectations and competing company or industry narratives; reconstruct historical narrative changes and investigate short-window returns. Use audited forecasts for current valuation and point-in-time evidence for historical work; form a final investment view only after validation and challenge.
metadata:
  version: 1.16.0
---

# Valuation, expectations and provisional thesis

For current company valuation, use a completed audited forecast, [model-audit findings](../pip-financial-quality/SKILL.md) and the [governance-to-value assessment](../pip-corporate-governance/SKILL.md). Produce a [valuation-thesis handoff](../pip-research-cycle/references/handoffs.md) for validation, not a final verdict or executable recommendation. Choose a method suitable for the underlying. Historical/short-window modes use their point-in-time evidence rather than requiring a current forecast.

Treat a narrative as a falsifiable account of future business economics, funding and cash flows. Distinguish observed facts, attributed commentary, conditional price-implied assumptions and independent scenarios.

Consume current [financial-red-flag dispositions](../pip-financial-quality/references/financial-red-flags.md) alongside governance and the audited model. Credit supported usable/excess cash and recoverable assets, not all reported balances mechanically. Model material losses/access constraints once through a stated mechanism; cheapness or arbitrary haircuts cannot resolve an unbounded essential baseline.

## Choose the mode

| Request | Work to perform | Reference |
| --- | --- | --- |
| Current company valuation/expectations | Compare an audited model with conditional price-implied assumptions and attributed views | [Current expectations](references/current-expectations.md) and the valuation workflow below |
| Industry/value-chain panorama | Compare companies on a consistent date and economic basis; map expectations upstream/downstream | [Current expectations](references/current-expectations.md) |
| Historical narrative reconstruction | Recreate successive information sets, priced scenarios and subsequent outcomes without hindsight | [Historical and short-window analysis](references/history-and-attribution.md) |
| Short-window move or marginal news | Construct an event timeline and test competing explanations for returns | [Historical and short-window analysis](references/history-and-attribution.md) |

Select the mode by the analytical question, horizon and available evidence. Full company investment research follows the [research cycle](../pip-research-cycle/SKILL.md); company-change ledgers use the [tracking specialist](../pip-company-change-tracking/SKILL.md).

For current valuation, query the [agent model's](../pip-company-model/references/agent-model.md) current calculated outputs by semantic metric/period/scenario. Record the model ID/version/fingerprint, engine version and run plus the valuation's separate price/rate cutoff. Do not manually retype EPS, cash-flow or financing outputs into an unlinked valuation table. If upstream assumptions change, the old valuation is stale until recomputed and checked. Missing essential model outputs make reverse valuation partial; a qualitative narrative map can still be useful. A readable Excel/report view is optional; the executable connection to the business model is essential.

## Establish the valuation basis

Record price/time, share class and share count, currency/scale, dilution, cash/debt and minority/preferred claims where relevant. Distinguish equity value from enterprise value and current shares from period-weighted EPS shares. A stock-linked perpetual is a separate instrument; ownership dividends and total-return assumptions do not transfer automatically.

By default, select the tool most suitable for this company's economics; no single method is the universal anchor. Read [method selection, peers and historical forward valuation](references/method-selection.md) for full company research. Assess business-model fit, relevant peers and the company's own historical forward valuation, then build a supported rerating/derating case. Explain unavailable comparisons rather than fabricating coverage. Preserve an explicitly user-chosen method/input while explaining limitations.

## Market expectations versus own assumptions

Use the [earnings clock and peer read-throughs](../pip-company-model/references/earnings-clock-and-peer-readthrough.md) to establish time since results/call, the next-period outlook, relevant peers already reported and upcoming catalysts with confirmed/estimated dates. Compare pre-event expectations, subsequent evidence and price/benchmark reaction without claiming price proves complete information absorption. A known event is not a guaranteed positive catalyst; connect differentiated next-period expectations to cash/multiple effects and the chosen target horizon.

Show the forecast drivers implied by today's price and compare them with the analyst model under comparable assumptions. When usable consensus exists, record its vintage/contributor coverage and run a separate comparison. Do not relabel an old broker forecast as current consensus or fabricate coverage to satisfy a fixed broker count.

Reverse DCF is a conditional consistency calculation: many combinations of growth, margin, reinvestment and discount rate can explain a price. It is not a uniquely observed market belief. Read [valuation-method.md](references/valuation-method.md) before using the included FCFE calculator.

Cash flows and discount rates must match. Distinguish net income, FCFE and FCFF; reconcile reinvestment, working capital, financing and dilution. A net-income-as-cash-flow approximation requires explicit justification and sensitivity. Do not fix a weak cash-conversion model by an arbitrary qualitative adjustment to terminal profit.

Use an explicit fiscal anchor and economically justified transition/steady-state horizon. Select discount-rate and terminal-growth scenarios from the business, currency and financing assumptions. Explain terminal reinvestment and require a mathematically valid rate/growth relationship.

## Build the thesis and range

Apply the [underwriting standard](../pip-research-cycle/references/underwriting-standard.md) and [investor judgment](../pip-research-cycle/references/investor-judgment.md) without a default dominant lens. Test [competitive response, marginal capital returns and advantage duration](../pip-company-model/references/competition-and-capital-returns.md), coherent reinvestment/fade and material terminal-value dependence. Build the earnings/multiple/cash return bridge, unchanged-multiple case and break-even assumptions. Distinguish probability of business success from prospective investment payoff, and target upside from expected return; use numerical weights only when defensible. Weigh source credibility, alternative valuations and plausible adverse cases without requiring success in every scenario.

Explain the business's core cash-earning mechanism and the evidence for its competitive edge/moat in concise language for an informed nonspecialist. Identify the pivotal difference between priced/attributed expectations and the analyst's supported case, its model impact and the shareholder-return or repricing mechanism. Define issuer-specific jargon. Do not confuse an attractive business with an attractive stock or invent a fact that the whole market has supposedly missed.

Explain the relevant return mechanisms with supporting and contradictory evidence. Operating changes can affect cash/per-share value and expectations; market-context or narrative changes can affect recognition and willingness to pay before operating results change. Keep these paths distinct without double counting or inventing revenue. Neither path is the universal source of return. Relative price moves or volume correlation do not identify a narrative cause by themselves.

Build coherent adverse/base/favourable scenarios, with driver assumptions, catalysts, horizon and falsification conditions. Scenario ranges are not statistical confidence intervals. Use probabilities only if their basis is defensible and labelled; do not invent precise probabilities to obtain a neat target price.

If using TAM x share x margin, align market definition, period and currency; avoid overlapping segments and reconcile arithmetic. Mathematical consistency does not establish economic feasibility. Do not backfill assumptions to reach a desired valuation.

Peer comparisons and own historical forward valuation are distinct default angles in full research. Align accounting, growth, capital intensity, share classes, dates and estimate horizons. Historical forward multiples require forecasts available at the historical date. Explain why the target multiple could change, test no rerating/derating, and separate earnings growth from multiple expansion. Reconcile these angles with the most suitable primary method rather than automatically choosing DCF, a peer median or a historical high.

## Governance, persistent discounts and target realisation

Include [market context and narratives](../pip-macro-event-analysis/references/market-regime-and-investor-base.md) according to decision materiality alongside operating value, governance and payoff. A credible topical association can affect the multiple or attainable price before earnings emerge without establishing operating exposure. Test priced-in recognition, persistence/fade and relevant neglect/rotation cases. Keep investor-demand detail proportionate; identified buyers or proven inflows are not prerequisites, while material access/liquidity risks remain explicit.

Distinguish economic value created by the business from value accessible to the exact common-share class. Apply supported governance consequences to cash flows, dilution, capital allocation, financing or required return, and show their lineage. Avoid charging the same concern repeatedly through lower cash flows, an unexplained multiple haircut and a higher discount rate.

Test why the stock looks cheap and why the discount could persist. Evidence of active investor avoidance must be attributed or observable; price alone does not establish it. Model a current-governance case and a conditional improvement case when material. Identify the actor, incentive, event and timing that could improve cash returns or allow repricing. Do not assume automatic convergence to peers or full intrinsic value.

Supply one proposed primary target price for an explicit horizon plus same-horizon bear/bull target scenarios for conclusion testing, following the [decision contract](../pip-investment-conclusion/references/decision-contract.md). Keep today's intrinsic value, a future market-price target, entry threshold and alternative-method cross-checks distinct. Select and explain a primary method when they disagree. Preserve a persistent discount where evidence warrants it; reject a Buy thesis whose required shareholder-return path is unsupported.

## Handoff

For expectations-only requests, default to a neutral map of evidence, conditional model results, attributed disagreements and next tests; do not add an unsolicited stock rating. Use a `valuation-thesis` handoff for current quantified company/industry work and a `hypothesis` handoff for historical/short-window investigations. Keep structured scenario, evidence and claim IDs; reference larger datasets through the existing envelope rather than adding unsupported schema fields.

Return the valuation basis, scenario inputs, numerical consistency/round-trip checks, sensitivities, own-versus-market assumptions, expected return components, counter-case, catalysts and observable thesis breakers. Separate price upside, dividends, FX and implementation costs on a consistent horizon; avoid double counting distributions already included in a total-return assumption.

Map unresolved assumptions to [management questions](../pip-management-questions/SKILL.md). Pass the provisional thesis to the [post-valuation financial validation](../pip-financial-quality/SKILL.md) and [challenge](../pip-research-challenge/SKILL.md) passes, then synthesise it through [investment conclusion](../pip-investment-conclusion/SKILL.md). If validation changes a material forecast, rerun its audit and valuation before concluding. Conditional value alone does not determine portfolio size or entry timing.
