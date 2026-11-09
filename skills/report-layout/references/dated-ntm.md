# Dated current-NTM bridges

Use within the existing P/E release record when NTM is the chosen economic convention. The target date does not move the earnings window forward. A fiscal-year target, P/B, dividend yield or SOTP retains its appropriate existing method; this feature does not require every company to use NTM.

## Choose the supported forecast profile

`ntm.mode: annual-interpolation` uses the existing whole-month fiscal-year weights; omitting mode retains that historical approximation. Label annual interpolation and test material seasonal/run-rate effects. It remains valid when finer forecasts are unsupported or annual smoothing is better justified. The checker does not infer when it is economically preferable.

`ntm.mode: dated-periods` takes explicit components using ISO `start` and exclusive `end` dates. Components can be quarters, halves or irregular fiscal periods and must cover the selected NTM window without gaps, overlaps or irrelevant periods. Every component declares its `period`, matching model `header` and earnings/share bindings. An optional `weight` must equal the computed overlap divided by that component's duration. These fractions need not sum to one: a full half contributes all of its half-year earnings, not half of them.

Use `allocation: uniform-days` and a substantive `rationale`. The script computes overlapping days and fractions; it does not establish actual within-period seasonality. A selected supported non-uniform profile should first be modeled into smaller dated components; do not disguise a handpicked haircut as time weighting. Actual fiscal dates support 52/53-week calendars without assuming every year ends on a month-end.

## Shares and calculation

- `metric: eps-sum`: each component binds `eps`, `shares` and `header`. Comparable weighted-average shares must be constant across components. NTM EPS is the sum of component EPS times its overlap fraction.
- `metric: profit-over-shares`: each component binds attributable `profit`, weighted-average `shares` and a matching earnings `header`. NTM profit is the sum of prorated period profits; NTM shares are weighted by overlap days divided by window days. Divide profit by those shares. Profit and shares must use compatible scales. Stock options, convertibles, buybacks, changing rights or within-period issuance can require a more detailed share schedule; uniform shares within a component remain an approximation.

The release gate reads calculated workbook values and checks period headers, numerical coverage and the bridge to `bindings.forwardEps`. Generate the Excel formula from the same period schedule so a human can inspect and change it. The clean [field example](../assets/dated-ntm.example.json) is fictional and contains no company forecasts. `dated_ntm.py` can also be imported by a builder to calculate auditable fractions. Its calculator validates component arithmetic; `release_check.py` additionally validates the current twelve-month anchor, target and decision.

## Review

Choose the method on evidence and forecast economics. Show a credible alternative when it materially changes the target or crosses a rating threshold; do not select the preferred rating and work backwards. Use the same convention in headline, scenarios, sensitivities and comparable benchmarks. Historical point-in-time NTM denominators may use a different vendor approximation: disclose and assess that difference rather than asserting exact equivalence without the vendor's construction data.

Input dates, source extraction, earnings definitions, units, corporate actions and intra-period forecasting still need substantive review. Passing this calculator is not proof that those assumptions are true.
