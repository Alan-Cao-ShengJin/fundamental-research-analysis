# Global data planning

Requirements for a reusable worldwide data foundation, covering **81 source families**, **20 sector activities** and **8 research-capability priorities**. These are source candidates and requirements; this directory does not activate integrations or establish complete country coverage.

| File | Use |
| --- | --- |
| [Human-readable brief](Global_data_and_research_capabilities_brief_2026-11-02.html) | Download and open in a browser for the searchable source catalogue, sector maps, build order and remaining research capabilities. |
| [Source catalogue](global_source_catalog.json) | Fields, geography, frequency, access, primary URLs, assumption use and limitations. |
| [Sector requirements](sector_assumption_requirements.json) | Observations and source mappings for all twenty activity guides, including what remains issuer-specific. |
| [Proposed observation contract](proposed_observation_contract.json) | Identity, time, meaning, quality, lineage and acceptance requirements. |
| [Research-capability gaps](research_capability_gaps.json) | Work to strengthen alongside data engineering; these are plans, not completed skills. |
| [Data-engineering prompt](data_engineering_prompt.txt) | A self-contained prompt/project brief for Tim or another data-engineering lead. |

## First implementation

Begin with a global schema and explicit coverage matrix, then select a small source set with high cross-sector reuse. Preserve raw snapshots and publication/revision histories before scaling. Regional official statistics and sector feeds extend the shared design; match data to operating exposure rather than listing location.

Validate source availability and rights with samples. Public access, API access, complete historical coverage and permitted bulk/internal use are different checks. Selected commercial products fill specific gaps; this is not an instruction to subscribe to every product listed.

Data engineering owns acquisition, normalization, vintage preservation and feed quality. Research owns proxy relevance, calibration, assumptions, models and economic review. Industry data informs those judgments without supplying every company-specific parameter.

Source documentation was reviewed on **2 November 2026**. No new production ingestion, entitlement trial or live-agent investment-quality benchmark is claimed. The capabilities and mandate remain defined by the [research coordinator](../../../skills/research-cycle/SKILL.md) and [decision contract](../../../skills/investment-conclusion/references/decision-contract.md).
