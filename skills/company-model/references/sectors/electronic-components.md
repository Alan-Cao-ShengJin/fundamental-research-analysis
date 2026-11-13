# Electronic components

Use with the [sector guide](index.md). The card is a guide: work out how this company
actually makes money before using it, and take each business unit separately. Skip the
rows that do not apply.

## 1. What is sold, to whom, and who decides demand

These companies make parts that go into other companies' devices. There are two kinds,
and they are built differently.

- **Parts made for one customer's product**: camera lenses and modules, connectors and
  cables, casings and cover glass, speakers, circuit boards, cooling parts and power
  supplies. The brand designs the part in, splits each product between two or three
  suppliers, and usually takes a price cut every year. A change of design can add to
  what a supplier sells per device or remove it.
- **Catalogue parts** sold to thousands of customers, much of it through distributors:
  ceramic capacitors, resistors, inductors and standard connectors. The lines are
  general purpose. Price follows how full the industry's plants are, and rises in a
  shortage.

Demand is the number of devices built, times the value of the part in each, times the
company's share. Phones, computers, cars and servers each have their own cycle. Servers
for AI and electric cars use many more parts than what they replace.

Customers and distributors hold stock. They order ahead in a shortage and cut orders
after it.

Numbers that get confused:

- **Value per device** against the company's **share** of a customer's product.
- A fall in **average price** that is a contract price cut against one that is mix.
- **Orders**, **backlog** and the **ratio of orders to sales** against revenue.
- Sales **into** distributors against sales **out of** them.
- **Units shipped**, which some makers publish each month, against revenue.
- **Gross margin** against **segment operating profit**, which some report instead.

Signs the card does not fit: the company assembles whole devices (see the
[contract manufacturing card](contract-manufacturing.md)); it makes display panels (see
the [display panels card](display-panels.md)); it makes chips (see the
[chip designers card](chip-design.md) and the
[analogue and power chips card](analogue-power-chips.md)); it makes optical transceivers for data networks (see
the [optical networking card](optical-networking.md)); or nearly all its parts go into
cars (see the [auto parts card](auto-parts.md)).

## 2. The driver tree

Build each main customer, product line or end market separately, with history beside the
forecast. The first rows are for parts made for one customer's product. The rows marked for
catalogue parts replace them for those. Where the company publishes units shipped,
units times price is the build, and devices times value per device times share is the
check on it.

| Row | Built from | If the data is missing |
| --- | --- | --- |
| Devices built | Units by customer and product, from the brand's shipments and launch calendar. For a maker with many customers, units by end market: phones, computers, cars, servers | Shipments of that kind of device in the market |
| Value per device | The number of the company's parts on each device, such as the cameras on a phone or a car, times the price of each. It changes with the design | Revenue over devices built |
| Share | The part of each product the customer gives this supplier | Hold the latest share |
| Price change | The yearly cut the customer takes, against any upgrade in the part | The net price change from history, or the price effect in the company's profit bridge |
| Revenue | Devices times value per device times share, by customer or end market | Revenue growth by product line |
| Units shipped | Where the company publishes units by product each month: units times average price | Average price is segment revenue over units, which blends parts of very different prices |
| Parts and modules | A module built around a bought-in chip, such as a camera module and its sensor, carries that chip's cost at a low margin. The part inside it, such as the lens, earns far more, and may be sold to the company's own module unit. Build the two apart | Margin by segment as reported |
| Orders and backlog | For catalogue parts: opening backlog, plus orders, less sales, and the ratio of orders to sales | As reported |
| Capacity and share in use | For catalogue parts: capacity by product, what is added each year, and the share in use | As the company states |
| Volume and price | For catalogue parts: capacity times the share in use, checked against end demand and distributors' stock. Price falls a little each year in normal times and rises in a shortage | Revenue growth, split by the price effect in the profit bridge |
| Materials | Copper, gold, silver, nickel, resin, laminate and bought-in chips: use times price | Gross margin, moved with the main input's price |
| Factory costs | Staff and depreciation, with the share of capacity in use | Costs grown with capacity |
| Profit by line | Gross profit, or segment operating profit where that is what the company gives | The margin the company guides. With none, the line's recent margin, moved with the share of capacity in use |
| New products and plants | Parts won, by launch date. New plants abroad, with their start-up losses | The schedule the company gives |
| Research and overheads | Engineers and selling costs | Their share of revenue |
| Working capital | Stock, receivables from the brand or its assembler, and payables | Their past ratios to revenue |
| Capex and currency | Lines built for a customer's product, or general capacity. Revenue in dollars against costs at home | The guided figure, and the sensitivity the company gives. With none, capex at its recent share of revenue, and revenue and cost by currency |
| Other income and partners | Grants and interest, on their own rows. Partners' share of a unit that is listed separately or about to be | As reported |

