# Chip designers

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A chip designer designs chips and sells them to the makers of devices and systems,
directly or through distributors. Most have their chips made by a foundry. Makers of
analogue and power chips that own their fabs are on the
[analogue and power chips card](analogue-power-chips.md).

The kinds differ widely:

- **Processors and accelerators for data centres**: few customers, very high prices, and
  demand set by the cloud companies' spending.
- **Chips for phones, computers and consumer devices**: demand follows device shipments.
- **Analogue and control chips** designed without fabs, for cars, industry and devices:
  many products and customers, and long product lives.
- **Licensing designs** to other chip makers, for a fee up front and a royalty on each
  chip shipped.

Demand is the number of devices built, times the chips in each, times the company's
share, times price. Customers and distributors hold stock, and they build it in a
shortage and run it down after. So a designer's shipments swing more than the devices
do. Export rules can close a market outright.

Numbers that get confused:

- Chips sold **into** distributors against chips sold **through** to device makers.
- A **design win**, which is being chosen for a product, against revenue, which comes
  when that product ships.
- **Units** against **average price**, which moves with the mix.
- Revenue by **end market**, which each company defines itself.
- Profit **with** and **without** share-based pay, which is large at US-listed
  designers.

Signs the card does not fit: the company owns the fabs that make its analogue or power
chips (see the [analogue and power chips card](analogue-power-chips.md)); it makes chips
for others to their designs (see the [foundries card](foundries.md)); it makes memory
(see the [memory card](memory.md)); it makes chip-making tools (see the
[equipment card](chip-equipment.md)); or it sells design software on subscription (see
the [software card](software.md)).

## 2. The driver tree

Build each end market or product line separately, with history beside the forecast.

For data-centre accelerators, build from the customers' capital spending: the part spent
on accelerators, and the company's share of it. Then test it against supply, which is
the foundry wafers, advanced packaging and memory the company has secured.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Devices built | Units of the end devices by market: phones, computers, servers, cars, machines | Growth in the end market |
| Chips per device | The number or value of the company's kind of chip in each device. It rises with new features | Leave it inside revenue growth |
| Share | The company's share of that content, product by product for large customers | Hold the latest share |
| Units shipped | Devices times chips per device times share, plus or minus the change in customers' and distributors' stock | Shipment growth |
| Price | A new generation sells for more. Older chips fall a little each year. The mix | Revenue over units |
| Revenue | Units times price, by end market | Revenue by end market, as reported |
| Gross margin | Wafers bought from the foundry, packaging and testing, the yield, and the mix. Write-downs of stock apart | The margin the company guides, or its recent level |
| Research | Engineers times pay, plus the cost of each new design at the foundry | Its share of revenue |
| Share-based pay | The yearly charge, and the new shares it creates | As reported |
| Stock and commitments | The company's own stock in days, and what it has committed to buy from the foundry | As reported |
| Licensing | Fees from new licences, and units shipped by licensees times the royalty on each | Their own growth |
| Export rules | Revenue from customers and countries the rules affect, on its own row | As disclosed |
| Tax and share count | The tax rate. Buybacks, less shares issued to staff | As reported |

## 3. The data behind the rows

- **Company.** Revenue by end market or segment each quarter, guidance for the next
  quarter's revenue and margin, stock in days, and the share of sales to the largest
  customers. Few give units or prices.
- **Industry:**

| Source | What exists |
| --- | --- |
| Chip sales | Monthly world chip sales by type and region (WSTS, the Semiconductor Industry Association) |
| Devices | Quarterly shipments of phones, computers and servers (IDC, Counterpoint, TrendForce) |
| Customers | The cloud companies' capital spending and guidance. Car and device makers' production |
| Supply chain | The leading foundry's monthly revenue. Distributors' stock and delivery times |
| Rules | Export controls, by product, customer and date |

- **What leads revenue.** Customers' spending plans. The foundry's monthly revenue.
  Delivery times and stock at distributors. Device launch dates. The company's own stock
  and purchase commitments.
- **Backtest.** Units times price against revenue by segment, where units are given.
  Revenue against the customers' spending or production behind it.

## 4. Costs and margin

- The cost of a chip is the wafer, packaging and testing. A designer with a product few
  can match sells it for several times that.
- Research is a large fixed cost, so profit grows much faster than revenue, and falls
  much faster.
- Each new manufacturing generation costs more to design for.
- When demand falls, chips made for one customer cannot be sold to another, and are
  written down.

## 5. Capacity, capex and working capital

- A designer without fabs needs little capex. Its commitments are to its foundry: wafers
  ordered months ahead, and sometimes prepayments for capacity.
- In a shortage customers order more than they need from several suppliers. Those orders
  vanish when supply catches up.
- One or two customers can be a large share of sales.

## 6. Cycle, policy and traps

- The chip cycle runs three to four years, driven by stock as much as by end demand.
- Spending on AI has its own cycle, set by a handful of buyers.
- Large customers design their own chips when they can.
- Traps:
  - shipments above end demand, read as growth;
  - design wins read as revenue;
  - a peak gross margin treated as normal;
  - profit quoted without share-based pay;
  - revenue from a market the rules have closed, left in the base;
  - one customer behind most of the growth;
  - a margin lifted by selling stock that was written down earlier.

## 7. What investors argue about, and the yardstick

- How long the present level of spending on AI lasts.
- How much share customers' own chips and rivals take.
- Where the stock cycle stands.
- Whether local chips replace imports in China.
- Whether the gross margin has peaked.

Yardstick: forward P/E, read with growth and with where the cycle stands
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

Device makers build 1,000 devices with 2 chips each, and the company has half: 1,000
chips at 10 is 10,000 of revenue.

In a shortage customers order 10% more than they use: the company ships 1,100. Next year
device output grows 5%, to 1,050, but customers use up the 100 they stocked. The company
ships 950, down 14%, while end demand is up 5%.

All figures are invented. They show the relationships, not a forecast.
