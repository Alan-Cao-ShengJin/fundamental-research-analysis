---
name: pip-chart-visualization
description: Build consistent, data-linked charts and business diagrams using AntV G2 and AntV Infographic with a shared professional theme. Use for research-report visuals, chart selection, rendering and export; preserve model values and reporting bases.
metadata:
  version: 1.0.0
---

# Consistent charts and diagrams

Use AntV as the default chart-building approach for research reports. This skill adapts [AntV Chart Visualization Skills](https://github.com/antvis/chart-visualization-skills), with financial-report conventions and a reusable house theme. It supports the communication stage; it does not replace analysis, valuation or the decision contract.

Explicit user templates or style requirements override the default theme while preserving data integrity and consistent visual meaning.

Read [the AntV workflow](references/antv-workflow.md) when building a visual. Load [the shared theme](assets/chart-theme.json) for every report, and apply it to all figures in that report. The report structure and reading budget remain in [visual report design](../pip-research-brief/references/visual-reports.md).

## Build from the question and data

Identify what the reader should learn, then choose the simplest supported view:

| Question | Default visual |
| --- | --- |
| How has a metric changed? | G2 line or columns, with actual/forecast separation |
| How do values compare? | G2 horizontal bars or points on a common scale |
| What creates the target or cash movement? | Reconciled waterfall or contribution bridge |
| What is the scenario risk? | Reference-price line and bear/base/bull points, with signed returns |
| Which assumptions matter most? | Sorted sensitivity bars; heatmap for two interacting assumptions |
| How does the business make money? | AntV Infographic relationship/process diagram |
| What forms a whole? | Stacked bars; a simple donut only for a few positive, exhaustive parts |

Do not use a pie for negative cash flows, a radar for financial quality, a word cloud for a thesis, or a Sankey whose apparent flow sizes have no quantitative basis. A compact table is useful when exact peer dates, definitions and numbers matter more than a chart.

Consume the current model outputs or dated observations directly. Preserve numeric precision in the data; round labels separately. Retain the dataset, field mapping, source/period/unit basis, chart spec and renderer version alongside the report when producing charts. Keep internal run identifiers out of investor-facing figures.

## Apply one visual language

Use the shared theme's font, colours, spacing and mark styles. Keep a metric's colour and legend order consistent across figures. Colours distinguish series or meaning; avoid a different colour for every bar in a single-series comparison.

Actual values are solid. Forecasts use dashed lines, lighter fills or another labelled pattern without changing what the series colour means. Mark the forecast boundary. Bear/base/bull and Buy/Hold/Sell use the named semantic colours in the theme, plus readable labels. A price reference is a neutral line, not another forecast.

Label the period, unit, currency and basis once where easy to see. Add a short takeaway and a readable source note. Keep chart titles and captions within the report's writing budget. Preserve the inclusive +/-10% Hold rule and the separation between price returns and dividends.

## Render and verify

Use local AntV rendering for report files, with exact dependency versions retained when used. Export a static figure or inline SVG for print and offline reading; interactive views may supplement it. Essential numbers and qualifications must remain visible without hover or JavaScript.

Check data-to-figure totals, scenario/bridge arithmetic, axis ranges, actual/forecast styles, labels, sources and colour consistency. Inspect the rendered desktop/mobile/export result. Keep the static artifact and its spec together so later updates regenerate figures from the revised model. If the preferred runtime is unavailable, preserve the same data specification/theme in a deterministic SVG fallback and record that implementation choice in supporting metadata.
