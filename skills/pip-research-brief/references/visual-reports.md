# Short, visual investment reports

Full research depth belongs in the model, evidence and analysis records. The investor report should make the decision easy to inspect. Use these defaults unless the user requests a different format or depth.

Build charts and diagrams with [pip-chart-visualization](../../pip-chart-visualization/SKILL.md), adapted from AntV. It supplies the shared palette, typography, actual/forecast styling, library workflow and export conventions. Use that common theme across companies and figures; this guide determines what the report needs to explain.

## Length and hierarchy

- **Decision brief:** about 250-350 words, normally one readable page. Lead with the call and one thesis sentence, then reference price/time, primary target/date, price return and bear/bull risks. Explain the business/moat, decisive evidence and principal invalidation concisely.
- **Main report:** about 800-1,200 words of narrative plus selected visuals and compact tables. Treat this as a reading budget, not a requirement to fill space. Do not hide another essay in captions or table cells.
- **Supporting material:** link the detailed model, assumptions, sources, governance ledger and sensitivity records. Put necessary lengthy reconciliations or methods in a clearly labelled optional appendix. Include material uncertainties and governance consequences in the main report.

Choose detail by its effect on the decision. Extend the default only when the extra explanation helps the reader judge a material issue. Deep research does not automatically require a long paper. Avoid shrinking type to meet a page count.

## Choose visuals that answer the investment questions

Use roughly three to five useful visuals in the main report, selecting or combining the following according to the business. A simple fact or short comparison may need only a sentence or table. Avoid a fixed chart quota and decorative illustrations.

| Reader's question | Suitable view | Essential meaning |
| --- | --- | --- |
| What is the call and risk? | Reference-price line with bear/base/bull markers, or a compact scenario table | Exact security, common target horizon/currency, signed price returns; distributions shown separately |
| How does it make money? | Small customer-to-company money-flow diagram with costs and reinvestment | Who pays, what the company retains, and how cash reaches owners; distinguish franchise/customer assets and group revenue |
| What drives the forecast? | Driver bridge or small revenue/profit/cash charts | The assumptions that matter; actual versus forecast clearly marked; show cash conversion separately from earnings |
| Why this target? | Earnings/rerating waterfall, cash/NAV bridge or comparable valuation table | Primary method, earnings versus multiple contribution, persistent discount, and peer/history horizon limits |
| What would make it wrong? | Compact risk/governance table, sensitivity chart or catalyst timeline | Mechanism, affected assumption/value and observable trigger; no invented scores, probabilities or confirmed dates |

The brief usually needs just the decision/scenario strip and, if useful, one small bridge. Do not pack the full report into a miniature dashboard.

Give each visual a short takeaway supported by its data. Follow it with only the explanation needed to judge the claim. A table filled with long paragraphs does not replace prose. Preserve the central business, moat, governance and counter-case explanations even when a chart is used.

## Data and chart integrity

Generate numbers from the current model or dated evidence; no manually retyped parallel estimates. Label currency, scale, period, share/earnings basis and source. Distinguish actuals, estimates, management guidance and analyst forecasts. Preserve each peer's data vintage and estimate horizon.

Use a common axis for comparable scenarios and zero-based axes for magnitude bars. If an axis is cropped for a valid reason, make that explicit. Avoid dual axes that suggest a false relationship, 3D effects and pie charts for quantities that do not form a whole. Waterfalls must reconcile to the selected target after disclosed rounding. A scenario range is not a probability interval or loss limit.

Do not invent an operating series, quarterly observation or past forward multiple to fill a chart. Explain the gap briefly and use a supported view. Do not remove a material risk because it is awkward to visualise.

## Readability and verification

Use the chart skill's shared theme, readable business typography and aligned numbers. Colour must support labels and symbols rather than carry meaning alone. Keep panels compact, with no oversized hero, unnecessary empty space or repeated metric cards. Use AntV G2 for financial charts and AntV Infographic for suitable business/process diagrams, with stable SVG/images for self-contained reports. Add interaction when it materially helps assess an assumption.

Check desktop, mobile and print/export layouts as applicable. Keep chart labels and sources legible, prevent clipping, and let tables scroll within their container on small screens. Material figures must remain visible without hover or JavaScript. Keep sources near claims, with a short source list and links to the full register. Verify visual values against the model and inspect the rendered result. Re-render after layout or visible-content changes.
