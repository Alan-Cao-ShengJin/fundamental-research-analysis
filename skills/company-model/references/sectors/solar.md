# Solar

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

Solar panels are made in a chain of four steps, and companies sit on one step or
several: **polysilicon**, **wafers**, **cells** and **modules**, which are the finished
panels. Around the chain are other products:

- **Materials and parts**: the glass, film, frames and silver paste that go into a
  module, and the mounting systems that hold it.
- **Equipment** for making cells and modules, bought when makers add lines or change
  cell type. Build an equipment maker from its orders, as on the
  [machinery card](machinery.md).
- **Solar farms** the maker builds, to sell or to keep. A farm it keeps goes on the
  [power generation card](power-generation.md).

Buyers are developers of solar farms, installers of rooftop systems, and distributors.
Demand follows the return a solar farm earns: the price of power, subsidies and tax
credits, interest rates, and whether the grid can take more. Policy deadlines pull
installations forward and leave a gap after. Trade rules decide which factories can
serve which country.

The products are close to standard, and capacity has been built far ahead of demand. So
price is set by the cost of the weakest producer still running, and by policy on supply.
A maker inside a protected market, such as the US, sells at a much higher price, and is
built from its contracts (the second table in section 2).

Numbers that get confused:

- **Shipments** by the maker against **installations** in the market. Stock sits in
  between.
- **Capacity**, **output** and **shipments**, in units of power. The capacity of each
  step differs, so a maker buys or sells the gap.
- The price **per unit of power** against revenue, and the price in the **home market**
  against prices abroad.
- Modules sold to **outside customers** against modules used in the company's **own
  farms**.
- **Orders** for future delivery, at prices that can be renegotiated, against sales.

Signs the card does not fit: the company mainly owns solar farms and sells power; it
makes inverters or assembles battery storage systems (see the
[inverters and storage card](inverters-energy-storage.md)); it makes battery cells (see
the [batteries card](batteries.md)); or it makes wind turbines (see the
[wind equipment card](wind-equipment.md)).

## 2. The driver tree

Build each step of the chain and each market separately, with history beside the
forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Installations | New solar capacity by market: farms and rooftops apart, with policy deadlines | Growth in world installations |
| Share and shipments | The company's share of each market, giving shipments by product. Sales to outside customers and own use apart | The shipments the company guides. With none, its recent share of industry shipments |
| Price | The market price per unit of power for the product and the market, with the lag between order and delivery | Revenue over shipments, moved with the published price |
| Revenue | Shipments times price, by product and market | |
| Cost per unit | Materials bought from the step before, at the market price or at own cost. Other materials such as silver, glass and film. Power, staff and depreciation, which fall per unit as the share of capacity in use rises | Cost per unit, moved with the price of the step before |
| Margin per unit | Price less cost, by product and market | Gross margin from history |
| Stock write-downs | Stock and purchase contracts worth less than their cost when prices fall | A named row |
| Order backlog | Opening backlog, plus orders, less deliveries and cancellations, by year, with prices | As reported |
| Tax credits and subsidies | Credits earned per unit made or sold, by the rule in force and its end date | As reported |
| Solar farms | Farms built and sold: capacity times price, less cost | Segment profit |
| Operating costs | Research, selling and warranty provisions, and freight where it is not inside cost of sales | Their share of revenue |
| Capex and capacity | New lines by step and by country. Old lines written off when a new cell type replaces them | The guided figure. With none, announced projects over their build years, plus other capex at its recent level |
| Debt and cash | Debt against cash, and what is owed to suppliers | As reported |

A maker inside a protected market that sells on long contracts is built from its backlog
and its factories. Use these rows in place of installations, share, price and cost per
unit above.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Backlog | Opening backlog, plus bookings, less deliveries and cancellations, in units of power and in value. Most give the total and the years it runs to, not each year | As reported |
| Volume sold | The output of each factory, by country, at its share of capacity in use, checked against the backlog due | The volume the company guides. With none, the backlog due in the year, within factory capacity |
| Contract price | Backlog value over backlog volume, moved by the prices of recent bookings. Clauses that adjust the price for technology, freight or materials. Fees customers pay to cancel | Revenue over volume sold |
| Cost per unit | The company's own cost of making a panel, with freight where it is booked in cost of sales. Add the cost of new factories starting up and of capacity left idle | The cost per unit the company guides. With none, cost of sales over volume sold, before credits |
| Tax credits | Credits per unit made in the home country, by the rule in force and its end date. Find where they are booked, often as a cut in cost of sales, and whether they are sold for cash at a discount. Show the margin with and without them | As reported |
| Country of manufacture | Volume by the country where it is made, which sets the price it can earn, the credit and the tariff | The split the company gives |

