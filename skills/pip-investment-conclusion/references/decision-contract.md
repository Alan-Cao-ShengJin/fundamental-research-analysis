# Stock decision and communication contract

Use for a completed single-stock recommendation and its user-facing brief. Narrow factual, historical or governance-only work need not manufacture a recommendation. Keep incomplete research explicitly incomplete; do not invent a target to satisfy this format.

## The decision block

Lead with one **Buy**, **Hold** or **Sell** call. Apply the Hold rule below before choosing between Buy and Sell. Do not substitute Neutral, Watch, Trim, Avoid, a valuation range or confidence wording for the primary label. Confidence and conditions follow the call. Sell means unattractive to buy and reduce/exit if owned, subject to a separate portfolio assessment; it does not authorise or recommend a short sale automatically.

### Hold threshold

For completed research, calculate the primary target's signed price return as `target_price / reference_price - 1`, using the same currency and share basis. If the return is **between -10% and +10%, inclusive, the call must be Hold**. Exactly -10%, 0% and +10% are Hold. Use the available price precision before rounding the displayed percentage; handle exact boundaries without floating-point rounding changing the call.

This rule uses the selected primary target and timestamped reference price, not a bear/bull target, a different valuation estimate, dividend yield, total return or annualised return. Report prospective distributions and risks separately; they do not override Hold within the band. Outside the band, assess Buy or Sell using the supported shareholder-return path, risk and any stated return hurdle.

Hold still requires a primary target/date, signed price return, bear/bull targets and returns, a thesis sentence, confidence and what would change the view. It means limited price upside/downside to the selected target, not missing evidence. Essential unresolved evidence remains explicitly incomplete research, not a Hold fallback. Recalculate the call whenever the reference price or selected target changes.

| Field | Required meaning |
| --- | --- |
| Security and reference | Issuer, exchange/ticker, exact share class, reporting currency, reference share price and quote timestamp/status |
| Call | Buy, Hold or Sell; Hold is mandatory when primary-target price return is within -10% to +10%, inclusive |
| Key thesis sentence | One sentence immediately beside/below the call explaining the pivotal reason and economic consequence |
| Primary target price | One selected, sourced/model-linked price for an explicit target date/horizon; state why the primary method is preferred |
| Return to target | `(target_price / reference_price - 1) * 100`; signed percentage, same currency/share basis |
| Downside case | Bear target at the same horizon, its signed price return and the few assumptions that cause the loss |
| Upside case | Bull target at the same horizon, its signed price return and the few assumptions needed |
| Distributions and total return | Prospective dividends/buybacks treated consistently; show dividend contribution separately and total/annualised return when useful. Do not add past paid dividends or count buybacks twice |
| What changes the call | Evidence/catalyst and time horizon, plus the principal invalidation condition |

The headline target is the analyst's attainable market-price scenario at the stated horizon. Intrinsic value today, a margin-of-safety entry level, an optimistic exit-multiple case and a published broker target are different quantities. Label them separately; roll forward a present-value estimate before calling it a future price target. A range can supplement the primary target, not replace it. If valuation methods disagree materially, explain the selection rather than averaging them to achieve a preferred call.

Choose the primary valuation by the company's economics and examine relevant peers and its own historical forward valuation using the [method-selection guide](../../pip-valuation-thesis/references/method-selection.md). Show what supports any rerating/derating and how much return comes from earnings growth versus multiple change. Short or unavailable historical coverage stays explicit. The brief displays the selected target and decisive reason; detailed valuation comparisons and internal audit records stay outside it.

Present completed research using the [short visual report format](../../pip-research-brief/references/visual-reports.md), with the [natural-writing edit](../../pip-research-brief/references/natural-writing.md) before delivery. Default to a 250-350-word decision brief and an 800-1,200-word main narrative with useful figures and compact tables. Preserve analytical depth in linked model/evidence records; retain material risks, governance consequences and valuation dependencies in the main report.

Use the same horizon and quotation basis across base/bear/bull. Scenario targets are neither guaranteed prices nor probability-weighted forecasts unless a probability method is supported. For Sell, the bull return is the rally/forgone-upside risk; it is not a short-position loss calculation. Outside the Hold band, a Sell target can be above today's price if the prospective return is inadequate for the stated horizon/risk: explain the return hurdle rather than forcing a lower target. A Buy needs an adequate shareholder-return path, not merely upside in the most optimistic method.

## Explain the economics to an informed nonspecialist

Use compact connected paragraphs, defining company-specific terms on first use. Assume the reader understands revenue, profit and valuation, but not the issuer's specialised products or acronyms.

**Business model:** who pays, for what, how revenue is earned, the main costs/reinvestment and how cash can reach owners. Distinguish customer money/assets from company revenue, cash flow and shareholder claims. Explain the core engine before secondary initiatives.

**Competitive edge and moat:** why customers choose the business and why rivals cannot readily remove its pricing power or returns. Identify the mechanism, evidence, durability and principal erosion risk. Growth, market size, a licence, brand recognition or an AI strategy alone does not prove a moat. It is acceptable to conclude that the advantage is limited or no durable moat is demonstrated.

**Why Buy, Hold or Sell:** state one pivotal investment insight, with secondary supports only as needed. For Hold, explain why the primary target is close to the reference price and what evidence or price change would reopen the decision. Distinguish a competitive advantage of the company from an information/interpretation advantage of the investment thesis. Explain: what price or attributed market commentary appears to assume -> the evidence-backed difference -> the effect on cash/per-share value -> how and when shareholders might be paid or the price might change. Quantify the relevant driver and connect it to the model and target.

Do not assert that the whole market has missed a fact without evidence. Use conditional price-implied expectations or attributed views when broad consensus is unavailable. If no overlooked driver is established, say so and explain the call through valuation, required return or persistent governance constraints. A popular narrative or a known fact is not a research edge by itself.

**Governance and realisation:** explain whether minority holders can receive the business's value, why a discount could persist, and what credible event or cash-return route could overcome it. Business improvement alone does not guarantee repricing. Cash distributions and per-share compounding can support a Buy without multiple expansion when their economics and shareholder access are supported.

## Machine-consumable result

Retain a referenced decision record containing the call; security/quote basis; target date and primary/bear/bull prices; calculated price returns; separately defined distributions/total returns; business-model/moat summary; pivotal insight and evidence; governance consequences; catalyst/invalidation; model/engine/run and market-data versions; method selection and material uncertainty. Missing essential values stay null with a reason and the research stays incomplete.

Use the existing strict handoff envelope to reference the record and its claims/calculations. Do not insert undocumented fields into that envelope. On an upstream revision, mark the prior target/call stale and recompute dependent figures before using them in a report.
