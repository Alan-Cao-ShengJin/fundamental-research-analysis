# Version 2.0 name migration

## Version 2.10 decision and review contracts

The decision schema is **1.1**, independently of the publication wrapper **1.2**. Before synchronization, explicitly supply `triggerCoverage` and `triggerTests` under the [decision contract](skills/report-layout/references/decision-record.md#numerical-trigger-meaning). Bind automatic call conditions to their economic input, strict/inclusive relation, displayed boundary and expected rating. Approximate watch levels carry no automatic call promise. Local probes do not establish global monotonicity or detect omitted conditions.

For each financial assertion family, declare economic `applicability` separately from verification `status`. Applicable families need checked definition-aware assertions and registered `claimIds`; generic arithmetic alone is not the family check. Missing rows, data or displays leave verification incomplete. Genuine non-applicability needs a reason and no hidden family assertions or claim links. Preparation leaves these judgments undecided; it never marks them passed. See the [publication workflow](skills/report-layout/references/publication-review.md).

Keep frozen historical outcomes, rule bytes, findings and actual review attempts. Current preparation refuses to silently relabel an earlier review history. Adopt current contracts in new work or perform an explicit migration preserving prior attempts/findings; do not reset a review budget to obtain publication. Earlier-version contracts below describe their own releases.

## Version 2.9 publication contracts

Current builders must generate a synchronized decision record before writing/review, including spec/workbook hashes and declared trigger-text bindings. The package defaults to `evidence/decision.json`; see [decision migration](skills/report-layout/references/decision-record.md). New scalar/range prose bindings use `bound_measure` and matching source/calculation assertions; existing financial-family `bound_value` bindings remain supported.

The publication wrapper is now 1.1: `draftVersion` counts preparations, while a named reader starts an attempt with `publication_review.py begin STUDY --reviewer NAME`. Failed/interrupted attempts retain their budget and prior findings survive intervening drafts. Routed research mode, comparison/incremental-flow coverage and brief fidelity are required. Preserve historical outcomes and rule snapshots; do not relabel old reviews or reset their budget. `--legacy` is explicitly historical inspection, not publication. Full details: [publication workflow](skills/report-layout/references/publication-review.md).

The decision schema 1.0 is distinct from the publication wrapper 1.1. Refresh genuine old model/evidence components in a new versioned study rather than treating an old decision as reviewed under the new contracts. Existing coverage plans need regeneration or a reconciled migration to the new catalog version; changing the label alone does not perform missing work.

## Generic skill names

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

## Version 2.8: publication review required

Existing full-report builders must add `Report.financial_summary(...)` for initiations, declare applicable financial assertions with bound displayed outputs, and adopt the [draft/review/finalize workflow](skills/report-layout/references/publication-review.md). The first `package()` call intentionally exits with `awaiting-review` and no ZIP. An actual fresh reader completes the partial review; finalization packages the reviewed PDF bytes without reprinting. Changed inputs require a new review within the recorded budget. `release_check.py STUDY --legacy` is historical integrity-only verification and does not create a current reviewed release. Keep the earlier analytical challenge; the later draft review is an additional stage.
