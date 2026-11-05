# Research skill verification ? 5 November 2026, version 2.2.1

This patch imports six changed instruction/reference files from the maintained workspace. Earlier release records below are historical.

## Changes

- Research challenge now distinguishes the economic dependence of the target on each investment reason from the assumption's difference versus comparable consensus. The model standard and company sequence carry this into valuation presentation and the challenge stage.
- Investment conviction now checks each numerical thesis breaker against the matching base-case metric and period and identifies shared causes behind multiple conditions. Conflicts require investigation; thresholds must not simply be moved to defend the thesis. Investment conclusion references this check.
- Full-report layout now directs study builders to draw figures in prose, tables and charts from calculated model outputs and saved source data, and rebuild both the report and brief after a model change.

These are instruction refinements. No new calculation helper, threshold evaluator, report-claim registry or automated claim-validation engine is introduced, and no real-company study was rerun. The existing scripts and assets remain unchanged. The public bundle still contains 20 skills and 11 flows; its coverage planner, scope boundaries and licence notices are preserved. Method inspirations discussed in the review include [GeniusTrader-Harry's pillar audit](https://github.com/GeniusTrader-Harry/equity-research-skill/blob/main/references/phase10-pillar-audit.md) and [Evilhill's report pipeline](https://github.com/evilhill/equity-research-skill).

## Executed verification

- Structural/catalog/link/schema/coverage checks passed.
- The six affected skill entry points passed the skill-entry validator (company-model, investment-conclusion, investment-conviction, report-layout, research-challenge and research-cycle).
- JavaScript: 65 tests passed. Python: 89 tests passed.
- Publication file/credential screening and canonical file-manifest checks passed.

The tests exercise existing deterministic behavior and structural integrity. No independent behavioral evaluation, new PDF render, native Excel recalculation or investment-performance assessment was performed for this wording patch. No private research, broker material, live responses or credentials are included. The refreshed manifest describes this supplied file set.

## Historical record: version 2.2.0

# Research skill verification - 5 November 2026

This section records version **2.2.0**. Earlier release records below are historical; their counts, names and test totals apply only to those releases.

## Current changes and scope

The workspace has 23 skills and 14 flows. The standalone company-research export now has **20 skills and 11 flows**, with twenty sector activity guides. Portfolio allocation, cross-asset strategy and risk budgeting remain external.

- Added `report-layout`: a reusable A4 full-report renderer, front page and section rails, numbered sources/exhibits, chart helpers, embedded IBM Plex Sans fonts and the complete SIL Open Font License. The one-page brief retains its separate template. PDF printing requires Chrome; page inspection has optional declared PyMuPDF dependencies.
- Expanded human-reviewable models with Cover, Summary, Scenarios and Checks, navigation, source tags, row-label comments, tab colours, grouping, print settings, chart controls and physical address translation for inserted source-tag columns. The supplied company example is synthetic.
- Adopted the updated workbook theme (blue hardcodes and blue/yellow assumptions, black formulas, green cross-sheet links, grey italic memo ratios and bold black key outputs) and aligned the older portable scaffold with it. Clarified the different annotation layouts for a compact scaffold and the full company model.
- Strengthened the research debate: identify the core contested investor questions, assemble the strongest claims on both sides, seek discriminating evidence, and build bear/bull outcomes from those questions rather than minor changes to every input.
- Updated full-initiation delivery guidance to accompany the report with its brief and Excel model. Provider guidance now includes benchmark/stock price history for the front-page comparison; access remains host- and entitlement-dependent.

Preserved the coverage planner, company-only scope, third-party notices and CI. Added the report-layout applicability rule. Removed a named-issuer example from the generic renderer, corrected stale scenario-selector examples, fixed displayed scenario-return arithmetic and a clipped final date label, and added regression coverage. Existing private research and provider responses are not part of the export.

## Executed verification

| Check | Result |
| --- | --- |
| Isolated dependency installation | `npm ci --ignore-scripts` passed |
| Skill entry validation | All 20 entry points validated |
| Structural check | 20 skills and 11 flows; catalog, coverage, schema and relative links checked |
| JavaScript suite | 65 tests passed across five files |
| Python suite | 89 tests passed, including eight new report-layout tests |
| Supplied synthetic company workbook | Formula/input/cached-value synchronization passed for 6,765 numeric cells |
| Portable operating scaffold | 48 named cells synchronized after the palette refresh |
| PDF smoke render | A two-page synthetic report printed in Chrome and its page images inspected; the fixture is deliberately sparse and is not an issuer report or a production content-density test |

The PDF smoke check confirms basic rendering and exposed a date-label clipping issue, which was corrected and re-rendered. It does not validate every chart type, every report length or every language. No new native Excel recalculation or native Excel visual review was performed; the supplied workbook's saved values were compared with its specification. No live-agent behavioral study, forecast-accuracy assessment or investment-performance evaluation was performed. Source truth and judgment are not established by these checks.

The file manifest records canonical Git bytes, excluding itself to avoid self-reference. Publication screening compares known local credential values, common token patterns, private paths and workbook XML metadata; it is bounded screening, not forensic assurance. Local save-path metadata was removed from the synthetic company fixture. Fonts retain their own OFL licence and are not relicensed under MIT.

## Historical record: version 2.1.0

# Research skill verification - 4 November 2026

This section records the version **2.1.0** export. The earlier 2.0.0 audit below is historical and its skill counts, invocation names and test totals do not describe the current release.

## Current scope and changes

The maintained workspace has 22 skills and 14 flows. This standalone company-research export has **19 skills and 11 flows**, including the new industry-analysis role and twenty sector activity guides. Portfolio allocation, risk-budget and cross-asset strategy extensions remain outside this repository. The issuer-question skill now uses the workspace's `issuer-questions` invocation; the former handoff kind remains accepted for compatibility.

Imported the current instructions, references, generic scripts, original synthetic assets and deterministic tests. Updates cover industry economics before forecasts and during reviews; integrated workbook construction and synchronization; current-forward earnings and own-versus-consensus P/E comparisons; target underwriting; evidence handling and source access limits; investor judgment; and drivers-first, selective investment writing and calibration.

Preserved the public repository's coverage planner/checker, CI, global data-planning documents, scope boundary and pinned third-party licences. Updated coverage for industry analysis and the renamed question skill. Removed an orphan dependency on an excluded strategy-testing stage. An additional regression verifies that industry work cannot be skipped in any of the three company modes. No issuer forecasts, private workbooks, broker reports, credentials or live provider responses are supplied.

## Executed verification

| Check | Result |
| --- | --- |
| Clean dependency installation | `npm ci --ignore-scripts` passed in an isolated publication checkout |
| Skill entry validation | All 19 entry points passed `quick_validate.py` |
| Bundle structure | 19 skills, 11 flows; local links, catalog, coverage and handoff schema checked |
| JavaScript tests | 65 passed across five test files |
| Python unittest suite | 80 passed, including coverage planning and workbook/forecast helpers |

The file manifest records the supplied file set and hashes. Its own bytes are excluded from its hash list to avoid self-reference. Credential-pattern and private-path screening is a bounded publication check, not forensic assurance. Workbook test results refer to synthetic fixtures, not recalculated issuer forecasts.

These checks establish structural consistency and tested deterministic behavior. No independent live-agent behavioral test, native Excel rendering run, forecast-accuracy study or investment-performance evaluation was performed for this export. Authored behavioral cases are evaluation material, not evidence of executed evaluation. No subscriptions, active monitors, dispatch service or trading capability are introduced.

## Historical audit: version 2.0.0, 2 November 2026

Version 2.0.0 removes the application-specific prefix from maintained skill identities, folders, sibling links, imports, catalog references, tests and visual-theme identity. Historical names remain only in migration documentation and unchanged provenance records. This audit concerns instruction and deterministic-tool coherence; it does not establish investment performance or source truth.

## Scope and review

The workspace has 21 generic skills. The standalone repository contains 18 company-research skills and ten routes. The three portfolio/strategy/risk extensions remain external to this repository. Reviewed the entry skills, their decision-relevant references, routing/dependency graph, shared handoff contract, model/revision requirements, sector ownership boundaries, conditional branches, support-file imports and deterministic tests. No issuer model, entitled broker report, credential, live response or private source archive is supplied.

## Findings and corrections

| Finding | Change |
| --- | --- |
| Available side branches did not guarantee an explicit consideration decision. | Added a mode-specific coverage specification and planner/checker covering every skill. Conditional work needs an applicability decision; required work needs completed or eligible reused references. |
| A screening handoff could bypass the proper new/existing coverage entry. | Selected names now enter initiation or the appropriate update mode before deeper company work. |
| The model specialist's stage table did not show costs as its own explicit build. | Added matched component costs, unit economics, segment margins and investment before integrated statements. |
| Conviction existed but was absent from some human-readable sequence summaries. | Made it an explicit stage before the conclusion, consistent with the catalog and references. |
| Core catalog routes ended at the brief without an explicit follow-up stage. | Added follow-up/learning stages after all three core modes; proposed observations remain separate from activated monitoring. |
| Regular reviews need valid inherited risk/audit support without automatically rebuilding forecasts. | Required coverage accounts for governance/model/quality reuse; targeted numerical revisions must reference risk review, recalculation, audit and refreshed outputs. |
| A standalone export can retain dangling dependencies on excluded workflows. | Removed extension-only stages and routes and replaced external links/instructions with explicit scope boundaries. |
| Public instructions contained workspace-specific branding and stale package scope/version claims. | Generic names, 2.0.0 package/manifest, updated index, migration guide and coherent standalone instructions. |
| A clean Linux run exposed an Excel-tracer dependency already installed on the development machine. | Declared pinned `openpyxl`/`et_xmlfile` requirements, documented setup and installed them explicitly in CI before testing. |

## Dependency logic

Initiation establishes identity/cutoff, business/competition, source history, early governance/reporting reliability and sector mechanisms before forecasting. Foundational revenue and cost assumptions feed linked earnings, capital, working capital, financing and cash. Audit precedes valuation; provisional valuation feeds thesis validation and challenge. Conviction and eligibility are assessed before the final target/rating and communication. Follow-up preserves observations, vintages and learning.

Regular review loads the previous case/model/conviction, checks new evidence and refreshes price/valuation/return while retaining operating forecasts unless concrete evidence warrants a change. Major earnings/catalyst work preserves frozen forecasts, evaluates matched outcomes before overwriting estimates, then recalibrates affected dependencies. A catalyst without period actuals uses an event-impact bridge. Material discoveries reopen affected work at any time.

## Skill coverage by mode

`required` means perform scoped work or explicitly reuse eligible dated artifacts; it does not require a new report per specialist. `conditional` means decide whether the specified trigger applies and retain the reason. The alternate entry mode is outside the chosen scope. Portfolio, trading and covariance-budget work are separately scoped and not silently required for a stock report.

| Skill | Initiation | Regular | Major |
| --- | --- | --- | --- |
| `research-cycle` | required | required | required |
| `stock-initiation` | required | outside-scope | outside-scope |
| `model-revision` | outside-scope | required | required |
| `evidence-intake` | required | required | required |
| `company-model` | required | required | required |
| `corporate-governance` | required | required | required |
| `financial-quality` | required | required | required |
| `valuation-thesis` | required | required | required |
| `research-challenge` | required | required | required |
| `investment-conviction` | required | required | required |
| `investment-conclusion` | required | required | required |
| `research-brief` | required | required | required |
| `monitor-review` | required | required | required |
| `company-change-tracking` | conditional | required | required |
| `macro-event-analysis` | conditional | conditional | conditional |
| `theme-screening` | conditional | conditional | conditional |
| `management-questions` | conditional | conditional | conditional |
| `chart-visualization` | conditional | conditional | conditional |

Management questions branch from unresolved decision-driving gaps, not a mandatory outreach quota. Macro/context work feeds operating drivers or valuation through distinct mechanisms. Screening discovers/triages candidates and does not complete underwriting. Charts are a communication subtask. Governance establishes facts and shareholder consequences; conviction preserves/test reasons; conclusion owns the price-based rating and eligibility explanation. Financial quality has three distinct passes using shared issue IDs. None duplicates a separate model or independent price target.

## Verification

| Check | Result |
| --- | --- |
| Entry-point validation | 21 workspace and 18 standalone entries passed |
| JavaScript tests | 44 passed in both workspace and standalone export |
| Python tests | 57 workspace; 50 standalone passed (seven portfolio-risk tests excluded with their module) |
| Catalog/links/English/schema/source checks | Passed; standalone checks supplied content without claiming private archives were shipped |
| Coverage behavior | Missing/duplicate skills, skipped required work, undecided conditions, stage reordering, stale method versions, missing reuse references and unchecked targeted revisions are rejected |
| Agent evaluation scenarios | Authored scenarios retained; no live-agent behavioral or investment-performance evaluation claimed |

The optional workbook renderer requires a compatible external runtime; it is not a supplied dependency or evidence that a real issuer model was rendered. No issuer forecasts or financial models were recalculated in this cleanup. The coverage helper checks declared completion and references; it cannot verify source claims or whether an analyst actually performed the referenced work. No automatic worker dispatcher, active monitor or trading integration is introduced.
