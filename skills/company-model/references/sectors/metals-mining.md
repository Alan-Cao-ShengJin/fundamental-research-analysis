# Metals, operating mines and development projects

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Separate operators, developers/explorers, royalty interests and processing. A machinery
supplier is not a miner simply because its customers mine.

## Operating build

Payable metal = ore processed × grade × recovery × the share of recovered metal for
which the buyer pays, with compatible units; sales reconcile production, opening/closing
stock and ownership. Bridge benchmark prices to realised net prices through
treatment/refining, penalties, logistics and hedges.

For bulk commodities such as coal or iron ore, saleable tonnes = raw tonnes × the yield of
each processing route, plus any product sold unprocessed. Price each product from the
matching benchmark, adjusted for quality (for coal, calorific value). Apply royalties,
levies and domestic-supply obligations by their actual rules, which often step with
price and grade.

Cost per ore tonne and required ore throughput link falling grade to metal cost. Model
mine plans, development, sustaining investment, royalties/tax and closure cash by
material asset.

## Evidence and calibration

Use current technical/reserve reports, mine plans, jurisdiction rules, issuer cost
reconciliations, output/sales and ownership schedules. Separate resources from
economically supported reserves and substantiate price and cost assumptions.

Record all-in sustaining cost (AISC) components and denominator: coproduct/byproduct
credits and sustaining expenditure differ across companies. Obtain debt, country/permit
and funding conditions.

## Checks and valuation

Do not subtract sustaining capex twice when a chosen AISC already includes it. Mining
richer ore first to improve current results (high-grading) can raise current cash while
weakening future economics.

Finite reserve-supported operations do not justify an unfunded perpetual terminal value;
replacement scenarios need timing, capex and permits. Use asset net present values,
finite-life cash flows and development scenarios adjusted for risk with commodity and
capital stress, not an unsupported universal cost-percentile price rule.

Locate assets on a comparable industry cost curve to assess downside resilience and closure risk. Compare P/NAV on consistent ownership, commodity decks, discount dates and project probabilities; a cost percentile alone does not determine price.

## Worked example

Processing 100,000 tonnes of ore at 2% grade, 80% recovery and 95% payability produces
1,520 tonnes of payable metal. With 20 in opening stock and sales of 1,500, closing
stock is 40.

Lower recovery reduces available stock; it does not automatically change the entered
sales forecast.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector metals-mining --example --out output/metals-mining.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
