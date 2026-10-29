# Investment research skills

Use [pip-research-cycle](pip-research-cycle/SKILL.md) for end-to-end work, or select a specialist for a focused request. Instructions are in English and apply across issuers and markets. Adapt the analysis and output language to an explicit user request.

## Research principles and sequence

Use the [underwriting standard](pip-research-cycle/references/underwriting-standard.md) and [investor judgment](pip-research-cycle/references/investor-judgment.md) as the shared analytical foundation. Integrate business economics/competition, financial quality and funded growth, governance/shareholder access, valuation/expectations, macro/market context and probability/payoff. Choose emphasis by the security, price, horizon and decision sensitivity; conversation order and document position do not determine importance. No dimension has a fixed weight or automatic precedence.

Reasoned estimates and differentiated opinions are normal. Make a defensible central return/risk judgment without requiring perfect information or success in every scenario. Separate probability of success from its payoff at today's price. Retain source-specific credibility, uncertainty, adverse cases and observable revision conditions.

Use [competition and capital-return analysis](pip-company-model/references/competition-and-capital-returns.md), [market context and narratives](pip-macro-event-analysis/references/market-regime-and-investor-base.md) and [empirical/source validation](pip-research-cycle/references/empirical-research-and-validation.md) within the existing stages as material. Topical association can affect market price before earnings emerge without creating reported revenue. Investor-demand detail remains supporting analysis unless decisive. Instructions, empirical records and actual operating services are distinct.

Investor output defaults to a **250-350-word decision brief** and an **800-1,200-word main narrative**, with detailed models/evidence linked as support. Apply [visual report design](pip-research-brief/references/visual-reports.md), the [Humanizer-adapted writing guide](pip-research-brief/references/natural-writing.md) and [AntV chart visualization](pip-chart-visualization/SKILL.md). Figures share a professional theme and preserve source/actual/forecast distinctions.

The sequence below expresses dependencies rather than a ranking of importance. Context and evidence can develop together, and material new findings reopen affected stages.

**Evidence -> model setup -> historical statements -> corporate governance and early financial-red-flag screening -> operating drivers and guidance -> revenue and cost projections -> integrated statement forecasts -> model audit -> valuation and expectations -> thesis validation and challenge -> Buy/Hold/Sell conclusion -> brief.**

Governance and [financial-red-flag collection](pip-financial-quality/references/financial-red-flags.md) start during intake; initial decision-driving reviews precede forecasts. Severe minority-governance concerns receive high-priority triage; reporting/fraud signals are another important risk lens and can independently be decisive. One financial-quality skill performs early screening, model audit and post-valuation validation with shared issue IDs and separate pass artifacts. A focused red-flag review can use filings directly. Governance findings must reach the model and valuation before the conclusion. Cheapness can reflect a justified, persistent discount, so identify how value reaches outside shareholders and what could change the discount. Full company updates refresh the existing governance record when material evidence changes.

A completed stock report follows the [decision contract](pip-investment-conclusion/references/decision-contract.md): **Buy, Hold or Sell**, one primary target price/date, current quote/time, signed return to target, and same-horizon bear/bull risks. Explain the core business, competitive edge/moat and pivotal investment insight concisely for an informed nonspecialist. Use **Hold when primary-target price return is within -10% to +10%, inclusive**, before rounding the displayed percentage and excluding dividends. Hold retains the target, scenarios and thesis; incomplete research stays explicitly incomplete. Reporting preferences, including omission of unsolicited token-cost reports, are maintained in the research-brief skill.

The company model is executable, versioned economic state for agent queries, scenarios, valuation and forecast evaluation. Workbooks and reports are optional views or calculation backends. [Company stage gates](pip-research-cycle/references/company-sequence.md) define readiness; [research branches](pip-research-cycle/references/research-branches.md) cover theme, macro, industry, historical and recurring work.

| Skill | Use for |
| --- | --- |
| [Research cycle](pip-research-cycle/SKILL.md) | Scope, routing, dependencies and follow-up |
| [Evidence intake](pip-evidence-intake/SKILL.md) | Source retrieval, definitions, reconciliation and information cutoffs |
| [Company model](pip-company-model/SKILL.md) | Operating drivers and integrated financial models |
| [Financial quality](pip-financial-quality/SKILL.md) | Statement review, accounting questions, model audit and thesis validation |
| [Corporate governance](pip-corporate-governance/SKILL.md) | Ownership/control, minority rights, conduct, incentives, capital allocation and whether valuation discounts can persist |
| [Valuation and narrative analysis](pip-valuation-thesis/SKILL.md) | Conditional valuation, expectations, industry comparisons and historical attribution |
| [Investment conclusion](pip-investment-conclusion/SKILL.md) | Explicit Buy/Hold/Sell, target/date, downside/upside, pivotal insight and action conditions |
| [Theme screening](pip-theme-screening/SKILL.md) | Sourced candidate universes and value-chain exposure |
| [Macro event analysis](pip-macro-event-analysis/SKILL.md) | Regimes/shocks, transmission, sector appetite, investor access and realistic repricing |
| [Company change tracking](pip-company-change-tracking/SKILL.md) | Comparable evidence chains and targeted model revisions |
| [Research challenge](pip-research-challenge/SKILL.md) | Fact checks, counter-cases and unresolved blockers |
| [Management questions](pip-management-questions/SKILL.md) | Decision-sensitive issuer questions and answer tracking |
| [Research brief](pip-research-brief/SKILL.md) | Concise, sourced decisions and updates |
| [Chart visualization](pip-chart-visualization/SKILL.md) | AntV charts/diagrams, shared theme, financial-data encodings, rendering and export |
| [Monitor and review](pip-monitor-review/SKILL.md) | Review plans, change propagation and outcome evaluation |

## Handoffs and tools

Use the [earnings clock and peer read-through procedure](pip-company-model/references/earnings-clock-and-peer-readthrough.md) to relate latest-period results, subsequent-period expectations, earlier peer calls and upcoming catalysts to the research cutoff. [Provider retrieval](pip-evidence-intake/references/research-data-providers.md) supports bounded local AlphaPai, Alpha Vantage, API Ninjas and Massive requests for relevant fundamentals/expectations, market/actions/ownership, macro and meeting evidence, with explicit access/field limits. Current evidence and the earnings clock support whole-company judgment internally; no routine freshness block is required in investor briefs. AlphaPai originals are generally Chinese and are translated to the preferred language, English by default. The included adapter supplies the registered AlphaPai routes; the standalone company bundle contains fifteen skills.

Use the [shared handoff contract](pip-research-cycle/references/handoffs.md) for identity, sources, claims, dependency versions, checks and next actions. Numerical helpers are optional and have documented input assumptions. Their examples are synthetic; passing structural or arithmetic checks does not establish financial completeness, source truth or investment performance.

Keep sibling skill folders together so relative links resolve. Load only the relevant specialist and references. Local skill files do not register tools, supply source access, activate monitoring or authorise external actions.

## Repository checks

```powershell
npm.cmd run skills:check
npm.cmd test -- skills/tests
python -B -m unittest discover -s skills/tests -p "test_*.py"
```

The catalog describes research dependencies; it does not install a scheduler or execution service. See the root README for standalone setup and third-party notices.
