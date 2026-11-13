# Metal miners

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A miner digs ore, processes it and sells the metal it holds: copper, gold, iron ore,
zinc, nickel, lithium, rare earths and others.

- Most base metals are sold as **concentrate** to smelters. The miner is paid for most
  of the metal contained, at the exchange price, less a charge for treatment and
  refining.
- Some miners sell **refined metal**, gold bars or iron ore priced off an index, with
  adjustments for grade.
- Many also run **smelters and refineries** that process concentrate bought from others.
  These earn the treatment charge and the value of by-products, a thin margin on large
  revenue.
- **Lithium** companies mine hard rock or pump brine and turn it into lithium
  chemicals. Many buy part of their raw material from other mines, some of which they
  part-own. Their margin depends on how much of it is their own.
- Some **trade** metal. That adds a great deal of revenue and very little profit.

The miner is a price taker. Prices are set on world exchanges by global supply and
demand, with China the largest buyer of most metals. What the company controls is how
much it produces and what that costs.

Numbers that get confused:

- **Ore** mined or processed, metal **contained**, metal **paid for**, and metal
  **sold**.
- A mine's **whole** output against the company's **share**. Many mines are joint
  ventures, some consolidated and some not.
- Metal from the company's **own mines** against metal from its **smelters**.
- **Cash cost** against **all-in sustaining cost**, which adds upkeep capex and
  overheads. Each company defines them itself, and costs quoted after by-product income
  move with by-product prices.
- The **benchmark** price against the price **realised**. Sales are often booked at a
  provisional price and adjusted when the final price is fixed.
- **Reserves**, which can be mined at a profit, against wider **resources**.

Signs the card does not fit: the company mines coal (see the [coal card](coal.md)); it
only smelts, or makes aluminium, where power and bought-in raw material decide the
margin (see the [steel, aluminium and cement card](steel-aluminium-cement.md)); it owns
only royalties or rights to buy part of a mine's output, which have no costs; or it has a
project and no production, where funding and dilution matter most. A battery unit inside
a lithium company goes on the [batteries card](batteries.md).

## 2. The driver tree

Build each mine separately where the company reports by mine, and each metal apart, with
history beside the forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Ore processed | The mill's capacity times its rate of use, from the mine plan | Leave it inside metal produced |
| Grade and recovery | The metal content of the ore, which changes as the mine moves through the deposit, and the share the plant recovers | Leave them inside metal produced |
| Metal produced | Ore times grade times recovery, by metal and by mine, in whole and as the company's share | The middle of the company's guidance, tested against how often it has met guidance. With none, last year's output adjusted for the grade in the mine plan |
| New mines and expansions | Start date, the months to reach full output, and capacity | The guided schedule, with a delay as the downside case. With none, the schedule in the technical report |
| Sales volume | Metal produced, less the part not paid for, less the change in stock | Equal to production |
| Realised price | The benchmark, less treatment and refining charges and freight. Hedges and sales owed at fixed prices apart. The adjustment on provisional prices | The benchmark times the past ratio of realised to benchmark |
| By-products | Volume times price, as revenue or as a credit against cost, the way the company reports | As reported |
| Mining cost | Cost per tonne of ore: staff, energy, supplies and the waste moved. Divided by metal, it rises when grade falls | The unit cost the company guides. With none, last year's unit cost moved with grade, energy and labour |
| Royalties and taxes | By each country's rule. Many rise with the price | Their past share of revenue |
| Smelting and refining | Tonnes of bought concentrate times the treatment charge, plus by-products, less running costs | Segment profit |
| Processing bought ore into chemicals | Output of the chemical, split by where the raw material comes from: own mines, mines the company part-owns and buys from, and the market. The tonnes of raw material needed per tonne of chemical. The cost of each source, with bought material priced off the market some months earlier, plus the cost of processing | Margin per tonne from history, moved with the gap between the chemical's price and the raw material's |
| Trading | Revenue and cost as reported | Leave it out of the build |
| Investments | Gains and losses on listed stakes and other holdings, kept apart from operating profit | A named row, zero in the forecast |
| Depreciation | The mine's cost spread over the reserves mined | Depreciation per unit, from history |
| Capex | Upkeep, and the cost of each new mine and expansion | The guided figure. With none, announced projects over their build years, plus other capex at its recent level |
| Partners | The partners' share of consolidated mines, and the company's share of profit from mines not consolidated | As reported |
| Closing mines | The provision, and the cash spent | As reported |

