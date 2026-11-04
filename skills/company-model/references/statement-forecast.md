# Build the linked three-statement forecast

This stage consumes the [revenue/cost projection](revenue-projection.md). A completed company model includes earnings, the balance sheet and cash/financing consequences. Copying a template's ratio formulas or making its balance-sheet check zero is not sufficient.

## Income statement and the next forecast period

- Link revenue and costs/GP from the operating build for the correct currency, scale, scope and period. Prevent an RP -> 3S -> same RP driver loop.
- Forecast selling, administration, R&D, other operating items and restructuring from supported drivers and cost timing. Examine same-quarter/half-year history, annual accruals, wage/bonus changes and disclosed investment; do not apply one flat ratio to everything.
- A fixed expense base with wage inflation assumes the activity can scale without additional people, engineering or service capacity. Substantiate that capacity and any closure/stranded costs; compare implied expense ratios with observed run-rates. Do not replace that analysis automatically with flat percentages.
- Build equity/associate income, finance expense/income, tax and minority interests separately where material. Avoid double-counting JV income embedded in an operating segment.
- Tax the profit of the entities that pay it. Costs borne by holding companies in another jurisdiction are not deductible against the operating subsidiary's tax, and the tax base and the minority base should treat the same costs the same way. Check tax-loss balances and their expiry before carrying a low historical rate forward.
- Schedule stock compensation and dilution from the relevant award terms and accounting basis. A vesting hurdle does not establish that management will meet it or justify capping expenses.
- For the current incomplete year, annual flow = reported YTD + forecast remaining period(s). Ratios become outputs of the underlying amounts. When full-year actuals arrive, replace the forecast boundary with reported FY figures and retain the old forecast for attribution.
- Compute basic/diluted EPS from the applicable weighted share count, not every period's closing common shares. Derive dividends from declared amounts or a labelled payout assumption; check cash affordability separately.

## Supporting schedules

Apply [capital-return and investment tests](competition-and-capital-returns.md#test-whether-additional-growth-creates-value): reconcile growth with required assets, working capital, expensed investment, financing and dilution. Define matched capital/earnings bases and separate historical from marginal returns, accounting for maturity lags and acquisitions. Use sector-appropriate capital measures. State estimated maintenance/growth splits without manufacturing precision, and pass the investment and return transition into valuation.

| Schedule | Link and check |
| --- | --- |
| Working capital | Receivables, inventory, payables and other operating balances from appropriate activity/turnover drivers; their cash effects follow changes on a consistent perimeter |
| PPE / construction | Opening balance + capitalised additions + transfers/acquisitions/FX - depreciation - disposals/impairments = closing balance |
| Intangibles / goodwill | Separate amortisation, acquisitions, impairment and FX; do not amortise goodwill automatically |
| Leases | Opening liability + new leases + interest/reassessments/FX - cash payments = closing liability; reconcile ROU assets and rent treatment |
| Debt / finance | Opening debt + drawdowns/noncash changes - repayments = closing debt; maturities, borrowing cost and available funding explicit |
| Tax | Book tax, cash tax and deferred effects distinguished; normalize exceptional items with a disclosed basis |
| Equity / dividends | Opening consolidated equity + consolidated profit including NCI + issuance/compensation/OCI - parent and NCI dividends - buybacks ± other changes = closing consolidated equity; separately roll parent equity if required |
| Cash | Opening cash + operating + investing + financing + FX/reclassification = closing cash |

Use the issuer's accounting framework and actual schedules. Simplifying assumptions are permitted when justified and labelled; omitted material funding or reinvestment is a model gap.

## Cash flow and financing closure

Start from the appropriate earnings subtotal and bridge noncash charges, equity-method income/distributions, working capital and cash tax/interest consistently. Add investing cash flows, then financing cash flows and distributions. Classify leases under the applicable framework and keep valuation treatment consistent.

For IFRS 16, use a consistent cash/claim basis: deduct lease principal in owner cash with leases excluded from the debt deduction, or treat leases as debt with appropriately unlevered operating cash flows. Do not charge the same lease obligation in both cash and net debt. Count SBC once, as an economic cash-equivalent cost or through dilution; reconcile repurchases rather than charging them again. Buybacks use financing cash and assumed repurchase prices/timing to derive weighted retired shares and EPS, not simply year-end shares.

Do not silently plug cash, debt, payables or Other assets to achieve a zero balance. An explicit cash sweep or financing plug can close a forecast only when its mechanics, debt/cash constraints and interest consequences are specified. A negative-cash result without available funding remains a liquidity gap, not a formatting issue.

Changing the group perimeter requires acquisition/disposal/FX bridges: ending balance-sheet differences alone do not reproduce operating cash flow. Check such changes before interpreting historical turnover or cash conversion.

## Readiness for the model audit

Show annual/interim reconciliation; statement and schedule identities; profit-to-cash conversion; debt/liquidity and dividend affordability; share/EPS checks; and downside sensitivity. Preserve the user's chosen reporting cadence: an annual-only BS/CF can support annual valuation, but do not claim quarterly cash forecasts that were never built.

Recalculate using a compatible engine, inspect relevant formula errors/circular references and compare intended changes with the baseline. See [workbook verification](workbook-profile.md) and the separate [assumption/model audit](forecast-audit.md). If these remain partial, state exactly which model/valuation claims depend on them.
