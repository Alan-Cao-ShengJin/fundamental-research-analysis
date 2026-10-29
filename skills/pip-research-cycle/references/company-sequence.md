# Company research sequence and stage gates

Build an executable financial model before valuation and assess whether governance allows outside shareholders to realise its value. Use calculated outputs and governance findings to form and test an expectations gap, then reach an investment conclusion. Portfolio implementation is a downstream extension.

| Stage | Specialist | Required result |
| --- | --- | --- |
| Scope and evidence | Research cycle; evidence intake; macro context | Question, cutoff, sources, reporting basis, current macro/sector/themes, credible stock association and material supporting investability findings/gaps |
| Model setup | Company model | Versioned backend, semantic metric/period/unit map and dependencies |
| Historical statements | Company model | Reconciled income statements, balance sheets and cash flows with supported interim derivations |
| Corporate governance | Corporate governance | Ownership/control and minority rights; conduct, incentives, capital allocation and disclosure; quantified or bounded model effects and discount-persistence case |
| Financial red flags | Financial quality - early screen | Account/cash/reliability findings with severity and confidence, benign alternatives, usable baseline, linked governance issues and essential unresolved inputs |
| Operating data | Company model | Defined segment/driver history, reconciled observations and material competitor/customer/supplier response evidence |
| Guidance assessment | Company model | Latest-period/call and next-period expectations, dated wording/Q&A, comparable earlier peer evidence, caveats and source/coverage limits |
| Revenue projection | Company model | Supported demand, volume, price/mix and recognition drivers linked to group revenue |
| Costs and unit economics | Company model | Matched cost bases, margins, unit contribution and segment/group reconciliation |
| Integrated forecast | Company model | Linked earnings, working capital, productive assets, financing, cash and balance sheet; funded growth and defined marginal-return estimates |
| Model audit | Financial quality | Current calculation run, pivotal source/calculation checks, assumption tests, liquidity checks and material blockers |
| Valuation and expectations | Valuation thesis | Conditional values and attainable targets, governance, advantage duration/fade, reinvestment, investor-demand/recognition mechanism, sensitivities and provisional expectations gap |
| Thesis validation and challenge | Financial quality; research challenge | Support/refutation, competitive response, historical/failed analogues, persistent neglect/crowding, buyer-capacity/supply tests, counter-case and actual review findings |
| Investment conclusion | Investment conclusion | Buy/Hold/Sell, primary target/date and return, same-horizon bear/bull risks, pivotal insight, catalysts and invalidation |
| Communication | Research brief | Short visual report, concise sourced decision block, natural prose, clear business/moat and linked analytical support |

Read the [model-building skill](../../pip-company-model/SKILL.md) for detailed construction. [Management questions](../../pip-management-questions/SKILL.md) branch from material gaps at any stage. Available evidence can resolve a question without issuer contact.

## Dependency rules

Use the [earnings/catalyst clock](../../pip-company-model/references/earnings-clock-and-peer-readthrough.md) to establish elapsed time since results/call, the next forecast/reporting period, comparable peer release order and confirmed versus estimated future events. Preserve pre-event expectations and publication cutoffs. Latest actuals and the next outlook anchor near-term analysis; older periods calibrate seasonality, cycles and credibility without overriding the shared materiality principle.

Include [market context and narratives](../../pip-macro-event-analysis/references/market-regime-and-investor-base.md) during intake and when testing attainable targets, with importance determined by the shared [materiality principle](underwriting-standard.md#integrate-the-analysis-by-materiality). It complements operating economics, financial quality, governance, valuation and payoff; neither topical narratives nor investor demand automatically take precedence. A context or investability change can reopen market-price valuation without changing operating forecasts. A standalone macro deep dive and detailed buyer map remain conditional on the task.

Use [competition and capital returns](../../pip-company-model/references/competition-and-capital-returns.md) across operating projections and valuation, and [empirical research and validation](empirical-research-and-validation.md) across evidence, challenge and later review. Historical comparisons and source checks are supporting records, not extra reports or an obligation to obtain perfect information. Keep planned procedures separate from completed work.

Actuals define the baseline; early governance and [financial-red-flag review](../../pip-financial-quality/references/financial-red-flags.md) test whether it can be relied upon. Complete these initial risk assessments before forecasts; operating data, guidance and bounded risk consequences then inform projections. Governance collection can start during intake, and a focused review can use filings directly without building a full model. Complete the material governance review before the company model audit/valuation and revisit its persistent-discount or improvement case after valuation. Post-valuation validation tests priced expectations rather than repeating the audit. A material change reopens the affected forecast, audit, valuation and conclusion.

Valuation consumes current [model outputs](../../pip-company-model/references/agent-model.md) with model/engine version, fingerprint and scenario/run identity. Preserve frozen forecasts for later matched-actual evaluation. A price or discount-rate change can refresh valuation without rebuilding unchanged operating assumptions.

Focused requests reuse valid upstream work. A standalone statement question does not require a full model or valuation; a full company investment conclusion requires the relevant construction and validation stages.

## Readiness gates

Apply the shared [underwriting standard](underwriting-standard.md) and [investor judgment](investor-judgment.md) across these gates. Retain assumption/evidence records, source-specific credibility assessments, return asymmetry and plausible adverse cases. A source ID and a successful calculation do not establish economic support, but uncertainty or a scenario reversing the call does not automatically prevent a recommendation. Proceed with a defensible central estimate and stated risks; keep research incomplete when missing essentials make meaningful valuation or the call arbitrary.

- **Model-ready:** early governance/red-flag review identifies a usable baseline, bounded risks and essential unresolved dependencies; it need not conclude that the company is risk-free. Model identity/backend and semantic definitions exist; actuals, drivers, governance inputs and guidance availability are reconciled or explicitly qualified. Missing inputs remain visible.
- **Valuation-ready:** a current revenue/cost projection feeds integrated statements and material schedules; governance-related cash access, allocation, dilution and financing effects are modelled or explicitly bounded. Scenarios and blocking checks have been reviewed. Inputs come from a calculated run with lineage. A workbook backend records recalculation and preservation status.
- **Conclusion-ready:** valuation, governance realisation/discount persistence, targeted validation and a substantive counter-case are current. Material revisions have propagated. A completed stock call meets the [decision contract](../../pip-investment-conclusion/references/decision-contract.md), including one Buy/Hold/Sell label and primary target/date with comparable downside/upside risks. Hold is mandatory when primary-target price return is within -10% to +10%, inclusive; apply the contract before rounding the displayed percentage.

The early red-flag screen, model audit and thesis validation use the same financial-quality skill with distinct pass IDs/versions and a shared issue register. A completed review can contain adverse findings; completion does not certify clean accounts or an attractive investment. Severe minority-rights concerns are high-priority red flags. Material reporting or solvency issues can also be decisive. Do not average them away in a score, infer fraud from a ratio, or make all imperfect disclosure a research blocker. A critical new finding reopens affected work at any stage.

Arithmetic success alone does not satisfy these gates. Where essential evidence is unavailable, return explicitly incomplete research and the next useful investigation; do not invent a target or use Hold as a completed stock rating. Research status and downstream portfolio no-action decisions are separate.

## Research follow-up

Preserve decision and model versions for subsequent review. New evidence reopens the affected research stage; monitoring remains proposed until an actual service acknowledges it. Portfolio sizing and implementation are separate from a company stock call.
