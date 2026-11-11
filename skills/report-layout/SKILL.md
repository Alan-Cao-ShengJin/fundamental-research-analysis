---
name: report-layout
description: Lay out and print a full stock report (initiation or full update) in the house style, so every company's report looks the same and reads like a research report rather than a printed web page. Use when producing the full visual pitch as an A4 PDF; the one-page brief keeps its own template in research-brief.
metadata:
  version: 2.9.5
---

# Full report layout

Content follows [visual pitch design](../research-brief/references/visual-reports.md) and the [writing standard](../research-brief/references/natural-writing.md); this skill fixes how the report looks. Build every report with [report_layout.py](scripts/report_layout.py). Its interface is the module docstring and the `package` docstring; read those two, not the source. It carries the page grid, fonts (IBM Plex Sans with tabular figures, embedded from [assets/fonts](assets/fonts), SIL Open Font License), running header and footer, exhibit numbering, tables, source markers, back matter and charts, with colours from the shared [chart theme](../chart-visualization/assets/chart-theme.json). Do not write company-specific CSS or copy layout code from an earlier study; extend the module instead. In the study's builder, write every figure in text, tables and charts from the calculated model and saved source data rather than typing it, and rebuild the report and brief after any model change so no stale figure survives.

Each `section(..., covers=(...))` names the investor questions it answers (`QUESTIONS` in the module, taken from the visual pitch guide); the build stops if a question is neither covered nor dropped with `omit(question, reason)`.

## Arguments, debates and business units

The report is built from arguments, not paragraphs. Write each substantive point as `Argument(point, evidence, inference, implication)`: the point in plain words; the two or three figures or the reason behind it, citing its source (`{{src:key}}`) or exhibit (`{{ex:key}}`); what it means; and what follows for earnings, cash, risk or the multiple. It renders as one paragraph without labels. Write each contested question as `Debate(question, claims, answer, moves, settles)`: the claims each side rests on, each with the evidence that tests it and its status (supported, contradicted or untested; contradicted needs incompatible evidence on the same proposition and period, while absence of an announcement alone leaves a future action untested); our answer; the number it moves (a forecast, margin or multiple, quantified); and the observation and date that would settle it. Choose the debates by how much each moves the target; when most of the return is a change in multiple, one debate is why the multiple moves. Bull and bear appear once, as the priced scenarios. Declare the business units the report must analyse with `segments([...])`, every unit above about 15% of segment profit or one a debate turns on; each needs an Argument tagged `segment=` that cites the exhibit showing its driver build (stores and sales per store, units and price, or channel and growth, with history).

The build stops when a section that covers a question holds no Argument or Debate, when a section covering the debate holds no Debate, when a plain paragraph carries a judgement ("we forecast", "we assume", "we expect", "we think", "we believe", "our view", "our reading", "we side") outside an Argument, or when a declared business unit has no argument. Plain paragraphs remain for context and definitions.

