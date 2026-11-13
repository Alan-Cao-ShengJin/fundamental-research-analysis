# Power generation

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A generator owns power plants and sells the electricity: coal, gas, nuclear, hydro, wind,
solar and batteries. Some also sell heat, and some are paid for keeping capacity ready.

The price is set in one of four ways, and one company can have all four.

- **A long-term contract** at a fixed or indexed price, often for ten to twenty years.
  This includes prices guaranteed by a government scheme.
- **The wholesale market.** The plant earns the market price, and the company sells much
  of its output a year or more ahead to fix it.
- **Yearly and monthly contracts** struck with large users and retailers, as in China,
  with a part sold at the spot price.
- **A tariff set by the government**, sometimes with a subsidy on top.

Electricity demand follows the economy and the weather. What a single plant sells depends
on its place in the queue. Wind, solar, hydro and nuclear run when they can, and coal and
gas fill what is left. So a coal plant's running hours fall as wind and solar are built
around it. Hydro follows rainfall. Wind and solar follow the weather, and lose output
when the grid cannot take it.

Numbers that get confused:

- **Capacity** the company controls against its **attributable** share, since many
  plants are part-owned.
- Electricity **generated** against electricity **sold**, after the plant's own use.
- **Running hours**, which is output over capacity. The same thing as a share of the
  year is the **load factor**.
- The price **with** and **without** sales tax.
- The cost of fuel **per unit of electricity** against the price of coal or gas.
- Profit **with** and **without** changes in the value of forward sales not yet
  delivered.

Signs the card does not fit: the plants sit in a regulator's asset base and earn an
allowed return (see the [regulated networks card](regulated-networks.md)); the company
makes turbines or panels; or it builds plants for other owners and keeps none.

## 2. The driver tree

Build each fuel and each market separately, with history beside the forecast.

A company that builds wind or solar farms and sells stakes in them needs more rows. The
gain on each stake is the price less the book value of the share sold, booked when the
sale completes. The fee for building the buyer's share is booked as construction
proceeds. Fees paid to cancel a project and write-downs are one-off rows. Keep all of
these apart from the profit on electricity, and forecast only the sales the company has
announced or guided.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Capacity | Opening capacity, plus plants started, less plants closed, by fuel and market. Use the average in service over the year | Year-end capacity as guided. With none, plants being built, by their stated start date |
| Running hours | Coal and gas: demand in the region, less the output of new wind, solar, hydro and nuclear. Hydro: water inflow against its long-run average. Wind and solar: the resource in a normal year, taken from the long-run average the company gives, times the share of time the plant is available, less output the grid refuses. Nuclear: the refuelling schedule | The latest year, or a long-run average for hydro and wind |
| Electricity sold | Capacity times hours, less own use | Volume growth |
| Price | By the way it is set. Contracted output at the contract price. Output sold ahead at the price fixed. The rest at the forward or spot price. Subsidies and green certificates on their own rows | The average price realised, moved with the benchmark or forward price |
| Capacity payments | Capacity that qualifies times the price set by auction or by rule | As reported |
| Fuel | Fuel used per unit of electricity times the price of fuel, with the mix of contract and spot supplies. The cost of carbon permits | Fuel cost per unit, moved with the coal or gas index |
| Spread | Price less fuel and carbon, per unit | |
| Fixed costs | Depreciation, staff and maintenance, per unit of capacity | Costs grown with capacity |
| Interest | Debt times its cost. Interest on plants being built is added to their cost until they start | Debt times the latest cost |
| Subsidies owed | Subsidies booked as revenue but not yet paid | Receivable days |
| Part-owned plants | The share of profit from plants not consolidated, and the partners' share of those that are. Some plants are booked line by line at the company's own share | As reported |
| Building | Capacity under construction times cost per unit, with start dates | The guided plan. With none, projects approved and being built |
| Funding | Debt, tax credits sold to investors, hybrid bonds whose coupons rank before ordinary shareholders, and new shares | As reported |
| Supply to customers | Where the company also retails: customers times use times the margin | Segment profit |

## 3. The data behind the rows

