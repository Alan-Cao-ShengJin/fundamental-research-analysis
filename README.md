# Fundamental Research Analysis

An English-language equity-research skill system for forming an investment view and maintaining it as evidence changes. Version **2.4.0** contains **20 skills**, **11 research flows** and **20 sector activity guides**, with reusable scripts, human-readable model templates, synthetic examples and tests.

Start with [research-cycle](skills/research-cycle/SKILL.md) and the [skill index](skills/README.md). Keep the complete `skills/` tree together so sibling references and helper imports resolve. These files guide an agent; they do not automatically run research, connect data services or activate monitoring.

## Choose the research mode

| Request | Work |
| --- | --- |
| New initiation | Establish the business and historical baseline; review governance, reporting quality and industry economics; build and audit operating and integrated financial forecasts; value, challenge and reach an initial investment view. |
| Existing coverage: regular review | Read the prior research, model and conviction record; check intervening evidence; preserve operating forecasts unless concrete evidence warrants revision; refresh price, justified valuation inputs and the decision. |
| Existing coverage: major earnings/catalyst update | Freeze the prior forecast; reconcile new disclosures; compare matched actuals with prior assumptions before replacing estimates; recalibrate affected forecasts, audit and refresh dependent conclusions. |

A price move alone changes prospective return, not earnings or fair value. Recurrence sets the review cadence; the evidence determines the analytical mode. See [request routing](skills/research-cycle/references/request-routing.md).

## Research dependencies

Scope and evidence → historical statements → early governance and financial-red-flag review → industry analysis → operating drivers and component revenue/cost forecasts → integrated statements → model audit → valuation and expectations → thesis validation and challenge → conviction → investment conclusion → communication and follow-up.

Frame the two or three contested investor questions early, state the strongest case on each side, and use the evidence that would settle them to construct meaningful bear and bull outcomes. The sequence expresses dependencies, not fixed analytical weights. Use [investor judgment](skills/research-cycle/references/investor-judgment.md) and the [underwriting standard](skills/research-cycle/references/underwriting-standard.md) to concentrate on what can change the decision. Reuse valid dated work; new evidence reopens affected stages. Financial quality has three distinct passes: early screening, pre-valuation model audit and post-valuation thesis validation.

## Modeling and valuation

- Build forecasts from the smallest useful, supportable economic components. Use the [sector guides](skills/company-model/references/sectors/index.md) for the relevant mechanisms rather than imposing every sector KPI.
- Deliver a formula-driven, [human-auditable Excel model](skills/company-model/references/workbook-profile.md) alongside the executable model interface when forecasts are built or numerically revised. Keep related calculations together, assumptions and explanations nearby, and both interfaces mechanically synchronized.
- Use the updated workbook theme: gridlines off; historical hardcodes blue; forecast assumptions blue on light yellow; ordinary formulas black and cross-sheet links green; memo ratios grey italic and key outputs bold black. A Cover and Summary lead the workbook, with source tags beside inputs and full explanations in row-label comments. Checks, navigation, grouping and print settings support human review.
- Match earnings periods, accounting basis, currency, share basis and estimate vintages. Explain the earnings and multiple contributions to the target. Distinguish our forecast P/E from a consensus-based comparison; a multiple implied by our own valuation is not independent confirmation.
- Anchor the target to an appropriate method, relevant history or peers and a defensible path to realization. Current-forward earnings and the target horizon are separate; do not silently roll the earnings denominator to the target date. See the [valuation calendar](skills/valuation-thesis/references/valuation-calendar.md).

The [full-report layout skill](skills/report-layout/SKILL.md) supplies a reusable A4 renderer, embedded licensed fonts, numbered exhibits and source references, and chart helpers. It is separate from the one-page brief template. Full-report sections now declare the investor questions they cover through `section(..., covers=(...))`; each remaining question needs an explicit `omit(question, reason)`. One section can cover several questions. This checks declared coverage, not whether the analysis is correct. Full initiations package the report, brief and model together.

The historical forward P/E band remains the primary comparison for a forward-EPS target. A separate trailing band uses earnings already reported at each price date, updating at announcement dates. Compare each band with today's matching P/E; subsequently realised forward earnings belong to forecast-bias analysis, not historical market expectations. Never merge trailing and forward series into one band.

The [company-model standard](skills/company-model/references/model-standard.md) and generic workbook builders support construction and verification. Supplied examples are synthetic, not issuer forecasts or recommended assumptions.

## Judgment, conviction and communication

[Industry analysis](skills/industry-analysis/SKILL.md) connects growth, competitive position, barriers, upstream costs and downstream behavior to forecast assumptions, valuation and tracking indicators. [Investment conviction](skills/investment-conviction/SKILL.md) preserves the decisive economic or avoidance proposition and the evidence that would change it. Conviction can survive price volatility; it does not excuse errors or a broken thesis.

Before concluding, check both a thesis driver's contribution versus comparable consensus and the target's dependence on that driver. Test numerical thesis breakers against the matching base-case metric and period; resolve conflicts rather than moving thresholds to defend the call. Report builders should obtain figures from calculated model outputs and saved source data, and rebuild the report and brief after model changes. These are analyst/builder requirements, not a claim that a new automated report-claim validator is supplied.

