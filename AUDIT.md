# Research skill verification - 13 November 2026, version 3.0.0

This release publishes the reworked research sequence. Earlier audit sections keep their original dates, scope and results.

## What changed

- **Valuation:** one six-step sequence. Name the kind of company and the yardstick buy-side investors value it on; read today's price on that yardstick; set the target level; apply it to our own numbers; build the bear and bull cases; give one target and the rating. A new yardstick list covers economic profiles, sectors with their own convention, how each yardstick is measured and when the market switches from one to another. Consensus enters at three named points and never while the forecast is being built.
- **Revenue drivers:** a fixed order for setting each base-case driver, from a specific supported number down to GDP-level growth as the last resort.
- **Sector cards:** 100 cards in one shape replace 21 broader guides. Each card covers what is sold and who decides demand, the driver tree with a fallback for missing data, the data behind the rows, costs and margin, capacity and working capital, the cycle and its traps, what investors argue about with the yardstick, and a worked example in invented figures. A card is a guide: each business unit takes its own card, and a business no card fits is modelled from first principles.
- **Debates:** written as why the question is live, what the bears say, what the bulls say, our view, what the share is worth either way and what settles it. The claims table is gone, and no debate is printed where investors are not arguing.
- **Writing:** the writing standard now teaches by before-and-after examples; the separate detail file is deleted.
- **Follow-up:** the monitor-and-review skill is folded into company change tracking and a short follow-up guide. The routing files now state the research-only scope directly.

## Executed verification

| Check | Result |
| --- | --- |
| Workspace | 263 Python tests, 66 JavaScript tests, all 19 skill validations and 1243 relative links passed |
| Public export | 272 Python tests, 66 JavaScript tests, all 19 skill validations and 1332 relative links passed |
| Sample model | The unchanged synthetic workbook still reproduces its specification |
| Sector cards | Every card has the same eight headings, one index row, intact tables and working links; the arithmetic of all 100 worked examples was recomputed in review |
| Scope | Private research, source packs and credentials excluded; private-path and token pattern checks passed |

## How the sector cards were checked

Each of the 100 cards was read once by a fresh reader that saw only the card and laid out a model for a real company of that kind. The findings were applied, and cards that mixed unlike businesses were split. Six cards rewritten after their read were read a second time.

## Limits

This release was not validated by a fresh end-to-end research run, a PDF print or a native Excel recalculation, so the effect of the new sequence on report quality is untested. On the sector cards: corrections made after a card's read were not read again; statements about costs, margins and named data sources rest on those reads and on general knowledge and were not audited source by source; and 113 fallbacks for missing guidance, added on 13 November, have not been read independently. The yardstick list records market conventions to start from, which each study confirms for its own stock. The worked numbers in the cards are invented and are not machine-tested.

---

# Research skill verification - 11 November 2026, version 2.13.0

This release applies the owner's decisions on the items left open in 2.12.1 and removes unused material. Earlier audit sections keep their original dates, scope and results.

## What changed

- **Cost of equity:** one method, the 10-year government yield plus the equity premium implied by the market's own index at the research date, with a country premium only where index inputs are missing and at most one point of company adjustment. A solver and its tests are added. The method follows Damodaran's implied premium and the implied-cost-of-capital literature cited in the reference.
- **Consensus:** forecasts are built independently of consensus; material differences are explained and a large unexplained gap is treated as a sign of error.
- **Scenarios:** probabilities are optional; the base case is the set of numbers the analysis believes in most.
- **New-money judgment removed:** attractiveness tiers, the new-money line and entry prices are gone from the decision contract, the brief renderer, the release check, templates, evaluation cases and tests. The rating rule is unchanged.
- **Total return:** may be shown, labelled, where the dividend is a real part of the holder's return; it stays out of the rating and the target.
- **Smaller bundle:** the unused forecast scaffold and node-graph tooling, an unrunnable layout checker, an unread inventory file and repeated statements of the same rule were deleted. The public README was rewritten in plain language.

## Executed verification

| Check | Result |
| --- | --- |
| Workspace | 271 Python tests, 65 JavaScript tests, all 23 skill validations and 743 relative links passed |
| Public export | 272 Python tests, 65 JavaScript tests, all 20 skill validations and 838 relative links passed |
| Sample model | The unchanged synthetic workbook still reproduces its specification |
| Scope | No public adaptation line was lost in the export; private research, source packs and credentials excluded; private-path and token pattern checks passed |

Test counts are lower than in 2.12.1 because the tests of the deleted tooling and of the retired new-money concept were removed with them; three tests of the new solver and one of the retained model tracer were added. No test of the rating, target, price return or dividend yield was weakened.

## Limits

No fresh research run, PDF print or native Excel recalculation was performed for this release, so the effect of the rule changes on report quality is untested. The implied-premium solver checks arithmetic only; choosing the index and retrieving its dated inputs remain analyst work. The worked numbers in the sector guides are no longer machine-tested, because the test covered the deleted example file rather than the prose. The sample model still shows a total return row.

---

# Research skill verification - 11 November 2026, version 2.12.1

This is a correction release after a clean review. Earlier audit sections keep their original dates, scope and results.

## What was reviewed and changed

Five independent readers each read one area in full without editing: sequence and routing; modelling and company analysis; valuation, decision and challenge; writing, layout and publication instructions; and the harness code, where the reader also reproduced defects on temporary fixtures. The author then checked each finding against the files and applied the confirmed ones.

- Sequence: the initiation trigger, the update order, the stage owners and the fresh model challenge on updates now agree between routing, the sequence table and the entry skills; the research record handed to the writer is defined.
- Valuation and decision: the rerating test no longer demands a catalyst for a return to the stock's own mean; discounted-cash-flow cross-checks stay out of the write-up; bond spreads and analyst-assumed yields no longer offer a route around comparable income investments for steady dividend payers; text left from an earlier product was removed.
- Modelling: the builder accepts blank text cells, names the cell and the fix in its errors, and records source tags passed to period rows; the standard no longer describes a second model backend or claims the sample holds every required feature.
- Writing and publication: passages that forced method narration, default hedging and figure-heavy paragraphs were deleted; the publication reference states the identifier rule, the reader's completion conditions, the route for a correction after the review budget is used, and no longer carries its own design history.
- Harness: file names instead of print-time links; pinned-rule check before a release archive is replaced; clearer runtime, identifier and rating-binding messages; consistent reading of reader-edited files; named failures for unreadable dates; lock files excluded from reviewed inputs; duplicate check names rejected; price tolerance scaled to the share price; rating tested on the reproduced target.

## Executed verification