In a full initiation, put the business drivers and their earnings/cash consequences before detailed valuation pages; the compact front-page call and valuation summary remain appropriate. Review the [displayed trigger contract](references/decision-record.md#numerical-trigger-meaning) and [economic applicability versus completed verification](references/publication-review.md#review-packet-and-financial-assertions) on every applicable study.

These are structure and reference checks. Claim statuses are analyst judgments, and a cited exhibit may not support the inference attached to it. Before release, apply the [inference review](../research-challenge/references/inference-quality.md) to the actual arguments; passing the build does not mark them supported.

Give each developed argument one main home. The front page and standalone brief summarize it; elsewhere refer back briefly. An implication can concern earnings, cash or risk without repeating the rating or target. Quantify a debate's effect with its answer rather than repeating its valuation argument in every section.

## Page 1 is the front page

A portfolio manager who reads only page 1 should get the call, the thesis, the key data and the price action.

- Byline: company, ticker, report type and date. Add an author, contact or firm only when the user supplies one.
- Headline: the thesis in plain words, per the [brief guide](../research-brief/references/one-page-brief.md).
- Main column: **Key points**, three or four bullets of at most 25 words (the call and its economic rationale, stating an expectations gap and its size where the analysis establishes one; the valuation and target logic, any comparable consensus difference and why, what would change the view), then a summary of at most two short paragraphs, then a 12-month indexed price chart against the local index or a peer basket, with the dated events that moved the stock marked. Do not invent a variant view or unique market belief to fill a bullet. The rating and the new-money judgment are separate: the key points and summary do not tell the reader to wait for a lower price.
- Sidebar: rating box (rating, price and date, 12-month target, price return computed from the displayed target, dividend yield shown separately, consensus target, bear / base / bull, and the new-money judgment with, when it is no, the decent and attractive entry prices, in the [decision contract's](../investment-conclusion/references/decision-contract.md#return-hurdle-and-calls) words); key data (ticker and exchange, 52-week range, market value, enterprise value, net cash or debt, shares outstanding with dilution, free float, average daily trading value, next catalyst with its date or "not confirmed"); key financials for the last actual and three forecast years (revenue, EPS, P/E, FCF yield or dividend yield).

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

Pin production rules at study creation and use the [implemented lifecycle](references/publication-review.md) for early model review, version-aware execution, staged printing and bounded presentation confirmation. The early review must cover the exact spec/workbook published; its frozen model and evidence accompany the writing packet automatically. A refused operation does not rewrite reviewed files. All distributed companions are frozen; the brief's visible content must reproduce its current payload, and its published structured scenario/yield fields need model bindings.

Before freezing a draft, synchronize the [decision record](references/decision-record.md) from the current calculated model, including bound trigger text. Current packages require this checkpoint and freeze it automatically. Render material prose calculations and source ranges with `bound_measure` and matching [claim display bindings](references/claim-support.md#feasible-bridges-and-actual-displayed-figures); the declared raw value alone does not validate a printed sign or range. Rebuild dependent writing after any correction, preserving the actual review budget and freshness requirements.

HTML generation uses the Python standard library. PDF printing needs Chrome (set `CHROME_PATH` if it is not found). Printing needs Chrome; the release check and page inspection need the packages in [requirements.txt](requirements.txt). These host capabilities are separate from installing the skill.

Use the [bounded publication workflow](references/publication-review.md). `package(study, zip, report_html, brief_html, [workbook], ...)` first prints drafts, checks integrity and prepares a **partial** review; it stops with `awaiting-review` and no ZIP. A named fresh reader must actually review the PDFs, model and evidence, record findings in the existing challenge handoff and assess applicable financial assertions. The host launches that context; a packet does not perform the work. Use `inspect_pdf` to render and look at every page.

Pass the routed `researchMode` (`initiation`, `regular-review`, `earnings-update` or `catalyst-update`) to the package adapter. Before the reader starts, run `publication_review.py begin STUDY --reviewer NAME`. Draft versions and review attempts are separate: re-rendering an unreviewed packet preserves the prospective attempt number; a started, interrupted or failed review consumes one. Complete the definition-aware comparison, incremental-flow and brief-fidelity coverage in the wrapper. The [claim guide](references/claim-support.md) explains valid reconciliations and data limitations; these controls do not prescribe a forecast or rating.

Correct material findings within the recorded review budget and refresh the draft/review after changes. Finalization checks the completed review, current file hashes and the study's pinned production-rule identity, applicable cash-coverage, normalized-ratio and financing bindings, plus existing model, decision, period, freshness and wording checks. It packages the **exact reviewed PDFs** without reprinting. Failure leaves no ZIP. An unresolved review remains a draft; do not manufacture a pass. Recheck with `release_check.py <study>`.

Fix page-end headings, label collisions/clipping and conflicting figures. About 15% blank space is an inspection prompt; intact charts or rows may justify a gap. Tables may split correctly with repeated headers. The checks verify declared definitions and arithmetic, completion and provenance; they do not certify source truth, reviewer independence, unbound prose or sound judgment. Historical integrity-only checks use the explicitly labeled `--legacy` mode, not a publication bypass.
