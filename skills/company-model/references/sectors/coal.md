# Coal producers

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

- **Thermal coal** goes to power plants and industry. **Coking coal** goes to steelmakers.
- Coal is sold under **contracts**, whose price follows a formula or a published
  benchmark, and on the **spot** market. The mix of the two decides how fast a producer's
  price follows the market.
- Some producers sell at home, some export, and some do both. Exports are priced off
  international indices, in dollars.
- Large groups also own power plants, railways, ports or chemical plants that use the
  coal. Each of those is its own unit.

Demand comes from power generation and steel output. Supply comes from how much the mines
are allowed and able to dig. Governments decide a great deal on both sides: output
approvals and quotas, safety inspections, price ranges for contract coal, the share that
must be sold at home and at what price, import and export controls, and royalties.

Four pairs of numbers get confused. **Raw coal** dug against **saleable coal** after
washing. **Coal the company mined** against **coal it bought and resold**. A price **at
the mine** against a price **at the port**, and with or without sales tax: published
market prices often include the tax, and companies report prices without it. A **benchmark**
price for a standard energy content against the price **realised** on the company's own
grades.

Signs the card does not fit: the company only trades coal and mines none; it mainly
burns coal to sell power (see the [power generation card](power-generation.md)); coal is
a small part of a wider mining group (see the [metal miners card](metal-miners.md)); or a power,
transport, chemical or equipment unit earns more than about 15% of profit (gross profit,
where that is what the segments report), in which case that unit gets its own card. A
smaller unit is one row, taken from its reported result.

## 2. The driver tree

Build each mine separately where the company reports by mine, with history beside the
forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Capacity | Approved yearly capacity or quota by mine, with the start dates and ramp of new mines and the years of reserves left | Company total |
| Raw coal output | Capacity times the rate of use, held back by approvals, inspections, geology and weather | Output growth by mine or in total |
| Saleable coal | Raw output times the washing yield, by product and energy content | Saleable output as reported |
| Sales volume of mined coal | Saleable coal, less coal used by the group's own plants, less the change in stock. Reported volumes usually cover every consolidated mine, and the other owners' share comes out lower down, in profit | Sales volume as reported |
| Bought-in coal | Tonnes bought and resold, times the selling price less the buying price. The margin is thin | Its revenue and cost as reported |
| Agency coal | Tonnes sold for others, times the fee per tonne. Only the fee is revenue | The fee income as reported |
| Price | The contract share times the contract price, plus the spot share times the spot price, each adjusted for energy content, delivery point, sales tax and currency. Thermal and coking coal apart | Realised price as a ratio to a benchmark, from history |
| Revenue | Volume times realised price, for mined, bought-in and agency coal apart | |
| Cost per tonne | Materials, staff, power, depreciation, stripping, transport to the buyer or port, and royalties and resource taxes | Unit cost as reported |
| Profit per tonne | Realised price less cost per tonne, for mined coal | Segment margin |
| Other units | Power, transport and chemicals, each on its own card, with internal coal sales removed | Segment results as reported |

## 3. The data behind the rows

- **Company.** Disclosure varies. Some producers publish monthly output and sales. Others
  report quarterly, with output, the ratio of waste to coal in open pits, cost per tonne
  and average price. Annual reports give output and reserves by mine, the realised price
  by type of sale and the make-up of unit cost. Some give none of this by mine.
- **Industry**, which differs by market:

| Market | What exists |
| --- | --- |
| China | Monthly national output from the statistics bureau and imports from customs. Daily port prices for standard grades (Qinhuangdao 5,500 kcal) and mine-mouth indices. The contract price for power coal, which is a base price plus a float tied to named spot indices, set monthly. Coking coal prices in the main producing province. Stocks at ports and power plants, and plants' daily burn. Power output by source. Steel output for coking coal |
| Indonesia | The government's reference price by grade. The price cap and share for coal that must be sold at home. Yearly output quotas by miner. Export volumes |
| Seaborne | Index prices at the main export ports (Newcastle, Richards Bay). Importers' customs data |

- **What leads revenue.** The spot price, which leads the realised price by the lag
  built into the contract formula. Power demand, which follows temperature. Hydropower
  output. Stocks at ports and plants. Safety campaigns and quota announcements. Import
  and export rule changes. Rain at open-pit mines.
- **Backtest.** Output times yield against saleable coal. Volume times the contract and
  spot mix of benchmark prices against revenue. Cost per tonne against its parts.

## 4. Costs and margin

- Staff, depreciation and much of the mining cost are fixed, so cost per tonne falls as
  output rises and jumps when a mine is stopped.
- Profit per tonne is the price less a cost that moves little, so profit moves several
  times as much as the price.
- Contracts dampen that. A producer selling mostly under contract sees its price move
  less than the spot price, in both directions.
- Royalties and resource taxes rise with the price, and some step up at higher prices.
- An inland mine can pay as much to move coal as to dig it.
- In an open pit, cost follows the ratio of waste to coal and the price of diesel.
- Staff costs tend to rise in good years, so the cost base does not fall all the way back.

## 5. Capacity, capex and working capital

- A new mine takes years and needs approvals and, in some countries, a large payment for
  the mining right.
- A mature producer may spend little beyond upkeep and pay out a large share of profit.
  Check what it actually spends, and whether the dividend rests on earnings or on cash
  already held.
- Mines run out. Compare reserves with output, and the cost of replacing them.
- Closing and restoring a mine is a liability that grows as the mine ages.

## 6. Cycle, policy and traps

- The price cycle is set by supply as much as demand: output curbs and safety campaigns
  lift prices, and new approvals and imports lower them.
- Demand peaks in summer and winter. A wet year lifts hydropower and cuts coal burn.
- A government can change a producer's year by decree: quotas, price ranges, the share
  sold at home, export levies and bans.
- Over the long run, power from other sources takes coal's share. Treat the pace as a
  scenario.
- An accident can stop a mine for months.
- Traps:
  - raw tonnes against saleable tonnes;
  - revenue swollen by bought-in coal that earns almost nothing;
  - prices with and without sales tax, and at the mine against at the port;
  - a benchmark for a standard grade applied to coal of lower energy content;
  - all of a mine's output against the company's share;
  - approved capacity against what is actually dug;
  - coal sold to the group's own power plants, which disappears on consolidation;
  - a change in royalty rules;
  - safety and maintenance funds, which different accounting rules book differently, so
    profit can differ between a company's two sets of accounts;
  - currency, for an exporter with home-currency costs.

## 7. What investors argue about, and the yardstick

- Where the price settles, and whether supply curbs put a floor under it.
- Whether the dividend can be sustained.
- Whether new mines add enough to offset old ones running down.
- How fast other power sources take coal's place.
- For coking coal, where steel output goes.

Yardstick: P/B and EV/EBITDA through the cycle, at spot and at long-run prices; dividend
yield for a producer that pays out most of its profit
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A mine with capacity of 10 digs 9.5 of raw coal. Washing leaves 80%, so 7.6 is saleable.
It sells 70% under contract at 600 and 30% on the spot market at 800, a realised price
of 660. Revenue is 5,016. Cost is 350 a tonne, so profit is 310 a tonne and 2,356 in
all.

The spot price falls 25% to 600 and the contract price holds. The realised price falls 9%
to 600, and profit per tonne falls 19% to 250. With no contracts, the price would have
fallen 25% and profit per tonne 44%.

All figures are invented. They show the relationships, not a forecast.
