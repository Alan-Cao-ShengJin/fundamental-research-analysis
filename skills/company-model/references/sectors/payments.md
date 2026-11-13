# Payments

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A payment company moves money between a payer and a merchant and keeps a small share of
each payment. There are three main kinds.

- **Card networks** connect the banks on each side. They charge a fee on the value paid
  and a fee for each transaction, and give some of it back to large banks and merchants
  as incentives.
- **Processors and acquirers** let merchants accept payments. The merchant pays a fee, and
  most of it is passed on to the cardholder's bank and the network. What the processor
  keeps is its net revenue.
- **Wallets and transfer services** hold customers' balances and move money for
  consumers, charging merchants or the sender.

Many also sell extra services: fraud tools, software for merchants, card issuing and
lending.

Volume follows consumer spending and the shift from cash to electronic payment.
Cross-border volume follows travel and online trade, and earns far more per payment. What
the company keeps per payment depends on the merchant and the product. Large merchants pay
least. A wallet's own checkout button earns more than processing done under a merchant's
brand, and transfers between friends earn almost nothing.
Regulators cap what can be charged, and new bank-to-bank payment systems compete on
price.

Three numbers get confused. **Payment volume**, which is the money moved. **Gross
revenue**, which includes the fees passed on to others. **Net revenue**, which is what
the company keeps. The **take rate** is revenue over volume, so it depends on which
revenue is used.

Companies use these words differently. A network reports revenue after incentives. A
processor may report before or after the fees it passes on. A wallet usually reports
revenue before the fees it pays to banks and networks and shows them as a cost. What is
left after that cost and after losses is often called the transaction margin. Put every
company on that basis before comparing them.

Signs the card does not fit: lending earns most of the profit (see the
[non-bank lenders card](non-bank-lenders.md)); the company is a bank (see the
[banks card](banks.md)); or payments are an add-on to software it sells, in which case
build the software first (see the [software card](software.md)).

## 2. The driver tree

Build each product or channel and each region separately, with history beside the
forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Payment volume | Consumer spending, times the share paid electronically, times the company's share. For a wallet, active accounts times payments per account times the average payment. Home and cross-border apart. By product, channel and size of merchant where given | Volume growth |
| Transactions | Volume divided by the average payment | Leave it inside volume |
| Take rate | Fees per unit of volume and per transaction, by product and kind of merchant, on the revenue the company reports. It falls as large merchants and lower-priced products become a bigger share. Currency-conversion fees move with cross-border volume | Reported revenue over volume, from history |
| Incentives and passed-on fees | For a network, incentives to clients. For a processor or wallet, the fees paid to banks and networks, which depend on how each payment is funded | As a share of volume |
| Payment revenue | Volume times take rate. Deduct incentives and passed-on fees once: here if the company reports revenue after them, as a cost below if it reports before | |
| Extra services | Each on its own driver: merchants using it times the fee | Their own growth |
| Interest on balances | Customers' balances held times the rate earned | Its past ratio to balances, moved with interest rates |
| Losses | Fraud, refunds and, where it lends, loan losses. Loans sold to outside investors take their losses with them | As a share of volume |
| Revenue after payment costs | All revenue, less passed-on fees and losses. Wallets guide on this figure as the transaction margin | |
| Operating costs | Technology, staff and marketing, with the fixed part shown | As a share of revenue after payment costs |
| Share count | Buybacks at the pace the company has set | Hold it flat |

## 3. The data behind the rows

- **Company.** Most report quarterly: payment volume, transactions, cross-border growth,
  net revenue, take rate or enough to derive it, and active accounts. Networks give
  incentives. Processors give volume by type of customer. Wallets give the transaction
  margin and the cost and loss rates behind it, and often growth by product without the
  amounts.
- **Industry:**

| Source | What exists |
| --- | --- |
| Spending | Monthly retail sales and consumer spending. Banks' card-spending data. The networks' own comments on recent weeks |
| Cross-border | Air passenger numbers and online trade |
| Payment habits | Central banks' statistics on payment methods |
| Rules | Caps on fees between banks, routing rules, and the growth of bank-to-bank instant payment |

- **What leads revenue.** Monthly spending data. Travel. Large merchants won or lost.
  Fee decisions by regulators. Interest rates.
- **Backtest.** Volume times take rate against reported revenue. Volume times the cost
  and loss rates against transaction costs.

## 4. Costs and margin

- Technology and staff are largely fixed. Passed-on fees and losses move with volume, and
  for a processor or wallet they are the larger cost. So the margin rises with volume by
  less than the fixed costs alone suggest.
- The take rate drifts down as large merchants and lower-priced products grow faster than
  the rest, so revenue grows more slowly than volume.
- A network's incentives grow with its largest clients' bargaining power.
- A wallet's cost depends on how customers fund payments. A payment funded from a bank
  account costs it far less than one funded by card.
- Interest on customers' balances is pure profit while rates are high.

## 5. Capacity, capex and working capital

- Little capital is needed. Money in transit and customers' balances sit on the balance
  sheet and are not the company's.
- A lending or pay-later arm needs funding and carries credit risk.

## 6. Cycle, policy and traps

- Volume follows spending. Cross-border volume follows travel, and falls furthest in a
  shock.
- A fee cap, a routing rule or a court settlement can lower the take rate at once.
- Bank-to-bank instant payment can take volume away from cards.
- Traps:
  - gross revenue compared with another company's net revenue;
  - volume growth read as revenue growth while the take rate falls;
  - customers' balances counted as cash;
  - interest on balances treated as lasting;
  - one large merchant leaving;
  - low-margin volume processed for others counted with the rest;
  - growth before and after currency effects.

## 7. What investors argue about, and the yardstick

- How fast the take rate falls.
- Whether instant bank payments and regulation erode the business.
- Whether extra services grow fast enough to matter.
- How far the margin can rise.

Yardstick: P/E and EV/EBITDA; EV to sales for a young company
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A processor handles 1,000 of payments. Merchants pay 1.5%, which is 15, and it passes 12
on to banks and the network. Net revenue is 3, a take rate of 0.30%.

Next year volume grows 20% to 1,200, but more of it comes from large merchants and the
take rate falls to 0.27%. Net revenue is 3.24, up 8%.

A wallet earns 3% on 400 paid through its own checkout button and pays 1% of that volume
to banks and networks, keeping 8. It earns 1.5% on 600 processed under merchants' brands
and pays 1.2%, keeping 1.8. Revenue is 21 and it keeps 9.8. If checkout grows 2% and
processing 20%, volume rises 13% and revenue 10%, but what it keeps rises only 5%.

All figures are invented. They show the relationships, not a forecast.
