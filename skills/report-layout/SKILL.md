---
name: report-layout
description: Lay out and print a full stock report (initiation or full update) in the house style, so every company's report looks the same and reads like a research report rather than a printed web page. Use when producing the full visual pitch as an A4 PDF; the one-page brief keeps its own template in research-brief.
metadata:
  version: 2.0.0
---

# Full report layout

Content follows [visual pitch design](../research-brief/references/visual-reports.md) and the [writing standard](../research-brief/references/natural-writing.md); this skill fixes how the report looks. Build every report with [report_layout.py](scripts/report_layout.py). It carries the page grid, fonts (IBM Plex Sans with tabular figures, embedded from [assets/fonts](assets/fonts), SIL Open Font License), running header and footer, exhibit numbering, tables, source markers, back matter and charts, with colours from the shared [chart theme](../chart-visualization/assets/chart-theme.json). Do not write company-specific CSS or copy layout code from an earlier study; extend the module instead. In the study's builder, write every figure in text, tables and charts from the calculated model and saved source data rather than typing it, and rebuild the report and brief after any model change so no stale figure survives.

## Page 1 is the front page

A portfolio manager who reads only page 1 should get the call, the thesis, the key data and the price action.

- Byline: company, ticker, report type and date. Add an author, contact or firm only when the user supplies one.
- Headline: the thesis in plain words, per the [brief guide](../research-brief/references/one-page-brief.md).
- Main column: **Key points**, three or four bullets of at most 25 words (the business and its driver, the valuation and target logic, where we differ from consensus and why, what would change the view with the entry level), then a summary of at most two short paragraphs, then a 12-month indexed price chart against the local index or a peer basket, with the dated events that moved the stock marked.
- Sidebar: rating box (rating, price and date, 12-month target, price return computed from the displayed target, dividend yield shown separately, consensus target, bear / base / bull); key data (ticker and exchange, 52-week range, market value, enterprise value, net cash or debt, shares outstanding with dilution, free float, average daily trading value, next catalyst with its date or "not confirmed"); key financials for the last actual and three forecast years (revenue, EPS, P/E, FCF yield or dividend yield).

## Later pages

- A 40mm left rail carries each section's heading and a one-line takeaway; text runs in the main column at 60-75 characters a line; exhibits and wide tables span the full width.
- Running header (company, ticker, report, date; firm if given), footer "Internal use only" and "Page N of M", all from the page margins, not the body.
- Every chart, diagram and table is an exhibit: "Exhibit N: [the point, not the topic]" above, "Source: ..." below, and the text refers to it as (Exhibit N). Use `{{ex:key}}` in text; numbering follows placement.
- An exhibit sits in the section whose argument it supports, on the page of its first citation or the next.
- Every claim from an external source carries a superscript number (`{{src:key}}`) matching the source list.
- Do not say the same thing in prose and in a table; keep one.

## Exhibits and tables

- Charts: round axis ticks, units at the top left of the axis, a legend entry for every series and state (actual, forecast, estimated history), no label overlaps (moved labels get leader lines), nothing drawn outside the plot, values on bars where they carry the point. Actuals solid; forecasts grey, lighter or dashed; estimated history dotted. One meaning per colour (the theme's `meaning`).
- Scenarios: a football field (bear, base, bull bars from the current price) with a table of the assumptions behind each case in the same format, base case included.
- Sensitivities: a tornado of the resulting target price, plus a two-way grid when the two largest risks move together.
- Financial tables: rows grouped under bold labels (volume, P&L, per share, cash flow, valuation); explicit row names; actual columns marked A and estimate columns E and shaded; consensus rows grey italic; negatives in parentheses; percentages and multiples to one decimal; currency as US$1,234m and -US$27; n/a, not blank. A peer table states each average's sample and shows the reference row that sets the target and the company at the target.

## Back matter

Numbered sources (publisher, title as a link, date; no raw URLs; primary documents rather than press summaries of them), the author only when the user supplies one, rating definitions from the [decision contract](../investment-conclusion/references/decision-contract.md), the pricing and consensus timestamps, and "Internal use only. Not investment advice." No pipeline notes such as model tab lists or chart-rendering remarks.

## Print and look

HTML generation uses the Python standard library. PDF printing needs Chrome (set `CHROME_PATH` if it is not found). Page inspection and page-image rendering need the optional dependencies in [requirements.txt](requirements.txt). These host capabilities are separate from installing the skill.

Print with `print_pdf` (headless Chrome), then use `inspect_pdf` to write page images and look at every page before release. Fix and re-render when a page ends on a heading, an exhibit splits, a page other than the last is more than about 15% blank, labels overlap or clip, an exhibit lacks its number, headline or source, an exhibit is not cited, or the same figure appears with two values (target and return, current P/E, peer averages, unit prices). Recompute displayed returns from the displayed target and price.
