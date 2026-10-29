---
name: pip-research-challenge
description: Fact-check and challenge an investment opinion, research thesis, valuation or strategy. Use for standalone devil's-advocate reviews or pre-decision scrutiny of unsupported claims, causal gaps, fragile assumptions and implementation risks.
metadata:
  version: 1.15.0
---

# Research challenge

Review the thesis against raw evidence, calculations and relevant investment constraints. Identify what would change the decision; generic risk lists do not substitute for testing the actual claims.

For a standalone opinion, first restate its strongest fair interpretation and separate factual premises, forecast, causal mechanism, valuation implication and proposed action. Check each premise and identify the omitted assumption between adjacent links. A user asserting profit growth, for example, has not necessarily asserted an attractive stock return. Avoid inventing a stronger claim to refute.

## Challenge in five dimensions

1. **Evidence:** trace the decision-driving claims to accessible source locations and publication/availability dates. Check whether multiple sources are independent, quotations retain their qualifications and contrary evidence was considered. Missing or synthetic evidence cannot silently support a real-account claim.
2. **Economics:** explain the strongest alternative causal account. Is the proposed return actually market beta, a liquidity/credit premium, short-volatility risk or leverage? Why is it not already priced? What specifically could falsify the thesis?
3. **Numbers:** reproduce key unit/period/currency conversions, statement bridges, scenario arithmetic and valuation basis. Check whether adjustments are motivated by evidence or by the desired conclusion. Do not treat a zero check or a numerical round trip as economic validation.
4. **Testing:** inspect point-in-time availability, selection/survivorship bias, alignment, cost assumptions, sample size, repeated parameter search and reuse of a holdout. A held-out correlation check is not proof of tradable spread convergence.
5. **Implementation and portfolio:** challenge exact contract mappings, fill/legging assumptions, margin pools, collateral, liquidity in stress, pending actions and overlap with existing risks. Ask how the strategy can fail even when the underlying thesis is right.

Use issue classifications: invalid fact/calculation, critical missing evidence, sensitive assumption, implementation blocker, or nonblocking uncertainty. Materiality depends on the mandate and decision, not an arbitrary count or severity score.

For a company recommendation, challenge the [governance assessment](../pip-corporate-governance/SKILL.md): is apparent cheapness compensation for weak rights, cash diversion or poor allocation, and what could actually change it? Check that the same risk is not charged multiple times. Test the pivotal investment insight against attributed/price-implied expectations and a credible cash-return or repricing mechanism; do not assume the market is unaware of a known fact.

Check the [stock decision contract](../pip-investment-conclusion/references/decision-contract.md) before the final conclusion: one Buy/Hold/Sell call (Hold mandatory within the inclusive -10% to +10% primary-target price-return band), one primary target/date, current quote/time and correctly calculated same-horizon bear/bull returns. Reconcile competing methods and distinguish intrinsic value from an attainable price. A strong business, a low multiple or a polished report does not by itself establish a Buy.

Before a severe governance/reporting conclusion, apply the [red-flag review](../pip-financial-quality/references/financial-red-flags.md): reconstruct pivotal evidence, check corrections/remediation and plausible benign explanations, separate severity from confidence and test double-counted losses. An audit qualification, low cash yield or allegation needs its exact scope; no ratio is a fraud finding. Equally, management reassurance, cheapness or a favorable aggregate score cannot dismiss a substantive threat. Review the same issue IDs and state what is bounded, resolved or still essential. A second self-review is not independent assurance.

## Resolve and hand off

For company recommendations, apply the [underwriting standard](../pip-research-cycle/references/underwriting-standard.md), [investor judgment](../pip-research-cycle/references/investor-judgment.md) and [empirical/source validation](../pip-research-cycle/references/empirical-research-and-validation.md). Select tests by decision materiality: critical assumptions/source credibility, competitive response and funded marginal returns, advantage duration, shareholder access, priced expectations, unchanged-multiple returns, joint downside and probability versus payoff. A high win rate or attractive upside/downside ratio alone is insufficient; a plausible losing case does not automatically block a defensible central call.

Test [market-context/narrative repricing](../pip-macro-event-analysis/references/market-regime-and-investor-base.md) when it contributes to the thesis, with no automatic priority over other dimensions. Examine credible association, what is priced in and persistence/fade without requiring named buyers or proven inflows. Deepen access/capacity/supply checks when they are themselves decisive. Keep operating exposure, attention, holdings and measured flows distinct.

Reconstruct pivotal claims from original evidence, reproduce important arithmetic and retain contrary/failed analogues. Record what was actually checked; repetition is not independent evidence, a second self-review is not an independent review, and drafted evaluation cases are not passed behavioral tests. This procedure does not require additional agents or delegation.

For an opinion-only request, return the reconstructed claim, fact checks, logical gaps, strongest contrary evidence, failure scenarios and tests that would settle them. Classify individual claims as supported, contradicted or unresolved according to the evidence. Include evidence strengthening the claim when found; challenge does not require reaching an adverse answer. State access gaps rather than fabricating counterexamples. This mode does not add a final stock rating.

Return the strongest counter-case, reproduced checks, unresolved issues, evidence that would settle each issue, and which upstream/downstream artifacts must be revised. State which issues block a candidate and which permit further paper observation.

Use a `challenge` [handoff](../pip-research-cycle/references/handoffs.md) for both standalone and full-cycle reviews, with stable claim IDs and explicit upstream versions.

After a material change, rerun the affected calculation and downstream interpretation. Do not mark an issue resolved merely because wording was softened. Preserve rejected cases and failed tests so the next cycle does not rediscover them.

If the result is no action, propose the next useful investigation or an observable watch with a review date. Do not force a bullish/bearish conclusion to satisfy a return ambition. This review does not approve any proposal or attest that a model's statements are all true.
