# Equity research workspace

Ordinary requests such as "initiation on X" and "update view on X" are complete mandates. Identify the rated security, information cutoff and research mode yourself; ask only for genuinely missing user intent or constraints. The analyst owns the assumptions and conclusion.

The skills are files, not automatically loaded tools. Read [research-cycle](skills/research-cycle/SKILL.md) and the relevant entry skill below. Read each stage's owner instructions when reaching that stage; follow deeper references only when relevant. Do not load the entire reference graph at the start.

- **Initiation:** use [stock-initiation](skills/stock-initiation/SKILL.md), in a new dated study. Use approved sources and documents expressly supplied for this request, including an inbox source pack and its evidence boundary. Do not inherit prior analyst forecasts or scan unrelated personal files.
- **Existing coverage:** use [model-revision](skills/model-revision/SKILL.md). Inspect eligible prior models, evidence, decisions and unresolved findings. Classify a regular review versus a material earnings/catalyst update; a price move alone does not revise operating assumptions.
- **Other work:** route through the research-cycle entry rather than forcing a stock initiation.

At study creation, pin the production rules before constructing the model:

```text
python -B -X utf8 skills/report-layout/scripts/research_rules.py pin STUDY
```

Keep that rule version through the run. After shared rules change, use `research_rules.py run STUDY HELPER ...` (or a study-relative builder) to execute the preserved version. Do not relabel contracts or reset old findings and attempts. Historical archives without a runtime receipt have an explicitly limited dependency provenance.

Follow the company sequence for modeling, governance, industry work, valuation and challenge. Each run gets one fresh review, after drafting, of the model, report and brief together; fix the blocking findings without a second read and leave minor ones. Deliver the human-readable Excel model, full report and one-page brief through the [publication workflow](skills/report-layout/references/publication-review.md).

The author session may launch the required fresh contexts through the host's available, authorized delegation tools. In Claude Code that is the Agent tool; other hosts use their supported equivalent. Tell each fresh context to work in batches as [research-cycle](skills/research-cycle/SKILL.md#continue-intelligently) sets out. Keep actual independent-reader work separate from self-review. If the host cannot provide it, retain an awaiting-review draft rather than fabricate completion. Skills do not themselves dispatch agents.

In Claude Code, launch each fresh context with an explicit model and effort; a context launched without them runs on the author's model at the session's effort.

| Role | Model | Effort |
| --- | --- | --- |
| Reviewer (model, report and brief) | The top non-Fable model: `opus` | `high` |
| Writer | The author's model | `high` |
| Mechanical helper (lookup, page fetch, extraction) | `sonnet` | `medium` |

When the author also runs on Opus, the reader is a fresh context on the same model and shares its blind spots; record it as a fresh same-model reader, not an independent one. Do not use `xhigh` or `max`: they add time and tokens for an uneven gain.

Prefer a slower run to one that uses tokens faster. Launch fresh contexts one at a time, do not split work across parallel helpers to save time, and do not turn on a faster output mode.

Keep production/retrieval times truthful and declare the session timezone with the research cutoff (`RESEARCH_TIMEZONE` or the release record's `timezone`; this workspace defaults to Asia/Singapore). Synthetic fixture clocks apply only to host-declared invented evidence packs. Supplied real-evidence snapshots retain their stated information cutoff and real timestamps.

## Standing instructions

When the user asks to remember something, or corrects how the research is done, write it into the owning skill under [skill calibration](skills/research-cycle/references/skill-calibration.md), in generic words. Do not keep it only in machine-local memory: another computer running these skills must behave the same way.
