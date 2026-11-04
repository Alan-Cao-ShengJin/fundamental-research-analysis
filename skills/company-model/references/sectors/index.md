# Sector research and modelling guide

Use these references to select the operating drivers, evidence and accounting checks
that matter for the company. They support the existing research sequence from
observations through assumptions and component forecasts to financial results.

## Select by the source of value and risk

Identify the activities generating material earnings, invested capital, cash or
future value. Choose the relevant reference by its economic mechanism, not the
company's label or stock-market classification. Use additional references only
for material activities requiring different drivers, accounting or valuation.
There is no fixed maximum: a diversified company may need several distinct
builds, but should not inherit every KPI mentioned across them.

An equipment supplier to mines uses industrial/equipment economics; owning mines
uses extraction economics. A battery factory is manufacturing, whereas an owned
power project and an EPC contract need different recognition and funding builds.
An online lender may need credit and capital analysis despite a software interface.
A hospital does not require drug-pipeline success probabilities unless it actually
owns a material development exposure. If no reference fits, adapt the nearest
mechanism and record what remains uncovered; do not force an unrelated template.

| Activity | Operating model to investigate | Reference |
| --- | --- | --- |
| Subscription/usage software | Retention and expansion, recognition, sales capacity and hosting cost | [Software](saas.md) |
| Chips, fabrication, memory, tools and IP | End demand/content, capacity/yield, inventory and capital cycle | [Semiconductors](semiconductors.md) |
| Devices, servers and contract manufacturing | Units, selling prices, material costs, channel inventory and services | [Hardware](hardware.md) |
| Ads, marketplaces and platforms | Impressions/price or GMV/net take, subsidies and segment cash | [Platforms](internet-platform.md) |
| Games, media and content rights | Payer/release cohorts, rights, content cash and amortisation | [Media](media-gaming.md) |
| Deposit-funded lending | Average balances/spreads, credit migration, liquidity and capital | [Banks](banks.md) |
| Underwriting and long-duration insurance | Current underwriting, reserve development, investment and capital | [Insurance](insurance.md) |
| Networks, acquiring, wallets and fintech credit | Net take rates, incentives, funding and loss cohorts | [Payments](payments-fintech.md) |
| Asset managers, exchanges and brokers | AUM/flow/activity, fee rates, cash spreads and regulatory capital | [Capital markets](capital-markets.md) |
| Rent ownership, development and mortgage investment | NOI/leases, AFFO, asset NAV and refinancing | [Property](reits.md) |
| Commercial drugs and development pipelines | Patient/net-price funnel, clinical milestones, rights and runway | [Pharma](pharma.md) |
| Care, devices, diagnostics and CRO/CDMO | Procedures/reimbursement, installed consumables and executable orders | [Healthcare services](healthcare-services.md) |
| Brands, stores and franchises | Sell-through, price/mix, store cohorts and franchise economics | [Consumer](consumer.md) |
| Machinery, projects and aftermarket | Orders/cancellations/acceptance, project costs and service base | [Industrials](industrials.md) |
| Vehicles, components and captive finance | Retail/wholesale, net unit contribution, utilisation and finance | [Autos](autos-ev.md) |
| Extraction, refining and contracted energy infrastructure | Decline, realised pricing, sustaining investment and contracts | [Energy](energy.md) |
| Regulated supply, owned generation and power projects | Rate base/earned return or output/PPA, approval and funding | [Utilities](utilities.md) |
| Mines and resource development | Ore/grade/recovery/payability, mine life, costs and closure | [Mining](metals-mining.md) |
| Telecom and towers | Active users/ARPU, network capex, spectrum and lease cash | [Telecom](telecom.md) |
| Aviation, shipping, rail, airports and logistics | Capacity/load/yield, supply deliveries, costs and commitments | [Transport](transport.md) |

## Use the references to construct assumptions

1. Establish a dated historical operating baseline and map each relevant operating metric to
   the exact period, units, perimeter, stock/flow, average/closing and gross/net
   definitions. Provider or broker terminology is not automatically the issuer's.
2. Identify what changes demand, price/mix, delivery, cost or capital for this
   activity. Gather the useful breakdown from filings, call detail, contracts and
   suitable outside observations. Keep inferred splits conditional.
3. Build [foundational estimates](../foundational-builds.md) locally with their
   evidence, reason, range and timing. Reconcile components to source totals and
   explain the latest observed profit/loss before extrapolating a new margin.
