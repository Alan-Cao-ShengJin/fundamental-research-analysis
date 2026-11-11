# Research data providers and local retrieval

## Approved sources

Research uses only these sources:

- Internet search, to find and read original issuer, exchange and regulator material (filings, announcements, IR material and earnings calls) on the issuer's or exchange's own site, public information about the company and its industry, and original public market-rate or valuation-input data published by central banks, treasuries, exchanges or academic authors. Preserve publication/observation dates and methods; a current academic dataset does not establish a historical vintage.
- The FactSet AI-Ready Data connector, for consensus, valuation bands and price history only (below).
- AlphaPai, Alpha Vantage, API Ninjas and Massive, through the [local adapter](#local-adapter-and-endpoint-catalog).

Do not use any other connector, database, charting application, expert network or data service, even when one is connected to the session. For a fresh initiation, do not inherit earlier analyst forecasts or browse unrelated personal files. Explicitly user-supplied documents and host-curated evidence packs are permitted; this remote-service allowlist does not prohibit material the user authorized. Existing-coverage updates inspect eligible prior components and unresolved findings under model revision. Download what the study needs into its own folder. Model structure comes from the skills' own [sample model](../../company-model/assets/company-model-example.xlsx). If a question cannot be answered from these sources, say what is missing rather than reaching for another.

## Using the providers

Use entitled provider data alongside original issuer/exchange material. Select a source by the question, universe, definitions and actual response, not provider branding. A configured key proves neither coverage nor product entitlement. Use only relevant families for each assignment; the catalog is not a mandatory research checklist.

## Route by research question

| Question | Useful routes | Interpretation |
| --- | --- | --- |
| What changed in the business and outlook? | Issuer filings/IR first; AlphaPai meetings/announcements; Alpha Vantage transcripts, statements, historical earnings and estimates; API Ninjas statements and earnings | Separate management guidance, vendor estimates, broker opinion and independent forecast. Reconcile fiscal periods, cumulative versus standalone flows, units and scope. |
| What is already expected? | FactSet consensus (below); Alpha Vantage earnings estimates, dispersion/contributor fields and revision snapshots when returned; dated guidance and earlier peer calls | Vendor coverage is not the whole market. Check horizon, actual versus estimate and contributor count. A current response containing past estimates is not a complete point-in-time consensus archive. |
| What price, actions and liquidity support the decision? | Massive daily bars, snapshots, dividends/splits, float and market/session status; Alpha Vantage prices/actions/FX; API Ninjas prices, splits and market cap | Preserve exact instrument, timestamp, delay and adjustment basis. Derive traded-value/liquidity distributions from an adequate window, not one bar. A snapshot is not automatically real time. |
| What do ownership and incentives suggest? | Alpha Vantage insider transactions/institutional holdings/ETF profile; API Ninjas insider transactions, holdings, compensation and fund profiles; official filings for rights/control | Filing/reporting lags, transaction codes and restricted fields matter. Holdings are not live flows; a fund holding is not a commitment to buy. Verify CEO pay components and incentive terms in the proxy. |
| Where does the stock sit in the market? | Massive news, related tickers, short interest/volume and movers; AlphaPai broker comments, thematic bluebooks, articles and hot-stock boards | Use as discovery/context. Related-ticker algorithms do not establish economic peers; popularity is not fund flow. Short volume is trading activity, not outstanding short interest or net bearish positioning. |
| Which outside conditions affect assumptions? | Massive economic series and FX/crypto bars; Alpha Vantage macro/commodity/FX series; API Ninjas yields, unemployment, commodity/metals/oil, mortgage rates and layoffs | Match geography, frequency, release vintage and lag to the business exposure. Layoff notices are local/covered notifications, not total employment losses. Revised macro history is not an unrevised backtest vintage. |
| Which Chinese industry/channel evidence is worth pursuing? | AlphaPai announcement/report/comment search, source-class recall, chart search and natural-language data query | Retain source class, original locator and date. Generated answers/tables are leads: verify pivotal values and underlying sources before modeling. Empty search is query-specific, not proof that no evidence exists. |

**FactSet: consensus, valuation bands and price history only.** Use the FactSet connector for these things: the company's consensus forecasts (EPS, revenue, net profit, target price and ratings) for the next three fiscal years and by business segment, with their high, low, estimate count and 100-day revisions, their point-in-time history, the surprise record and the consensus that stood the day before each guidance (the reads in [what the market trades](../../research-cycle/references/what-the-market-trades.md#1-find-what-sets-the-price)); the monthly price and consensus forward-EPS history that builds its valuation band, which also gives the reference price; and the 12-month price history of the stock, its peers and its benchmark for the price chart and the price-reaction log. Take reported actuals, segment data, guidance and operating data from filings, calls and the sources above, not from FactSet fundamentals. Keep requests to what the model and band need. Request estimates with `currency='ESTIMATE'` (or the reporting currency): `LOCAL` converts into the listing currency but still reports the broker's currency in `estimateCurrency`, so a Hong Kong-listed RMB reporter comes back in HKD labelled CNY. This applies to the company, its band history and every peer.

Keep key-specific test outcomes in project development records, outside generic research instructions. Access can change. A successful sample does not certify accuracy, universal coverage or sufficient history.

## Inspect the delivered fields, not the endpoint name

For a quick screen, use an available finished board/preset or normalized source response before many primitives when it answers the question. Record the universe, filters, observation dates, provider and stale/fallback status; vendor discovery lists are leads, not an exhaustive exchange universe. Deeper research verifies pivotal figures against filings. A cache or fallback can keep a tool available while leaving the underlying observation stale.

Keep analyst price-target consensus separate from fiscal-period earnings estimates, estimate revisions and historical estimate vintages. A route called `estimates` may supply only targets; inspect actual fields, periods and contributor coverage before stating what the market expects.

Retain the exact discovered instrument and source identifiers, interval, currency, adjustment basis and first/last observations. Distinct feeds for one ticker remain distinct series; an empty search may mean disabled or missing coverage rather than a nonexistent security. Use available catalog/help surfaces, preserve provider-native symbols and document justified mappings; do not guess flags or silently enable/configure providers. Price/bar age does not by itself measure feed delay. See [historical replay](../../valuation-thesis/references/history-and-attribution.md) for session and availability alignment.

## Evidence for forward valuation

A historical forward P/E series requires prices and earnings forecasts available at each observation date on a consistent horizon and split/accounting basis. A latest TTM ratio, reported EPS history, announcement-date earnings surprise or recent estimate-revision fields do not supply that series. Check the actual endpoint specification and returned fields before requesting a five-year mean.

A provider-reported mean can serve as a dated benchmark when its window, forward definition and source access are retained. Label it as reported; do not claim a reconstructed series, distribution or valid-observation count without the underlying records. Distinguish an indexed excerpt from a fully read document. See [valuation calibration](../../valuation-thesis/references/method-selection.md#select-the-primary-target).

For peer comparisons, combine common-date prices with explicitly dated fiscal-period estimates; retain contributor counts and adjustment definitions when available. Fiscal year-end differences and unreturned estimate timestamps remain limitations. When a configured provider lacks entitlement or the required field/history, use another approved source for the missing component, document the fallback and its timing limits, and continue the authorized research. Do not reinterpret trailing data as forward, bypass access or purchase an expansion without authorization. Keep key-specific access results in project records.

## Local adapter and endpoint catalog

Run `python -B -X utf8 skills/evidence-intake/scripts/research_data.py PROVIDER OPERATION ...` from the project. `PROVIDER catalog` lists registered read-only operations, required/allowed parameters and official documentation without making an API call. The machine [endpoint registry](../assets/provider-endpoints.json) is an allowlist, including some documented but unverified or currently restricted routes. Its presence does not grant access. Legacy meeting/transcript/calendar operations below remain supported in addition to the registry.

| Provider | Selected operation families | Key usage constraint |
| --- | --- | --- |
| `alphapai` | `health`, `meetings`, `meeting`; announcements/reports/comments and details, comment events, bluebooks, articles, hot stocks, `recall`, `search-charts`, `data-query`, `document-text` | Fresh list IDs and advertised note types; a listed item can still have restricted full text. Parsed document text may be absent even when the source exists. Earnings and broker-hosted calls are found through `recall` with `recallType=["roadShow"]` (a JSON array) and come back as excerpts; `meetings` keyword search misses them. |
| `alphavantage` | `transcript`, `calendar`; statements, earnings/estimates, prices/actions, holdings/insiders, ETF, macro/FX, indicators | Establish fiscal period first. Free-tier daily and per-second limits apply; budget requests, cache permitted responses and stop on rate limits rather than cycle keys. |
| `api-ninjas` | `transcript`, `transcript-search`, `calendar`; statements/earnings, insider/holdings/compensation, fund profiles, prices/actions, SEC links, macro/commodity data | Free responses can be partial or limited to the latest record. Inspect actual dates, field restrictions and statement period basis. |
| `massive` | `ticker`, `earnings`, `guidance`; bars/snapshots, actions, float/short data, news, economy, cross-asset routes and partner products | Core, real-time and partner/add-on entitlements differ. No undocumented transcript route is assumed. |

Credentials come from process environment or ignored `.env.research-data`; `.env.example` contains names only. Each invocation makes one request with fixed HTTPS endpoints, bounded time/response size, blocked cross-origin redirects and a redacted receipt. Full responses/provenance are saved under ignored `.data/research-data` by default; `--output` selects an appropriate research artifact path subject to data rights.

Examples without credentials (replace sample identifiers/periods with the research subject):

```powershell
python -B -X utf8 skills/evidence-intake/scripts/research_data.py alphapai catalog
python -B -X utf8 skills/evidence-intake/scripts/research_data.py alphapai meetings --market HK --content-type performance_meeting company_communication --limit 3
python -B -X utf8 skills/evidence-intake/scripts/research_data.py alphapai meeting --roadshow-id ID_FROM_CURRENT_LIST --note-type asr_note
python -B -X utf8 skills/evidence-intake/scripts/research_data.py alphavantage earnings-estimates --symbol TICKER
python -B -X utf8 skills/evidence-intake/scripts/research_data.py api-ninjas balancesheet --symbol TICKER
python -B -X utf8 skills/evidence-intake/scripts/research_data.py massive daily-bars --symbol TICKER --param from=YYYY-MM-DD --param to=YYYY-MM-DD --param limit=30
```

Use repeated `--param NAME=VALUE` for allowed catalog parameters; JSON arrays/booleans are accepted. Query/path parameters are validated and authentication/function overrides rejected. Pagination is explicit; do not blindly follow a returned URL with credentials. Narrow time windows/pages to the evidence needed; a provider may ignore a requested count. The response byte bound remains in force. Defaults such as a macro series, exchange or FX pair are illustrative routes, not a choice of company exposure or proof of freshness. Review them before use.

## Status, normalization and evidence

Distinguish `ok`, `partial`, `no_data`, `not_entitled`, `auth_error`, `access_denied`, `rate_limited`, `provider_error`, `http_error` and `network_error`. HTTP 200 can contain a business error or an upgrade notice. AlphaPai JSON success requires code 200000; its document-download route can return plain Markdown. Correct invalid parameters before deciding that an endpoint is unavailable. An empty filtered sample establishes only that query's result; missing parsing is not missing disclosure. Do not upgrade subscriptions or circumvent access.

The receipt is not the evidence. Inspect the saved payload, original dates, source/speaker roles and actual usable values. Premium placeholders become null in `normalized_response`, while the original `response` and restricted field paths remain. Partial records can still supply usable data; locked fields remain missing. Strings such as `None`, `n/a` or absent observations also need explicit missing-value handling before numeric conversion. Never coerce them to zero. Preserve raw values and transformation lineage.

Response hashes refer to received bytes; redaction is labeled. Retrieval time is not publication/first-available time. A latest endpoint can return an old period. Reconcile important statements and observations with original filings rather than calling two republishers independent confirmation. Check access/retention/redistribution rights; link/excerpt entitled material instead of copying full transcripts into investor reports.

## Chinese material and translation

AlphaPai generally supplies Chinese material. Search original Chinese issuer/industry terms and identifiers where useful, using UTF-8 end to end. Preserve the original and source locator; translate into the user's preferred language, English by default. Check numeric scales (including ten-thousand and hundred-million units), currency, fiscal period, year-on-year versus sequential change, speaker and forward-looking qualifiers. Keep uncertainty from ASR or ambiguous wording; a translated AI summary is not a verified verbatim management transcript. Do not assume all AlphaPai meetings have management present.

## Method and authority boundary

Pair earnings evidence with the [earnings clock and peer read-through procedure](../../company-model/references/earnings-clock-and-peer-readthrough.md). Maintain the current information set internally; show timing in an investor brief only when it helps assess the thesis/catalyst. The whole company's economics, growth funding, governance, valuation and payoff determine the decision; one quarter or a provider popularity score does not replace that judgment.

Official references: [AlphaPai installation/docs](https://open-api.rabyte.cn/alpha/open-api/v1/file/api-docs/alphapai-research/install.md), [Alpha Vantage](https://www.alphavantage.co/documentation/), [API Ninjas](https://api-ninjas.com/api), [Massive REST](https://massive.com/docs/rest/stocks/overview). Consult the endpoint's linked documentation for specific parameters. Retrieval authorization does not authorize account writes, bookings, uploads, purchases, outreach or live monitoring.
