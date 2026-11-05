# Company model standard

This is the minimum for any new company model and the target for any full update. Build the smallest useful forecastable pieces, show where every number comes from, and link everything live. A one-sheet annual operating plan is a scaffold, not a company model.

Build it with [model_workbook.py](../scripts/model_workbook.py): one cell specification produces the Excel workbook and the agent model, [recalc_excel.ps1](../scripts/recalc_excel.ps1) recalculates it in Excel, and `check` confirms Excel and the specification agree. Lay it out for a reader, not the builder, under [Presentation](#presentation): a Cover and Summary up front, a short source tag beside every assumption and its reasoning in a cell comment.

## Sample model

The [sample model](../assets/company-model-example.xlsx) is a complete model of a fictitious manufacturer, built from the [specification](../assets/company-model-example.json) that [model_example.py](../scripts/model_example.py) writes. It has every tab and feature below: five annual columns of history (the first an opening year) with three forecast years, quarters from 1Q25 to 4Q27, the full schedules, a case selector, guidance tests, segment unit economics, a live target table, sensitivities and a ten-year valuation band with a chosen cut-off. Copy its structure, row patterns and linking; replace every number, label and note with the company's own evidence. All its figures are invented.

In the sample, history follows these conventions:

- Reported figures are blue.
- Estimated quarterly splits are blue on light yellow, like assumptions. The fourth quarter is the annual report less nine months.
- Each driver's history is the ratio the reported figures imply.

A real model takes history from filings rather than generating it.

## Periods

- Annual: at least four reported years plus three forecast years.
- Quarterly: every reported quarter for at least the last two years, the remaining quarters of the current year and the quarters of the next year. Use half-years where only halves are reported. Derive single quarters from cumulative reports (Q2 = H1 − Q1, Q3 = 9M − H1, Q4 = FY − 9M) and check them against the reported single-quarter table ([actuals](actuals.md)).
- The current year is reported year-to-date plus forecast remaining quarters, never a fresh full-year guess.
- Label every column's regime in a header row: reported, sum of quarters, quarterly forecast or annual forecast.

## Tabs

In this order, named in plain words:

**Cover.** Company, tickers, model and price dates, the case selector, the colour legend, a linked index of sheets with one line each, and the master check status.

**Summary.** One landscape screen, every number linked: the valuation box (price, target, price return, dividend yield, bear/base/bull, consensus target), key financials for the last actual and three forecast years, valuation metrics with today's forward P/E against the band, the reasons for the call, and two small charts (revenue by segment, the valuation band).

**Valuation**, **Valuation Band** and **Scenarios** follow (described below), then **Revenue Build**, **Statements**, **Data**, any input-price tab, **Guidance**, **Questions** and **Checks**.

**Statements.** Annual and quarterly columns side by side.

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

**Revenue Build.**

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

**Valuation.**

- Why we invest, in a few numbered points, each a driver the target depends on ([research challenge](../../research-challenge/SKILL.md)).
- The target price table, linked live to model EPS and DPS and the current price: target multiple, target, upside, dividend yield, and current P/E on two fiscal years.
- Consensus comparison: profit, EPS and target.
- One sensitivity table: thesis risk, shock size (an input), EPS change, EPS change % and target change, sorted by impact; inputs the shocks need sit in their own block above it.
- Peers: P/E for two years, EPS growth, P/E per growth point and market value, each average labelled with its sample.
- Scenario outcomes recalculated on every build, with the build date and a check that the active case matches the live model.
- A summary of the valuation band.

**Valuation Band.**

- A monthly history of month-end price over the consensus forward EPS that was current at each month-end.
- The mean, standard deviation and ±1 and ±2 SD lines.
- Today's P/E on consensus EPS and on our EPS, each with its position in SD.
- The prices implied at the mean and ±1 SD on both earnings bases.
- A chart that draws the mean and SD lines only inside the chosen window, shows excluded history in grey, and scales the axis to the window rather than past peaks.
- Use P/B bands for cyclicals and yield bands for dividend payers in the same way ([own historical valuation](../../valuation-thesis/references/method-selection.md#the-companys-own-historical-forward-valuation)).

**Scenarios.** The bear/base/bull drivers with their own header row (driver, unit, bear, base, bull, active, rationale); nothing above them labels columns as years.

**Checks.** Every check row in one list (balance sheet, cash flow against balance-sheet cash, retained earnings roll-forward, reported profit and cash, segments against revenue, gross-profit build, scenario snapshot) and one master flag shown on every sheet.

**As the business needs.** Ownership and structure, capacity, a unit-economics tab, and separate tabs for large segments or regions.

## Features the other skills rely on

- One bear/base/bull selector that drives every case, with each case's driver values shown side by side.
- Key metric rows: our forward P/E, P/B, dividend yield and next-year ROIC.
- Consensus comparison rows next to our forecasts.
- Decision rows: rating, target multiple, target, price return, dividend yield and total return.
- Dividend schedule where distributions matter.
- Sensitivities for the assumptions that move EPS most, a two-way grid of the two largest, and the value of the main driver that today's price implies at the target multiple.
- Excel and the agent model kept in sync and recalculated in Excel. Hard numbers appear only as inputs in their own labelled cells, never inside formulas, apart from 0, 1 and period counts. A base ratio adjusted by a case is two rows: the base input, then the formula that adds the case.
- Text that quotes a model number links to it (a model value column) instead of retyping it.

## Presentation

The workbook is read by people who did not build it. [model_workbook.py](../scripts/model_workbook.py) applies most of this from the specification; see [workbook-profile.md](workbook-profile.md#house-theme-and-reporting-detail) for the details.

- Tabs in the order above, coloured by type (outputs navy, calculations grey, inputs and data light blue). The Cover links to every sheet and every other sheet links back to the Cover from row 1. Gridlines off; calculation sheets open at 85% zoom, output sheets at 100%.
- Header on every sheet: row 1 company, ticker and sheet; row 2 active case, units and price date; row 3 the master check status. Header text never wraps. The colour legend appears once, on the Cover, with an example cell for each style.
- Colour: hardcoded history blue; assumptions and scenario levers blue on light yellow; formulas black; links to other sheets green; memo ratios dark grey italic; key outputs (rating, target, return, EPS) bold black, never grey. Where rules overlap: key output, then input, then link, then ratio, then formula.
- One number format per unit (RMB m to one decimal, per-share to two decimals, % to one decimal, multiples with "x", days whole, FX to four decimals, dates as real dates in d mmm yyyy). Negatives always in parentheses. One currency label throughout.
- Columns: spacer, label, units (centred), a short source tag ("AR25", "3Q26 call", "Est."), then the periods, with a narrow spacer between annual and quarterly blocks. Sub-items are indented, not padded with spaces. Longer commentary goes in a cell comment on the row label. Data rows are 15 high with no wrapping; text-heavy tables (Guidance, Questions, scenario rationale) wrap, top-aligned. No text is clipped and no #N/A shows.
- Forecast columns have shaded headers with a rule at the boundary. Quarterly columns and each schedule's detail rows are grouped so they collapse, leaving the section header and total visible.
- Inputs never sit under period headers they do not belong to; a non-time-series block gets its own header row.
- Summary fits one landscape page: valuation box (rating, price, target, price return, dividend yield, total return, then bear/base/bull), key financials, valuation metrics and why the call on the left; two charts on the right. Chart data sits below the printed area, grouped.
- Charts use the house palette, a takeaway title in sentence case, the legend at the bottom, hatched bars or dashed lines for forecasts, and a note for data the axis clips. Each sits inside its sheet's print area without covering a table.
- Defined names only for key outputs and the case selector; the specification holds every cell binding.
- Every sheet prints A4 landscape, one page wide, centred, with title rows (and on time-series sheets the label columns) repeated and the file, sheet and page number in the footer. Page breaks fall between sections, not inside a table. Cover, Summary, Scenarios, Checks, Guidance and Questions each fit one page.
- Notes cite sources a reader can follow, never pipeline paths.

## Sector depth

Read the sector card for every activity the company runs. Build each mechanism in its operating build and evidence sections as rows, or note in the model why it does not apply.
