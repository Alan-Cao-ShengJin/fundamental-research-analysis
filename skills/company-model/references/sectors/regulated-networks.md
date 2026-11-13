# Regulated networks: electricity, gas and water

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

These companies own the wires and pipes that deliver electricity, gas and water. Each is
the only supplier in its area, so a regulator decides what it may earn.

The regulator counts the money invested in the network, called the rate base in the US
and the regulated asset base elsewhere, and allows a return on it. Revenue is set to
cover that return plus depreciation, running costs and tax. Profit follows the size of
the asset base and the allowed return. Where rates are adjusted for the amount sold,
volume does not matter. Where they are not, as in many US states, the weather and
demand move profit between rate decisions.

How the return is set differs.

- **In the US**, each state commission sets rates in a rate case the utility files. The
  allowed return is a return on the equity share of the rate base. Many US utilities
  also own power plants inside the rate base, which earn the same way.
- **In Britain, Australia and much of Europe**, the regulator sets revenue for a period
  of about five years. The allowed return is on the whole asset base, and the company
  keeps part of what it saves against its cost allowance.

The regulator and the company's investment plan decide growth. New demand matters through
the investment it calls for: connections for data centres, electric vehicles, new homes
and renewable power.

Numbers that get confused:

- The return the regulator **allows** against the return the company **earns**.
- The **asset base** the regulator counts against the assets in the accounts.
- A return set **before inflation**, with the asset base raised by inflation each year,
  against one set **after** it. Adding inflation to the second counts it twice.
- **Revenue**, which includes the cost of energy passed straight through to customers,
  against the part the network keeps.
- **Reported profit**, which can include revenue collected early or late, against the
  company's **underlying** profit.

Signs the card does not fit: the company earns a margin on the gas it sells and a fee for
each connection (see the [gas distributors card](gas-distributors.md), which also suits
a water company paid an approved price per unit); its power plants sell at market prices
(see the [power generation card](power-generation.md)); or it builds and runs plants
under a contract for a set number of years, such as water treatment or waste plants.

## 2. The driver tree

Build each jurisdiction separately, with history beside the forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Asset base | Opening balance, plus investment as it enters the base, less regulatory depreciation, plus inflation where the rules add it. Use the regulator's definition: deferred tax is usually taken off, and work in progress is counted in some places and not in others | The growth the company guides. With none, the opening base plus the approved investment less depreciation |
| Investment | The plan by jurisdiction and by year. How it gets into rates: approved in a rate case, or added as it is spent under a formula or a special charge | The guided total, spread evenly. With none, the plan the regulator approved |
| Allowed return | The share of the base funded by equity times the allowed return on equity, or the base times the allowed return on capital. From the latest decision, with the date of the next one | Hold the latest |
| Earned against allowed | The delay between spending and new rates, which is shortest where rates follow a formula or are set on a forecast year. Rewards and penalties for cost and service. Costs the regulator refuses | The past gap between earned and allowed |
| Network profit | Average equity in the asset base times the earned return. This is profit after the regulated company's own interest | |
| Sales volume | Only where revenue still moves with it: customers times use, which follows the weather and new large users | Leave it out |
| Other businesses | Unregulated units, each built as what it is | Segment profit |
| Parent interest and costs | Debt held by the parent, above the regulated companies, times its cost, plus the parent's own costs. Do not deduct the regulated companies' interest again. Where the regulator allows a cost of debt on the whole base, add the gap between that and the actual cost | As reported |
| Partners' share | The share of profit that belongs to outside investors in subsidiaries | As reported |
| New shares | Investment, less cash kept after dividends, less the debt the credit rating allows. Shares sold ahead and hybrid securities count as they arrive. Shares issued above book value dilute less | The amount the company guides. With none, what is needed to hold the equity share of the base |
| Earnings and dividend per share | Profit over the share count after new shares. The payout policy | |

## 3. The data behind the rows

- **Company.** Networks publish the asset base and allowed return by jurisdiction, a
  five-year investment plan, the new shares they expect to issue and a target for
  earnings growth. The filings in each rate case and the regulator's decisions are
  public.
- **Industry:**

| Source | What exists |
| --- | --- |
| Regulators | Decisions, draft decisions and the timetable for the next reset (state commissions in the US, Ofgem in Britain, the AER in Australia) |
| Rates and prices | Government bond yields, which feed the allowed return at each reset. Inflation, where returns are indexed |
| Weather | Heating and cooling degree days |
| Demand | Grid operators' forecasts of load, and the queue of connection requests |

- **What leads profit.** A draft decision comes before a final one. Bond yields move
  before the allowed return does. The investment plan gives asset growth years ahead.
- **Backtest.** Average equity in the asset base times the earned return against network
  profit.

## 4. Costs and margin

- Running costs are paid for by customers. They change profit only where the company
  spends more or less than it was allowed.
- Where the regulator allows a cost of debt, the company keeps the gap between that and
  what it actually pays. In the US the cost of debt is settled in each rate case.
- Between rate decisions, costs rise while rates stand still, so the earned return drifts
  below the allowed one until the next decision.

## 5. Capacity, capex and working capital

- A growing network spends far more than its depreciation, so it has negative free cash
  flow and funds the gap with debt and new shares.
- Credit rating limits cap the debt. What the rating will not allow has to come from new
  shares, and those dilute the growth in earnings per share.
- Costs waiting to be recovered from customers, such as storm repairs or fuel, sit on the
  balance sheet until the regulator lets them into rates.
- Debt at the parent, above the regulated companies, earns no allowed return.

## 6. Cycle, policy and traps

- Profit barely moves with the economy. The shares move with bond yields, because
  investors hold them for income.
- The risk is political. When bills rise fast, regulators cut allowed returns and refuse
  costs.
- A single event, such as a wildfire or a storm, can bring liabilities larger than a
  year's profit.
- Traps:
  - the allowed return read as the earned return;
  - growth in the asset base read as growth in earnings per share;
  - revenue growth that is only higher energy cost passed through;
  - inflation counted twice;
  - profit that includes revenue to be handed back to customers in later years;
  - interest added to the cost of projects under construction, which lifts profit
    without cash;
  - a dividend paid from borrowing.

## 7. What investors argue about, and the yardstick

- What the next regulatory decision does to the allowed return.
- Whether a large investment plan becomes growth per share after it is funded.
- Where bond yields go.
- Whether customers and politicians will accept the bills.

Yardstick: P/E and dividend yield, with enterprise value against the regulated asset
base where one exists
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A network has an asset base of 100, half funded by equity. It invests 12 and depreciation
is 4, so the base ends at 108 and averages 104. Equity in it averages 52. The regulator
allows 10%, which would be 5.2. The company earns 9%, which is 4.68.

To keep half the base in equity, equity must rise by 4. The company pays out 60% of
profit and keeps 1.87. The other 2.13 is new shares. If they are sold at book value the
share count rises about 4%, so earnings per share grow about 4% while the asset base
grows 8%.

All figures are invented. They show the relationships, not a forecast.
