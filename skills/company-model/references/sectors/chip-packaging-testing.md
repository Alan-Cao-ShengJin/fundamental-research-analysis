# Chip packaging and testing

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

These companies take finished wafers, package them into chips and test them. Their
customers are chip designers and chip makers that send part of this work out. There are
three lines of work.

- **Mature packages**, such as wire-bonded ones. Many companies can make them, and the
  price follows how fully the industry's machines are used.
- **Advanced packages**: flip chip, bumping, wafer-level packages, several chips in one
  package, and the stacking used for AI chips. Fewer companies can make them, the price
  is higher and the capex heavy. The leading foundry does this work itself and passes on
  what it cannot handle.
- **Testing**, charged by the time a chip spends on a tester.

Revenue includes materials bought and billed on, above all the substrates. Where a
package holds several chips and parts, bought-in content is a large share of revenue.

Demand follows the number of chips shipped, the customers' stock, and how much of the
work chip makers and foundries keep in-house. A few customers can be a large share of
sales.

Numbers that get confused:

- **Capacity**, counted in machines such as wire bonders and testers, against output.
- **Revenue by type of package** and by end market against **units**, which are seldom
  given.
- Revenue that includes **passed-through materials** against the company's own work.
- **Packaging and test** against other arms, such as contract manufacturing.
- **Advanced packaging** revenue, which each company defines for itself.
- **Capex** split between packaging, testing and buildings.

Signs the card does not fit: the company turns wafers into chips (see the
[foundries card](foundries.md)); its packaging is a line inside a foundry; it assembles
devices (see the [contract manufacturing card](contract-manufacturing.md), and build
such an arm there); or it makes the substrates and frames that packages use (see the
[electronic components card](electronic-components.md)).

## 2. The driver tree

Build mature packaging, advanced packaging and testing separately, with history beside
the forecast.

A company that reports one product line and no machine counts is built by plant, from
the table of subsidiaries in its annual report. Where one customer takes most of a
plant's output, and may co-own it, drive that plant from the customer's own shipments
and guidance.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Chips shipped | Units of chips by end market, and the customers' stock | Growth in world chip units, or the customers' guidance |
| Work sent out and share | The part of packaging and testing that chip makers send out, and the company's share of it by customer | Hold the latest share |
| Capacity | Machines by type, with what is added each year | Machine counts as reported |
| Share in use | By type of machine. Mature lines follow the chip cycle | The company's comments |
| Revenue per machine | Revenue of each type over its machines, at the share in use. It falls with the price cuts customers take and rises with the mix | Revenue growth by type |
| Mature packaging | Machines times the share in use times revenue per machine | Its growth with chip units |
| Advanced packaging | Its own line: capacity added for named customers' products, tied to the foundry's wafer output and how much the foundry keeps | Revenue as the company guides. With none, its recent growth, checked against the capacity added |
| Testing | Testers times hours used times the rate | Its own growth |
| Passed-through materials | Substrates and parts bought and billed on, apart from the company's own work | Materials as a share of revenue |
| Materials | Substrates, frames, gold and copper wire, and moulding compound: use times price | Their past share of revenue |
| Labour | Staff times pay | Its past share of revenue |
| Depreciation | By class of tool. Testers and advanced lines cost the most | As reported, grown with capex |
| Gross margin | It moves with the share in use, the mix, price, currency and new lines starting | The margin the company guides. With none, the recent margin moved with the share of machines in use |
| Research and overheads | Development and selling costs | Their share of revenue |
| Customers | The largest customers' share of sales, and any customer tied by contract or by a stake in a plant. The customer's own filings say how much work it sends out | As disclosed |
| Capex | Split into packaging, testing and buildings, with any part paid for by customers | The guided budget. With none, capex at its recent share of revenue |
| Currency | Revenue in dollars against costs at home | The sensitivity the company gives |
| Other arms | Contract manufacturing or materials, each on its own card | Segment profit |
| Grants, partners and payout | Grants. Partners' share of each plant's profit, which is large where a customer co-owns the plant. Goodwill on plants bought. Tax and dividend | As reported |

## 3. The data behind the rows

- **Company.** Taiwanese makers publish revenue every month. Each quarter they give
  revenue by type of package and by end market, machine counts, cost by kind, capex by
  type and guidance for the next quarter. Chinese makers give revenue and margin at
  home and abroad, sometimes by product, units made and sold once a year, results by
  subsidiary, and the largest customers' share.
- **Industry:**

| Source | What exists |
| --- | --- |
| Chip sales | Monthly world chip sales in value and units (WSTS) |
| Foundries | The leading foundry's monthly revenue and its plans for advanced packaging capacity |
| Customers | Chip designers' guidance and stock in days |
| Peers | The large packagers' monthly revenue and results |
| Equipment | Billings for packaging and test equipment (SEMI), and the orders of bonder and tester makers |
| Rules | Export controls on advanced packaging tools, and tariffs |

- **What leads revenue.** Customers' stock. Monthly revenue. The foundry's wafer output,
  which packaging follows by a few weeks. Orders at the makers of testers and bonders.
- **Backtest.** Machines times the share in use times revenue per machine against
  revenue by type. The share in use against gross margin. Revenue over units sold, year
  by year, where units are given.

## 4. Costs and margin

- Materials, labour and depreciation are each a large cost. Materials are the largest
  where the packager buys the substrates. The margin moves with the share of machines
  in use, though less than a foundry's.
- Customers take a price cut on mature packages every year.
- Advanced packages sell for more and need far more capex. They do not always earn
  more: bought-in substrates and one strong customer can leave a thin margin. The work
  can be taken in-house by the customer or kept by the foundry.
- Testing earns a higher margin and needs the most capex for each unit of revenue.

## 5. Capacity, capex and working capital

- Machines can be added in months, where a fab takes years. Buildings take longer.
- Testers and advanced lines are often bought for one customer's product. If the
  product is late or moves, they sit idle.
- Capex follows customers' forecasts, so capacity is overbuilt at the top of the cycle.

## 6. Cycle, policy and traps

- Demand follows the chip cycle and the customers' stock.
- Chinese packagers are adding capacity, helped by policy and by customers who want a
  supplier at home.
- Traps:
  - revenue growth from passed-through substrates read as growth in the company's work;
  - advanced packaging revenue compared between companies that define it differently;
  - one blended share in use, when advanced lines are full and mature ones are idle;
  - capacity added for a single customer's product;
  - a margin forecast that leaves out new lines' depreciation;
  - a contract-manufacturing arm's thin margin lowering the group's;
  - grants inside profit;
  - gains on the exchange rate.

## 7. What investors argue about, and the yardstick

- How much advanced packaging the foundry keeps, and how much flows out.
- How long demand for AI chips keeps the advanced lines full.
- When mature packaging recovers, and at what price.
- How much share Chinese packagers take.
- What the capex earns.

Yardstick: P/E, with P/B at the bottom of the cycle
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A packager has 100 wire bonders and 20 testers. At full use a bonder earns 10 a year and
a tester 25. Bonders run at 70%, which gives 700, and testers at 80%, which gives 400.
Revenue is 1,100. Costs that move with volume are 40% of packaging revenue, 280. All
other costs, testing's among them, are fixed at 570. Gross profit is 250.

The bonders' share in use rises to 85%. Revenue is 1,250, up 14%. Variable costs
are 340. Gross profit is 340, up 36%.

It then buys 10 testers for a customer's new chip for 500, written off over five years.
At 80% use they add 200 of revenue against 100 of depreciation. If the chip is a year
late, the 100 is charged against no revenue.

All figures are invented. They show the relationships, not a forecast.
