# Chip materials

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

These companies sell what a fab uses up in making chips. There are two kinds, and they
earn differently.

- **Silicon wafers**, the discs chips are built on. A handful of makers supply the
  world. Their plants are expensive, so depreciation is a large fixed cost. Much is sold
  under agreements that fix volume and price for several years, with a spot market
  beside them. Large wafers go to newer chips and small ones to older chips.
- **Process materials**: gases, wet chemicals, photoresist, polishing slurries and pads,
  metal targets, photomasks and the parts inside tools that wear out. Each one has to be
  approved by each fab for each process, which takes a year or more. Once approved it is
  seldom changed.

Demand is the number of wafers fabs start, times the material used on each, times the
company's share, times price. A silicon wafer is used once per wafer started. Process
materials are used more as chips gain layers and steps.

Customers hold stock. Under a long agreement a chip maker keeps taking wafers it does
not need, so its stock builds, and its buying falls later while its own fabs are
recovering. In China, local makers are replacing imports from a low base.

Numbers that get confused:

- The **wafer area the industry ships** against the **wafers fabs start**. Customers'
  stock sits between them.
- The **contract** price under long agreements against the **spot** price.
- Volume by **wafer size**.
- **Approved** at a customer against **shipping in volume**.
- **Advances** from customers under long agreements against revenue.
- A chip-materials **segment** against the larger chemical or metals group it sits in.

Signs the card does not fit: the company makes the tools (see the
[chip equipment card](chip-equipment.md)); it is a general chemical or gas company with
a small sale to chip makers (see the
[specialty chemicals card](specialty-chemicals.md)); it makes wafers for solar cells
(see the [solar card](solar.md)); or it makes circuit boards and package substrates.

## 2. The driver tree

Build each product, and each wafer size, separately, with history beside the forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Wafer starts | The industry's fab capacity times the share in use, by kind of chip and region | Growth in the wafer area the industry ships |
| Use per wafer | The amount of the material used on a wafer, which rises with layers and steps. For silicon wafers it is one | Leave it inside volume growth |
| Customers' stock | The change in customers' stock of the material | The direction, from what customers and the company say |
| Share | The company's share by product and customer, with new approvals and gains from replacing imports | Hold the latest share |
| Volume | Wafer starts times use times share, plus or minus the change in customers' stock, within the company's own capacity | Revenue growth less the price change |
| Price | Contract prices and the dates agreements renew, the spot price, and the mix | Revenue over volume where volume is given. Otherwise the direction the company describes |
| Revenue | Volume times price, by product | Segment revenue growth |
| Capacity and share in use | The company's plants by product, with new plants by start date and ramp | As the company describes |
| Depreciation | Past capex over the life of the plant, starting when each plant opens | As guided. With none, last year's charge plus each new plant's cost over its stated life |
| Other costs | Raw materials, energy and staff, and what the company has committed to buy | Their past ratio to revenue |
| Gross margin | Revenue less depreciation and other costs. It moves with the share in use, price, new plants and currency | The margin guided for the next quarter, or its recent level |
| Research and overheads | Development for each new process, and selling | Their share of revenue |
| Long agreements | Volume and price customers have committed to, the advances received and how they are released | As disclosed |
| Capex and grants | New plants, less grants | The guided figure. With none, announced projects over their build years, plus other capex at its recent level |
| Currency | Prices in dollars against costs in the home currency. For a maker that sells at home and imports its inputs, the exposure runs the other way | The sensitivity the company gives |
| Scope | Subsidiaries that enter or leave the accounts, and partners' share of profit | As announced |

A maker of process materials is built from its customers. Use these rows for its volume
and revenue.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Customers' wafer output | Wafers started by each main customer, from the capacity and share in use it reports | The industry's wafer starts in the company's market |
| Revenue per wafer | The company's sales to a customer over that customer's wafers. It rises with new approvals and with processes that use more material | Total revenue over the wafers its customers make |
| New products | Materials newly approved, starting from nothing, by customer and date | Only those already shipping |
| Volume and price | Tonnes sold, and revenue over tonnes, by product. Tonnes mix materials of very different prices, so read the average with care | Revenue by product |
| Consignment | Where a fab draws material from stock the maker keeps at the fab, revenue is booked when it is drawn, and that stock sits on the maker's balance sheet | As disclosed |
| Raw materials | Abrasives, chemicals and resins bought in, some of them imported: use times price | Their past share of cost |

