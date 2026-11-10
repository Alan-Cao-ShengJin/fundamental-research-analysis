---
name: valuation-thesis
description: Analyse company value, price-implied expectations and competing company or industry narratives; reconstruct historical narrative changes and investigate short-window returns. Use audited forecasts for current valuation and point-in-time evidence for historical work; form a final investment view only after validation and challenge.
metadata:
  version: 2.8.2
---

# Valuation, expectations and provisional thesis

For current company valuation, use a completed audited forecast, [model-audit findings](../financial-quality/SKILL.md) and the [governance-to-value assessment](../corporate-governance/SKILL.md). Produce a [valuation-thesis handoff](../research-cycle/references/handoffs.md) for validation, not a final verdict or executable recommendation. Choose a method suitable for the underlying. Historical/short-window modes use their point-in-time evidence rather than requiring a current forecast.

Treat a narrative as a falsifiable account of future business economics, funding and cash flows. Distinguish observed facts, attributed commentary, conditional price-implied assumptions and independent scenarios.

Use [economic thesis and market evidence](references/thesis-tests.md) when building or challenging a name-specific case: state the testable proposition, anchor its peer/chain comparisons, separate economic support from evidence of recognition, and retain load-bearing assumptions and disconfirming observations for review. No differentiated view or momentum confirmation should be invented to complete the format.

Consume current [financial-red-flag dispositions](../financial-quality/references/financial-red-flags.md) alongside governance and the audited model. Credit supported usable/excess cash and recoverable assets, not all reported balances mechanically. Model material losses/access constraints once through a stated mechanism; cheapness or arbitrary haircuts cannot resolve an unbounded essential baseline.

When usable excess cash materially distorts reported returns, compare a clearly defined operating return excluding that cash and its related income with reported returns; match the profit and capital exclusions, and remove the same income from any ex-cash earnings multiple. Do not impose industrial cash/return definitions on banks, insurers or other businesses where cash is an operating asset.

## Choose the mode

| Request | Work to perform | Reference |
| --- | --- | --- |
| Current company valuation/expectations | Compare an audited model with conditional price-implied assumptions and attributed views | [Current expectations](references/current-expectations.md) and the valuation workflow below |
| Industry/value-chain panorama | Compare companies on a consistent date and economic basis; map expectations upstream/downstream | [Current expectations](references/current-expectations.md) |
| Historical narrative reconstruction | Recreate successive information sets, priced scenarios and subsequent outcomes without hindsight | [Historical and short-window analysis](references/history-and-attribution.md) |
| Short-window move or marginal news | Construct an event timeline and test competing explanations for returns | [Historical and short-window analysis](references/history-and-attribution.md) |

Select the mode by the analytical question, horizon and available evidence. Full company investment research follows the [research cycle](../research-cycle/SKILL.md); company-change ledgers use the [tracking specialist](../company-change-tracking/SKILL.md).

