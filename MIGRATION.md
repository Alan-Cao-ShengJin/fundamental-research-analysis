# Version 2.0 name migration

All maintained skills use generic names. Update copied skill directories, explicit invocation names, import paths and relative links together. Keep the complete sibling tree. Old names below are historical identifiers, not compatibility folders or current invocations.

| Previous name | Current name |
| --- | --- |
| `pip-research-cycle` | `research-cycle` |
| `pip-evidence-intake` | `evidence-intake` |
| `pip-company-model` | `company-model` |
| `pip-financial-quality` | `financial-quality` |
| `pip-corporate-governance` | `corporate-governance` |
| `pip-valuation-thesis` | `valuation-thesis` |
| `pip-investment-conclusion` | `investment-conclusion` |
| `pip-research-challenge` | `research-challenge` |
| `pip-management-questions` | `management-questions` |
| `pip-research-brief` | `research-brief` |
| `pip-chart-visualization` | `chart-visualization` |
| `pip-monitor-review` | `monitor-review` |
| `pip-theme-screening` | `theme-screening` |
| `pip-company-change-tracking` | `company-change-tracking` |
| `pip-macro-event-analysis` | `macro-event-analysis` |
| `pip-stock-initiation` | `stock-initiation` |
| `pip-model-revision` | `model-revision` |
| `pip-investment-conviction` | `investment-conviction` |

The fundamental-only repository now includes initiation, model revision and investment conviction. Existing coverage must select regular or major update mode. New coverage plans have the 2.0.0 catalog identity; reconcile old plans explicitly rather than only changing their version label. Shared handoff schema kinds remain unchanged; conviction is referenced support, not a new rating or envelope kind.

Portfolio allocation, risk-budgeting and cross-asset trading remain outside this repository. No private evidence or issuer model is migrated here.

## Version 2.1 invocation update

`management-questions` is now `issuer-questions`, matching the maintained workspace. Update explicit invocations and coverage records. The shared handoff schema still accepts the historical `management-questions` kind for compatibility; new work uses `issuer-questions`. Industry analysis is a required role before operating forecasts and an evidence refresh in both update modes. Reconcile earlier coverage plans against the current catalog instead of changing their version label alone.

## Version 2.2 presentation update

The bundle adds `report-layout` for full A4 reports; the one-page brief remains under `research-brief`. Update coverage plans to the 2.2.0 catalog and decide whether the full-report layout applies. Chrome and optional PDF-inspection dependencies are separate host capabilities.

New full company workbooks use the updated theme, Cover/Summary/Checks structure and compact source tags with row-label comments. A compact operating scaffold may retain visible full explanations to the right. Preserve valid existing user workbook names and edits during a narrow revision. Source-tag insertion changes physical addresses; use the model builder's address translation rather than manually shifting isolated formulas. The supplied example's case selector is `Cover!C9`.

## Version 2.3 report-coverage API

Existing full-report builders must now account for the renderer's `QUESTIONS`: pass question IDs through `section(..., covers=(...))`, or call `omit(question, reason)` for a genuinely inapplicable question. Unknown IDs and empty omission reasons fail. A section can answer several questions; this does not require twelve separate chapters. The check covers declarations, not the quality or truth of the analysis. The standalone one-page brief API is unchanged.

Historical trailing P/E is an optional, separately labelled cross-check using announcement-date-aware reported earnings. It must not replace or be merged with historical forward P/E, and later realised forward earnings remain a forecast-bias diagnostic. A multiple's earnings basis alone does not determine the target date.
