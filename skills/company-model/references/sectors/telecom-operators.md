# Telecom operators

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A telecom operator sells connections over a network it owns.

- **Mobile service** to consumers, on monthly contracts or prepaid.
- **Home broadband**, often bundled with television and mobile.
- **Services to businesses and government**: lines, cloud and data-centre services, and
  projects that install and run their systems.
- **Handsets and equipment**, sold at little or no profit to win or keep customers.
- **Wholesale**: network access sold to other operators.

In most markets nearly everyone already has a phone, so operators grow by taking
customers from each other, by raising prices and by moving customers to dearer plans.
Competition decides how much of that sticks. Regulators shape it: they approve mergers,
admit new entrants, sell the radio spectrum and sometimes push prices down. Business
services are where most operators look for growth.

Numbers that get confused:

- **Service revenue** against total revenue, which includes handsets.
- **Average revenue per user (ARPU)**, which each operator defines differently: per
  mobile line, per account, or per household with broadband and television included.
- **Subscribers**, which may count second cards and connected machines that pay very
  little.
- **Lines** against **accounts**. One account can hold several phone lines and home
  broadband, and revenue per account includes them all.
- **Net additions** against gross additions and **churn**, the share of customers who
  leave.
- **EBITDA** before and after the rent paid on leased towers and sites.
- **Capex** with and without spectrum payments.

Signs the card does not fit: the company owns towers or data centres and rents them out
(see the [towers and data centres card](towers-data-centres.md)); it makes network
equipment; or it resells another operator's network and owns none.

## 2. The driver tree

Build each service and each country separately, with history beside the forecast. Some
operators report accounts and revenue per account in place of lines and ARPU. Build on
the unit the operator reports, and do not add broadband again if it is already inside
revenue per account.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Mobile subscribers | Opening subscribers, plus gross additions, less those who leave. Contract and prepaid apart | Net additions |
| Mobile ARPU | The mix of plans: customers moving to dearer plans, price rises, promotions ending, and cheap second lines pulling the average down | The recent trend |
| Mobile service revenue | Average subscribers times ARPU times twelve | Growth in service revenue |
| Broadband | Homes the network reaches times the share that subscribe, times revenue per home. Broadband sold over the mobile network has no homes reached, so build it from subscribers added | Subscriber growth and the recent ARPU |
| Business services | By product: lines, cloud, data-centre space, and projects. Each on its own growth, with projects kept apart because they earn least | Growth by line, slowing |
| Handsets and equipment | Units times price, which follows new models and upgrades by existing customers. The cost of the handsets on its own row, since they are sold near cost | Hold revenue and cost flat |
| Wholesale and other | Contracts with other operators | As reported |
| Network costs | Rent on towers and sites, energy, maintenance and spectrum fees | Their past share of service revenue |
| Customer costs | Gross additions and upgrades times the cost of each: handset subsidy, commission and advertising. Where gross additions are not given, work them out from net additions and churn | Selling costs as a share of service revenue |
| Staff and other costs | Staff numbers times pay, and overheads | Costs grown at their own rate |
| Depreciation | Past capex written off over the life of the equipment, plus spectrum over its licence | Depreciation over average fixed assets |
| Capex | Capex as a share of revenue. It peaks while a new network generation is rolled out and falls after. Fibre and computing on their own rows | The guided figure. With none, its recent share of revenue, lowered once a network rollout ends |
| Spectrum and leases | Payments for spectrum at auction and renewal. Rent on towers, deducted once: under US accounting most of it is already inside EBITDA | As reported |
| Purchases and ventures | Customers and networks bought from others. Fibre networks held in ventures with partners, where the operator keeps the customers and books a share of the venture's profit | Announced deals only |
| Free cash flow | EBITDA less capex, interest, tax, spectrum and the change in working capital, and less leases where they are not already inside EBITDA | |
| Cash returned and share count | Dividends and buybacks as a share of free cash flow, and the share count after buybacks | The guided payout. With none, the stated policy or the recent payout ratio |

## 3. The data behind the rows

- **Company.** Most report quarterly: service revenue, EBITDA, net additions, churn,
  ARPU and capex. Chinese operators publish subscriber numbers every month but not
  churn, and give ARPU twice a year. Most guide yearly on capex and on the payout.
- **Industry:**

| Source | What exists |
| --- | --- |
| Regulator or ministry | Subscribers, revenue and data traffic for the industry (MIIT in China monthly, the FCC and Ofcom and their peers elsewhere). Numbers switched between operators |
| Prices | The operators' published plans and promotions |
| Rivals | Their net additions, ARPU and capex plans |
| Suppliers | Tower companies' results, which are the operators' rent. Handset shipments |
| Rules | Spectrum auction dates. Decisions on mergers, new entrants and prices |

- **What leads revenue.** Net additions and price changes lead service revenue. Capex
  guidance leads depreciation and free cash flow. A rival's promotion leads churn.
- **Backtest.** Average subscribers times ARPU times the months in the period against
  service revenue.

## 4. Costs and margin

- The network is a fixed cost, so the margin moves with service revenue.
- Winning a customer costs money at the start. When competition heats up, churn and the
  cost of each addition rise together.
- Depreciation follows capex with a lag of years. After a rollout, capex falls first and
  depreciation later, so free cash flow rises before profit does.
- Projects for businesses and the resale of equipment add revenue at a low margin.

## 5. Capacity, capex and working capital

- Each network generation needs a wave of capex, and spectrum to run it.
- Operators that sold their towers pay rent for them. That rent is a lasting cost, even
  where the accounts show it below EBITDA.
- Handsets sold on instalments tie up cash in receivables.
- Debt is high in many markets. The dividend depends on free cash flow after spectrum.

## 6. Cycle, policy and traps

- Demand barely moves with the economy. Price wars, network generations and regulation
  move profit.
- A new entrant or a merger can change a market's prices for years.
- Traps:
  - subscriber growth made of low-paying lines and connected machines;
  - ARPU compared across operators that define it differently;
  - revenue growth that comes from handsets and projects;
  - EBITDA that leaves out tower rent, or rent deducted twice;
  - free cash flow on the company's definition, which may leave out spectrum;
  - a low point in capex treated as lasting;
  - spectrum payments left out of cash flow;
  - a longer assumed life for equipment, which lifts profit;
  - a dividend paid from borrowing;
  - growth before and after a change in tax or accounting.

## 7. What investors argue about, and the yardstick

- Whether price competition has eased for good.
- How far capex falls, and how much of the saving is paid out.
- Whether cloud and computing services earn a real return.
- Whether a merger will be allowed.

Yardstick: EV/EBITDA and dividend yield, with free cash flow yield beside them; P/E and
dividend yield for the Chinese operators
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

An operator has 100m subscribers paying 50 a month: service revenue is 60,000m a year.
Each month 1% leave, which is 12m a year. Replacing them costs 300 each, or 3,600m. If
churn rises to 1.2%, standing still costs 720m more.

EBITDA is 24,000m. Capex is 12,000m, a fifth of revenue. Leases are 2,000m, interest
1,000m, tax 3,000m and spectrum 1,000m, so free cash flow is 5,000m. When the rollout
ends and capex falls to 9,600m, free cash flow rises to 7,400m, up 48%, with profit
unchanged.

All figures are invented. They show the relationships, not a forecast.