| Check | Result |
| --- | --- |
| Workspace | 297 Python tests, 73 JavaScript tests, all 23 skill validations and 791 relative links passed |
| Public export | 298 Python tests, 73 JavaScript tests, all 20 skill validations and 878 relative links passed |
| Sample model | The unchanged synthetic workbook still reproduces its specification under the corrected builder |
| Scope | Each exported file matched its pre-review public counterpart apart from notices and scope links before it was replaced; private research, source packs and credentials excluded; private-path and token pattern checks passed |

## Limits

No fresh research run, PDF print or native Excel recalculation was performed for this release, so the effect of the instruction changes on report quality is untested. One existing test assertion was updated because it asserted the link that caused the path leak. A proposed check of the dividend yield quoted in a brief's key metrics was not added: its formatting rule conflicted with existing fixtures.

Known items left for the owner: the sample model still shows a combined price-plus-dividend return row; an unused single-sheet model scaffold and a brief layout checker that cannot run remain in the bundle; the cost-of-equity guidance allows both an additive and a beta build; several rules are still restated in more than one file.

---

# Research skill verification - 11 November 2026, version 2.12.0

This release locks the updated instructions into a public versioned snapshot. Earlier audit sections retain their original dates, scope and results.

## Changes reviewed and included

- Steady dividend payers use accessible, economically comparable income investments to calibrate the primary required yield. The peer universe follows relevant income investors rather than industry labels alone. Relevant own-yield history is the fallback; unavailable or inapplicable history remains a gap. This is a house mandate for that branch, not a universal valuation law. Cost of equity minus growth and P/E restatements do not silently become its target anchor.
- Market-expectations analysis examines the available dated valuation path, highs/lows and largest swings before describing stability or rerating. Sample coverage and missing estimate vintages remain explicit.
- A contradiction needs incompatible evidence on the same proposition and period. No announcement alone leaves a future action untested. Cash that funds a shortfall does not guarantee an uncut dividend.
- Research writing favors concise, plain, precise explanations, business economics before detailed valuation and one main home per argument. Synthetic writing examples supply the facts they use; editorial improvements cannot create peer/customer evidence or a uniquely observed market belief.
- Autonomous required-return selection remains part of the analyst workflow for appropriate uses. Users need not pick rates. Numerical interfaces and validation checks remain explicit and reproducible.

Before export, narrow consistency fixes aligned the older DDM instruction with the new steady-payer target policy, clarified the missing-history fallback and the meaning of an unannounced action, preserved path-coverage limitations, and removed an unsupported output/market-belief inference from a writing example. Owning skill patch versions were updated. No numerical helper, review budget, financial schema or research stage changed.

## Executed verification

| Check | Result |
| --- | --- |
| Workspace | 297 Python tests, 73 JavaScript tests, all 23 skill validations and 793 relative links passed |
| Public export | 298 Python tests, 73 JavaScript tests, all 20 skill validations and 880 relative links passed |
| Public structure | 20 skills, 11 research flows and 21 sector guides; shared schema and coverage checks passed |
| Skill snapshot | Local content inventory captured and rechecked for changes during validation; public snapshot is identified by its canonical Git manifest and release tag |
| Scope and provenance | Public scope adaptations and original attribution retained; private research, source packs and credentials excluded; bounded private-path/token pattern checks passed |
| Synthetic workbook | Existing cleaned example retained and rechecked during manifest preparation; no issuer workbook was revised |

The public Python count differs because its coverage-planner tests are included while private portfolio-risk tests are excluded. No new deterministic test is claimed for prose changes; existing suites verify the supported mechanics and structure. Frozen issuer studies, source bytes and review budgets were not changed.

## Limits and adoption

No fresh research run, semantic-transfer evaluation, live provider check, new PDF rendering or native Excel recalculation was performed for this release. Clear instructions and passing arithmetic tests do not establish source truth, correct calibration or reviewer independence. The host must launch the required contexts and analysts must perform the work.

The local message-board comparison proposals are not all represented as completed repairs. This snapshot includes the actual updated guidance and consistency fixes above; it does not claim new historical-line reconciliation automation, scenario/target verification code or translation testing. Subsequent behavioral trials should assess the pinned version and retain material errors and false blocks honestly.

New studies pin these production files. Existing frozen studies keep their archived version, findings and attempts under [migration](MIGRATION.md). The company-research scope, current-forward target convention and rating/attractiveness thresholds remain in force.

---

# Research skill verification - 10 November 2026, version 2.11.1

This section records the calibration update. Earlier release records remain below.

Main-branch clarification after v2.11.1: the analyst system autonomously retrieves and calibrates required-return inputs; explicit calculator parameters do not require user selection. Added a dated rate-selection reference, source routing and a host-only behavioral case. Numerical helper logic is unchanged. This instruction update has not been established by a fresh research run; historical verification below retains its original scope.

## Changes

- A central forecast follows the evidence without an automatic pessimistic or optimistic bias. Supported execution risks remain in base; joint scenarios do not combine every independent worst or best endpoint. Material asymmetric outcomes distinguish most likely from expected value.
- Scenario coverage extends to cash flow, funding, dilution and asset value as well as EPS and dividends. One authoritative input feeds the scenario and local calculations; pivotal values and rationale remain visible locally. Justified invariants are allowed.
- Dividend valuation compares economically relevant yield investments where available, retaining justified alternatives when peers are weak. Yield-to-P/E conversion is not independent validation, while an independently sourced benchmark can challenge the target. Conditional event weights require explicit outcome values; price alone does not identify real-world probabilities.
- Transcript attribution is checked against available context/original evidence, ambiguity remains unresolved, and subsequent results respect the research cutoff.
- The reverse-DCF helper requires an explicit equity risk premium for component-derived rates, reconciles a supplied total with its components, and always validates inputs. Supplied output metadata can no longer bypass financial checks. Standalone explicit discount rates remain supported.
- The actual pre-writing reader task directs the reviewer to the owning calibration, scenario and dividend references. No new research stage, publication schema or review budget was introduced.

## Executed verification

| Check | Result |
| --- | --- |
| Workspace | 297 Python tests, 73 JavaScript tests, all 23 skill validations and 787 relative links passed |
| Public export | 298 Python tests, 73 JavaScript tests, all 20 skill validations and 870 relative links passed |
| Focused calculator regressions | 17 tests passed, including 4 new tests for explicit premium, total/component reconciliation, normalized-input revalidation and metadata bypass |
| Public structure | 20 skills, 11 flows, shared schema and coverage planning passed |
| Existing synthetic workbook | Rechecked against its specification during manifest preparation; no workbook asset was changed |
| Export integrity | Public scope links and original attribution retained; common credential and private-path pattern scan passed, including workbook XML; canonical staged manifest checked before push |

The first public structural run caught two restored private-workflow links; their public scope references were repaired and the affected structural validation rerun. No Python or JavaScript regression failed. The public Python count includes coverage-planner tests and excludes private portfolio-risk tests.

