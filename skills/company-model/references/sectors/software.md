# Software

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

Software is sold in four ways, and many companies mix them.

- **Subscription.** The customer pays per user or per module for a set period, usually
  billed a year or more ahead. Revenue is booked evenly over the period.
- **Usage.** The customer pays for what it uses: data stored, queries run, events
  monitored. Revenue follows usage month by month.
- **Licence and maintenance.** The customer buys the right to use the software once, and
  pays a yearly fee for support and updates.
- **Projects and equipment.** Custom installation work, and devices sold with software on
  them.

The customer's technology budget decides demand: how many staff need the product, how much
data and computing it runs, and whether it renews, expands or switches. Customers buy
directly from the vendor's sales force, through resellers, or through cloud providers'
stores.

Five numbers get confused. **Annual recurring revenue** is the yearly value of contracts
in force. **Billings** are what was invoiced in the period. **Revenue** is what was
earned. **Remaining performance obligations** are everything contracted and not yet
earned. **Net retention** is what last year's customers pay this year as a share of what
they paid then. Companies define each of these in their own way.

Signs the card does not fit: the company sells people's time, with projects and services
as most of its revenue (see the [IT services card](it-services.md)); it earns from
advertising or from transactions on a platform (see the
[e-commerce and advertising card](ecommerce-advertising-platforms.md)); it makes games
(see the [games card](games.md)); or its revenue is mostly one-off projects for a few
public bodies, where contract timing and collection matter more than this card allows.

## 2. The driver tree

Build each product and each way of selling separately, with history beside the forecast.

There are two main routes. For subscriptions, build from recurring revenue. For usage,
build from customers and what they consume. Licence, maintenance and projects are rows of
their own.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Customers | Opening count, plus new, less lost, by size band | Customer growth |
| Recurring revenue | The company's reported figure, on its own definition: opening balance, plus new customers, plus expansion, less reductions, less customers lost. Where retention is given by product but recurring revenue only in total, apply each product's retention to its subscription revenue | Opening balance times net retention, plus new customers |
| Subscription revenue | The average recurring revenue in force over the period | Subscription revenue growth |
| Usage revenue | Customers times usage per customer times price per unit | Last year's revenue from existing customers times net retention, plus new customers |
| Licence and maintenance | New licences sold, and maintenance as a share of the licences in use. Customers moved from licences to subscriptions leave this row and join recurring revenue | Each line's growth |
| Installation and services | New contracts signed, delivered over the months the work takes; or delivery staff times the share of their time billed times the rate. It follows new licence and subscription sales | Its past ratio to new licence and subscription sales |
| Equipment | Units times price, with the subscriptions attached to them | Its own growth |
| Billings and contracted backlog | Revenue plus the change in deferred revenue. Contract length and how far ahead customers are billed | Deferred revenue only |
| Sales capacity | Salespeople times new recurring revenue per salesperson, with time to become productive | Selling cost as a share of new recurring revenue |
| Gross margin | Hosting and computing cost, support, and low-margin project work | Margin by revenue type |
| Operating costs | Selling, research and administration, with share-based pay shown | Each as a share of revenue |
| Free cash flow | Operating profit, plus depreciation and amortisation, plus share-based pay, plus the change in deferred revenue, less capex and capitalised development | Operating cash flow less capex |

## 3. The data behind the rows

- **Company.** Disclosure varies widely. Many companies listed in the US report each
  quarter: revenue by type, recurring revenue, contracted backlog and the part due within
  a year, net retention, customers above a size threshold, and free cash flow. Others give
  only revenue by product and deferred revenue, twice a year.
- **Industry:**

| Source | What exists |
| --- | --- |
| Budgets | Forecasts of technology spending (Gartner, IDC), and surveys of technology buyers |
| Usage | The large cloud providers' revenue growth, which shows how much computing customers are using |
| Staff | Employment and layoffs at customers, where the product is priced per user. The vendor's own job postings for salespeople |
| Peers | Other vendors' recurring revenue, retention and comments on deal timing |
| Public sector | Budget cycles and year-ends, and rules that favour local suppliers |

- **What leads revenue.** Contracted backlog due within a year, and billings. Cloud
  providers' growth. Sales hiring. Price changes. Large contract announcements.
- **Backtest.** Opening recurring revenue times net retention, plus new customers, against
  closing recurring revenue. Average recurring revenue against subscription revenue, which
  can differ by a few per cent through timing and definition.

## 4. Costs and margin

- Subscription and licence revenue carry little direct cost. Hosting and computing are the
  main one, and rise where the product uses heavy computing.
- Project work and equipment earn far less. A rising share of either lowers the gross
  margin.
- Selling is the largest cost and comes first: a customer is won this year and pays over
  several. The margin rises as growth slows.
- Share-based pay can be large. Show profit with it and without it, and count the new
  shares.
- Some companies capitalise development cost, and sales commissions, and others expense
  them. Compare on one basis.

## 5. Capacity, capex and working capital

- Capex is small unless the company runs its own data centres.
- Customers pay ahead, so cash arrives before revenue and free cash flow runs above
  profit. A change in how far ahead customers are billed moves cash flow and billings with
  no change in demand.
- Receivables can be long where customers are public bodies, and some are never
  collected.
- Acquisitions are frequent. Separate growth that was bought from growth that was earned.

## 6. Cycle, policy and traps

- Technology budgets tighten in a downturn: deals slip, customers cut users and trim
  usage.
- A change in how the product is sold distorts the numbers. Moving from licences to
  subscriptions lowers revenue at first. Free periods offered to win a customer from a
  rival lower billings now.
- New technology can add products to sell, or let customers do the same work with fewer
  users.
- Public bodies buy near their year-end, so quarters are uneven.
- Traps:
  - recurring revenue, billings and backlog defined differently from one company to the
    next;
  - billings moved by contract length and invoicing, not by demand;
  - backlog that counts several years of a contract;
  - net retention measured over different periods or customer groups;
  - growth that came from acquisitions;
  - profit and cash flow measures that leave out share-based pay;
  - licences sold for a term and booked at the start, which makes revenue lumpy;
  - capitalised development cost and sales commissions;
  - a company's own headline, such as "cloud revenue", that mixes subscriptions with
    service work;
  - tax refunds, grants and rent that are a large part of a thin profit;
  - a 53-week year or an extra week in a quarter.

## 7. What investors argue about, and the yardstick

- Whether new technology adds to demand or replaces the product.
- Whether growth and retention last.
- How far the margin and free cash flow can rise as growth slows.
- Which vendors win as customers cut the number of suppliers.
- Whether share-based pay is a real cost.

Yardstick: EV to sales, read against growth and margin; EV to free cash flow; P/E once
mature ([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A vendor opens the year with recurring revenue of 1,000. Existing customers pay 110% of
what they did, so 1,100, and new customers add 150. Closing recurring revenue is 1,250, up
25%. Subscription revenue for the year is about the average of opening and closing, 1,125,
so it grows more slowly than recurring revenue does.

It signs 100 a year of new three-year contracts. Billed all at once, they add 300 to
billings. Billed a year at a time, they add 100. Demand is the same in both cases.

All figures are invented. They show the relationships, not a forecast.
