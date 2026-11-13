# Oil services

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

Oil service companies sell work and equipment to oil and gas producers. There are four
kinds, and large companies have several.

- **Drilling contractors** hire out rigs with their crews by the day, offshore or on
  land.
- **Well services**: fracturing, logging, cementing, directional drilling and surveys,
  priced by the job, the stage or the day.
- **Offshore vessels and construction.** Support vessels are hired by the day. Building
  and installing platforms and pipelines is contract work, booked as it progresses.
  Build it on the [construction and engineering card](construction-engineering.md).
- **Equipment**, sold and serviced: wellheads, pumps, pipe and subsea systems. Build it
  from orders and backlog, as on the [machinery card](machinery.md).

Producers' capex budgets decide demand. Budgets follow the oil and gas price with a lag
of several months on the way up, and are cut at once on the way down. Spending on shale
turns fastest. Offshore and state-owned producers' spending turns slowly and runs for
years.

A contractor owned by a state producer gets most of its work from that parent. Its
revenue follows the parent's capex budget, and the two agree prices between them.

Numbers that get confused:

- Rigs **owned**, rigs **offered for work**, rigs **under contract** and rigs
  **working**. The share in use means different things on each base.
- The day rate on **new contracts** against the **average** rate the fleet earns, which
  catches up only as old contracts end.
- **Backlog**, which is contracted days times their rates, against revenue.
- Revenue that includes **costs recharged** to the customer and fees for moving a rig.

Signs the card does not fit: the company produces oil and gas (see the
[producers card](oil-gas-producers.md)); it owns pipelines; or it makes equipment mainly
for other industries.

## 2. The driver tree

Build each kind of work and each region separately, with history beside the forecast.

Where one parent is most of the business, build from the parent's capex budget: the part
of it spent on services of this kind, and the share of that the company wins. Use days
worked and day rates as the check.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Customers' spending | Producers' capex budgets by region and by onshore, offshore and shale, from their own guidance | Growth in rigs at work |
| Fleet | Rigs or vessels by type: opening fleet, plus delivered and brought back into service, less sold, scrapped or laid up. Owned and hired-in apart, since a hired rig brings a rental cost | The fleet as reported |
| Days worked | For each rig, the days under its contract. For days not yet contracted, the share of the market's fleet that is working | Operating days by rig type as the company reports them, moved with the fleet and its share in use |
| Day rate | Each contract at its own rate until it ends, then the rate on new contracts | Average daily income by rig type as reported, moved towards the rate on new contracts |
| Drilling revenue | Days worked times day rate, plus fees for moving rigs and costs recharged | |
| Well services | Jobs, stages or crews working, times the price of each. They follow rigs at work and wells completed in the region | Where no volumes are given: last year's revenue by line, moved with customers' spending in the region and with what management says about price |
| Vessels and surveys | Vessels: days worked times day rate, owned and hired-in apart, as for rigs. Surveys: the area or length surveyed times the price | Revenue by line, moved with customers' spending |
| Equipment and contracts | Orders, backlog and the rate at which backlog becomes revenue | Revenue growth by line |
| Operating costs | Crew, maintenance and supplies for each working day. A laid-up rig still costs something | Cost per working day, or the margin by line |
| Bringing rigs back | The one-off cost of returning an idle rig to work | A named row |
| Depreciation and capex | New rigs, upgrades and the periodic surveys each rig must pass | The guided figure. With none, announced projects over their build years, plus other capex at its recent level |
| Write-downs | Rigs unlikely to work again | A named row |
| Interest and currency | Debt times its cost. Day rates are often in dollars and costs in the home currency, so the exchange rate moves the margin and the value of dollar debt | As reported |

## 3. The data behind the rows

- **Company.** Many drilling contractors publish a fleet status report every quarter or
  month. It lists each rig, its customer, the contract dates and often the day rate.
  Others, including state-owned contractors, give only operating days, the share in use
  and average daily income by rig type. Service companies give revenue and margin by
  region and by line each quarter. Most give backlog.
- **Industry:**

| Source | What exists |
| --- | --- |
| Activity | Rigs at work, weekly for the US and monthly elsewhere (Baker Hughes). Fracturing crews at work |
| Customers | Producers' capex budgets, mostly set at the start of the year, and changes to them |
| Rigs | Share in use and day rates by rig type (Westwood, Esgian), quoted in the trade press. Contract awards, announced one by one |
| Prices | Oil and gas prices |

- **What leads revenue.** Producers' budgets lead the year's activity. Rigs at work lead
  well services. A contract award leads revenue by six to eighteen months. The rate on
  new contracts leads the average rate.
- **Backtest.** Days worked times day rate against drilling revenue. Revenue by region
  against customers' spending there.

## 4. Costs and margin

- A working rig costs much the same to run whatever its day rate, so a change in the rate
  goes almost wholly to profit.
- Prices rise only when most of the fleet is working. Below that, contractors bid against
  each other and rates fall towards running cost.
- In an upturn, crews and supplies cost more, which takes back part of the gain.
- Laying a rig up saves most of its cost, and bringing it back is expensive.

## 5. Capacity, capex and working capital

- Fleets are built in booms and last for decades, so too many rigs can hold rates down
  for years after spending recovers.
- New rigs are ordered only when rates cover their cost. The gap between the two shows
  how far the cycle has to run.
- Much of the industry carries debt from the last boom.
- State-owned customers pay slowly, so receivables are long.

## 6. Cycle, policy and traps

- This is the most cyclical part of the oil industry. It lags the oil price on the way up
  and falls with it at once.
- A state producer told to raise output keeps its contractors busy whatever the price.
- Traps:
  - backlog that the customer can cancel for a small fee;
  - the rate on new contracts read as the fleet's average;
  - a share in use quoted without the laid-up rigs;
  - fees for moving rigs read as recurring revenue;
  - a peak margin treated as normal;
  - prices agreed with a parent company that is also the main customer;
  - optional contract extensions counted as firm.

## 7. What investors argue about, and the yardstick

- How long the upturn in spending lasts.
- Whether rates will rise far enough to justify new rigs.
- Whether gains come from price or only from activity.
- Whether cash is returned or spent on the fleet.

Yardstick: EV/EBITDA and P/E on mid-cycle earnings, meaning earnings at the day rates
and activity of an average year in the cycle, with P/B and the fleet's replacement cost
beside them ([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A contractor has 10 rigs. Eight work all year at 100,000 a day: revenue is 292m. A
working rig costs 50,000 a day and an idle one 10,000, so costs are 153.3m and the margin
is 138.7m.

Two contracts end and are renewed at 130,000 a day. Revenue rises 21.9m, costs do not
change, and the margin rises 16%.

A ninth rig goes to work at 100,000 a day. Revenue rises 36.5m and costs 14.6m, so the
margin rises 21.9m again.

All figures are invented. They show the relationships, not a forecast.