## Limits and adoption

Numerical checks establish the tested input/calculation behavior, not sound market calibration. Added host-only behavioral cases have not been run. No new issuer study, live-provider test, native Excel recalculation or PDF rendering was performed for this patch. The model reader must actually interpret evidence, test scenario connections and assess assumptions; task wording does not automate or authenticate that work.

The house rating thresholds, current-forward convention, public research-only scope and frozen studies remain unchanged. See [migration](MIGRATION.md) for the explicit-premium input change. New studies pin the new production files; old studies retain their archived rules, findings and budgets. Private research, source packs and credentials are excluded.

---

# Research skill verification - 10 November 2026, version 2.11.0

The overview covered all 23 workspace skill entrypoints, company-mode sequencing, sector applicability, key financial and publication contracts, and targeted implementation counterexamples. This public release retains 20 company-research skills, 11 flows and 21 sector activity guides; the three portfolio/strategy extensions remain outside it. Earlier audit entries below retain their original dates and outcomes.

## Findings patched in this overview

- **Review identity:** a pre-writing review could verify its original model while publication selected a different spec/workbook. The checkpoint now requires both declared files in its frozen inputs and matches their resolved identities to the published model. The writer automatically receives the reviewed model/evidence and receipt. Positive and negative synthetic tests cover this boundary.
- **Valuation input semantics:** zero FX or required yield could silently become unity in some method checks. Shared adapters now reject supplied missing, nonfinite, boolean or nonpositive denominators and unusable multiple bases. Omitted same-currency FX and zero DPS have explicit valid controls. Asset parts must be finite.
- **Analytical consistency:** removed a requirement for exclusive information/certainty before disagreeing with consensus, an automatic incentive-hurdle earnings floor, blanket assumptions about dual-listing disclosures, and wording that could hide material qualifications or force a call on an unusable baseline. A known event date does not establish how its outcome is priced.
- **General applicability:** the manufacturer example supplies depth and readable sequence, not compulsory industrial accounts for financial institutions or asset-based companies. Inapplicable ratios and unavailable bands are identified rather than fabricated. Pivotal rationale stays visible beside calculations; comments hold longer source detail.

These changes preserve the house rating thresholds, current-forward target convention, approved-source boundary, fundamental dependency sequence and distinction between target, rating, attractiveness and action. House conventions remain mandate choices, not universal valuation standards.

## Other repairs included since 2.10

This release also publishes the already-tested production-rule archive/runner, early fresh model review, staged printing and read-only preflight, frozen companions, brief-content consistency, bounded original-reader presentation confirmation, worksheet/date/display corrections, enterprise/asset valuation bridges, generic model layout, source-byte receipt and bond/yield-spread helper. Post-pair additions include metric-identity guidance and an original IRR/profit counterexample, dated cash-receipt calculations and claims, live numerical/rating explanations, and explicit sourced/discretionary/price-implied valuation derivations. Native Excel testing of linked text exposed a formula-normalization defect that is fixed: sheet identity and spaces inside literal text are preserved.

## Executed verification

| Check | Result |
| --- | --- |
| Workspace | 297 Python tests, 69 JavaScript tests, all 23 skill validations and the bundle check passed |
| Public export | 298 Python tests, 69 JavaScript tests, all 20 skill validations and the public coverage/schema/link checks passed |
| New targeted regressions | 8 tests added for review/model identity, writing inputs and valuation inputs, with valid controls |
| Synthetic integrated workbook | 6,778 numeric cells checked against the existing specification; cleaned public workbook retained |
| Native Excel component test | Earlier local repair verified linked figures and Buy/Sell/Hold text in Excel 16.0 after input changes; not a new issuer-model recalculation in this overview |
| Export integrity | Common credential/private-key and private-machine-path patterns checked, including workbook XML; original attribution footers and licenses retained |
| Release manifest | Canonical staged Git bytes, excluding the manifest itself; checked before push |

The public test count differs because its coverage-planner tests are included while portfolio-risk tests are excluded with that module. Test-double publication fixtures are explicitly synthetic; they do not represent an independent research review.

## Limits and next validation

No fresh issuer research, live provider coverage, investment-performance evaluation or full behavioral transfer trial was performed in this overview. Earlier component/native-rendering tests and real-evidence trials retain their own scope and outcomes. Deterministic checks do not authenticate source truth, event completeness, reviewer independence or omitted analytical claims. A host must actually launch fresh writer/reviewer contexts. Further cross-sector runs should measure first-draft errors, escaped material errors, false blocks and corrective interventions, not just successful packaging or equal targets.

New studies follow [migration](MIGRATION.md) and [publication review](skills/report-layout/references/publication-review.md). Frozen earlier work keeps its rule bytes and review budgets; it is not retroactively regraded or silently migrated. Private research, source packs, live provider outputs, credentials and correspondence are excluded from this export.

---

# Research skill verification - 10 November 2026, version 2.10.0

This section records the current standalone export. Earlier sections retain their original outcomes.

## Changes

- Decision contract 1.1 requires explicit numerical-trigger coverage. Automatic rating conditions probe the full model at the printed strict/inclusive boundary and one display increment further inside; approximate watch levels do not promise a new call. Decimal price-return arithmetic avoids binary noise at exact house thresholds. Local probes do not establish monotonicity outside the tested points or detect omitted prose.
- Publication wrapper 1.2 separates economic applicability from verification status for cash coverage, normalized ratios and financing. Applicable families need definition-aware assertions and registered claim links. Missing inputs/rows are incomplete implementation, not non-applicability. Genuine absent instruments/claims remain N/A; no automatic ownership haircut or sector cash formula is imposed.
- Writer and reviewer instructions test price/cash payoff explanations, date-matched alternatives to causal claims, and drivers before detailed valuation. The original synthetic payoff asset and positive/negative regressions support the checks; argument quality remains a substantive judgment.
- Added a generic real-evidence trial preparer that copies a host-curated source-only snapshot into a new workspace, retains real timestamps, stores audit hashes outside the author workspace and refuses overwriting. It supplies no issuer source data, expected call or synthetic clock. Context separation is not an OS sandbox or authenticated reviewer independence.
- Retained the public coverage planner, 20 company-research skills, 11 flows, 21 sector activity guides, all source adaptations/licenses and cleaned synthetic workbook assets. Private issuer reports/models, live provider responses, local trial material, correspondence and credentials are excluded.

## Executed verification

| Check | Result |
| --- | --- |
| Standalone structure | 20 skills, 11 flows; 860 relative links, coverage and shared schema passed |
| Standalone JavaScript | 69 tests passed |
| Standalone Python | 242 tests passed, including public coverage planning and new trigger/applicability/preparation regressions |
| Skill entrypoints | All 20 validations passed |
| Synthetic workbook | Existing cleaned example checked against its specification before manifest creation; numeric-cell result recorded in manifest |
| Export scan | Common token/private-key patterns and private machine paths checked, including workbook XML; no private credential file read |
| Manifest | Canonical staged Git bytes, excluding the manifest itself |

