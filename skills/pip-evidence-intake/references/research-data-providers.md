# Research data providers and local retrieval

Use entitled provider data alongside original issuer/exchange material. Select a source by the question, universe, definitions and actual response, not provider branding. A configured key proves neither coverage nor product entitlement. Use only relevant families for each assignment; the catalog is not a mandatory research checklist.

## Route by research question

| Question | Useful routes | Interpretation |
| --- | --- | --- |
| What changed in the business and outlook? | Issuer filings/IR first; AlphaPai meetings/announcements; Alpha Vantage transcripts, statements, historical earnings and estimates; API Ninjas statements and earnings | Separate management guidance, vendor estimates, broker opinion and independent forecast. Reconcile fiscal periods, cumulative versus standalone flows, units and scope. |
| What is already expected? | Alpha Vantage earnings estimates, dispersion/contributor fields and revision snapshots when returned; dated guidance and earlier peer calls | Vendor coverage is not the whole market. Check horizon, actual versus estimate and contributor count. A current response containing past estimates is not a complete point-in-time consensus archive. |
| What price, actions and liquidity support the decision? | Massive daily bars, snapshots, dividends/splits, float and market/session status; Alpha Vantage prices/actions/FX; API Ninjas prices, splits and market cap | Preserve exact instrument, timestamp, delay and adjustment basis. Derive traded-value/liquidity distributions from an adequate window, not one bar. A snapshot is not automatically real time. |
| What do ownership and incentives suggest? | Alpha Vantage insider transactions/institutional holdings/ETF profile; API Ninjas insider transactions, holdings, compensation and fund profiles; official filings for rights/control | Filing/reporting lags, transaction codes and restricted fields matter. Holdings are not live flows; a fund holding is not a commitment to buy. Verify CEO pay components and incentive terms in the proxy. |
| Where does the stock sit in the market? | Massive news, related tickers, short interest/volume and movers; AlphaPai broker comments, thematic bluebooks, articles and hot-stock boards | Use as discovery/context. Related-ticker algorithms do not establish economic peers; popularity is not fund flow. Short volume is trading activity, not outstanding short interest or net bearish positioning. |
| Which outside conditions affect assumptions? | Massive economic series and FX/crypto bars; Alpha Vantage macro/commodity/FX series; API Ninjas yields, unemployment, commodity/metals/oil, mortgage rates and layoffs | Match geography, frequency, release vintage and lag to the business exposure. Layoff notices are local/covered notifications, not total employment losses. Revised macro history is not an unrevised backtest vintage. |
| Which Chinese industry/channel evidence is worth pursuing? | AlphaPai announcement/report/comment search, source-class recall, chart search and natural-language data query | Retain source class, original locator and date. Generated answers/tables are leads: verify pivotal values and underlying sources before modeling. Empty search is query-specific, not proof that no evidence exists. |

Keep key-specific test outcomes in project development records, outside generic research instructions. Access can change. A successful sample does not certify accuracy, universal coverage or sufficient history.

## Local adapter and endpoint catalog

Run `python -B -X utf8 skills/pip-evidence-intake/scripts/research_data.py PROVIDER OPERATION ...` from the project. `PROVIDER catalog` lists registered read-only operations, required/allowed parameters and official documentation without making an API call. The machine [endpoint registry](../assets/provider-endpoints.json) is an allowlist, including some documented but unverified or currently restricted routes. Its presence does not grant access. Legacy meeting/transcript/calendar operations below remain supported in addition to the registry.

| Provider | Selected operation families | Key usage constraint |
| --- | --- | --- |
| `alphapai` | `health`, `meetings`, `meeting`; announcements/reports/comments and details, comment events, bluebooks, articles, hot stocks, `recall`, `search-charts`, `data-query`, `document-text` | Fresh list IDs and advertised note types; a listed item can still have restricted full text. Parsed document text may be absent even when the source exists. |
| `alphavantage` | `transcript`, `calendar`; statements, earnings/estimates, prices/actions, holdings/insiders, ETF, macro/FX, indicators | Establish fiscal period first. Free-tier daily and per-second limits apply; budget requests, cache permitted responses and stop on rate limits rather than cycle keys. |
| `api-ninjas` | `transcript`, `transcript-search`, `calendar`; statements/earnings, insider/holdings/compensation, fund profiles, prices/actions, SEC links, macro/commodity data | Free responses can be partial or limited to the latest record. Inspect actual dates, field restrictions and statement period basis. |
| `massive` | `ticker`, `earnings`, `guidance`; bars/snapshots, actions, float/short data, news, economy, cross-asset routes and partner products | Core, real-time and partner/add-on entitlements differ. No undocumented transcript route is assumed. |

