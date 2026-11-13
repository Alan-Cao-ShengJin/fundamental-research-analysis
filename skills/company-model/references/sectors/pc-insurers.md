# Property and casualty insurers

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A property and casualty insurer sells cover, for six months or a year at a time, against
damage, accident and liability: cars, buildings, cargo, crops, health and legal claims.
It collects the premium at the start and pays claims later, and invests the money in
between.

It earns in two ways: the **underwriting result**, which is premiums less claims and
costs, and the **investment income** on the money it holds. Which is larger differs by
market. Where prices are tightly regulated, underwriting is thin and investment income
matters as much. Where an insurer prices well, underwriting is most of the profit.

The amount of cover bought follows how many cars, buildings and businesses there are to
insure. The price follows competition and, for car insurance in many countries, the
regulator. Claims follow accidents, repair and medical costs, the weather, and what courts
award.

Four pairs of numbers get confused. Premiums **written**, which is what was sold, against
premiums **earned**, which is the part of the cover period that has passed. The **loss
ratio** against the **expense ratio**, which add up to the **combined ratio**: below 100%
is an underwriting profit. This year's claims against **changes to reserves** for earlier
years' claims. Premiums **before** against **after** the share passed to reinsurers.

Signs the card does not fit: the company sells long-term life and savings policies (see
the [life insurers card](life-insurers.md)); it is mainly a reinsurer, where single
catastrophes dominate; or it sells insurance for others without carrying the risk.

## 2. The driver tree

Build each line of business separately, car insurance apart from the rest, with history
beside the forecast. A line is whatever the company reports results by: a product or a
sales channel.

There are two routes to premiums. For an insurer whose share is steady, build from what
there is to insure. For one that is taking or losing share, build from its own policy
count: policies at the start times the share that renew, plus new policies, which follow
its advertising and its price against rivals.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| What is insured | Cars on the road and new cars sold, by type; or insured value and policy count for other lines | Leave it inside premium growth |
| Price | Average premium per policy, moved by competition and by pricing rules | Leave it inside premium growth |
| Premiums written | What is insured times price, with the company's share of the market | Premium growth by line |
| Premiums earned | Premiums written, spread over the cover period, so growth shows with a lag | Written premiums of the past year, averaged |
| Loss ratio | How often claims arise times the cost of each, over premiums earned. Catastrophes and changes to earlier years' reserves on their own rows | The reported loss ratio, with catastrophes and reserve changes named |
| Expense ratio | Commissions, advertising and running costs over premiums, on the company's own basis, earned or written | The reported ratio |
| Underwriting result | Premiums earned times one less the combined ratio | |
| Reinsurance | Premiums passed on and claims recovered | Net figures only |
| Investment income | Invested assets times the yield by asset type, with gains on shares apart | Assets times the reported yield |
| Other income and charges | Fees, interest on debt and tax | As reported |
| Solvency and payout | The capital rule that applies, whether a solvency ratio or a limit on premiums against capital, profit kept, dividends and buybacks | As reported |

## 3. The data behind the rows

- **Company.** Some insurers publish premiums every month. Most report twice a year or
  quarterly: premiums and the combined ratio by line, the loss and expense ratios,
  catastrophe losses, investment yield and asset mix, and solvency. Annual reports add
  tables showing how each past year's claims estimates have developed.
- **Industry:**

| Source | What exists |
| --- | --- |
| Regulator | Industry premiums by line. Rules on car-insurance pricing and on commissions |
| What is insured | New car sales and the number of cars in use, with the share that are electric. Distance driven. Property and trade activity |
| Claims | Records of storms, floods and earthquakes. Indices of repair and medical costs, and used-car prices |
| Prices | Rate changes filed with regulators, where filings are public |
| Reinsurance | The price changes at the yearly renewal of reinsurance contracts |
| Markets | Bond yields and share indices, for investment income |

- **What leads profit.** Car sales. Changes in pricing rules. Storm and flood seasons.
  Repair-cost inflation. Reinsurance renewals. Bond yields.
- **Backtest.** Premiums earned times one less the combined ratio against the underwriting
  result. Invested assets times yield against investment income.

## 4. Costs and margin

- Claims are most of the cost. A point on the loss ratio is a point of premiums, which is
  a large share of a thin underwriting profit.
- The insurer holds assets worth a multiple of its yearly premiums, so investment income
  often matters as much as underwriting.
- Commissions rise when insurers fight for share, and are capped by regulators in some
  markets.
- Reserves are estimates. Releasing them lifts this year's profit and adding to them cuts
  it, so the trend in past estimates matters.
- New kinds of risk are priced before the claims are known. Electric cars are one: their
  claims have run above those on petrol cars.
- Lines sold for policy reasons, such as crop and public health cover, earn little.

## 5. Capacity, capex and working capital

- Solvency rules limit how much premium can be written on a given amount of capital, and
  how much can be held in shares.
- Reinsurance protects capital from a single large event, at a price that rises after a
  bad year.
- An insurer needs no fixed assets to speak of. Its capital is its capacity.

## 6. Cycle, policy and traps

- Prices move in a cycle. Good results draw in competition and prices fall. Losses drive
  capacity out and prices rise.
- For an insurer of property, a catastrophe can take a year's underwriting profit. Treat
  a year without one as lucky, not as normal.
- Rising repair, medical or legal costs make past reserves too low.
- Traps:
  - growth in premiums written read as growth in profit;
  - a combined ratio flattered by reserve releases or by a year without catastrophes;
  - this year's result mixed with changes to earlier years';
  - gains on shares inside investment income;
  - losses on bonds that are in book value but not in profit;
  - profit that rules require to be handed back to policyholders when it is too high;
  - a group's figures used for its property and casualty business;
  - results under different accounting rules compared without adjusting.

## 7. What investors argue about, and the yardstick

- Whether the combined ratio holds as competition and claims costs rise.
- Whether reserves are adequate.
- What falling bond yields do to investment income.
- Whether the dividend is covered by underwriting and investment together.

Yardstick: P/B against return on equity, with P/E beside it, and P/E first where returns
are high and steady
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

An insurer earns premiums of 100. Claims take 70 and costs 27, a combined ratio of 97%,
so the underwriting profit is 3. It holds invested assets of 200 earning 3.5%, which is 7.
Profit before tax is 10.

One more point on the combined ratio costs 1, a tenth of profit. So does a fall of half a
point in the investment yield. A storm that adds 3 points to claims takes 30% of the
year's profit.

All figures are invented. They show the relationships, not a forecast.
