# Clear, visual stock pitches

The reader is deciding whether to own a stock at the stated price. Present an investment argument that can be understood, tested and challenged. The research workflow determines how evidence is gathered; it is not the pitch's table of contents. Keep the main investment reasoning in the pitch and technical reproduction in supporting records.

Build charts and diagrams with [chart-visualization](../../chart-visualization/SKILL.md), adapted from AntV. It supplies the shared palette, typography, actual/forecast styling, library workflow and export conventions. Use that common theme across companies and figures; this guide determines what the report needs to explain.

## Length and hierarchy

- **Decision brief:** the gist of the stock pitch, normally one readable page and about 250-400 words. Lead with the call and one thesis sentence, then price/target/earnings year/return, the few reasons to believe it and the main way it fails. Give rounded headline figures with a compact valuation explanation and scenario strip. It must stand on its own.
- **Full visual pitch:** a developed investment case, often around 1,800-3,000 words plus selected figures and compact tables. Cover the company from enough angles for an investor to assess the argument. Length follows material questions, not a quota. Do not replace depth with unexplained labels, dense dashboards or a second brief.
- **Supporting material:** complete statements, account reconciliations, detailed assumptions and source locations. The appendix enables inspection and reproduction; it cannot contain the only explanation of a headline valuation, the investment argument or a decisive risk.

Choose detail by its effect on the decision. Extend the default only when the extra explanation helps the reader judge a material issue. Deep research does not automatically require a long paper. Avoid shrinking type to meet a page count.

## Choose visuals that answer the investment questions

Develop the argument across the material angles below. Use as many visuals as the case needs, often six to ten useful figures/tables in a developed pitch. A simple fact may need only a sentence. Avoid fixed quotas and decorative illustrations.

| Reader's question | Suitable view | Essential meaning |
| --- | --- | --- |
| What is the call and risk? | Reference-price line with bear/base/bull markers, or a compact scenario table | Exact security, common target horizon/currency, signed price returns; distributions shown separately |
| How does it make money? | Small customer-to-company money-flow diagram with costs and reinvestment | Who pays, what the company retains, and how cash reaches owners; distinguish franchise/customer assets and group revenue |
| What drives the forecast? | Driver bridge or small revenue/profit/cash charts | The assumptions that matter; actual versus forecast clearly marked; show cash conversion separately from earnings |
| Why this target? | Earnings/rerating waterfall, cash/NAV bridge or comparable valuation table | Primary method, earnings versus multiple contribution, persistent discount, and peer/history horizon limits |
| What would make it wrong? | Compact risk/governance table, sensitivity chart or catalyst timeline | Mechanism, affected assumption/value and observable trigger; no invented scores, probabilities or confirmed dates |

Also explain competitive response and moat durability, the latest performance versus the next outlook, management delivery, evidence behind the important forecast assumptions, cash conversion and funded growth, minority access to value, peers and dated own-history valuation, market context and credible catalysts. Combine sections and choose emphasis by materiality; these are investor questions, not mandatory equal-sized chapters.

The brief usually needs just the decision/scenario strip and, if useful, one small bridge. Do not pack the full report into a miniature dashboard.

Give each visual a short takeaway supported by its data. Follow it with only the explanation needed to judge the claim. A table filled with long paragraphs does not replace prose. Preserve the central business, moat, governance and counter-case explanations even when a chart is used.

## Write for someone outside the model

Build each section from claim to evidence to explanation to investment consequence. Define unfamiliar terms before using them. Explain a number's denominator, period and meaning when they affect the conclusion. Growth rates and account movements alone do not make an argument.

Put the central conviction in the thesis sentence. When governance is the concern, explain whether the price compensates for it and why, rather than using a long string of conditions as the headline. Put qualifications and the strongest counter-case into the supporting argument. Do not assert attractive risk/reward simply to match suggested wording; the recalculated case must support it.

Introduce each valuation claim before explaining its calculation. Use natural rounding, such as "about 5x FY2027 earnings", in the thesis or valuation paragraph when it matters; do not force it into the headline. Under a simple heading such as Valuation, show the profit, shares, EPS, FX and price calculation. Use net profit attributable to shareholders, not parent profit. Adjusted accounting profit is not cash after investment.

If a higher P/E drives the target, explain why investors would pay it using the [rerating test](../../valuation-thesis/references/method-selection.md#rerating-and-derating). "Confidence may recover" needs a reason and observable evidence. Then explain the alternative directly: "If investors keep paying today's P/E..." followed by the price and return. The brief must retain the decisive reason for any assumed rerating; the full pitch develops its evidence and counter-case.

When dividends drive the valuation, use the [dividend guide](../../valuation-thesis/references/valuation-driver-and-dividends.md): put DPS, annual yield, payout ratio and funded coverage in the brief, with higher-payout and cash-stress detail in the full pitch. Show the price at alternative required yields. Explain whether a higher price comes from a higher sustainable dividend or investors accepting less yield; do not disguise the latter as unexplained peer-P/E convergence. Keep annual yield and horizon cash receipts distinct.

Apply the [return hurdle and calls](../../investment-conclusion/references/decision-contract.md#return-hurdle-and-calls) separately: a +20% case is Buy by rating, but unattractive under the 50% attractiveness hurdle. State both clearly. Keep the supported target and show an entry price meeting the hurdle if useful; do not inflate valuations or rely on the bull case to make the opportunity look attractive.

Apply the [valuation calendar](../../valuation-thesis/references/valuation-calendar.md). A twelve-month target does not itself allow another forward-year roll. Later-year forecasts can inform durability and cash-flow valuation without becoming the headline P/E denominator.

## Data and chart integrity

Generate numbers from the current model or dated evidence; no manually retyped parallel estimates. Label currency, scale, period, share/earnings basis and source. Distinguish actuals, estimates, management guidance and analyst forecasts. Preserve each peer's data vintage and estimate horizon.

Use a common axis for comparable scenarios and zero-based axes for magnitude bars. If an axis is cropped for a valid reason, make that explicit. Avoid dual axes that suggest a false relationship, 3D effects and pie charts for quantities that do not form a whole. Waterfalls must reconcile to the selected target after disclosed rounding. A scenario range is not a probability interval or loss limit.

Do not invent an operating series, quarterly observation or past forward multiple to fill a chart. Explain the gap briefly and use a supported view. Do not remove a material risk because it is awkward to visualise.

## Readability and verification

Use the chart skill's shared theme, readable business typography and aligned numbers. Colour must support labels and symbols rather than carry meaning alone. Keep panels compact, with no oversized hero, unnecessary empty space or repeated metric cards. Use AntV G2 for financial charts and AntV Infographic for suitable business/process diagrams, with stable SVG/images for self-contained reports. Add interaction when it materially helps assess an assumption.

Check desktop, mobile and print/export layouts as applicable. Keep chart labels and sources legible, prevent clipping, and let tables scroll within their container on small screens. Material figures must remain visible without hover or JavaScript. Keep sources near claims, with a short source list and links to the full register. Verify visual values against the model and inspect the rendered result. Re-render after layout or visible-content changes.

Read the opening as a prospective investor: can the reader explain what the business does, why this stock is attractive or unattractive, where its headline valuation comes from, how owners earn a return and what could go wrong? If this requires the model or source log, rewrite the passage. Reapply the call and Hold band after any financial correction; a polished pitch cannot preserve stale numbers.
