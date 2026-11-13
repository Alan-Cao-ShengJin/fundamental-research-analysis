# Shipping

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A shipping company owns or hires ships and sells transport by sea.

- **Container lines** run scheduled services and charge for each box carried. Part of
  the volume is on contracts set once a year, and the rest at the spot rate. Many lines
  also own terminals and logistics businesses.
- **Dry bulk and tanker owners** hire their ships out, for a single voyage at the spot
  rate or for a period at a fixed rate. Some carry cargo themselves under contracts with
  shippers and report the gross freight. Either way their earnings are measured per ship
  per day, after fuel and port costs.
- **Gas and car carriers** are mostly on charters of several years.

Rates are set by the balance between cargo to move and ships to move it. Demand is the
volume of trade times the distance it travels: consumer goods for containers, iron ore,
coal and grain for bulk, oil for tankers. A closed canal or a war that lengthens routes
adds demand. Supply is the fleet, plus ships delivered, less ships scrapped, adjusted for
speed and for time lost in ports. Small changes in the balance move rates a long way.

Numbers that get confused:

- **Spot** rates against **contract** rates, and a published **index** against what the
  company itself earned.
- **Time-charter equivalent** earnings per day, which are after fuel and port costs,
  against gross freight, which is before them.
- Days the ships **earned** against days in the calendar.
- Ships **owned** against ships **hired in**. The rental is fixed on a long hire and
  follows the market on a short one.
- Boxes **carried** against the fleet's **capacity**.

Signs the card does not fit: the company runs ports (see the
[toll roads, ports and airports card](transport-infrastructure.md)); it builds ships (see
the [shipbuilding card](shipbuilding.md)); it arranges freight and owns no ships (see the
[logistics card](logistics-express.md)); or it buys ships and leases them out for their
whole lives, which is a lending business.

## 2. The driver tree

Build each kind of ship or each trade route separately, with history beside the
forecast. Use the container rows, the bulk and tanker rows, or both, then the rows for
all.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Container volume | Boxes carried by route: the market's growth times the company's share, limited by the capacity it deploys | Volume growth |
| Freight rate | The contract share times the contract rate, which is reset once a year, plus the spot share times the spot index, by route. Surcharges | The average rate, moved with the index that includes contract rates, after a lag |
| Cost per box | Fuel, as the amount burned times its price. Hire of ships, port and handling charges, moving empty boxes, and depreciation | Cost per box before fuel held flat, and fuel moved with its price |
| Fleet days | Ships owned and hired in, times the days in the period, less days in dry dock | Ships times about 355 days |
| Earnings per day | Days not yet covered times the market rate for that size of ship, which is the index times the company's usual premium or discount to it. Plus days already covered by charters or cargo contracts, at their fixed rate | The index for the ship type times the company's past premium or discount |
| Short-term ships | Ships hired in for single voyages to carry the company's cargoes: days times the margin earned per day | Its past contribution |
| Running cost per day | Crew, upkeep and insurance for owned ships. The rental for ships hired in. Overheads, spread over all the days the fleet earns | As reported, grown with inflation |
| Fleet changes | Ships delivered, sold and scrapped. What is still owed on ships on order, and when | The fleet list |
| Depreciation and dry-docking | Each ship's cost over its life, and the periodic overhauls | As reported |
| Interest | Debt, and long leases on hired ships, times their cost | As reported |
| Part-owned businesses | Terminals and joint ventures, which are steadier than the ships | As reported |
| Dividend and buybacks | The payout rule, which is often a share of each period's profit | |
| Fleet value | Second-hand prices by type and age of ship, less debt, per share | Book value |

## 3. The data behind the rows

- **Company.** Container lines report volume, average rate and cost per box each
  quarter. Bulk and tanker owners report earnings per day by ship type, and with each
  result the share of the next quarter's days already fixed and at what rate. All
  publish a fleet list.
- **Industry:**

| Source | What exists |
| --- | --- |
| Container rates | Weekly spot indices from Shanghai (SCFI) and others (Drewry, Freightos). A weekly index that includes contract rates (CCFI) |
| Bulk and tanker rates | Daily indices by ship size (Baltic Exchange) |
| Fleet | Ships in service, on order and scrapped, by type, and second-hand prices (Clarksons; Alphaliner for containers), quoted in the trade press |
| Cargo | Port throughput, customs trade data, steel output, oil production and exports |
| Fuel | Ship fuel prices at the main ports |

- **What leads profit.** Spot indices lead reported rates by weeks for bulk and tankers,
  and by months for a container line with contracts. The days already fixed for the next
  quarter. The schedule of ships to be delivered. The result of the yearly contract
  round. Routes opened or closed.
- **Backtest.** Volume times the average rate against container revenue. Fleet days
  times earnings per day against revenue less voyage costs.

## 4. Costs and margin

- A ship costs much the same to run whatever it earns. On the days not already covered,
  nearly all of a change in rates reaches profit.
- Fuel is the cost that moves. On a voyage the owner pays it, and on a period charter
  the hirer does.
- Ships hired in at the top of the market keep costing that rate after earnings fall.
- Depreciation is on what the ship cost, which may be far from what it is worth.

## 5. Capacity, capex and working capital

- Ships are ordered when rates are high and delivered two or three years later, often
  into a weak market.
- The business is financed with debt against the ships. When ship values fall, lenders
  can ask for more security.
- Rules on emissions shorten the useful life of older ships and add a carbon cost on
  some routes.
- In a strong year a company earns a large part of its market value, and what it does
  with that cash matters more than the year's profit.

## 6. Cycle, policy and traps

- This is among the most cyclical of all businesses. Booms are short and slumps long.
- Events move rates overnight: wars, sanctions, canal closures, port congestion.
- Traps:
  - a multiple put on peak earnings;
  - a spot index applied to a line that sells mostly on contract;
  - an index that rose because of one route;
  - earnings per day set against gross freight;
  - fixed rentals on hired ships in a falling market;
  - fleet value taken at peak second-hand prices;
  - a dividend that depends on the peak;
  - the order book left out of the forecast.

## 7. What investors argue about, and the yardstick

- How long the present disruption or strength lasts.
- How many new ships are coming.
- Whether the lines hold back capacity when rates fall.
- Where next year's contract rates settle.
- Whether cash goes to shareholders or to new ships.

Yardstick: price to the net value of the fleet, and P/B; the dividend yield at the peak
is read with what follows it
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A container line carries 10m boxes at 1,200: revenue is 12,000m. Cost is 1,000 a box, so
profit is 2,000m. Half its volume is on yearly contracts. If the spot rate rises 20%, its
average rate rises 10%, revenue rises 1,200m and profit rises 60%.

A tanker owner has 10 ships earning for 355 days each, at 40,000 a day: 142m. Running
costs are 9,000 a day, 32m in all, and depreciation and interest are 40m. Profit is 70m.
If earnings fall 25%, to 30,000 a day, profit falls to 34.5m, down by half.

All figures are invented. They show the relationships, not a forecast.
