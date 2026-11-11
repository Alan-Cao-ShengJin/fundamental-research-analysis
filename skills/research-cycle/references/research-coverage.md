# Sequence and skill coverage

Use this plan for an initiation or a completed existing-coverage decision update. A narrow source, model, accounting or question-only task uses the relevant subset and states its boundary; it must not claim a full company recommendation. The catalog is a dependency guide, not an automatic skill loader. The coordinator must actually open the selected skills and relevant references and retain evidence of the work.

## Plan every skill without running every workflow

At scope, select initiation, regular review or major update through [request routing](request-routing.md). Account for every installed skill using the [coverage specification](../assets/skill-coverage.json). Each has one of three requirements for the selected mode:

- **Required:** perform the scoped work or explicitly reuse eligible dated work with references. A review of an inherited governance finding is not another complete governance investigation. A required modeling role in a regular review can reuse the unchanged valid model.
- **Conditional:** decide whether its trigger applies. Record the reason for using it, reusing eligible work or marking it not applicable. Revisit that decision if later evidence changes the trigger. This prevents silent omission of management questions, context, screening and visuals without imposing them on every request.
- **Outside scope:** name the boundary. The alternative entry mode and portfolio/trading extensions do not become company-research prerequisites. If the user requests an extension, use its own route and dependencies rather than marking a stock plan as a complete portfolio decision.

Record the disposition as `completed`, `reused`, `not-applicable`, `deferred` or `pending`, with a reason and references for completed/reused work. Do not restamp old evidence as current. Missing essential work and unexplained pending conditional work prevent claiming full coverage; deferred work can support a useful explicitly partial report. Ordinary forecast uncertainty does not make otherwise completed analysis deferred.

Keep the plan with the research brief, not in the investor pitch. The optional [planner/checker](../scripts/research_plan.py) generates the selected catalog stages and a coverage entry for each skill. It does not retrieve data, execute specialists, approve reused artifacts or establish investment readiness. Manual records with the same decisions are acceptable.

```powershell
python skills/research-cycle/scripts/research_plan.py --mode initiation --out output/research-plan.json
python skills/research-cycle/scripts/research_plan.py --mode regular --out output/review-plan.json
python skills/research-cycle/scripts/research_plan.py --validate output/review-plan.json
```

A generated plan starts incomplete. Fill it from actual work; validation intentionally fails while required work or conditional decisions remain pending. Versions and exact stage order must match the current catalog. Rebase an old plan explicitly after a method change rather than silently updating its version. A validated plan shows that coverage was accounted for, not that its claims are true.

## Shared dependency sequence

1. **Scope and mode:** issuer/share class, cutoff, investment horizon, existing baseline, requested output and capability gaps. Draft or retrieve the conviction anchor. Begin a proportionate context scan and identify relevant sector mechanisms.
2. **Evidence and historical baseline:** official statements, operating data, relevant calls/Q&A, market/peer observations and attributed guidance. Reconcile definitions and historical IS/CF/BS; assess business/competition and source reliability. Setup and historical actuals precede relying on the operating forecast.
3. **Early risk work:** governance/minority rights and financial red flags, begun during intake and completed to decision-relevant depth before forecasts. Findings constrain usable cash, dilution, investment and shareholder access. Reuse valid findings on updates; reopen affected findings promptly.
4. **Economic forecast:** substantiate foundational drivers with history, guidance or calibrated external evidence; aggregate revenue, costs, capital, working capital and funding into linked statements. Apply relevant sector guidance and the human-auditable Excel contract. Keep actuals, guidance and judgment separate.
5. **Audit before valuation:** check calculations, economic support, remaining periods, cash, shares, financing and user-edit preservation. A balanced model alone does not pass the economic review.
6. **Value, validate and challenge:** use current audited outputs, material governance consequences, relevant peers/history and priced expectations. Test the provisional thesis and strongest alternative; changes return to affected model/audit/value work.
7. **Conviction and conclusion:** confirm or revise the original decisive proposition and any active exclusion. Keep belief, value, price-based rating and eligibility distinct; give the target/date, return/scenarios and what would change the view.
8. **Communicate and retain follow-up:** verify quoted figures against current outputs, deliver the requested brief/report and revised Excel when applicable, preserve vintages and define the next decisive observation. Build charts only when used. Monitoring, outreach and implementation need their actual authorized capabilities.

The catalog lists the detailed stages; the above groups explain their purpose. Conditional specialists enter at the relevant group, not at the end as decorative appendices. Management answers return through evidence into affected assumptions. Market context can change operating drivers or attainable valuation through separate causal paths. Screening precedes selecting a research candidate; it does not stand in for underwriting it.

## Existing coverage and targeted changes

Regular reviews start with the original research/model/conviction record and check intervening concrete evidence. They refresh valuation and prospective return without forcing another forecast build. Inherited governance and audit artifacts must remain usable for the current scope; a discovery of error or an active unresolved blocker cannot be marked reused simply to complete the plan.

If a regular review changes a numerical forecast, record `targetedForecastRevision.needed = true` and the affected risk review, calculation run, audit and refreshed dependent outputs. The checker requires those references. Escalate material changes in economics/thesis to the major route. The flag is an analyst declaration: the helper cannot detect hidden workbook edits or judge whether escalation was necessary.

Major updates preserve the pre-event forecast and conviction record, reconcile new disclosures, evaluate matched assumptions and log learning **before replacing estimates**. Then update actuals, recalibrate affected future drivers, review changed risks and audit before downstream valuation/challenge. A catalyst with no new period actuals uses an event-impact bridge; future guidance cannot be scored as realized delivery.

## Reopen, do not blindly restart

An invalid upstream artifact invalidates its affected descendants regardless of the chosen mode. Follow source observation -> foundational driver -> statements -> model audit -> valuation -> challenge/conviction -> conclusion -> quoted report. Update learning and watch triggers as appropriate. Preserve unaffected work with its true dates and scope; do not rebuild it just to make every skill appear invoked. No skill may approve its own evidence merely because its name appears in a plan.