## 3. The data behind the rows

- **Company.** Shipments by product each quarter, revenue by region, capacity at each
  step, and plans for new lines. Makers in the US give the backlog in units of power and
  in value, the years it runs to, and the price of recent bookings. Chinese makers give
  write-downs and the share of capacity in use in their reports and calls.
- **Industry:**

| Source | What exists |
| --- | --- |
| Prices | Weekly prices for polysilicon, wafers, cells, modules, glass and film (InfoLink, TrendForce, the silicon industry association) |
| Installations | Monthly new capacity in China (National Energy Administration). Quarterly or yearly figures elsewhere (SEIA in the US, SolarPower Europe) |
| Trade | China's customs exports of modules and cells by country, monthly |
| Supply | Capacity and output by step, and stock in the chain, from the industry association and price reporters |
| Rules | Tariffs and anti-dumping duties. Tax credit rules. Policy on output and on prices below cost |

- **What leads profit.** Weekly prices at each step. Exports by month. Tender results
  for large farms. Stock in the chain. The dates when subsidies change. Trade rulings.
- **Backtest.** Shipments times the published price against revenue. The price of each
  step less the price of the step before against the margin.

## 4. Costs and margin

- Each step's main cost is the product of the step before. So a price fall at the top of
  the chain passes down it, and the margin at each step depends on how tight that step
  is.
- Power is a large cost for polysilicon. Silver is a large cost for cells.
- Factories are fixed costs. When they run part-empty, cost per unit rises just as the
  price falls.
- Technology moves fast. A new cell type can make lines a few years old worthless.
- A falling price brings write-downs on stock and on materials bought under contract.
- Warranties run for twenty-five years or more, and are provisions made on estimates.
- A maker that turns raw materials into panels in one factory has no step before it.
  Its cost is its own, and falls with scale and with each change to the process.

## 5. Capacity, capex and working capital

- A new line can be built in under a year, which is why supply overshoots.
- Makers fund themselves partly with what they owe suppliers and with customers'
  deposits. Both shrink in a downturn.
- Many have heavy debt after the last wave of building. In a long slump the question is
  who runs out of cash.
- Factories abroad cost more to build and run, and exist to get inside a trade wall.

## 6. Cycle, policy and traps

- The industry swings between shortage and glut every few years. In a glut most of the
  chain sells below cost.
- Policy sets demand and trade. It can also limit supply, by closing old capacity or
  setting a floor under prices.
- Traps:
  - shipment growth read as profit while price falls faster;
  - the price in one market applied to all;
  - profit that rests on tax credits;
  - orders at old prices that customers renegotiate;
  - write-downs treated as one-off when they recur every quarter of a falling market;
  - capacity counted that will be written off;
  - sales to the company's own farms inside shipments;
  - a tariff that moves the business from one country to another.

## 7. What investors argue about, and the yardstick

- When supply is cut enough for prices to recover.
- Which makers survive.
- Whether a new cell type gives its leader a lasting edge.
- How long protection and tax credits last in each market.
- Whether demand keeps growing as subsidies fall away.

Yardstick: P/E when the industry is growing and profitable; P/B, with cash and debt
beside it, in a downturn
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A module maker ships 100 units of power at a price of 1.00: revenue is 100. Cells cost
0.55 a unit, other materials 0.25 and factory costs 0.10, so the margin is 0.10 a unit
and gross profit is 10.

The module price falls 15%, to 0.85. Cells fall 20%, to 0.44. The margin is 0.85 less
0.44, 0.25 and 0.10, which is 0.06. Shipments grow 20%, to 120. Revenue is 102, up 2%,
and gross profit is 7.2, down 28%.

It also holds 20 units of stock made at a cost of 0.90. At a price of 0.85 it writes off
1.

A maker in a protected market sells 10 units at a contract price of 0.30: revenue is 3.
Its cost is 0.20 a unit, so gross profit is 1 before credits. Half the units are made at
home and earn a tax credit of 0.15 each, 0.75 in all. Gross profit is 1.75. The margin is
33% without the credit and 58% with it.

All figures are invented. They show the relationships, not a forecast.
