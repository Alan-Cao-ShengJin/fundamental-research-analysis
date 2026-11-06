# Company research sequence and stage gates

This is the single statement of the stages that establish new coverage. [Request routing](request-routing.md) decides whether a task is an initiation or an update, and which stages an update reopens. Build an executable financial model before valuation, assess whether governance lets outside shareholders realise its value, use calculated outputs and governance findings to form and test an expectations gap, then reach an investment conclusion. Portfolio implementation is a downstream extension.

| # | Stage | Specialist | Required result |
| --- | --- | --- | --- |
| 1 | Scope, evidence and the debate | Research cycle; [evidence intake](../../evidence-intake/SKILL.md); proportionate [market context](../../macro-event-analysis/references/market-regime-and-investor-base.md) | Question, rated security, cutoff, sources, reporting basis, where the company sells (region, channel, largest customers), a dated [world-state record](world-state.md) with its decision-changing developments worked through, market context, investability gaps, [what the market is trading](what-the-market-trades.md) (the variable and period that set the price, the figure the price implies and the market's current reading against ours), and the two or three contested questions the stock turns on, with the strongest case on each side |
| 2 | Model setup | [Company model](../../company-model/SKILL.md), setup | Versioned model state, semantic metric/period/unit map and workbook bindings |
| 3 | Historical statements | Company model, actuals | Reconciled income statements, balance sheets and cash flows with supported interim derivations |
| 4 | Corporate governance | [Corporate governance](../../corporate-governance/SKILL.md) | Ownership/control and minority rights; conduct, incentives, capital allocation and disclosure; quantified or bounded model effects; discount-persistence case |
| 5 | Financial red flags | [Financial quality](../../financial-quality/SKILL.md), early screen | Reporting/cash/asset/financing findings with severity and confidence, benign alternatives, usable baseline and essential unresolved inputs |
| 6 | Industry analysis | [Industry analysis](../../industry-analysis/SKILL.md) | Market definition and value chain; industry growth, competitive niche, barrier trend, upstream costs and downstream behaviour, each mapped to the model input, multiple or indicator it changes |
| 7 | Operating data | Company model, drivers | Segment/driver history, reconciled observations and competitor/customer/supplier response evidence |
| 8 | Guidance | Company model, guidance | Latest-period and next-period expectations, dated attributed wording, peer read-throughs and caveats |
| 9 | Revenue projection | Company model, revenue/unit economics | Demand, volume, price/mix and recognition drivers linked to group revenue at the supported cadence |
| 10 | Costs and unit economics | Company model, cost build | Matched cost bases, margins, unit contribution and segment/group reconciliation |
| 11 | Integrated forecast | Company model, statements | Linked earnings, working capital, productive assets, financing, cash and balance sheet; funded growth and marginal-return estimates |
| 12 | Model audit | Financial quality, model audit | Current calculation run, pivotal source/calculation checks, assumption tests, liquidity checks, consensus-gap decomposition and blockers |
| 13 | Valuation and expectations | [Valuation thesis](../../valuation-thesis/SKILL.md) | Economic value and realisable target scenarios under current governance, sensitivities and the provisional expectations gap |
| 14 | Thesis validation and challenge | Financial quality, validation; [research challenge](../../research-challenge/SKILL.md) | Support/refutation, whether cheapness can persist, the strongest counter-case, and whether the stated reasons for the call are the drivers the target depends on |
| 15 | Conviction | [Investment conviction](../../investment-conviction/SKILL.md) | Decisive proposition, supporting/contrary evidence, milestones, exclusion and reconsideration conditions |
| 16 | Conclusion | [Investment conclusion](../../investment-conclusion/SKILL.md) | Buy/Hold/Sell, primary target/date, price return, dividend yield shown separately, bear/bull cases, pivotal insight and invalidation |
| 17 | Communication and follow-up | [Research brief](../../research-brief/SKILL.md); [monitor review](../../monitor-review/SKILL.md) | World state, price and consensus [refreshed to the release cutoff](world-state.md#8-refresh-at-the-cutoff); stock pitch and sourced decision block; unresolved questions, lessons and next review |

[Issuer questions](../../issuer-questions/SKILL.md) branch from a material gap at any stage; available evidence can often answer them without contact.

## Dependency rules

The table expresses dependencies, not fixed analytical weights; apply the [materiality principle](underwriting-standard.md#integrate-the-analysis-by-materiality). Market context, governance and operating evidence can develop together. The stage-1 debate sets the modelling agenda: build the drivers the stock turns on in quarterly or half-year detail, and keep the rest at the level the decision needs. Frame the debate as informed investors argue it, not only as a gap to consensus numbers: start from [what the market is trading](what-the-market-trades.md), which can be a year beyond the forward year or an asset outside current earnings, and build the model through that year or around that asset. The questions that split them often decide whether growth is a temporary window or a durable shift: whether the technology works at scale, how far costs can fall, whether it changes how customers buy. Company and sell-side material often understates these questions, so look for them in technical evidence, long and short theses, expert and channel commentary, customers and competitors, and treat context the user supplies as leads.

At the end of stage 14, independently challenge the thesis, the three load-bearing assumptions and their ranges, and the strongest counter-case before concluding. The analyst owns those judgments; do not ask the user to choose forecasts, valuation inputs or the call. Invite user challenge when they request a collaborative review, and ask only for missing user intent or constraints that cannot reasonably be inferred. Record whether external challenge actually occurred without making it a completion requirement.

Actuals define the baseline; the governance review and red-flag screen (stages 4 and 5) test whether it can be relied on. **At initiation, complete both before building forecasts.** Governance collection can start during intake, and a focused review can use filings directly. Deepen material issues during model audit and revisit the discount-persistence case after valuation. For existing coverage, carry known findings into the inputs and reopen the screens only when new evidence raises an issue. Post-valuation validation tests priced expectations rather than repeating the audit.

Valuation consumes the current calculated model outputs with their model/run identity; preserve frozen forecasts for later matched-actual evaluation. A price or discount-rate change can refresh valuation without rebuilding unchanged operating assumptions. A material change at any stage reopens the affected forecast, audit, valuation and conclusion.

Industry analysis (stage 6) can start with evidence intake and must be finished before the revenue and cost projections: it sets or tests market growth, share, price, input costs and how long margins last, so forecasts do not simply extend the company's own history. Anchor near-term analysis on the latest reported period, its call and peers already reported; keep the [earnings clock](../../company-model/references/earnings-clock-and-peer-readthrough.md) in the research record, not the brief. Apply [competition and capital returns](../../company-model/references/competition-and-capital-returns.md) in projections and valuation, and [empirical validation](empirical-research-and-validation.md) in evidence, challenge and later review.

Focused requests reuse valid upstream work. A standalone statement question does not require a full model or valuation; a full investment conclusion requires the construction and validation stages. [Model revision](../../model-revision/SKILL.md) reruns affected stages in dependency order and does not create new versions of unaffected stages.

## Readiness gates

Apply the [underwriting standard](underwriting-standard.md) and [investor judgment](investor-judgment.md). A source ID and a successful calculation do not establish economic support; a scenario that reverses the call does not prevent a recommendation. Proceed on a defensible central estimate with stated risks.

- **Model-ready:** governance and red-flag review identify a usable baseline, bounded risks and essential unresolved dependencies; model identity and semantic definitions exist; actuals, drivers, governance inputs and guidance availability are reconciled or explicitly qualified.
- **Valuation-ready:** a current revenue/cost projection feeds integrated statements and material schedules; governance-related cash access, dilution and financing effects are modelled or bounded; inputs come from a calculated run with lineage; the workbook records recalculation and preservation status.
- **Conclusion-ready:** current valuation, governance, targeted validation and counter-case support a defensible central target; revisions have propagated. Apply the [decision contract](../../investment-conclusion/references/decision-contract.md).

A completed review may contain adverse findings; completion does not certify clean accounts. Where evidence is incomplete, make the call on the financials available; do not use Hold as a placeholder.

## Optional implementation

Investment conclusion, then instrument/strategy design, cost and adverse-execution testing, implementation challenge, portfolio sizing, any separately authorised action, and monitoring. An underlying valuation is not itself a trade return or portfolio weight. See [workflow.md](workflow.md#optional-downstream-implementation-and-other-assets).
