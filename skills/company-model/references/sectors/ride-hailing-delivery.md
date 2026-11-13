# Ride-hailing and delivery platforms

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A platform matches people who want a ride or a delivery with drivers, couriers and
merchants, and keeps part of what the customer pays.

- **Rides.** The passenger pays a fare. The platform keeps a share and the driver gets the
  rest.
- **Delivery** of meals, groceries and goods. The customer pays for the order plus fees.
  The merchant pays a commission. The courier is paid per drop. Where the platform's own
  couriers deliver, it may book the delivery fee as revenue and the courier's pay as a
  cost; where the merchant delivers, it books only the commission.
- **Advertising** sold to merchants who want to appear first. It costs almost nothing to
  serve.
- **Subscriptions**, which cut fees for frequent users.
- **Other units**, such as lending, payments or freight, which follow different rules.

Three groups decide demand. Customers decide how often they order and how much they
spend. Drivers and couriers decide whether the pay is worth their time. Rivals decide how
much has to be given away in discounts and bonuses to hold both.

Three numbers get confused. **Gross bookings**, also called gross merchandise value, are
everything customers spend through the platform. **Revenue** is the part the platform
books, and depends on accounting: whether it treats itself as the seller of the service,
and whether discounts are taken off revenue or shown as a cost. **Take rate** is
commission and fee revenue, after the incentives netted against it, divided by gross
bookings. It moves with those accounting choices as well as with the business.
Advertising and subscriptions are counted apart from it.

