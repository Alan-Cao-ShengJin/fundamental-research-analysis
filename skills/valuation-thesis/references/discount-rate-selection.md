# Select the discount rate from current evidence

Use whenever a valuation or capital-return comparison needs a cost of equity or WACC. The analyst system derives the rate itself from dated market evidence; never ask the user for a premium, beta or rate. A required return the user specifies is a mandate to respect, and is labelled as one.

For a steady dividend payer the target yield comes from [comparable income investments](valuation-driver-and-dividends.md#comparable-yields-own-band-and-bonds); a cost of equity is only a supporting check there.

## The rate: the 10-year yield plus the premium the market itself implies

`cost of equity = 10-year government yield + market-implied equity premium ± company adjustment`

1. **Risk-free rate.** The 10-year government yield of the valuation currency at the research cutoff; for a pegged currency, the anchor currency's yield plus any observed spread. Where the sovereign carries default risk, deduct its default spread so that risk is not charged twice.
2. **Market-implied premium.** Solve for the return that today's index price implies, for the index the stock's buyers benchmark against. Take the index level `P`, the cash paid to index holders over the past twelve months `C` (dividends plus net buybacks, in index points), consensus earnings growth `g` for the next five years, and long-run growth equal to the risk-free rate `rf`. Find `r` in

   `P = sum over t=1..5 of C(1+g)^t / (1+r)^t  +  [C(1+g)^5 (1+rf) / (r - rf)] / (1+r)^5`

   The premium is `r - rf`. [implied_premium.py](../scripts/implied_premium.py) solves it. The figure moves with the index, with earnings expectations and with rates, so recompute it at every cutoff; never carry a premium over from another study.
3. **Where the index inputs cannot be had.** Use the implied premium of a mature market computed the same way, plus a country premium: the sovereign default spread (from credit-default swaps or the rating) scaled by the ratio of equity to government-bond volatility in that market. Do not add a country premium to a premium already solved from the local index.
4. **Company adjustment.** Up to one point either way for clearly higher or lower business risk than the index (leverage, cyclicality, cash-flow visibility, shareholder access), with the reason stated. The stock's own regression beta is not used: for a thinly traded stock it changes with the sampling day. Do not charge the same risk in both the cash flows and the rate.

Estimates of the premium differ widely between methods, so show the inputs and their dates, not false precision. Show one alternative only where it changes the conclusion: the same calculation with growth one point lower.

For enterprise cash flows build WACC from this cost of equity, the dated after-tax cost of debt and the financing weights; do not substitute the cost of equity for WACC.

## Keep it in the model

Store the inputs with their dates and sources in the data area and link them into a visible rate build beside the valuation. Refresh them at each new cutoff and keep the earlier build to explain a change; within a frozen study use the pinned inputs. The reverse-DCF helper takes `riskFreePct`, `equityRiskPremiumPct` and `riskAdjustmentPct` (the company adjustment). If an input cannot be retrieved, use a dated, labelled alternative and show the range; leave an optional DCF cross-check out rather than ask the user for a rate.

## Why this method

- Damodaran, *Equity Risk Premiums: Determinants, Estimation and Implications* (updated annually), and his [country-risk method](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html): the implied premium is forward-looking and can be recomputed whenever prices move, while a historical premium is backward-looking and noisy. Steps 2 and 3 follow his construction: dividends plus buybacks, analyst growth for five years, then growth at the risk-free rate; and a country premium from the default spread scaled by relative equity volatility.
- Li, Ng and Swaminathan, "Predicting market returns using aggregate implied cost of capital", *Journal of Financial Economics* 110(2), 2013: the market's implied cost of capital predicts its excess return from one month to four years ahead, beyond valuation ratios and business-cycle variables.
- Gebhardt, Lee and Swaminathan (2001) and Claus and Thomas (2001): the same idea built from analysts' earnings forecasts in a residual-income model.
- Duarte and Rosa, "The Equity Risk Premium: A Review of Models", Federal Reserve Bank of New York Staff Report 714, 2015: twenty models in five classes give widely different premiums, which is why one method is applied consistently and its inputs are shown.

These references explain the method; their published figures are not inputs for another cutoff.