## Limits and migration

No new fresh-agent research outcome, native Excel recalculation, PDF print/visual trial, live provider entitlement test or investment performance was evaluated for this export. Deterministic regressions and clean trial preparation do not establish consistently high research quality, source truth, complete claim coverage or independence. Actual source interpretation, claims omitted from declarations, causal reasoning and prose meaning require a reader.

Adopt decision 1.1 and review wrapper 1.2 explicitly. Preserve earlier study outcomes, original rule snapshots, findings and review budgets rather than relabeling old packets or adding an unbudgeted review to obtain a release. Detailed contracts and migration instructions remain in the bundle.

---

# Research skill verification - 9 November 2026, version 2.9.0

This section records this standalone export. Earlier sections retain their original release results.

## Changes

- Added dated NTM coverage for quarterly, half-year and irregular periods, with changing-share profit/share treatment and retained annual interpolation. Added quantity/date/unit/currency/perimeter/basis-aware comparisons, explicit contextual comparisons, incremental-flow candidates for earnings updates and report-to-brief fidelity review.
- Separated prepared draft versions from named started review attempts, including failed/interrupted attempts. Prior blocking findings and their evidence-backed dispositions survive subsequent drafts; paths cannot silently reset the review budget. No authenticated reviewer identity or hostile-tampering guarantee is claimed.
- Added an affine bounded-bridge helper and claim assertions for feasible counterexamples to aggregate-earnings necessity claims. Added guidance for observed facts versus inferred classification, recognition, settlement and assumed constraint deadlines. These do not identify contributor models or prescribe a conservative forecast.
- Added general source/calculation-to-render bindings for scalars and ranges, explicit sign/magnitude transformations and ordering. Required current decision checkpoints validate spec/workbook hashes, model-bound fields and trigger text; decision artifacts are frozen with the draft. Qualitative judgments and omitted/unbound claims remain subject to substantive review.
- Added the optical-networking activity guide, conditional calendar-year comparisons and original synthetic acceptance packs/setup helpers. Ordinary short requests route through AGENTS.md and CLAUDE.md. Public-only coverage planning, 20-skill/11-flow boundaries, source notices and licenses remain preserved.

## Executed verification

| Check | Result |
| --- | --- |
| Standalone structure | 20 skills, 11 flows; 847 relative links, shared schema and retained source mappings passed |
| Standalone JavaScript | 69 tests passed |
| Standalone Python | 223 tests passed, including the public coverage planner and new period/review/claim/decision regressions |
| Skill entrypoints | All 20 validations passed |
| Synthetic workbook | Removed one local save-path extension from workbook.xml; every other archive member remained identical; 6,778 numeric cells checked against the specification with no issues |
| Export scan | Common token/private-key patterns and private machine paths checked, including workbook XML; no private credential file read |
| Manifest | Canonical staged Git bytes, excluding the manifest itself |

## Limits and migration

No new fresh-agent company research, native Excel recalculation, PDF print/visual trial, live data-provider test or investment-performance test was performed for this export. Passing these checks establishes the supported deterministic controls, not complete source truth, material-claim coverage, reviewer independence or reliably good future reports. The affine helper assumes independent linear ranges; real feasibility and omitted constraints remain economic judgments. Rendered bindings verify declared spans, not all unbound PDF prose or hidden styling.

Current builders must adopt the decision checkpoint and updated publication wrapper/coverage before release. The decision schema 1.0 and publication wrapper 1.1 are distinct. Frozen prior studies retain their real outcomes and original rule snapshots; legacy inspection is not publication. Preserve review budgets and findings rather than obtaining a pass through another unbudgeted correction.

---

# Research skill verification - 7 November 2026, version 2.8.0

This section records the current standalone export. Earlier sections describe their own releases.

## Changes

- Added a publication boundary around the existing strict challenge handoff: frozen draft/model/source fingerprints, a named fresh-reader declaration, six editorial dimensions plus source/financial and visual review, bounded correction rounds, and exact reviewed-PDF finalization. The first package attempt produces a partial review and no ZIP. Missing, incomplete or stale reviews block the supported release path. A host launches contexts; no dispatcher or authentication of reviewer identity was added.
- Added applicable financial assertions for after-obligation distribution coverage, paired asset/income normalization and effective-dated convertible/share states, with displayed value and period checks. These test declared financial definitions and arithmetic, not original-source interpretation or every material claim.
- Shortened the main writing standard and moved detailed examples to an optional reference. Added portable inference guidance, driver-proxy measurement tests, calibrated partial recognition, non-circular valuation cross-checks and original synthetic transfer material. Removed wording that encouraged defending an unchanged target by relocating contrary evidence.
- Fixed debate/table pagination, numeric alignment, adjacent price-event labels and print sizing; added optional explicit waterfall truncation and summary financial statements for initiations. Long tables can split with repeated headers and intact rows.
- Retained the public-only coverage planner, 20-skill/11-flow scope, source adaptations, licenses and clean synthetic workbooks. No private issuer artifacts, raw entitled research, credentials or internal correspondence are included.

## Executed verification

| Check | Result |
| --- | --- |
| Standalone structure | 20 skills, 11 flows; 762 relative links, coverage and shared handoff schema passed |
| Standalone JavaScript | 68 tests passed |
| Standalone Python | 135 tests passed, including public coverage and 16 publication-review regressions |
| Local native print probe | Shared renderer printed and visually inspected on a synthetic five-page document; continued debate and statement headers repeat without answer/header overlap |
| Local independent control trial | Real Chrome/model-check/CLI draft-to-finalize cycle exercised on synthetic inputs, preserving reviewed PDF bytes; three discovered defects corrected and independently rechecked |
| Export scan | Known local credential values, token patterns, personal paths and workbook XML metadata checked before commit |
| Manifest | Updated from canonical staged Git bytes, excluding the manifest itself |

The independent control trial used an explicitly synthetic review-completion test double to test transitions. It was not a completed substantive investment review. A separate earlier six-case fresh-agent inference test and follow-up reviewed synthetic reasoning only; it did not evaluate complete research execution. Neither private trial artifacts nor private studies are exported.

## Limits and migration

The current supported release path enforces review records and defined bindings; it does not establish review quality, source truth, independent identity, correctness of unbound prose, complete material-claim coverage or consistent research scores. No full research controller, automatic semantic judge, live provider entitlement test, native Excel recalculation or investment-performance evaluation is included. The native print/control trials above ran in the local workspace on the copied shared implementation, not as an additional full issuer run in this export checkout.

