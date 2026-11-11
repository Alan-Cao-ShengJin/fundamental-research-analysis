# Identify what supports the valuation

Read when selecting a primary target or explaining why a stock could rise. Choose the mechanism from the evidence, not from the desired target. Several mechanisms can coexist, but name the primary one and keep their contributions separate.

| Primary mechanism | What must support it |
| --- | --- |
| Earnings growth at today's valuation | Forecast EPS and its operating drivers; a consistent fiscal/share basis; price gain that survives without a higher P/E |
| Higher P/E or other valuation multiple | The reason for today's discount, a specific change, observable evidence/timing and a justified future valuation; follow the rerating test in method-selection.md |
| Sustainable cash dividends | A credible annual dividend forecast, payout history/policy, funded cash coverage and a market-anchored required yield for a steady income payer; dated dividend-discount calculations can cross-check the economics |
| Asset realisation or capital return | Realisable asset value after claims/costs, an actor and a credible route and timetable for shareholders to receive it |

Do not explain a dividend-led case only as cheap P/E. If the reason to own the stock is cash distributions, quantify that reason. Conversely, a rising dividend does not automatically justify P/E convergence. A results date, generic cash improvement or hope that investors notice is not a revaluation mechanism.

## Dividend evidence and period alignment

For a material dividend thesis, retrieve the latest policy and its adoption, conditions and expiry; the latest interim/final declarations and ex/payment dates; and the relevant annual payout record. Prefer original filings. Read policy and subsequent approval together: a proposed policy is not adopted, and even an adopted conditional payout is not guaranteed.

Separate these measures:

- **Earnings-year payout:** dividends attributable to the fiscal year divided by net profit attributable to shareholders for that year. Show special dividends separately. Do not divide calendar cash paid by the same year's earnings if payments include an earlier year's final dividend.
- **Annual forward yield:** forecast annual dividend per share divided by the dated share price. State the earnings year, currency, share basis and gross/net-tax treatment.
- **Next-twelve-month receipts:** only distributions a buyer at the reference date can still receive within the target window. Exclude already-ex dividends. Show receipts separately; they are never added to the target, rating or attractiveness tier.

For a material claim about cash arriving over a dated window, use the [dated receipt helper](../../company-model/scripts/cash_receipts.py) with [the original synthetic schedule](../../company-model/assets/cash-receipts.example.json) as a field example. Declare the buyer date, window, currency/unit, gross/net basis and each event's amount, status, entitlement and payment dates. Missing dates remain unresolved; forecast dates remain assumptions. Ordinary ex-date entitlement excludes purchases on/after the ex-date. Due-bill or other unusual rights need explicit sourced entitlement treatment. A fiscal-year DPS is not a receipt schedule. Bind material published totals/yields with the existing [claim-support mechanism](../../report-layout/references/claim-support.md#dated-cash-receipts); the helper cannot discover omitted events or authenticate rights.

Show the dividend if the payout ratio stays at its supported level, not merely a guessed cash amount. If the policy floor differs from the latest actual payout, show both as distinct scenarios. A higher payout is upside until management intent and cash capacity support it.

## Cash coverage and room for more payout

