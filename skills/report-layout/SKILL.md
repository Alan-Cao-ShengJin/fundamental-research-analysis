---
name: report-layout
description: Lay out and print a full stock report (initiation or full update) in the house style, so every company's report looks the same and reads like a research report rather than a printed web page. Use when producing the full visual pitch as an A4 PDF; the one-page brief keeps its own template in research-brief.
metadata:
  version: 2.10.0
---

# Full report layout

Content follows [visual pitch design](../research-brief/references/visual-reports.md) and the [writing standard](../research-brief/references/natural-writing.md); this skill fixes how the report looks. Build every report with [report_layout.py](scripts/report_layout.py). Its interface is the module docstring and the `package` docstring; read those two, not the source. It carries the page grid, fonts (IBM Plex Sans with tabular figures, embedded from [assets/fonts](assets/fonts), SIL Open Font License), running header and footer, exhibit numbering, tables, source markers, back matter and charts, with colours from the shared [chart theme](../chart-visualization/assets/chart-theme.json). Do not write company-specific CSS or copy layout code from an earlier study; extend the module instead. In the study's builder, write every figure in text, tables and charts from the calculated model and saved source data rather than typing it, and rebuild the report and brief after any model change so no stale figure survives.

Each `section(..., covers=(...))` names the investor questions it answers (`QUESTIONS` in the module, taken from the visual pitch guide); the build stops if a question is neither covered nor dropped with `omit(question, reason)`.

## Arguments, debates and business units