## 3. The data behind the rows

- **Company.** Wafer makers give sales, profit, capex, depreciation and guidance for the
  next quarter, and describe volume and price by wafer size in words. Few give figures.
  Makers of process materials give sales by segment, sometimes by product and region.
  Chinese makers give units made and sold once a year, and revenue and margin by product
  twice a year.
- **Industry:**

| Source | What exists |
| --- | --- |
| Wafers | Quarterly silicon wafer area shipped, and yearly revenue (SEMI) |
| Fabs | Capacity forecasts (SEMI). The share in use and wafers shipped that foundries and memory makers report. Trackers' estimates (TrendForce) |
| Materials market | The yearly market by type of material and by region (SEMI, TECHCET) |
| Trade | Customs figures for wafers, photoresist and gases: exports from Japan and Korea, imports into China |
| Peers | The results of the few wafer makers, which report on different calendars |
| Rules | Export controls on materials, and targets for buying at home |

- **What leads revenue.** The share of fab capacity in use. Customers' stock of wafers,
  which chip makers mention on their calls. The renewal of long agreements. Spot prices.
  New fabs starting up.
- **Backtest.** Industry wafer area times share times price against revenue. The share
  of the company's capacity in use against gross margin. For process materials,
  customers' wafer output times revenue per wafer against revenue.

## 4. Costs and margin

- For a wafer maker, depreciation and energy are fixed, so the margin swings with the
  share in use and with price. A new plant's depreciation starts before its volume, and
  the margin can fall while shipments rise.
- Process materials need lighter plant. The margin depends on how hard the material is
  to make.
- An approved material is seldom replaced, so share moves slowly. Price is negotiated
  each year.
- Each new chip process needs new materials, so research cannot stop.

## 5. Capacity, capex and working capital

- A wafer plant takes two to three years to build and fill. Makers have asked customers
  for long agreements and advances before building.
- Wafer makers buy their own raw material under long contracts, and hold a large stock
  of it.
- When every maker adds capacity at once, supply stays ahead of demand for years.
- A maker of process materials often sells most of its output to a handful of fabs.

## 6. Cycle, policy and traps

- Demand follows wafer starts, which swing less than spending on tools. Customers' stock
  adds a cycle of its own.
- Long agreements delay a fall in price. They do not prevent one: customers ask to defer
  volume or reopen terms.
- Chinese makers are adding capacity in smaller wafers and gaining share at home.
- Traps:
  - growth in the industry's wafer area read as the company's growth;
  - a contract price assumed safe to the end of the agreement;
  - a margin forecast without the next plant's depreciation;
  - recovering shipments read as recovering profit;
  - customers' advances read as demand;
  - a wafer maker assumed to be steady because materials are;
  - revenue growth that is only the exchange rate.

## 7. What investors argue about, and the yardstick

- When customers' stock is used up.
- Whether prices rise when long agreements renew.
- What the new plants earn.
- How much share Chinese makers take.
- Whether demand for wafers for the newest chips makes up for weakness in older ones.

Yardstick: P/E for makers of process materials. For a wafer maker, P/E when it is
profitable, and P/B or EV/EBITDA when depreciation has taken earnings to nothing
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A wafer maker can make 100 wafers and ships 98 at a price of 10: revenue is 980.
Depreciation is 300, other fixed costs 200, and each wafer costs 2 more to make. Profit
is 284.

It opens a new plant, which adds 100 of depreciation. Shipments rise 5%, to 102.9, and
the price falls 3%, to 9.7. Revenue is 998, up 2%. Costs are 806. Profit is 192, down
32% in a year when shipments rose.

A slurry maker supplies 30% of a material used at 2 units a wafer and priced at 5. On
100 wafers that is 300. If fabs run 10% fewer wafers, it is 270. If a fifth of the 100
wafers move to a process that uses 3 units, it is 330.

All figures are invented. They show the relationships, not a forecast.