Older builders must adopt the new summary/assertion/review workflow before making a current release. Historical integrity-only inspection uses explicitly labeled `--legacy` and is not a publication shortcut. Partial-multiple calibration, aggregate-to-segment attribution and other causal judgments still require substantive review and repeated end-to-end research trials. Passing these code checks is not evidence of a consistent 9/10 research process.

---

# Research skill verification - 7 November 2026, version 2.7.0

This section records the current standalone export. Earlier records below describe their own releases.

## Changes

- Added the shared report renderer's Argument and Debate blocks, declared-business-unit checks, and focused regression tests. Arguments require a point, cited evidence, inference and implication; debates require cited claims/statuses, an answer, quantified implications and a dated test. These checks validate structure, not whether a claim is true or the inference follows.
- Added a second review of the actual drafted report and brief, retaining the pre-conclusion analytical challenge. This remains a research instruction; release packaging does not enforce challenge-handoff completion.
- Updated earnings-basis reconciliation, material asset/claim valuation, event expectations, rating/new-money presentation and thesis-led writing guidance. The current-forward target convention and house rating bands are preserved.
- Required disclosed operating drivers to feed material segment forecasts and expanded the consumer-sector guide for branded apparel/sportswear. Company-specific data, models, reports and review correspondence remain excluded.
- Retained public-only coverage planning, scope adaptations, licensed assets, existing release checks and clean synthetic workbook fixtures.

## Executed verification

| Check | Result |
| --- | --- |
| Bundle structure | 20 skills, 11 flows; catalog, coverage, links and handoff schema passed |
| JavaScript suite | 67 tests passed |
| Python suite | 115 tests passed, including standalone coverage and new report-block regressions |
| Export scan | Known local credential values, token patterns, personal paths and workbook XML metadata checked |
| Manifest | Updated from canonical staged Git bytes |

## Limits

No fresh-agent transfer evaluation, native Excel recalculation, live data-provider test or visual PDF review was performed for this release. Source truth, inference quality, scenario calibration and investment performance are not established by passing the code checks. Plain-language judgment detection is a limited phrase check and can miss paraphrases. Existing studies require adapter changes to use the new blocks. Review-record enforcement and a runtime controller remain unimplemented. The public bundle remains 20 company-research skills and 11 flows.

---

# Research skill verification - 6 November 2026, version 2.6.0

This section records the current standalone export. Earlier sections describe their own releases.

## Changes

- Added the report-layout release checker and shared `package()` build path: supported valuation-method reconciliation, annual/NTM period bindings, fiscal-calendar interpolation, current-year disclosure checks, model/brief/rendered decision agreement, age checks, approved contacts and house wording regressions.
- Added release fingerprints, existing-file comparison, PDF printing from the supplied HTML, atomic package/record completion and failed-attempt handling. These controls apply to builders invoking `package()`; older studies are not automatically migrated.
- Preserved generic summaries while adding investment-publication dependencies and conditional render stages. Regular-review metadata identifies forecast-change recalculation/audit stages. Catalog metadata is not an automatic scheduler.
- Revised market-expectations instructions to qualify public-information incorporation, price/year/multiple inference, high estimates, attribution and guidance/run-rate assumptions.
- Added two original synthetic evaluation packs and an arithmetic grader, with answer notes separate from evidence packs. No fresh-agent behavioral trial was performed for this release.
- Declared PDF inspection and date-parsing dependencies so fresh installations can execute the release regressions.

## Executed verification

| Check | Result |
| --- | --- |
| Installation | Isolated npm ci --ignore-scripts passed |
| Bundle structure | 20 skills, 11 flows; catalog, coverage, links and handoff schema passed |
| JavaScript | 67 tests passed |
| Python | 110 tests passed, including standalone coverage tests |
| Skill metadata | All 20 entry points validated |
| Export scan | Known local credential values, token patterns, personal paths and workbook XML metadata checked |

The local review separately verified a copied ANTA model with its real calculation checker: 37 saved-release checks passed, and the reported period/hash/render/package-failure regressions were exercised. Issuer artifacts and review logs are excluded from this public bundle. Packaging fault tests in that review reused PDFs through a printer stub; this export did not independently run native Excel, Chrome or visual PDF inspection.

## Limits and scope

The validation record explicitly leaves source truth, economic judgment, prose figures, share class/scale, substantive question coverage, estimate vintages, exchange-session lookup and visual quality with analyst review. A reported operating update is permitted by the current house period convention; the local message board records that convention as still available for the user's confirmation/change. Passing code tests does not establish reliable research behavior or investment performance. No controller, live data entitlement, automated judge or recurring monitor was added.

The standalone coverage planner, scope adaptations, licensed fonts and third-party notices are retained. Public scope stays company-only: 20 skills and 11 flows. Private issuer work, entitled evidence, credentials, internal discussion archives and the previously removed dated data-planning directory remain excluded. The synthetic workbook was retained because the local difference was only save-path metadata.

---

# Research skill verification ? 6 November 2026, version 2.5.0

This section records the current export. Earlier records below describe their own releases.

## Changes

- Added `world-state.md`: a dated exposure map and scan of developments since the last filing/call, materiality triage, transmission into forecasts/valuation, unresolved resolution dates and a release-cutoff refresh.
- Added `what-the-market-trades.md`: research guidance for inferring the variable, period or asset that appears to drive price, using dated consensus/revisions, surprises, guidance comparisons, price reactions and investor questions. Model the later debate year or value an asset outside current earnings where relevant, while preserving the current-forward target denominator.
- Linked the new work into initiation, regular and major updates, intake, industry analysis, forecasts, valuation, challenge, conclusions, writing and proposed monitoring. Evidence-pack handoffs retain referenced records; no new envelope kind was added.
- Added a competitive-position procedure for clinical pipeline assets under the existing pharma guide, with stage/population/scale qualifications and scenario/funding consequences.
- Expanded provider retrieval guidance for dated three-year/segment consensus and price-reaction evidence, and documented the AlphaPai roadshow recall route. These are requested reads, not a new connector, tested entitlement or guarantee of fields/history.
- Added three authored evaluation prompts: a forward year covered by backlog, price expectations ahead of a public plan, and a substantial unlaunched asset. They are not completed agent evaluations.

Preserved the standalone coverage planner and updated relevant role purposes. The public scope remains 20 skills and 11 flows, with portfolio/strategy extensions outside the bundle. The dated data-planning directory remains excluded. The only local workbook difference was save-path metadata, so the clean public asset was retained unchanged. Existing licences and pinned adaptation notices are preserved.

## Executed verification

| Check | Result |
| --- | --- |
| Installation | Isolated `npm ci --ignore-scripts` passed |
| Bundle structure | Catalog, coverage, handoff schema and relative links passed |
| Skill entry validation | All 20 entries passed |
| New reference anchors | 13 fragment links checked |
| JavaScript suite | 65 tests passed |
| Python suite | 93 tests passed |

