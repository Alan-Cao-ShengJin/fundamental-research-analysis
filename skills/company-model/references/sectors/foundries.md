# Chip foundries

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A foundry makes chips to its customers' designs and sells them by the wafer. The price
of a wafer depends on the manufacturing process: the newest processes cost several times
the older ones. Many foundries also package chips. Companies that only package and test
chips are on the [packaging and testing card](chip-packaging-testing.md).

Customers are chip designers. Their demand follows their own markets, such as phones,
data centres and cars, and their stock. Two other forces matter. Designs move to newer
processes over time. And governments want chips made at home, which sends orders to
local foundries and pays for fabs abroad.

A foundry at the leading edge has few rivals and sets its price. A foundry on older
processes has many, and its price follows how full the industry's fabs are.

Numbers that get confused:

- **Capacity** in wafers a month, which may be stated in two wafer sizes, against wafers
  **shipped**. The ratio is the **share in use**. It can read above 100%, because
  capacity is a rated figure. Companies with two wafer sizes convert both to one,
  usually the smaller.
- The **average price** of a wafer, which rises when the mix moves to newer processes,
  against a like-for-like **price change**.
- **Gross margin**, which falls when a new fab's depreciation starts before its revenue.
- **Capex** before and after government grants.
- A fab's **whole** output against the company's **share** where partners co-own it.

Signs the card does not fit: the company designs its own chips (see the
[chip designers card](chip-design.md)); it makes memory (see the
[memory card](memory.md)); or it makes the tools (see the
[equipment card](chip-equipment.md)).

## 2. The driver tree

Build each process generation, technology platform, wafer size or fab separately,
whichever the company reports, with history beside the forecast.

For a foundry on older processes the short path is capacity, the share in use, the
blended price per wafer and depreciation. Skip the leading-edge and packaging rows.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Capacity | Wafers a month by process and by fab, with new fabs by start date and ramp | Capacity growth as guided. With none, the fabs being built and their stated opening dates |
| Share in use | Customers' demand against capacity, by process where given. Older processes follow the industry cycle. The newest are often sold out. Check whether the company measures it on wafers started or shipped | The company's stated rate, on its recent trend |
| Wafers shipped | Capacity times the share in use | Shipment growth |
| Price per wafer | By process, with announced price changes. The mix of processes | Revenue over wafers shipped |
| Wafer revenue | Wafers shipped times price, by process and by the customers' end market | Revenue as guided for the next quarter. With none, wafers shipped times average price, each on its recent trend |
| Packaging and other | Advanced packaging capacity times price. Masks and services | Their own growth |
| Depreciation | Past capex spread over the life the company uses for its tools, starting when each fab begins production | Depreciation as guided. With none, last year's charge plus each new fab's cost over its stated life |
| Other costs | Materials, staff and power for each wafer. The cost of bringing a new process to a good yield. The higher cost of fabs abroad | Their past ratio to wafers shipped |
| Gross margin | Revenue less depreciation and other costs. It moves with the share in use, the mix, new fabs and the exchange rate | The margin the company guides. With none, the recent margin moved with the share of capacity in use and the new depreciation |
| Research | Development of the next processes | Its share of revenue |
| Capex | The guided budget, by process and location, less grants | The guided figure. With none, announced projects over their build years, plus other capex at its recent level |
| Grants and partners | Government grants, booked against cost or as other income: find which. Partners' share of a jointly owned fab's profit or loss, which comes out before profit attributable to shareholders | As reported |
| Fabs bought or injected | A fab acquired from the parent or a partner changes revenue and capacity from the date it is consolidated. Use restated history where the company gives it | Build it as a separate fab from that date |
| Currency | The currency customers pay in against the currency of costs and of the accounts. Some Chinese foundries sell largely in renminbi and report in dollars | The sensitivity the company gives |
| Tax and dividend | The tax rate and the payout | As reported |

## 3. The data behind the rows

- **Company.** Each quarter: wafers shipped, revenue by process, by end market and by
  region, the capex budget, and guidance for the next quarter's revenue and margin.
  Foundries on older processes also give the share of capacity in use. The largest
  foundry publishes revenue every month.
- **Industry:**

| Source | What exists |
| --- | --- |
| Chip sales | Monthly world chip sales (WSTS) |
| Fabs | Forecasts of fab capacity and equipment spending, and quarterly silicon wafer shipments (SEMI) |
| Foundry market | Quarterly ranking of foundries by revenue, and estimates of prices and of capacity in use (TrendForce) |
| Customers | Chip designers' guidance and stock in days |
| Rules | Export controls on tools and on customers. Grant programmes for new fabs |

- **What leads profit.** Customers' stock. Monthly revenue. The trend in the share in
  use. Notices of price changes. Demand for advanced packaging. Capex, which becomes
  depreciation a year or two later.
- **Backtest.** Wafers shipped times price against wafer revenue. The share in use
  against gross margin.

## 4. Costs and margin

- Depreciation is the largest cost and is fixed. On older processes the share in use
  decides the margin.
- At the leading edge the foundry can raise prices, and margin follows price and mix.
- A new fab lowers the margin for a year or two: its depreciation starts at once and its
  wafers come slowly. A fab abroad costs more to run for good.
- Tools are written off over five to ten years and used for much longer, so old fabs
  are very profitable when full.

## 5. Capacity, capex and working capital

- A fab costs a great deal and takes two to three years to build and fill.
- The money comes from the foundry's own cash flow, debt, governments, partners and
  sometimes customers' prepayments.
- Capacity added by everyone at the top of a cycle is what makes the next downturn.

## 6. Cycle, policy and traps

- Demand follows the chip cycle. Older processes also face new capacity built for
  reasons of policy and not of return.
- Export rules decide which tools a foundry may buy and which customers it may serve.
- Traps:
  - a share in use quoted on a capacity base that changed;
  - a rise in average price that is mix, read as a price rise;
  - a margin forecast that leaves out the next fab's depreciation;
  - grants inside profit;
  - customers' prepayments read as certain demand;
  - revenue growth that is only the exchange rate;
  - a capex cut read as good news when it means less growth later.

## 7. What investors argue about, and the yardstick

- How long demand for the newest processes keeps growing.
- Whether the leader can keep raising prices.
- What fabs abroad do to the margin.
- How deep the glut in older processes becomes.
- What all the capex earns.

Yardstick: P/E for a foundry at the leading edge; P/B for one on older processes
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A foundry has capacity for 100 wafers and 80% is in use. At a price of 10, revenue
is 800. Depreciation and other fixed costs are 500 and each wafer costs 2 more to
make. Gross profit is 140, a margin of 17.5%.

The share in use rises to 90%. Revenue is 900 and gross profit 220: up 57% on revenue up
12.5%.

It then opens a new fab with capacity for 20 more wafers. Depreciation rises by 120
before the fab ships anything. On the same 80 wafers, gross profit falls from 140 to 20,
and the share in use reads 67% on the larger base.

All figures are invented. They show the relationships, not a forecast.
