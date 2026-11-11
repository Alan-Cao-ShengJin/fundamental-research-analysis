# Company model standard

This is the minimum for any new company model and the target for any full update. Build the smallest useful forecastable pieces, show where every number comes from, and link everything live. A one-sheet annual operating plan is a scaffold, not a company model.

Apply this standard by economic activity. The detailed rows below describe the synthetic industrial example; they are not a compulsory chart of accounts. Banks and insurers need their lending, claims, funding and regulatory-capital schedules; asset holdings and finite-life businesses need their relevant asset, ownership and realization builds. Preserve linked statements, an auditable operating/value build, financing and scenarios, while replacing inapplicable gross-margin, working-capital or ROIC rows. Use a meaningful valuation history where available; an unavailable or economically invalid P/E band is a documented limitation, not invented data. Historical depth and quarterly/half-year detail follow available comparable disclosure.

Build it with [model_workbook.py](../scripts/model_workbook.py): one cell specification produces the Excel workbook and the agent model, [recalc_excel.ps1](../scripts/recalc_excel.ps1) recalculates it in Excel, and `check` confirms Excel and the specification agree. Lay it out for a reader, not the builder, under [Presentation](#presentation): a Cover and Summary up front, short source tags and pivotal assumption reasoning beside the calculation, with longer source detail in comments when useful.

The original integrated example's price-return-plus-annual-yield row is a memo illustration, never the rating input or a forecast of distributions actually received in the target window. New work labels any such row explicitly as a secondary memo and uses eligible dated cash receipts for an investor-payoff forecast.

## Sample model

The [sample model](../assets/company-model-example.xlsx) is a complete model of a fictitious manufacturer, built from the [specification](../assets/company-model-example.json) that [model_example.py](../scripts/model_example.py) writes. It has every tab and feature below: five annual columns of history (the first an opening year) with three forecast years, quarters from 1Q25 to 4Q27, the full schedules, a case selector, guidance tests, segment unit economics, a live target table, sensitivities and a ten-year valuation band with a chosen cut-off. Copy its structure, row patterns and linking; replace every number, label and note with the company's own evidence, including its currency, price date and period labels, which come from the research date and the issuer's fiscal calendar. All its figures and dates are invented.

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
- Where a disclosed driver is predictive and comparable, run the forecast through it: stores × sales per store, units × price, channel × growth. A material segment (about 15% of profit, or less when it drives the debate or risk) needs supported assumptions rather than an unexplained growth rate. Apply the [driver measurement tests](revenue-projection.md#test-what-a-driver-actually-measures); counts sitting beside an unrelated growth forecast do not establish a build, and back-solving a ratio adds no evidence. If reliable decomposition is unavailable or unsuitable, justify the coarser forecast and its sensitivity instead of inventing units.
- Carry history beside the forecast, quarterly where disclosed.
- Give gross margin and gross profit for each segment, and reconcile revenue, cost of sales and gross profit to the group.
- For the businesses that drive profit, build unit economics: price, cost and profit per unit, and a segment P&L with its share of group profit.
- An earnings stream that drives the debate or out-year EPS gets its own [adoption-to-EPS bridge](revenue-projection.md#emerging-earnings-streams), even while it is small.
- Test guidance targets, multi-period outlooks, capacity plans, backlog and purchase commitments, incentive hurdles and the quarter the forecast implies, as their own rows: the dated statement, the model value in the matching period, the gap and the constraint that binds. A forecast below an incentive hurdle needs a stated reason ([corporate governance](../../corporate-governance/SKILL.md)).

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
- The target price table, linked live to model EPS and DPS and the current price: target multiple, target, upside, dividend yield on the same forward year as the target EPS, and current P/E on two fiscal years.
- Consensus comparison: profit, EPS and target.
- One sensitivity table: thesis risk, shock size, EPS change, EPS change % and target change, sorted by impact. Each shock moves named model inputs and is recalculated through the whole model when it is built, declared under `sensitivities` in the specification, so tax, each unit's minority share, financing and the target EPS's share basis act as they do in the forecast; `model_workbook.py check` fails a row that does not reproduce. One tax rate × one group minority share ÷ one share count is a shortcut, not a sensitivity.
- Peers: P/E for two years, EPS growth, P/E per growth point and market value, each average labelled with its sample, the closest same-market peers doing the same business first.
- Scenario outcomes recalculated on every build, with the build date and a check that the active case matches the live model.
- A summary of the valuation band.

**Valuation Band.**

- A monthly history of month-end price over the consensus forward EPS that was current at each month-end.
- The mean, standard deviation and ±1 and ±2 SD lines.
- Today's P/E on consensus EPS and on our EPS, each with its position in SD.
- The prices implied at the mean and ±1 SD on both earnings bases.
- A chart that draws the mean and SD lines only inside the chosen window, shows excluded history in grey, and scales the axis to the window rather than past peaks.
- Window alternatives: each defensible start (a dated event or a conventional lookback) with its mean, observations, target and rating, the chosen window first.
- Where a trailing band helps, put it beside the forward band with its own label, on reported EPS from the filings at their announcement dates.
- For a dividend-led case, show relevant comparable yield investments (yield, payout, risk, market access and tax treatment), the stock's own absolute-yield band where available, and a dated bond-spread comparison when useful. State which evidence calibrates the required yield; where no comparable yield investments exist, the own yield band does. See [comparable yields](../../valuation-thesis/references/valuation-driver-and-dividends.md#comparable-yields-own-band-and-bonds). Use business-appropriate P/B or yield comparisons ([own historical valuation](../../valuation-thesis/references/method-selection.md#the-companys-own-historical-forward-valuation)).

**Scenarios.** The bear/base/bull drivers have their own header row (driver, unit, bear, base, bull, active, rationale); nothing above them labels columns as years. Cover uncertain assumptions material to earnings, dividends, cash flow, funding, dilution, asset value or the target. Give each assumption one authoritative input location; the scenario selector must reach its dependent calculations. The scenario overview may link to a detailed local assumption block, or the local build may link to the overview's active value. Keep that value and pivotal rationale visible beside the calculations either way, without duplicate editable inputs. Explain material assumptions held constant across cases; not every input must change. Test representative changes through the full model and use economically coherent joint cases rather than stacking unrelated extremes.

**Checks.** Every check row in one list (balance sheet, cash flow against balance-sheet cash, retained earnings roll-forward, reported profit and cash, segments against revenue, gross-profit build, scenario snapshot) and one master flag shown on every sheet.

**As the business needs.** Ownership and structure, capacity, a unit-economics tab, and separate tabs for large segments or regions.

## Features the other skills rely on

- One bear/base/bull selector that drives every case, with each case's driver values shown side by side.
- Key metric rows: our forward P/E, P/B, dividend yield and next-year ROIC.
- Where the investors, the valuation convention or the comparison set work in calendar years, calendar-year rows built from the quarters by their end dates with time-weighted shares ([calendarize.py](../scripts/calendarize.py)); fiscal rows stay the reporting basis.
- Consensus comparison rows next to our forecasts.
- Decision rows: rating, target multiple, target and price return; show dividend yield separately. A combined-return illustration is a secondary memo, on matched price/cash horizons with receipt eligibility, and never the rating hurdle.
- Dividend schedule where distributions matter.
- Sensitivities for the assumptions that move EPS most, a two-way grid of the two largest, and the value of the main driver that today's price implies at the target multiple.
- Excel and the agent model kept in sync and recalculated in Excel. Hard numbers appear only as inputs in their own labelled cells, never inside formulas, apart from 0, 1 and period counts. A base ratio adjusted by a case is two rows: the base input, then the formula that adds the case.
- Text that quotes a model number links to it (a model value column) instead of retyping it.

## Presentation

The workbook is read by people who did not build it. [model_workbook.py](../scripts/model_workbook.py) applies most of this from the specification; see [workbook-profile.md](workbook-profile.md#house-theme-and-reporting-detail) for the details.

- Tabs in the order above, coloured by type (outputs navy, calculations grey, inputs and data light blue). The Cover links to every sheet and every other sheet links back to the Cover from row 1. Gridlines off; calculation sheets open at 85% zoom, output sheets at 100%.
- Header on every sheet: row 1 company, ticker and sheet; row 2 active case, units and price date; row 3 the master check status. Header text never wraps. The colour legend appears once, on the Cover, with an example cell for each style.
- Colour: hardcoded history blue; assumptions and scenario levers blue on light yellow; formulas black; links to other sheets green; memo ratios dark grey italic; key outputs (rating, target, return, EPS) bold black, never grey. Where rules overlap: key output, then input, then link, then ratio, then formula.
- One number format per unit (reporting currency in millions to one decimal, per-share to two decimals, % to one decimal, multiples with "x", days whole, FX to four decimals, dates as real dates in d mmm yyyy). Negatives always in parentheses. One currency label throughout.
- Columns: spacer, label, units (centred), a short source tag ("AR25", "3Q26 call", "Est."), then the periods, with a narrow spacer between annual and quarterly blocks. Sub-items are indented, not padded with spaces. Place pivotal rationale in a visible explanation column beside the build; use row-label comments for longer supporting source detail. Data rows are normally 15 high; rows with visible explanations wrap and expand to fit. Text-heavy tables (Guidance, Questions, scenario rationale) wrap, top-aligned. No text is clipped and no #N/A shows.
- Forecast columns have shaded headers with a rule at the boundary. Quarterly columns and each schedule's detail rows are grouped so they collapse, leaving the section header and total visible.
- Inputs never sit under period headers they do not belong to; a non-time-series block gets its own header row.
- Summary fits one landscape page: valuation box (rating, price, target, price return, separate dividend yield, then bear/base/bull; any combined-return memo is secondary), key financials, valuation metrics and why the call on the left; two charts on the right. Chart data sits below the printed area, grouped.
- Charts use the house palette, a takeaway title in sentence case, the legend at the bottom, hatched bars or dashed lines for forecasts, and a note for data the axis clips. Each sits inside its sheet's print area without covering a table.
- Defined names only for key outputs and the case selector; the specification holds every cell binding.
- Every sheet prints A4 landscape, one page wide, centred, with title rows (and on time-series sheets the label columns) repeated and the file, sheet and page number in the footer. Page breaks fall between sections, not inside a table. Cover, Summary, Scenarios, Checks, Guidance and Questions each fit one page.
- Notes cite sources a reader can follow, never pipeline paths.

## Sector depth

Read the sector cards for activities material to earnings, assets, funding or the investment debate. Build the applicable mechanisms into the operating/value build and evidence sections. Do not require a separate model for immaterial activities or every KPI named by a card.
