# Valuation calendar and earnings basis

Apply the [target definition](../../investment-conclusion/references/decision-contract.md#target-and-earnings-basis). Record the research cutoff, fiscal year-end, current open fiscal year, latest actual period, current forward earnings window, target date and target earnings window separately. Use explicit dates, profit definition, shares and currency; vendor FY1/FY2 labels are not reliable period identities.

The rules here use P/E as the example. They apply in the same way to every yardstick in the [yardstick list](yardsticks.md#how-each-yardstick-is-measured): the band, the headline level and the target all use the same forward figure (EPS, book value per share, EBITDA, sales or DPS).

Keep headline P/E on current forward earnings. The target applies the target multiple to the same forward earnings, a price the stock should reach within twelve months. Do not roll the earnings forward to the target date.

Keep the economic anchor on that period too. Multiplying another period's EPS by its peer multiple, then dividing the result by current-forward EPS to print a forward multiple, is a restatement of a different target basis. It does not satisfy this convention. A comparison on another calendar/fiscal period may inform a supported multiple judgment, with the bridge and its limitations stated; it does not silently replace the target denominator. Bear, base, bull and material sensitivity prices retain the selected target convention. The publication [economic-basis contract](../../report-layout/references/publication-review.md#review-packet-and-financial-assertions) records their actual anchors and tests exact inverse-EPS cancellation. It does not decide which company deserves a premium.

For ordinary next-year fiscal P/E, establish the issuer's naming convention from the research date: a December-year-end issuer researched in the fourth calendar quarter of year N has open FY N and next FY N+1; a March-year-end issuer researched then may already name its open year FY N+1, with next FY N+2. Take N from the [research date](../../research-cycle/SKILL.md#start-from-the-task), not from memory or a skill example. NTM, mid-cycle or milestone earnings can be more informative; retain the current-forward comparison and explain the choice.

Derive NTM weights from the fiscal calendar at the selected anchor date. Prefer supported quarterly detail for seasonal businesses; identify annual-weight approximations and test material seasonality. Align peers and historical observations to the same forward convention, accounting and share basis. Historical forward ratios require estimates available at those historical dates.

For publication, [dated NTM controls](../../report-layout/references/dated-ntm.md) support explicit quarter/half/irregular-period coverage as well as annual interpolation. Choose the forecast profile on economic support, not because one method is accepted by a checker or gives a preferred call. If a credible alternative changes the target or rating materially, show it and explain the primary choice. Within-period allocation is still approximate; finer rows without evidence do not create a better forecast. Do not add EPS across changing weighted-share counts; use attributable profit and time-weighted shares on a common scale.

`current forward P/E = reference price / current forward EPS`

`target price = our selected current-forward EPS * justified target multiple`

For an enterprise-value yardstick, `target price = (target multiple * our forward figure - net debt and other claims) / shares`, with the claims at the same date as the price.

Include currency conversion where required. Across dated reviews, separate changes in the current earnings window, forecast revisions and multiples. Within one fixed current-forward target calculation, there is no earnings-period roll; with identical EPS at both endpoints the earnings contribution is zero. Recompute targets, returns and ratings when a period error is corrected, preserving the prior dated decision. Profit terminology follows the [writing guide](../../research-brief/references/natural-writing.md#profit-labels-and-valuation-language).

## Calendar-year comparisons

Show calendar-year EPS beside the fiscal figures when the investors, the valuation convention or the comparison set work in calendar years; a non-December fiscal year alone does not require it, and the fiscal or NTM basis stays when that is how the stock is compared. Build it from the quarterly forecast, mapping each fiscal quarter by its actual end date ([calendarize.py](../../company-model/scripts/calendarize.py)): a comparison convention, not a day-by-day reallocation of earnings. Use calendar profit over time-weighted shares; an equal-quarter weighting, or interpolation of annual figures where quarterly detail is missing, is an approximation to label. Fiscal statements stay the reporting basis. Compare our calendar EPS only with consensus, peer and band figures on the same calendar window, and keep the target on the forward period the house rule names: a calendar year shown for comparison is not the target's earnings period, and neither is the target date.

## Own forecast and consensus P/E

Use the same price, period, earnings definition, currency and share basis before comparing forecasts. Keep each denominator explicit:

- Our current forward P/E = price / our forward EPS.
- Consensus-based forward P/E = price / matched consensus forward EPS.
- Target = target multiple * our forward EPS.

The same split applies to any yardstick, with EPS replaced by the figure the yardstick is applied to. These are two ratios describing the same reference price. A higher P/E on our forecast can simply reflect lower forecast EPS, not a different observed market valuation. Use our ratio for the headline and target-return comparison; show the consensus-based ratio separately. A limited broker sample remains a sample.

Holding our current P/E against the same own EPS reproduces the reference price. Applying the consensus-based P/E to our EPS instead resets the earnings estimate while retaining the multiple derived from consensus. Label that as an earnings downgrade or upgrade scenario, according to its direction; do not call it unchanged own P/E. Keep this secondary explanation in supporting research when it would confuse the brief.

The two bridges reconcile to the same target:

`own-forecast bridge = our EPS * (target P/E - our current P/E)`

`consensus earnings effect = (our EPS - consensus EPS) * consensus-based P/E`

`consensus multiple effect = our EPS * (target P/E - consensus-based P/E)`

The latter two effects sum to the own-forecast bridge. They are alternative explanations, not additional gains. With fixed current-forward EPS, neither bridge adds target-date earnings growth. Dividends remain separate.

Use [compare_forward_pe.mjs](../scripts/compare_forward_pe.mjs) with canonical period and earnings definitions to verify this arithmetic. It rejects mismatched comparison bases and nonpositive EPS; it cannot judge whether a historical mean is relevant, a commercial recovery is likely or a target is attainable.
