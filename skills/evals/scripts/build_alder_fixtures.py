"""Generate invented distributor evidence and two later evidence-only updates; no real issuer inputs."""
import json
from pathlib import Path

FIXTURES = Path(__file__).resolve().parents[1] / 'fixtures'


def half(period, core, orders, core_gp, core_opex, joint, joint_opex, corporate=10, finance=2):
    joint_gp = joint * .22
    core_op, joint_op = core_gp - core_opex, joint_gp - joint_opex
    pre_tax = core_op + joint_op - corporate - finance
    tax, minority = pre_tax * .2, joint_op * .8 * .4
    return dict(period=period, coreRevenue=core, coreOrders000=orders, coreGrossProfit=core_gp, coreOpex=core_opex,
                jointRevenue=joint, jointGrossProfit=joint_gp, jointOpex=joint_opex,
                corporateCost=corporate, netFinanceCost=finance, preTax=pre_tax, tax=tax,
                groupProfit=pre_tax-tax, minorityProfit=minority, attributableProfit=pre_tax-tax-minority,
                shares=100, eps=(pre_tax-tax-minority)/100)


def data():
    history = [half('1H FY2025',600,600,156,105,200,24), half('2H FY2025',642.6,630,167.076,108,220,26),
               half('1H FY2026',676,650,175.76,111,220,26), half('2H FY2026',682.5,650,191.1,114,240,28)]
    q1 = half('1Q FY2027',350,335,91,58,125,14,5,1)
    h1 = half('1H FY2027',720,680,187.2,120,250,29,10.3,2)
    balances = {
        'FY2025': dict(cash=60,receivables=180,inventory=240,ppe=140,rou=30,otherAssets=30,
                       payables=150,accruals=60,debt=150,leases=30,parentEquity=270,minorityEquity=20),
        'FY2026': dict(cash=100,receivables=190,inventory=260,ppe=156,rou=30,otherAssets=30,
                       payables=160,accruals=64,debt=156.352,leases=30,parentEquity=326.944,minorityEquity=28.704),
        '1H FY2027': dict(cash=139.52,receivables=205,inventory=238,ppe=164,rou=30,otherAssets=30,
                          payables=162,accruals=66,debt=161.352,leases=30,parentEquity=353.344,minorityEquity=33.824)}
    cash = {
        'FY2025': dict(operating=118,capex=24,leasePrincipal=10,parentDividends=45,minorityDividends=4.8,
                       netBorrowing=.8,openingCash=25,closingCash=60,jointAfterInvestment=22,jointDividends=12),
        'FY2026': dict(operating=138.048,capex=28,leasePrincipal=10,parentDividends=60,minorityDividends=6.4,
                       netBorrowing=6.352,openingCash=60,closingCash=100,jointAfterInvestment=27,jointDividends=16),
        '1Q FY2027': dict(operating=82.4,capex=7,leasePrincipal=2.5,jointAfterInvestment=8,jointDividends=4.8),
        '1H FY2027': dict(operating=87.72,capex=15,leasePrincipal=5,parentDividends=30,minorityDividends=3.2,
                          netBorrowing=5,openingCash=100,closingCash=139.52,jointAfterInvestment=14,jointDividends=8)}
    pe = [16,16.2,16.5,16.8,17,17.5,18,18.3,18.1,17.8,17.4,17,
          17,17.3,17.5,17.9,18.1,18,17.6,17.2,17,16.8,16.5,16.2,
          16,15.8,16.1,16.4,16.8,17,17.2,17,16.5,16.2,15.9,15.7]
    return history, q1, h1, balances, cash, pe


def table(rows):
    fields = ['period','coreRevenue','coreOrders000','coreGrossProfit','coreOpex','jointRevenue','jointGrossProfit',
              'jointOpex','corporateCost','netFinanceCost','preTax','tax','groupProfit','minorityProfit','attributableProfit','eps']
    out = ['| '+' | '.join(fields)+' |', '| '+' | '.join(['---']*len(fields))+' |']
    for row in rows:
        out.append('| '+' | '.join(str(round(row[k],6)) if isinstance(row[k], (int,float)) else row[k] for k in fields)+' |')
    return '\n'.join(out)