Use the [classification/recognition/payment bridge](../../company-model/references/statement-forecast.md#classification-recognition-and-payment-states) where distribution timing matters. An observed cash payment does not identify its earnings year. Separate declared entitlements, forecast policy payouts, settlement and any applicable prudential deduction, reconciling amounts already included. A management capital goal without a deadline is not a mandatory immediate restoration. State the constraint and assumed timing behind each coverage conclusion; preserve a rating-sensitive alternative rather than choosing the most restrictive convention automatically.

Reconcile operating cash to cash available for common shareholders after working capital, investment, leases, interest, taxes, debt movements and other claims, on a consistent accounting basis. Do not deduct an item twice. Exclude one-off loan/advance recoveries, asset sales and new borrowing when assessing recurring capacity; show them separately as liquidity sources.

Compare the proposed dividend with recurring cash capacity, statutory/distributable reserves, parent-company access, regulatory/covenant constraints and minimum operating liquidity. Include competing buybacks and dilution. High bank cash or a low accounting payout ratio alone does not prove room for more dividends.

Quantify cash coverage and the amount left after the base dividend. Show a higher-payout case and a stress with weaker earnings, tighter working capital or higher investment. A theoretical maximum payout that exhausts recurring cash is not a sustainable recommendation. Distinguish capacity, management willingness and an approved declaration.

Show recent historical/current-year coverage as well as the forward point. If coverage improves sharply, explain the operating cash, working-capital and investment assumptions behind the change; do not describe borrowing-funded payments as evidence of recurring dividend strength.

## Comparable yields, own band and bonds

For a dividend-led case, the required yield is the forward yield of comparable yield investments the stock's marginal buyers can hold: the same investor access, ownership type and dividend tax and, where a new investor group is about to gain access, what that group can already buy. Choose them by who owns them for income, not by industry; a broad set of such payers is better than a few industry peers. Match the forward period, currency/FX exposure, distribution basis and tax treatment; explain differences in payout sustainability, growth, leverage, liquidity and shareholder rights, and adjust the yield for them rather than discarding the set. The stock's own yield band is the sense check, and sets the yield only where no such investments exist. A cost of equity less growth or a P/E never sets the target for a steady payer. When defensible anchors change the rating, show their yields, targets and calls and explain the primary choice. A yield outside the historical band needs an economic explanation of changed risk, growth, rates, rights or investor access, not an automatic rejection or a catalyst date alone.

Where investor eligibility or index membership could change, test the actual rules and measurement window using information available by the cutoff. Assess whether new access plausibly changes demand rather than assuming buying or rerating. Compare values with and without the change on matched dates, cash-flow and share bases. Infer a conditional price-implied weight only if explicit, independently justified outcome values support it: in a stated two-state linear mixture, `p = (price - value_without) / (value_with - value_without)`. This is conditional on the chosen values and pricing assumptions, not an observed real-world probability. Equal outcome values do not identify a weight; price outside their range rejects that mixture rather than warranting a weight clipped to 0 or 1. Test material alternative values, or report that price does not identify the probability.

This is the house convention for steady income payers, not a universal valuation law. Verify that any own-yield fallback has usable observations on a relevant payout and business regime. An unavailable or inapplicable band remains a documented evidence gap, not a series to invent. Apply the existing economic-fit and supported-target rules where no defensible market anchor can be reconstructed. Cost-of-equity and dividend-discount calculations remain supporting economic checks, with their assumptions disclosed; they do not become this branch's primary target.

Government-bond yields alone do not set an equity-yield target. Where bond evidence informs the valuation, justify currency, tenor, observation dates, tax/access and rate regime; show dated spreads and their distribution. The generic [yield_spread.py](../scripts/yield_spread.py) separates equity-yield and government-rate changes and retains benchmark/source definitions. Its mean spread is descriptive: bond spreads are context for the comparable yields and do not set the target yield. Do not apply a historical mean spread automatically to every dividend stock, or treat a stock distribution as a guaranteed bond coupon.

## Price, yield and the investment argument

For yield capitalisation, show `target price = sustainable annual DPS / required dividend yield`. The required yield comes from the comparable set above. Show a range; do not choose the yield to reproduce an old price target. A dividend-discount model can cross-check explicit growth and changing payouts; for a steady income payer it does not replace the house market-yield anchor.

Reconcile P/E and yield on the same earnings/dividend/share basis: `dividend yield = payout ratio / P/E`. These are two expressions of the same valuation, not independent evidence to average or add. Higher payout, earnings growth and a lower required yield have different effects; explain which causes the price change. A lower required yield means investors pay more for the same dividend, and needs a reason just as a higher P/E does.

The pitch must state the annual DPS/yield, payout ratio, coverage, room for more payout and why the target yield is reasonable when these drive the call. Explain what happens if the payout stays unchanged and investors demand the same or a higher yield. Retain governance and dividend-cut risk. A high yield is not a price floor, a bond coupon or proof of attractive expected return. Apply the rating and separate attractiveness rules without changing the valuation to meet a hurdle.
