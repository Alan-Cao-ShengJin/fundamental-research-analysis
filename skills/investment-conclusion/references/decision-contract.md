# Stock decision and communication contract

Use for completed single-stock research. A narrow factual question need not manufacture a recommendation.

## Valuation yardstick

First work out what type of company this is and what investors pay for. Then select the valuation method that fits and keep it as the main anchor throughout; other metrics can support it but stay secondary. Investors with different purposes look at a stock differently depending on its characteristics:

- **Low growth, high yield:** a dividend payer. Its yield, compared with what investors can get in the bond market, is the yardstick.
- **Growth, little or no dividend:** P/E or price-to-sales, compared with peers that have similar characteristics.
- **Cyclical:** its own historical P/B or peer P/B.
- **Very consistent cash flow:** a DCF can cross-check fair value, but it is never the main anchor.
- **Other cases:** sum of the parts using EV/EBITDA, EV/Sales or similar.

Follow [method selection](../../valuation-thesis/references/method-selection.md).

## Target and earnings basis

The twelve-month target applies a reasonable target multiple to today's forward earnings: a price plausibly realisable within the next twelve months. The horizon rolls: at each review the target date is twelve months from the review date, and the target is re-derived from that day's forward earnings.

The target is about the gap between today's intrinsic value and the current share price, and what that intrinsic value will become within twelve months. That cross-check shows how large the gap is and can point towards a target price, but do not rely on it completely. Use a DCF sparingly: only for companies with strong, predictable cash flow, as a cross-check of the midpoint intrinsic value against the P/E or other primary target. Follow the [dated-value mechanics](../../valuation-thesis/references/valuation-method.md#dated-economic-value-and-price-target) when rolling it forward.

Explain how the price reaches the target:

- earnings growth above market expectations, which can give the stock a temporary re-rating against peers or its past valuation;
- consistent earnings growth while the valuation multiple holds;
- for a dividend payer, its yield re-rating against the bond market as the price rises, through a higher payout or higher earnings.

A dated catalyst that is already known should be more or less priced in by the time you look at the stock.

**Forward P/E.** State the consensus EPS and the implied forward P/E, on next fiscal year or NTM depending on how detailed the data is. In the first half of the fiscal year (1Q or 2Q results out) the market is still looking at the current year's valuation or NTM; once 3Q results are out, start looking at next year's valuation. It is a good habit to show two years to cover more angles: after 3Q26 results, show FY26 and FY27 valuations. For the target, apply the target multiple to the same forward earnings and state which period that is. Do not roll the earnings forward to the target date. Follow the [valuation calendar](../../valuation-thesis/references/valuation-calendar.md).

