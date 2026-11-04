# Company model standard

This is the minimum for any new company model and the target for any full update. Build the smallest useful forecastable pieces, show where every number comes from, and link everything live. A one-sheet annual operating plan is a scaffold, not a company model.

Build it with [model_workbook.py](../scripts/model_workbook.py): one cell specification produces the Excel workbook and the agent model, [recalc_excel.ps1](../scripts/recalc_excel.ps1) recalculates it in Excel, and `check` confirms Excel and the specification agree. Use the [house theme](workbook-profile.md#house-theme-and-reporting-detail) and put each assumption's source and reasoning in the notes column beside it.

## Sample model

The [sample model](../assets/company-model-example.xlsx) is a complete model of a fictitious manufacturer, built from the [specification](../assets/company-model-example.json) that [model_example.py](../scripts/model_example.py) writes. It has every tab and feature below: five annual columns of history (the first an opening year) with three forecast years, quarters from 1Q25 to 4Q27, the full schedules, a case selector, guidance tests, segment unit economics, a live target table, sensitivities and a ten-year valuation band with a chosen cut-off. Copy its structure, row patterns and linking; replace every number, label and note with the company's own evidence. All its figures are invented.

In the sample, history follows these conventions:

- Reported figures are dark blue.
- Estimated quarterly splits are purple. The fourth quarter is the annual report less nine months.
- Each driver's history is the ratio the reported figures imply.

A real model takes history from filings rather than generating it.

## Periods

- Annual: at least four reported years plus three forecast years.
- Quarterly: every reported quarter for at least the last two years, the remaining quarters of the current year and the quarters of the next year. Use half-years where only halves are reported. Derive single quarters from cumulative reports (Q2 = H1 − Q1, Q3 = 9M − H1, Q4 = FY − 9M) and check them against the reported single-quarter table ([actuals](actuals.md)).
- The current year is reported year-to-date plus forecast remaining quarters, never a fresh full-year guess.
- Label every column actual or estimate.

## Tabs

**3S (statements).** Annual and quarterly columns side by side.

- Income statement: every reported line, each with growth or % of revenue beneath it. Include gross profit and margin, each tax and expense line, finance income and cost, other income, impairments, non-operating items, EBITDA, depreciation and amortisation by type, pre-tax profit, tax and effective rate, minority interests, profit to shareholders, diluted shares and EPS.
- Dividends: interim and final DPS, total dividend, payout ratio and dividend yield. Then market value and P/E at the current price, with a peer P/E table beside it.
- Cash flow: operating cash flow from profit, D&A by type, each working-capital line (inventory, receivables, payables, other) and other adjustments. Investing: capex on PPE and intangibles, disposals, investments, and dividends from associates. Financing: borrowing, equity raised, dividends to shareholders and minorities, buybacks, other. Then the cash roll-forward with FX.
- Balance sheet: every reported line, totals, a check row that is zero in every column, and leverage.
- Schedules beneath, driving the statements:
  - Working-capital days or % of revenue for each item.
  - A fixed-asset roll-forward: opening gross cost, capex, transfers, disposals and closing cost; accumulated depreciation with a depreciation rate; impairment; book value.
  - Construction in progress.
  - Right-of-use assets and leases.
  - Intangibles and amortisation.
  - Net finance income: yield on opening cash, cost of debt on debt, and FX.
  - Share count, buybacks and employee plans.
  - Tax, minority share and named one-off items.

**Revenue projection.**

- Break revenue into segment → product → region, down to the smallest unit that can be forecast. Use the driver the business actually runs on, taken from the [sector card](sectors/index.md): volume × price, market size × share, capacity × utilisation, customers × spend, or contract backlog × conversion.
- Carry history beside the forecast, quarterly where disclosed.
- Give gross margin and gross profit for each segment, and reconcile revenue, cost of sales and gross profit to the group.
- For the businesses that drive profit, build unit economics: price, cost and profit per unit, and a segment P&L with its share of group profit.
- Test guidance targets, incentive hurdles and the quarter the forecast implies, as their own rows.

**Data.** Monthly or quarterly operating data in one clean table:

- company volumes by product and region;
- industry totals;
- peers;
- exports;
- prices;
- the industry series behind the [industry analysis](../../industry-analysis/SKILL.md): upstream input prices and downstream customer or channel indicators.

Assumption notes for market growth, share, price, unit cost and margin cite the industry finding they rest on.

Identities must hold: months sum to quarters, and domestic plus export equals the total. Reconcile annual sums to the annual report. Add an input-price tab when commodity or input costs drive margins.

**Guidance.** Dated, numbered management guidance grouped by topic, each item with its source (call, filing or meeting) and checked for transcription errors.

**Questions.** Questions for management. Each one shows the current model assumption it tests and how each possible answer would change that assumption.

**Investment thesis.**

- Why we invest, in a few numbered points.
- The target price table, linked live to model EPS and DPS and the current price: target multiple, target, upside, dividend yield, and current P/E on two fiscal years.
- Consensus comparison: profit, EPS and target.
- Thesis breakers, each quantified as its effect on EPS or the target.
- A summary of the valuation band.

**Valuation band.**

- A monthly history of month-end price over the consensus forward EPS that was current at each month-end.
- The mean, standard deviation and ±1 and ±2 SD lines.
- Today's P/E on consensus EPS and on our EPS, each with its position in SD.
- The prices implied at the mean and ±1 SD on both earnings bases.
- A chart.
- Use P/B bands for cyclicals and yield bands for dividend payers in the same way ([own historical valuation](../../valuation-thesis/references/method-selection.md#the-companys-own-historical-forward-valuation)).

**As the business needs.** Ownership and structure, capacity, a unit-economics tab, and separate tabs for large segments or regions.

## Features the other skills rely on

- One bear/base/bull selector that drives every case, with each case's driver values shown side by side.
- Key metric rows: our forward P/E, P/B, dividend yield and next-year ROIC.
- Consensus comparison rows next to our forecasts.
- Decision rows: target multiple, target, price return and re-rating upside.
- Dividend schedule where distributions matter.
- Sensitivities for the assumptions that move EPS most, a two-way grid of the two largest, and the value of the main driver that today's price implies at the target multiple.
- Excel and the agent model kept in sync and recalculated in Excel. Hard numbers appear only as inputs, never inside formulas, apart from documented constants such as days in a period.

## Sector depth

Read the sector card for every activity the company runs. Build each mechanism in its operating build and evidence sections as rows, or note in the model why it does not apply.
