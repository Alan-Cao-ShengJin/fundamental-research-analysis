---
name: valuation-thesis
description: Analyse company value, price-implied expectations and competing company or industry narratives; reconstruct historical narrative changes and investigate short-window returns. Use audited forecasts for current valuation and point-in-time evidence for historical work; form a final investment view only after validation and challenge.
metadata:
  version: 2.9.0
---

# Valuation, expectations and provisional thesis

For current company valuation, use a completed audited forecast, [model-audit findings](../financial-quality/SKILL.md) and the [governance-to-value assessment](../corporate-governance/SKILL.md). Produce a [valuation-thesis handoff](../research-cycle/references/handoffs.md) for validation, not a final verdict or executable recommendation. Choose a method suitable for the underlying. Historical/short-window modes use their point-in-time evidence rather than requiring a current forecast.

Treat a narrative as a falsifiable account of future business economics, funding and cash flows. Distinguish observed facts, attributed commentary, conditional price-implied assumptions and independent scenarios.

When a cost of equity or WACC is needed, apply [discount-rate selection](references/discount-rate-selection.md): autonomously retrieve dated inputs, select and justify the method, and link the resulting rate into valuation. Do not ask the user to choose a premium or rate; explicit calculator inputs are resolved by the analyst system, with their evidence and uncertainty retained.

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

## Value the company in six steps

