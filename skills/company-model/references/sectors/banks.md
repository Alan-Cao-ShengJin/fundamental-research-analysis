# Banks

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A bank takes deposits and borrows, then lends and invests. It earns in three ways.

- **Net interest income**: what it earns on loans and investments, less what it pays on
  deposits and borrowing.
- **Fees**: for cards, payments, selling funds and insurance, and arranging finance.
- **Trading and investment gains**, which swing from year to year.

Against that it sets operating costs and the loans that go bad. A bank's statements are
its own kind: there is no revenue line to build from units and price, and no factory. The
balance sheet is the business.

Several parties decide the result. Borrowers decide loan demand, which follows the
economy. The central bank sets the rates that loans and deposits reprice from. Savers
decide whether money sits in cheap current accounts or dearer fixed deposits. Regulators
set how much capital the bank must hold, which caps how fast it can grow and how much it
can pay out. In some countries the state also directs lending and sets the rates banks
may offer.

Signs the card does not fit: the lender takes no deposits (see the
[non-bank lenders card](non-bank-lenders.md)); it earns mainly from trading commissions
(see the [brokers card](brokers.md)) or from managing money (see the
[asset and wealth managers card](asset-wealth-managers.md)); or it arranges loans that
others fund.

## 2. The driver tree

Build the balance sheet first and the income statement from it, with history beside the
forecast.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Loans | By type: companies, bills, mortgages, consumer, credit cards, small business. Growth from the banking system's credit growth and the bank's share, limited by capital | Total loan growth |
| Other earning assets | Bonds, lending to other banks and balances at the central bank | Total earning assets |
| Asset yield | By asset. Loans reprice from the benchmark lending rate, with a lag that depends on how many are floating and on what date they reset | Total yield, moved by part of the change in the benchmark rate, the part taken from past rate moves |
| Deposits and borrowing | Current and savings accounts, fixed deposits, and market borrowing | Total funding |
| Funding cost | Rate by type times the mix. How much of a rate change reaches depositors, and the drift from current accounts to fixed deposits | Total cost, moved by part of the rate change, the part taken from past rate moves |
| Net interest income | Interest earned on each asset less interest paid on each kind of funding. Check it as average earning assets times the net interest margin, which is net interest income over average earning assets and is not the same number as yield less funding cost | Average earning assets times the reported margin |
| Fees | By line, each from its own driver: card spending, payment volumes, deals, and for wealth business the clients' assets and the funds and insurance sold to them | Fee growth |
| Trading and investment gains | Rate moves on the bonds that are marked to market through profit, and markets | A normal level from history, with the latest year's excess named |
| Operating costs | Staff, branches and technology | The cost-to-income ratio |
| Loan losses | New bad loans by type times the loss on each, less recoveries, and the cover the bank wants to hold against them, taken from what management says or has kept in the past | Loan losses as a share of average loans |
| Tax | Including income that is tax-exempt | The effective rate |
| Capital | Risk-weighted assets, profit kept, dividends and new capital raised, giving the capital ratio. The limit is the regulator's minimum plus the margin the bank has kept above it | The ratio as reported |
| Profit for ordinary shareholders | Net profit, less minority interests, less payments on capital securities. Then earnings, book value and dividend per ordinary share | |

Close the loop: loan growth uses capital, profit kept supplies it, and the dividend is
what is left without the ratio falling too far.

## 3. The data behind the rows

- **Company.** Most banks report each quarter: the interest margin, loans and deposits
  by type, the bad-loan ratio and the cover against it, loan losses, fees by line and
  capital ratios. In some markets the first- and third-quarter reports are much thinner
  than the half-year and annual ones. Annual reports add how soon assets and liabilities
  reprice, loans by industry, loans by stage of impairment, and the sensitivity of
  interest income to a rate change.
- **Industry:**

| Source | What exists |
| --- | --- |
| Central bank | Policy rates and benchmark lending and deposit rates. Monthly system loans, deposits and money supply |
| Regulator | Quarterly figures for the whole sector by type of bank: margin, bad-loan ratio, cover and capital |
| Markets | Government bond yields, which move the bond book. Property sales and prices, which move mortgage quality |
| Rules | Capital and provisioning rules, deposit-rate ceilings, and state capital injections |

- **What leads profit.** Policy-rate changes and the dates loans reset. Monthly credit
  data. Bond yields. The property market. Deposit-rate cuts.
- **Backtest.** Average earning assets times the margin against net interest income.
  Average loans times the loss rate against the impairment charge.

## 4. Costs and margin

- A small change in the interest margin is a large change in profit, because it applies
  to the whole balance sheet.
- When rates fall, loan yields usually fall before deposit costs, and the margin narrows.
  When rates rise the reverse holds, unless savers move to fixed deposits.
- Loan losses are the cyclical swing. They are low for years and then take most of a
  year's profit. In some banking systems the charge is smoothed instead, with cover built
  up in good years and drawn on in bad ones.
- A bank holding more cover than it needs can release it to steady profit. Check the
  cover as well as the charge.
- Gains on bonds come when yields fall. They do not repeat once yields stop falling.

## 5. Capacity, capex and working capital

- Capital is the capacity. A bank whose profit does not cover its growth and its dividend
  must slow down, cut the dividend or raise capital, which dilutes holders.
- Securities that rank between debt and shares count as capital and are paid before
  ordinary shareholders.
- Bonds held to maturity can carry losses that are not in profit or capital. They matter
  if the bank is forced to sell.
- Promises outside the balance sheet, such as guarantees and savings products sold to
  clients, can come back onto it.

## 6. Cycle, policy and traps

- Two cycles drive profit: interest rates, through the margin, and credit, through loan
  losses.
- Where the state directs banks to support the economy, it can ask for lower loan rates,
  lending to weak borrowers and patience with those who cannot pay.
- Traps:
  - a bad-loan ratio held down by writing loans off, by rolling them over or by fast loan
    growth;
  - overdue loans not yet classed as bad;
  - profit growth supplied by releasing cover;
  - bond gains inside non-interest income;
  - margins defined differently from bank to bank;
  - return on equity in a good year read as normal;
  - dividends counted before payments on capital securities;
  - a different tax on dividends for different classes of the same bank's shares.

## 7. What investors argue about, and the yardstick

- Whether the margin has stopped falling.
- How good the loans really are.
- Whether the dividend can be kept without raising capital.
- How far the bank is run for the state and how far for its shareholders.

Yardstick: P/B against return on equity; dividend yield for a bank that pays out a large
share of profit ([yardstick list](../../../valuation-thesis/references/yardsticks.md)). Do
not use enterprise value: deposits are the raw material, not debt to be added back.

## Worked build

A bank has earning assets of 1,000 and a margin of 1.6%, so net interest income is 16.
Fees add 4. Costs are 7. Loans are 600 and 0.5% is lost, which is 3. Profit before tax is
10 and after tax 8. Equity is 80, so the return is 10%.

If the margin falls by 0.1 of a point, net interest income falls by 1 and profit after
tax by 10%. If loan losses rise by 0.2 of a point, profit falls by 12%.

Its risk-weighted assets are 650 and its core capital 70, a ratio of 10.8%. Growing loans
by 10% adds 65 of risk-weighted assets, which needs 7 of capital to hold the ratio. It
earns 8 and pays out 30%, keeping 5.6. The ratio falls unless growth slows, the payout is
cut or capital is raised.

All figures are invented. They show the relationships, not a forecast.

Adaptation credit and licence: [notice](NOTICE.txt).
