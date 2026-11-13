# Memory chips

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

Memory makers sell two main products. **DRAM** is the working memory of servers,
computers and phones. **NAND flash** is their storage. A third, **high-bandwidth
memory** (HBM), is DRAM stacked for AI accelerators, and is sold under yearly contracts
that fix price and volume in advance.

Memory is close to a standard product, made by a handful of companies. Buyers are the
makers of servers, phones and computers, who agree prices each quarter or, when supply
is short, under contracts of a year or more, and distributors who trade on a spot
market.

The price is set by the balance of supply and demand, measured in bits.

- **Demand** is devices built times the memory in each. Memory per device rises every
  year. AI servers need far more than ordinary ones.
- **Supply** is the wafers the makers run times the bits on each wafer, which rises as
  they move to newer processes. HBM uses several times the wafer capacity of ordinary
  DRAM for the same bits, so more HBM means less of everything else.

Small gaps between the two move prices a long way, in both directions.

Numbers that get confused:

- Growth in **bits shipped**, the change in **price per bit**, and revenue. Makers
  report the first two as percentages.
- **Contract** prices against **spot** prices.
- The price change from **mix**, such as more HBM, against like-for-like.
- **Stock** at the makers against stock at their customers.
- Gross margin **before** and **after** write-downs of stock and their later reversal.
- Fiscal quarters that do not match the calendar.

Signs the card does not fit: the company assembles memory modules or designs
controllers and buys the chips; it is a foundry (see the
[foundries card](foundries.md)); or it designs other chips (see the
[chip designers card](chip-design.md)).

## 2. The driver tree

Build DRAM, HBM and NAND separately, with history beside the forecast. A maker of one
product skips the others.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Bit demand | Servers, phones and computers built, times memory per device, by use | The demand growth the makers and trackers publish |
| Bit supply | The industry's wafer capacity times bits per wafer, less capacity moved to HBM, less production cuts | The supply growth the makers and trackers publish |
| Balance and stock | Supply against demand, and stock at makers and customers. This sets the direction of price | Stock in weeks, as reported |
| Bits shipped | The company's bit output, plus or minus the change in its stock | The growth the company guides. With none, the industry's bit growth from the trackers, with share held |
| Price per bit | Contract prices quarter by quarter, the spot market, and the mix of products | The price change the company guides, then the trackers' forecast |
| Revenue | Last period's revenue times the change in bits times the change in price, for each product | |
| HBM | Capacity for HBM times the contracted price, by generation, with the customer's product schedule | Revenue as the company describes it |
| NAND mix | The share of bits sold as drives for data centres, as storage for phones and computers, and as loose chips, which earn different prices. The move to more layers, which lowers cost per bit | Leave it inside price |
| Cost per bit | It falls each year as newer processes pack more bits on a wafer. It rises when fabs run below capacity | Cost of sales over bits shipped, on its past rate of decline |
| Gross margin | Price per bit less cost per bit, times bits | |
| Stock valuation | Write-downs when price falls below cost, and the gain when written-down stock is sold | A named row |
| Research and overheads | Staff and development of new processes | Their share of revenue |
| Capex | New tools and new fab space, by product. Grants | The guided figure. With none, announced projects over their build years, plus other capex at its recent level |
| Shared fabs | Where fabs are run with a partner: the company's share of the output, what it sells to and buys from the venture, and the venture's leases it guarantees | As disclosed |
| Currency | Prices in dollars against costs in the home currency | The sensitivity the company gives |
| Cash and payout | Cash, debt, dividends and buybacks | As reported |

## 3. The data behind the rows

- **Company.** Each quarter: the percentage change in bits shipped and in average price,
  for DRAM and NAND, sometimes only as a range in words; stock in days or weeks where
  given; the capex plan; and comments on how much HBM is already sold. Some guide the
  next quarter in detail.
- **Industry:**

| Source | What exists |
| --- | --- |
| Prices | Contract prices by month or quarter and spot prices by day (TrendForce) |
| Trade | Korea's chip exports for the first ten and twenty days of each month, and its memory exports by product in the monthly figures |
| Demand | Shipments of servers, phones and computers. The cloud companies' capital spending |
| Supply | Makers' announcements of production cuts and capex. Trackers' estimates of capacity |
| Chip sales | Monthly world memory sales (WSTS) |

- **What leads profit.** Spot prices lead contract prices by a quarter or two.
  Customers' stock. Announced cuts in output or capex. Korea's export figures. The
  schedule of new AI accelerators, which sets demand for each generation of HBM.
- **Backtest.** The changes in bits and in price against the change in revenue. Price
  per bit less cost per bit against gross margin.

## 4. Costs and margin

- Nearly all cost is fixed: fabs, tools and staff. Cost per bit falls steadily and does
  not respond to price.
- So margin is price less a slowly falling cost. When price rises, almost all of it is
  profit. When it falls far enough, makers sell below cost.
- Running fabs below capacity to support prices raises cost per bit.
- HBM earns more per bit and is harder to make, with lower yields.

## 5. Capacity, capex and working capital

- Capex is very large. New fab space takes years, and new tools take months.
- What the makers spend, taken together, decides supply two years on. Restraint by all
  of them makes an upturn last, and a race for share ends it.
- Stock is the buffer. Makers build it when demand is weak and sell it into the
  recovery.
- One or two customers can be a large share of a maker's sales.

## 6. Cycle, policy and traps

- Memory has the sharpest cycle in the chip industry. Prices can double or halve within
  a year.
- New makers supported by their governments add supply whatever the price.
- Traps:
  - a margin at the peak valued as if it would last;
  - growth in bits read as growth in revenue;
  - a rise in average price that is mix;
  - gains from selling written-down stock inside the margin;
  - a spot price move read as a new contract price before it is one;
  - capacity counted twice, as both HBM and ordinary DRAM.

## 7. What investors argue about, and the yardstick

- Whether demand from AI has made the cycle longer and shallower for good.
- How HBM is shared between the makers, and at what price next year.
- Whether the makers stay restrained on supply.
- How much new makers in China take.

Yardstick: P/B through the cycle; forward P/E when the market believes demand is
structural. If the cycle returns, P/B and mid-cycle earnings are what the shares fall
back to ([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A maker ships 100 bits at a price of 10 and a cost of 7: gross profit is 300.

Next year it ships 15% more bits. Price falls 20%, to 8, and cost falls 10%, to 6.3.
Revenue is 920, down 8%. Gross profit is 115 times 1.7, which is 195.5, down 35%.

If price had risen 20%, to 12, revenue would be 1,380 and gross profit 655.5, more than
double.

All figures are invented. They show the relationships, not a forecast.