Consensus enters at three points and never while the forecast is being built. Before valuation starts, the [forecast audit](../company-model/references/forecast-audit.md#audit-the-assumption-register) has compared the finished model with dated consensus and explained each material difference; a large gap we cannot explain goes back to the model. Steps 2 and 4 use consensus again.

1. **Name the kind of company and its yardstick.** Use the [yardstick list](references/yardsticks.md): what kind of company this is and how buy-side investors usually value it. Ask whether the market is using that yardstick now or has switched to another. If it has switched, state the belief behind the switch and what the price becomes if the belief fails and the old yardstick returns; that switch is one of the report's debates. Broker notes are evidence of which yardstick is in use; their target prices and target multiples do not set ours. Keep a method or input the user has explicitly chosen, and explain its limits.

2. **Read today's price on that yardstick.** Run the reads in [what the market trades](../research-cycle/references/what-the-market-trades.md) and record three things:
   - **The level.** The yardstick on consensus and on our numbers, for the period investors are looking at: the current year, the next, an out-year or mid-cycle. The market pays price over consensus; the same price over our numbers shows whether the stock looks cheap on the multiple or because our earnings differ.
   - **The comparison.** The stock's own history on the same yardstick and earnings basis, and its closest peers ([bands and peers](references/method-selection.md)).
   - **The reason.** What the market must believe for today's price to be right, and whether a gap to history or peers is temporary (sentiment, a one-off), cyclical (the point in the cycle) or structural (the business has changed).

   Check the consensus date against the latest results and news. After results or a sharp move the price often moves before the estimates; the multiple on consensus then misleads, so say where the live buy-side view appears to sit above or below it. Do not relabel an old broker forecast as current consensus or invent coverage.

3. **Set the target level of the yardstick.** The reason found in step 2 decides it, under the [target-multiple rule](../investment-conclusion/references/decision-contract.md#target-and-earnings-basis):
   - **Temporary gap:** the mean of the stock's own band. No catalyst is needed.
   - **Cyclical gap:** the stock's own band on its through-cycle yardstick (P/B, or the multiple on mid-cycle earnings), not a multiple on peak or trough earnings.
   - **Structural change:** the old band no longer applies. Use the history since the change, or the closest same-market peers of what the business has become.
   - **Above the mean:** only with a significant catalyst. Any level other than the mean, in any case including the bull case, needs the [rerating test](references/method-selection.md#rerating-and-derating).
   - **Cheap against peers but at its own mean:** it can stay cheap. Do not assume it converges.

   For a dividend payer the level is a yield, taken from comparable yield investments its marginal buyers can hold ([dividend valuation](references/valuation-driver-and-dividends.md#comparable-yields-own-band-and-bonds)). If an inherited multiple or yield is unsupported, redo this step before publishing; calling it analyst judgment does not finish the work. If an essential gap remains after that, narrow the claim.

4. **Apply it to our numbers.** `target price = target level × our figure`, for the same period and definition the band was built on: today's forward figure, never rolled forward to the target date ([valuation calendar](references/valuation-calendar.md)). Split the return into our earnings against consensus and the change in the multiple, so optimism is not counted once in above-consensus earnings and again in a re-rating ([own forecast and consensus](references/valuation-calendar.md#own-forecast-and-consensus-pe); the [comparison helper](scripts/compare_forward_pe.mjs) checks the arithmetic). Say how the price reaches the target within twelve months: earnings above expectations, steady growth at a held multiple, or a yield re-rating. A large gap between target and price raises the burden of evidence. Cross-check with a second yardstick from the list, set from its own evidence; a figure backed out of the primary target confirms nothing.

5. **Build the bear and bull cases** on the same horizon. Each is a coherent resolution of the actual debate, or of the main earnings drivers where there is no clear debate, with its effect on valuation, funding, dilution and access to cash where material. Where step 1 found a switched yardstick, the bear case values the stock on the old one. A bear price is not a loss floor: show a more severe plausible outcome separately when the three cases leave out a material tail. If a bear case uses a higher multiple than today's, give the earnings reason; trough earnings can raise P/E while value falls.

6. **Give one primary target and the rating** under the [decision contract](../investment-conclusion/references/decision-contract.md): Buy, Hold or Sell on price return, with dividend yield shown separately.

## Basis and claims

Follow the [target and earnings-basis contract](../investment-conclusion/references/decision-contract.md#target-and-earnings-basis) and [calendar guide](references/valuation-calendar.md). Show the headline multiple's arithmetic and selected earnings period in the pitch. Use the [shared financial terminology](../research-brief/references/natural-writing.md#profit-labels-and-valuation-language).

Record price/time, share class and share count, currency/scale, dilution, cash/debt and minority/preferred claims where relevant. Distinguish equity value from enterprise value and current shares from period-weighted EPS shares.

When the market trades an asset outside current earnings, value that asset explicitly against what the price places on it. A listed stake, surplus cash or other claim large enough to move the value (about a tenth of market value, or less when its earnings or funding effect is large) gets our own assessment of its value and next result, which can agree with consensus after testing it; a sum of the parts carries stakes and cash at market or face, or states the discount applied, at one date and at attributable ownership, says what multiple the core is left on (and, when that residual carries the thesis, what it implies for the weakest unit once the others are valued, and how it moves with the stakes' share prices), and never counts an investee's earnings and its stake value twice.

A residual valuation identifies a conditional combination, not a unique market belief: state the asset values, accessible cash, ownership and values assigned to other activities that produce it, then test plausible alternatives. A low implied value for one unit does not by itself prove that investors misunderstand that unit; the discount may sit in the other assets, cash access, growth duration or allocation risk. Keep target-implied unit values distinct from independently supported estimates of what those units are worth.

Establish the next-period outlook, already-reported peers and upcoming events on the [earnings clock](../company-model/references/earnings-clock-and-peer-readthrough.md). A known event is not a guaranteed positive catalyst; connect any differentiated next-period expectation to its cash or multiple effect within the target horizon.

Use a DCF, or a reverse DCF, sparingly: only for companies with predictable cash flow, and at most as a cross-check of the primary valuation. Do not rely on it, set the target from it or discuss it in the write-up. When one is used, follow [valuation-method.md](references/valuation-method.md).

## Build the thesis and range

Apply the [underwriting standard](../research-cycle/references/underwriting-standard.md) and [investor judgment](../research-cycle/references/investor-judgment.md) without a default dominant lens. Test [competitive response, marginal capital returns and advantage duration](../company-model/references/competition-and-capital-returns.md). Build the earnings/multiple/cash return bridge, unchanged-multiple case and break-even assumptions. Distinguish probability of business success from prospective investment payoff, and target upside from expected return; give scenario probabilities only where there is a basis. Weigh source credibility, alternative valuations and plausible adverse cases without requiring success in every scenario.

Explain the business's core cash-earning mechanism and the evidence for its competitive edge/moat in concise language for an informed nonspecialist. Identify the pivotal difference between priced/attributed expectations and the analyst's supported case, its model impact and the shareholder-return or repricing mechanism. Define issuer-specific jargon. Do not confuse an attractive business with an attractive stock or invent a fact that the whole market has supposedly missed.

Explain the relevant return mechanisms with supporting and contradictory evidence. Operating changes can affect cash/per-share value and expectations; market-context or narrative changes can affect recognition and willingness to pay before operating results change. Keep these paths distinct without double counting or inventing revenue. Neither path is the universal source of return. Relative price moves or volume correlation do not identify a narrative cause by themselves.

Build coherent adverse/base/favourable scenarios, with driver assumptions, credible return paths, any relevant catalysts, horizon and falsification conditions. Scenario ranges are not statistical confidence intervals. Probabilities are optional; where given, state their basis and do not choose them to obtain a neat target price.

If using TAM x share x margin, align market definition, period and currency; avoid overlapping segments and reconcile arithmetic. Mathematical consistency does not establish economic feasibility. Do not backfill assumptions to reach a desired valuation.

A valuation-only correction can change the target and rating without changing the operating forecast. Preserve the prior version, attribute the valuation-input and period-alignment effects, and propagate the recomputed decision through the workbook, reports, challenge/conclusion records and current references. Recheck consistency rather than defending the old call.

## Governance, persistent discounts and target realisation

Include [market context and narratives](../macro-event-analysis/references/market-regime-and-investor-base.md) according to decision materiality alongside operating value, governance and payoff. A credible topical association can affect the multiple or attainable price before earnings emerge without establishing operating exposure. Test priced-in recognition, persistence/fade and relevant neglect/rotation cases. Keep investor-demand detail proportionate; identified buyers or proven inflows are not prerequisites, while material access/liquidity risks remain explicit.

Distinguish economic value created by the business from value accessible to the exact common-share class. Apply supported governance consequences to cash flows, dilution, capital allocation, financing or required return, and show their lineage. Avoid charging the same concern repeatedly through lower cash flows, an unexplained multiple haircut and a higher discount rate.

Test why the stock looks cheap and why the discount could persist. Evidence of active investor avoidance must be attributed or observable; price alone does not establish it. Model a current-governance case and a conditional improvement case when material. Identify the actor, incentive, event and timing that could improve cash returns or allow repricing. Do not assume automatic convergence to peers or full intrinsic value.

Keep today's intrinsic value, a future market-price target and alternative-method cross-checks distinct. Preserve a persistent discount where evidence warrants it; reject a Buy thesis whose required shareholder-return path is unsupported.

## Handoff

For expectations-only requests, default to a neutral map of evidence, conditional model results, attributed disagreements and next tests; do not add an unsolicited stock rating. Use a `valuation-thesis` handoff for current quantified company/industry work and a `hypothesis` handoff for historical/short-window investigations. Keep structured scenario, evidence and claim IDs; reference larger datasets through the existing envelope rather than adding unsupported schema fields.

Return the valuation basis, scenario inputs, numerical consistency/round-trip checks, sensitivities, own-versus-market assumptions, expected return components, counter-case, catalysts and observable thesis breakers. Separate price upside, dividend yield, FX and implementation costs on a consistent horizon.

Map unresolved assumptions to [management questions](../issuer-questions/SKILL.md). Pass the provisional thesis to the [post-valuation financial validation](../financial-quality/SKILL.md) and [challenge](../research-challenge/SKILL.md) passes, then synthesise it through [investment conclusion](../investment-conclusion/SKILL.md). If validation changes a material forecast, rerun its audit and valuation before concluding. Conditional value alone does not determine portfolio size or entry timing.