def write():
    history, q1, h1, balances, cash, pe = data()
    initial = FIXTURES / 'alder-industrial-supply'; initial.mkdir(parents=True, exist_ok=True)
    initial_facts = {'reportedHalves': history, 'latestQuarter': q1,
        'balanceSheets': {k: balances[k] for k in ('FY2025','FY2026')},
        'cashFlows': {k: cash[k] for k in ('FY2025','FY2026','1Q FY2027')},
        'monthlyNtmPe': pe, 'historyStart': '2023-11',
        'quote': {'price':19.2,'date':'2026-11-06','shares':100},
        'consensus': {'FY2027':1.25,'FY2028':1.38,'date':'2026-11-09'}}
    (initial/'facts.json').write_text(json.dumps(initial_facts,indent=2)+'\n',encoding='utf-8')
    (initial/'pack.md').write_text('''# Alder Industrial Supply (ALDR): synthetic evidence

Everything in this pack and `facts.json` is invented. No issuer, counterparty, price or estimate is real. Use these files only as evidence. Research cutoff: 9 November 2026. Reporting currency USD; money is millions except per-share data and order values. Fiscal year ends 30 June, named by its ending year. Quarters end September, December, March and June. Shares: 100m throughout; no options, convertible or planned share change.

## Business, ownership and value chain

Alder is a US-listed industrial maintenance distributor. Its wholly owned Core division buys mechanical parts from manufacturers, keeps local stock and supplies factories under recurring maintenance contracts and spot orders. It owns no factories. Reported order counts include contract releases; average revenue per order includes mix, not a pure price index. Core revenue / orders in thousands x 1,000 gives dollars per order. It cannot identify end-customer production from one order count.

The consolidated Joint division distributes factory consumables in a neighboring region. Alder owns 60%; a local partner owns 40%. Tax is 20% for both divisions; minority profit is 40% of Joint operating profit after tax. Corporate costs and net finance costs belong to Alder's parent shareholders. Joint has no separate interest cost. Related-party sales are zero. Founder holds 8%, independent chair since 2022; no controlling holder. No material transactions or changes of ownership since 2018. There are 40 service depots in both FY2025 and FY2026; depot counts alone do not drive sales.

Core contracts represented 75% of FY2026 Core sales; the rest were spot orders. Three newly won multiyear maintenance contracts, disclosed 20 October 2026, have total expected annual revenue of $60m once fully implemented in January 2027. The amount is expected sales, not guaranteed backlog: customers can adjust release quantities. It sits inside management's full-year growth outlook. The company is not sole supplier.

## Reported financial results

FY2026 annual results published 18 August 2026; 1Q FY2027 trading/financial update published 27 October 2026. Halves are additive; full precision appears in facts.json. Divisional opex includes depreciation and lease depreciation; corporate cost is separate. Net finance cost includes lease interest; cash interest and tax are within operating cash flow.

'''+table(history+[q1])+'''

FY2026 second-half Core gross profit includes a **$13.65m one-off supplier rebate settlement** for purchases made in prior periods. The settlement was cash received in June and is included once in operating cash flow. It is not a customer price increase or a new recurring margin. No similar settlement existed in FY2025. Full-year GAAP profit and EPS above include it; no other adjustments are disclosed. Annual basic EPS is annual attributable profit divided by 100m shares. Group gross profit is the sum of the two divisions.

Balance sheets and cash flows are in facts.json. Balance sheet cash is consolidated and includes Joint cash of $9m at FY2025 and $20m at FY2026. FY2026 Core/parent cash is therefore $80m. There is no parent cash restriction. Joint cash is held locally, with an $8m operating-cash covenant; additional distributions require unanimous Joint board approval. Only the reported distributions were approved. Parent economic ownership of Joint cash does not mean the cash has been remitted.

FY2026 operating cash flow of $138.048m equals group profit $132.048m plus depreciation $22m less working-capital absorption $16m. Depreciation is $12m on PPE and $10m on right-of-use assets. PPE capex is $28m; lease principal is $10m. Parent dividends are $60m; cash dividends to the partner are $6.4m; net new borrowing is $6.352m. FY2025 parent dividends were $45m. Lease principal is not already deducted from operating cash flow. No buyback occurred.

Joint generated $27m of cash after its own capex and leases in FY2026, included in group cash. It distributed $16m in total ($9.6m to Alder, $6.4m to the partner) and retained $11m. For FY2027, the Joint board has approved distributing **60% of Joint cash after its capex/leases**, provided the covenant holds; it has not approved release of previously retained cash. Parent dividend policy is 45-55% of attributable reported earnings, reviewed annually.

## Latest cash and operating update, 27 October 2026

1Q FY2027 CFO was $82.4m, including a $40m inventory reduction and a temporary $20m supplier payment extension, partly offset by a $16m receivables increase. D&A was $6m. Inventory fell from $260m to $220m. The extra supplier terms reverse in 2Q FY2027. Capex was $7m and lease principal $2.5m. Management expects some restocking: FY2027 year-end inventory about **$240m**, receivables 38-40 days of sales, normal supplier terms, no further exceptional extension.

## Management FY2027 outlook

At the August results, reiterated 27 October: Core revenue +4-6%, approximately flat transaction pricing with contract wins and volume providing growth; Core gross margin **26-27% excluding exceptional settlements**. Core opex +4%. Joint sales/order volume +8-10%, price flat, gross margin about 22%, opex +7%. Corporate costs +3%. Capex about $30m; no new lease expansion. No FY2028 outlook. The outlook is a range, not an earnings guarantee. No backlog amount beyond the contracts above, competitor capacity or customer-specific production data is supplied.

## Independent industry and peers

An invented independent survey of 350 industrial buyers published 30 October reports maintenance-spend volume flat in FY2026 and +1% in 1Q FY2027; factory output index grew 0% and -1% respectively. The published methodology covers a buyer sample. Distributor replacement-part input prices were +3% in FY2026 and flat in September 2026. No market-share level is supplied.

Same-market listed distributors, all June year ends; consensus as of 6 November 2026:

| Peer | FY2027 P/E | FY2027 EPS growth | Maintenance-contract sales | Operating margin | ROIC | Net debt/EBITDA |
| --- | --- | --- | --- | --- | --- | --- |
| Harbor Supplies | 16x | 10% | 80% | 10% | 18% | 1.0x |
| Cobalt Logistics | 13x | 7% | 45%, rest project supply | 7.5% | 13% | 1.5x |
| Rill Service | 18x | 12% | 85% | 12% | 23% | 0.5x |

Peer P/E and EPS exclude exceptional supplier settlements, use attributable earnings and match June FY2027. The other ratios are normalized FY2027 consensus on the same lease convention (leases excluded from net debt, lease cash remains an operating cost). No peer cash-yield series is provided.

## Price, expectations and history

Close 6 November: **$19.20**, 100m shares; 52-week range $15.40-23.80. Consensus as of 9 November, 12 contributors: FY2027 adjusted EPS **$1.25**, FY2028 **$1.38**, target $22.00. Vendor EPS excludes exceptional supplier rebates. Detailed contributor assumptions and dispersions are unavailable. Treasury yield 4.0%; no other macro or sector-flow change disclosed.

The 36 monthly forward P/E observations in facts.json run chronologically from November 2023 through October 2026, on point-in-time consensus NTM attributable adjusted EPS. No older history, daily prices or index series is supplied. Business perimeter was unchanged over this interval. There is no announced lasting regime change; price/input and working-capital cycles can still affect the relevant anchor. Treat choice of valuation method and central assumptions as analysis, not a prescribed call.
''',encoding='utf-8')
    regular = FIXTURES/'alder-regular-update'; regular.mkdir(parents=True,exist_ok=True)
    (regular/'pack.md').write_text('''# Alder Industrial Supply: 2 December 2026 evidence

Synthetic exercise. Use this pack with the frozen eligible prior research/model supplied under research/. No real issuer data. Fiscal year ends June; all values USD. Cutoff 2 December 2026.

Close 1 December: $22.50 (100m unchanged shares), versus $19.20 on 6 November. The same 12-contributor vendor snapshot refreshed 2 December still has FY2027 adjusted EPS $1.25 and FY2028 $1.38. No new results, trading update, contracts, ownership change or guidance since the 27 October statement. An IR calendar notice on 30 November says 2Q results are expected in February, date unconfirmed; it contains no trading information. Rates and peer estimates are unchanged; no new evidence of a valuation-regime change is supplied. There is no post-October monthly valuation history in this closed pack.

The 9 November evidence remains the latest operating information. No external material is included in this closed exercise.
''',encoding='utf-8')
    earnings = FIXTURES/'alder-earnings-update'; earnings.mkdir(parents=True,exist_ok=True)
    (earnings/'facts.json').write_text(json.dumps({'reportedHalf':h1,'balanceSheet':balances['1H FY2027'],
        'cashFlow':cash['1H FY2027'],'price':18.1,'priceDate':'2027-02-09'},indent=2)+'\n',encoding='utf-8')
    (earnings/'pack.md').write_text('''# Alder Industrial Supply: 10 February 2027 evidence

Synthetic exercise. Use this pack and facts.json with the frozen eligible baseline supplied under research/. Fiscal year ends June; currency USD millions except EPS. Cutoff 10 February 2027. No real issuer data or external lookup.

## Official 1H FY2027 results, published 9 February 2027

'''+table([h1])+'''

The half is cumulative and includes the previously reported first quarter. There is no exceptional supplier settlement this year; the comparable 1H FY2026 had none either. The FY2026 second-half $13.65m settlement remains a historical one-off.

Closing balances and cash flows are in facts.json. CFO $87.72m equals group profit $64.72m + D&A $12m - receivables increase $15m + inventory reduction $22m + payables increase $2m + accrual increase $2m. D&A comprises PPE $7m and ROU $5m; cash interest/tax are already in CFO. Capex $15m, lease principal $5m, parent dividends $30m, partner dividends $3.2m, net borrowing $5m, cash increased from $100m to $139.52m. Joint cash after its investment/leases was $14m and total Joint distributions $8m; retained Joint cash rose from $20m to $26m. Access and partner rights are unchanged.

The first-quarter $20m temporary supplier extension was reversed as announced. Inventory is $238m, after reaching $220m in September; management restocked $18m. No cash-flow restatement occurred.

## Revised FY2027 outlook, same release

Core revenue +3-4% (previously +4-6%), Core gross margin 25-26% (previously 26-27%), Core opex +7-8% (previously +4%). Management attributes labor/service costs to contract implementation; that explanation is not separately audited. Joint volume +9%, price flat, gross margin 21.5-22%, opex +8%. Corporate costs +3%. FY2027 capex remains $30m and inventory target about $240m, receivables 38-40 days, normal supplier terms. No FY2028 outlook or new contract beyond those already disclosed. Dividend policy and JV distribution rights unchanged.

## Market inputs

Close 9 February **$18.10**, unchanged 100m shares. Latest available consensus snapshot is **8 February, before these results**: FY2027 adjusted EPS $1.25, FY2028 $1.38, 12 contributors. A post-results consensus revision is not available. The peer snapshot and historical valuation data remain those in the prior pack; no new peer/regime evidence was supplied.

No additional issuer disclosures are included in this pack.
''',encoding='utf-8')


if __name__ == '__main__':
    write()
    print('Wrote three synthetic Alder evidence packs and their raw facts.')
