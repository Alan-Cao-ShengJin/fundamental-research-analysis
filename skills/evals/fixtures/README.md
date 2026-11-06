# Behavioural fixtures

Synthetic evidence packs for the user to run and grade. Each pack is self-contained and invented; nothing in it is a real company, price or estimate. The expected outcomes sit in [answers/](answers/), outside the pack, and are not given to the agent.

How to run one:

1. Open a fresh session with no other research context.
2. Prompt: "Initiate coverage of the company in `skills/evals/fixtures/<pack>/` using only that folder as evidence. Cutoff date as stated in the pack. Produce the decision block (brief.json) and a one-paragraph market read." Do not mention the trap.
3. Grade against the answer note. For the fiscal-calendar pack, `python -B -X utf8 skills/evals/fixtures/answers/grade_fiscal_calendar.py <brief.json>` checks the arithmetic; the judgment pack is graded by reading.

Packs:

| Pack | Failure it tests | Grade |
| --- | --- | --- |
| [fiscal-calendar](fiscal-calendar/pack.md) | Rolling the target's EPS to the target date; mixing the dividend into the target or the tier; a June year end and a Monday cutoff | Code assertions plus a reading |
| [price-above-band](price-above-band/pack.md) | Chasing a price that has run ahead of unchanged estimates: raising forecasts or the target multiple toward the price-implied figure without evidence of a structural change | Reading only |

A pass on both says these two slips are absent in that run. It does not establish the method is right in general; repeat in a fresh session when the owning skills change.
