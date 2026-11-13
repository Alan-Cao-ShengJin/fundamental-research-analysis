# Restaurant and coffee chains

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A chain earns in three ways, and most chains mix them by market.

- **Company-operated stores.** The chain runs the store, books every sale and pays for
  food, staff and rent.
- **Franchised or licensed stores.** Someone else runs the store. The chain earns a
  royalty on its sales, rent where it controls the site, and fees.
- **Supply to franchisees.** The chain earns mainly by selling ingredients, packaging and
  equipment to its franchisees. Its revenue is the goods it sells to stores, not what
  customers pay in them.

Some chains also sell packaged products through shops. Some operate stores under another
company's brand and pay that company a royalty. A chain that hands a whole country to
one such operator earns a lower royalty there, reports it as a single line and takes the
currency risk.

The consumer decides demand: how often they visit and how much they spend each time.
That depends on value, convenience (location, drive-through, delivery, app), new products,
competitors' prices and, where delivery platforms compete, the platforms' subsidies.

Two numbers are easy to confuse. **System sales** are what customers spend in every
store, whoever runs it. **Revenue** is what the company books. **Same-store sales** growth
covers stores open for a stated time, and each company defines that pool its own way.

Signs the card does not fit: the company is a contract caterer; it makes packaged food
(see the [packaged food and drink card](packaged-food-drink.md)); it is a delivery
platform (see the [ride-hailing and delivery card](ride-hailing-delivery.md)); or it
supplies ingredients mainly to restaurants outside its own brand, which is a distributor
(see the [trading and distribution card](trading-distribution.md)).

## 2. The driver tree

Build each brand and market separately, at the level the company reports, with history
beside the forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Stores | By ownership and market: openings, closures, transfers between company and franchise, and the average for the period | Net additions only |
| Sales per store | Mature stores at last period's level times same-store growth. New stores on a ramp by age, taken from the company's comments or from franchise disclosure documents | Revenue per average store, labelled as such |
| Same-store growth | Visits times spend per visit, and spend split into price and mix. By channel (in store, pick-up, delivery) where disclosed | One growth rate |
| System sales | Stores times sales per store, for each ownership type | The company's reported system sales growth |
| Company-store revenue | The company stores' part of system sales | |
| Franchise revenue | Franchised sales times the royalty rate, plus other recurring fees such as technology charges, plus rent on sites the chain controls, plus opening fees | Franchise revenue as a share of franchised sales, from history |
| Advertising fund | Franchised sales times the contribution rate, with an equal cost | Leave it out of revenue and costs alike |
| Supply revenue | Volume, which follows the franchised stores' sales, times a price that passes food costs through. Equipment follows openings. Sales to the chain's own stores are internal | Supply revenue per average franchised store, labelled as such |
| Other revenue | Packaged goods, delivery fees, unused stored value | One row |
| Company-store costs | Food and packaging, staff, rent, delivery and other, each split into the part that moves with sales and the part that does not | Store-level margin |
| Franchise and supply profit | Franchise revenue less site costs. Gross margin on goods sold to franchisees | Segment margin |
| Central costs | Marketing, administration, pre-opening and depreciation | |
| Store economics | Cost to open a store, its yearly cash profit and its payback, for the chain and for a franchisee | |

The opening forecast rests on store economics. Stores get opened while they pay back, and
openings slow and closures rise when they stop. In a franchise chain it is the
franchisee's payback that matters, not the chain's.

## 3. The data behind the rows

- **Company.** Disclosure varies widely. Chains listed in the US report quarterly:
  same-store growth, stores by ownership and market, openings, system sales, and for
  company stores the store-level margin and its cost lines. Some split same-store growth
  into visits and spend; others give that only on the results call, or not at all.
  Chains listed in Hong Kong report twice a year: stores by city tier, franchised
  closures and goods sold to franchisees, and few give visits.
- **Industry**, which differs by market:

| Market | What exists |
| --- | --- |
| United States | Monthly government restaurant sales. Same-store and traffic trackers (Black Box Intelligence, Placer.ai), which miss delivery orders. The price index for food away from home. Prices of beef, chicken, dairy and coffee. Wage data |
| China | Monthly national catering revenue. Third-party store counts by brand. Delivery-platform data. Prices of coffee, tea, dairy and sugar |
| Elsewhere | National statistics and franchise disclosures, of uneven detail |

