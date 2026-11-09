# Equity research workspace

Production requests are usually one line: "initiation on <company>" or "update view on <company>". Treat that as a complete instruction. Choose the workflow, evidence, financial periods, methods and assumptions yourself; ask only for intent or constraints that are genuinely missing, such as a security that cannot be identified.

The research skills live in `skills/` and are not registered as Claude Code skills. Read the files named below; nothing under `skills/` loads by itself.

Check issuer-scoped material in `inbox/` and `data/` for supplied evidence, alongside eligible components in `research/`, before remote discovery. Respect any explicit evidence boundary in a supplied exercise pack.

The ordinary short request supplies the mandate, not a checklist. Derive the research mode yourself and carry it as `researchMode` into publication. Follow the current [publication workflow](skills/report-layout/references/publication-review.md), including explicit review start, material period/comparison coverage and report-to-brief fidelity. Do not ask the user to supply these controls in the prompt.

## Route the request

For material assumption choices, separate [source facts from classification/recognition/payment timing and target deadlines](skills/company-model/references/statement-forecast.md#classification-recognition-and-payment-states). An aggregate earnings estimate supplies a conditional bridge, not unique component assumptions: test [feasible alternatives](skills/company-model/references/benchmark-comparison.md#a-conditional-bridge-is-not-a-unique-explanation) before claiming necessity. Calculate the model, synchronize the [decision checkpoint and trigger text](skills/report-layout/references/decision-record.md), then write/render with the [figure bindings](skills/report-layout/references/claim-support.md#feasible-bridges-and-actual-displayed-figures) before review. These controls neither prescribe a conservative forecast nor require identical targets across fresh runs.

- **"initiation on X"**: [stock initiation](skills/stock-initiation/SKILL.md), following the [research cycle](skills/research-cycle/SKILL.md) and its company sequence. Work in a new dated study folder under `research/<company>/`. Deliver the Excel model, the full report and the one-page brief through the [publication workflow](skills/report-layout/references/publication-review.md).
- **"update view on X"**: [request routing](skills/research-cycle/references/request-routing.md) into [model revision](skills/model-revision/SKILL.md). Build the baseline from the latest usable components in `research/<company>/`: a released model and decision, plus valid evidence from any later draft. Carry that draft's unresolved or stale review findings forward; do not reuse a conclusion that failed review. The evidence since the baseline decides between a regular review and a major update.
- Anything else: the [skill index](skills/README.md).

## Standing defaults

These apply in every study where the situation arises. The owning file holds the method; the line here makes it hard to miss.

1. **Valuation window.** A historical band's window starts at the dated event its rationale names, with the defensible alternative windows and the target and rating each gives beside it. Choose on the economics, never because a window is shortest, lowest or gives a preferred rating, and say so when an alternative crosses a rating threshold ([method selection](skills/valuation-thesis/references/method-selection.md#the-companys-own-historical-forward-valuation)).
2. **Sensitivities run through the model.** Each shock moves model inputs and is recalculated through the whole model, so tax, each unit's minority share, financing and the target's share basis act as in the forecast. Declare them under `sensitivities` in the specification; `model_workbook.py check` fails a row that does not reproduce ([model standard](skills/company-model/references/model-standard.md)).
3. **Material emerging earnings streams** get an adoption → revenue → profit → EPS bridge even while small, with substitution against existing products counted once ([revenue projection](skills/company-model/references/revenue-projection.md#emerging-earnings-streams)).
4. **Forward statements.** Reconcile the forecast with dated outlooks, capacity plans, backlog and commitments in the periods they cover. A beat record informs where in the range the base case sits; it does not make guidance a floor ([operating drivers and guidance](skills/company-model/references/drivers-guidance.md)).
5. **Periods.** The target uses the house forward period on today's earnings, and the target date is not the earnings period. Show calendar-year EPS only where the investors, the valuation convention or the comparison set work in calendar years; build it from the quarters with fiscal figures underneath. A non-December year end alone does not call for it. Match every benchmark to its denominator ([valuation calendar](skills/valuation-thesis/references/valuation-calendar.md#calendar-year-comparisons)).
6. **The brief keeps the report's qualifications.** Conditions, partial answers and alternatives that change the rating survive compression.
7. **Revisions after review** rerun the study's package adapter with `revise=True`, so integrity checks use the current bindings.

For a host-configured synthetic acceptance workspace, `.research-evaluation.json` supplies an explicit fixture clock through the publication workflow. Keep actual production/retrieval timestamps truthful; this configuration never permits live evidence to use a synthetic clock. Review preparation preserves full draft inputs before handoff. Complete the economic-basis contract from the actual valuation anchor, and classify ordinary forecast uncertainty separately from essential publication blockers.

## Conditional, not universal

Use a sector reference only for an activity that is material ([sector index](skills/company-model/references/sectors/index.md); optical networking covers lasers, modules and optical switching). Calendar-year EPS is for comparisons made in calendar years. The valuation anchor follows the company's economics and the claim valued under [method selection](skills/valuation-thesis/references/method-selection.md); a historical P/E band applies only where earnings are that anchor, and labels such as "cyclical" or "dividend payer" do not choose the method. A new-product bridge is for a stream that matters to the debate or out-year EPS. Do not import a sector's terms or tables into companies they do not describe.
