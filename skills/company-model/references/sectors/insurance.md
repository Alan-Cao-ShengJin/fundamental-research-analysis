# Insurers, reinsurers and brokers

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Separate property and casualty (P&C), life/annuities, health, reinsurance and fee-based
brokerage. International Financial Reporting Standard 17 (IFRS 17), local statutory
accounts and management value measures are not interchangeable.

## Operating build

P&C: exposure × net rate → written premium → earned premium. Apply the current
accident-year loss ratio and the matching expense ratio to estimate underwriting
contribution; show prior-year reserve development separately. Life: bridge new business, persistency,
expenses, guarantees and investment spread, and reconcile the contractual service margin
(CSM) and embedded-value movements using the actual framework.

Health: average members × net premium with utilisation/severity-driven claims. Brokerage
uses eligible premium × commission plus fees.

## Evidence and calibration

Seek gross/net reinsurance bases, claims-development tables showing estimates and
payments by accident year and time since the claim, catastrophe assumptions, recoverable
counterparties and limits. For long-duration products obtain surrender behaviour,
duration mismatch, guarantee costs and reinvestment yields.

Bridge investment credit/liquidity risk, group and entity capital, parent cash and
remittance capacity.

## Checks and valuation

Reserve releases and assumption changes can boost reported results without better
current underwriting. Do not equate the contractual service margin or value of new
business (VNB) with available cash or add them to equity value without a consistent
valuation framework.

Use earnings, book value, residual income or business-value methods on a consistent
basis and stress asset/liability economics; group solvency does not prove subsidiary
capital is distributable.

## Worked example

Earned premiums of 100, a 60% current accident-year loss ratio and a 25% expense ratio
produce 15 of current underwriting contribution. A prior-year reserve release of 5 lifts
reported contribution to 20 without changing current underwriting.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector insurance --example --out output/insurance.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