Credentials come from process environment or ignored `.env.research-data`; `.env.example` contains names only. Each invocation makes one request with fixed HTTPS endpoints, bounded time/response size, blocked cross-origin redirects and a redacted receipt. Full responses/provenance are saved under ignored `.data/research-data` by default; `--output` selects an appropriate research artifact path subject to data rights. The adapter is a local CLI, not a registered continuous worker or alert service.

Examples without credentials (replace sample identifiers/periods with the research subject):

```powershell
python -B -X utf8 skills/pip-evidence-intake/scripts/research_data.py alphapai catalog
python -B -X utf8 skills/pip-evidence-intake/scripts/research_data.py alphapai meetings --market HK --content-type performance_meeting company_communication --limit 3
python -B -X utf8 skills/pip-evidence-intake/scripts/research_data.py alphapai meeting --roadshow-id ID_FROM_CURRENT_LIST --note-type asr_note
python -B -X utf8 skills/pip-evidence-intake/scripts/research_data.py alphavantage earnings-estimates --symbol TICKER
python -B -X utf8 skills/pip-evidence-intake/scripts/research_data.py api-ninjas balancesheet --symbol TICKER
python -B -X utf8 skills/pip-evidence-intake/scripts/research_data.py massive daily-bars --symbol TICKER --param from=YYYY-MM-DD --param to=YYYY-MM-DD --param limit=30
```

Use repeated `--param NAME=VALUE` for allowed catalog parameters; JSON arrays/booleans are accepted. Query/path parameters are validated and authentication/function overrides rejected. Pagination is explicit; do not blindly follow a returned URL with credentials. Narrow time windows/pages to the evidence needed; a provider may ignore a requested count. The response byte bound remains in force. Defaults such as a macro series, exchange or FX pair are illustrative routes, not a choice of company exposure or proof of freshness. Review them before use.

## Status, normalization and evidence

Distinguish `ok`, `partial`, `no_data`, `not_entitled`, `auth_error`, `access_denied`, `rate_limited`, `provider_error`, `http_error` and `network_error`. HTTP 200 can contain a business error or an upgrade notice. AlphaPai JSON success requires code 200000; its document-download route can return plain Markdown. Correct invalid parameters before deciding that an endpoint is unavailable. An empty filtered sample establishes only that query's result; missing parsing is not missing disclosure. Do not upgrade subscriptions or circumvent access.

The receipt is not the evidence. Inspect the saved payload, original dates, source/speaker roles and actual usable values. Premium placeholders become null in `normalized_response`, while the original `response` and restricted field paths remain. Partial records can still supply usable data; locked fields remain missing. Strings such as `None`, `n/a` or absent observations also need explicit missing-value handling before numeric conversion. Never coerce them to zero. Preserve raw values and transformation lineage.

Response hashes refer to received bytes; redaction is labeled. Retrieval time is not publication/first-available time. A latest endpoint can return an old period. Reconcile important statements and observations with original filings rather than calling two republishers independent confirmation. Check access/retention/redistribution rights; link/excerpt entitled material instead of copying full transcripts into investor reports.

## Chinese material and translation

AlphaPai generally supplies Chinese material. Search original Chinese issuer/industry terms and identifiers where useful, using UTF-8 end to end. Preserve the original and source locator; translate into the user's preferred language, English by default. Check numeric scales (including ten-thousand and hundred-million units), currency, fiscal period, year-on-year versus sequential change, speaker and forward-looking qualifiers. Keep uncertainty from ASR or ambiguous wording; a translated AI summary is not a verified verbatim management transcript. Do not assume all AlphaPai meetings have management present.

## Method and authority boundary

Pair earnings evidence with the [earnings clock and peer read-through procedure](../../pip-company-model/references/earnings-clock-and-peer-readthrough.md). Maintain the current information set internally; show timing in an investor brief only when it helps assess the thesis/catalyst. The whole company's economics, growth funding, governance, valuation and payoff determine the decision; one quarter or a provider popularity score does not replace that judgment.

Official references: [AlphaPai installation/docs](https://open-api.rabyte.cn/alpha/open-api/v1/file/api-docs/alphapai-research/install.md), [Alpha Vantage](https://www.alphavantage.co/documentation/), [API Ninjas](https://api-ninjas.com/api), [Massive REST](https://massive.com/docs/rest/stocks/overview). Consult the endpoint's linked documentation for specific parameters. The included adapter handles the registered AlphaPai operations; no separate vendor skill installation is required for those routes. Additional vendor routes require their own documentation and entitlement review. Retrieval authorization does not authorize account writes, bookings, uploads, purchases, outreach or live monitoring.