- **Company.** Chinese generators publish electricity generated and sold each quarter by
  fuel and province, with the average price. Twice a year they add running hours and the
  cost of fuel per unit. US generators publish the share of the next few years' output
  already sold, and how profit moves with power and gas prices. Wind and solar owners
  give capacity, load factor, and the price and remaining life of each contract.
- **Industry**, which differs by market:

| Market | What exists |
| --- | --- |
| China | Monthly power use, output by fuel, running hours and new capacity (National Energy Administration, China Electricity Council). Coal prices at the northern ports and the yearly contract benchmark. The results of each province's yearly power trading. Reservoir inflows |
| United States | Output, capacity and fuel prices (EIA). Prices and capacity auction results from each grid operator (PJM, ERCOT and others). Gas prices |
| Europe | Output and prices by country (ENTSO-E). Forward power prices and the price of carbon permits. Public registers of the price guaranteed to each project, such as the UK's |

- **What leads profit.** The price of coal or gas, a quarter or so ahead of fuel cost.
  The yearly contract round, which sets much of next year's price. Forward prices and the
  share already sold. Capacity auctions, which fix payments years ahead. Rainfall and
  wind. Plants due to start.
- **Backtest.** Capacity times hours times price against revenue. Fuel cost per unit
  against the fuel index a quarter earlier.

## 4. Costs and margin

- For coal and gas plants, fuel is most of the cost and profit is the spread between the
  power price and fuel. Where the power price is slow to move, profit rises when fuel
  falls and falls when it rises.
- For hydro, nuclear, wind and solar, nearly all costs are fixed: depreciation, interest
  and upkeep. A change in output or price reaches profit almost in full.
- A plant written off in the accounts can run for many more years. Profit steps up when
  its depreciation ends.
- A plant built for more than planned, or with a contract price below today's costs, is
  written down. So is one whose future income is worth less because interest rates have
  risen.

## 5. Capacity, capex and working capital

- Building wind, solar and nuclear takes a great deal of capital before any revenue. It
  is borrowed against each project or by the parent, and topped up with partners' money,
  hybrid bonds and new shares.
- Subsidies can be paid years late, and build up as receivables.
- Selling stakes in finished plants recycles capital, at a price that depends on
  interest rates.
- Nuclear plants carry the cost of closing them, and coal plants the cost of early
  retirement.

## 6. Cycle, policy and traps

- Policy sets most of it: how prices are formed, what is paid for capacity, the price of
  carbon, and which subsidies last.
- Rainfall and wind differ from year to year by enough to move profit.
- Power markets tighten and loosen over years as demand and new plants get out of step.
- Traps:
  - growth in capacity read as growth in profit while hours and prices fall;
  - controlled capacity read as the company's share;
  - a wet year, or a year of cheap coal, read as normal;
  - subsidies booked and not collected;
  - gains and losses on forward sales inside reported profit;
  - forward sales made at old prices that run out;
  - a contract that ends and resets to the market price;
  - new sites with weaker wind or sun than the old ones;
  - gains on stakes sold read as recurring;
  - perpetual securities counted as equity.

## 7. What investors argue about, and the yardstick

- Where power prices settle as more wind and solar are built.
- Where fuel prices go.
- Whether new demand, such as data centres, tightens the market for years.
- Whether new projects earn more than their cost of capital.
- How much of the cash is paid out.

Yardstick: P/E, with P/B for coal and gas plants and dividend yield for hydro and
nuclear; EV/EBITDA is common outside China; a cash-flow valuation project by project
for a developer whose profit is small against what it is building
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A coal plant runs 4,500 hours and sells 4,500 units at 0.40: revenue is 1,800. Fuel costs
0.25 a unit, 1,125. Fixed costs are 450. Profit is 225.

If coal falls 10%, profit rises to 337.5, up 50%. If the power price falls 5%, profit
falls to 135, down 40%. If hours fall 10%, revenue falls 180 and fuel 112.5, and profit
falls to 157.5, down 30%.

A wind farm runs 2,200 hours at 0.35: revenue is 770. Its costs are all fixed, at 550, so
profit is 220. If the grid refuses 5% of its output, revenue falls 38.5 and profit 17.5%.

All figures are invented. They show the relationships, not a forecast.
