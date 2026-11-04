# DCF mechanics (cross-check only)

Use a DCF sparingly: most of the time investors do not value stocks this way. Use it only for companies with strong, predictable cash flow, and at most as a cross-check of the midpoint intrinsic value against the P/E or other primary target. Do not rely on it, set the target from it or discuss it in the write-up. The mechanics below apply only when that test is met.

## Match the claim and cash flows

For a nonfinancial corporate issuer, an FCFE bridge may start from attributable net income, add relevant noncash charges, deduct capex and increases in noncash working capital, and include net borrowing/repayment and other claims as appropriate. Validate the issuer-specific bridge. FCFF belongs with a firm-level discount rate and an enterprise-to-equity bridge; FCFE belongs with a cost of equity. See [Damodaran's cash-flow lecture](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/dcfinput.html).

Neither net income nor operating cash flow alone is generally distributable equity cash flow. Avoid double counting SBC add-backs while ignoring dilution, cash settlement or repurchase costs. A growing terminal business also needs an economically coherent reinvestment and financing assumption.

Lower cash conversion lowers value for the same profit path, and at a fixed price raises the profit needed to justify it (required profit = required FCFE / conversion). Distinguish that inferred requirement from the analyst's own estimate of what the business can earn.

## Dated economic value and price target

A DCF gives value today. At a target date T years later, equity economic value is `V_T = V_0 * (1 + k_e)^T - sum(D_t * (1 + k_e)^(T-t))`, where D_t are distributions paid before T. Use cost of equity on equity value; roll enterprise value at WACC before bridging to target-date equity. State whether flows are discounted mid-year or year-end, and model stub periods explicitly.

This is an economic-value roll, not proof of a realisable market price. Apply the [target contract](../../investment-conclusion/references/decision-contract.md#target-and-earnings-basis). Keep the share basis and target-date cash/debt consistent: buybacks change shares and cash, retained cash must not be added twice, and per-share compounding cannot blindly treat repurchases as cash dividends.

## Required return (house convention)

When a DCF cross-check is used, the default cost of equity is the **10-year government bond yield of the valuation currency, as of the research cutoff, plus a 5% equity risk premium**. Adjust by up to ±1 percentage point for clearly lower or higher business risk (leverage, cyclicality, cash-flow visibility, governance access) and state the reason. Any other deviation needs its own stated reason beside the assumption. State the risk-free source and date in the model. This convention is a comparability tool, not a claim about the market's discount rate. Use WACC on enterprise value with the same equity component.

## Terminal reinvestment

Under consistent steady-state assumptions, `g = ROIC * reinvestment rate` for FCFF and `g = ROE * retention` for FCFE. Thus required terminal net income is `FCFE / (1 - g/ROE)` where sustainable ROE exceeds g and net borrowing/capital structure are consistent. Do not grow cash indefinitely without the reinvestment required to generate it. Test marginal returns, competitive duration and financing, not merely g < discount rate. See [Damodaran on growth, returns and reinvestment](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/termvalueexreturns.htm).

## Included calculator

`scripts/reverse-dcf.mjs` is a small, dependency-free FCFE sensitivity helper, not the complete analyst model. Run with Node 24 or later:

```powershell
node skills/valuation-thesis/scripts/reverse-dcf.mjs skills/valuation-thesis/references/fcfe-example.json
```

The example is synthetic. Inputs state equity value, currency/scale, explicit forecast FCFE, terminal growth in percentage points and transition years. `10` means 10 percent, not `0.10`. Give the cost of equity either explicitly as `costOfEquityPct`, or by the house convention as `riskFreePct` (the 10-year government yield) plus an optional `riskAdjustmentPct` (default 0; the convention allows ±1), with `equityRiskPremiumPct` defaulting to 5; the result reports the components. `firstFlowYears` gives the timing of the first cash flow (default 1); subsequent explicit and transition flows follow one year apart. No calendar year or discount-rate grid is inferred from the current date.

At explicit year K, the final forecast FCFE must be positive for this helper's geometric transition. Over N subsequent years it transitions to unknown steady-year FCFE S. At T=K+N, terminal value is `S * (1+g) / (r-g)`; the first terminal cash flow is at T+1. The helper discounts the explicit flows, transition flows and terminal value once each. It solves S only for a bracketed nonnegative root and checks forward value against the target.

The helper permits earlier negative explicit cash flows but cannot represent a nonpositive final cash flow with its chosen transition. Use an explicit cash-flow model for turnarounds, finite-life assets or other incompatible cases. It does not estimate probabilities, select rates, choose terminal reinvestment, calculate an enterprise/equity bridge or recommend trades.

## Interpretation checks

- Price x relevant share count reconciles to the stated equity basis and currency; take share-class and dilution differences seriously.
- Forecast and market inputs share the same information cutoff and reporting periods.
- Numerical forward/reverse agreement tests arithmetic, not the reasonableness of inputs.
- Compare scenarios on the same fiscal anchor and terminal timing. Different terminal horizons/rates can change an inferred requirement without new business evidence.
- A fitted profit/cash-flow target outside plausible scenarios is a sign to reassess assumptions, not evidence that the target will be achieved.
- A perpetual linked to a share/index/commodity needs separate basis, funding, oracle and margin analysis; a cash-market valuation cannot be copied into a trade return unchanged.
