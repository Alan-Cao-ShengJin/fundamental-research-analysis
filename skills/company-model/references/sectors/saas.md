# Subscription and usage software

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Separate contracted subscriptions, metered consumption, implementation and resale. A
software label does not establish recurring economics.

## Operating build

Bridge opening annual recurring revenue (ARR) through new sales, expansion, contraction,
churn, acquisitions and FX. Reconcile closing ARR to period revenue through service
timing.

Alternatively use active seats × net seat price, or measured consumption × net unit
price; do not count the same expansion twice through net revenue retention (NRR) and
another growth assumption. Model sales capacity, customer-acquisition payback,
hosting/inference costs, support and renewal cohorts locally.

## Evidence and calibration

Obtain KPI definitions and changed cohorts; gross and net retention, remaining
performance obligations (RPO) and the portion expected within the next year, contract
duration, cancellations and revenue recognition; sales-representative productivity and
time to full productivity; cloud commitments and capitalised development; share
compensation, buybacks and net dilution. Use issuer filings/call detail and
customer/product evidence; distinguish bookings, billings, ARR, cash and recognised
sales.

## Checks and valuation

Growth in remaining performance obligations from longer contracts is not necessarily
stronger consumption. Test an artificial-intelligence product through paid adoption,
usage, net price and delivery cost.

Retention deterioration, longer payback and gross-margin pressure should constrain the
same forecast. Value supported post-investment cash flows and per-share claims;
ARR/revenue multiples need an explicit mature-margin and retention bridge.

Do not deduct share-based compensation (SBC) twice through both a cash haircut and
equivalent dilution without reconciling the claim.

## Worked example

With opening ARR of 100, new ARR of 25, expansion of 15 and churn of 10, closing ARR is
130. Net revenue retention is 105%; the new ARR is excluded from that retention
calculation.

ARR and recognised period revenue remain separate measures.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector saas --example --out output/saas.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
