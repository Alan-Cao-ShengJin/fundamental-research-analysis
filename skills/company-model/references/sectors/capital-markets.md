# Asset managers, exchanges, brokers and market data

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Separate client-asset fee franchises, activity-linked exchanges, investment
banking/trading, balance-sheet brokerage and subscription data.

## Operating build

Assets under management (AUM) at the end of the period = opening + net flows +
market-value movements + foreign-exchange movements + acquisitions - disposals; average
fee-earning AUM for the period × net fee rate for that same period gives management fees. Model performance
fees separately.

Exchanges use contract/trade/clearing volumes × net unit fees plus
data/listings/technology. Brokers separate the interest spread earned on customer cash,
transactions and corporate-finance fees; ratings depend on issuance mix/volume and
recurring research/data.

## Evidence and calibration

Gather net versus gross flows, product/fee mix, average client balances, activity and
volatility measures, rate sensitivity, compensation, clearing guarantees and
regulatory/net capital. Isolate acquired AUM/data revenue.

Distinguish client assets from assets owned by the group. Check the ownership, funding
and segregation of client cash separately.

## Checks and valuation

Avoid perpetuating a high-rate cash spread, trading boom or peak issuance. Fixed
platform costs and variable compensation have different leverage.

Reconcile fee compression and market returns to per-share cash/capital generation.
Choose cash/earnings methods for fee businesses and equity/capital methods for
risk-taking balance sheets, with appropriate parts reconciliation.

## Worked example

Opening AUM of 1,000 plus 50 net inflows, 100 market appreciation and a 20
foreign-exchange loss closes at 1,130. An illustrative midpoint average of 1,065 at a 1%
annual fee rate generates 10.65 of management fees.

Use actual average balances when available.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector capital-markets --example --out output/capital-markets.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
