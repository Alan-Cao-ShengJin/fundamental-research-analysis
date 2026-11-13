# Innovative drugs and biotech

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

A drug owner earns in three ways, and most companies mix them.

- **Selling its own drugs.** Doctors prescribe, patients take the drug, and an insurer or
  a government pays most of the bill.
- **Selling rights.** A partner pays for the right to develop or sell a drug in some
  markets: a payment up front, more when milestones are reached, and a royalty on sales.
- **A pipeline** of drugs still in trials, which earns nothing yet and costs money until
  each one succeeds or fails.

Four parties decide demand. The regulator decides whether the drug can be sold and for
which patients. The payer decides whether it is reimbursed and at what price. Doctors
decide whether to prescribe it over the alternatives. Rivals decide how long it has the
field: other drugs in the class now, and copies after the patent ends.

Three pairs of numbers get confused. **List price** against **net price**, which is what
the company keeps after rebates and discounts. **In-market sales**, which are what
patients take, against **company sales**, which also move with distributors' stock. A
partner's **sales** against the company's **royalty** on them.

Signs the card does not fit: the company makes generic drugs or drug ingredients (see
the [generic drugs card](generic-drugs.md)); it does
research or manufacturing for other drug makers (see the
[CRO and CDMO card](contract-research-manufacturing.md)); it distributes drugs (see the
[drug distribution card](drug-distribution.md)); or a
listed stake in another drug developer is more than about 15% of its value, in which case
that stake gets its own build.

## 2. The driver tree

Build each drug, each use it is approved for and each market separately, with history
beside the forecast. Where the company reports a drug's sales by market only, split them
by use from the patient counts it gives, the date each use was approved and the dose
each use needs, and label the split as an estimate.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Eligible patients | People with the disease, times the share diagnosed, times the share treated at this stage of the disease, times the share who qualify for this drug | Total treated patients from published estimates, labelled as such |
| Share of patients | The drug's share of those treated, against named rivals and against the treatment patients use today, on a ramp from launch or from reimbursement | Volume growth, labelled as such |
| Patients on the drug | New patients, less those who stop, giving the average on treatment. Then doses per patient in the period, which depend on whether treatment is continuous or in cycles, and on body weight where the dose is set by weight | Volume in boxes or doses |
| Net price | List price less rebates and discounts, by market and by form of the drug, with dated cuts at each reimbursement review | Revenue divided by volume |
| Drug sales | Patients times doses times net price, plus the change in distributors' stock, taken from the company's comments | Sales growth by drug |
| End of protection | The date patents or exclusivity end, and the rate at which copies take volume and price. Copies of biological drugs take share more slowly than copies of pills | A named date and a labelled decline |
| Pipeline drugs | For each: stage, use, the chance of approval, launch date, peak sales and ramp. A new use of a drug already on sale is a pipeline row until it is approved. Where a new drug would replace the company's own, take the patients from one shared total | Named late-stage drugs only |
| Partner income | Payments up front, milestones (amount, chance and date), royalties on the partner's sales, and product sold to the partner at a supply price | Deals already signed only |
| Research cost | By programme and trial phase, with dates | Research cost as a whole, with late-stage trials named |
| Selling cost | Sales force and launch spending by drug | Selling cost as a share of sales |
| Cash runway | For a company not yet profitable: cash divided by yearly spending, and the size and timing of the next funding | |

## 3. The data behind the rows

- **Company.** Disclosure varies widely. Companies listed in the US, Europe and Japan
  report sales by drug each quarter. Companies listed in China and Hong Kong report twice
  a year and often name only the largest drugs. Most publish a pipeline table with stages
  and expected trial results, and the terms of large deals, usually as one headline total
  with only the payment up front stated exactly.
- **Industry**, which differs by market:

| Market | What exists |
| --- | --- |
| United States | Weekly prescription counts by drug (IQVIA), which miss drugs given in clinics. For those, the public insurer's quarterly average selling prices and its spending by billing code. Approval decision dates from the regulator. Patent and exclusivity listings. Companies' own disclosure of rebates as a share of gross sales |
| China | The national reimbursement list, updated once a year with the price cut each drug accepted. Hospital drug sales audits from data providers. Rounds of volume-based procurement for drugs whose patents have ended |
| Everywhere | Trial registries (ClinicalTrials.gov) and results presented at medical conferences. Published estimates of how many people have each disease. Deal databases |

- **What leads revenue.** Prescription counts. The yearly reimbursement result. Trial
  results and approval decisions on known dates. Rivals' launches. Patent rulings.
- **Backtest.** Patients times net price against reported sales of each drug.
  Prescriptions times net price against sales, where prescription data exist.

## 4. Costs and margin

- Making a drug costs little against its price, so gross margin is high. Royalties owed
  to a licensor sit in cost of sales.
