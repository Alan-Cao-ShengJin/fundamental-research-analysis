# Securities brokers

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A securities broker earns in six ways, in very different proportions from firm to firm.

- **Commissions** on clients' share trading.
- **Interest** on money lent to clients to buy shares, on clients' idle cash, and on
  shares lent to other investors. For an online broker this can be most of revenue, and
  it moves with interest rates.
- **Fees** for selling and managing funds and for advice to savers.
- **Investment banking fees** for arranging share and bond issues and for advising on
  deals.
- **Gains and losses on its own trading and investments** in shares, bonds and
  derivatives. For many firms this is the largest line and the most volatile.
- **Its share of profit** from fund managers and other companies it partly owns.

The market decides almost all of it. Commissions and lending follow trading turnover and
investors' confidence. Investment banking follows how many issues the regulator and the
market allow. The firm's own book follows share and bond prices. Regulators set how much
the firm may borrow against its capital, what it may charge and how fast new issues are
approved.

Three things get confused. The **market's** turnover and lending against the **firm's**
share of each. **Fee businesses**, which need little capital, against **balance-sheet
businesses** (lending, trading, derivatives), which need a great deal. **Clients' money**,
which sits on the balance sheet, against the firm's own.

Signs the card does not fit: the company mainly manages money for fees (see the
[asset and wealth managers card](asset-wealth-managers.md)); it runs an exchange; it is a
bank's securities arm reported inside the bank; or it is an advisory firm with no trading
or lending.

## 2. The driver tree

Build each business line separately, with history beside the forecast.

There are two routes to commissions. A broker that is one of many in a single market is
built from the market's turnover and its share. An online broker that reports its own
activity is built from client accounts, trades per account and commission per trade, by
product.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Market turnover | Average daily turnover times trading days, by market | Turnover growth |
| Share of turnover | The firm's clients' trading as a share of the market's | Hold the latest share |
| Commission rate | Commission on the basis the firm charges: per unit of value, per share or per order, by product. It tends to fall, and moves with the mix of products. Exchange and regulatory fees collected from clients and passed on are not the firm's | Commission revenue divided by clients' turnover, from history |
| Commissions | Market turnover times share times rate | Commission revenue moved with market turnover |
| Net interest | Built as one table so that funding is counted once. Interest earned on loans to clients, on clients' cash the firm holds, and on shares lent, each as balance times rate. Less interest paid on clients' credit balances and on the firm's borrowing. Each rate follows the benchmark interest rate by its own share | Net interest moved with client balances and with the benchmark rate, using the sensitivity the firm discloses |
| Fund and advice fees | Client assets times the fee rate | Fee growth |
| Investment banking | Issues expected, by type, times the firm's share times the fee rate | A normal level from history |
| Own trading and investments | The book by asset type times an expected return, with its sensitivity to share prices and bond yields | A normal return on the book, with the latest year's excess named |
| Associates | The share of profit of each material one, built as what it is | As reported |
| Costs | Staff, with pay tied to revenue, technology, trading and clearing charges, and other fixed cost. The mix differs widely: staff dominate at a full-service firm and not at an online one | Costs as a share of revenue |
| Credit losses | Loans against shares that fall below their collateral | A normal charge, raised in a falling market |
| Capital and borrowing | Equity, the permitted multiple of borrowing and so the size of the book | Assets over equity as reported |
| Profit for ordinary shareholders | Net profit less the share that belongs to other owners of the operating business | |

## 3. The data behind the rows

- **Company.** Brokers report quarterly, with revenue by line every quarter in some
  markets and twice a year in others. Online brokers add client numbers, client assets,
  trades per day, loan and cash balances, and often publish them monthly. Few give their
  share of turnover or commission rate directly, but both can be derived.
- **Industry:**

| Source | What exists |
| --- | --- |
| Exchanges | Daily turnover. The daily balance of lending to investors. New accounts opened. Share and bond issues and the amounts raised |
| Markets | Share indices and bond yields, daily. These give most of a quarter's trading result before the firm reports |
| Industry body and regulator | Quarterly results for the whole industry. Rules on borrowing, on lending to investors and on fees |

- **What leads profit.** Daily turnover and lending balances. Interest rates. Index
  moves. Issue approvals. New accounts. Policy announcements aimed at the market.
- **Backtest.** Market turnover times share times rate against commission revenue. The
  book times index and yield moves against the trading result.

## 4. Costs and margin

- Costs are mostly staff and partly move with revenue. The rest is fixed, so profit moves
  much more than turnover.
- The firm's own book decides whether a year is good or bad more often than commissions
  do.
- Commission rates fall over time, so turnover has to grow just to hold revenue.
- Lending to investors earns a steady spread until the market falls, when collateral can
  be worth less than the loan.

## 5. Capacity, capex and working capital

- Lending, trading and derivatives use capital. Return on equity is capped by how much
  borrowing the rules allow.
- Brokers raise capital in good markets by selling shares, which dilutes holders.
- Regulators in some markets push brokers to merge.

## 6. Cycle, policy and traps

- Everything follows the market, so broker shares move further than the market does.
- A government that wants a firmer market can change the rules on trading costs, lending
  and issues at short notice.
- When new issues are paused, investment banking fees can fall by most of their value.
- Traps:
  - a strong quarter multiplied by four;
  - gains on the firm's own book treated as recurring;
  - turnover growth read as commission growth when the rate is falling;
  - lending income shown before the cost of funding it;
  - profit from part-owned fund managers counted as broking;
  - clients' cash counted as the firm's;
  - investment income classed differently from firm to firm.

## 7. What investors argue about, and the yardstick

- Whether the current level of turnover lasts.
- Which firms gain from mergers.
- Whether fee income from savers can replace falling commissions.
- How high return on equity can go under the borrowing rules.

Yardstick: P/B, read against where the market cycle stands; P/E for a broker that earns
mainly fees and interest on client balances ([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

The market trades 1,000bn a day for 240 days. The firm's clients are 5% of that, 12,000bn
a year. At a commission of 0.025% it earns 3.0bn. If turnover falls 30%, commissions fall
to 2.1bn.

The firm's own book is 100bn on equity of 20bn, with a fifth in shares. A 10% fall in
share prices costs 2bn, a tenth of its equity and two-thirds of a year's commissions.

All figures are invented. They show the relationships, not a forecast.
