# Set up the company model

Establish model identity, reporting definitions and a calculation backend before populating actuals or projecting revenue.

## Choose the model state and calculation backend

Start with the [agent-model contract](agent-model.md): stable metric/period IDs, evidence and assumptions, executable dependencies, versioned runs and checks. Choose an available backend that can actually recalculate the issuer model. It can initially be Excel plus a semantic map; the agent need not navigate the human presentation to query inputs/outputs. A code-based economic model is also valid. Preserve an auditable mapping when importing a workbook.

- Follow the [workbook contract](workbook-profile.md) for the synchronized human and machine interfaces. A scoped query can reuse a current model without rebuilding it.

Resolve missing inputs and material formula errors before declaring a model ready. Do not suppress undefined ratios or missing data by returning zero.

## Establish a period and metric map

Record company/entity, fiscal year-end, accounting framework, reporting currency and scale, valuation currency and FX purpose, annual/interim cadence, last actual period and forecast horizon. Keep published, derived, guidance, assumption and broker-estimate classifications separate.

Map rows by meaning rather than fixed cell coordinates. Repeated labels such as Other income require explicit issuer-specific account definitions.

Represent annual and interim periods explicitly. In a workbook, keep period columns and the actual/forecast boundary readable. Use each statement's supported cadence; an issuer may report interim earnings but only annual balance-sheet or cash-flow detail. Do not invent undisclosed quarterly statements.

## Standard workbook components

| Component | Role |
| --- | --- |
| Cover and Summary | Model details, case selector, colour legend, sheet index, check status; the call, target and key outputs |
| Statements | Historical and forecast IS/CF/BS, EPS/DPS, assumptions, roll-forwards and checks |
| Revenue Build or UE | Business-specific segment demand, price, revenue, costs, margins and unit economics |
| Data and relevant price tabs | Source operating observations, tracker aggregation and matched benchmarks |
| Guidance | Attributed and dated management statements; retain conflicting or unverified items |
| Questions | Decision-sensitive gaps, model sensitivity and answer tracking |
| Valuation | Model-linked investment conclusion after valuation and validation |
| Valuation Band | Historical valuation context when suitable dated inputs exist |
| Scenarios | Bear/Base/Bull driver values with the active case chosen by the selector |
| Checks | Every model check in one place, with the failing count shown on each sheet |

These are functional components, not mandatory sheet names. Preserve valid existing names and check dependencies before replacing or retiring a component.

## Preserve features and authority

Fingerprint the starting file and inventory hidden sheets, charts/images, control or drawing parts, names, external links, RTD/vendor formulas and extensions. The bundled [inspector](../scripts/inspect_workbook.py) reads the OOXML package without recalculation, refresh or source writes:

```powershell
python skills/company-model/scripts/inspect_workbook.py "path/to/model.xlsx" --output "path/to/inspection.json"
```

The inspector samples formulas and numeric inputs across all sheets and reports observed formatting. It does not classify actuals or assumptions from colours; establish those classifications from source definitions and the model's documented legend.

Read [workbook-profile.md](workbook-profile.md) before editing. Open/lock and fingerprint checks protect intervening user changes. Structural inspection does not require external-data refresh or macro execution. Choose a compatible writer and calculation engine based on actual workbook features.

Setup is complete when the model version, period/metric map, dependencies and calculation backend exist, and, for an imported workbook, its working copy and preservation plan. Setup does not mean the model is populated, calculated or reconciled.
