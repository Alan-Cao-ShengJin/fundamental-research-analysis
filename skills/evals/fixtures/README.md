# Behavioural fixtures

Synthetic evidence packs for the user to run and grade. Each pack is self-contained and invented; nothing in it is a real company, price or estimate. The expected outcomes sit in [answers/](answers), outside the pack, and are not given to the agent.

How to run one:

1. Open a fresh session with no other research context.
2. Prompt: "Initiate coverage of the company in `skills/evals/fixtures/<pack>/` using only that folder as evidence. Cutoff date as stated in the pack. Produce the decision block (brief.json) and a one-paragraph market read." Do not mention the trap.
3. Grade against the answer note. For the fiscal-calendar pack, `python -B -X utf8 skills/evals/fixtures/answers/grade_fiscal_calendar.py <brief.json>` checks the arithmetic; the judgment pack is graded by reading.

Packs:

| Pack | Failure it tests | Grade |
| --- | --- | --- |
| [fiscal-calendar](fiscal-calendar/pack.md) | Rolling the target's EPS to the target date; mixing the dividend into the target or the tier; a June year end and a Monday cutoff | Code assertions plus a reading |
| [price-above-band](price-above-band/pack.md) | Chasing a price that has run ahead of unchanged estimates: raising forecasts or the target multiple toward the price-implied figure without evidence of a structural change | Reading only |
| [inference-review](inference-review/pack.md) | Asset/income boundaries, target-dependent cross-checks, composite operating proxies, governance persistence, cyclical ratios and business-appropriate valuation; includes a supported distribution case | Reading against [the answer note](answers/inference-review.md) |

| [corvane-photonics](corvane-photonics/pack.md) | Non-December fiscal year with emerging product lines: calendar-year EPS from quarters, adoption-to-EPS bridges without overlapping architectures, capacity and commitment reconciliation, guidance not treated as a floor, an event-anchored valuation window | Reading against [the answer note](answers/corvane-photonics.md) |
| [halden-outdoor](halden-outdoor/pack.md) | Segment-specific minorities in model-recalculated sensitivities, an event-anchored window whose alternatives cross a rating threshold, a brief that keeps management-only claims attributed; negative control for calendar-year EPS, optical terms and new-product bridges | Reading against [the answer note](answers/halden-outdoor.md) |
| [alder-industrial-supply](alder-industrial-supply/pack.md) | Distributor order economics, nonrecurring cash release, supplier rebate normalization, economic versus accessible JV cash, sample-versus-industry claims; June year end with no automatic CY requirement | Reading against [host-only criteria](answers/alder-industrial-supply.md) |
| [alder-regular-update](alder-regular-update/pack.md) | Price-only update on a checked prior model; retain operating assumptions and carry unresolved findings | [Update criteria](answers/alder-updates.md) |
| [alder-earnings-update](alder-earnings-update/pack.md) | Cumulative results versus the actual frozen forecast, revised guidance, cash timing, consensus vintage and affected-model recalibration | [Update criteria](answers/alder-updates.md) |
| [cedar-bank](cedar-bank/pack.md) | Held-out bank mechanism: earning-asset/funding spreads, impairment and regulatory capital, cumulative versus quarter flows with changing shares, bank-appropriate valuation and distribution constraints | [Host-only criteria](answers/cedar-bank.md) |

The corvane-photonics and halden-outdoor packs are acceptance tests of the normal entry point: copy `CLAUDE.md`, `skills/` without `evals/fixtures/answers/`, and the pack into a clean workspace, start a fresh session there and give only "initiation on <company>; evidence in <pack path>".

For a full clean-workspace run, [prepare_acceptance.py](../scripts/prepare_acceptance.py) creates a new directory with the production bundle and raw pack, excludes evaluations/tests/answers and prior work, records the exact short request and file hashes in a separate host audit directory, disables project auto-memory, and predeclares a synthetic evaluation clock without changing production timestamps. It never deletes or overwrites an existing run. Example arguments: `--pack halden-outdoor --destination NEW_DIRECTORY --audit HOST_AUDIT_DIRECTORY --request "initiation on Halden Outdoor Group (HDOG); evidence in inbox/halden-outdoor/pack.md" --evaluation-time 2026-11-09T12:00:00Z`. The host separately starts and logs a fresh session under its ordinary permissions. A denied launch is not a completed acceptance run and must not be bypassed. Preserve first-draft and corrected-draft results separately within the declared review budget.

For inference-review, use its own scoped review task rather than the initiation prompt above. Give the agent only the pack and owning skills, keeping the answer note separate until grading.

A pass says the tested slips are absent in that run. It does not establish the method is right in general; repeat in a fresh session when the owning skills change.

For Alder, `prepare_acceptance.py` copies both pack.md and raw facts.json when present. Prepare a second identical initiation workspace before reviewing the first result to compare independent runs on the same bundle/evidence. Prepare the two update workspaces too, but **do not run an update until a genuine checked baseline exists**. The host then runs [stage_update_acceptance.py](../scripts/stage_update_acceptance.py) with `--study SELECTED_STUDY --destination PREPARED_UPDATE_WORKSPACE --audit HOST_AUDIT_DIRECTORY --evidence ORIGINAL_RAW_INBOX_DIRECTORY`. It verifies model reproduction, copies that exact study and selected raw evidence, records component eligibility and carries unresolved review checks; it does not certify or publish a rejected conclusion. The update author receives only `update view on Alder Industrial Supply (ALDR)`, with new evidence in inbox/ and baseline components in research/. No fabricated CURRENT_MODEL pointer or approved decision is supplied.
