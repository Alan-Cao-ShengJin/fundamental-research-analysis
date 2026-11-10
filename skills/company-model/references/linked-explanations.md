# Keep model explanations connected to their figures

Use for repeated targets, rates, percentages, period labels and rating words inside the human-readable model. Link these components instead of retyping them in explanatory prose. This is not a requirement to turn every source description or assumption rationale into a formula.

The generic [model_text.formula](../scripts/model_text.py) creates Excel formulas with cell references, concatenation and simple numeric `TEXT` formats. They update when a person changes the model in Excel and are reproduced by the supported worksheet interpreter. [model_layout.Sheet.linked_note](../scripts/model_layout.py) places the result in a visible, wrapped cell beside the build, extends its visible width and avoids the legacy comment-only notes column.

```python
sheet.linked_note(12, 'Target {target}; price return {ret}; call {call}.', {
    'target': {'model': 'Value!D7', 'style': 'number', 'decimals': 2},
    'ret': {'model': 'Value!D8', 'style': 'percent', 'decimals': 1},
    'call': {'model': 'Value!D9', 'style': 'text'}
}, column='H')
```

`style: multiple` adds `x`; `grouping: True` adds numeric grouping. Templates accept plain named placeholders, not code, attributes or arbitrary format strings. The `TEXT` subset supports numeric forms such as `0`, `0.00`, `#,##0.0` and `0.0%` with up to six decimals; date/custom financial formats and error-valued concatenation remain unsupported and are rejected. Keep dates/period names in labeled model text cells and link them with `style: text`.

Mark a generated explanation as a text formula and retain the formula in the workbook. Recalculate and run the normal workbook check: a saved text cache that no longer matches its formula is a failure. Missing caches are unfinished recalculation, not a passing preview. The helper does not certify Excel's complete formula language or replace native recalculation/visual review when required.

The surrounding explanation still needs analyst review. “Cash is restricted” can become false even if the cash amount updates correctly. After a material model/evidence change, re-evaluate affected causal explanations, scenario labels, source status and supporting records; regenerate dependent report/brief/decision content. Use existing source, claim and model-review records to retain what changed. Do not preserve an obsolete paragraph merely because its printed numbers are now current.