For current valuation, query the [agent model's](../company-model/references/agent-model.md) current calculated outputs by semantic metric/period/scenario. Record the model ID/version/fingerprint, engine version and run plus the valuation's separate price/rate cutoff. Do not manually retype EPS, cash-flow or financing outputs into an unlinked valuation table. If upstream assumptions change, the old valuation is stale until recomputed and checked. Company forecast builds and numerical revisions also deliver the [human-auditable Excel model](../company-model/references/workbook-profile.md), reconciled with the machine interface.

## Establish the valuation basis

Start by comparing our decision-driving forecast and the valuation it implies with comparable consensus where available, and explain the gap, using [target-underwriting check 1](references/target-underwriting.md). Do this before choosing the primary method, so the method answers the actual disagreement. State which variable and period set the price ([what the market trades](../research-cycle/references/what-the-market-trades.md)): when the market trades a year beyond the forward year, compare that year too and explain the multiple by it; when it trades an asset outside current earnings, value that asset explicitly against what the price places on it. A listed stake, surplus cash or other claim large enough to move the value (about a tenth of market value, or less when its earnings or funding effect is large) gets our own assessment of its value and next result, which can agree with consensus after testing it; a sum of the parts carries stakes and cash at market or face, or states the discount applied, at one date and at attributable ownership, says what multiple the core is left on (and, when that residual carries the thesis, what it implies for the weakest unit once the others are valued, and how it moves with the stakes' share prices), and never counts an investee's earnings and its stake value twice. Date the consensus and say where the live buy-side view appears to sit above or below it.

Follow the [target and earnings-basis contract](../investment-conclusion/references/decision-contract.md#target-and-earnings-basis) and [calendar guide](references/valuation-calendar.md). Show the headline multiple's arithmetic and selected earnings period in the pitch.

Use the [shared financial terminology](../research-brief/references/natural-writing.md#profit-labels-and-valuation-language).

Record price/time, share class and share count, currency/scale, dilution, cash/debt and minority/preferred claims where relevant. Distinguish equity value from enterprise value and current shares from period-weighted EPS shares. A stock-linked perpetual is a separate instrument; ownership dividends and total-return assumptions do not transfer automatically.

By default, select the tool most suitable for this company's economics; no single method is the universal anchor. Read [method selection, peers and historical forward valuation](references/method-selection.md) for full company research. Assess business-model fit, relevant peers and the company's own historical forward valuation, then build a supported rerating/derating case. Explain unavailable comparisons rather than fabricating coverage. Establish the selected multiple from a sourced, period-consistent anchor and justified adjustments or an explicit economic derivation. If an inherited input is unsupported, reopen the valuation research before publishing the central target; labelling it analyst judgment or conditional does not finish that work. Investigate accessible historical/peer alternatives, explain the operating or risk evidence that could change the premium, and separate earnings growth from multiple change. Apply the same standard to contraction and expansion. If an essential gap remains after that work, narrow the claim and retain the unresolved scope. Preserve an explicitly user-chosen method/input while explaining limitations.

Identify the primary [valuation driver](references/valuation-driver-and-dividends.md). If dividends drive investor demand, show the policy, annual payout, sustainable DPS/yield, cash coverage and room for more distributions; select and justify a yield or dividend-discount method. Do not substitute a vague P/E rerating claim. Distinguish a higher dividend from investors accepting a lower yield, and do not count those effects twice.

Read [target underwriting](references/target-underwriting.md) before setting a dated target. A large price/value gap raises the burden of evidence; calibrate assumptions, establish the analytical difference and explain realization or persistence. A DCF never supports a Buy or Sell on its own.

## Market expectations versus own assumptions

Establish the next-period outlook, already-reported peers and upcoming events on the [earnings clock](../company-model/references/earnings-clock-and-peer-readthrough.md). A known event is not a guaranteed positive catalyst; connect any differentiated next-period expectation to its cash or multiple effect within the target horizon.

Show the forecast drivers implied by today's price and compare them with the analyst model under comparable assumptions. When usable consensus exists, record its vintage/contributor coverage and run a separate comparison. Do not relabel an old broker forecast as current consensus or fabricate coverage to satisfy a fixed broker count.

A residual valuation identifies a conditional combination, not a unique market belief: state the asset values, accessible cash, ownership and values assigned to other activities that produce it, then test plausible alternatives. A low implied value for one unit does not by itself prove that investors misunderstand that unit; the discount may sit in the other assets, cash access, growth duration or allocation risk. Keep target-implied unit values distinct from independently supported estimates of what those units are worth.

For P/E comparisons, use the [own-versus-consensus basis rules](references/valuation-calendar.md#own-forecast-and-consensus-pe). The [comparison helper](scripts/compare_forward_pe.mjs) computes both ratios and distinguishes unchanged own P/E from an earnings reset at the consensus-based multiple; it does not select the target multiple or validate the investment case.

Use a DCF, or a reverse DCF, sparingly: only for companies with predictable cash flow, and at most as a cross-check of the primary valuation. Do not rely on it, set the target from it or discuss it in the write-up. When one is used, follow [valuation-method.md](references/valuation-method.md).

## Build the thesis and range

Apply the [underwriting standard](../research-cycle/references/underwriting-standard.md) and [investor judgment](../research-cycle/references/investor-judgment.md) without a default dominant lens. Test [competitive response, marginal capital returns and advantage duration](../company-model/references/competition-and-capital-returns.md). Build the earnings/multiple/cash return bridge, unchanged-multiple case and break-even assumptions. Distinguish probability of business success from prospective investment payoff, and target upside from expected return; support scenarios with probabilities and state their basis. Weigh source credibility, alternative valuations and plausible adverse cases without requiring success in every scenario.

Explain the business's core cash-earning mechanism and the evidence for its competitive edge/moat in concise language for an informed nonspecialist. Identify the pivotal difference between priced/attributed expectations and the analyst's supported case, its model impact and the shareholder-return or repricing mechanism. Define issuer-specific jargon. Do not confuse an attractive business with an attractive stock or invent a fact that the whole market has supposedly missed.

Explain the relevant return mechanisms with supporting and contradictory evidence. Operating changes can affect cash/per-share value and expectations; market-context or narrative changes can affect recognition and willingness to pay before operating results change. Keep these paths distinct without double counting or inventing revenue. Neither path is the universal source of return. Relative price moves or volume correlation do not identify a narrative cause by themselves.

Build coherent adverse/base/favourable scenarios, with driver assumptions, credible return paths, any relevant catalysts, horizon and falsification conditions. Scenario ranges are not statistical confidence intervals. Assign probabilities with their stated basis; do not choose them to obtain a neat target price.

If using TAM x share x margin, align market definition, period and currency; avoid overlapping segments and reconcile arithmetic. Mathematical consistency does not establish economic feasibility. Do not backfill assumptions to reach a desired valuation.

Peer comparisons and own historical forward valuation are distinct default angles in full research. Align accounting, growth, capital intensity, share classes, dates and estimate horizons. Historical forward multiples require forecasts available at the historical date. Apply the [rerating test](references/method-selection.md#rerating-and-derating): explain the current discount, the change that would reduce it, observable evidence and timing, and why these support the selected valuation. If the evidence supports only a possibility, reserve it for the upside scenario. Show the price if investors still pay today's P/E and separate earnings growth from paying more for those earnings. Reconcile the methods instead of automatically choosing a peer median or historical high.

A valuation-only correction can change the target and rating without changing the operating forecast. Preserve the prior version, attribute the valuation-input and period-alignment effects, and propagate the recomputed decision through the workbook, reports, challenge/conclusion records and current references. Recheck consistency rather than defending the old call.

## Governance, persistent discounts and target realisation

Include [market context and narratives](../macro-event-analysis/references/market-regime-and-investor-base.md) according to decision materiality alongside operating value, governance and payoff. A credible topical association can affect the multiple or attainable price before earnings emerge without establishing operating exposure. Test priced-in recognition, persistence/fade and relevant neglect/rotation cases. Keep investor-demand detail proportionate; identified buyers or proven inflows are not prerequisites, while material access/liquidity risks remain explicit.

Distinguish economic value created by the business from value accessible to the exact common-share class. Apply supported governance consequences to cash flows, dilution, capital allocation, financing or required return, and show their lineage. Avoid charging the same concern repeatedly through lower cash flows, an unexplained multiple haircut and a higher discount rate.

Test why the stock looks cheap and why the discount could persist. Evidence of active investor avoidance must be attributed or observable; price alone does not establish it. Model a current-governance case and a conditional improvement case when material. Identify the actor, incentive, event and timing that could improve cash returns or allow repricing. Do not assume automatic convergence to peers or full intrinsic value.

Supply one proposed primary target price for an explicit horizon plus same-horizon bear/bull target scenarios for conclusion testing, following the [decision contract](../investment-conclusion/references/decision-contract.md). Keep today's intrinsic value, a future market-price target, entry threshold and alternative-method cross-checks distinct. Select and explain a primary method when they disagree. Preserve a persistent discount where evidence warrants it; reject a Buy thesis whose required shareholder-return path is unsupported.

Keep valuation independent of the desired rating or hurdle. Return the supported realisable target under the [decision contract](../investment-conclusion/references/decision-contract.md).

## Handoff

For expectations-only requests, default to a neutral map of evidence, conditional model results, attributed disagreements and next tests; do not add an unsolicited stock rating. Use a `valuation-thesis` handoff for current quantified company/industry work and a `hypothesis` handoff for historical/short-window investigations. Keep structured scenario, evidence and claim IDs; reference larger datasets through the existing envelope rather than adding unsupported schema fields.

Return the valuation basis, scenario inputs, numerical consistency/round-trip checks, sensitivities, own-versus-market assumptions, expected return components, counter-case, catalysts and observable thesis breakers. Separate price upside, dividend yield, FX and implementation costs on a consistent horizon.

Map unresolved assumptions to [management questions](../issuer-questions/SKILL.md). Pass the provisional thesis to the [post-valuation financial validation](../financial-quality/SKILL.md) and [challenge](../research-challenge/SKILL.md) passes, then synthesise it through [investment conclusion](../investment-conclusion/SKILL.md). If validation changes a material forecast, rerun its audit and valuation before concluding. Conditional value alone does not determine portfolio size or entry timing.