## 3. The data behind the rows

- **Company.** Most publish a production report each quarter by mine and metal, guidance
  for the year on output and unit cost, and a yearly statement of reserves. Technical
  reports on each large mine give the mine plan. Chinese miners give a yearly production
  plan, and output by metal each quarter or only each year, with less detail by mine. A
  partner in a mine often reports on it in more detail than the company does.
- **Industry:**

| Source | What exists |
| --- | --- |
| Prices and stocks | Exchange prices and stocks (LME, SHFE, COMEX). The iron ore index and stocks at Chinese ports. Lithium and other minor-metal prices from price reporters (SMM, Fastmarkets, Asian Metal), and futures where they trade. Chinese quotes usually include sales tax |
| Treatment charges | The yearly benchmark and spot charges for copper and zinc concentrate |
| Supply and demand | Monthly balances from the international study groups for copper, zinc and nickel. Quarterly gold demand (World Gold Council). China's customs imports of ore and concentrate |
| Rules | Changes to royalties, export bans and ownership rules, country by country |

- **What leads profit.** For a miner selling what it digs, metal prices reach profit in
  the same quarter. Where raw material is bought and processed, stock and the lag in its
  price delay the effect, and a falling price brings write-downs on stock. Production
  reports come out before results. News on a new mine's progress. Guidance on grade. The
  prices of energy and supplies. Strikes and rainy seasons.
- **Backtest.** Ore times grade times recovery against metal produced. Sales volume times
  the benchmark, less charges, against revenue.

## 4. Costs and margin

- A mine's costs are mostly fixed for each tonne of ore. So the cost of each unit of
  metal rises when grade or throughput falls, and profit moves by much more than the
  price.
- A mine's costs are usually in local currency and the metal is priced in dollars.
  Mining currencies often weaken when metal prices fall, which cushions the miner. A
  processor that buys raw material in dollars and sells at home is exposed the other
  way.
- Energy, staff and supplies cost more in a boom, so costs follow prices up with a lag.
- Royalties and special taxes take a larger share when prices are high.
- When smelters are short of concentrate, treatment charges fall. That helps a miner and
  hurts its smelting arm.

## 5. Capacity, capex and working capital

- Mines run out. Reserves have to be replaced by exploring or by buying, and bought
  reserves are dearest when prices are high.
- A new mine takes many years, needs permits, and usually costs more than planned.
- One mine can be a large part of a company. A flood, a strike or a change of rules there
  changes the whole forecast.
- Governments can raise taxes, ban exports of ore or demand a stake.
- Closing a mine and making its waste safe is a liability that grows with age.

## 6. Cycle, policy and traps

- Metal prices move in long cycles, driven by how slowly new supply arrives. Forecast
  with a stated price and show the result at others.
- Traps:
  - a mine's whole output read as the company's share;
  - a cost quoted after by-product income when by-product prices are high;
  - mining the richest ore first, which lifts profit now and lowers it later;
  - guidance that is missed year after year;
  - growth bought with acquisitions at high prices;
  - a mine life that counts resources as reserves;
  - today's price assumed to last for ever;
  - adjustments on provisional prices read as recurring;
  - metal already sold forward at a fixed price;
  - trading revenue read as size.

## 7. What investors argue about, and the yardstick

- Where the metal price goes, and the supply and demand case behind it.
- Whether new mines arrive on time and on budget.
- Whether acquisitions were worth what was paid.
- How much the countries it mines in will take.
- Whether cash is paid out or spent on growth.

Yardstick: price to net asset value, and EV/EBITDA at spot and at long-run prices; P/E
is common for Chinese miners
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A mine processes 100,000 tonnes of ore at a grade of 2% and recovers 80%: 1,600 tonnes of
metal. It is paid for 95%, which is 1,520 tonnes. The benchmark is 9,000 and charges are
400, so it realises 8,600 and revenue is 13.07m. Mining costs 60 a tonne of ore, 6m in
all, or 3,947 a tonne of metal. Profit is 7.07m.

The grade falls to 1.8%. Payable metal is 1,368 tonnes and revenue 11.76m. The cost is
still 6m, now 4,386 a tonne of metal, up 11%. Profit is 5.76m, down 18%, with no change
in the price.

All figures are invented. They show the relationships, not a forecast.
