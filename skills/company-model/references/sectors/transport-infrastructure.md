# Toll roads, ports and airports

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

These companies own a fixed asset that traffic has to pass through, and charge for each
passage.

- **Toll roads** charge each vehicle by its class and the distance driven.
- **Ports** charge for each container or tonne handled, and for storage.
- **Airports** charge airlines for each passenger and each landing. They also earn from
  shops, duty-free sales, car parks and property, usually as a share of the shopkeeper's
  sales with a guaranteed minimum.

Many hold the asset under a concession: the right to run it and collect the charges for a
set number of years, after which it goes back to the government. Others own it outright.

Traffic follows the economy, trade and travel. It also depends on what else is built: a
new parallel road, a high-speed railway beside an air route, a rival port. The tariff is
seldom the company's to set. It is fixed by the government, linked to inflation in the
concession, or reset every few years by a regulator. Container terminals are the
exception, and agree much of their pricing with the shipping lines.

Numbers that get confused:

- **Traffic** against **revenue**, which also depends on the mix: trucks against cars,
  long trips against short, international passengers against domestic.
- A port group's **total** throughput, which counts terminals it part-owns, against the
  throughput of the terminals it **consolidates**.
- Containers that **start or end** their journey at the port against those **moved
  between ships** there, which pay less and can leave for another port.
- A shop concession's **guaranteed minimum** against the **share of sales**.
- Revenue that includes **construction work** on the concession, booked at no profit
  under some accounting rules.

Signs the card does not fit: the company is a railway (see the
[railways card](railways.md)); it owns the ships, aircraft or trucks and not the fixed
asset; or it is a logistics company that buys capacity from others.

## 2. The driver tree

Build each road, terminal or airport separately, with history beside the forecast. Where
charges are set for a whole network of airports at once, build that network as one.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Traffic | Roads: vehicles a day by class, and distance. Ports: containers or tonnes by terminal. Airports: passengers, international and domestic apart, and aircraft movements. Each grows with the activity behind it, then is adjusted for a competing route opening, works on the asset, or a limit on capacity | Traffic growth against economic growth, from history |
| Tariff | The charge per vehicle and distance, per container or tonne, per passenger and per landing. Follow the rule that sets it: fixed, linked to inflation, or reset by a regulator. A regulator's reset takes an allowed return on the assets plus costs, and divides by the traffic it forecasts for the period. Check whether profit from shops is counted against the charges | Revenue over traffic, from history |
| Traffic revenue | Traffic times tariff, for each asset | |
| Commercial revenue | For airports: passengers times spend per passenger times the airport's share, or the guaranteed minimum where that is higher. A minimum booked evenly over the contract can differ from the cash received. Car parks, advertising and property on their own rows | Commercial revenue per passenger |
| Other revenue | Service areas, storage and logistics. Take out construction revenue booked on concessions | As reported |
| Operating costs | Staff, maintenance and energy. Mostly fixed. They step up when a new terminal or road opens | Costs grown at their own rate |
| Fees to the government | The share of revenue, or the fixed sum, the concession requires the company to pay | As reported |
| Depreciation | Concession cost written off over the remaining years, by straight line or in proportion to traffic. Owned assets over their lives | As reported |
| Concession life | The years left on each asset, and what happens at the end: handed back, or extended in return for new investment | |
| Capex | Widening, new terminals and runways, and the upkeep the concession requires | The guided plan. With none, the approved expansion projects over their build years |
| Interest | Debt times its cost. Interest on an asset being built is added to its cost until it opens | Debt times the latest cost |
| Part-owned and foreign assets | The share of profit from each, and the partners' share of those consolidated. Assets abroad in their own currency, then translated | As reported |
| Dividend | The payout policy | |

## 3. The data behind the rows

- **Company.** Many publish traffic monthly: vehicles and toll revenue by road, containers
  by terminal, passengers and aircraft movements by airport. Results give revenue by
  asset, the years left on each concession, and for airports revenue per passenger from
  charges and from shops.
- **Industry:**

| Source | What exists |
| --- | --- |
| Transport ministries and regulators | Monthly road freight, port throughput by port, and airport passengers. Notices on tolls, charges and toll-free days |
| Trade | Customs exports and imports. Container freight indices. Factory surveys |
| Air travel | Airline seats scheduled for the months ahead (OAG, Cirium). Airlines' own traffic reports |
| Rivals | Opening dates of competing roads, railways, berths and runways |

- **What leads revenue.** Seats that airlines have scheduled. Export orders. Opening dates
  of competing routes. The timetable for tariff decisions. Results of duty-free tenders.
- **Backtest.** Traffic times tariff against revenue for each asset. Passengers times
  commercial revenue per passenger against commercial revenue.

## 4. Costs and margin

- Costs are mostly fixed, so most of a change in traffic reaches profit. Where a
  regulator resets the charges, traffic above its forecast is kept only until the next
  reset.
- Depreciation and interest are large. Both step up when an expansion opens, before the
  traffic that justifies it arrives, so profit often dips after a new terminal or a
  widened road.
- Where depreciation follows traffic, a change in the traffic forecast changes the
  charge.

## 5. Capacity, capex and working capital

- Capacity comes in large steps: a lane, a berth, a runway. Traffic is capped until the
  step is built, and returns fall just after.
- Spending on an expansion often buys more years on the concession. That can be worth
  more than the extra traffic.
- Assets are funded with debt against their own cash flow.
- A concession requires the asset to be handed back in good condition, so heavy repairs
  rise towards the end.

## 6. Cycle, policy and traps

- Traffic follows the economy and trade. Trucks and containers move more than cars and
  passengers, except in a shock that stops travel.
- Governments change the terms: toll-free days, lower charges for trucks, a cut in
  airport charges, or pay for a toll cut with a longer concession.
- A concession is worth nothing on its last day.
- Traps:
  - a concession valued on its earnings as if they would last for ever;
  - a dividend yield read without the years left;
  - total throughput set against consolidated revenue;
  - construction revenue counted as growth;
  - traffic that jumped once because a connecting road opened;
  - profit that falls when interest on a finished project stops being added to cost;
  - a guaranteed minimum that the shop operator later negotiates down;
  - assets bought from the parent at a high price to extend the average life.

## 7. What investors argue about, and the yardstick

- How fast traffic grows against the economy.
- What the next tariff decision or new rule does.
- Whether concessions will be extended, and on what terms.
- Whether expansion earns its cost.
- Whether the dividend is safe while spending is high.

Yardstick: dividend yield and EV/EBITDA, checked with a cash-flow valuation over the
years left on the concession; P/E and EV/EBITDA where the assets are owned outright
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A road carries 50,000 vehicles a day at an average toll of 40: revenue is 730m a year.
Costs are 250m and fixed, so profit is 480m. If traffic grows 5%, revenue rises 36.5m and
profit 7.6%.

A road with ten years left pays a dividend of 1 a year. At a price of 10 the yield is
10%, but the holder gets back only the 10 paid, so the return is nil. At a price of 7 the
return is about 7% a year.

An airport has 50m passengers. Each spends 100 in the shops and the airport's share is
30%, which is 1,500m. If the shop operator negotiates the share down to 20%, revenue
falls by 500m with no change in cost.

All figures are invented. They show the relationships, not a forecast.