Write each substantive point as `Argument(point, evidence)`: the point in plain words, then the reason and the two or three figures behind it, citing its source (`{{src:key}}`) or exhibit (`{{ex:key}}`). It renders as one paragraph, kept to the [limits](../research-brief/references/natural-writing.md#limits). The optional `inference` and `implication` add what it means and what it does to earnings, cash, risk or the multiple. Use them only where the reader would not see that unprompted, so paragraphs do not all end the same way.

Write each debate as `Debate(question, live, bears, bulls, view, worth, settles)`: the question in the words investors use; why it is live (what raised it, where we saw investors argue it, and what today's price assumes); what the bears say and what the bulls say, each side's two or three best points with the evidence cited; our view, with the evidence that decides it and what the other side gets right; what the share price is worth if each side is right, quoting the bear and bull scenario prices and not a second set; and the observation, its date and the level that would change our mind.

A debate is a question investors visibly disagree on: cite the call questions, broker split or price reaction that shows it. A sensitive assumption nobody disputes belongs in the forecast section. Rank debates by the gap between the bull and bear price and print the ones that are real. One is fine. Where investors are not clearly arguing about anything that matters, do not squeeze one out: drop the section with `omit('debate', reason)`. A switched [yardstick](../valuation-thesis/references/yardsticks.md#when-the-yardstick-switches) is always one; when most of the return is a change in multiple, the debate is what investors need to see to pay more, not which number we chose. Put the debates in one section straight after the business description, give each a line with our side on the front page, and let later sections refer back to them. An update opens that section with what has moved on each debate since the last report.

Declare the business units the report must analyse with `segments([...])`, every unit above about 15% of segment profit or one a debate turns on; each needs an Argument tagged `segment=` that cites the exhibit showing its driver build (stores and sales per store, units and price, or channel and growth, with history).

The build stops when a section that covers a question holds no Argument or Debate, when a section covering the debate holds no Debate, when a plain paragraph carries a judgement ("we forecast", "we assume", "we expect", "we think", "we believe", "our view", "our reading", "we side") outside an Argument, or when a declared business unit has no argument. Plain paragraphs remain for context and definitions.

In a full initiation, put the business drivers and their earnings/cash consequences before detailed valuation pages; the compact front-page call and valuation summary remain appropriate. Review the [displayed trigger contract](references/decision-record.md#numerical-trigger-meaning) and [economic applicability versus completed verification](references/publication-review.md#review-packet-and-financial-assertions) on every applicable study.

These are structure and reference checks. Claim statuses are analyst judgments, and a cited exhibit may not support the inference attached to it. Before release, apply the [inference review](../research-challenge/references/inference-quality.md) to the actual arguments; passing the build does not mark them supported.

## Page 1 is the front page

A portfolio manager who reads only page 1 should get the call, the thesis, the key data and the price action.

- Byline: company, ticker, report type and date. Add an author, contact or firm only when the user supplies one.
- Headline: the thesis in plain words, per the [brief guide](../research-brief/references/one-page-brief.md).
- Main column: **Key points**, three or four bullets of at most 25 words (the call and its economic rationale, stating an expectations gap and its size where the analysis establishes one; the valuation and target logic, any comparable consensus difference and why, what would change the view), then a summary of at most two short paragraphs, then a 12-month indexed price chart against the local index or a peer basket, with the dated events that moved the stock marked. Do not invent a variant view or unique market belief to fill a bullet.
- Sidebar: rating box (rating, price and date, 12-month target, price return computed from the displayed target, dividend yield shown separately, consensus target and bear / base / bull, in the [decision contract's](../investment-conclusion/references/decision-contract.md#return-hurdle-and-calls) words); key data (ticker and exchange, 52-week range, market value, enterprise value, net cash or debt, shares outstanding with dilution, free float, average daily trading value, next catalyst with its date or "not confirmed"); key financials for the last actual and three forecast years (revenue, EPS, P/E, FCF yield or dividend yield).

Use sector-appropriate key data and financial rows. Industrial EV/net-debt/FCF metrics are not mandatory for banks or insurers; use meaningful capital, return and distribution measures, and label unavailable or inapplicable comparisons without manufacturing them.

## Later pages

- A 40mm left rail carries each section's heading and a one-line takeaway; text runs in the main column at 60-75 characters a line; exhibits and wide tables span the full width.
- Running header (company, ticker, report, date; firm if given), footer "Internal use only" and "Page N of M", all from the page margins, not the body.
- Every chart, diagram and table is an exhibit: "Exhibit N: [the point, not the topic]" above, "Source: ..." below, and the text refers to it as (Exhibit N). Use `{{ex:key}}` in text; numbering follows placement.
- An exhibit sits in the section whose argument it supports, on the page of its first citation or the next.
- Every claim from an external source carries a superscript number (`{{src:key}}`) matching the source list.
- The self-contained summary-statement appendix need not be cited from an investment argument; its model/source basis still appears below the table.
- Do not say the same thing in prose and in a table; keep one.

## Exhibits and tables

- Charts: round axis ticks, units at the top left of the axis, a legend entry for every series and state (actual, forecast, estimated history), no label overlaps (moved labels get leader lines), nothing drawn outside the plot, values on bars where they carry the point. Actuals solid; forecasts grey, lighter or dashed; estimated history dotted. One meaning per colour (the theme's `meaning`).
- Scenarios: a football field (bear, base, bull bars from the current price) with a table of the assumptions behind each case in the same format, base case included.
- Sensitivities: a tornado of the resulting target price that includes the valuation input the method rests on (the target multiple, required yield, asset discount or equivalent). Size each shock from history or guidance and name the basis in the exhibit's source line. Add a two-way grid when material risks move together, using the selected method's operating/value driver against its valuation input and marking the current price. Isolated shocks do not replace the coherent adverse scenario.
- Financial tables: rows grouped under bold labels (volume, P&L, per share, cash flow, valuation); explicit row names; actual columns marked A and estimate columns E and shaded; consensus rows grey italic; negatives in parentheses; percentages and multiples to one decimal; currency as US$1,234m and -US$27; n/a, not blank. A peer table states each average's sample and shows the reference row that sets the target and the company at the target.

Full initiations include model-linked income, balance-sheet and cash-flow summaries through `Report.financial_summary(...)`, with sector-appropriate rows, available history and forecasts. Label unavailable periods rather than inventing them. Long tables can split with repeated headers and intact rows; charts remain intact. A small earnings bridge may work better as a table. Any deliberately truncated waterfall axis must be explicitly labeled; a broken axis is not a default requirement.

## Back matter

Numbered sources (publisher, title as a link, date; no raw URLs; primary documents rather than press summaries of them), the author only when the user supplies one, rating definitions from the [decision contract](../investment-conclusion/references/decision-contract.md), the pricing and consensus timestamps, and "Internal use only. Not investment advice." No pipeline notes such as model tab lists or chart-rendering remarks. Write the workbook, report and brief into `deliverables/` and list the model and brief in `r.companions` and the brief's `links` by bare file name; they print as file names, not links.

## Print and look

Publish through the [publication workflow](references/publication-review.md): it owns rule pinning, the model review before writing, draft printing, the fresh reader's review, corrections and finalization. The early model review's frozen model and evidence accompany the writing packet automatically. A refused operation does not rewrite reviewed files. All distributed companions are frozen; the brief's visible content must reproduce its current payload, and its published structured scenario/yield fields need model bindings.

HTML generation uses the Python standard library. PDF printing needs Chrome (set `CHROME_PATH` if it is not found); the release check and page inspection need the packages in [requirements.txt](requirements.txt). These host capabilities are separate from installing the skill.

Use `inspect_pdf` to render and look at every page. Fix page-end headings, label collisions/clipping, type that is not readable at the actual printed width and conflicting figures. About 15% blank space is an inspection prompt, not an automatic failure or an excuse to shrink type; intact charts or rows may justify a gap. Keep a debate in one normal-flow wrapper so its answer cannot overlap a repeated table header.
