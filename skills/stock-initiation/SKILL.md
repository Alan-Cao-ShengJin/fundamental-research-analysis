---
name: stock-initiation
description: Initiate investment coverage of a stock with a historical/model baseline, independent forecasts, valuation and investment case. Use for a first stock report or explicitly fresh initiation; use model-revision for new evidence on an existing model.
metadata:
  version: 2.1.0
---

# Initiate stock coverage

Establish whether this security offers an attractive payoff at the reference price. Use the full company sequence in [research cycle](../research-cycle/SKILL.md), with [company model](../company-model/SKILL.md) supplying the financial construction. A request only to build a financial model can use that specialist without producing a stock recommendation.

## Establish the initial case

- Define the issuer/share class, accounting basis, question, horizon and evidence universe. A new initiation is a fresh study: work only from the [approved sources](../evidence-intake/references/research-data-providers.md#approved-sources) and the skills, and do not open earlier research, models or other local files. Use the existing-coverage route only when the user asks to update coverage.
- Run [industry analysis](../industry-analysis/SKILL.md) before the operating forecasts: industry growth, the company's competitive niche, whether entry barriers are rising or falling, upstream costs and downstream customer behaviour. Use its findings to set growth, share, price, cost and margin-duration assumptions, rather than extending the company's reported history. Establish historical base rates and a credible shareholder-return mechanism. Separate management ambition, market expectations and the analyst's case.
- Select applicable [sector economic mechanisms](../company-model/references/sectors/index.md) to guide the initial source questions, operating breakdown and relevant accounting/valuation checks. Material mixed activities can need different builds; do not import every KPI from a sector label.
- Build source-backed historical statements and operating drivers. Complete initial governance and financial-red-flag reviews before forecasts, then build revenue/costs and integrated IS/CF/BS. Use the [company sequence](../research-cycle/references/company-sequence.md) for dependencies and readiness.
- Select valuation methods from the business economics. Audit the model, test implied expectations and minority shareholder access, challenge the central case, then conclude under the shared [decision contract](../investment-conclusion/references/decision-contract.md).
- Freeze the initial evidence, assumptions, model/run identity, forecast, valuation and decision. Identify pivotal assumptions and observable revision conditions for future reviews.

Draft the [conviction anchor](../investment-conviction/SKILL.md) during investigation and finalize it after model, risk and challenge work, so future reviews test the same proposition rather than rewrite the story around price movements.

Take the model's structure from the [sample model](../company-model/assets/company-model-example.xlsx) and its evidence from sources downloaded for this study.

## Skill emphasis and output

Use evidence intake, company modeling, governance, financial quality, valuation, challenge and investment conclusion across the material company case. Theme, macro, management questions and portfolio work remain conditional. Existing uncertainty and rating rules apply.

The output explains the business, the industry and its effect on the forecasts, competitive economics, supported investment insight, model/valuation, counter-case and what would change the view. Deliver the [human-auditable Excel forecast model](../company-model/references/workbook-profile.md), built to the [model standard](../company-model/references/model-standard.md), with the initial coverage package, alongside any machine interface. Use [research brief](../research-brief/SKILL.md) for the initial pitch and its decision brief, matching the requested format and length. Deliver the full report, the one-page brief and the Excel model together in the study's deliverables folder and as one zip; the report lists the model and brief as accompanying files (`Report.companions` in [report layout](../report-layout/SKILL.md)). A source folder or earnings summary alone is not an initiation.

For existing coverage, follow the governing [request routing](../research-cycle/references/request-routing.md) into a regular review or major earnings/catalyst update through [model revision](../model-revision/SKILL.md). Invalid or missing foundations can require targeted rebuilding; identify that scope before calling the analysis complete.
