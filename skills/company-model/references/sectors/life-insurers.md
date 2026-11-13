# Life insurers

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A life insurer sells long-term policies and invests the premiums for decades.

- **Protection** policies pay on death, illness or medical cost. They earn the insurer a
  wide margin.
- **Savings** policies return money with a guaranteed or shared return, and compete with
  bank deposits. Those with a guaranteed return bring large premiums and a thin margin.
  Those that share the investment result with the policyholder can earn a good one.
- Policies are sold by the insurer's own **agents**, through **banks**, and through
  brokers and online channels.

Profit comes from two places: the margin built into policies, which is earned over their
life, and the gap between what the investments earn and what was promised to
policyholders. Which matters more depends on what the insurer sells. One that sells
mostly protection and shared-return policies lives on the first. One with a large book
of guaranteed-return policies lives or dies on the second.

Households decide demand. Savings policies sell when deposit rates fall. Protection
depends on how many productive agents the insurer has. The regulator often sets the
highest return a policy may promise and the commissions that may be paid, and a cut in
either moves sales forward before it takes effect. Bond yields and share prices decide
the investment result.

Four numbers get confused. **Premiums** are cash collected. **Revenue** under current
accounting leaves out the savings part of each premium. **Value of new business** is the
present value of the profit expected from this year's sales. **Embedded value** is net
assets plus the value of all policies already sold. A year's value of new business is
often worth far more than its effect on that year's profit.

Signs the card does not fit: the company insures property and liability (see the
[P&C insurers card](pc-insurers.md)); it reinsures others; it distributes policies for insurers without
carrying the risk; or it is a group with a bank, an asset manager or a general insurer of
any size, each of which gets its own build.

## 2. The driver tree

Build new sales and the existing book separately, with history beside the forecast. For
an insurer in several countries, build each market on its own in local currency and
translate, since margins, channels and growth differ more by market than by anything
else.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| New sales by channel | Agents: number, the share who are active, policies per active agent and premium per policy. Banks: partner branches and sales per branch. Other channels on their own rows | Growth in new premiums by channel |
| Product mix | The share of protection against savings, and of regular against single premiums. Count a single premium as a tenth of a regular one | New premiums in total |
| New business margin | Value of new business over annualised new premiums, by product or market. It moves with the mix, the promised return and commission rules | The reported margin |
| Value of new business | New sales times the margin | Its reported growth |
| Embedded value | Opening value, plus the expected return on it at the company's own assumed rates, plus value of new business, plus or minus differences in investment results, claims and lapses, plus or minus currency, less dividends and buybacks | Reported value, moved by new business and the expected return |
| Stored margin | The contractual service margin: opening balance, plus new business, plus interest, less the release to profit, plus or minus changes in estimates | The balance as reported |
| Insurance profit | The release of the stored margin, as a share of its opening balance, plus or minus claims and lapse experience, less expenses | Its past ratio to the stored margin |
| Investment result | Invested assets times the return by asset type, less the return owed to policyholders | Assets times the spread between the two, from history |
| Operating profit | Where the company defines one that removes short-term market moves. Show the items between it and net profit | Leave it out |
| Net profit | Insurance profit plus the investment result. It swings with share prices where shares are marked to market through profit | |
| Solvency and dividend | The solvency ratio on the local rules, the cash the book generates after funding new business, and the payout rule, including buybacks and the share count | The ratio and payout as reported |

## 3. The data behind the rows

- **Company.** Some insurers publish premiums every month. Most report twice a year:
  value of new business and its margin, embedded value with a table of what moved it,
  agent numbers and productivity, how many policies are kept after one and two years,
  investment returns and the asset mix, solvency, and sensitivity to assumptions.
- **Industry:**

| Source | What exists |
| --- | --- |
| Regulator and industry body | Industry premiums, monthly in some markets and quarterly with a long delay in others. Decisions on the highest promised return and on commissions. Solvency rules. Sales to visitors from another country, where that is a large source of demand |
| Markets | Long government bond yields and share indices, which set the investment result and, over time, the assumptions |
| Distribution | Agent numbers by insurer. Banks' reports of insurance sold through them |

- **What leads value and profit.** Monthly premiums. Agent numbers. Bond yields and share
  prices. Dates when a promised-return or commission rule changes. Sales in the opening
  weeks of the year.
- **Backtest.** New sales times margin against value of new business. The embedded value
  table: opening value plus each item against closing value.

## 4. Costs and margin

- Commission and the cost of acquiring a policy are paid at the start and earned back
  over its life.
- The margin differs several-fold between protection and savings, so the mix matters more
  than total sales.
- The promised return on old policies is fixed. If investment yields fall below it, the
  insurer loses on every such policy for decades.
- Embedded value and value of new business rest on assumptions, above all the long-run
  investment return. A cut to it lowers both at once.
- With-profits policies pass part of the investment result to policyholders.

## 5. Capacity, capex and working capital

- Solvency rules limit how much can be held in shares and how much can be paid out.
- Liabilities usually last longer than the bonds held against them, so falling yields
  hurt.
- Capital can be raised through bonds that count towards solvency.

## 6. Cycle, policy and traps

- For an insurer with guaranteed-return policies, long-run interest rates are the main
  risk: they narrow the gap between returns and promises, and force assumptions down.
- Share markets swing net profit from year to year.
- Rule changes on promised returns and commissions bring a rush of sales before and a gap
  after.
- Traps:
  - premium growth read as value growth;
  - value of new business compared across years on different assumptions;
  - embedded value taken as fact when it rests on a return assumption;
  - net profit moved by share prices read as operating performance;
  - single premiums counted like regular ones;
  - all agents counted when only some sell;
  - a group's figures used for its life business;
  - growth in the reporting currency against growth at constant exchange rates.

## 7. What investors argue about, and the yardstick

- Whether investment returns will cover what old policies promise.
- Whether new business can grow with fewer agents and tighter rules on bank sales.
- How much of profit is the share market.
- What the dividend is tied to, and whether solvency allows it.

Yardstick: price to embedded value, with a multiple on value of new business as the
check; P/B where embedded value is not published
([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

An insurer has 100,000 agents, of whom 30% sell in a month. Each active agent sells 2
policies a month at a first-year premium of 5,000. New premiums are 3.6bn a year. At a
25% margin, value of new business is 0.9bn.

Embedded value opens at 100. The expected return adds 8 and new business 9. Investment
returns fall short by 3 and the dividend is 4. It closes at 110.

Invested assets of 1,000 earn 4.0%, which is 40. Policyholders are owed 3.2% on 950,
which is 30.4, leaving a spread of 9.6. If the yield falls to 3.5%, the spread is 4.6,
less than half.

All figures are invented. They show the relationships, not a forecast.
