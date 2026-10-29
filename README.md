# Fundamental Research Analysis

Reusable agent skills for researching a listed company, building an executable financial model, assessing shareholder risks and reaching a clear investment decision.

The repository contains **15 English-language skills** from research bundle **1.20.0**, with the references, scripts, synthetic examples and tests they need. It focuses on company fundamental research; portfolio allocation and trading execution are separate workflows.

## Start here

Give your agent this repository and ask it to read [the research coordinator](skills/pip-research-cycle/SKILL.md). It should load the relevant specialists and references as the work progresses.

Example request:

> Research COMPANY (TICKER, EXCHANGE) at the current price using the fundamental-research workflow. Build the operating and financial model, assess governance and financial red flags, select suitable valuation methods, challenge the thesis, and produce a compact decision brief plus a visual research report with supporting evidence.

Keep the complete `skills/` tree together. Copying only individual `SKILL.md` files omits supporting methods and can break sibling links and helper imports.

## Research sequence

| Stage | Main work |
| --- | --- |
| 1. Frame and gather evidence | Confirm the security, business model, price, horizon and source coverage; understand current company and market context. |
| 2. Establish the model baseline | Set up semantic definitions and reconcile historical income statements, cash flows and balance sheets. |
| 3. Review governance and red flags | Examine minority rights, control, allocation and reporting reliability before relying on the baseline for forecasts. |
| 4. Build operating assumptions | Collect operational proxies, management guidance and relevant peer evidence; substantiate volumes, prices, margins and investment needs. |
| 5. Construct forecasts | Link revenue and cost projections to funded, integrated financial statements and scenarios. |
| 6. Audit the model | Check statement links, cash, financing, shares, assumptions and the treatment of flagged issues. |
| 7. Value the company | Choose methods suited to its economics; assess relevant peers, its own historical forward valuation and price-implied expectations. |
| 8. Validate and challenge | Test the provisional thesis, persistent-discount case, strongest counterargument and probability versus payoff. |
| 9. Decide and communicate | State Buy, Hold or Sell, a primary target and horizon, scenario returns, one key thesis sentence and what would change the view. |

The financial-quality skill performs **three distinct passes**: early red-flag screening, model audit and post-valuation validation. Shared evidence and issue IDs carry across those passes.

[Detailed stage gates](skills/pip-research-cycle/references/company-sequence.md) ? [Machine-readable catalog](skills/catalog.json)

## Included skills

| Role | Skill |
| --- | --- |
| Workflow coordination | [Research cycle](skills/pip-research-cycle/SKILL.md) |
| Evidence and provider retrieval | [Evidence intake](skills/pip-evidence-intake/SKILL.md) |
| Operating models and linked financial statements | [Company model](skills/pip-company-model/SKILL.md) |
| Accounting, cash and financial red flags | [Financial quality](skills/pip-financial-quality/SKILL.md) |
| Minority rights, control and value realization | [Corporate governance](skills/pip-corporate-governance/SKILL.md) |
| Valuation, narratives and expectations | [Valuation thesis](skills/pip-valuation-thesis/SKILL.md) |
| Stock call, targets and investment rationale | [Investment conclusion](skills/pip-investment-conclusion/SKILL.md) |
| Counterarguments and evidence testing | [Research challenge](skills/pip-research-challenge/SKILL.md) |
| Decision-sensitive issuer questions | [Management questions](skills/pip-management-questions/SKILL.md) |
| Concise investor communication | [Research brief](skills/pip-research-brief/SKILL.md) |
| Consistent AntV charts and diagrams | [Chart visualization](skills/pip-chart-visualization/SKILL.md) |
| Macro transmission and sector context | [Macro event analysis](skills/pip-macro-event-analysis/SKILL.md) |
| Candidate and value-chain discovery | [Theme screening](skills/pip-theme-screening/SKILL.md) |
| Disclosure changes and model revisions | [Company change tracking](skills/pip-company-change-tracking/SKILL.md) |
| Proposed follow-up and outcome review | [Monitor and review](skills/pip-monitor-review/SKILL.md) |

## Investment and reporting principles

- Use reasoned estimates under imperfect information. Distinguish evidence, management expectations and analyst judgment.
- Give severe governance threats to minority shareholders high-priority attention. Financial anomalies require investigation and alternative explanations; an unusual ratio is not proof of fraud.
- Judge the whole company. Latest results and the next outlook inform near-term catalysts alongside durable economics, governance, valuation and market context.
- Separate the probability of business success from the investment payoff available at the current price.
- Use **Hold when primary-target price return is between -10% and +10%, inclusive**, before rounding and excluding dividends. Incomplete valuation is not a Hold fallback.
- Default to a **250-350-word decision brief** and an **800-1,200-word visual main report**, with detailed models and evidence linked separately. Explain the business, moat, pivotal thesis and material risks concisely.

English is the default output language. AlphaPai material is generally Chinese: preserve original evidence and locators, then translate into the user's preferred language without changing units, attribution or qualifications.

## Optional data connections

The [provider adapter](skills/pip-evidence-intake/scripts/research_data.py) supports registered read-only routes for **AlphaPai, Alpha Vantage, API Ninjas and Massive**. Follow the [provider guide](skills/pip-evidence-intake/references/research-data-providers.md) for question-based routing, source interpretation and access limits.

Copy [.env.example](.env.example) to `.env.research-data` locally and supply only the keys you use, or set the corresponding environment variables. Credentials and provider response files are ignored by Git. No credentials or subscriptions are included; coverage and entitlement vary by endpoint and field.

List registered operations without making a network request:

```powershell
python -B -X utf8 skills/pip-evidence-intake/scripts/research_data.py alphapai catalog
```

## Run the checks

The instructions can be read directly. To run the included helpers and checks, use **Node.js 24.13+** and **Python 3.11+**. Python helpers use the standard library; rendering charts may require separately selected AntV packages.

```powershell
npm ci
npm run skills:check
npm test
python -B -m unittest discover -s skills/tests -p "test_*.py"
```

Checks cover structure, links, dependencies, handoff schemas and calculation/retrieval behavior. They do not establish source truth, investment performance or forensic assurance. Proposed watches do not activate a monitoring service.

## Repository scope and attribution

This repository stores maintained skills and their supporting tools. Application code, company research exercises, proprietary source payloads, credentials and raw historical imports are excluded. Portfolio allocation, risk budgeting and cross-asset trading skills are outside this bundle.

[Third-party notices](THIRD_PARTY_NOTICES.md) retain attribution and license notices for adapted methods. The [bundle manifest](bundle-manifest.json) records the initial backup snapshot; subsequent documentation edits do not change that historical record.
