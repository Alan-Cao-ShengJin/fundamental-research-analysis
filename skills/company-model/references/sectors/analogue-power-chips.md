# Analogue and power chips

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

These companies make the chips that handle power and signals: power switches and
modules in silicon, silicon carbide and gallium nitride, power management chips,
sensors, microcontrollers, converters and amplifiers. Most make them in their own fabs,
with some output bought from foundries. A power chip's quality comes from the process as
much as from the design.

Customers are carmakers and their parts suppliers, makers of industrial equipment, power
supplies and appliances, device makers, and builders of power systems for data centres.
There are thousands of products and thousands of customers. A product sells for ten
years or more. Much of the volume goes through distributors.

Demand is the number of end products built, times the value of chips in each, times the
company's share. The value per car rises with electric drive and driver assistance. For
power systems it is counted per unit of power.

Customers and distributors hold stock. In a shortage they order twice over, and then
they run stock down for a year or more. So sales swing far more than end demand.

Large customers agree prices once a year, usually a little lower. In a shortage prices
rise. Standard power parts that many can make are priced by how full the industry's
fabs are.

Numbers that get confused:

- Sales **into** distributors against sales **out of** them, and stock at distributors
  against the maker's own stock.
- A **design win**, often quoted as value over the product's life, against revenue.
- Gross margin **reported** and **adjusted**, and with or without the charge for idle
  capacity.
- **Capacity** in wafers of different sizes, and the share made in-house against the
  share bought.
- The **order book**, which customers can cancel or push out.
- A **price** change against a change in **mix**.
- **Capex** before and after grants.

Signs the card does not fit: the company has no fabs and sells processors or phone
chips, or licenses designs (see the [chip designers card](chip-design.md)); it makes
chips to others' designs (see the [foundries card](foundries.md)); it makes memory (see
the [memory card](memory.md)); or it assembles modules and inverters from chips it buys.

## 2. The driver tree

Build each segment or end market separately, with history beside the forecast.

A Chinese maker that reports units and gives no guidance is built from volume times
average price by product, with capacity by wafer size. Where it also sells foundry or
packaging services from the same fabs, build that segment on the
[foundries card](foundries.md) or the
[packaging and testing card](chip-packaging-testing.md), and split the shared fabs'
fixed cost by the output each segment takes.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| End demand | Cars built by kind of drive, industrial output and capex, power equipment installed, servers, appliances and devices | Growth in the end market |
| Content | The value of the company's kind of chip in each car, by kind of drive, or per unit of power in a power system | Leave it inside revenue growth |
| Share | The company's share of that content, from yearly rankings and from designs already in production | Hold the latest share |
| Stock in the chain | The change in distributors' and customers' stock. Shipments are end demand plus or minus that change | The direction, from distributors' stock in weeks |
| Price | The yearly change agreed with customers, and the mix. For standard parts, the market price | The change the company describes |
| Revenue | End demand times content times share, moved by stock and price, for each segment | Revenue as guided for the next quarter, and segment growth. Where units are given, units times average price by product |
| Capacity and loading | Wafer capacity by fab and wafer size, converted to one size before adding, and the share in use. Management lowers loading to cut stock | The company's comments on loading, and its own stock in days |
| Idle cost | The fixed cost of capacity not used, charged in the period | As guided. Where the accounts never show it, leave it inside gross margin and move the margin with loading |
| Depreciation | Past capex over the life of the tools, starting when each fab opens | As guided, or as reported and grown with capex |
| Other cost of sales | Materials, wafers bought from foundries, packaging done outside, staff and energy | Their past ratio to revenue |
| Gross margin | Revenue less the three cost rows. It moves with loading, price, mix, new fabs and currency | The margin the company guides, or its recent level by segment |
| Research and selling | Engineers and sales staff | Their share of revenue |
| Own stock | Stock in days, and what is written down | As reported |
| Capex and grants | New fabs, larger wafers and silicon carbide lines, less grants and tax credits. Grants booked in other income, on their own row | The guided figure, or its recent level |
| Associates and partners | Fabs held as associates, whose losses come through the equity line while they fill. Partners' share of fabs that are consolidated | As reported |
| Currency | Revenue in dollars against costs in the home currency | The sensitivity the company gives |
| Acquisitions and charges | Revenue bought. Segments redrawn, with restated history. Restructuring charges | As announced |
| Debt, tax and share count | Net debt, the tax rate, buybacks | As reported |

