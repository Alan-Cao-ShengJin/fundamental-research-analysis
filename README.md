# Fundamental Research Analysis

An English-language, company-research skill bundle for building a defensible investment view and maintaining it as evidence changes. Version **2.0.0** contains **18 skills**, twenty conditional sector activity guides, generic modeling/coverage helpers, clean synthetic examples and tests.

## Start with the research mode

Ask the agent to read [research-cycle](skills/research-cycle/SKILL.md), then [request routing](skills/research-cycle/references/request-routing.md). Keep the complete `skills/` tree together so sibling references and helper imports resolve. These are instructions and tools for an agent to use; the catalog is not an automatic runtime dispatcher.

| Request | Sequence |
| --- | --- |
| New initiation | Business and evidence baseline -> early governance/reporting review -> sector-guided operating and integrated model -> audit -> valuation -> validation/challenge -> conviction -> initial view, Excel and report. |
| Existing research: regular review | Read prior research/model/conviction -> check intervening concrete evidence -> retain operating forecasts by default -> refresh justified valuation inputs, quote, prospective return and decision. Supported forecast changes reopen affected checks. |
| Existing research: major earnings/catalyst update | Freeze the prior forecast -> reconcile official disclosures/calls -> compare assumptions with matched actuals and record learning -> update actuals/recalibrate affected forecasts -> audit -> valuation/challenge/conviction -> revised decision and Excel when forecasts change. |

A price move alone changes upside/downside, not earnings or fair value. A catalyst without new period actuals uses an event-impact bridge. First coverage and existing-coverage updates share analytical standards, while their evidence windows and work differ.

## Account for every skill

Use the [coverage plan](skills/research-cycle/references/research-coverage.md). It identifies required roles, conditional triggers and the work reused from earlier research. A generated plan starts incomplete; listing a skill does not perform its analysis. The checker catches missing roles, skipped required work, dependency-order changes and unsupported completion declarations.

```powershell
python skills/research-cycle/scripts/research_plan.py --mode initiation --out output/research-plan.json
python skills/research-cycle/scripts/research_plan.py --mode regular --out output/review-plan.json
python skills/research-cycle/scripts/research_plan.py --validate output/review-plan.json
```

Choose a mode, perform the work and fill the plan with actual references. The initial validation is expected to fail until coverage is accounted for. Manual records following the same coverage rules are acceptable. A narrow accounting, source or model request uses its relevant subset and does not claim a complete stock recommendation.

## Research dependencies

Scope/mode -> evidence and business baseline -> historical statements -> governance and early financial red flags -> operating data and guidance -> component revenue and cost forecasts -> integrated statements -> model audit -> valuation/expectations -> thesis validation and challenge -> conviction -> investment conclusion -> communication and proposed follow-up.

The financial-quality skill performs three separate passes: early screening, pre-valuation model audit and post-valuation thesis validation. Corporate governance owns control, conduct and minority rights; conviction preserves the decisive belief or avoidance condition across reviews. Neither duplicates the other's factual work. Conditional context, screening, management questions and charts enter where useful and feed their findings back to affected stages. Valid work can be reused with its true scope/date; broken dependencies reopen downstream outputs.

[Detailed stages](skills/research-cycle/references/company-sequence.md) and the [catalog](skills/catalog.json) define the sequence. [Scope boundaries](skills/research-cycle/references/scope-boundary.md) distinguish company research from external portfolio, trading and active-monitoring workflows.

## Included skills

| Skill |
| --- |
| [Research Cycle](skills/research-cycle/SKILL.md) |
| [Evidence Intake](skills/evidence-intake/SKILL.md) |
| [Company Model](skills/company-model/SKILL.md) |
| [Financial Quality](skills/financial-quality/SKILL.md) |
| [Corporate Governance](skills/corporate-governance/SKILL.md) |
| [Valuation Thesis](skills/valuation-thesis/SKILL.md) |
| [Investment Conclusion](skills/investment-conclusion/SKILL.md) |
| [Research Challenge](skills/research-challenge/SKILL.md) |
| [Management Questions](skills/management-questions/SKILL.md) |
| [Research Brief](skills/research-brief/SKILL.md) |
| [Chart Visualization](skills/chart-visualization/SKILL.md) |
| [Monitor Review](skills/monitor-review/SKILL.md) |
| [Theme Screening](skills/theme-screening/SKILL.md) |
| [Company Change Tracking](skills/company-change-tracking/SKILL.md) |
| [Macro Event Analysis](skills/macro-event-analysis/SKILL.md) |
| [Stock Initiation](skills/stock-initiation/SKILL.md) |
| [Model Revision](skills/model-revision/SKILL.md) |
| [Investment Conviction](skills/investment-conviction/SKILL.md) |

