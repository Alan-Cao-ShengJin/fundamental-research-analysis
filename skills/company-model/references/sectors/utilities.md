# Regulated utilities and power projects

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Separate regulated jurisdictions, merchant generation, contracted assets with power
purchase agreements (PPAs), development-for-sale and engineering, procurement and
construction (EPC) contracts. Their risk, capital ownership and revenue mechanisms
differ.

## Operating build

The regulated asset base used to set allowed returns rolls approved eligible additions,
depreciation, disallowances and net book value of disposals, plus jurisdiction-specific ADIT/CWIP adjustments. Do not subtract gross retired cost again after its accumulated depreciation has been removed. Equity return uses the relevant average
rate base × equity share × allowed return on equity (ROE), then earned-versus-allowed
differences and lag.

Build other revenue-requirement components separately. Generation uses capacity in
megawatts (MW) × available hours × utilisation × realised price per megawatt-hour
(MWh). Model fuel, variable costs and capacity or contract income separately.

Do not count availability twice if hours already reflect it.

## Evidence and calibration

Gather actual rate cases, approved versus planned capex, construction milestones,
rate-recovery dates, load/customer contracts and bills. For owned projects verify
ownership, commissioning and output sale terms; for EPC verify acceptance and
construction working capital.

Trace debt/equity financing, noncash capitalised interest, regulatory assets,
rating/covenant definitions and environmental/retirement obligations.

## Checks and valuation

An allowed return is not an earned return; capex or a connection request is not assured
revenue. Earnings per share can rise through capitalised interest without cash.

Test project overruns, recovery, funding dilution and customer affordability together.
Use cash-flow, dividend-capacity or sum-of-the-parts methods suited to each jurisdiction
and project without treating merchant exposure as regulated earnings.

Compare P/E against sustainable rate-base growth and funded EPS growth; use EV/RAB where the debt, regulatory and asset boundaries match.

Rate-base accounting follows local regulation; see [FERC retirement accounting](https://www.ferc.gov/accounting-questions-and-answers).

## Worked example

An opening regulated asset base of 100 plus 20 approved additions less 5 depreciation
and 2 of net book disposals closes at 113. An illustrative average of 106.5 with a 50% equity
share earns 5.325 at 10% allowed ROE, but only 4.7925 at 9% earned ROE.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector utilities --example --out output/utilities.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