- A launch needs a sales force before it has sales. Selling cost falls as a share of
  sales as the drug grows.
- Research cost follows the trials running. Late-stage trials cost far more than early
  ones.
- Joining a reimbursement list trades a large price cut for more patients. Being listed
  does not guarantee the volume, because hospitals add new drugs slowly.
- Payments up front and milestones carry almost no cost and do not repeat. Keep them out
  of the margin on drug sales.
- Some companies capitalise development costs instead of expensing them. Compare profit
  on one basis.

## 5. Capacity, capex and working capital

- Factories are a small need, except for biological drugs and cell therapies. The real
  call on cash is research.
- A company not yet profitable lives on its cash. New shares dilute holders, so model the
  funding as well as the spending.
- Rights bought from others sit on the balance sheet and are written off if the drug
  fails. Milestones owed to licensors are commitments not yet on it.
- Receivables from hospitals and distributors can be long, and distributors hold stock
  that moves before price changes.

## 6. Cycle, policy and traps

- A drug's life has a shape: slow launch, a ramp, a peak, then a fall when protection
  ends, sharp for pills and slower for biological drugs. A company's growth is the sum
  of its drugs at different points.
- Trial results and approval decisions are all-or-nothing events on known dates.
- Payers set the price. Reimbursement reviews, procurement rounds for older drugs,
  government price negotiation and tariffs can each reset a drug's revenue in a year.
  Each has its own dates and exemptions.
- Traps:
  - in-market sales read as company revenue;
  - list price read as net price;
  - milestone and up-front payments inside revenue growth;
  - a deal's headline value, most of which depends on milestones that may never be reached;
  - peak sales with no probability attached;
  - the chance of passing the next trial read as the chance of reaching the market;
  - a filing read as an approval, or a secondary measure in a trial read as its main
    result;
  - trials on different patients compared as if they were alike;
  - distributors stocking up ahead of a price change;
  - free drug given to patients counted in volume;
  - adjusted profit that leaves out share-based pay and amortisation of bought rights.

## 7. What investors argue about, and the yardstick

- Whether the lead drug's sales hold as rivals arrive and prices are cut.
- What the pipeline is worth: how likely the key drugs are to succeed, and how large.
- Whether a partner will take the drug global, and on what terms.
- Whether the cash lasts until the company earns a profit.

Yardstick: P/E for a profitable company; for one that is not, the risk-adjusted value of
its pipeline plus cash, with value to peak sales as a check
([yardstick list](../../../valuation-thesis/references/yardsticks.md)). Value the pipeline
from the cash flows at each outcome, and do not multiply peak sales by one probability.
Do not count shared research spending or a shared technology twice across drugs.

## Competitive position of a pipeline asset

When a clinical asset carries a large share of the market value, apply the general [asset competitive-position procedure](../../../research-cycle/references/what-the-market-trades.md#4-when-the-price-is-an-asset-not-the-earnings) in its drug form, against the rivals for the same target and indication:

- **Mechanism and target.** What the drug does, the mutations or populations it covers,
  and what the rivals cover. A broader mutation set, a different binding mode or
  resistance coverage is only an advantage if the clinical data bear it out.
- **Data against rivals.** Response rates, durability, safety and dosing from each
  programme's latest disclosed data, with trial stage, population, line of therapy and
  sample size beside each number. A Phase I signal in a small cohort is not a Phase III
  result; say what the comparison can and cannot show.
- **Timing.** Each rival's stage, next readout and likely approval date in each market.
  Second to market with better data can win; first with similar data usually keeps
  share.
- **Commercial frame.** Addressable patients by mutation and line, the price regime and
  the partnering or licensing deals comparable assets have drawn, which price the asset
  before approval.
- **What it is worth under each outcome.** Best in class, one of several, or failed,
  each with its probability and the cash the company needs to get there. Compare with
  the residual the price places on it.

Conclude with a stated view: best in class, competitive, or behind, with the data that
would change it and the date it is due.

## Worked build

A disease has 100,000 patients a year who qualify for a drug. The drug has a 20% share, so
20,000 patients, each treated for 8 months at a net price of 1,000 a month: sales of 160m.

The drug joins a reimbursement list and its price is cut by half, to 500. Its share
doubles to 40%. Sales are 40,000 times 8 times 500, which is still 160m. Twice the
patients brought no growth, and the share has to pass 40% before the listing pays.

A pipeline drug has a 30% chance of reaching the market, where its cash flows would be
worth 200 today. Trial costs of 10 are committed whatever happens. Its risk-adjusted value
is 60 less 10, which is 50.

All figures are invented. They show the relationships, not a forecast.

Adaptation credit and licence: [notice](NOTICE.txt).
