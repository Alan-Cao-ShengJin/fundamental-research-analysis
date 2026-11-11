# Optical networking and photonic components

Apply the [shared sector guide](index.md) when selecting the activity and building
its forecast. Use this reference only for material optical activity; a company that
merely mentions artificial-intelligence networking does not need it.

## Choose the relevant activity

Separate laser and photonic chip making (own indium phosphide or gallium arsenide
fabs), module and transceiver assembly, systems (optical circuit switches, line
systems, coherent interconnect) and contract manufacturing. Revenue is often booked
where goods first ship, such as a module maker or contract manufacturer, not with the
end customer who decides demand.

## The demand chain

Explain what the end customer needs before forecasting: bandwidth per accelerator,
power per bit, reach, latency, reliability and serviceability, and assured supply.
Then place every product in the network tier and link architecture it serves.

| Tier | What it connects | Usual medium |
| --- | --- | --- |
| Scale-up | Accelerators inside one memory-coherent domain | Copper inside a rack; optics when the domain spans racks or lane speeds outrun copper's reach |
| Scale-out | Racks and clusters on the data-centre fabric | Mostly optical beyond a few metres |
| Scale-across | Buildings, campuses and sites | Coherent optics |

For a given link the architectures are alternatives: copper (passive or active
cables); pluggable modules with a signal processor; linear-drive pluggables; high-
density pluggable form factors;
near-packaged optics (NPO, optical engines on the board or substrate beside
the chip); and co-packaged optics (CPO, optical engines inside the switch or
accelerator package, fed by external laser sources). An optical circuit switch (OCS)
is different: it redirects light between fibres and replaces electrical switch ports,
while the link ends still need optics. Name the product the company actually sells
in each architecture (laser chip, laser source module, engine, full module, switch
system); most companies sell only some of them.

## Operating build

Build ports or links by tier and speed generation, split them across architectures
with shares that sum to 100% of each tier, then multiply by the company's content
per port for the product it sells and its share. Content per port differs by
architecture: a pluggable using externally modulated lasers needs one per lane, a
silicon-photonics design shares fewer continuous-wave lasers across lanes, and CPO
uses laser source modules that each feed several ports. A shift towards CPO can
therefore lower laser revenue per port while total ports rise; let it flow from the
one shared port total rather than adding a separate CPO growth line.

Forecast an OCS line from deployed switches or ports, price and service, with its own
margin and ramp costs. Each emerging line follows the
[adoption-to-EPS bridge](../revenue-projection.md#emerging-earnings-streams).

Test every period against supply: substrate supply, wafer starts × yield at each fab
and the start and ramp dates of new capacity. Say which limit binds. Prices per bit
fall each generation, while a new speed generation earns a premium at first; price
by generation rather than holding a blended price.

## Evidence and calibration

Use issuer product-line and call disclosures, customer capital-spending statements,
switch and accelerator roadmaps (announced, sampling, qualified, shipping at volume),
standards and multi-source agreements, third-party trackers labelled as such,
purchase commitments, take-or-pay terms, prepayments and capacity reservations, and
competitors' capacity. Date each adoption stage separately; an announcement or design
win is not volume revenue.

Keep the record of management's guidance against actual results, and relate company
revenue to the customer spending behind it. Both calibrate the forecast; neither
replaces the port build.

## Checks and valuation

- Architecture shares sum to 100% in every tier and period; no port is counted in two architectures.
- Revenue stays within capacity × price in every period. A commitment's period, cancellability and product scope (lasers versus modules) are known before it is treated as revenue cover; a prepayment is financing as well as a demand signal.
- Customer concentration is stated by end customer as well as by shipment destination.
- What the price embeds: value the established lines at a supportable multiple, show the residual the price places on the emerging lines, and show which adoption path the out-year EPS at the target multiple needs. Separate topical association from economic exposure (ports × content × share × margin).
- Shortage pricing and customer digestion periods are cyclical; do not capitalise peak margins.
- Many optical companies close their fiscal year mid-calendar; where the investors or the peer set compare calendar years, compare EPS on calendar years ([valuation calendar](../../../valuation-thesis/references/valuation-calendar.md#calendar-year-comparisons)).

## Worked example

A tier of 10,000 ports splits 70% pluggable, 10% near-packaged and 20% co-packaged.
At a 30% share, pluggables using 8 lasers at 10 each give 168,000 of laser revenue;
near-packaged engines using 2 lasers at 12 give 7,200; co-packaged ports, each taking
a quarter of a laser source module at 60, give 9,000. All pluggable, the same ports
would have given 240,000, so the architecture shift costs 55,800 of revenue. Five
optical circuit switches at 400 add 2,000. At 55% and 45% gross margins, less 300 of
ramp costs and 15% tax, the laser-source and switch lines add 4,717.5 of profit, or
4.72 per share on 1,000 shares.

All figures are invented. They illustrate selected relationships, not an issuer
forecast or a complete financial model.
