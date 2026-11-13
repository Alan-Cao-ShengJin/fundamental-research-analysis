# Cruise lines

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

Cruise lines sell holidays on ships. Revenue is the ticket plus what passengers spend on
board: drinks, the casino, excursions, shops and internet.

Capacity is fixed by the fleet: berths times the days the ships sail. Ships sail full,
and often above the count of two guests to a cabin, so the price is what moves.
Passengers book and pay deposits months ahead, and the lines say how much of the coming
year is booked and at what price.

The costs are crew, food, port fees, marketing and travel agents' commissions, fuel,
depreciation and the interest on the debt that paid for the ships.

Demand follows what people spend on holidays, and the price of a cruise against a
holiday on land. New ships and the lines' own islands and ports draw passengers. A
health scare or a conflict can stop sailings in a region.

Numbers that get confused:

- **Capacity days**, which is berths times days and which the lines call available
  passenger cruise days, against **passenger days**. Occupancy above 100% is normal.
- Revenue **before** and **after** commissions, flights and the cost of goods sold on
  board. The lines quote the second for each capacity day and call it net yield.
- Cost for each capacity day **with** and **without** fuel, which the lines call net
  cruise cost.
- The share of next year **booked** against revenue.
- Growth at **constant currency** against reported growth.

Signs the card does not fit: the company carries cargo or runs ferries (see the
[shipping card](shipping.md)); it runs parks on land (see the
[theme parks and tourist sites card](theme-parks-sites.md)); or it sells other lines'
cruises (see the [online travel card](online-travel.md)).

## 2. The driver tree

Build each brand separately where the company reports it, with history beside the
forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Capacity | Ships times berths times days in service, with new ships by delivery date, ships sold, and days in dry dock | The capacity growth the company guides. With none, the berths of ships on order by delivery date, less ships leaving the fleet |
| Occupancy | Passenger days over capacity days | Its past level |
| Ticket revenue | Passenger days times the ticket price for each day, after commissions and flights. The share of the year already booked, and its price | The growth in revenue for each capacity day that the company guides. With none, the recent trend in prices and what the company says of bookings |
| On-board revenue | Spend for each passenger day, after the cost of goods | Its past ratio to ticket revenue |
| Revenue | Ticket and on-board revenue for each capacity day, times capacity days. Add back commissions, flights and the cost of goods to reach reported revenue | |
| Costs without fuel | Crew, food, ports, marketing and overheads, for each capacity day. Newer ships cost less for each berth. Dry docks add cost in the year they fall | As guided. With none, last year's cost for each capacity day, raised with inflation |
| Fuel | The amount used for each capacity day times its price, with hedges and the cost of emissions rules | As guided. With none, last year's fuel used for each capacity day at the current fuel price |
| Depreciation | The fleet, with new ships from delivery | As guided. With none, last year's charge plus each new ship's cost over its life |
| Interest | Debt times its cost, with what is refinanced | As guided. With none, closing debt times the average rate paid last year |
| Own islands and ports | The capex on them, and what they add to revenue | The company's comments |
| Ventures | The share of profit from cruise brands and resorts owned with partners. Their ships are in the fleet list and outside the company's capacity days | As reported |
| Deposits | Passengers' deposits, which fund part of the business | As reported |
| Capex | Ships on order by delivery year, with the financing arranged for each. Spending on islands, ports and systems | The order book, and the guided figure for the year |
| Debt and payout | Debt by the year it falls due, the limits lenders set, dividends, buybacks and the share count | As reported |
| Currency and tax | Revenue by currency. Tax, which is low on income from sailing under shipping tax rules, with a minimum tax now applying in some countries | As reported |

## 3. The data behind the rows

- **Company.** Each quarter: capacity days, occupancy, revenue and cost for each
  capacity day, fuel used and its cost, and guidance for each. Comments on how much of
  the coming year is booked, and at what price against a year earlier.
- **Industry:**

| Source | What exists |
| --- | --- |
| Capacity | The industry's order book of ships by delivery year, from shipyards and the industry association |
| Passengers | The association's yearly passenger counts, and port figures |
| Fuel | Marine fuel prices by port |
| Peers | The other large lines' bookings, prices and costs |

- **What leads revenue.** Bookings and prices in the first months of the year, when most
  holidays are booked. Deposits. Deliveries of new ships. Fuel prices.
- **Backtest.** Capacity days times revenue for each against revenue. Capacity days
  times cost for each against costs.

## 4. Costs and margin

- A ship's costs are mostly fixed, so a change in price falls almost wholly on profit.
- Fuel and interest are the costs that move from outside.
- Newer and larger ships earn more and cost less for each berth.

## 5. Capacity, capex and working capital

- A ship costs a great deal, takes years to build and is financed with debt arranged at
  the order.
- The industry's capacity is known years ahead from the order book.
- Deposits arrive before the cruise, so cash runs ahead of revenue while bookings grow.

## 6. Cycle, policy and traps

- Demand is discretionary, though bookings made months ahead make the next quarters
  visible.
- Rules on fuel and emissions add cost and can retire older ships.
- The summer quarter earns much of the year's profit.
- Traps:
  - a rise in revenue for each capacity day that comes from new ships, read as a price
    rise;
  - costs without fuel flattered by the timing of dry docks;
  - fuel left unhedged;
  - debt falling due in a weak year;
  - a strong booked position bought with lower prices;
  - growth in capacity read as growth in demand.

## 7. What investors argue about, and the yardstick

- Whether prices can keep rising against holidays on land.
- How long demand stays this strong.
- How fast debt is paid down, and when cash returns to shareholders.
- What the new ships and the lines' own islands earn.

Yardstick: EV/EBITDA, with P/E beside it
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A cruise line has 10m capacity days and fills 105% of them at 200 for each passenger
day, after commissions and the cost of goods: revenue is 2,100m, or 210 for each
capacity day, which is the figure the lines quote. Costs without fuel are
120 for each capacity day, 1,200m. Fuel is 250m, and depreciation and interest 400m.
Profit is 250m.

If revenue for each passenger day rises 5%, revenue rises 105m and profit is 355m, up
42%. If fuel rises 20%, profit falls by 50m, a fifth.

All figures are invented. They show the relationships, not a forecast.
