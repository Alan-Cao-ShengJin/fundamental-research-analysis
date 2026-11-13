# Optical networking

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

Use this card only where optical products are a material part of the business. A company
that merely mentions networking for artificial intelligence does not need it.

## 1. What is sold, to whom, and who decides demand

Optical companies make the parts that carry data as light between chips, racks and
buildings. They sit at different steps, and most sell at only one or two.

- **Laser and photonic chips**, made in the company's own indium phosphide or gallium
  arsenide fabs.
- **Modules and transceivers**, which package those chips into the part that plugs into
  a switch.
- **Systems**: optical circuit switches, line systems and coherent links between sites.
- **Contract manufacturing** of modules for others.

The end customer decides demand: the cloud and AI companies that build data centres.
Revenue is often booked a step earlier, with a module maker or contract manufacturer,
where the goods first ship. Start from what the end customer needs: bandwidth for each
accelerator, power used per bit, reach, delay, reliability, ease of repair, and a supply
it can count on. Then place each product in the part of the network it serves.

| Tier | What it connects | Usual medium |
| --- | --- | --- |
| Scale-up | Accelerators working as one memory domain | Copper inside a rack. Optics when the domain spans racks or the speed outruns copper's reach |
| Scale-out | Racks and clusters on the data-centre network | Mostly optical beyond a few metres |
| Scale-across | Buildings, campuses and sites | Coherent optics |

For any one link the designs are alternatives:

- copper cables, passive or active;
- pluggable modules with a signal processor, linear-drive pluggables, and high-density
  pluggable formats;
- near-packaged optics (NPO), with optical engines on the board beside the chip;
- co-packaged optics (CPO), with optical engines inside the switch or accelerator
  package, fed by separate laser source modules.

An optical circuit switch (OCS) is different. It redirects light between fibres and
replaces electrical switch ports, while the ends of each link still need optics. Name
the product the company actually sells in each design: laser chip, laser source module,
engine, full module, or switch.

Numbers that get confused:

- **Ports**, **links** and **lanes**. One port carries several lanes, and the number of
  lasers depends on the design.
- The stages of adoption: **announced**, **sampling**, **qualified**, and **shipping in
  volume**. A design win is not volume revenue.
- The customer by **where goods ship** against the **end customer** who decides.
- The company's **fiscal year** against the calendar year its peers report on.

Signs the card does not fit: optical products are a small part of sales; the company
makes copper cables and connectors (see the
[components card](electronic-components.md)); or it is a telecom operator that buys the
equipment.

## 2. The driver tree

Build ports by tier and by speed generation, with history beside the forecast. Every
product line draws on the same port total.

