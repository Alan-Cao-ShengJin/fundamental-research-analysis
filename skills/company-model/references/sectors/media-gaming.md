# Games, media and content rights

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast.

## Choose the relevant activity

Separate live games, project releases, subscriptions, advertising, licensing and owned
versus distributed content rights.

## Operating build

Games: active users × paying share × revenue per paying user over the same period, plus
separately recognised ads/licensing. Model titles and launch cohorts through launch,
retention, payer conversion and decay.

Subscription revenue uses average paying subscribers × average revenue per user (ARPU)
for the period; subscriber churn belongs in the subscriber roll-forward, not a second
multiplier on an already churn-adjusted average. Bridge content opening assets +
capitalised investment − amortisation/impairment/disposals = closing assets.

## Evidence and calibration

Obtain recognised revenue versus billings/bookings/gross receipts, platform fees and
rights ownership; release timing, development/marketing budgets, content cash
commitments and amortisation profiles; licence/approval calendars and talent
dependencies. Audience/download measures need conversion and revenue evidence.

## Checks and valuation

Test release delays through both competitive windows and spending, not a simple
sales-date shift. Capitalisation can separate profit from cash without proving
misconduct.

Value cash flows over the supported lives of content and intellectual-property rights.
Assess optional launches with explicit probabilities and spending. Reconcile platform
value with any title cash flows already included, and do not assume a blockbuster
lasts indefinitely.

## Worked example

10,000 average monthly users, a 5% paying share and monthly revenue of 20 per payer
produce 30,000 of revenue over three months. Content assets of 100 plus 60 capitalised
spending less 40 amortisation leave 120; the 20 cash-versus-amortisation gap is shown
separately.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model. Generate the matching example with:

```powershell
python skills/company-model/scripts/sector_plan.py --sector media-gaming --example --out output/media-gaming.json
```

Omit `--example` to create a blank scaffold. Replace its period and inputs with
the relevant observations and assessed assumptions before real use.

Adaptation credit and licence: [notice](NOTICE.txt).
