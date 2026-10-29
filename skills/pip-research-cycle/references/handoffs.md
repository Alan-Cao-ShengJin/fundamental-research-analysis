# Shared research handoffs

Every specialist should return a compact, versioned handoff. Reuse existing records rather than copying tables between documents. This is a research contract; it does not create execution authority.

## Common envelope

Use the JSON schema in [handoff.schema.json](handoff.schema.json) when a machine-readable handoff is needed:

- `id`, `kind`, `version`, `status`: stable identifier, artifact class, positive version and `complete`, `partial`, `blocked` or `not-applicable`.
- `mandateId`, `mandateVersion`, `scopeIds`: the mandate and instruments/entities this analysis actually covers.
- `asOf`, `producedAt`: information cutoff and generation time, with explicit offsets. Earlier publication/effective times remain on evidence records.
- `summary`: what was learned and its decision implication.
- `sources`: source id, location, locator, publication/availability/retrieval timestamps, access status and whether synthetic. Use null for genuinely unknown dates; unknown availability limits historical testing.
- `claims`: classification (`reported`, `derived`, `guidance`, `estimate`, `assumption`, `inference`), supporting source ids and, for derived numerical claims, a calculation/assumption record. Material unsupported claims remain explicitly uncertain.
- `dependencies`: upstream artifact id/version and whether its content changed since this output was produced. An affected downstream artifact is stale until recalculated/reviewed.
- `checks`: meaningful tests, their results and which failures block a candidate.
- `criticalUnknowns`: unresolved essentials that prevent a meaningful scoped conclusion or proposal, such as unusable identity, financial baseline or obligations. This field is a readiness blocker, not a list of every assumption or risk capable of changing the call. Keep ordinary forecast uncertainty, reasonable adverse cases and educated estimates in claims/rationales and referenced assumption/scenario records.
- `nextActions`: ranked task, action kind, completion condition and review/due time or observable trigger. For a proposed watch, distinguish `planned` from `active`; active requires a host acknowledgement.

`not-applicable` requires a reason. It does not mean a dependency silently passed. `complete` means this artifact's scoped research is complete, not that a candidate is approved or live monitoring works.

A blocking check tests an essential condition or whether required analysis was performed correctly. Do not define investment readiness as every scenario having a positive return. A well-supported forecast assumption can remain uncertain in a complete artifact; label it as an assumption/inference with its rationale instead of presenting it as an unsourced reported fact. A source gap blocks reliance on a claim attributed to that source, not all independent estimates or research.

For governance/red-flag work, reference one issue register with stable issue IDs, owner, priority, evidence/confidence, affected periods/accounts, benign alternatives, checks performed, bounded model effects, next verification and disposition. The financial-quality early screen, model audit and thesis validation have distinct artifact IDs/versions referencing that register. Completion means the scoped review was performed, not absence of risk. Put only missing essentials preventing a meaningful conclusion in `criticalUnknowns`; keep ordinary flags and scenarios in claims/referenced records. No additional envelope fields or automated fraud detector are implied.

## Evidence and numerical identity

Keep these fields with observations when relevant: entity/contract id; metric definition; value; currency; scale; period start/end or snapshot time; stock/flow/per-share type; consolidated/parent and reported/adjusted basis; segment coverage; restatement vintage; source locator. Store raw observations separately from normalised or derived data.

An arithmetic identity does not identify which source value is wrong. Record a residual and investigate scope, definitions, timing, rounding and missing categories. Do not alter source values to obtain a zero check. Two notes from the same call or two feeds republishing one filing are not independent confirmations.

Forecast assumptions cite their basis and uncertainty. A management target is guidance, not an observed actual or a forecast that must be hit. Historical quarterly derivations remain traceable even if a workbook displays hard values as actuals.

