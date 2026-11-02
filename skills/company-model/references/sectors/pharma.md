# Drug development and commercial medicines

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Separate marketed products, clinical assets, royalties/licences and platforms, with
geographic rights and development obligations.

## Operating build

Product sales follow a compatible patient funnel: incident cases or the existing patient
population, as appropriate → diagnosed and eligible patients → treated share →
duration/adherence × net realised price. Avoid repeating a restriction already present
in the starting patient count.

Roll launches, competition and patent/exclusivity erosion by asset. Build trial and
commercial spending from programmes and dates, not a percentage of sales.

Pipeline risk-adjusted net present value (rNPV) discounts timed contingent cash flows
and stage-specific costs through an explicit probability tree.

## Evidence and calibration

Use trial registries/protocols, full results, regulatory reviews/labels, payer evidence,
patent records and issuer contracts. Record primary endpoints, effect size/confidence
intervals, population, comparator, safety, follow-up and revisions.

Distinguish the probability of passing the next stage from the cumulative probability
of reaching commercialisation. Start with relevant, dated stage and indication base
rates, then explain asset-specific adjustments using clinical and regulatory evidence.

## Checks and valuation

A filing is not approval; a secondary endpoint is not a successful primary endpoint. Do
not compare unmatched trials as equivalent.

Track correlation across related assets, net pricing, milestone/royalty rights, time to
next catalyst, runway and financing dilution. Calculate rNPV from the cash-flow tree
rather than peak sales × success probability; avoid double-counting shared platform
value, overhead or the same development spend.

## Worked example

A patient population of 100,000, 50% diagnosis, 20% eligibility and 10% treated share
gives 1,000 treated patients. A separate pipeline illustration has a 30% probability of
commercial cash flows with a present value of 200.

Less 10 of committed trial costs paid regardless of success, rNPV is 50.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector pharma --example --out output/pharma.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
