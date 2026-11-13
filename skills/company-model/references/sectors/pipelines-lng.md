# Pipelines, storage and LNG terminals

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

These companies move, store and process oil and gas for a fee. They sit between the
producers and the users, and mostly do not own what they carry.

- **Long-distance pipelines.** On gas pipelines, customers mostly reserve capacity for
  years and pay for it whether or not they use it. Oil and liquids pipelines mostly
  charge for each barrel shipped, often with a minimum volume. In some countries a
  regulator sets the tariff from the cost of the pipeline and an allowed return.
- **Gathering and processing.** Pipes that collect gas and oil from wells, and plants
  that separate the liquids. Paid per unit handled, or with a share of the product, which
  ties income to drilling and to prices. Plants that split the liquids into their parts,
  and docks that export them, charge a fee per unit.
- **Storage and terminals**, rented by capacity.
- **Liquefied natural gas (LNG) export terminals.** They chill gas into liquid for
  shipping. Buyers sign contracts of fifteen to twenty years and pay a fixed fee per
  unit plus the cost of the gas. Cargoes not under contract are sold at the market
  price.
- **LNG import terminals**, paid per unit turned back into gas.

Contracts protect the near term. Over a longer time, income follows how much oil and gas
the connected fields produce, and how much gas the markets at the other end want.

Numbers that get confused:

- **Capacity reserved** against **volume carried**.
- Income from **fees** against income that moves with **prices**.
- **Revenue**, which can include the full value of product bought and resold, against
  **gross margin**, which is what the company keeps.
- **EBITDA** against **distributable cash flow**, which is after interest, tax and the
  capex needed to keep the assets running.
- Assets counted **in full** against the company's **share** of jointly owned ones.

Signs the card does not fit: the company pipes gas to homes and businesses in a city
(see the [gas distributors card](gas-distributors.md)); a regulator sets all its revenue
from an asset base (see the [regulated networks card](regulated-networks.md)); it
produces the oil and gas; or it owns the ships that carry LNG.

## 2. The driver tree

Build each system or terminal separately, or each segment where that is all the company
gives, with history beside the forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Capacity | Pipelines, plants, tanks and liquefaction units in service, plus projects by start date | Capacity as reported |
| Contracts | Capacity reserved times the fee, contract by contract or by group, with the year each ends, the minimum payment and any yearly increase | The share of margin the company reports as fee-based, and the average years left. Annual reports often give a table of the minimum payments customers have committed to, by year |
| Volumes | Where fees are paid on use: the output of the fields served, from producers' plans, wells connected and output per well | Volume growth |
| Fee | Per unit, by contract or by regulated tariff | Gross margin over volume, from history |
| Income tied to prices | Processing paid in product: volume times the price of the liquids less the price of gas. Margins on moving product between places where its price differs. Plants that turn one product into another earn the gap between the two prices. Uncontracted LNG cargoes times the price abroad less the cost of gas and shipping | The average of several years, with any excess named |
| Gross margin | Fees plus income tied to prices, by segment. Check whether the company states it before or after operating costs | |
| Operating costs | Staff, maintenance and power, mostly fixed | Costs grown with the assets |
| Upkeep capex | What the assets need each year | The guided figure. With none, its recent level |
| Growth projects | Each project's cost, start date and the EBITDA it is expected to add | The guided list. Where no profit is given, the cost times the return earned on past projects |
| Interest | Debt times its cost, against the debt-to-EBITDA level the company targets | As reported |
| Jointly owned assets | The company's share of each | As reported |
| Distributable cash flow | EBITDA less interest, tax and upkeep capex. How many times it covers the payout. A partnership pays little tax itself, and counts the cash it receives from part-owned assets | |
| Share or unit count | Buybacks, and new units issued to pay for projects | Hold flat |

## 3. The data behind the rows

- **Company.** Quarterly: volumes by system, gross margin by segment, the share that is
  fee-based, distributable cash flow and how it covers the payout, and debt against
  EBITDA. A list of projects with cost and start date. LNG exporters give the volume
  under long-term contract and the cargoes left to sell.
- **Industry:**

| Source | What exists |
| --- | --- |
| Field output | Production by basin, rigs at work and pipeline flows (EIA in the US) |
| Tariffs | Regulators' filings and notices (FERC in the US, NDRC in China) |
| LNG | Gas delivered to export terminals each day, cargoes exported each month, and prices in Asia and Europe against the US hub price. Imports by country from customs |
| Rates | Government bond yields, which these steady payouts are valued against |

- **What leads profit.** Producers' plans and output per well lead volumes. Rigs at work
  are a weak guide where each well produces more than it used to. Project start dates.
  The years in which contracts end. Price gaps between regions lead trading and LNG
  margins.
- **Backtest.** Volume times fee against fee margin. Contracted quantity times the fixed
  fee against LNG contract income.

## 4. Costs and margin

- Costs are fixed, so the margin is as steady as the contracts behind it.
- Many contracts raise the fee each year with inflation.
- Fuel and power to run compressors and chillers are usually recovered from the
  customer.
- Income tied to prices can double or halve in a year. Keep it apart, so that a windfall
  is not read as growth.

## 5. Capacity, capex and working capital

- Projects take years and often run over budget. They are funded mostly with debt,
  which the contracts support.
- A project built without contracts carries the risk that the volume never comes.
- When a contract ends, the capacity is resold at the going rate. That can be much lower
  where fields are declining or a rival pipeline has been built.
- A producer in bankruptcy may be able to walk away from its contract.

## 6. Cycle, policy and traps

- Income is steadier than a producer's, though volumes still fall when drilling stops.
- Permits, export licences and tariff reviews decide what can be built and charged. A
  government can also move pipelines into a national company.
- Traps:
  - revenue growth that is only higher prices passed through;
  - jointly owned assets counted in full;
  - distributable cash flow before the capex the assets really need;
  - minimum payments from customers that are about to end;
  - a year of high LNG or trading margins read as normal;
  - a payout covered by borrowing or new units;
  - debt ratios quoted with the company's own adjustments.

## 7. What investors argue about, and the yardstick

- Whether the fields served will keep producing.
- How much long-term demand there is for LNG, and how much capacity to leave uncontracted.
- What new projects earn against their cost.
- What happens when contracts end.
- Where interest rates go.

Yardstick: EV/EBITDA, with the payout yield and distributable cash flow yield beside it
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A pipeline has capacity of 100. Customers reserve 90 at a fee of 2 and pay 180 whether or
not they ship. The other 10 is sold as used, 60% of the time, at 2.5: 15. Costs are 60,
so EBITDA is 135. If shipments fall 20%, the 180 does not change.

When the contracts end, the 90 is resold at 1.5. Income falls by 45 and EBITDA by a
third.

An LNG terminal sells 9 units on contract for a fixed fee of 3 each: 27, whatever the gas
price. It sells 1 unit itself. The price abroad is 12, gas costs 4 and shipping 3, so it
earns 5. If the price abroad falls to 8, it earns 1, and the total falls from 32 to 28.

All figures are invented. They show the relationships, not a forecast.
