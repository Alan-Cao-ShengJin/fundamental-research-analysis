# AntV implementation workflow

Adapted from [AntV Chart Visualization Skills](https://github.com/antvis/chart-visualization-skills/tree/a105fa12a9fa41fccccc2eba7f4b34973628f5d3/skills), Copyright (c) 2025 AntV Visualization Team, [MIT licensed](https://github.com/antvis/chart-visualization-skills/blob/a105fa12a9fa41fccccc2eba7f4b34973628f5d3/LICENSE). Use the selected upstream library guidance with the house theme and financial-data rules in this skill. The upstream default palette and decorative templates do not override the report style.

## Select the implementation

- **G2 v5:** statistical charts, financial histories/forecasts, valuation bridges and sensitivities. Use local browser rendering and retain the complete declarative spec.
- **AntV Infographic:** concise business relationships, operating processes and timelines. Match a documented template to the information structure. Prefer simple relationship or sequence templates over ornamental cards or 3D layouts.
- **G6:** consider only for an actual complex network or hierarchy. Read its current primary guidance when needed; a small business-model diagram does not require a graph editor.

Check the project's available packages before adding a dependency. When a library is used, retain its exact version and any local bundle needed to reproduce the figure. Verify current APIs against the relevant official library documentation when implementing unfamiliar features. Do not rely on a moving `latest` CDN URL for a final report.

Local G2 rendering is the normal report path. The upstream chart-image HTTP API is an optional hosted-image route, not a required service or a replacement for the shared theme. Do not make offline reports depend on an expiring returned URL.

## Prepare a chart specification

Start with the data meaning and units. Record the chart ID, reader question, dataset source, columns/encodings, series order, actual/forecast field, labels, scale/domain, theme version, caption and output paths. This is supporting metadata, not a new research handoff schema.

Use numeric values for calculations and separate display formatting. Keep dates in sortable form and categories in an intentional order. Distinguish missing from zero. Preserve signed cash flows and negative earnings. For a price/valuation plot, retain the share class, FX purpose, target date and earnings basis.

For a waterfall, derive start/end positions from signed contributions and reconcile the last value to the selected total. For scenario points, use a common scale and a separate current-price reference. For financial trends, use the disclosed cadence and mark where forecast begins. Reuse metric colours across panels rather than letting each chart assign them independently.

## G2 v5 conventions

Use an explicit container, a complete `chart.options({...})` initial specification, and `await chart.render()`. Use `type: 'view'` with `children` for multiple overlaid marks. Repeatedly changing the root mark type does not create an overlay.

Use `encode` as an object, `transform` as an array and `labels` in the plural. Transpose through a coordinate transform. Use actual G2 mark names: for example `interval`, `line`, `point`, `lineY` and `rangeY`; do not copy mark names from another chart library. Do not mix v4 chained APIs into v5 examples or assume `d3` is exposed.

Load [the theme tokens](../assets/chart-theme.json) and map them into valid G2 settings. `g2BaseTheme` selects the base preset; the other fields are house design tokens. Set mark styles explicitly. Use a fixed fill for a single-series bar chart. For multiple series, map a semantic category field to an explicit palette/domain; do not encode hexadecimal strings as category data. Use a scalar or documented automatic padding value, not an array copied from another API.

Use a labelled forecast segment with dashed line or lighter fill. Handle dense labels by reducing or repositioning them while retaining the important values in a visible caption/table. In investor reports, a tooltip cannot be the only place to find a decision-relevant number.

## Infographic conventions

Use the documented `infographic <template-name>` syntax and two-space indentation for nested `data` and `theme` blocks. Select the template's required data structure: lists, sequences, relationships or a hierarchy. Avoid mixing payload fields from unrelated template families. Set the house font and semantic palette explicitly.

Represent only supported relationships and dated events. Arrow width or node size must not imply invented amounts. Use the library's documented export to produce a stable SVG/image after rendering and font loading. Its syntax-only response convention applies to the configuration payload; the requested report still contains the chart, sources and concise explanation.

## Final output checks

Inspect chart errors and the rendered figure, not merely whether a file exists. Compare visible values with the current model/observations and ensure fonts, axes, labels, legends and source notes survive desktop, mobile and print/export. Re-render after visible changes. Save a static artifact with accessible description and a compact data table when exact reading or fallback requires one.
