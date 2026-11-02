# Internet marketplaces, advertising and platforms

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Separate advertising, third-party marketplaces, owned inventory, subscriptions, cloud
and new activities. Principal versus agent treatment determines revenue.

## Operating build

Advertising: delivered impressions / 1,000 × effective revenue per thousand impressions
(eCPM); explain users, engagement, advertisements per unit of user activity and
sell-through feeding impressions in compatible time units. Marketplace gross merchandise
value (GMV): buyers × frequency × net order value; revenue: eligible GMV × net take
rate.

Owned-goods sales and commissions are not additive measures of the same sale. New
activities need order-level contribution, customer acquisition, retention and an
achievable scale and path to positive contribution.

## Evidence and calibration

Gather operating-metric definitions, net/cancelled/refunded GMV, geographic user
monetisation, advertiser/customer retention, incentives, fulfilment costs and merchant
settlement obligations. For cloud and artificial-intelligence services trace contracted
demand, consumption, compute capacity, utilisation, depreciation, cash capex and
commitments.

Treat gross transaction balances and customer cash separately from owned liquidity.

## Checks and valuation

User or transaction growth can coincide with falling monetisation and cash contribution.
Check subsidy dependence and the limits of engagement/advertisements per unit of user
activity.

Reconcile share-based compensation (SBC) and per-share dilution, segment losses and
shared costs. Sum-of-the-parts valuation (SOTP) can separate business models but must
reconcile investments, ownership, tax and group costs; never add a new-business option
already embedded in the same cash forecast.

## Worked example

100,000 users receiving 20 impressions each produce 2,000,000 impressions. At 5 per
thousand impressions, advertising revenue is 10,000.

Separately, marketplace GMV of 1,000,000 at an 8% net take rate produces 80,000 of
recognised fee revenue.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector internet-platform --example --out output/internet-platform.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
