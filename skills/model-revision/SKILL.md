---
name: model-revision
description: Update existing stock research in regular-review or major earnings/catalyst mode. Regular reviews preserve operating forecasts unless concrete new evidence warrants revision; major updates compare prior assumptions with disclosures and recalibrate affected forecasts. Use stock-initiation for first coverage.
metadata:
  version: 2.3.2
---

# Revise an existing stock model

Start from the prior evidence and executable model. Determine what the new information changes and whether it changes the investment decision. A supported no-material-change result is valid; a new document does not require different numbers.

Read [revision workflow](references/revision-workflow.md) for baseline eligibility, change records, attribution and completion. The [company model](../company-model/SKILL.md) remains the shared calculation method. Reuse business, historical, governance and valuation work that remains valid; record what was reviewed or reopened.

## Choose the update mode first

Follow the governing [request routing](../research-cycle/references/request-routing.md). Both modes start with the previous research/model, rather than another initiation.

Retrieve the original/latest [conviction record](../investment-conviction/SKILL.md) with that baseline. In either mode, separate evidence about its decisive proposition from changed estimates, value, price-based rating and investment eligibility. In major updates, evaluate its expected observations alongside the frozen forecast before replacing estimates; retain original deadlines and the reason for any changed belief. A broken anchor requires prompt reassessment, even between earnings; an intact anchor does not freeze the numbers or waive another essential risk.

- **Regular review:** retain operating assumptions by default; rerun the [world-state scan](../research-cycle/references/world-state.md) for the period since the last review and re-establish [what the market is trading](../research-cycle/references/what-the-market-trades.md); check intervening disclosures, concrete data pipelines and the industry indicators from the last [industry analysis](../industry-analysis/SKILL.md). Refresh price, valuation and prospective return on the existing forecast. Price movement alone changes return to target, not operating estimates or fair value. Any supported assumption or valuation change needs its own evidence and attribution; targeted forecast changes reopen calculation and audit work.
- **Major earnings/catalyst update:** preserve pre-event forecasts before entering new actuals, reconcile official disclosures/calls, evaluate which assumptions held or missed and why, then recalibrate affected subsequent forecasts and the decision. For material cumulative flow disclosures, derive the latest non-overlapping period where comparable earlier cumulative figures exist; distinguish a cash reversal from an earnings miss. Document unavailable or noncomparable inputs rather than inventing quarters. A catalyst may require an event-impact bridge without new period actuals. An unchanged future forecast is valid after this evaluation.

Escalate a regular review when material evidence changes the economics or thesis. State the chosen mode and reason; the presence of a new transcript alone does not require a full rebuild.

## Skill emphasis

| Work | Main specialist | Revision focus |
| --- | --- | --- |
| Compare evidence | [Evidence intake](../evidence-intake/SKILL.md), [change tracking](../company-change-tracking/SKILL.md) | Definitions, dates, restatements, guidance/actuals, conflicts and forecast surprises |
| Refresh the industry view | [Industry analysis](../industry-analysis/SKILL.md) | Indicator changes, new entrants or barrier shifts, input-cost and customer-behaviour changes, and the assumptions they reopen |
| Update economics | [Company model](../company-model/SKILL.md) | Affected drivers and linked statements; preserve useful structure, formulas and user edits |
| Check changed risks | [Financial quality](../financial-quality/SKILL.md); [governance](../corporate-governance/SKILL.md) when affected | Carry reviewed issues forward; assess new exposures and invalid foundations |
| Reassess decision | [Valuation](../valuation-thesis/SKILL.md), [challenge](../research-challenge/SKILL.md), [conclusion](../investment-conclusion/SKILL.md) | Explain target/payoff changes and test the new assumptions without defending the old call |
| Communicate | [Research brief](../research-brief/SKILL.md) | Short change note and before/after bridge; refresh affected existing outputs |

The catalog's `company-regular-review` route retains the forecast unless evidence reopens affected stages. Its `company-update` route covers major earnings/catalyst work, including forecast evaluation before model revision. Both reuse eligible artifacts. A scoped evidence review can finish without numerical changes, or explain why a missing baseline prevents quantification.

## Output

Lead with whether forecasts, cash/funding, valuation, conviction and the call change. Show material old/new assumptions and calculated outputs, causal reasons, unchanged judgments, unresolved source issues and next evidence. A small EPS or target change can conceal offsetting business changes or a large cash effect.

Default to a concise revision note. Refresh affected figures and decision blocks in existing requested deliverables without rewriting unchanged business background. Reissue a full pitch when requested or when the old thesis becomes misleading. Preserve the original vintage and link the revision to it.

For a numerical forecast revision, deliver an updated [formula-driven Excel model](../company-model/references/workbook-profile.md) with the material old/new assumptions and results visible. Preserve the original workbook and user edits, reconcile with the machine model, and verify affected formulas and input changes. A no-numerical-change review may link the existing valid workbook instead of reissuing it.

Use the same [rating rules](../investment-conclusion/references/decision-contract.md) as initiation. Revision changes emphasis and evidence scope, not numerical/source standards. It does not activate monitoring or authorize implementation.

When publishing rendered reports or briefs, use the [bounded publication workflow](../report-layout/references/publication-review.md). Reuse valid upstream analysis, but review the actual changed output against its current model and evidence. A previous initiation's review does not certify a new draft; changed frozen inputs invalidate the affected review. A narrow conversational update does not require generating a full report.