Map actual geographic, channel and customer exposure before researching trade or demand risks. Interpret share changes alongside absolute growth and comparable segments. Test forecasts against the exact incentive-plan terms without forcing earnings to meet a hurdle. Triangulate valuation with relevant own history, close same-market peers and sector investment conditions; a short or single-regime history cannot set the multiple alone. Dividend yield uses the same forward fiscal year as the selected target EPS, with the current-year yield alongside it where useful.

The [decision contract](skills/investment-conclusion/references/decision-contract.md) keeps rating, attractiveness, eligibility and portfolio action distinct. Its thresholds are house mandate defaults, not universal investment standards; an explicit user mandate takes precedence.

Investor output follows the [one-page brief standard](skills/research-brief/references/one-page-brief.md), supported by a fuller stock pitch when requested. Develop the business drivers before valuation. Each substantive argument connects the point/data, derivation, significance and implication for the stock; include only decision-useful content. Use the shared templates and visual checks without changing the investment case merely to fit the layout.

For method changes, use [skill calibration](skills/research-cycle/references/skill-calibration.md): improve the owning instructions and reusable resources, then test transfer to an independent synthetic case. A polished issuer report alone does not validate the method.

## Coverage and scope

For a completed initiation or existing-coverage decision, use the [coverage plan](skills/research-cycle/references/research-coverage.md). It accounts for each bundled skill as performed, validly reused or not applicable. A generated plan starts incomplete; listing a skill does not perform its work.

```text
python skills/research-cycle/scripts/research_plan.py --mode initiation --out output/research-plan.json
python skills/research-cycle/scripts/research_plan.py --mode regular --out output/review-plan.json
python skills/research-cycle/scripts/research_plan.py --validate output/review-plan.json
```

Fill the plan with actual artifact references before validation. Validation checks declared coverage and dependencies; it does not establish the truth of the underlying work.

This repository publishes the company-research subset. Portfolio allocation, risk budgeting, cross-asset strategy, trading and active monitoring infrastructure remain outside its [scope](skills/research-cycle/references/scope-boundary.md). Issuer research, private models, entitled source materials, credentials and live provider responses are excluded. Included workbook examples are independently authored synthetic fixtures.

## Included skills

| Role | Skills |
| --- | --- |
| Routing and entry | [Research cycle](skills/research-cycle/SKILL.md), [stock initiation](skills/stock-initiation/SKILL.md), [model revision](skills/model-revision/SKILL.md) |
| Evidence and economics | [Evidence intake](skills/evidence-intake/SKILL.md), [industry analysis](skills/industry-analysis/SKILL.md), [company model](skills/company-model/SKILL.md), [issuer questions](skills/issuer-questions/SKILL.md) |
| Risk and judgment | [Corporate governance](skills/corporate-governance/SKILL.md), [financial quality](skills/financial-quality/SKILL.md), [research challenge](skills/research-challenge/SKILL.md), [investment conviction](skills/investment-conviction/SKILL.md) |
| Valuation and decision | [Valuation thesis](skills/valuation-thesis/SKILL.md), [investment conclusion](skills/investment-conclusion/SKILL.md) |
| Context and maintenance | [Theme screening](skills/theme-screening/SKILL.md), [macro event analysis](skills/macro-event-analysis/SKILL.md), [company change tracking](skills/company-change-tracking/SKILL.md), [monitor and review](skills/monitor-review/SKILL.md) |
| Communication | [Research brief](skills/research-brief/SKILL.md), [chart visualization](skills/chart-visualization/SKILL.md), [full-report layout](skills/report-layout/SKILL.md) |

`issuer-questions` replaces the earlier `management-questions` invocation. See [migration notes](MIGRATION.md) for compatibility details.

## Setup and checks

Use Node.js 24.13+ and Python 3.11+. Provider credentials belong in `.env.research-data`, which is ignored by Git; [.env.example](.env.example) contains names only. The [provider guide](skills/evidence-intake/references/research-data-providers.md) documents optional adapters and access limits. Installing this bundle supplies no subscriptions or entitlements.

```text
npm ci
python -m pip install -r requirements.txt
npm run skills:check
npm test
python -B -m unittest discover -s skills/tests -p "test_*.py"
```

On Windows PowerShell, use `npm.cmd` if execution policy blocks the `npm.ps1` wrapper. Full-report PDF printing needs Chrome (`CHROME_PATH` can select it). Page inspection and page images additionally use `python -m pip install -r skills/report-layout/requirements.txt`. Native Excel recalculation needs Microsoft Excel. These optional host capabilities are separate from the portable test suite.

Checks establish structural and deterministic behavior, not source truth, research judgment or investment performance. Preserve [third-party notices](THIRD_PARTY_NOTICES.md). Research output does not authorize outreach, trading or active monitoring.

The [release verification record](AUDIT.md) and [file manifest](bundle-manifest.json) describe this export. Authored evaluation scenarios are separate from executed tests.