## 3. The data behind the rows

- **Company.** Taiwanese companies publish revenue every month. Some Hong Kong-listed
  makers publish units shipped by product every month. Japanese makers give orders,
  backlog, the share of capacity in use, a profit bridge that shows the price effect,
  and the device units they assume. Results give revenue by product line or by use, and
  the share of sales to the largest customers. Few name their customers.
- **Industry:**

| Source | What exists |
| --- | --- |
| Devices | Quarterly shipments of phones, computers, tablets and servers by brand (IDC, Counterpoint, Canalys, TrendForce) |
| Brands and end markets | The brands' results and launch dates. Vehicle production. The cloud companies' capital spending |
| Prices | Published prices of capacitors and laminate (TrendForce), and of copper and gold |
| Trade and output | Japan's monthly shipments of electronic components (JEITA) and customs exports of capacitors |
| Distributors | The large distributors' results and stock |

- **What leads revenue.** Monthly revenue and shipments. The ratio of orders to sales.
  The brands' launch calendar. Reports of which supplier is in a new device, labelled as
  reports. Component prices. Distributors' stock.
- **Backtest.** Devices times value per device times share against revenue by customer.
  For catalogue parts, capacity times the share in use times price against revenue.

## 4. Costs and margin

- The margin depends on how hard the part is to make. Parts many can make are cut in
  price until little is left.
- For a part made for one customer, the price falls every year, so cost has to fall as
  fast.
- For catalogue parts, plants are fixed costs. The margin follows the share of capacity
  in use and the price.
- New products and new plants lose money at the start, and a new part takes time to
  reach a good yield.

## 5. Capacity, capex and working capital

- A line built for one customer's product is idle if the product fails or the order
  moves. A catalogue line can serve any customer.
- Circuit boards and capacitors need heavy capex, added a year or two ahead of demand.
- Customers order more than they need in a shortage. Those orders vanish when supply
  catches up.
- Brands and assemblers pay slowly.

## 6. Cycle, policy and traps

- Demand follows how often people replace devices and the stock held in the chain.
- Tariffs and customers' wish to spread risk move work between countries.
- Traps:
  - a share of one product assumed for the next;
  - a gain in value per device assumed to last;
  - one customer behind most of the sales;
  - orders placed ahead in a shortage, read as demand;
  - a price rise in a shortage, read as lasting;
  - stock built ahead of a launch that sells less than planned;
  - grants from local governments inside profit;
  - gains on the exchange rate.

## 7. What investors argue about, and the yardstick

- Who gains and loses share at the main customer.
- Whether the value of parts per device keeps rising, in phones, AI servers and cars.
- How long a shortage and its prices last.
- How much share Chinese makers take in catalogue parts.
- Whether new uses become real businesses.

Yardstick: P/E ([yardstick list](../../../valuation-thesis/references/yardsticks.md)).

## Worked build

A lens maker supplies half of a product at 10 a device: 1,000 devices give 5,000. Next
year units fall 3%, the price falls 5%, a new design lifts value per device 20%, and its
share falls to 45%. Revenue is 970 times 11.4 times 45%, which is 4,976.

A capacitor maker can make 100 units and uses 85% of its capacity. It sells 85 at 10:
revenue is 850. Fixed costs are 400 and each unit costs 3 more, so profit is 195. Orders
then run ahead of sales. It lifts the share in use to 95% and the price rises 4%.
Revenue is 988, up 16%. Costs are 685. Profit is 303, up 55%.

All figures are invented. They show the relationships, not a forecast.
