# Workflow: scoping, implementation branch, recurring reviews and stopping

## Scope the work

Start with a research brief: question, objective, horizon/deadline, information cutoff, existing work, available sources/tools and required deliverable. For portfolio or implementation work, also record mandate/version, permitted instruments and exposures, capital/liquidity needs, positions in scope and actual/paper mode. Do not infer missing constraints from account balances or a return aspiration.

The approved mandate is owned by the application. A research brief may propose a change but cannot make it effective. Personal loss capacity is neither an expected return nor an instruction to consume the full loss budget.

[Request routing](request-routing.md) selects initiation, regular review or major update and defines the two update procedures. [Company sequence](company-sequence.md) defines the initiation stages and gates. A revision can end with no material change or identify an invalid baseline needing targeted reconstruction; carry unaffected artifacts by reference. Use the [workbook profile](../../company-model/references/workbook-profile.md) for the synchronised human and machine models.

Management questions branch from forecast sensitivities and unresolved validation issues. Ask only what cannot be established from available sources, and do not wait passively for a nonessential IR response.

## Optional downstream implementation and other assets

The following describes an external handoff, not installed skills or a required part of company research. Apply the [scope boundary](scope-boundary.md); this repository does not provide portfolio allocation, strategy backtesting or non-company underwriting.

1. Refresh account/market context and inventory sources and tools.
2. Reconcile facts and record conflicts, publication times, units and missing coverage.
3. Compare a few economically distinct tradable hypotheses with an appropriate simple baseline, including taking no new risk. For a company trade, use the completed company-research conclusion as the underlying input.
4. Route by underlying economics, then analyse the exact tradable instrument separately:
   - **Single-company equity:** the model, audit, valuation, validation and conclusion sequence. Stock-linked perpetuals additionally need contract analysis.
   - **Equity index:** index definition, constituents/concentration, earnings/valuation context, macro/factor exposure and contract basis; no invented consolidated company accounts.
   - **Commodity:** physical balance, inventories, supply response, marginal costs, reference contract and roll/carry when applicable. Gold and an industrial commodity require different drivers.
   - **FX/rates:** quote convention, rate differentials, policy/flow drivers and instrument mechanics. A yield-reference price and a bond price need different P&L treatment.
   - **Crypto:** protocol economics, token supply/unlocks, liquidity, concentration, catalysts and venue/custody risks. A token is not automatically a claim on protocol cash flows.
   - **Carry or a pair:** identify what exposure is offset and what return remains; evaluate every leg's product and margin pool.
5. Define tradable entry/exit rules and test them using only information available at each decision time. Apply costs and adverse execution assumptions.
6. Challenge the economics, evidence, numerical model and implementation. Separate a promising hypothesis from a validated signal.
7. Evaluate portfolio-level concentration, gross/net exposures, stress losses, liquidity and collateral. Only then derive candidate weights through an explicit sizing policy.
8. Produce a sourced brief and candidate or no-action result. Recheck current authority and account state before any later approved paper/live action.
9. Save follow-ups, proposed watches and evaluation dates. Activate only through actual reviewed monitoring infrastructure. Attribute outcomes and revise assumptions when evidence warrants it.

These are dependencies, not a requirement to run every specialist on every question. A source-only request stops after a useful source handoff; a financial-statement question does not need a full reverse DCF; a commodity pair does not need an equity P/E band.

## Recurring-review path

Load the last decision, watch specifications, active-monitor acknowledgements and unresolved tasks. Check data/worker health before interpreting a lack of alerts. Identify whether new information changes facts, thesis, strategy validity, portfolio fit or just price.

A company review's cadence does not determine its research mode. Apply [request routing](request-routing.md): regular review between major events, escalating when material earnings/catalyst evidence requires recalibration.

Examples of selective invalidation:

- Restated actuals: recheck affected model rows, forecasts, valuation and briefing text.
- New management guidance: update affected drivers and the scenarios depending on them.
- Changed control, rights, related-party terms or capital allocation: refresh the governance bridge and affected cash/dilution/value assumptions, target and call.
- Changed price/funding: refresh instrument economics and portfolio sizing; do not rebuild an unchanged company model.
- Oracle/margin change: suspend the affected implementation hypothesis and re-evaluate all dependent pairs.
- User changes risk limits: require the host's mandate revision; recheck every candidate against the approved new version.

Do independent work while a nonessential answer is missing. A critical missing fact blocks the dependent claim or candidate, not unrelated research. A failed data feed is an operational issue with its own next action.

## Priorities and stopping conditions

Rank tasks by their ability to change a decision, material downside, imminence, information gain and cost. A high score is a prioritisation aid, not a fabricated probability. Record what success/failure of a test would mean before running it.

Stop a cycle at its time, step, output-size or compute limit and retain the next useful task. Stop for mandatory input, revoked authority or an uncertain external request where retry could duplicate charges/effects. Do not ask the user to approve another ordinary research read already in scope.

Watch outcomes need an expiry/review date. If a hypothesis repeatedly fails, retire or reformulate it; do not endlessly postpone a decision or lower the evidence bar. Revising the mandate remains the user's choice.