No numerical helper, market-expectations detection engine or automated world-state retrieval service was introduced. The newly authored market-reading heuristics are analytical inferences, not observed investor beliefs or independently validated explanatory models. No live provider/data-entitlement test, native Excel recalculation, PDF render, issuer study, independent behavioral assessment or investment-performance evaluation was performed for this export. Structural checks cannot establish source truth, completeness, causal interpretation or investment quality.

The canonical file manifest and bounded publication scan were refreshed. The scan checks known local credential values, common token patterns, private paths and workbook XML metadata; it is not forensic assurance. Private evidence, broker material and credentials are excluded.

## Historical record: version 2.4.1

# Research skill verification ? 5 November 2026, version 2.4.1

This patch imports eight instruction/reference changes. Earlier records below are historical.

## Changes

Research scope now explicitly obtains its date from the environment and verifies current prices, reporting periods, consensus, relevant policy/trade/macro conditions and investment themes against dated sources. Earnings-clock and fiscal-calendar references point back to that rule. Examples use relative fiscal-year language, clarify that historical market regimes are illustrations rather than current facts, and describe the reporting currency generically. Model instructions explicitly require replacing synthetic dates, periods and currency labels with issuer-specific evidence.

The standalone coverage planner and company-only scope remain intact: 20 skills and 11 flows. The removed data-planning directory stays excluded. A local workbook difference was verified as save-path metadata only; the already-clean public workbook was preserved. No runtime script, numerical model input, report template or calculation asset changed.

## Executed verification

- Structural checks passed for the catalog, links, coverage and handoff schema.
- Five owning skill entries validated: research-cycle, company-model, investment-conclusion, macro-event-analysis and valuation-thesis.
- JavaScript: 65 tests passed. Python: 93 tests passed.
- Canonical file-manifest verification and bounded publication screening passed.

No new PDF rendering, native Excel recalculation, live market-data retrieval, issuer study or independent behavioral evaluation was performed. The new instructions require date-aware research; this export does not establish that current market conditions or data access were checked for a particular issuer. Existing deterministic test results do not prove research quality or investment performance.

## Historical record: version 2.4.0

# Research skill verification ? 5 November 2026, version 2.4.0

This section records the current export. Earlier records below apply to their own versions.

## Changes

- Added early mapping of actual revenue/volume exposure by region, channel and material customers before interpreting demand or trade risks. Market-share analysis now compares absolute growth and like-for-like business/geographic segments before drawing a negative conclusion.
- Expanded term-level employee-incentive review and tests against forecast hurdles. Below-hurdle estimates need an explanation; the existing prohibition on forcing costs or earnings to meet a KPI remains. Incentive motivation is not a guarantee of reported delivery.
- Required valuation triangulation across relevant own history, close same-market business peers and current sector investment conditions. Short or single-regime histories cannot determine the multiple alone.
- Aligned annual dividend yield with the selected forward EPS fiscal year and changed the synthetic model's yield reference from FY2026 to FY2027 DPS. Added an all-scenario regression for the earnings/dividend-year alignment.
- Strengthened writing guidance: trace facts and interpretations to evidence, avoid false causal links and unsupported generic claims, and develop analysis rather than description.

The bundle still has 20 skills and 11 flows. The dated data-planning directory remains removed. Public scope adaptations, coverage planning and licence notices are preserved. Only the original synthetic company-model assets are supplied; no issuer study, private workbook, entitled source material or live provider response was imported.

## Executed verification

| Check | Result |
| --- | --- |
| Installation | Isolated `npm ci --ignore-scripts` passed |
| Structural check | Catalog, skill links, coverage and handoff schema passed |
| Skill-entry validation | Eight owning skill entries passed |
| JavaScript suite | 65 tests passed |
| Python suite | 93 tests passed |
| Synthetic asset | JSON matches its generator; workbook formula/input/cached-value synchronization passed for 6,765 numeric cells |
| Dividend-year regression | Selected forward EPS and dividend yield use FY2027 in Bear, Base and Bull |

Removed local save-path metadata from the supplied synthetic workbook while retaining its other members and calculated caches. No new native Excel recalculation, spreadsheet visual review, PDF render, live-agent behavioral study, issuer forecast review or investment-performance evaluation was performed for this export. Instruction changes and mathematical reconciliation are not independent evidence of sound investment judgment.

The canonical file manifest and bounded publication scan were refreshed. The scan checks known local credential values, common token patterns, private paths and Excel XML metadata; it is not forensic assurance.

## Historical record: version 2.3.0

# Research skill verification ? 5 November 2026, version 2.3.0

This section records the current release. Earlier records below describe their own versions.

## Changes

- Historical forward P/E remains the primary comparison for a forward-EPS target. A separate trailing band uses actual earnings already published at each price date, updated on announcement dates. Subsequent realised forward earnings are a forecast-bias diagnostic, not historical investor knowledge. The bands must remain distinct. Historical context does not guarantee twelve-month price convergence.
- Corrected a sentence implying that applying a trailing multiple to forecast EPS automatically sets a one-year target date. It changes the earnings basis and requires justification; the target horizon remains a separate choice.
- Full-report sections declare investor questions through `covers=(...)`. Every remaining question needs `omit(question, reason)`. One section can cover multiple questions. Unknown question IDs and blank omission reasons fail; the renderer checks declarations, not whether the substantive analysis is correct.
- Updated the module example and migration guidance for that API. Added three coverage regression tests and extended scenario-price precision coverage for prices below 100. Back matter now avoids internal page breaks where feasible.

The standalone scope remains 20 skills and 11 flows, with existing coverage planning, licences and private-data exclusions preserved. The one-page brief API is unchanged. No new trailing-band data connector/calculator or automated financial-claim validator is introduced, and no issuer forecast or valuation target was changed.

## Executed verification

| Check | Result |
| --- | --- |
| Installation | Isolated `npm ci --ignore-scripts` passed |
| Bundle structure | Catalog, 20 skills, 11 flows, handoff schema, coverage and relative links checked |
| Entry validation | company-model, valuation-thesis, research-brief and report-layout passed |
| JavaScript tests | 65 passed |
| Python tests | 92 passed, including 11 report-layout tests |
| PDF smoke render | Two-page synthetic fixture printed in Chrome and both page images inspected; covers and reasoned omissions exercised |

The PDF fixture is deliberately sparse and is not a production content-density or complete research-quality test. No independent live-agent evaluation, native Excel recalculation, real issuer study rerun, forecast-accuracy assessment or investment-performance evaluation was performed. Trailing-band guidance is not proof that release-aware historical data have been retrieved.

