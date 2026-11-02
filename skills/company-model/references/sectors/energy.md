# Oil, gas, refining and contracted energy infrastructure

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Choose upstream production, refining, midstream or liquefied natural gas (LNG), or
services. Clean-energy equipment is usually manufacturing; owned generation may instead
need utilities/project economics.

## Operating build

For upstream production, roll existing-field decline, new projects and outages into
period-average production and sold volumes. Realised price bridges benchmark,
quality/location differentials, contracts and hedges without counting hedged volume
twice.

Refinery throughput = available capacity × utilisation; margins derive from captured
product/feedstock spreads. Midstream uses enforceable contract volumes, tariffs,
escalation, counterparties and expiries; services use active rigs/vessels, utilisation
and daily rates.

## Evidence and calibration

Obtain reserves by category/price basis, decline curves, productive inventory,
production versus sales, field operating costs, transport and taxes, sustaining versus
growth investment, hedges and abandonment timing. Reconcile commodity units, currencies
and royalties.

Energy Information Administration (EIA) data, regulatory reserves disclosures and issuer
technical reports and contracts are useful starting sources, not substitutes for
verified asset data.

## Checks and valuation

Production growth can require large replacement investment and dilution. Free cash after
all investment differs from cash after sustaining investment; label both accurately.

Depleting assets have finite supported lives unless replacement is explicitly funded.
Use asset-level cash flows, through-cycle estimates and contractual cash flows with
price, differential and funding stress, not peak spot-price perpetuities.

## Worked example

Opening output of 100 barrels per day, 10% decline and 20 barrels per day of new output
gives 110 at period end. A linear average of 105 over 365 days gives 38,325 barrels.

A benchmark of 70 less a 5 differential, with 20% hedged at 60, gives a realised price
of 64.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector energy --example --out output/energy.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
