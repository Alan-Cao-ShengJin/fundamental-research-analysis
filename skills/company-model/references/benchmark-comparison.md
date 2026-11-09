# Compare forecasts without treating a benchmark as truth

Use when comparing a company model with another analyst, broker or prior model.
Compare attributable reported forecasts on one basis before interpreting gaps.
A higher forecast is not a realised overestimate; accuracy needs later matched
actuals. Keep the original forecasts and do not move assumptions just to converge.

## Establish the comparison perimeter

Map dates from each schedule's headers, not from a shared column position. Record
each model's evidence cutoff, units, fiscal period, business scope, source cells
and reported/adjusted earnings bridge. Moving an operation between segments is a
mapping adjustment, not a forecast difference. Keep approximate product matches
explicit and do not invent the undisclosed parts of a benchmark.

Check each source's component totals against its statements. An exported workbook
can contain useful cached forecasts with broken external links or hardcoded
statement outputs. Identify the residual and whether the relevant totals match
the dated research report. A file modification date alone does not establish an
estimate vintage. Do not refresh or repair the source just to make comparison easy.

## Explain the gap at its economic source

Trace material differences through component revenue, mix, margins, operating
costs, other income, tax, ownership and shares. Reconcile an additive bridge to
attributable earnings; retain unexplained residuals rather than burying them.
Keep the gross-profit bridge separate from below-GP costs to prevent counting
depreciation or other embedded costs twice. State the interaction convention when
splitting revenue and margin effects. Without physical activity and prices, call
the revenue effect revenue, not volume.

Compare material opposing component bets even when their sum is close. Similar
segment totals can mask different demand exposures. A stable historical mix is
an assumption: test it against new products, backlog, capacity, customer wins and
management's latest explanation of growth. Replace unsupported split precision
with an explicit allocation range and a research question.

Test implied cost leverage against the [statement-forecast guidance](statement-forecast.md); neither a fixed expense base nor a constant revenue ratio is automatically valid.

Normalise cash-flow classifications before assessing conversion. Show gross debt
and cash together, alongside a consistently defined net-debt measure. More
borrowing can explain more cash. Receivable/payable days are comparable only with
matched balances, activity bases and closing-versus-average conventions.

## A conditional bridge is not a unique explanation

When only aggregate earnings are supplied, a reconciliation holding our other drivers fixed shows **one route** to the number. It does not reveal the contributors' margins, costs, tax or share assumptions. State what is held fixed and distinguish “would imply under these assumptions” from “requires.” A sentence saying contributor detail is unavailable does not cure a preceding necessity claim.

Before claiming the target requires a particular component, try a feasible counterexample with that component outside the claimed necessary condition and other components inside their supported ranges. One valid counterexample disproves necessity; failing to find one manually does not prove it. Test conjunctive claims component by component. Preserve reporting periods, cumulative/remaining-period bridges and units before applying ranges. Do not treat independent extremes as a coherent joint case when drivers are coupled.

[bounded_bridge.py](../scripts/bounded_bridge.py) tests one affine equality over independent closed ranges and returns the achievable interval and a witness. Use the original [generic input](../assets/bounded-bridge.example.json), or register a bound `bounded-bridge` assertion under the [claim contract](../../report-layout/references/claim-support.md). For a necessity test, restrict the domain to the proposed counterexample condition, then test whether the target remains feasible. Nonlinear products, shared capacity constraints and changing denominators need the actual model or another appropriate solver. The helper does not identify consensus inputs, certify economic feasibility or make the midpoint the correct forecast.

## Revisit the model, then the method

For each material gap distinguish a source correction, different information
date, scope/accounting difference, estimate with defensible evidence, weak
assumption or implementation defect. Attribute broker claims and investigate
conflicting sources chronologically; do not silently combine their mechanisms.
Separate validated policy applicability, timing and pass-through from a broker's
illustrative sensitivity. A sensitivity shown next to unchanged forecasts is not
proof that the effect was included in the active model.

Test changed component economics against comparable historical results and support any forecast step change with an operating mechanism.

Use the findings to make narrow, general improvements. Keep issuer-specific
numbers and source content in the research project. If a correction invalidates
current valuation or conviction, flag affected outputs pending a versioned rebuild
and rerun; a comparison note alone does not constitute that numerical repair.

## Reusable calculation helper

[compare_forecasts.py](../scripts/compare_forecasts.py) accepts two explicitly
normalised snapshots. It excludes basis/scope/unit mismatches and missing
counterparts, rejects duplicate or nonnumeric observations, preserves sources,
and computes left-minus-right gaps. Its importable helpers reconcile signed
earnings bridges and split gross-profit gaps exactly between revenue and margin,
sharing their interaction equally. These are arithmetic aids, not automatic
workbook interpretation or evidence validation.

Start from the [blank comparison snapshot](../assets/forecast-comparison-template.json)
for each side, replacing its empty fields. Missing values intentionally prevent
calculation. Use a separately maintained mapping for every source workbook.