- **What leads revenue.** Store-count trackers. Traffic trackers. Announced price changes.
  Commodity prices. Changes in wage law. Delivery platforms' subsidy campaigns.
- **Backtest.** Stores times sales per store against system sales, then each revenue line
  against its own driver. Growth in system sales against store growth plus same-store
  growth, with the remainder explained by new-store ramp, ownership changes and currency.

## 4. Costs and margin

- In a company store, food and packaging move with sales and commodity prices. Staff and
  rent are largely fixed for each store, so store profit moves much more than sales.
- A price rise lifts the margin only if visits hold. Keep price and visits apart.
- Delivery brings commissions and packaging costs. A platform subsidy raises visits at a
  lower spend, and reverses when it ends.
- A new store sells less and earns a thinner margin while it ramps, and takes sales from
  stores nearby.
- Royalty income carries little cost, but depends on franchisees staying profitable. A
  chain may cut its supply prices or royalties to keep them, and that comes out of its
  own margin.
- In the supply model the profit is the gross profit on goods: raw materials, the chain's
  own factories and logistics. Where food costs are passed through, or supply profit is
  shared with franchisees, judge it in money, because the margin percentage moves with
  food prices.
- Advertising funds paid in by franchisees appear as revenue with an equal cost. Leave
  them out of margins.

## 5. Capacity, capex and working capital

- Capex is new company stores times the cost of each, plus refits, kitchens, roasting
  plants, warehouses and systems. Franchisees pay for their own stores.
- Under current lease accounting, rent appears as depreciation and interest. Compare
  store margins on one basis.
- Customers pay at once and suppliers are paid later, so cash arrives ahead of profit.
  Stored-value cards and loyalty points are liabilities.
- Selling company stores to franchisees cuts revenue, lifts the margin and books a gain,
  without changing the business.
- Closing stores brings write-offs and lease exit costs.

## 6. Cycle, policy and traps

- Saturation: sales per store fall as stores crowd each other, and closures follow.
- A price war or a round of platform subsidies lifts volumes, then reverses, and distorts
  same-store comparisons a year later.
- Consumers trade down when incomes are squeezed. Wage and minimum-wage rises, a
  food-safety incident or a boycott can change a year.
- Weather, the timing of holidays and an extra week move a quarter.
- Traps:
  - system sales read as revenue;
  - same-store pools defined differently, or leaving out closed stores;
  - spend per visit rising from price against mix;
  - store-level margin before or after rent, depreciation and delivery costs;
  - net store additions that hide closures;
  - sales before coupons and subsidies against net revenue;
  - "revenue per store" at a supply-model chain, which is goods sold to the store and not
    the store's own sales;
  - currency, a 53-week year, and fiscal quarters of unequal length.

## 7. What investors argue about, and the yardstick

- How many more stores the chain can open before sales per store fall.
- Whether same-store growth is visits or price.
- Whether a price war or subsidy period is temporary, and who is left after it.
- Whether franchisees earn enough to keep opening.
- Whether the margin holds against wages and commodity costs.

Yardstick: P/E and EV/EBITDA; store payback for a young chain; free cash flow yield for a
mature franchisor ([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A chain has 1,000 mature company stores that each sold 2.0 last year. Visits fall 1% and
spend per visit rises 4%, so same-store sales rise 3% to 2,060. It opens 200 stores, open
for half the year on average and selling 70% of a mature store: 140. Company-store revenue
is 2,200. Its 500 franchised stores sell 1.8 each, 900 in all, and pay a 5% royalty: 45.
Revenue is 2,245 on system sales of 3,100.

In the mature stores, 40% of sales goes on costs that move with sales and 800 is fixed.
Store profit is 436. Had same-store sales fallen 3% instead, it would be 364: 17% less
profit on 6% less sales.

If the chain also supplies its franchisees, and they buy goods worth 30% of their sales,
supply revenue is 270. At a 12% margin that is 32 of profit. If food costs rise 10% and
are passed through, supply revenue rises to 297 with the same 32 of profit, and the
margin falls to 10.9% though nothing has gone wrong.

All figures are invented. They show the relationships, not a forecast.
