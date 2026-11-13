# Commodity chemicals and refining

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

- **Bulk chemicals, plastics and fuels** made from oil, gas, coal or salt. One producer's
  product is the same as another's, so it sells at the market price to manufacturers and
  processors.
- A company usually runs a **chain**: a feedstock becomes an intermediate, which becomes
  the product it sells. Part of the output is used by its own downstream plants.
- Several **process routes** make the same product from different feedstocks. Which route
  is cheapest changes with the prices of oil, gas and coal.

No producer sets the price. It settles where the most expensive plant still needed can
cover its costs, so it follows the balance of industry capacity and demand, and the cost
of the feedstock. What a producer earns is the **spread**: the product price less the
feedstock it takes to make a tonne.

Four pairs of numbers get confused. **Nameplate capacity** against **output**. **Output**
against **sales outside the group**. The **spot spread** quoted in the market against the
spread the company **realises** on its own contracts, grades and timing. Profit on
**replacement cost** against reported profit, which also carries gains and losses on
stock.

Signs the card does not fit: the product is sold on what it does, not what it is, and
priced customer by customer, or the company sells industrial gases under long contracts
(see the [specialty chemicals card](specialty-chemicals.md) for both); it trades or
distributes chemicals it does not make (see the
[trading and distribution card](trading-distribution.md)); or it makes
fertiliser or crop chemicals, where seasons and farm policy matter more than this card
allows.

## 2. The driver tree

Build each product chain separately, and each plant where the company reports by plant,
with history beside the forecast. Give a minor product one row, from its reported
revenue.

Where one plant turns several feedstocks into several products at once, do not build a
cost for each product. Build the plant's feedstock cost once, as the tonnes of each
feedstock times its landed price, and set it against the combined value of what the
plant makes. Split it by product only where the company does. Add a row for the
producer's choice between selling an intermediate and processing it further, since that
choice changes the product mix from one period to the next.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Capacity | By plant and product, with start dates and ramp of new units and the dates of planned shutdowns | Company total by product |
| Output | Capacity times the operating rate | Output as reported |
| Sales volume | Output, less what the group's own plants use, less the change in stock, at home and exported. Products bought and resold apart. Processing done for others for a fee is its own row | Sales volume as reported |
| Product price | The market series for each product, adjusted for grade, region, sales tax and contract lag | Realised price as a ratio to the market series, from history |
| Feedstock cost | The landed feedstock price (market price plus freight, tariff and currency) times the tonnes of feedstock per tonne of product, plus energy | Unit raw material cost as reported |
| Spread | Product price less feedstock cost, per tonne | Skip to profit per tonne, using gross profit per tonne from history, which is the spread after conversion cost |
| Industry balance | Capacity being added across the industry against demand growth, giving the industry operating rate. Use it to set the direction and size of the spread forecast | The spread's own history, and the forward price curve where the product is traded on an exchange |
| Conversion cost | Staff, depreciation, maintenance and other fixed cost, per tonne at the forecast output | Unit cost less raw materials, as reported |
| Profit per tonne | Spread less conversion cost | Segment margin |
| Stock effect | The change in feedstock and product prices over the period times the stock held at its start | Leave it out, and say so |

## 3. The data behind the rows

- **Company.** Disclosure varies. Some producers publish quarterly output, sales volume,
  average selling prices and raw material prices by product. Others give operating rates
  and margins by segment, with planned shutdowns and stock valuation effects called out.
  Some give only revenue and margin by segment.
- **Industry:**

| Source | What exists |
| --- | --- |
| Prices | Daily and weekly prices for products and feedstocks from price reporting agencies (ICIS, Argus, S&P Global; in China, providers such as SunSirs and Mysteel). Futures prices where the product is traded on an exchange |
| Spreads | Published profit per tonne by process route, and refining margins by region |
| Supply | Industry operating rates and stocks by product. Lists of plants being built, with start dates. Planned shutdowns |
| Trade and policy | Customs imports and exports. Anti-dumping duties, export tax rebates, capacity and energy-use rules |

- **What leads revenue.** The spot spread so far in the period, adjusted for sales made
  at earlier contract prices and feedstock bought earlier. That lag can send the margin
  the opposite way to the spot spread for a period. Start-ups of new plants. Shutdowns.
  Feedstock prices. Customers' operating rates.
- **Backtest.** The market spread times volume against reported gross profit, period by
  period. Capacity times operating rate against output.

## 4. Costs and margin

- Feedstock is most of the cost, so profit is the spread less a conversion cost that
  moves little. A small change in the spread is a large change in profit.
- Fixed cost per tonne rises when the operating rate falls, which compounds a weak
  spread.
- When prices move, stock bought at the old price is sold at the new one. Reported profit
  carries that gain or loss. Separate it.
- A chain that makes its own feedstock keeps the spread at every step, and is steadier
  than a plant that buys it.
- Where a plant sits on the industry's cost ranking decides whether it earns through the
  cycle: its feedstock, its energy price, its size and its location.
- A planned shutdown costs output and money in the quarter it falls.

## 5. Capacity, capex and working capital

- A new plant is a large, multi-year commitment, usually debt-funded. Interest is
  capitalised while it is built and expensed once it runs, and a new plant often loses
  money while it ramps.
- High spreads lead everyone to build at once. Track the industry's projects, not only
  the company's.
- Working capital rises and falls with prices.
- Plants can be closed for safety or environmental reasons, or moved at the government's
  request.

## 6. Cycle, policy and traps

- The capacity cycle runs for years: high spreads, building, glut, closures, recovery.
- Demand follows construction, cars, packaging and textiles.
- An energy shock changes which route and which region is cheapest.
- Governments act on supply: closing old capacity, capping energy use, changing export
  rebates, imposing duties, and setting quotas on crude imports and fuel exports.
- Traps:
  - nameplate capacity read as output;
  - volumes that include transfers inside the group or products bought and resold;
  - prices quoted with sales tax against revenue without it;
  - the spot spread read as the realised spread;
  - profit lifted by gains on stock;
  - capitalised interest on plants under construction;
  - subsidies and tax refunds inside profit;
  - a peak-year margin carried into the forecast.

## 7. What investors argue about, and the yardstick

- Where the industry is in the capacity cycle, and when supply growth slows.
- Whether government action on capacity lifts spreads.
- Whether a cost advantage lasts.
- Whether a large new project earns its cost or strains the balance sheet.

Yardstick: P/B, and EV/EBITDA on mid-cycle spreads, checked against the cost of building
the same capacity new ([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A plant can make 1.0 and runs at 90%, so output is 0.9. The product sells at 1,000 a
tonne. Each tonne takes 0.8 of feedstock at 700, which is 560, plus 90 of energy, so the
spread is 350. Fixed costs of 180 are 200 a tonne at this output. Profit is 150 a tonne,
135 in all.

The product price falls 10% to 900. The spread falls to 250 and profit to 50 a tonne,
down 67%. If the plant also cuts its rate to 80%, fixed cost rises to 225 a tonne, profit
falls to 25 a tonne and 20 in all, down 85%.

All figures are invented. They show the relationships, not a forecast.
