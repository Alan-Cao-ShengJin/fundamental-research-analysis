# Fundamental Research Analysis

Instructions and tools that let an AI coding agent do equity research the way a careful analyst would: read the filings, build a financial model, value the stock, have the work challenged, and write it up.

You ask for "an initiation on X". You get three things back:

- an **Excel model** you can open and audit, with every forecast built from business drivers;
- a **full report** (A4 PDF) that explains the business, the forecasts, the valuation and the risks;
- a **one-page brief** with the call: Buy, Hold or Sell, and a 12-month target price.

Version **3.1.0** contains **19 skills**, **11 research flows** and **100 sector cards**, with helper scripts, a sample model and tests.

## How to use it

1. Clone the repository and install it (see [Setup](#setup)).
2. Open the folder in an agent that reads project instructions, such as Claude Code or Codex. [CLAUDE.md](CLAUDE.md) and [AGENTS.md](AGENTS.md) tell the agent where to start.
3. Ask for the research in ordinary words:

| You ask | The agent does |
| --- | --- |
| "Initiation on X" | Starts a new study from the company's own filings and builds the model, report and brief from scratch. |
| "Update view on X" (routine) | Reads the earlier study, checks what has happened since, refreshes the price and the valuation, and changes forecasts only where new evidence calls for it. |
| "Update X after results" | Compares the results with what the model expected, revises the affected forecasts, and refreshes the valuation and the call. |

The skills are instructions the agent follows. They do not run on their own, connect to data services for you, or monitor anything.

## What the agent does, in order

1. **Gathers evidence.** Company filings and announcements first, then the past year's results calls and the covering brokers' notes, then prices, consensus estimates and industry data from the sources you have connected. Broker notes supply facts the company gave out; the agent sets its own assumptions.
2. **Works out what the share price is paying for**: which year's earnings, at what valuation, and where investors disagree.
3. **Checks the company**: who controls it, how reliable its accounts are, how its industry works.
4. **Builds the model.** It picks the [sector card](skills/company-model/references/sectors/index.md) for each business unit and builds revenue and costs from business drivers (volumes, prices, margins). Each driver is set from the best evidence available: a specific supported number first, then the recent trend and its cause, and a plain average only as a last resort. The forecasts flow through the three financial statements.
5. **Values the stock in six steps.** It names the kind of company and the yardstick investors value it on (P/E, P/B, EV/EBITDA, a yield and so on), reads today's price on that yardstick, sets a target level, applies it to its own forecast, builds the bear and bull cases, and gives one target and a rating.
6. **Has the model challenged** by a second agent that starts fresh, with no memory of how it was built.
7. **Writes the report and brief** in a fresh session, working only from the finished analysis.
8. **Has the printed report reviewed** by another fresh reader, who checks the numbers against the model and the sources.
9. **Runs a release check** and packages the three files.

The full sequence is in [company-sequence.md](skills/research-cycle/references/company-sequence.md); the entry point is [research-cycle](skills/research-cycle/SKILL.md).

## The house rules, in brief

These are defaults. Tell the agent if your mandate differs.

- **Rating.** Buy if the target is more than 10% above the price, Sell if more than 10% below, Hold in between. The rating looks at price return only.
- **Target price.** A target level of the yardstick investors use for that kind of company, times today's forward figure: earnings for a P/E, book value for a P/B, and so on. The stock's own historical average is the default; going above it needs a clear reason.
- **Dividend payers.** A steady, high-payout company is valued on the dividend yield that comparable income stocks offer, not on a P/E.
- **Dividends and total return.** Dividend yield is shown separately. Price return plus yield is shown as total return only where the dividend is a real part of what the holder earns.
- **Forecasts.** Built independently of consensus. The agent then compares with consensus and explains every material difference; a large gap it cannot explain is treated as a warning.
- **Base case.** The numbers the analysis believes in most, not a deliberately cautious set. Caution belongs in the bear case.
- **Bear and bull cases.** Each is the main debate resolved the other way, with the rest of the base case kept, so the range is narrow enough to act on. A likelihood is given only where a record supports it.
- **Cost of equity.** When one is needed, it is the 10-year government yield plus the premium the market's own index implies on the research date, recomputed for every study.
- **Debates.** The report prints only the questions investors are really arguing about: what the bears say, what the bulls say, our view, and what the share is worth if each side is right. Where there is no real debate, none is invented.
- **Writing.** Sharp, concise and plain. Every fact has a source; anything not known is said to be not known.

The rules live in the [decision contract](skills/investment-conclusion/references/decision-contract.md), the [yardstick list](skills/valuation-thesis/references/yardsticks.md), [dividend valuation](skills/valuation-thesis/references/valuation-driver-and-dividends.md), [discount-rate selection](skills/valuation-thesis/references/discount-rate-selection.md) and the [writing standard](skills/research-brief/references/natural-writing.md).

## What is checked, and what is not

The scripts check things that can be checked mechanically: the workbook recalculates to the model, the rating follows from the target, the brief's figures match the model, dates are consistent, the brief fits one page, and a review was actually completed before anything is packaged ([publication workflow](skills/report-layout/references/publication-review.md)).

They cannot check judgment. A passing run does not prove that the sources are right, that the forecasts are sensible or that the call will make money. Treat the output as a well-organised analyst draft and read it critically.

## What's inside

| Purpose | Skills |
| --- | --- |
| Entry and routing | [Research cycle](skills/research-cycle/SKILL.md), [stock initiation](skills/stock-initiation/SKILL.md), [model revision](skills/model-revision/SKILL.md) |
| Evidence and the business | [Evidence intake](skills/evidence-intake/SKILL.md), [industry analysis](skills/industry-analysis/SKILL.md), [company model](skills/company-model/SKILL.md), [issuer questions](skills/issuer-questions/SKILL.md) |
| Risk and challenge | [Corporate governance](skills/corporate-governance/SKILL.md), [financial quality](skills/financial-quality/SKILL.md), [research challenge](skills/research-challenge/SKILL.md), [investment conviction](skills/investment-conviction/SKILL.md) |
| Valuation and the call | [Valuation thesis](skills/valuation-thesis/SKILL.md), [investment conclusion](skills/investment-conclusion/SKILL.md) |
| Context and follow-up | [Theme screening](skills/theme-screening/SKILL.md), [macro event analysis](skills/macro-event-analysis/SKILL.md), [company change tracking](skills/company-change-tracking/SKILL.md), which also keeps the follow-up plan |
| Writing and layout | [Research brief](skills/research-brief/SKILL.md), [chart visualization](skills/chart-visualization/SKILL.md), [full-report layout](skills/report-layout/SKILL.md) |

There are also [sector cards](skills/company-model/references/sectors/index.md) for 100 kinds of company, a [model standard](skills/company-model/references/model-standard.md) with a sample workbook, and a [skill index](skills/README.md). Keep the whole `skills/` folder together: the files refer to each other.

## Setup

You need Node.js 24.13 or later and Python 3.11 or later.

```text
npm ci
python -m pip install -r requirements.txt
npm run skills:check
npm test
python -B -m unittest discover -s skills/tests -p "test_*.py"
```

- **Printing reports** needs Chrome (set `CHROME_PATH` if it is not found) and `python -m pip install -r skills/report-layout/requirements.txt`.
- **Recalculating the Excel model** needs Microsoft Excel.
- **Data services** are optional and you bring your own access. Put credentials in `.env.research-data`, which Git ignores; [.env.example](.env.example) lists the names. See the [provider guide](skills/evidence-intake/references/research-data-providers.md).
- On Windows PowerShell, use `npm.cmd` if the execution policy blocks `npm`.

## Latest update: version 3.1.0

- **Broker notes.** Before modelling, the agent reads the past year's results calls and the covering brokers' notes in full. It takes the company facts they record and sets every assumption itself, because brokers lean optimistic ([evidence intake](skills/evidence-intake/SKILL.md)).
- **Bear and bull cases.** Each case moves only the drivers of the main debate and is priced at the base multiple unless its own outcome changes what investors pay. Other uncertain assumptions go in the sensitivity table. The sample model is rebuilt this way ([valuation sequence](skills/valuation-thesis/SKILL.md#value-the-company-in-six-steps)).
- **Loss-making units.** A unit that loses money or is being exited gets its own revenue and profit rows ([model standard](skills/company-model/references/model-standard.md)).
- **Running a study.** The agent works in batches and prefers a slower run to one that uses tokens faster. [CLAUDE.md](CLAUDE.md) names the model and effort for each reviewer and writer in Claude Code.
- **Standing instructions.** When you correct how the research is done, the agent writes the correction into the skills, so another computer behaves the same way ([skill calibration](skills/research-cycle/references/skill-calibration.md)).

Version 3.0.0 brought the six-step valuation, the order for setting revenue drivers, the 100 sector cards and debates written as what bears and bulls say.

Earlier changes, verification results and limits are in [AUDIT.md](AUDIT.md); upgrade notes are in [MIGRATION.md](MIGRATION.md).

## Scope and limits

This repository covers research on a single company. Portfolio construction, risk budgeting, cross-asset strategy, trading and live monitoring are [out of scope](skills/research-cycle/references/scope-boundary.md). It contains no research on real companies, no private models, no licensed data and no credentials; the sample workbook is invented.

Nothing here is investment advice, and research output does not authorise trading or outreach. Third-party material is credited in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The files in this release are listed in [bundle-manifest.json](bundle-manifest.json).
