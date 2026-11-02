# Banks and deposit-funded lending

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Use a banking balance sheet and regulatory-capital model. Deposits and financial
liabilities fund the operating business; a generic industrial enterprise-value (EV)
bridge that subtracts net debt is unsuitable.

## Operating build

Net interest income = average interest-earning assets × yield × period fraction −
average interest-bearing funding × cost × period fraction. Split loan/funding pools only
where useful and supported.

Bridge allowance = opening + provision − gross charge-offs + recoveries ± other
identified movements; if using net charge-offs, do not add recoveries again. Build fees,
operating costs, tax, risk-weighted assets (RWA), regulatory capital and distributable
surplus.

## Evidence and calibration

Gather average versus closing loans/deposits, repricing and maturity schedules and rate
curves, deposit mix, concentration and sensitivity of deposit rates to market rates,
loan origination cohorts, delinquencies/stage migration, collateral and sector exposure.
Obtain the applicable capital definition, buffers and distribution restrictions from
current local rules.

Securities book classifications, unrealised losses, hedges and liquidity eligibility
matter even when losses are not recognised in earnings.

## Checks and valuation

Low credit losses during rapid lending growth are not a cycle norm. Stress funding
outflows, credit migration, collateral and rates jointly.

Capital growth constrains balance growth and dividends. Relate sustainable return on
equity (ROE) or return on tangible common equity (ROTCE) to the corresponding book-value
base and cost of equity; do not compare ROE with tangible book without adjustment or
treat a low book multiple as an investment conclusion.

## Worked example

Average earning assets of 1,000 yielding 6%, less average funding of 900 costing 3%,
produce annual net interest income of 33. An opening allowance of 20 plus provision 4
less gross charge-offs 5 plus recoveries 1 closes at 20.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector banks --example --out output/banks.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