The canonical file manifest and bounded publication scan were refreshed. The scan checks known local credential values, common token patterns, private paths and workbook XML metadata; it is not forensic assurance. Private research, entitled broker material, live provider responses and credentials remain excluded.

## Historical record: version 2.2.1

# Research skill verification ? 5 November 2026, version 2.2.1

This patch imports six changed instruction/reference files from the maintained workspace. Earlier release records below are historical.

## Changes

- Research challenge now distinguishes the economic dependence of the target on each investment reason from the assumption's difference versus comparable consensus. The model standard and company sequence carry this into valuation presentation and the challenge stage.
- Investment conviction now checks each numerical thesis breaker against the matching base-case metric and period and identifies shared causes behind multiple conditions. Conflicts require investigation; thresholds must not simply be moved to defend the thesis. Investment conclusion references this check.
- Full-report layout now directs study builders to draw figures in prose, tables and charts from calculated model outputs and saved source data, and rebuild both the report and brief after a model change.

These are instruction refinements. No new calculation helper, threshold evaluator, report-claim registry or automated claim-validation engine is introduced, and no real-company study was rerun. The existing scripts and assets remain unchanged. The public bundle still contains 20 skills and 11 flows; its coverage planner, scope boundaries and licence notices are preserved. Method inspirations discussed in the review include [GeniusTrader-Harry's pillar audit](https://github.com/GeniusTrader-Harry/equity-research-skill/blob/main/references/phase10-pillar-audit.md) and [Evilhill's report pipeline](https://github.com/evilhill/equity-research-skill).

## Executed verification

- Structural/catalog/link/schema/coverage checks passed.
- The six affected skill entry points passed the skill-entry validator (company-model, investment-conclusion, investment-conviction, report-layout, research-challenge and research-cycle).
- JavaScript: 65 tests passed. Python: 89 tests passed.
- Publication file/credential screening and canonical file-manifest checks passed.

The tests exercise existing deterministic behavior and structural integrity. No independent behavioral evaluation, new PDF render, native Excel recalculation or investment-performance assessment was performed for this wording patch. No private research, broker material, live responses or credentials are included. The refreshed manifest describes this supplied file set.

## Historical record: version 2.2.0

# Research skill verification - 5 November 2026

This section records version **2.2.0**. Earlier release records below are historical; their counts, names and test totals apply only to those releases.

## Current changes and scope

The workspace has 23 skills and 14 flows. The standalone company-research export now has **20 skills and 11 flows**, with twenty sector activity guides. Portfolio allocation, cross-asset strategy and risk budgeting remain external.

- Added `report-layout`: a reusable A4 full-report renderer, front page and section rails, numbered sources/exhibits, chart helpers, embedded IBM Plex Sans fonts and the complete SIL Open Font License. The one-page brief retains its separate template. PDF printing requires Chrome; page inspection has optional declared PyMuPDF dependencies.
- Expanded human-reviewable models with Cover, Summary, Scenarios and Checks, navigation, source tags, row-label comments, tab colours, grouping, print settings, chart controls and physical address translation for inserted source-tag columns. The supplied company example is synthetic.
- Adopted the updated workbook theme (blue hardcodes and blue/yellow assumptions, black formulas, green cross-sheet links, grey italic memo ratios and bold black key outputs) and aligned the older portable scaffold with it. Clarified the different annotation layouts for a compact scaffold and the full company model.
- Strengthened the research debate: identify the core contested investor questions, assemble the strongest claims on both sides, seek discriminating evidence, and build bear/bull outcomes from those questions rather than minor changes to every input.
- Updated full-initiation delivery guidance to accompany the report with its brief and Excel model. Provider guidance now includes benchmark/stock price history for the front-page comparison; access remains host- and entitlement-dependent.

Preserved the coverage planner, company-only scope, third-party notices and CI. Added the report-layout applicability rule. Removed a named-issuer example from the generic renderer, corrected stale scenario-selector examples, fixed displayed scenario-return arithmetic and a clipped final date label, and added regression coverage. Existing private research and provider responses are not part of the export.

## Executed verification

| Check | Result |
| --- | --- |
| Isolated dependency installation | `npm ci --ignore-scripts` passed |
| Skill entry validation | All 20 entry points validated |
| Structural check | 20 skills and 11 flows; catalog, coverage, schema and relative links checked |
| JavaScript suite | 65 tests passed across five files |
| Python suite | 89 tests passed, including eight new report-layout tests |
| Supplied synthetic company workbook | Formula/input/cached-value synchronization passed for 6,765 numeric cells |
| Portable operating scaffold | 48 named cells synchronized after the palette refresh |
| PDF smoke render | A two-page synthetic report printed in Chrome and its page images inspected; the fixture is deliberately sparse and is not an issuer report or a production content-density test |

The PDF smoke check confirms basic rendering and exposed a date-label clipping issue, which was corrected and re-rendered. It does not validate every chart type, every report length or every language. No new native Excel recalculation or native Excel visual review was performed; the supplied workbook's saved values were compared with its specification. No live-agent behavioral study, forecast-accuracy assessment or investment-performance evaluation was performed. Source truth and judgment are not established by these checks.

The file manifest records canonical Git bytes, excluding itself to avoid self-reference. Publication screening compares known local credential values, common token patterns, private paths and workbook XML metadata; it is bounded screening, not forensic assurance. Local save-path metadata was removed from the synthetic company fixture. Fonts retain their own OFL licence and are not relicensed under MIT.

## Historical record: version 2.1.0

# Research skill verification - 4 November 2026

This section records the version **2.1.0** export. The earlier 2.0.0 audit below is historical and its skill counts, invocation names and test totals do not describe the current release.

## Current scope and changes

The maintained workspace has 22 skills and 14 flows. This standalone company-research export has **19 skills and 11 flows**, including the new industry-analysis role and twenty sector activity guides. Portfolio allocation, risk-budget and cross-asset strategy extensions remain outside this repository. The issuer-question skill now uses the workspace's `issuer-questions` invocation; the former handoff kind remains accepted for compatibility.

Imported the current instructions, references, generic scripts, original synthetic assets and deterministic tests. Updates cover industry economics before forecasts and during reviews; integrated workbook construction and synchronization; current-forward earnings and own-versus-consensus P/E comparisons; target underwriting; evidence handling and source access limits; investor judgment; and drivers-first, selective investment writing and calibration.

Preserved the public repository's coverage planner/checker, CI, global data-planning documents, scope boundary and pinned third-party licences. Updated coverage for industry analysis and the renamed question skill. Removed an orphan dependency on an excluded strategy-testing stage. An additional regression verifies that industry work cannot be skipped in any of the three company modes. No issuer forecasts, private workbooks, broker reports, credentials or live provider responses are supplied.

## Executed verification

| Check | Result |
| --- | --- |
| Clean dependency installation | `npm ci --ignore-scripts` passed in an isolated publication checkout |
| Skill entry validation | All 19 entry points passed `quick_validate.py` |
| Bundle structure | 19 skills, 11 flows; local links, catalog, coverage and handoff schema checked |
| JavaScript tests | 65 passed across five test files |
| Python unittest suite | 80 passed, including coverage planning and workbook/forecast helpers |

The file manifest records the supplied file set and hashes. Its own bytes are excluded from its hash list to avoid self-reference. Credential-pattern and private-path screening is a bounded publication check, not forensic assurance. Workbook test results refer to synthetic fixtures, not recalculated issuer forecasts.

These checks establish structural consistency and tested deterministic behavior. No independent live-agent behavioral test, native Excel rendering run, forecast-accuracy study or investment-performance evaluation was performed for this export. Authored behavioral cases are evaluation material, not evidence of executed evaluation. No subscriptions, active monitors, dispatch service or trading capability are introduced.

## Historical audit: version 2.0.0, 2 November 2026

Version 2.0.0 removes the application-specific prefix from maintained skill identities, folders, sibling links, imports, catalog references, tests and visual-theme identity. Historical names remain only in migration documentation and unchanged provenance records. This audit concerns instruction and deterministic-tool coherence; it does not establish investment performance or source truth.

## Scope and review

The workspace has 21 generic skills. The standalone repository contains 18 company-research skills and ten routes. The three portfolio/strategy/risk extensions remain external to this repository. Reviewed the entry skills, their decision-relevant references, routing/dependency graph, shared handoff contract, model/revision requirements, sector ownership boundaries, conditional branches, support-file imports and deterministic tests. No issuer model, entitled broker report, credential, live response or private source archive is supplied.

## Findings and corrections

| Finding | Change |
| --- | --- |
| Available side branches did not guarantee an explicit consideration decision. | Added a mode-specific coverage specification and planner/checker covering every skill. Conditional work needs an applicability decision; required work needs completed or eligible reused references. |
| A screening handoff could bypass the proper new/existing coverage entry. | Selected names now enter initiation or the appropriate update mode before deeper company work. |
| The model specialist's stage table did not show costs as its own explicit build. | Added matched component costs, unit economics, segment margins and investment before integrated statements. |
| Conviction existed but was absent from some human-readable sequence summaries. | Made it an explicit stage before the conclusion, consistent with the catalog and references. |
| Core catalog routes ended at the brief without an explicit follow-up stage. | Added follow-up/learning stages after all three core modes; proposed observations remain separate from activated monitoring. |
| Regular reviews need valid inherited risk/audit support without automatically rebuilding forecasts. | Required coverage accounts for governance/model/quality reuse; targeted numerical revisions must reference risk review, recalculation, audit and refreshed outputs. |
| A standalone export can retain dangling dependencies on excluded workflows. | Removed extension-only stages and routes and replaced external links/instructions with explicit scope boundaries. |
| Public instructions contained workspace-specific branding and stale package scope/version claims. | Generic names, 2.0.0 package/manifest, updated index, migration guide and coherent standalone instructions. |
| A clean Linux run exposed an Excel-tracer dependency already installed on the development machine. | Declared pinned `openpyxl`/`et_xmlfile` requirements, documented setup and installed them explicitly in CI before testing. |

## Dependency logic

Initiation establishes identity/cutoff, business/competition, source history, early governance/reporting reliability and sector mechanisms before forecasting. Foundational revenue and cost assumptions feed linked earnings, capital, working capital, financing and cash. Audit precedes valuation; provisional valuation feeds thesis validation and challenge. Conviction and eligibility are assessed before the final target/rating and communication. Follow-up preserves observations, vintages and learning.

Regular review loads the previous case/model/conviction, checks new evidence and refreshes price/valuation/return while retaining operating forecasts unless concrete evidence warrants a change. Major earnings/catalyst work preserves frozen forecasts, evaluates matched outcomes before overwriting estimates, then recalibrates affected dependencies. A catalyst without period actuals uses an event-impact bridge. Material discoveries reopen affected work at any time.

## Skill coverage by mode

`required` means perform scoped work or explicitly reuse eligible dated artifacts; it does not require a new report per specialist. `conditional` means decide whether the specified trigger applies and retain the reason. The alternate entry mode is outside the chosen scope. Portfolio, trading and covariance-budget work are separately scoped and not silently required for a stock report.

| Skill | Initiation | Regular | Major |
| --- | --- | --- | --- |
| `research-cycle` | required | required | required |
| `stock-initiation` | required | outside-scope | outside-scope |
| `model-revision` | outside-scope | required | required |
| `evidence-intake` | required | required | required |
| `company-model` | required | required | required |
| `corporate-governance` | required | required | required |
| `financial-quality` | required | required | required |
| `valuation-thesis` | required | required | required |
| `research-challenge` | required | required | required |
| `investment-conviction` | required | required | required |
| `investment-conclusion` | required | required | required |
| `research-brief` | required | required | required |
| `monitor-review` | required | required | required |
| `company-change-tracking` | conditional | required | required |
| `macro-event-analysis` | conditional | conditional | conditional |
| `theme-screening` | conditional | conditional | conditional |
| `management-questions` | conditional | conditional | conditional |
| `chart-visualization` | conditional | conditional | conditional |

Management questions branch from unresolved decision-driving gaps, not a mandatory outreach quota. Macro/context work feeds operating drivers or valuation through distinct mechanisms. Screening discovers/triages candidates and does not complete underwriting. Charts are a communication subtask. Governance establishes facts and shareholder consequences; conviction preserves/test reasons; conclusion owns the price-based rating and eligibility explanation. Financial quality has three distinct passes using shared issue IDs. None duplicates a separate model or independent price target.

## Verification

| Check | Result |
| --- | --- |
| Entry-point validation | 21 workspace and 18 standalone entries passed |
| JavaScript tests | 44 passed in both workspace and standalone export |
| Python tests | 57 workspace; 50 standalone passed (seven portfolio-risk tests excluded with their module) |
| Catalog/links/English/schema/source checks | Passed; standalone checks supplied content without claiming private archives were shipped |
| Coverage behavior | Missing/duplicate skills, skipped required work, undecided conditions, stage reordering, stale method versions, missing reuse references and unchecked targeted revisions are rejected |
| Agent evaluation scenarios | Authored scenarios retained; no live-agent behavioral or investment-performance evaluation claimed |

The optional workbook renderer requires a compatible external runtime; it is not a supplied dependency or evidence that a real issuer model was rendered. No issuer forecasts or financial models were recalculated in this cleanup. The coverage helper checks declared completion and references; it cannot verify source claims or whether an analyst actually performed the referenced work. No automatic worker dispatcher, active monitor or trading integration is introduced.
