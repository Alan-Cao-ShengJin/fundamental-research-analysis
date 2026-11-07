# Build the revenue and cost projection

Use reconciled [actuals](actuals.md), the operating-data map, dated [guidance](drivers-guidance.md) and the [industry analysis](../../industry-analysis/SKILL.md) to build the operating projection before the [statement forecast](statement-forecast.md). Market growth, share, price, input costs and customer behaviour come from the industry findings; the company's own history calibrates them, it does not replace them.

## Preserve the user's presentation

For an existing workbook, retain useful row order, product/geographic breakdown, notes and annual/interim columns. Change its structure only where the modelling requirement justifies it.

For a new workbook view, keep related calculations in a clear sequence on one worksheet. Place active assumptions, their basis and relevant history beside the results they drive. Longer source archives can sit in support tables. Reuse completed totals across schedules rather than scattering a local calculation chain between tabs.

Use [foundational builds](foundational-builds.md) to decompose material financial items into the smallest useful forecastable components. Investigate breakdowns available only in management calls or external series before settling for aggregate growth/margin assumptions. Forecast the foundational estimates from history, assessed guidance and matched third-party observations, with the remaining judgement explicit. Aggregate component forecasts upward. The evidence and reasoning behind the pieces determine how much conviction the segment forecast warrants.

## Test what a driver actually measures

Before forecasting from a derived unit ratio, align its numerator and denominator by activity, ownership, channel, cohort and period. Total revenue divided by stores can include online revenue, acquisitions and wholesale; it is not automatically store productivity or same-store growth. Revenue per customer can rise through churn of small customers, and output per asset through disposals. Separate these effects where supported, retain a composite proxy's actual label otherwise, and do not infer demand, pricing power or margins that the proxy cannot identify. Match average active units to period flows and test seasonality before annualising an interim result.

Distinguish an explanatory driver from a ratio back-solved to reproduce a growth assumption. Show what independently supports the forecast change in units, price, utilization, retention or other relevant components. Greater detail adds confidence only when those components are predictive and substantiated; do not invent undisclosed splits or a numerical elasticity to make the model look granular. Where a coarser forecast is the best supported approach, state its basis, limits and decision-sensitive range in the assumption note.

## Build the operating waterfall

Use the [competition and capital-return framework](competition-and-capital-returns.md) to test demand, price and margin assumptions against competitor capacity, product/pricing responses and customer/supplier bargaining. Link observed or inferred responses to the affected metrics and timing; a static peer list or qualitative risk paragraph is not a forecast of their economic effects.

1. **Historical calibration.** Reconcile segment/product/region revenue and costs to the official group totals before forecasting. Where a split is unavailable, identify an estimate and its residual. A total revenue tie does not establish that an undisclosed segment estimate is true.
2. **Demand and volume.** Choose matching drivers: industry demand x share, capacity x utilisation x operating days, stores x productivity, users x monetisation, or another supported structure. Separate production, shipments, sold volume and inventory. Where plants, mines or lines start and ramp at different times, forecast each one and check it against its own run rate. Test each period against every limit (capacity, ramp-up, permit or quota, demand) and say which one binds.
3. **Price and mix.** Match product, geography, channel, tax basis, quality and period to the volumes. Back-solve historical realised prices only from compatible observations. Forecast realised prices separately from spot benchmarks, with contract/lag/FX assumptions where relevant. When the mix is shifting, price each product and let the blended price follow from the mix.
4. **Segment revenue.** Calculate driver x realised price or the appropriate recognition formula. Separate owned retail revenue from licensing/royalties and other business models; do not assign the full retail sales of licensees to the licensor. Aggregate to group revenue.
5. **Costs and gross profit.** Build material/unit costs, labour, freight, conversion costs and fixed-cost absorption at the economic level the evidence supports. Look for a cost-of-sales-by-nature table in the MD&A or notes and calibrate to it. Give each cost its own driver (input quantity, output, units sold, or fixed per period) so unit cost falls with volume only where the cost is fixed. Estimate an undisclosed item inside a reported line (a royalty, a processing fee) from its rule; the remainder of that line tests the estimates. Prefer management's own split of the line when one exists: a small remainder can also come from offsetting errors, such as a cost counted in the wrong line. Choose either costs or margin as the independent lever for a line, not inconsistent independent assumptions for both. Cost = revenue - GP; GP = revenue x margin when margin is the chosen driver.
6. **Unit economics.** Show price, unit cost, unit GP and a clearly defined operating/after-tax contribution. Identify allocated overhead and unallocated financing/other items. Reconcile segment contributions to group earnings; a proxy is not reported company unit profit. A volume sensitivity saves only variable cost.
7. **Period roll-up.** Quarter/half-year flows sum to annual flows. Annual ASP is volume-weighted; annual margin is total GP / total revenue. Apply the [remaining-period identity](statement-forecast.md#income-statement-and-the-next-forecast-period) without treating an implied remainder as evidence for the full-year premise.
8. **Links into Statements.** Link revenue and costs/GP once into the matching fiscal period. Convert currency and scale explicitly from the documented units; do not infer them from a sheet name or prior model.

## Choose the business engine

For a more specific activity, select an applicable [sector reference](sectors/index.md). Use its operating chain and evidence questions to design the build; do not turn its miniature example into a company forecast or force unavailable physical units. Banking/insurance and other specialised capital models need their actual statements and funding mechanisms rather than an industrial working-capital schedule.

| Pattern | Modelling requirement |
| --- | --- |
| Unit-based manufacturing | Match product and geographic buckets; separate volume, realised price and mix; use weighted average selling prices |
| Segment-led industrial business | Retain disclosed segment definitions and historical cost/margin calibration; do not force unavailable unit volumes |
| Process manufacturing | Reconcile feedstock and product quantities, yields, tax basis, freight, shutdowns and contract timing |
| Resource extraction | Reconcile raw output, saleable production, inventory and sales; use matching unit denominators and separate cash cost, depreciation, policy costs and capex |
| Retail or licensing | Distinguish average store base, store maturity, productivity, transactions/ticket, owned/licensed mix and royalty recognition |
| Subscription or usage-based services | Bridge customers, retention, usage, pricing, recognition timing and service-delivery costs |

Product recipes or engineering ratios can cross-check the build; they do not override reconciled company actuals or establish undisclosed costs.

## Assumptions and revisions

Classify editable judgements explicitly, including formulas that encode an assumption such as holding the prior year's margin. Record historical basis, forecast rationale, source/date, output sensitivity and uncertainty. Preserve user-authored notes. Workbook colours may reflect an existing legend but do not determine a value's classification.

Build the base forecast from supported drivers. If target-implied calibration is requested, keep it as a labelled scenario alongside the evidence-based forecast.

Check implied remaining periods, capacity limits, changed mix, start dates, missing months and matching volume/price units. Rebuild affected costs when changing output. Do not assume a zero contribution means zero sales, or keep a run rate despite clear contrary evidence: resolve the definition and show scenarios.

The projection is complete when historical calibration, forecast drivers, costs/margins, unit economics, annual/interim sums and links to Statements are explicit. A list of segment growth rates without those bridges is a partial projection.