**Target multiple.** Understand why the stock was valued higher before and why it has de-rated, or the reverse. If the change is structural, the old range no longer applies: healthcare stocks were re-rated and crowded during Covid, and once Covid went away they were no longer valued at those levels, so their five-year history would mislead and closely related peers make more sense. If the stock is only temporarily oversold or overbought, compare it with its historical forward P/E band: it should return to the mean eventually, so the mean is the default target multiple. Pushing above the mean requires a significant catalyst. A stock that looks cheap against peers or the market but already trades at its own historical mean can stay cheap for a long time. Which multiple to use depends on the argument and how the market is likely to perceive the stock over the next twelve months. Support it from more than one angle: the stock's own history, the closest same-market peers doing the same business, and the market's current appetite for the sector ([market context](../../macro-event-analysis/references/market-regime-and-investor-base.md#locate-the-opportunity-in-the-investment-landscape)).

Any multiple different from today's, including one used only in the bull case, needs an analysis of how it could actually happen: why the stock is valued where it is now, what changes, what investors will see and when, and why that level. Do not pick a multiple without this. Apply the [rerating test](../../valuation-thesis/references/method-selection.md#rerating-and-derating).

**Consensus.** Compare our EPS and target with consensus: how far above or below we are and why. Is the market missing something, or are we? Consensus is usually to be respected. Depart from it only when we know something the market does not and are confident, with conviction, that it will happen.

**Always give a call.** Arrive at the target through a logical sequence of assumptions, cross-check it with the other valuation methods above, and apply the bands below. Give a call on the financials available. If the stock is an avoid, unattractive or raises a red flag, say so beside the call.

## Return hurdle and calls

Calculate before rounding, on the same currency and share basis:

- Price return = `primaryTarget / referencePrice - 1`.
- Dividend yield = forward annual dividend per share / `referencePrice`, shown separately. Use the same fiscal year as the target's forward EPS (after 3Q results, next year's DPS), with the current-year yield beside it where it helps.

| Price return | Rating |
| --- | --- |
| Below -10% | Sell |
| -10% through +10%, inclusive | Hold |
| Above +10% | Buy |

A target more than 10% above the price is a Buy even when it is an unattractive Buy. If the business has no meaningful pivot and no other attractive feature, it can still be a Buy: state that it is unattractive and that investors should consider avoiding it.

Sell is the opposite of Buy. It is a recommendation, not an action or instruction.

**Dividends.** The target price is the main figure. Present dividend yield entirely separately and do not build dividends into the target. Read yield as a measure of cheapness or a cushion for downside. A high-yield stock earns its return through re-rating: as more investors buy into the yield, the price rises and the yield falls, and that price gain is what we cash out. Holding a high-yield stock just for the yield is generally not attractive; above a certain yield it gives downside protection. Companies sometimes promise a return built from yield and buybacks, for example 12% from a 10% dividend yield plus 2% buybacks; report that separately from the target. Do not add buyback yield to a target that already reflects the lower share count. Label FX and costs separately; never invent them.

Keep attractiveness separate from the rating. Judge it on base-case price return over the rolling twelve-month horizon, and state the tier beside the rating:

| Base-case price return | Tier |
| --- | --- |
| 50% or more | Attractive |
| 30% to below 50% | Decent |
| 10% to below 30% | Risk/reward looks less attractive to compensate for downside risk |
| Below 10% | Not meaningful |

Write it as **New money: yes/no (tier), because…** A Buy in a lower tier remains Buy. A tier is necessary, not sufficient: consider downside, governance, costs, timing and active exclusions. Use the primary target, never the bull case; do not fix dividends into the target, inflate it or extend the horizon to reach a tier. When new money is no, give the pre-cost entry price for the attractive tier, `primaryTarget / 1.50`, and for the decent tier, `primaryTarget / 1.30`, provided the target remains valid at that price; carry it into the conviction record as a watch level. An explicit current mandate can change these tiers; record its basis.

## Decision block

Show the exact security/share class, currency, timestamped quote, Buy/Hold/Sell, primary target/date, price return, dividend yield and bear/bull prices/returns.

A portfolio manager generally wants one target price so they are not confused. Show that target in the header or decision block. In the narrative, establish the business drivers and earnings/cash consequences before the detailed valuation calculation; explain its anchor and any comparable consensus difference. Keep bear and bull cases with little emphasis. Place the pivotal thesis sentence beside the call. Use the [argument sequence](../../research-brief/references/natural-writing.md#argument-sequence).

State the re-rating upside: our current forward P/E against the target multiple, with the consensus P/E beside it. Both headline and target use our same current-forward EPS, so holding our current P/E reproduces the reference price. Applying the consensus-based P/E to our EPS instead is an earnings-reset scenario; follow the [basis rules](../../valuation-thesis/references/valuation-calendar.md#own-forecast-and-consensus-pe). Explain why any change in willingness to pay is supported and why a discount/premium could persist. Do not discuss the DCF in the write-up. A known fact is not necessarily overlooked by the market; use attributed or conditional price-implied expectations rather than asserting a market mistake.

Explain two things separately. First, the company's moat and earnings drivers. Second, why one should look at the company as an investment: it is cheap, growth is strong and likely to continue, the yield is very attractive, or the market is simply not valuing it properly.

For a dividend-led case, follow [valuation drivers and dividends](../../valuation-thesis/references/valuation-driver-and-dividends.md): sustainable annual DPS/yield, payout, recurring cash coverage, capacity and a justified required yield.

## Machine-consumable result

Retain the decision record with quote/security basis; target date and valuation basis; primary/bear/bull targets; price return; dividend yield; separate new-money judgment/hurdle; evidence and material uncertainty; and current model/run references. A null dividend is unknown, not zero. Preserve prior decisions and invalidate dependent claims when upstream facts change. Reference the record through the existing [handoff](../../research-cycle/references/handoffs.md), without adding undeclared envelope fields. Research completion does not authorise allocation, trading, outreach or monitoring activation.
