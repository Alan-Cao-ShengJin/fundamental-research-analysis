# Payments, wallets and credit fintech

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Identify payment-network, merchant-acquiring, merchant-software, wallet, credit,
buy-now-pay-later (BNPL) and brokerage activities. A technology interface does not
remove credit, funding or safeguarding obligations.

## Operating build

Payment revenue = eligible volume × gross fee rate − incentives/rebates not already
deducted; net take rate = net payment revenue / matching volume. Separate
domestic/cross-border and merchant/product mix.

Credit income uses average balances, asset yields, funding costs and loss cohorts; do
not subtract funding twice from an already net spread. Link originations, amortisation,
collections and funding to the balance sheet.

## Evidence and calibration

Obtain gross/net definitions, the coverage of total payment volume (TPV), transaction
counts, rebates/contract renewals, fraud losses, merchant churn and acquisition costs.
For lending gather loss curves for origination cohorts compared at the same age,
charge-offs, recoveries, securitisation and warehouse-funding terms and retained
exposure.

Clarify customer-money ownership, safeguarding and any permissible interest benefit
using actual rules.

## Checks and valuation

Fast origination growth can dilute an aggregate loss ratio while older cohorts worsen.
Take rate is an estimate to explain through mix, competition and regulation, not a rate
assumed to decline in every business.

Value credit exposure with capital/credit economics and fee networks with supported cash
returns. Avoid treating customer balances as excess corporate cash.

## Worked example

Eligible payment volume of 1,000,000 at a 2% gross fee rate gives 20,000 of fees.
Subtracting 3,000 of rebates gives 17,000 of net revenue and a 1.7% net take rate.

Rebates have been deducted once.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector payments-fintech --example --out output/payments-fintech.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
