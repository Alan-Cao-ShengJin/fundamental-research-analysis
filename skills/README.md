# Investment research skills

Use [research-cycle](research-cycle/SKILL.md) for end-to-end work, or select a specialist for a focused request. Instructions are in English and apply across issuers and markets. Adapt the analysis and output language to an explicit user request.

Investment briefs follow the [one-page house format](research-brief/references/one-page-brief.md): selective decision-useful content, flexible headings and the shared issuer-neutral minimalist template, an institutional editorial review and one verified A4 page. Each substantive point follows [data, derivation, significance and stock-view implication](research-brief/references/natural-writing.md#argument-sequence) in connected prose. The full investment report remains separate. Reusable payload/render/check assets live with research-brief; formatting changes preserve the current model and decision.

The governing [request routing](research-cycle/references/request-routing.md) distinguishes **new initiation** from **existing research updates**. Initiation establishes the full baseline and initial view with relevant sector guidance. Existing updates use [model revision](model-revision/SKILL.md) in **regular-review mode**, retaining operating forecasts unless concrete evidence supports a change, or **major earnings/catalyst mode**, evaluating prior assumptions against disclosures before recalibrating forecasts. The two workflow entry skills are `stock-initiation` and `model-revision`. The catalog flows `company-regular-review` and `company-update` describe the regular and major branches of model-revision, alongside seventeen analytical and presentation specialists. Both retain shared modeling, risk and decision standards; cadence alone does not select a mode.

## Sequence and skills

This bundle holds the instructions, references and helper scripts for equity research: initiating coverage, updating existing coverage and the specialist analysis both rely on. [Research cycle](research-cycle/SKILL.md) owns scope, routing and the reading path. The [company sequence](research-cycle/references/company-sequence.md) is the single statement of the stages, their dependencies and readiness gates.

| Skill | Use for |
| --- | --- |
| [Stock initiation](stock-initiation/SKILL.md) | Establish first coverage or a fresh stock investment case |
| [Model revision](model-revision/SKILL.md) | Assess new evidence against a frozen model and update affected forecasts, cash and decisions |
| [Investment conviction](investment-conviction/SKILL.md) | Preserve a decisive economic or avoidance belief, test it against evidence and retain reconsideration conditions across reviews |
| [Research cycle](research-cycle/SKILL.md) | Scope, routing, dependencies and follow-up |
| [Evidence intake](evidence-intake/SKILL.md) | Source retrieval, definitions, reconciliation and information cutoffs |
| [Company model](company-model/SKILL.md) | Operating drivers and integrated financial models |
| [Financial quality](financial-quality/SKILL.md) | Statement review, accounting questions, model audit and thesis validation |
| [Industry analysis](industry-analysis/SKILL.md) | Industry growth, competitive niche, barrier trends, upstream costs and downstream behaviour, turned into forecast assumptions, multiples and indicators |
| [Corporate governance](corporate-governance/SKILL.md) | Ownership/control, minority rights, conduct, incentives, capital allocation and whether valuation discounts can persist |
| [Valuation and narrative analysis](valuation-thesis/SKILL.md) | Conditional valuation, expectations, industry comparisons and historical attribution |
| [Investment conclusion](investment-conclusion/SKILL.md) | Explicit Buy/Hold/Sell, target/date, downside/upside, pivotal insight and action conditions |
| [Fundamental/theme screening](theme-screening/SKILL.md) | Financial screens, comparable peer triage, value-chain exposure and prioritized research questions |
| [Macro event analysis](macro-event-analysis/SKILL.md) | Regimes/shocks, transmission, sector appetite, investor access and realistic repricing |
| [Company change tracking](company-change-tracking/SKILL.md) | Comparable evidence chains and targeted model revisions |
| [Research challenge](research-challenge/SKILL.md) | Fact checks, counter-cases and unresolved blockers |
| [Management questions](issuer-questions/SKILL.md) | Decision-sensitive issuer questions and answer tracking |
| [Research brief](research-brief/SKILL.md) | Concise, sourced decisions and updates |
| [Chart visualization](chart-visualization/SKILL.md) | AntV charts/diagrams, shared theme, financial-data encodings, rendering and export |
| [Report layout](report-layout/SKILL.md) | House page, decision strip, sections, captions, charts and PDF printing for full reports |

## Coverage and scope

Account for all bundled roles with the [coverage plan](research-cycle/references/research-coverage.md). Required work may reference eligible dated artifacts; conditional work needs an explicit applicability decision. Portfolio allocation, risk budgeting, strategy testing and non-company underwriting are [external workflows](research-cycle/references/scope-boundary.md). No scheduler or monitoring service is supplied.

## Handoffs and tools

Use the [earnings clock and peer read-through procedure](company-model/references/earnings-clock-and-peer-readthrough.md) to relate latest-period results, subsequent-period expectations, earlier peer calls and upcoming catalysts to the research cutoff. [Provider retrieval](evidence-intake/references/research-data-providers.md) supports bounded requests to the configured data providers for fundamentals/expectations, market/actions/ownership, macro and meeting evidence, with explicit access/field limits. Non-English originals are retained and translated to the requested output language, English by default. The methodology has seventeen analytical and presentation specialists, with initiation and revision as two workflow entry skills.

Use the [shared handoff contract](research-cycle/references/handoffs.md) for identity, sources, claims, dependency versions, checks and next actions. Numerical helpers are optional and have documented input assumptions. Their examples are synthetic; passing structural or arithmetic checks does not establish financial completeness, source truth or investment performance.

Keep sibling skill folders together so relative links resolve. Load only the relevant specialist and references. Local skill files do not register tools, supply source access, activate monitoring or authorise external actions.

## Repository checks

```powershell
npm.cmd run skills:check
npx.cmd vitest run skills/tests
python -B -m unittest discover -s skills/tests
```

The catalog describes local skills and routes; live runtime integration remains separate. Required third-party licence notices are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Full-report publication follows [frozen drafts, fresh review and bounded correction](report-layout/references/publication-review.md). The catalog separates draft rendering, draft review and publication in initiation, regular-review and major-update routes. The package path enforces review records and defined financial bindings. Historical integrity-only checks explicitly use `--legacy` and do not establish a current reviewed release.
