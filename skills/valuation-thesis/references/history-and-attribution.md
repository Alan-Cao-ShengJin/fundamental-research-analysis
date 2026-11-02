# Historical reconstruction and short-window attribution

Use this reference for historical narrative reconstruction and short-window return analysis.

## Reconstruct the anchor before reading the outcome

Freeze the decision timestamp/timezone, security, benchmark and question. Retain source-native instrument/feed IDs, bar interval, price adjustment and currency. Check each source's actual latest observation against the intended trading session, accounting for holidays and intraday/bar boundaries. Retrieval today does not make the last close current, and the age of a bar is not a measured feed delay. Label stale coverage and seek a suitable available alternative when it matters; do not silently splice feeds or fabricate a contemporary snapshot.

Keep contemporaneously available filings, estimates and news separate from later outcomes. Date-windowed searches can return later explanations or restated data: check actual publication/availability times before admitting them to the historical information set. An as-of API parameter alone does not establish point-in-time coverage. If contemporaneous fundamentals are unavailable, label a partial price/event replay rather than claiming to reproduce the original investable thesis.

## Shared evidence timeline

Record event ID, event/disclosure/availability times and timezone, source/locator, contemporaneous claim, affected driver and observed price/volume response. Use adjusted prices and a declared total-return or price-return convention. Align trading sessions, holidays, FX and publication times before assigning a response window.

Historical information sets contain only evidence available at each cutoff. Keep subsequent outcomes and later restatements in a separate layer. Current consensus estimates cannot stand in for a historical consensus vintage. If archived forecasts or prices are unavailable, mark historical reverse valuation uncomputed; do not substitute today's model as a contemporary observation.

## Longer reconstruction

Choose economically distinct turning points rather than explaining every daily fluctuation. At each point record: available facts; dominant attributed narratives and disagreements; contemporaneous model assumptions/conditional valuation where supported; what could reasonably have been known; subsequent evidence and outcome. Preserve failed narratives and competing cases as well as the eventual winner.

Separate business delivery, revisions to future cash flows, discount rates/risk premia, dilution, dividends and broader factor moves where data permits. Scenario valuation bridges are conditional explanations; they are not identified causes merely because they reproduce the price change. Report residual or unidentifiable contributions explicitly.

## Short-window moves

Define the window and benchmark before inspecting the preferred explanation. Collect company, sector, macro, positioning/flow and technical events where observable. Align overnight disclosures with the next tradable session. Calculate security return and benchmark-relative return with stated method; simple subtraction is descriptive excess return, not a fitted factor-model alpha.

Test the strongest alternative accounts, overlapping news, pre-existing expectations and whether the event preceded the response. Use causal language only when the design and evidence support it. Otherwise distinguish observed co-movement, plausible contributor and unresolved attribution. A strong headline and a same-day return are insufficient to identify causation.

Update the [company change ledger](../../company-change-tracking/SKILL.md) only for supported new observations. Return dated evidence, supported/refuted/unresolved explanations, affected model drivers and the next verification. Choose event windows and analytical depth according to the question and event density.

## Hypothetical entry or exit

When asked whether an entry, stop or holding rule would have worked, save dated inputs and an inspectable calculation with the results. State signal availability, earliest executable entry, exit/stop convention, holding horizon, sizing, benchmark, distributions, FX, fees and slippage. A signal computed from a closing price cannot assume a fill at that same close without a supported execution mechanism. Gaps can cross stop prices; daily OHLC cannot establish intraday order of touches or an exact fill. Report unresolved paths or bounded alternatives rather than a fabricated execution.

Measure maximum favorable/adverse excursion only after the executable entry and within the holding interval; exclude pre-entry highs/lows. Align series on dates, not row positions. Keep the rule fixed before inspecting its outcome; label later-tuned variants as exploratory. Separate business/forecast validity, descriptive event attribution and simulated trade returns. One successful replay is not evidence of repeatable alpha.

Persist the anchor evidence, availability decisions, calculation/script, assumptions, dated path and outcome together in the existing dossier. The next review should reproduce the saved case rather than substitute today's adjusted data or current consensus without recording the change. Use the [empirical validation procedure](../../research-cycle/references/empirical-research-and-validation.md) for a broader comparison set and independent evaluation window.