For earnings/event work, reference the [earnings clock](../../pip-company-model/references/earnings-clock-and-peer-readthrough.md): fiscal periods, release/call/availability timestamps, elapsed time, pre-event expectations, peer read-throughs and next dates with confirmed/estimated status. These belong in the referenced evidence/model record rather than undeclared envelope fields. A retrieved transcript can be ASR, a generated note or an original call; source type and access/field limits remain explicit.

## Stage-specific artifacts

| Kind | Required substantive content |
| --- | --- |
| `research-brief` | Decision, horizon/deadline, mandate, capital scope, baseline, capabilities and budget |
| `evidence-pack` | Source register, reconciled observations, conflicts and freshness/coverage gaps |
| `hypothesis` | Economic return source, baseline, support/counterevidence and falsifiable failure conditions |
| `company-model` | Executable model/backend reference and fingerprint, scenario/run, semantic period/metric/unit map, current calculated outputs and lineage, statement/driver maps, assumptions, checks, frozen forecasts and downstream valuation dependencies |
| `financial-quality` | Earnings-to-cash, balance-sheet and financing bridges, material anomalies, alternatives and follow-up tests |
| `corporate-governance` | Control/rights, dated conduct and shareholder events, allocation/incentives, issue-level evidence/confidence, model/value consequences, discount-persistence and credible improvement cases |
| `valuation-thesis` | Method/basis, governance consequences, present intrinsic value versus attainable target/date, scenarios, sensitivities, expectations gap and invalidation |
| `investment-conclusion` | Current model/governance/valuation/validation references; Buy/Hold/Sell, primary target/date and calculated signed return; same-horizon bear/bull risks; business/moat, pivotal insight, catalysts and invalidation |
| `challenge` | Strongest counter-case, reproduced key calculations and unresolved blockers |
| `management-questions` | Unresolved decision-sensitive questions, available facts already checked and answer-to-model implications |
| `brief` | What changed, evidence, implications, uncertainty, proposed action and next task |
| `monitor-review` | Watch specifications/activation status, health, due times, material changes and attribution |

Before calling a candidate decision-ready: require relevant current upstream artifacts, source support for material factual/attributed claims, reasoned assumptions, passed blocking checks, resolution of essential blockers and freshness compatible with the task. Apply the [underwriting standard](underwriting-standard.md) to ordinary uncertainty. These checks do not establish suitability or profit; actual portfolio execution additionally needs the host's applicable account/risk/approval checks.

Company setup, actuals, operating data, revenue projection, cost/unit economics and integrated forecasts use separate IDs even though their kind can be company-model. The primary interface is the [executable agent model](../../pip-company-model/references/agent-model.md), not a human-readable table. Store the larger model package/calculation runs separately and reference them through evidence/dependency locations in the existing handoff envelope; do not add undocumented fields to the strict handoff schema. A workbook backend additionally records file/baseline, semantic cell bindings, preservation and recalculation status. Likewise, model audit and post-valuation thesis validation use separate financial-quality IDs. A valuation-thesis is provisional; the investment-conclusion comes after validation/challenge. Portfolio proposals are a further downstream artifact, not another name for a company research conclusion.

Governance has its own artifact and dependency version. A changed control/right, related-party exposure, capital-allocation policy or credibility finding invalidates affected model, valuation and conclusion claims. Refer to the [decision contract](../../pip-investment-conclusion/references/decision-contract.md) for the referenced stock decision record and return formulas. The envelope remains strict; the contract does not silently add fields to it. A past completed report is a dated artifact, not evidence that a new governance review has been performed.

Valuations and reviews bind to the model version/fingerprint, engine version, scenario/run, selected output IDs and their own market-data cutoff. A model change makes dependent evaluations stale; recompute and recheck them before presenting a current conclusion. Preserve earlier forecasts and decisions for evaluation against later matched actuals. A package that passes graph arithmetic is not automatically financially complete or decision-ready.

If a source or necessary tool is unavailable, return a useful partial handoff and a concrete next task. Do not fabricate a successful download, recalculation, broker comparison, market fill or alert activation.
