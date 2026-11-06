# World state at the research date

Company filings describe the business as of the last reporting date. The price reflects everything known today. This step finds out what has happened since then, and in the wider world, in the places where this company earns, buys, competes, is regulated and is valued. Then it works through the developments that could change the call. It is part of stage 1 of the [company sequence](company-sequence.md), and every update repeats it for the period since the last review.

The model's own knowledge stops before the research date. Treat anything remembered about current conditions as a lead to check, never as a finding.

## 1. Fix the date and the gap

- Take the research date from the environment.
- Record the latest reported period, its filing and call dates (the [earnings clock](../../company-model/references/earnings-clock-and-peer-readthrough.md) holds these), the latest price and its date, and the date of the consensus being used.
- The **gap window** runs from the latest filing or call to the research date. Company documents do not cover it, so it gets the closest search. Use the trailing year as background for the regime.

## 2. Map the exposures

List the specific places where outside events reach this business. Build the list from the filings and from evidence intake, using names rather than categories wherever the sources give them. The revenue rows are the same map of where the company sells that [industry analysis](../../industry-analysis/SKILL.md) uses; build it once.

| Exposure | What to list |
| --- | --- |
| Revenue | Regions, channels and end markets with their shares; the largest customers and how concentrated they are |
| Supply | Key inputs and their price drivers; critical or single-source suppliers; plant and contract-manufacturing locations |
| Competition | Direct competitors, substitutes, new entrants and customers making it themselves |
| Policy and regulation | Rules on the products, trade and export controls, tariffs, subsidies, pricing, and data or security reviews that apply in each revenue and supply location |
| Funding and currency | Reporting and cost currencies, debt maturities and rates, listing venue, index membership, major holders |
| Corporate status | Pending or rumoured deals involving the company or its counterparties, activists, litigation, management changes, capital raises |
| Investor themes | The themes investors in the stock's own market are paying for now, and whether this stock is classed with them |

## 3. Scan each exposure

Search exposure by exposure. Pair the company's name with each named counterparty, policy and input, then search the counterparties' own news. A general market search misses most company-specific events.

- **Company:** releases, current-report filings, proxy and deal filings, and investor-day material in the gap window.
- **Counterparties:** recent results, guidance and capex plans of the largest customers, key suppliers and listed competitors; their calls often comment on this company's market.
- **Policy:** the regulators' and trade authorities' own announcements, not only news reports of them.
- **Markets:** prices of key inputs, currencies and rates over the gap window; the share price of the company, its peers and its counterparties, with the dates of any large moves and what caused them.

For each development, record:
- the date;
- the source;
- its status: rumoured, proposed, announced, effective or reversed;
- which exposure it touches.

A large price move with no identified cause is itself a finding to chase. The dated moves and their causes also feed the price-reaction log in [what the market is trading](what-the-market-trades.md#1-find-what-sets-the-price).

## 4. Sort by what each development changes

For each development, name what it changes and in which direction, with a rough size:
- a model input (volume, price, cost, margin, capex, funding);
- the valuation method or multiple;
- the probability of a scenario;
- or the realisation path.

Compare the price reaction since it became known with that estimate to judge whether the market has already priced it.

Sort the developments into three groups:
- **Decision-changing:** it could move the target or the call by itself, or it changes what sets the price. Examples: a pending acquisition of the company, a restriction on a major product or market, a large customer's spending change, an input shock outside the company's pricing power.
- **Model input:** it adjusts an assumption without changing the call.
- **Background:** worth a line in the record, but no further work.

Keep developments that touch none of the exposures out of the work, and write no general macro survey.

## 5. Dig into the decision-changing items

Work each decision-changing item before the model is built, because it can change the model's structure, not only its inputs.

- **Primary documents.** Read the actual documents: the deal agreement and its conditions, the rule text and its effective date, the counterparty's own guidance. Do not rely on secondary summaries.
- **Transmission.** Trace the path from the event to the business response, then to the model line or valuation term, with timing. Use [macro event analysis](../../macro-event-analysis/SKILL.md) for policy, rate and geopolitical shocks.
- **Ranges.** Set a base, bear and bull reading, and say whether the item splits the scenarios or shifts all of them.
- **Resolution.** Name the observable that will settle it, when that is due, and what reading would change the view.
- **The debate.** Add the item to the contested questions stage 1 names, so the model and valuation are built to answer it.

Developments that change what sets the price, such as an offer for the company, change the valuation method itself. Hand their terms and conditions to [method selection](../../valuation-thesis/references/method-selection.md) so the method is chosen with them in view. Unresolved items stay open in the record with their resolution dates; they do not stop the study.

## 6. Place the stock among investor themes

Use [market context](../../macro-event-analysis/references/market-regime-and-investor-base.md) to judge where the stock sits relative to what investors in its own market are buying now, and whether its multiple and its peers' multiples carry a theme premium or discount that may build or fade. Base this on dated evidence from the research date.

## 7. Record the world state

Keep a dated world-state record in the research files with one row per development:
- date;
- development;
- source;
- status;
- exposure;
- effect on the model or valuation;
- whether it is priced;
- next resolution date.

Rank the rows by group. The record belongs in the evidence pack. The report's market context covers only the decision-changing items and the model inputs. [Monitor review](../../monitor-review/SKILL.md) inherits the resolution dates.

## 8. Refresh at the cutoff

Before release, rerun step 3 from the record's date to the release cutoff and refresh the price and consensus. A new decision-changing development reopens the affected stages under the company sequence's reopening rule. State the information cutoff in the deliverables.