## Models and sector guidance

Use [foundational builds](skills/company-model/references/foundational-builds.md) and the applicable [sector activity cards](skills/company-model/references/sectors/index.md). Select the actual economic mechanism, not every KPI associated with a sector label. Break forecasts into the smallest useful predictable components, substantiate them and aggregate into linked statements, capital requirements and owner cash.

New forecasts and numerical revisions require a human-auditable, formula-driven Excel model alongside the executable model interface. Keep related calculations together, assumptions and source explanations nearby, and presentation consistent under the [workbook profile](skills/company-model/references/workbook-profile.md). Use quarters when supported, or halves when quarterly evidence is thin. The supplied examples are independently invented; they are not issuer forecasts or recommended assumptions.

The coverage, provider, forecast-compiler and sector helpers use the Python standard library. Read-only Excel tracing and workbook-fixture tests require `openpyxl`; install the pinned [Python requirements](requirements.txt). The optional workbook-authoring JavaScript helper requires a compatible environment with `@oai/artifact-tool`; that runtime is not supplied by this repository or required for the test suite. Use another supported authoring/recalculation backend where appropriate and verify the resulting formulas and presentation. A workbook that merely balances is not economically validated.

## Conviction and the included decision profile

The [conviction skill](skills/investment-conviction/SKILL.md) records one decisive economic or avoidance proposition, supporting/contrary evidence, original milestones and conditions for reconsideration. An intact belief can survive volatility while valuation and attractiveness change. A persistent evidenced value-diversion condition can maintain an exclusion despite cheapness; verified remediation can reopen it. A recorded process does not create lived experience or a calibrated track record.

The included mandate plans investments for at least a year. Its [decision contract](skills/investment-conclusion/references/decision-contract.md) uses Buy above +10% primary-target price return, Hold from -10% to +10% inclusive and Sell below -10%, excluding dividends and before rounding. A separate 50% base-case upside hurdle informs attractiveness. These are included mandate defaults, not universal professional standards; an explicit user mandate takes precedence and must be applied consistently. Never inflate targets to meet a hurdle or treat incomplete valuation as Hold. Investment eligibility, the numerical rating and portfolio action remain distinct.

## Data and access

The optional [read-only provider adapter](skills/evidence-intake/scripts/research_data.py) supports registered routes for AlphaPai, Alpha Vantage, API Ninjas and Massive. Follow its [provider guide](skills/evidence-intake/references/research-data-providers.md) and verify actual entitlement/field coverage. Copy [.env.example](.env.example) locally or set environment variables. No credentials, subscriptions, live responses, original company reports or private models are included. Do not redistribute entitled broker or transcript material without the necessary rights.

AlphaPai originals are generally Chinese: retain original evidence/locators and translate accurately into the preferred language, English by default. Source language or provider identity does not establish management attendance or make a generated summary verbatim speech.

## Global data roadmap

The [global data-planning brief](docs/data-planning/2026-11-02/README.md) maps 81 source families to the twenty sector activities, with a proposed observation contract, implementation order and remaining research-capability gaps. Start with the [source catalogue](docs/data-planning/2026-11-02/global_source_catalog.json) and [data-engineering prompt](docs/data-planning/2026-11-02/data_engineering_prompt.txt). This is a worldwide requirements plan; integrations and source rights need separate validation.

## Checks and audit

Use Node.js 24.13+ and Python 3.11+. On Windows PowerShell, use `npm.cmd` if execution policy blocks the `npm.ps1` wrapper.

```text
npm ci
python -m pip install -r requirements.txt
npm run skills:check
npm test
python -B -m unittest discover -s skills/tests -p "test_*.py"
```

See the [coherence audit](AUDIT.md), [name migration](MIGRATION.md) and [third-party notices](THIRD_PARTY_NOTICES.md). Tests establish structural and deterministic behavior, not source truth, sound judgment or investment performance. Authored agent-evaluation cases are separate from executed tests. Research does not contact issuers, activate monitoring or trade.
