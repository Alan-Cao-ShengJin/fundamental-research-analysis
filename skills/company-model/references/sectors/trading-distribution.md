# Trading, distribution and agency

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

These companies stand between a maker and a buyer. They earn in three ways.

- **Distribution.** The company buys goods from makers and resells them to many customers.
  It earns a mark-up for holding stock, breaking it into smaller lots, giving credit and
  delivering.
- **Agency and broking.** The company arranges a sale or a service and takes a commission.
  It never owns the goods.
- **Trading on its own account.** The company buys and sells a commodity for the spread.
  It carries price risk unless each purchase is matched to a sale.

Demand is not the company's own. It follows the activity of the market it serves: how
much its customers buy, how many deals are done, how much of a commodity moves. It also
follows the price of the goods, since a mark-up or a commission is a share of value. The
supplier decides whether the middleman keeps its place, and can choose to sell direct.

Two numbers get confused. A company that owns the goods books their **full value** as
revenue. One that acts as agent books only its **commission**. The same activity can be
booked either way, so revenue cannot be compared across companies or even across one
company's lines. **Gross profit** can.

Signs the card does not fit: the company sells to consumers through shops or online (see
the [retail card](retail.md)); it moves goods for a fee without buying them, which is
logistics (see the [logistics and express card](logistics-express.md)); it distributes
medicines, where government pricing rules dominate (see the
[drug distribution card](drug-distribution.md)); or most of its profit comes from a manufacturing
joint venture, from investments or from interest on cash. In that last case the trading
lines use this card and each of the others gets its own build.

## 2. The driver tree

Build each business line separately, with history beside the forecast. A line is
whatever the company reports gross profit by: a region, a product group or a service.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Activity | Units, tonnes or deals handled, driven by the market the line serves. Use that market's own card for its drivers | Growth of the market served, in value. A distributor's sales can rise while the market's unit count falls, through price and mix |
| Value per unit | The price of the goods, or the value of each deal | Leave it inside sales value |
| Sales value handled | Activity times value per unit, whether or not it is booked as revenue | Revenue, for a line booked at full value |
| Share booked net | The part of sales value booked as commission and not at full value. It changes with the product mix | Leave it out where every line is booked the same way |
| Margin or commission rate | Gross profit as a share of sales value handled, by line. Forecast this rate, not the margin on revenue, which moves whenever the share booked net moves | Gross margin as reported |
| Gross profit | Sales value times the rate. This is the figure to compare across lines | Gross profit as reported |
| Revenue as booked | Full value where the company owns the goods, commission where it is agent | |
| Suppliers | Which rights the company holds, when they come up for renewal, and the share of purchases from the largest | Leave it out, and say so |
| Customers | Number, concentration and credit terms. Sales to companies in the same group apart | Leave it out, and say so |
| Operating costs | Staff, warehouses and delivery, with the fixed part shown | Costs as a share of gross profit |
| Working capital | Days of stock, receivables and payables, measured on sales value handled where that is given, and the cost of funding them. Include stock financed by lenders and receivables sold | Working capital as a share of revenue |
| Joint ventures and associates | Each material one on its own build, using the card for what it does | The share of profit as reported |
| Currency | Sales and costs by currency | The currency effect as reported |
| Interest on cash | The cash balance times the rate earned | Finance income as reported |

## 3. The data behind the rows

- **Company.** Most give revenue and profit by line. Some give gross profit by line and
  the volumes handled. Larger distributors report the gross value of what they bill
  alongside revenue, and say how much of the change in margin came from booking more lines
  as agent. Notes to the accounts give the largest customers and suppliers, sales to and
  from related companies, and summary accounts of material joint ventures.
- **Industry:** the data are those of the market served: its volumes, prices and orders.
  The suppliers' own reports show what they sell through distributors. Customs data show
  trade volumes.
- **What leads revenue.** Orders and deliveries in the market served. Prices of the goods.
  Announcements of distribution rights won or lost. Customers' spending plans.
- **Backtest.** Activity times value per unit times the margin rate against reported gross
  profit, line by line.

## 4. Costs and margin

- The margin rate is thin. It moves with the mix of products and customers more than
  with anything else, so gross profit follows volume, the price of the goods and mix.
- A distributor holds stock. When prices rise it sells cheap stock at the new price and
  the margin widens for a while. When they fall the reverse happens, unless the supplier
  compensates it for price cuts.
- Suppliers pay rebates for volume, often settled at year-end. They can be a large part of
  the margin.
- Costs are mostly staff and warehouses, and largely fixed, so profit moves more than
  gross profit.
- Working capital is funded with borrowing, so interest rates move profit.
- A customer that fails takes its receivable with it.

## 5. Capacity, capex and working capital

- Capex is small. The capital is in stock and receivables, and growth uses cash.
- Return on capital is the margin times how often the capital turns over in a year. A
  thin margin can still earn a good return if stock and receivables turn quickly.
- A pure agent needs almost no capital and can build up cash. Ask where the cash is held,
  what it earns and whether shareholders will receive it. A line that is only booked as
  commission is different: if the company still pays the supplier and collects from the
  customer, it carries the receivable and sometimes the stock.

## 6. Cycle, policy and traps

- The business follows the cycle of the market it serves, with more force because price
  and volume move together.
- A supplier that sells direct, or moves to another distributor, can remove a line.
- A commodity price swing brings gains or losses on stock and on open positions.
- Traps:
  - revenue growth from lines that carry little or no margin;
  - a jump or fall in revenue from a change between full-value and commission booking;
  - gains on stock inside the margin;
  - the timing of supplier rebates;
  - profit that comes mainly from joint ventures and interest, not from trading;
  - sales and purchases with companies in the same group, at prices the parent sets;
  - cash deposited with a finance company in the same group;
  - receivable days rising faster than sales.

## 7. What investors argue about, and the yardstick

- Whether the middleman keeps its place.
- How fast the market it serves grows.
- How much of profit is earned by the trading business itself.
- Whether cash on the balance sheet will be paid out.
- Whether dealings with the parent are on fair terms.

Yardstick: P/E; dividend yield for a cash-rich agent; a sum of the parts where a joint
venture or the cash is most of the value
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A distributor sells goods worth 1,000 at a 5% margin, so gross profit is 50. Costs are
30, leaving 20. It has 150 tied up in stock and receivables, a return of 13%.

The price of the goods rises 10% with volume unchanged. Revenue is 1,100 and gross
profit 55. Costs stay at 30, so profit is 25, up 25%. Capital tied up rises to 165.

An agent arranges 1,000 of sales for a 1% commission. Its revenue is 10, a hundredth of
the distributor's, and with costs of 6 it earns 4 on almost no capital.

All figures are invented. They show the relationships, not a forecast.
