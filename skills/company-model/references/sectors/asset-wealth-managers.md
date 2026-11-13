# Asset and wealth managers

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

- An **asset manager** invests clients' money in funds and mandates, and charges a yearly
  fee as a share of the assets. Some products also pay a fee on performance.
- A **wealth platform** holds and administers investments for savers and advisers. It
  earns a platform fee on the assets, a share of the fund managers' fees, charges on
  trades and currency conversion, and interest on clients' cash.
- An **administrator** runs pension or fund schemes for a fee per member or on assets,
  under multi-year contracts.

Revenue follows assets, and assets move for two reasons. Markets rise and fall, which the
company cannot control. Clients add or withdraw money, which follows performance, the
reach of the sales channel and what savers currently want to own. Regulators decide what
fees may be charged, and interest rates decide what client cash earns.

Four pairs of numbers get confused. Assets **managed** against assets **administered**,
which earn far less. **Period-end** assets against the **average** over the period, which
is what fees are charged on. **Gross** sales against **net** flows after withdrawals.
**Gross** fees against fees **net** of what is passed on to distributors.

Signs the card does not fit: the company earns mainly from trading commissions and loans
to investors, which is a broker (see the [brokers card](brokers.md)); it takes deposits
and lends, which is a bank (see the [banks card](banks.md)); or most of
its profit is a share of gains on private investments, which arrives irregularly and needs
its own build.

## 2. The driver tree

Build each product group or client channel separately, with history beside the forecast.
Use whichever split the company gives its assets by. Where fees are not split the same
way, use one fee rate and say so.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Opening assets | By asset class, product and channel. Assets of joint ventures and associates apart, since their fees are not in revenue | Total assets |
| Market movement | Each asset class's share times the return of its market, plus currency | One blended return |
| Net flows | Sales less withdrawals by product. Large mandates and new schemes on their own rows, with start dates. Assets sold through a partner's network under an agreement on their own row, with the date it expires | Net flows as a share of opening assets, from history |
| Changes in scope | Assets bought, sold or moved between units | Leave it out only where there are none |
| Closing and average assets | Opening, plus market movement, plus net flows, plus changes in scope. Average the period-end figures, monthly where they are published | |
| Fee rate | By product, net of what is passed to distributors, on consolidated assets only. It falls as money moves from active funds to index funds and other cheaper products, and when fees are cut | Fees divided by average consolidated assets, from history |
| Asset-based fees | Average assets times the fee rate | |
| Performance fees | Returns above each product's hurdle. Keep them out of the recurring base | Leave them out, and say so |
| Trading and currency income | Clients' trading volume times the charge on each trade | Its past ratio to assets |
| Interest on client cash | Client cash balances times the spread kept | Its past ratio to assets, moved with interest rates |
| Contract fees | Members or assets served times the fee, as each scheme comes on | Contract revenue as reported |
| Other revenue | Technology and services sold to other managers, and income on the company's own money | As reported |
| Joint ventures and associates | The company's share of their profit, which arrives below revenue, built from their own assets and fees | The share of profit as reported |
| Costs | Staff, with the bonus pool tied to revenue; technology; and other fixed cost | Costs as a share of revenue |

## 3. The data behind the rows

- **Company.** Disclosure varies. Some managers publish assets and net flows every month.
  Others report quarterly: assets by class, net flows, and revenue split between recurring
  and one-off. Fee rates are often left for the analyst to derive.
- **Industry:**

| Source | What exists |
| --- | --- |
| Markets | Index levels and interest rates, daily. These give most of the period's asset movement before the company reports |
| Flows | Fund flow data by asset class from fund industry bodies (ICI in the US, EFAMA in Europe, AMAC in China) and data providers (Morningstar) |
| Schemes | Statistics from pension regulators on members and assets |
| Rules | Regulators' decisions on fund fees and on payments to distributors |

- **What leads revenue.** Index levels through the period. Monthly flows. New fund
  launches. Mandates and schemes already announced, with their start dates. Rate changes.
- **Backtest.** Opening assets, plus market movement, plus net flows, against closing
  assets. Average assets times the fee rate against fee revenue.

## 4. Costs and margin

- Staff are the largest cost, and part of their pay moves with revenue. Technology and the
  rest are fixed.
- Because most cost is fixed, profit moves more than assets do, in both directions.
- Fee rates drift down: money moves to cheaper products, and regulators cut fees.
- A new administration contract brings cost before revenue. A new banking or lending arm
  loses money while it builds.
- Gains and losses on the company's own seed investments are not operating profit.

## 5. Capacity, capex and working capital

- Little capital is needed, except where a bank or broker arm must hold regulatory
  capital.
- Clients' money is held apart and is not the company's cash.
- Most managers pay out a large share of profit, and buy other managers to add assets.

## 6. Cycle, policy and traps

- Markets drive assets, revenue and, with more force, profit.
- Flows follow performance and fashion, and can reverse within a year.
- When rates fall, interest on client cash falls with them.
- Traps:
  - period-end assets used where the average belongs;
  - assets that earn little or nothing counted with the rest;
  - headline assets that include joint ventures and associates, whose fees are not in
    revenue;
  - assets changed by a purchase, a sale or a transfer and read as flows;
  - a large mandate won at a thin fee read as growth;
  - performance fees in the recurring base;
  - gross fees read as net;
  - one-off set-up fees on a new contract;
  - gains on seed investments inside profit;
  - assets moved by the exchange rate.

## 7. What investors argue about, and the yardstick

- How much of asset growth is markets and how much is new money.
- How fast fees fall.
- How much profit grows as a platform's assets grow against a fixed cost base.
- Whether income from a new contract or a new arm lasts.
- What a fall in interest rates takes away.

Yardstick: P/E, with market value as a share of consolidated assets as a check
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A manager opens with assets of 100bn. Markets add 10% and clients add a net 5bn, so it
closes at 115bn and averages 107.5bn. At a fee of 0.50% that is 537.5m of revenue. Costs
are 350m, so profit is 187.5m.

Had markets fallen 10% instead, it would close at 95bn and average 97.5bn. Revenue would
be 487.5m, 9% lower, and profit 137.5m, 27% lower.

All figures are invented. They show the relationships, not a forecast.
