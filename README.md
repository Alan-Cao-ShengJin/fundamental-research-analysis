# Fundamental research analysis

A standalone backup of 15 English-language skills for full company fundamental research, adapted from research bundle 1.20.0. Start with [the research coordinator](skills/pip-research-cycle/SKILL.md), or use a specialist for a scoped question. [Skill overview](skills/README.md) and [catalog](skills/catalog.json).

The sequence is evidence and business context -> model setup/historical statements -> governance and early financial-red-flag review -> operating proxies and management guidance -> revenue/cost projections and linked financial forecasts -> model audit -> valuation/expectations -> thesis validation/challenge -> Buy/Hold/Sell, targets, risks and a compact report. [Detailed gates](skills/pip-research-cycle/references/company-sequence.md).

Severe governance threats to minority shareholders receive high-priority triage. Reporting/cash/asset red flags require evidence and alternative explanations; a ratio is not proof of fraud. Use reasoned estimates under uncertainty, distinguish win probability from payoff, and integrate market context by materiality. Hold is mandatory when primary-target price return is within -10% to +10%, inclusive, before rounding and excluding dividends.

## Included scope

Company modeling; evidence/provider retrieval; financial quality and red flags; governance; valuation and narrative; investment conclusions; macro/sector context; theme screening; company-change tracking; challenge; management questions; compact reporting; AntV visualization; company review; and the coordinating workflow. Portfolio allocation, risk-budgeting and cross-asset trading methods are outside this bundle.

Only maintained instructions, their supporting references/assets/scripts, synthetic examples, tests and license notices are included. Application code, company exercises, paid source payloads, personal paths, credentials, old imports and scratch archives are excluded.

## Use with an agent

Keep this repository's `skills/` tree together so sibling references and helper imports resolve. Give the agent this repository and the research coordinator entry point. When installing in another skill directory, retain the full sibling tree plus the `lib/` helpers required by scripts; copying only SKILL.md omits important methods. The agent reads relevant references on demand rather than all skills at once.

Research outputs use English by default unless requested otherwise. AlphaPai material is generally Chinese: retain originals and source locators, and translate into the preferred language while preserving units, speaker roles and qualifications.

## Local checks and helpers

Node.js 24.13+ and Python 3.11+ are supported. Python helpers use the standard library; chart rendering may need separately selected, version-pinned AntV packages.

```powershell
npm ci
npm run skills:check
npm test
python -B -m unittest discover -s skills/tests -p "test_*.py"
```

The checks cover links, metadata, dependencies, schema consistency and numerical/retrieval behavior. They do not certify investment performance, source truth or that a live research worker exists. Behavioral cases are specifications, not automatically passed model evaluations.

## Optional data-source setup

Copy `.env.example` to `.env.research-data` locally and populate only the providers you use. Credentials can also come from process environment. Never commit them. The [bounded provider adapter](skills/pip-evidence-intake/scripts/research_data.py) supports AlphaPai, Alpha Vantage, API Ninjas and Massive; its [guide](skills/pip-evidence-intake/references/research-data-providers.md) and [catalog](skills/pip-evidence-intake/assets/provider-endpoints.json) describe routes and limits. `PROVIDER catalog` makes no network request.

```powershell
python -B -X utf8 skills/pip-evidence-intake/scripts/research_data.py alphapai catalog
```

Configured credentials do not establish complete coverage or product/field entitlement. No provider key, subscription, runtime integration, active monitoring or trading authority is supplied.

See [third-party notices](THIRD_PARTY_NOTICES.md) for source attribution and retained license notices. This scoped backup preserves the upstream research methods while removing unrelated trading/portfolio routes and machine-specific claims.
