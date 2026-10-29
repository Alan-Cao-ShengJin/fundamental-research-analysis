---
name: pip-investment-conclusion
description: Turn audited company forecasts, governance, valuation and thesis validation into a Buy, Hold or Sell recommendation with a primary target price, upside/downside scenarios and a concise investment rationale. Portfolio sizing remains a downstream task.
metadata:
  version: 1.16.0
---

# Investment conclusion

Reach the view after the model, governance, valuation and evidence checks. Follow the [company sequence](../pip-research-cycle/references/company-sequence.md) and [handoff contract](../pip-research-cycle/references/handoffs.md). Read the [stock decision contract](references/decision-contract.md) when forming a recommendation; it defines the required decision, target/return basis and business/thesis explanation.

## Required inputs

Assess recommendation readiness using the [underwriting standard](../pip-research-cycle/references/underwriting-standard.md) and [investor judgment](../pip-research-cycle/references/investor-judgment.md). Make the call from a defensible central estimate, prospective return/risk, source credibility and room for estimation error. Educated estimates and downside scenarios that reverse the call are normal; neither requires certainty or agreement with consensus. Reserve incompleteness for missing essentials that make a meaningful valuation/call arbitrary. Preserve decisive uncertainty and revision triggers without disguising incomplete research as Hold.

Load the current model/forecast and assumption versions, [governance findings](../pip-corporate-governance/SKILL.md), model audit, conditional valuation/market-expectations analysis, targeted financial/thesis validation and counter-case. Confirm that governance consequences and material model revisions propagated through valuation and all quoted numbers. If an essential input cannot be established, state that research is incomplete, identify the missing target/call inputs and continue the useful investigation; do not fabricate precision or present an incomplete analysis as a completed recommendation.

Review the current [red-flag issue dispositions](../pip-financial-quality/references/financial-red-flags.md). High-priority minority-governance concerns and material cash/reporting/solvency risks must change the thesis, model, target or readiness when warranted, rather than survive as decorative risk bullets. Separate suspected issues from established findings. A discounted price does not itself compensate for inaccessible value or an unreliable essential baseline. Preserve the decision contract: do not invent a target to force Sell, waive the inclusive Hold band or label incomplete valuation Hold.

## Synthesis

Use the current [earnings/catalyst clock](../pip-company-model/references/earnings-clock-and-peer-readthrough.md) to distinguish latest reported performance from subsequent-period expectations and the next information event. State the decisive change versus the available baseline, material peer read-through and what appears recognized versus still conditional. Date/window and confidence must support the repricing horizon; unknown timing stays unknown rather than an invented catalyst.

Integrate the dimensions by the [shared materiality principle](../pip-research-cycle/references/underwriting-standard.md#integrate-the-analysis-by-materiality), not conversation order. Use [competition/capital-return analysis](../pip-company-model/references/competition-and-capital-returns.md), [market context](../pip-macro-event-analysis/references/market-regime-and-investor-base.md) and actual [validation findings](../pip-research-cycle/references/empirical-research-and-validation.md) as relevant to the pivotal thesis. Explain whether return rests on funded per-share growth/distributions, valuation change, narrative repricing or a combination, with price, duration, shareholder access and loss severity considered together. No dimension is automatically dominant; detailed investor-demand analysis appears when material.

Follow the [probability-versus-payoff assessment](../pip-research-cycle/references/investor-judgment.md#separate-probability-of-success-from-the-payoff-at-the-price): explain whether likely success is already reflected in the price and whether gains compensate for the likelihood and severity of losses. High confidence in business performance is not the same as attractive expected shareholder return. Assess regime dependence and permanent-loss exposure. Use qualitative likelihoods when numerical weights are unsupported; keep expected return separate from the primary target and preserve the existing Hold rule.

Explain the core money-making engine and evidence for the competitive advantage/moat in concise language for an informed nonspecialist. Define company-specific jargon. Then identify the pivotal reason to invest or not invest: the difference from priced/attributed expectations, its cash/per-share effect and the credible shareholder-return or repricing path. If there is no validated overlooked driver, say so rather than inventing a market mistake. Separate supported observations, analyst assumptions and remaining uncertainty.

Select one primary target price for a stated date/horizon and explain the preferred valuation method. Show its signed return from the timestamped current price, plus bear and bull targets/returns at the same horizon. Separate price change, prospective distributions, FX and costs. Distinguish present intrinsic value from an attainable future target, especially when a governance discount can persist. State catalysts, downside mechanisms and observable thesis breakers; recompute all dependent targets when evidence changes.

For a completed stock recommendation, state **Buy**, **Hold** or **Sell** prominently. **Hold is mandatory when the primary target's price return from the reference price is between -10% and +10%, inclusive.** Calculate before rounding the displayed percentage; dividends and total return do not override this threshold. Follow the exact boundary, completeness and repricing rules in the [decision contract](references/decision-contract.md). Outside this band, assess Buy or Sell on the supported return/risk case. Trim/Avoid/Watch can describe follow-up or implementation but cannot replace the primary call. Explain confidence and the strongest counter-case without diluting the label. A Sell is not automatically a short instruction. Avoid unsupported probabilities and never tune valuation assumptions to force the desired call.

Test whether governance explains apparent cheapness and whether outside shareholders can realise the value. A persistent justified discount, weak rights or repeated value diversion can overturn a Buy even when headline multiples are low. Equally, do not infer poor governance from price alone or mechanically convert a governance score into a recommendation.

Provide the few management/research questions that could still change the view, ranked by sensitivity. Use [management questions](../pip-management-questions/SKILL.md) to draft them when useful, and [research brief](../pip-research-brief/SKILL.md) to communicate the result.

## Boundary and continuation

This is an investment-research conclusion, not an approved position, portfolio weight or order. If implementation is requested, hand the decision and exact security basis to a separately supplied portfolio/implementation workflow. An underlying share valuation does not transfer unchanged to a perpetual contract.

Return an investment-conclusion handoff referencing the decision record, Buy/Hold/Sell call, target and return calculations, business/moat and pivotal insight, governance consequences, supporting/counterevidence, catalysts/invalidation and material gaps. Keep prior versions for later learning. Research status and portfolio execution status are separate from the stock rating; a completed Sell need not generate an order, and incomplete research must not be disguised as Hold.
