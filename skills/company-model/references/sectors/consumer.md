# Consumer brands, stores and franchising

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Choose branded goods, owned retail/restaurants, franchises/licensing, durable
replacement demand or a marketplace. Sales across a franchise network are not
automatically the issuer's recognised revenue.

## Operating build

Brand revenue uses sold units × net realised price by category/channel; reconcile
shipments to distributors, sales to end customers, returns and channel stock. Store
revenue uses time-weighted operating stores × productivity, with opening cohorts that
reflect ramp-up, closures, maturity and sales diverted from existing stores.

Same-store growth applies only to its matching eligible pool. Franchise revenue uses
contract royalties/fees; franchisee economics constrain sustainable opening.

For a branded apparel or sportswear group, build each brand separately: stores by
format (own retail, franchise, kids, outlet) × sales per store, plus online as its own
line with its share of sales, and reconcile the retail sell-through the company reports
(all channels, at retail value) to recognised revenue through the wholesale discount,
franchise take and channel inventory. Carry discount depth, channel inventory months
and gross margin by channel as drivers, because they set margin before volume does; a
brand forecast as one growth rate with its store counts unused is not a build.

## Evidence and calibration

Gather customer traffic, purchase conversion and average transaction value,
units/price/mix, promotions, comparable-store definitions, opening dates, rents/wages,
inventory/markdowns, royalties and channel credit. Price changes need volume elasticity
and competitive responses.

Separate acquisitions, foreign-exchange movements, replacement purchases and purchases
by first-time users. Margin bridges need inputs, logistics, waste and marketing, not
just the best peer margin.

## Checks and valuation

Closing weak stores changes the same-store denominator. Advertising cuts, longer
supplier-payment terms and stock reduction can improve current cash/profit without
better sustainable demand.

Link new-store cash flows, capital expenditure and lease commitments to funded returns. Choose
consumer cash/earnings and peer checks consistent with owned/licensed mix and capital
intensity.

## Worked example

10 opening stores plus 2 openings less 1 closure gives 11 closing stores. If changes
occur evenly through the year, 10.5 average stores × 100 monthly sales per store × 12
months produces 12,600.

A real build needs the opening dates and store maturity curve.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector consumer --example --out output/consumer.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
