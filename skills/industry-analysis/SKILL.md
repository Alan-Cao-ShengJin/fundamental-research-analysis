---
name: industry-analysis
description: Analyse the industry a company competes in. Cover how fast the market grows and why, the company's competitive niche, whether entry barriers are rising or falling, upstream input-cost and supply changes, and downstream customer and end-user behaviour. Turn the findings into model assumptions, valuation judgments, report content and tracking indicators. Use in every initiation before operating forecasts, in reviews when industry evidence changes, and for standalone industry questions.
metadata:
  version: 1.0.0
---

# Industry analysis

A company's reports show what has happened to it. The industry explains why, and what is likely to happen next. Do this work before forecasting, so that growth, share, price, cost and margin-duration assumptions rest on the industry rather than on extrapolating the company's own history. Every material finding must change something: a model driver, a scenario, the target multiple, a risk or a tracking indicator. A finding that changes nothing is background; keep it short.

## Define the market and the value chain

- Define the market the company actually sells into: product, price band, channel, customer type and geography. Do not use the stock-market sector label. Where several markets matter, analyse each one that drives profit.
- Before researching trade, policy or demand risks, map where the company actually sells: revenue and volume by region, channel and largest customers, from filings, calls and customer or customs data. Research the markets that matter, not the most familiar ones. Where the split is not disclosed, piece it together and say how confident the map is; write with no more certainty than the map supports. The [world-state scan](../research-cycle/references/world-state.md) uses the same map; build it once.
- Map the value chain from inputs to end users: who supplies, who sells, who buys, who pays, and where the profit pool sits today. Mark where the company sits and who could take its margin: suppliers, customers, platforms or competitors.

## The five lenses

Consider all five at initiation. Go deep on the lenses behind the two or three drivers the stock turns on (the debate set at scope), and say briefly when a lens does not matter for this company.

**1. Industry growth.** Market size and growth, split into volume and price. Penetration and saturation, new versus replacement demand, structural versus cyclical growth, and where the cycle stands now. How comparable markets matured: growth decay, consolidation, price deflation. Decompose the company's growth into market growth and share change. This feeds the market-size and share build, the long-run growth path and the scenarios.

**2. Competitive niche.** The slice of the market the company occupies, and why customers choose it there: price, convenience, quality, brand, service, speed or cost. Who competes for the same customers in that slice, and who attacks from adjacent slices: trading up or down, new formats, substitutes, platforms and private label. Is the niche widening or being squeezed? What are the share trend within it and the company's unit economics against those competitors (price, unit cost, return on capital)? Read share against the whole picture: a falling share of a fast-growing market can still mean strong volume growth, and rivals' gains may come in different models, types or regions. Compare like-for-like segments and the company's own growth before calling share loss a negative; if the evidence is mixed, say so and do not build the call on it. This feeds share, price premium and the competitor-response map in [competition and capital returns](../company-model/references/competition-and-capital-returns.md).

**3. Barriers to entry, rising or falling.** What protects incumbents: scale and cost, network effects, brand, switching costs, distribution, licences and quotas, capital needs, IP, data or privileged access to inputs. What is changing them: technology, regulation, platforms that cut the cost of reaching customers, cheaper capital, supply chains now open to anyone. Evidence includes entries and exits, new capacity, new entrants' share, price behaviour after entry, and the returns recent entrants earn. This feeds how long excess margins and returns last, the fade path, and the target multiple against peers and history.

**4. Upstream costs and supply.** The few inputs that drive unit cost (commodities, energy, labour, rent, freight, components, content, platform fees), their price cycle and outlook, supplier concentration and bargaining power, contract and hedging lags, and how far the company can pass cost changes on. Include supply-side changes such as capacity additions, shortages and rules on inputs. This feeds the unit-cost build from dated input-price series, margin scenarios and the lag between input prices and margins.

**5. Downstream customers and end users.** What end users are doing differently: frequency, ticket or basket, trading down or up, channel shift (online, delivery, direct), new uses, substitution, demographics, income and confidence. Customer concentration and bargaining power, channel inventory, and how demand responds to price. This feeds the volume, frequency, price, mix and channel drivers, and the elasticity behind scenarios.

When material, add regulation and policy, technology and substitutes, and the industry capacity cycle.

## Evidence

- Start outside the company, within the [approved sources](../evidence-intake/references/research-data-providers.md#approved-sources):
  - industry and government statistics, trade associations, and customs and trade data;
  - commodity and input-price series;
  - competitors', suppliers' and customers' filings and calls, and regulatory documents;
  - observable activity data: outlet counts, app and web traffic, platform listings and prices, job postings, search interest.
- Treat management's and brokers' industry views as attributed claims and test them against independent data. Prefer series to anecdotes, dated observations to undated ones, and several independent sources to one.
- Put quantitative industry series in the model's Data or Input prices tab with source and date, so drivers link to them rather than to typed numbers.
- Keep observations, inferences and judgments distinct, and record what evidence would change each judgment.

## From findings to the forecast and the call

For each material finding, record:
- what is changing, and the evidence;
- its direction, speed and size;
- the model input it moves (market growth, share, price, unit cost, margin path, capex or multiple);
- the indicator to watch.

The assumption notes in the model cite the finding. Where the industry view disagrees with guidance or consensus, show the difference and choose.

Test the company forecast against the industry:
- the market share it implies;
- the price it implies against input-cost pass-through;
- the margin it implies against competitors and against the barrier trend.

A forecast that needs implausible share gains, or stable margins while barriers fall, needs an explicit reason. For valuation, the barrier trend and the durability of the niche set how long excess returns last and whether the multiple should sit above or below peers and history.

## Output

- An industry section in the full report, placed before the forecasts. Organise it around the lenses that matter, and end each with its effect on the forecast or valuation. It is not a textbook description of the industry.
- In the one-page brief, include the industry point only when it drives the call.
- Industry indicators, handed to [monitor review](../monitor-review/SKILL.md) and checked in every regular review.
- A handoff of kind `industry-analysis` under the [shared contract](../research-cycle/references/handoffs.md).

## Reviews

In regular and major reviews, refresh the indicators, state what changed and reopen only the affected assumptions. An unchanged industry view needs no rewrite. When a structural change appears between results (a new entrant, a barrier falling, a shift in input costs or customer behaviour), it can justify a forecast change on its own evidence.
