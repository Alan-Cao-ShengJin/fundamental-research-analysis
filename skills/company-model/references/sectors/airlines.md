# Airlines

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

An airline sells seats. Around the seats it sells extras such as bags and seat choice,
cargo space, and loyalty points, which banks buy to give to their card customers.

- **Network airlines** feed passengers through hubs, fly long routes and sell premium
  cabins.
- **Low-cost airlines** fly point to point with one type of aircraft, and earn a large
  part of revenue from extras.

Leisure travel follows incomes, business travel follows the economy, and travel abroad
follows visas and exchange rates. In some countries high-speed trains take the short
routes. Fares are set by the balance between demand and the seats all airlines put on a
route. Seats depend on aircraft deliveries, airport slots and pilots. Two outside
prices move profit as much as fares do: jet fuel and the dollar.

Numbers that get confused:

- **Capacity**, measured in seats times distance flown. **Traffic**, in passengers times
  distance flown. Traffic over capacity is the **load factor**.
- **Yield**, which is revenue per unit of traffic, against **unit revenue**, which is
  revenue per unit of capacity. Unit revenue is yield times load factor.
- **Unit cost** with and without fuel.
- Routes of different lengths. Longer flights have lower revenue and cost per unit, so
  compare like with like.
- Profit **before** and **after** gains and losses on dollar debt.

Signs the card does not fit: the company runs airports (see the
[toll roads, ports and airports card](transport-infrastructure.md)); it leases aircraft
to airlines, which is a lending business; or it sells tickets for others.

## 2. The driver tree

Build each group of routes the company reports separately, such as home, regional and
international, with history beside the forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Capacity | The fleet, as opening aircraft plus deliveries less retirements, times seats, times flights a day, times the average length of a flight, times the days in the period | The capacity growth the company guides, or the growth in its fleet and hours flown |
| Load factor | Hold it near its recent level unless capacity is growing much faster or slower than demand. Yield is the row that carries the balance between the two | The recent level |
| Yield | The average fare per passenger and distance. It follows the industry's capacity growth against demand, the mix of cabins, and fuel surcharges | Unit revenue on its recent trend, read against the industry's capacity plans. Where yield is given only twice a year, use monthly traffic and published fares in between |
| Passenger revenue | Capacity times load factor times yield | Capacity times unit revenue |
| Extras and loyalty | Passengers times extras per passenger. Points sold to card partners | Their own growth |
| Cargo | Cargo carried times distance, times the rate. Freighters apart from the holds of passenger aircraft | Its own growth |
| Other revenue | Ground handling, maintenance for other airlines and commissions | As reported |
| Fuel | Capacity times fuel burned per unit of capacity, times the price of jet fuel, after hedges. Where the government sets the fuel price and the surcharge, both follow the oil price by rule, with a lag | Fuel cost per unit of capacity, moved with the jet fuel price |
| Unit cost before fuel | Staff, airport and navigation charges, maintenance, aircraft depreciation and rent, and selling costs, per unit of capacity. It falls when aircraft fly more hours | The figure the company guides, or each cost line grown with capacity and inflation |
| Currency | Fuel, aircraft rent and aircraft debt in dollars against revenue in the home currency. The change in the value of dollar debt | The sensitivity the company gives |
| Fleet and capex | Aircraft on order, their delivery dates, and how each is paid for or leased | The fleet plan |
| Interest | Debt and leases times their cost | As reported |
| Other income | Route subsidies and other grants, which can recur every year and be a large part of profit. Compensation from aircraft and engine makers | Grants at their recent level. Compensation not repeated |
| Partners' share | The profit of airline subsidiaries that belongs to their other owners | Its past share of profit |

## 3. The data behind the rows

- **Company.** Many airlines publish capacity, traffic and load factor every month.
  Results give unit revenue and unit cost, the fleet plan, fuel hedges, and how profit
  moves with the fuel price and the exchange rate.
- **Industry:**

| Source | What exists |
| --- | --- |
| Traffic | Monthly traffic from the aviation regulator and from IATA. In the US, route-level data from the transport department |
| Seats | Flights and seats scheduled for the months ahead (OAG, Cirium) |
| Fares | Fare trackers and travel agents' data, weekly in China |
| Fuel | Jet fuel prices in the main markets, and crude oil |
| Events | Holiday travel figures, visa changes, new high-speed rail lines, delays in aircraft deliveries |

- **What leads profit.** The industry's scheduled seats. Weekly fares and bookings. The
  jet fuel price, which reaches cost within a month or two. The exchange rate. The
  holiday calendar.
- **Backtest.** Capacity times load factor times yield against passenger revenue.
  Capacity times fuel burned times the fuel price against fuel cost.

## 4. Costs and margin

- Once the schedule is set, nearly all costs are fixed. An extra passenger or a higher
  fare is almost all profit, and an empty seat is all loss.
- Margins are thin, so a few percent on fares or on fuel changes the year.
- Fuel is the largest or second-largest cost. Surcharges recover part of a rise, with a
  lag.
- Pilots' and crews' pay moves in steps when contracts are renewed.
- Flying each aircraft more hours spreads its fixed cost.

## 5. Capacity, capex and working capital

- Aircraft are bought or leased, and airlines carry heavy debt.
- Passengers pay before they fly, so a growing airline is funded by its customers. When
  bookings fall, that cash flows out.
- Aircraft makers are years behind on deliveries, which caps capacity for the whole
  industry.
- An engine fault can ground part of a fleet for months.

## 6. Cycle, policy and traps

- Demand follows the economy and is hit hard by shocks. Most of a year's profit is made
  in the peak travel season.
- Governments control routes, slots and, in some countries, fares and fuel prices.
- Traps:
  - traffic growth read as profit while yield falls;
  - a high load factor bought with low fares;
  - unit revenue compared across airlines with different route lengths;
  - gains on fuel hedges or on dollar debt inside profit;
  - subsidies, and compensation from aircraft makers;
  - gains on aircraft sold and leased back;
  - capacity plans that, added up across the industry, exceed demand.

## 7. What investors argue about, and the yardstick

- Whether the shortage of aircraft keeps fares high.
- How long demand for travel holds.
- Where fuel goes.
- How fast pay rises.
- For airlines with heavy debt, how fast it is repaid.

Yardstick: EV/EBITDA, with aircraft rent treated the same way for every airline
compared; P/B and P/E on mid-cycle earnings beside it
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

An airline flies 100bn of capacity at a load factor of 80%: 80bn of traffic. At a yield
of 0.50 revenue is 40bn. Fuel costs 12bn and everything else 26bn, so profit is 2bn.

If yield rises 3%, revenue rises 1.2bn and profit 60%. If fuel rises 10%, profit falls by
the same 1.2bn. One more point of load factor at the same yield adds 0.5bn.

All figures are invented. They show the relationships, not a forecast.