A module maker reports by speed and not by tier. Build it as modules shipped by speed
generation times price, with a module at each end of a link, and use the tiers and
designs to judge where the units come from.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Ports | Ports or links by tier and speed generation, from the end customers' build plans | Customers' spending on networking, labelled as such |
| Design shares | The share of each tier's ports that use each design. The shares add to 100% in every tier and period, and no port sits in two designs | The mix the company or third-party trackers describe |
| Content per port | The number of the company's parts on a port of each design. A module maker sells one module per port. A pluggable with externally modulated lasers needs one laser per lane. A silicon-photonics design shares fewer lasers across lanes. In CPO one laser source module feeds several ports | Product revenue over ports shipped, from history |
| Share | The company's share of each product, in units, with the second sources customers insist on. Trackers often quote shares of revenue: say which is used | Hold the latest share |
| Price | By speed generation. A new generation earns a premium at first, and price per bit falls with each one. Large customers take a price cut every year | The blended price on its trend, with the generation mix stated |
| Revenue by product | Ports times design share times content times the company's share times price | Revenue by product line |
| Optical circuit switches | Switches or ports deployed, times price, plus service, with its own margin and start-up costs | Leave it out until volume orders exist |
| Emerging lines | Each follows the [adoption-to-EPS bridge](../revenue-projection.md#emerging-earnings-streams) | |
| Supply limit | For a chip maker: substrate supply, wafer starts times yield at each fab, and the start and ramp dates of new capacity. For a module maker: the lasers and signal-processing chips it can buy, and its assembly capacity. Say which limit binds in each period | Capacity as the company states it |
| Commitments | From customers to the company, and from the company to its own suppliers: purchase commitments, take-or-pay terms, prepayments and capacity reservations, with their period, whether they can be cancelled, and which product they cover. A module maker's prepayments to chip suppliers, and the stock they fund, sit on its balance sheet | As disclosed |
| Margin by line | Gross margin by product, with start-up costs on new lines. For a module maker: the mix of speeds, the share of modules built on its own silicon-photonics designs, the price of bought-in chips and the yearly price cut | Segment margin |
| Capex | New fab and assembly capacity | The guided figure. With none, announced projects over their build years, plus other capex at its recent level |
| Trade rules and currency | Tariffs on modules by country of assembly. Government lists that bar a supplier from some customers. Revenue in dollars against costs at home | As disclosed |

A shift towards CPO can lower laser revenue per port while total ports rise. Let that
come out of the shared port total. Do not add a separate growth line for CPO.

## 3. The data behind the rows

- **Company.** Product-line disclosure in results and on calls, guidance, capacity plans,
  and the largest customers' share of sales. Chinese module makers give units made, sold
  and in stock once a year, and little by speed. Keep the record of management's guidance
  against what happened.
- **Industry:**

| Source | What exists |
| --- | --- |
| End customers | The cloud companies' capital spending and their statements on network design |
| Roadmaps | Switch and accelerator makers' product plans, with the adoption stage of each |
| Standards | Industry standards and multi-source agreements, which show when a design can ship from several suppliers |
| Trackers | Third-party estimates of module shipments by speed (LightCounting, Cignal AI, Dell'Oro). Label them as estimates |
| Rivals | Competitors' capacity and qualification status |

- **What leads revenue.** End customers' spending plans. The shipment plans for new
  accelerators and switches. Qualification at a large customer. The start dates of new
  capacity.
- **Backtest.** Ports times content times share times price against revenue by product.
  Company revenue against the customers' spending behind it. Both calibrate the forecast
  and neither replaces the port build.

## 4. Costs and margin

- A company with its own fabs has high fixed costs. Its margin moves with wafer starts
  and yield.
- A module maker buys most of its chips. Its margin follows what it pays for them, the
  mix of speeds and the yearly price cut, and can be high while the newest speed is
  short.
- When supply is short, prices and margins rise above what lasts.
- A new product line loses money while it ramps.

## 5. Capacity, capex and working capital

- Revenue cannot exceed capacity times price in any period. Test every period.
- A prepayment from a customer is financing as well as a sign of demand.
- A few customers buy most of the output. State concentration by end customer as well as
  by where goods ship.
- Stock builds at customers when they order ahead of need, and is worked off later.

## 6. Cycle, policy and traps

- Demand comes in waves. Customers order hard in a shortage and then pause to use what
  they hold.
- Export rules, tariffs and government lists can limit which customers may be served,
  and from which country.
- Traps:
  - a design win or an announcement read as revenue;
  - a port counted in two designs;
  - a separate growth line for a new design on top of the port total;
  - revenue forecast above capacity;
  - a commitment that can be cancelled, or that covers a different product, read as
    cover;
  - margins at the peak of a shortage treated as normal;
  - a company linked to a theme by name, with little of its sales exposed to it.

## 7. What investors argue about, and the yardstick

- How long the cloud companies keep raising their spending.
- How fast CPO and NPO replace pluggable modules, and what that does to content per
  port.
- How much share second sources and customers' own designs take.
- Whether optical circuit switches are adopted at volume.

Yardstick: forward P/E. Value the established lines at a multiple they can support, show
what the price then puts on the emerging lines, and show which adoption path the
out-year earnings need. Many optical companies end their fiscal year in mid-year. Where
investors compare calendar years, compare earnings on calendar years
([valuation calendar](../../../valuation-thesis/references/valuation-calendar.md#calendar-year-comparisons),
[yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A tier has 10,000 ports: 70% pluggable, 10% near-packaged and 20% co-packaged. The
company's share is 30%.

- Pluggables use 8 lasers at 10 each: 168,000 of laser revenue.
- Near-packaged engines use 2 lasers at 12: 7,200.
- Each co-packaged port takes a quarter of a laser source module at 60: 9,000.

If all the ports were pluggable they would have given 240,000, so the shift in design
costs 55,800 of revenue. Five optical circuit switches at 400 add 2,000.

At gross margins of 55% on laser sources and 45% on switches, less 300 of start-up costs
and 15% tax, those two lines add 4,717.5 of profit, or 4.72 a share on 1,000 shares.

A module maker sells 1,000 modules of the new speed at 500 and 2,000 of the old speed at
200: revenue is 900,000. Next year both prices fall 15%, new-speed units double and
old-speed units halve. Revenue is 2,000 at 425 plus 1,000 at 170, which is 1,020,000,
up 13%.

All figures are invented. They show the relationships, not a forecast.
