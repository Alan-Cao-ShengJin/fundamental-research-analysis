# Synthetic calibration example: preserve the investment argument

Use the original, issuer-neutral [case asset](../assets/calibration-case.json) to practice reasoning and the [P/E comparison helper](../../valuation-thesis/scripts/compare_forward_pe.mjs) to check valuation arithmetic. The asset is a teaching fixture, not a universal company model. Its economic and forecast data are invented.

## What the evidence permits

Units rise from100 to110 at a price of10, so revenue rises from1,000 to1,100. Gross margin falls from40% to36%, leaving gross profit of396 versus400. Subtract operating expense83.5 and20% tax to obtain attributable profit250; divide by50 diluted shares for EPS5. The matched broker snapshot estimates EPS6.25 but does not supply its detailed driver build.

At a price of100, our forward P/E is20x and the broker-based P/E is16x. Applying a supported24x target multiple to our EPS gives120, or20% upside. Holding our current20x against our EPS gives100. Holding the broker-based16x while replacing its EPS with ours gives80: an earnings-downgrade scenario, not unchanged own P/E. The two return bridges give the same20 price gain: either0 earnings effect plus20 multiple effect on our forecast, or minus20 earnings effect plus40 multiple effect starting from the broker snapshot.

## One possible narrative

> Volume growth does not protect gross profit from higher costs. We forecast10% more units at unchanged prices, lifting revenue to1,100. Supplier quotations imply a36% gross margin against40% previously, leaving gross profit slightly lower at396. The investment case therefore depends on cost recovery as well as demand.
>
> We forecast attributable profit of250 and diluted EPS of5 after83.5 of operating expense and20% tax. The matched broker snapshot estimates EPS6.25. Our cost assumptions make us cautious about earnings, but without its detailed schedules we cannot allocate that gap precisely to individual drivers.
>
> At100, the shares trade at20x our forward earnings, versus16x on the broker estimate. A return to the relevant24x historical mean supports a target of120, or20% price upside. This depends on higher costs being manageable within an otherwise durable business; stable market share supports that interpretation but does not prove contractual pass-through.
>
> If customers resist repricing or the higher cost base persists, the former valuation regime may no longer fit. Contract implementation and the next reported margin and cash results will test that judgment. A lower share price alone would not resolve those operating risks.

This illustrates the chain from drivers to financial consequence, expectations, valuation and risk. It is not final one-page copy: adapt voice, selective detail, dates and sources to the evidence and house template. No fixed number of paragraphs or headings is required. Where a distribution or asset-value mechanism drives the investment, use that mechanism rather than copying this P/E case.

## Review a revision without losing the chain

Ask a fresh run to explain where the target multiple came from. A sound revision strengthens the valuation anchor while retaining the volume/cost mechanism and forecast gap. It does not replace the opening with several paragraphs of target arithmetic, raise EPS to match the broker, or describe the80 downgrade scenario as a pure no-re-rating price.

Check claim strength as well as calculations. Stable aggregate share does not establish that every customer stayed or that pricing power is unchanged. Potential cost recovery is not an implemented contract. A clean layout, correct ratios or an assertive headline cannot repair those unsupported inferences.