Signs the card does not fit: the company's main product is delivery sold to other
businesses, which is a logistics firm (see the
[logistics and express card](logistics-express.md); a platform that pays couriers to
carry its own orders still fits); it earns mainly from advertising on content or search
(see the [e-commerce and advertising card](ecommerce-advertising-platforms.md)); or a unit
that holds stock and sells goods itself, or a lending or payments arm, earns more than
about 15% of profit or revenue, in which case that unit gets its own build under
[when no card fits](index.md#when-no-card-fits).

## 2. The driver tree

Build each service and market that the company reports separately, with history beside
the forecast.

There are two routes. Where the company publishes gross bookings, orders or users, build
from users down to revenue with the rows below. Where it publishes only revenue by type,
build each type on its own. Delivery revenue is the orders the platform itself delivers
times the fee per order after discounts. Commission is merchants' sales times the
commission rate, and advertising is its own line. Where those two are reported as one
line and merchants' sales are not published, forecast the line as estimated orders times
revenue per order, taken from the line's own history. Goods the platform sells from its
own stock are a retail business and get their own build.

Orders then have to be estimated. Start from the last count the company published and
move it with revenue, with app-usage trackers and with what rivals report. A peak-day
figure in a press release is not an average. Delivery cost divided by courier pay per
order is a check, but only where the delivery cost covers the same business. Label every
such figure as an estimate. The cost rows below apply to both routes.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Active users | Users of each service on the company's own definition, monthly or yearly. A user of two services counts once in the group total. A tracker's count of app users is a different number | Group users |
| Frequency | Orders or trips per user per month | Orders divided by users |
| Orders | Users times frequency | Order growth |
| Value per order | Fare or basket, moved by price, distance and mix | Gross bookings divided by orders |
| Gross bookings | Orders times value per order, at constant exchange rates and then translated | Growth in gross bookings by service |
| Incentives | Customer discounts and driver or courier bonuses, each as a share of gross bookings, or of revenue where bookings are not published | The take rate, which absorbs them |
| Take rate | Commission and fees, less the incentives netted against revenue. Restate for changes in how revenue is booked | Take rate from history |
| Revenue | Gross bookings times take rate, plus advertising and subscriptions on their own rows. Split out any other business reported inside the same segment, such as vouchers or hotel booking | |
| Cost per order | Driver or courier pay where the platform books it, insurance, payment processing and support | Segment margin as a share of gross bookings |
| Segment profit | Per order, and as a share of gross bookings | |
| Central costs | Technology, marketing, administration and share-based pay | |
| Supply | Active drivers or couriers, and their earnings per hour | Leave it out |

Read profit as a share of gross bookings as well as of revenue. Revenue moves when the
accounting changes; gross bookings do not. Where gross bookings are not published, read
profit as a share of revenue and say so.

## 3. The data behind the rows

- **Company.** Most platforms report each quarter: gross bookings and revenue by service,
  orders or trips, monthly users and profit by service. Some give incentives separately,
  split between customers and drivers. Some state how much a change in accounting moved
  revenue growth. Few give value per order or frequency directly, but both can be
  derived.
- **Industry:**

| Source | What exists |
| --- | --- |
| Usage | App download and usage trackers (Sensor Tower; QuestMobile in China). Card-spending panels that estimate each platform's share, where they exist |
| Rivals | Competitors' own reports, and announcements of subsidy programmes |
| Regulators | Rules on driver status, minimum pay, commission caps and subsidies, with their start dates, and fines. Order counts where a regulator publishes them |
| Merchants | Restaurant and retail sales, as the pool delivery draws from |

- **What leads revenue.** App usage. A rival's subsidy campaign. Dates when pay or
  commission rules start. Fuel prices, where drivers use cars. Weather.
- **Backtest.** Users times frequency times value per order against gross bookings. Gross
  bookings times take rate against revenue. On the second route, each revenue line
  against its estimated driver.

## 4. Costs and margin

- Incentives are what swings. A rival's campaign forces more discounts and bonuses, and
  profit falls with no change in orders.
- Courier cost per order falls as orders in an area get denser and can be batched.
- Insurance is a large cost of rides in some markets, and its reserves can be reset.
- Advertising and subscriptions carry little cost, so a small share of revenue can be a
  large share of profit.
- Central costs grow more slowly than gross bookings, which is where the margin comes
  from as a platform matures.
- Share-based pay is large. Show profit with it and without it.

## 5. Capacity, capex and working capital

- A platform owns little, so capex is small. Check for exceptions: vehicles, warehouses
  for fast grocery delivery, or self-driving fleets.
- It collects from customers before paying drivers and merchants, so it holds their cash.
  Some of its cash is restricted, for insurance or for regulators.
- Stakes in other platforms are marked to market and can swing net profit. Keep them out
  of the operating build.

## 6. Cycle, policy and traps

- Subsidy wars: a new entrant buys share with discounts, profit falls across the market,
  and it recovers when one side stops.
- Rules on driver and courier status, minimum pay and commission caps reset costs on a
  known date.
- Self-driving vehicles could add supply or bypass the platform. Treat either as a
  scenario until fleets are operating at scale.
- Orders move with weather, holidays and consumer spending.
- Traps:
  - gross bookings read as revenue;
  - take rates compared across companies that book revenue differently;
  - revenue growth changed by a change in accounting, with no change in the business;
  - incentives netted against revenue at one company and shown as marketing at another;
  - profit measures that leave out share-based pay and legal or regulatory charges;
  - operating or net profit moved by gains on investments and stakes in other companies;
  - users counted once for each service and added up;
  - growth at constant exchange rates against reported growth.

## 7. What investors argue about, and the yardstick

- Whether profit as a share of gross bookings keeps rising, and how far.
- Whether a subsidy war is temporary, and who is left after it.
- Whether self-driving vehicles help the platform or replace it.
- Whether rules on driver status and pay raise costs for good.
- Whether new services, such as grocery and advertising, extend growth.

Yardstick: EV to adjusted EBITDA while reported profit is thin, then P/E or free cash
flow yield once it is real ([yardstick list](../../../valuation-thesis/references/yardsticks.md)).
Value a loss-making new business apart from a profitable core, as a sum of the parts.

## Worked build

A platform has 10 million monthly users who each order 5 times a month at 20 an order:
600 million orders and gross bookings of 12bn a year. It keeps 20%, so revenue is 2.4bn.

A rival starts a discount campaign. To hold its users the platform gives away another 2%
of gross bookings in discounts, which come off revenue. Orders and gross bookings are
unchanged. Revenue falls 10% to 2.16bn, and since no cost has fallen, profit falls by the
whole 240m.

On the second route, a platform reports delivery revenue of 3.0bn and is estimated to
deliver 1bn orders itself, so it books 3.0 an order. If discounts taken off the fee rise
by 0.3 an order, delivery revenue falls 10% with orders unchanged.

All figures are invented. They show the relationships, not a forecast.