4. Link growth to capacity, service/engineering effort, working capital, required
   investment and funding. Use applicable capital/claim accounting: banking and
   insurance are not industrial working-capital templates.
5. Reuse completed results in the statements and selected valuation. Check
   important constraints and a coherent adverse case. Freeze observable operating
   predictions under the existing model/revision/monitor interfaces; a stock-price
   outcome alone does not validate their economics.

Apply the [shared foundational-build method](../foundational-builds.md): keep each
assumption, relevant history, explanation and source near the result it drives. Use
the established workbook theme and supported quarters or halves. Label reported
actuals, derived actuals, management guidance, third-party estimates and analyst
assumptions separately. An arithmetic tie does not establish that a component
allocation is true.

Select material questions and evidence rather than a quota of tables or indicators.
Keep missing data visible and identify any estimate used in its place. A report
mentioning a metric is not evidence that its economics have been examined. Use a
history, forecast horizon and valuation method appropriate to the activity and task.

The sector references supply methods, not forecast inputs. Establish any claimed
normal margin, cycle average, success probability or peer range from dated evidence.
Their synthetic examples cannot supply those empirical assumptions.

## Responsibilities within the research workflow

| Work | Owning skill and sector contribution |
| --- | --- |
| Sources and definitions | [Evidence intake](../../../evidence-intake/SKILL.md) retrieves and reconciles observations; the selected sector reference identifies useful questions and fields. |
| Forecast construction | [Company modelling](../../SKILL.md) owns the local operating builds, linked statements, capital, cash and shares. |
| Accounting and reporting concerns | [Financial quality](../../../financial-quality/SKILL.md) tests the sector-specific issues using the issuer's accounting basis. |
| Ownership and shareholder access | [Corporate governance](../../../corporate-governance/SKILL.md) owns control, related-party issues, restrictions and capital allocation. |
| Valuation and priced expectations | [Valuation](../../../valuation-thesis/SKILL.md) selects suitable methods and reconciles the claim being valued. Sector examples do not select a target price. |
| New coverage and updates | [Initiation](../../../stock-initiation/SKILL.md) establishes a baseline; [model revision](../../../model-revision/SKILL.md) preserves it and recalculates affected forecasts. |

A task to build or inspect a model does not require an unsolicited recommendation.
Full stock research continues through the existing challenge, decision and brief
skills. Sector references add no new rating threshold, report format or portfolio rule.

Accounting, tax, tariff, reimbursement, regulatory capital, product approvals and
licence rules vary by place and date. Check the current primary source for an
actual assignment. The references describe methods, not a current rules database.
Issuer filings/supplements are the usual starting point; regulator datasets,
technical reports, contracts and matched industry series then fill specific gaps.
Use [evidence intake](../../../evidence-intake/SKILL.md) and its existing
provider guide rather than assuming a new data connection from this directory.

## Tools and clean examples

[sector_plan.py](../../scripts/sector_plan.py) lists supported activities and
creates a blank scaffold by default. `--example` supplies an independently
invented arithmetic miniature from [sector examples](../../assets/sector-examples.json).
Each miniature makes its limited coverage explicit; none is a broker model,
empirical base rate or full forecast framework.

```powershell
python skills/company-model/scripts/sector_plan.py --list
python skills/company-model/scripts/sector_plan.py --sector banks --out output/bank-plan.json
python skills/company-model/scripts/sector_plan.py --sector transport --example --out output/transport-example.json
python skills/company-model/scripts/forecast_blocks.py output/transport-example.json --output output/transport-compiled.json
```

The existing compiler validates dependencies and performs arithmetic; the existing
workbook adapter can author a chosen compiled plan using the house theme. These
tools do not determine issuer applicability, estimate inputs or certify economic
completeness. A full company model still requires appropriate history, other
material activities, statements/capital, cash, shares and valuation. No Excel
files or source-collection jobs are created merely by reading a sector card.

## Integration boundaries

Formula conventions still need task-specific checks of ratios, units and double counting.

The other specialists retain responsibility for source access, financial
quality/governance, valuation, decision thresholds, portfolio sizing, reports
and monitoring. The house workbook, initiation/update distinction and user
output preferences continue to apply.

Adaptation credit and licence: [notice](NOTICE.txt).
