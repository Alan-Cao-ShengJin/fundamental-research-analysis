# Synthetic calibration example: preserve the investment argument

Use the original, issuer-neutral [case asset](../assets/calibration-case.json) to practice reasoning and the [P/E comparison helper](../../valuation-thesis/scripts/compare_forward_pe.mjs) to check valuation arithmetic. The asset is a teaching fixture, not a universal company model. Its economic and forecast data are invented.

## What the evidence permits

Units rise from 100 to 110 at a price of 10, so revenue rises from 1,000 to 1,100. Gross margin falls from 40% to 36%, leaving gross profit of 396 versus 400. Subtract operating expense 83.5 and 20% tax to obtain attributable profit 250; divide by 50 diluted shares for EPS 5. The matched broker snapshot estimates EPS 6.25 but does not supply its detailed driver build.

At a price of 100, our forward P/E is 20x and the broker-based P/E is 16x. Applying a supported 24x target multiple to our EPS gives 120, or 20% upside. Holding our current 20x against our EPS gives 100. Holding the broker-based 16x while replacing its EPS with ours gives 80: an earnings-downgrade scenario, not unchanged own P/E. The two return bridges give the same 20 price gain: either 0 earnings effect plus 20 multiple effect on our forecast, or minus 20 earnings effect plus 40 multiple effect starting from the broker snapshot.

## One possible narrative

> Volume growth does not protect gross profit from higher costs. We forecast 10% more units at unchanged prices, lifting revenue to 1,100. Supplier quotations imply a 36% gross margin against 40% previously, leaving gross profit slightly lower at 396. The investment case therefore depends on cost recovery as well as demand.
>
> We forecast attributable profit of 250 and diluted EPS of 5 after 83.5 of operating expense and 20% tax. The matched broker snapshot estimates EPS 6.25. Our cost assumptions make us cautious about earnings, but without its detailed schedules we cannot allocate that gap precisely to individual drivers.
>
> At 100, the shares trade at 20x our forward earnings, versus 16x on the broker estimate. A return to the relevant 24x historical mean supports a target of 120, or 20% price upside. This depends on higher costs being manageable within an otherwise durable business; stable market share supports that interpretation but does not prove contractual pass-through.
>
> If customers resist repricing or the higher cost base persists, the former valuation regime may no longer fit. Contract implementation and the next reported margin and cash results will test that judgment. A lower share price alone would not resolve those operating risks.

This illustrates the chain from drivers to financial consequence, expectations, valuation and risk. It is not final one-page copy: adapt voice, selective detail, dates and sources to the evidence and house template. No fixed number of paragraphs or headings is required. Where a distribution or asset-value mechanism drives the investment, use that mechanism rather than copying this P/E case.

## Review a revision without losing the chain

Ask a fresh run to explain where the target multiple came from. A sound revision strengthens the valuation anchor while retaining the volume/cost mechanism and forecast gap. It does not replace the opening with several paragraphs of target arithmetic, raise EPS to match the broker, or describe the 80 downgrade scenario as a pure no-re-rating price.

Check claim strength as well as calculations. Stable aggregate share does not establish that every customer stayed or that pricing power is unchanged. Potential cost recovery is not an implemented contract. A clean layout, correct ratios or an assertive headline cannot repair those unsupported inferences.
