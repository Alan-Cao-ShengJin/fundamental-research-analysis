---
name: pip-financial-quality
description: Analyse issuer financial statements, financial red flags and potential reporting manipulation; reconcile earnings, assets, cash and financing; and test research theses. Use for early reporting-reliability screens, full statement reviews, cash-authenticity questions, account investigations and model audits.
metadata:
  version: 1.11.0
---

# Financial quality and statement challenge

Use issuer statements and notes directly for a scoped review, and reconciled actuals/forecasts from the [company-model branch](../pip-company-model/SKILL.md) when available. Return a [financial-quality handoff](../pip-research-cycle/references/handoffs.md). This branch does not apply a corporate-accounting template to a commodity, currency or token.

## Choose the pass

- **Early financial-red-flag screen, before forecasts:** use the [red-flag procedure](references/financial-red-flags.md) on available statements/notes, audit evidence and business observations. Identify material reporting, asset, cash and financing concerns before relying on the baseline. Coordinate overlapping controller/related-party issues with governance; retain one issue ID and economic loss mechanism. A focused screen can use filings directly without a full model.
- **Standalone statement analysis:** review a filing, earnings preview, selected account or peer comparison at the requested depth. Read [statement review modes](references/statement-review.md) for full coverage, drilling down and preliminary disclosures. A narrow accounting question does not require a new valuation.
- **Model audit, before valuation:** review the assembled actuals/forward model, its cash/financing consistency, assumptions and comparable consensus differences. Incorporate [governance findings](../pip-corporate-governance/SKILL.md) affecting cash access, related-party transfers, issuance, compensation and allocation. Fix material errors before valuation.
- **Thesis validation, after valuation:** test priced expectations and the provisional thesis against financial, operating, industry and governance evidence. Check whether minority shareholders can receive the cash and whether the assumed discount closure is credible. Reuse the audit and expand only decision-driving issues.

Use distinct artifact IDs for these passes. Do not write two complete financial reports or require a finished valuation thesis merely to audit the model.

Compare financial delivery with priced expectations during post-valuation thesis validation. Keep the pre-valuation model audit independent so a desired valuation does not become an accounting assumption.

## Review material drivers and anomalies

Anchor earnings reviews to the [latest-versus-next-period clock](../pip-company-model/references/earnings-clock-and-peer-readthrough.md). Test the latest actuals, current outlook and implied remaining/next-period economics against seasonal/cycle history and comparable already-reported peers. Avoid giving old periods equal narrative weight, extrapolating one-off changes or confusing a peer signal with issuer evidence. Preserve pre-event estimates and source availability before labeling a surprise.

Identify material changes in amount and business significance, not just a universal percentage threshold. Small bases can make a large percentage unimportant; a stable but large liability can matter greatly. For each important issue explain: observation and period, plausible causes, supporting/counterevidence, historical/peer context, decision impact and next verification.

Cover the statements as a connected system:

- **Revenue and working capital:** recognition policy, receivables/contract assets, cash receipts, customer concentration, inventories and supplier terms. Distinguish cash collection, recognition and indirect taxes.
- **Profit and earnings quality:** price/mix/cost bridges, recurring versus adjusted earnings, associates, minorities, incentives, impairments and tax. Reproduce the issuer's adjustment bridge before adopting an alternative definition.
- **Productive assets and investment:** capex, construction-to-PPE transfers, utilisation, depreciation, capitalised R&D, acquisitions, goodwill and impairment assumptions.
- **Cash flow:** bridge net income to operating cash through noncash items and working capital; distinguish maintenance/growth capex where evidence permits; reconcile investing/financing cash and FX to the reported cash definition.
- **Financing and obligations:** unrestricted versus restricted cash, debt maturities, covenants, lease obligations, guarantees, refinancing dependence and contingent claims. Profit does not establish liquidity.
- **Equity and per-share claims:** changes in ownership, issuance/buybacks, dilution, payout and related-party transactions.

Ratios and heuristics are investigation triggers, not automatic quality scores or proof of fraud. Banks, insurers and other specialised businesses need sector-appropriate statements and valuation methods. Read the issuer's applicable accounting framework rather than forcing a universal chart of accounts.

## Connect to the thesis without confirmation bias

Carry the same [red-flag records](references/financial-red-flags.md) through the early screen, model audit and thesis validation, using separate pass artifact IDs/versions. Prioritize severe governance threats to minority claims; financial fraud/reliability signals are an additional risk lens that can independently become decisive. Separate potential severity, evidence confidence and resolution status. Investigate cash existence, ownership, usability and distributability rather than equating a large bank balance or high cash plus debt with fraud. Do not let a score or cheap multiple offset a critical issue, and do not require perfect information for ordinary forecast assumptions.

Use [source and economic validation](../pip-research-cycle/references/empirical-research-and-validation.md) to verify pivotal claims and reproduce key calculations from original observations. Assess [returns on additional investment](../pip-company-model/references/competition-and-capital-returns.md): acquisition/organic spending, maturation, capital definitions, financing and per-share effects. Distinguish profitable growth from expansion that fails to earn an adequate return. Record review scope and unresolved judgments; structural checks do not establish research quality.

Apply the [cash and economic tests](../pip-research-cycle/references/underwriting-standard.md): explain large remaining-period cash recoveries, sustainable working capital, investment/asset lives, compensation and net dilution, and restrictions on common-share distributions. Distinguish observed schedules from aggregate proxies. Test whether plausible critical inputs overturn the conclusion, not merely whether the model calculates or reconciles. A missing regulatory-capital disclosure cannot be resolved by a balanced proxy schedule.

Perform the model audit before relying on its outputs in valuation. After valuation, ask which specific thesis assumptions are supported, contradicted or untested. Avoid declaring every financial change a narrative confirmation. Preserve an alternative benign explanation and an adverse explanation for suspicious patterns.

Cash flow is not immune to classification or timing effects. Higher operating cash than net income is not automatically superior; working-capital release or delayed supplier payment can be temporary. A receivable increase or large impairment does not, by itself, establish manipulation.

Do not force expenses, reserves, provisions or segment data to fit an investment conclusion or incentive threshold. Carry unresolved issues into forecast assumptions, ranges and concrete follow-up tests. Reserve decision blockers for missing essentials that prevent meaningful estimation; ordinary uncertainty or an adverse case is not itself a reason to withhold a call.

## Handoff

Provide the relevant statement/cash bridges, review coverage, referenced red-flag issue records and dispositions, material findings and evidence, alternative explanations, forecast constraints, sensitivities, essential unresolved dependencies and affected downstream artifacts. A full financial review includes cash flow and financing as well as earnings and the balance sheet. Escalate material new evidence at any stage and reopen affected forecasts/values; an earlier no-flag screen is not continuing assurance.

A balanced workbook or a completed checklist is insufficient evidence of financial quality. Do not claim a fraud finding without adequate corroboration. The analysis can be complete while the investment case remains unproven.
