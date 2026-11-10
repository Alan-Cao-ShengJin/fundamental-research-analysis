# Keep the reusable decision current

Use after model calculation and before writing/review in every initiation or update that produces a stock decision. This is a dependent artifact, not a second source of targets or a review approval. The package adapter defaults `decisionRecord` to `evidence/decision.json`; an alternative path must stay inside the study. Current publication requires the contract below. Frozen historical studies retain their original rules; an explicit legacy integrity inspection does not establish current publication readiness.

## Derived core and judgment

`schemaVersion: "1.1"` identifies this **decision** contract, independently of the publication wrapper version. The record contains `security`, `currency`, `cutoff`, routed `researchMode`, `quote.price/date`, `rating`, `targetPrice`, ISO `targetDate` (cutoff plus twelve months), `priceReturn`, and any `dividendYield`, `bearTarget`, `bullTarget` available through the release record's model bindings. Dividend yield is numeric or null, with descriptive detail in separate fields. `model` contains the study-relative `spec`, `workbook`, `specSHA256` and `workbookSHA256` for the actual current files.

Keep qualitative judgments, source uncertainty, preferred method and material alternatives in the record. A model hash does not establish that these are supported. Extra `bindings` entries map an existing JSON `pointer` to a logical `model` reference, for example a sustainable return, target multiple or threshold. `boundText` entries contain a destination `pointer`, a `template` with plain named tokens, and `inputs` mapping each token to `model`, optional `style: number|percent|multiple`, `decimals: 0..6` and `transform: identity|negate|magnitude`. The saved string must reproduce that template from the current calculated values. Bind the numeric thresholds in material triggers; do not type an older rounded threshold into the surrounding sentence. Unbound causal or qualitative clauses remain subject to review.

The original [generic template](../assets/decision-record.example.json) supplies only extra fields/bindings. The helper fills the derived core; replace its fictional references with this study's cells. It does not prescribe the method, forecast, trigger or source classification.

## Numerical trigger meaning

Every current decision explicitly supplies `triggerCoverage` and `triggerTests`. For material numeric conditions in the decision, use `status: checked` with the exact unique `testIds`. Each test has `id`, `rationale`, and `boundary: {pointer, token}` identifying one numeric input in a `boundText` rule. Bind the actual economic level, with its signed coordinate and displayed precision. If there are no numerical decision conditions, use `status: not-applicable`, a substantive `reason`, empty `testIds` and empty tests. The reader still checks for omitted conditions in prose.

Use `mode: watch` for an approximate level that invites reassessment. It has no `expectedRating` or `relation`; its text must not promise an automatic rating change. Use `mode: automatic` when the text says crossing a level produces a particular call. Also supply `inputRef` for the economic model cell to change, `relation: >|>=|<|<=`, and `expectedRating: Buy|Hold|Sell`. For example, a strict sufficient Buy threshold can be tested with `relation: >`; at exactly the house +10% price-return boundary the call is still Hold. The rating output itself cannot be overridden.

The checker recalculates the whole model at the displayed boundary (inclusive conditions) or just inside it (strict conditions), and one display quantum further inside. It checks both the model rating and the house price-return call. A rounded number can reproduce its source cell yet fail this implication. Increase justified precision, choose a sufficient threshold, or describe it honestly as a watch level. A sufficient threshold need not be the unique or necessary boundary. Automatic tests require identity transformation: the displayed coordinate must be the economic input coordinate.

These are local numerical probes, not proof of monotonicity everywhere, causal support or completeness of prose coverage. The reviewer tests any additional material regimes or interacting conditions. Synchronization does not invent applicability or mark tests complete. Historical decision contracts retain their original outcomes; adopt this contract explicitly for a new study rather than relabeling an old review history.

## Build and check

After recalculation, call `decision_record.synchronize(study, release_record, spec, existing_decision)` from the builder and save the returned dictionary **before** preparing the writing/review checkpoint. It refreshes derived core and declared bindings while preserving judgments. It never marks a review complete. The caller must update qualitative reasoning where a new model invalidates it; synchronization is not evidence that an old conclusion survives.

For a study that already has a saved release record:

```text
python -B -X utf8 skills/report-layout/scripts/decision_record.py sync <study-folder>
python -B -X utf8 skills/report-layout/scripts/decision_record.py check <study-folder>
```

Use `--record` for a different saved build record. The first build can pass its in-memory release-record dictionary directly; it need not fabricate an earlier release. Fresh model/spec hashes and all declared binding values are independently checked by `release_check.py`. The decision file is automatically frozen among review inputs and included in release fingerprints. Missing or stale decisions block current publication even when the headline target is unchanged.

Order: calculate model → refresh decision and trigger bindings → render report/brief from those inputs → integrity checks → freeze → actual reader starts/reviews → finalize exact reviewed files. Any correction invalidates affected downstream artifacts and review freshness. Keep existing attempt limits; synchronizing or reprinting after the last review does not create approval or an extra review allowance.

## Material horizon choices

For methods using a normalized economic return, keep the target's earnings/book/asset period distinct from the period or transition used to estimate that sustainable return. Record the rationale for normalization and show a plausible alternative when it can change the rating or pivotal conclusion. The current-forward P/E contract still applies to a P/E target; choosing later normalized returns for another method is not permission to relabel a later EPS as current NTM. Do not force different analysts' defensible assumptions or target prices to match.
