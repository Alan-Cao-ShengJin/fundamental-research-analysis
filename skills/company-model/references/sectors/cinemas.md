# Cinemas

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

Cinemas sell tickets, food and drink, and advertising on their screens. The box office
is shared with the distributor and producer, who are paid film rental. Chinese cinemas
keep roughly half after a levy and tax. US cinemas keep rather less, and less still on
the biggest films. A cinema's own costs are rent, depreciation
and staff, which are fixed.

Many chains also run a circuit: cinemas owned by others that take the chain's brand and
booking, and pay it a fee.

The films on release decide how many people go. A few titles make a year, and holidays
are the peaks. Where screens have been built faster than audiences have grown, the box
office for each screen falls.

Numbers that get confused:

- Box office **with** the ticketing fee against box office **without** it, and both
  against the cinema's ticket revenue.
- The **national** box office against the box office of the **company's cinemas**.
- The share of the cinemas the company **owns** against the share of its whole
  **circuit**.
- **Admissions** against **ticket price**.
- **Rent** paid against the lease charges in the accounts.

Signs the card does not fit: the company makes or distributes films (see the
[film and television production card](film-tv-production.md), and build that unit there);
it streams films to subscribers (see the [streaming card](streaming.md)); or it runs
theme parks (see the [theme parks and tourist sites card](theme-parks-sites.md)).

## 2. The driver tree

Build cinemas at home and cinemas abroad separately, with history beside the forecast.
A chain that reports its own admissions and ticket price is built from those, by
region, with the national box office as the check.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| National box office | Admissions times ticket price, from the films due, the holidays and last year's base | The average of several past years, with this year's main titles named |
| Screens and share | The company's cinemas and screens, with openings and closures, and its share of the national box office | Hold the latest share |
| Admissions and ticket price | The company's admissions times its average ticket price, which rises with premium screens and formats | Its box office over the national ticket price |
| Ticket revenue | The company's box office, less any ticketing fees, levies and tax | Its past ratio to box office |
| Film rental | The share of ticket revenue paid to distributors, which rises a little when the biggest films are showing | Its past ratio |
| Food and merchandise | Admissions times spend per visitor, less the cost of the goods | Its past ratio to admissions |
| Advertising and other | Screen advertising for each screen or each visitor, by contract. Booking fees and other income | Their own trend |
| Circuit fees | Fees from cinemas owned by others | Their own growth |
| Cinema costs | Rent, both fixed and tied to sales, depreciation, staff and power, for each cinema. Staff and power move a little with admissions | Their past level per screen, grown with screens |
| Leases | Lease liabilities. Some accounting rules turn rent into interest and depreciation, and others keep it as one expense | As reported |
| Cinemas abroad | Box office, admissions and costs by country or region, translated, with inflation and currency | Segment profit |
| Overheads and goodwill | Head office, and goodwill on cinemas bought | Their share of revenue |
| Cash and debt | Debt, leases, dividends, buybacks and the share count | As reported |

## 3. The data behind the rows

- **Company.** Box office, admissions, cinemas, screens and share. Revenue by line.
  Chinese chains give few costs by kind. US chains give admissions, ticket price, food
  spend for each visitor and costs by line, by region, each quarter.
- **Industry:**

| Source | What exists |
| --- | --- |
| Box office | Daily box office by title and by cinema circuit (Maoyan and Dengta in China, Comscore and Box Office Mojo elsewhere). The film authority's yearly totals |
| Films due | The release calendar, approvals and advance sales |
| Screens | The number of screens in the country, and openings and closures |
| Peers | Circuit rankings and other chains' results |

- **What leads revenue.** The films due and their advance sales. Daily box office.
  Holiday bookings.
- **Backtest.** National box office times share against the company's box office. Box
  office against ticket revenue. Fixed cost for each screen.

## 4. Costs and margin

- A cinema's costs are mostly fixed, so profit swings hard with admissions and turns to
  loss in a weak year.
- Film rental moves with the box office.
- Food and advertising earn a high margin.

## 5. Capacity, capex and working capital

- Cinemas are leased for many years. Rent is owed whether or not people come.
- Chains that grew by buying cinemas carry goodwill.
- Fitting out a new cinema is capex, and screens and seats need replacing.

## 6. Cycle, policy and traps

- A year is made by its films, so results follow the release calendar more than the
  economy.
- In China regulators decide which films are released and when. Elsewhere, the weeks a
  film stays in cinemas before it reaches streaming affect admissions.
- Traps:
  - the share of the whole circuit read as the share of the cinemas the company owns;
  - a blockbuster quarter multiplied by four;
  - a record year taken as the normal one;
  - box office with fees read as ticket revenue;
  - profit before rent quoted for a business whose main cost is rent;
  - goodwill that weak years have not yet tested.

## 7. What investors argue about, and the yardstick

- Whether audiences return to their old level, given streaming and short video.
- How many strong films are coming, local and foreign.
- How many screens close.
- Whether ticket prices can rise.

Yardstick: P/E on a normal year. In loss years, EV/EBITDA with rent counted as a cost,
and P/B ([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

The national box office is 1,000 and the company's cinemas take 15%, which is 150. After
fees, levies and tax, ticket revenue is 135. Film rental is 45% of that, 61. Food and
advertising bring 30 at a margin of 70%, which is 21. Fixed costs are 80. Profit is 15.

The box office rises 20%. Ticket revenue is 162, rental 73, food and advertising earn
25, and profit is 34, more than double. If the box office falls 20% instead, profit is
108 less 49, plus 17, less 80: a loss of 4.

The build treats the whole change as admissions and holds rental at 45% and other costs
flat. In a strong period rental rises a little and rent tied to sales rises with it.

All figures are invented. They show the relationships, not a forecast.