## 3. The data behind the rows

- **Company.** Each quarter: revenue by segment, guidance for the next quarter's revenue
  and margin, stock in days, and capex. Some give the idle-capacity charge, distributors'
  stock in weeks, and the order book or the ratio of orders to sales. Chinese makers
  give revenue and margin by product twice a year, and units sold and capacity by wafer
  size in the annual report. They give no guidance.
- **Industry:**

| Source | What exists |
| --- | --- |
| Chip sales | Monthly world sales by region, free. Sales by type, with analogue, discrete, sensor and microcontroller lines apart, in WSTS's paid data and its twice-yearly forecast |
| Shares | Yearly rankings for car chips (TechInsights), power discretes and modules (Omdia) and microcontrollers |
| End markets | Vehicle production and electric car sales (S&P Global Mobility, national associations). Industrial surveys. Solar, storage and charger installations. The cloud companies' capital spending |
| Supply chain | The results and stock of the large distributors. Delivery times |
| China | Local makers' capacity plans, and reports of prices for standard power parts |
| Rules | Grants for new fabs, export controls, tariffs, and carmakers' targets for buying at home |

- **What leads revenue.** Distributors' stock and delivery times. The ratio of orders to
  sales. The company's own stock in days. Carmakers' production plans. Changes in
  loading. The price round at the start of the year.
- **Backtest.** End demand times content times share against segment revenue over
  several years; stock explains the gap. Loading against gross margin.

## 4. Costs and margin

- Fabs are fixed costs. When management cuts loading to lower stock, the idle cost hits
  the margin though revenue holds. When loading recovers, the margin rises ahead of
  revenue.
- An old fab that is written off earns well. A new fab on larger wafers lowers cost per
  chip once it is full, and carries heavy depreciation until then.
- Products with long lives and many customers hold their prices. Standard power parts do
  not.
- Silicon carbide costs more to make, and its price is falling fast.
- Adjusted profit leaves out charges tied to acquisitions. Compare companies on the same
  basis.

## 5. Capacity, capex and working capital

- Capex is heavy and comes in lumps. A fab takes two to three years, and governments pay
  for part of it.
- These makers hold more stock than designers without fabs. The products sell for years,
  so stock is seldom written off, and a downturn shows up in loading.
- Supply agreements and capacity reservations signed in a shortage are renegotiated when
  supply is plentiful.
- Many have grown by acquisition, which leaves goodwill and debt.

## 6. Cycle, policy and traps

- A shortage is followed by a long run-down of stock. Car and industrial customers run
  down later than device makers.
- Chinese makers are adding capacity in standard power parts and silicon carbide, and
  Chinese carmakers are buying more at home.
- Traps:
  - sales into distributors read as demand;
  - an order book read as firm;
  - a margin forecast without idle cost or a new fab's depreciation;
  - content per car assumed to rise while sales of electric cars stall;
  - design wins quoted at lifetime value;
  - an adjusted margin compared with a reported one;
  - grants inside profit;
  - revenue growth that is only the exchange rate.

## 7. What investors argue about, and the yardstick

- Where the stock cycle stands, and when loading recovers.
- Whether more content per car and per power system outruns falling prices.
- How much share Chinese makers take.
- What the new fabs earn.
- Whether silicon carbide pays back.

Yardstick: forward P/E, read with where the cycle stands. When idle costs have
depressed earnings, investors look to earnings at normal loading
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A maker can make 100 chips. Fixed fab costs are 250 and each chip costs 1.5 more to
make. At full loading it sells 100 chips at 7: revenue is 700, cost 400 and gross profit
300, a margin of 43%.

End demand falls 5% and customers run down stock, so it sells 85: revenue is 595. To cut
its own stock it makes only 75 and sells 10 from stock. The quarter of its fixed cost
that is idle, 62.5, is charged at once. The 85 chips sold cost 4 each, 340. Gross profit
is 192.5, a margin of 32%. Revenue is down 15% and gross profit down 36%.

At the yearly price round customers take 3% off. On 85 chips at 7 that is 18, nearly a
tenth of gross profit.

All figures are invented. They show the relationships, not a forecast.
