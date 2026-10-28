# Page content for checkcartax.com. Facts verified against gov.uk (vehicle tax rate tables, exemptions,
# Direct Debit, refunds, SORN, historic vehicles) on 28 Oct 2026. Rates apply from 1 April 2026.
G = "https://www.gov.uk"
SRC = f'<p class="src">Source: <a href="{G}/vehicle-tax-rate-tables" rel="noopener">GOV.UK vehicle tax rate tables</a>. Rates change each April, so always confirm on GOV.UK before you pay.</p>'

T_FIRST = """<div class="tw"><table><caption>First tax payment, cars registered on or after 1 April 2017</caption>
<thead><tr><th>CO2 emissions</th><th>Petrol, RDE2 diesel, alternative fuel and zero emission</th><th>All other diesel</th></tr></thead><tbody>
<tr><td>0g/km</td><td>£10</td><td>£10</td></tr><tr><td>1 to 50g/km</td><td>£115</td><td>£135</td></tr>
<tr><td>51 to 75g/km</td><td>£135</td><td>£280</td></tr><tr><td>76 to 90g/km</td><td>£280</td><td>£365</td></tr>
<tr><td>91 to 100g/km</td><td>£365</td><td>£405</td></tr><tr><td>101 to 110g/km</td><td>£405</td><td>£455</td></tr>
<tr><td>111 to 130g/km</td><td>£455</td><td>£560</td></tr><tr><td>131 to 150g/km</td><td>£560</td><td>£1,410</td></tr>
<tr><td>151 to 170g/km</td><td>£1,410</td><td>£2,270</td></tr><tr><td>171 to 190g/km</td><td>£2,270</td><td>£3,420</td></tr>
<tr><td>191 to 225g/km</td><td>£3,420</td><td>£4,850</td></tr><tr><td>226 to 255g/km</td><td>£4,850</td><td>£5,690</td></tr>
<tr><td>Over 255g/km</td><td>£5,690</td><td>£5,690</td></tr></tbody></table></div>"""

T_STD = """<div class="tw"><table><caption>Second tax payment onwards, cars registered on or after 1 April 2017</caption>
<thead><tr><th>Payment option</th><th>Standard rate</th><th>List price over £40,000*</th></tr></thead><tbody>
<tr><td>Single 12 month payment</td><td>£200</td><td>£640</td></tr>
<tr><td>12 month payment by Direct Debit</td><td>£200</td><td>£640</td></tr>
<tr><td>Total of 12 monthly Direct Debits</td><td>£210</td><td>£672</td></tr>
<tr><td>Single 6 month payment</td><td>£110</td><td>£352</td></tr>
<tr><td>6 month payment by Direct Debit</td><td>£105</td><td>£336</td></tr></tbody></table></div>
<p class="note">*The expensive car supplement of £440 a year applies to cars with a list price over £40,000 (for electric cars, GOV.UK sets the threshold at £50,000). It is paid for 5 years from the second time the vehicle is taxed. Zero emission cars registered before 1 April 2025 do not pay it.</p>"""

T_0117 = """<div class="tw"><table><caption>Cars registered 1 March 2001 to 31 March 2017 (12 month rate)</caption>
<thead><tr><th>Band</th><th>CO2 emissions</th><th>12 months</th><th>6 months</th></tr></thead><tbody>
<tr><td>A</td><td>Up to 100g/km</td><td>£20</td><td>N/A</td></tr><tr><td>B</td><td>101 to 110g/km</td><td>£20</td><td>N/A</td></tr>
<tr><td>C</td><td>111 to 120g/km</td><td>£35</td><td>N/A</td></tr><tr><td>D</td><td>121 to 130g/km</td><td>£170</td><td>£93.50</td></tr>
<tr><td>E</td><td>131 to 140g/km</td><td>£200</td><td>£110</td></tr><tr><td>F</td><td>141 to 150g/km</td><td>£225</td><td>£123.75</td></tr>
<tr><td>G</td><td>151 to 165g/km</td><td>£275</td><td>£151.25</td></tr><tr><td>H</td><td>166 to 175g/km</td><td>£325</td><td>£178.75</td></tr>
<tr><td>I</td><td>176 to 185g/km</td><td>£360</td><td>£198</td></tr><tr><td>J</td><td>186 to 200g/km</td><td>£410</td><td>£225.50</td></tr>
<tr><td>K*</td><td>201 to 225g/km</td><td>£445</td><td>£244.75</td></tr><tr><td>L</td><td>226 to 255g/km</td><td>£760</td><td>£418</td></tr>
<tr><td>M</td><td>Over 255g/km</td><td>£790</td><td>£434.50</td></tr></tbody></table></div>
<p class="note">*Band K includes cars with a CO2 figure over 225g/km that were registered before 23 March 2006.</p>"""

T_PRE01 = """<div class="tw"><table><caption>Cars and light goods vehicles registered before 1 March 2001</caption>
<thead><tr><th>Engine size</th><th>12 months</th><th>6 months</th></tr></thead><tbody>
<tr><td>Not over 1,549cc</td><td>£230</td><td>£126.50</td></tr><tr><td>Over 1,549cc</td><td>£375</td><td>£206.25</td></tr></tbody></table></div>"""

T_VAN = """<div class="tw"><table><caption>Light goods vehicles (vans) up to 3,500kg</caption>
<thead><tr><th>Vehicle</th><th>12 months</th><th>6 months</th></tr></thead><tbody>
<tr><td>Registered on or after 1 March 2001 (TC39), including zero emission</td><td>£360</td><td>£198</td></tr>
<tr><td>Euro 4 vans registered 1 March 2003 to 31 December 2006 (TC36)</td><td>£140</td><td>£77</td></tr>
<tr><td>Euro 5 vans registered 1 January 2009 to 31 December 2010 (TC36)</td><td>£140</td><td>£77</td></tr>
<tr><td>Registered before 1 March 2001, not over 1,549cc</td><td>£230</td><td>£126.50</td></tr>
<tr><td>Registered before 1 March 2001, over 1,549cc</td><td>£375</td><td>£206.25</td></tr></tbody></table></div>"""

DD = "<p>If you pay by Direct Debit, monthly and 6-monthly payments carry a 5% surcharge; paying yearly has no surcharge. DVLA takes payments on the first working day of the month, and the Direct Debit renews automatically when the tax runs out.</p>"

PAGES = []
def page(path, title, desc, h1, crumb, intro, body, faqs=(), kind="article"):
    PAGES.append(dict(path=path, title=title, desc=desc, h1=h1, crumb=crumb, intro=intro, body=body, faqs=list(faqs), kind=kind))

page("", "Check Car Tax Online | Free UK Vehicle Tax Checker",
 "Check if any UK car is taxed using its number plate. Find out when car tax is due, how VED is worked out and what you should pay.",
 "Check car tax on any UK vehicle", "Home",
 "Enter a registration number to check the tax status of any car, van or motorbike in the UK, then use our guides to understand Vehicle Excise Duty (VED).",
 f"""<h2>Why check a vehicle's tax?</h2>
<p>Paper tax discs were scrapped in 2014, so you can no longer tell from the windscreen whether a car is taxed. DVLA holds the record against the registration number instead, which means a quick number plate check is the only reliable way to confirm a vehicle is taxed, untaxed or declared off the road (SORN).</p>
<ul><li><strong>Your own car:</strong> confirm the date your tax runs out so you never drive untaxed by accident.</li>
<li><strong>Buying used:</strong> vehicle tax does not pass to the new keeper. You must tax a car before you drive it away, so check its status and expected rate before you buy.</li>
<li><strong>After a change:</strong> if you have just taxed a vehicle or made a SORN, GOV.UK says records can take up to 2 working days to update.</li></ul>
<h2>How car tax is worked out</h2>
<p>What you pay depends mainly on when the vehicle was first registered:</p>
<ul><li><strong>Before 1 March 2001:</strong> based on engine size (£230 or £375 a year).</li>
<li><strong>1 March 2001 to 31 March 2017:</strong> based on CO2 emissions, in bands A to M (£20 to £790 a year).</li>
<li><strong>From 1 April 2017:</strong> a first-year rate based on CO2, then a flat standard rate of £200 a year, plus £440 a year for 5 years on cars with a high list price.</li></ul>
<p>Since 1 April 2025, electric cars pay vehicle tax too. Read <a href="/how-much-is-my-car-tax">how much is my car tax</a> for the full tables, or <a href="/car-tax-info">our complete guide to car tax</a>.</p>
<h2>Popular guides</h2>
<ul class="cards"><li><a href="/check-car-tax">Check car tax</a></li><li><a href="/car-tax-price-check">Car tax price check</a></li><li><a href="/check-van-tax">Check van tax</a></li><li><a href="/car-tax-check-northern-ireland">Car tax in Northern Ireland</a></li><li><a href="/check-tax-on-car">Check tax on a car you're buying</a></li><li><a href="/check-car-tax-online">Check and pay car tax online</a></li></ul>""",
 [("Is checking a car's tax status free?", "Yes. Checking whether a vehicle is taxed only needs its registration number, and you can check any vehicle, not just your own."),
  ("Do I still need a tax disc?", "No. Paper tax discs were abolished in 2014. DVLA keeps the tax record electronically against the number plate."),
  ("Do electric cars pay car tax?", "Yes. From 1 April 2025 electric cars, vans and motorcycles have to pay vehicle tax."),
  ("Does tax transfer when I buy a used car?", "No. Vehicle tax does not transfer to a new keeper, so you must tax the car yourself before driving it.")], kind="home")

page("about", "About Check Car Tax | UK Vehicle Tax Checker",
 "About CheckCarTax.com: a UK vehicle tax checking service run by Outbound BPO Ltd, with plain-English guides to Vehicle Excise Duty.",
 "About Check Car Tax", "About",
 "CheckCarTax.com helps UK drivers check whether a vehicle is taxed and understand how much Vehicle Excise Duty they should be paying.",
 """<h2>Who we are</h2>
<p>CheckCarTax.com is a trading style of Outbound BPO Ltd, a London-based vehicle data business registered in England and Wales (company number 05940797). Our checks are built to be quick and simple: enter a registration number and follow the steps to see the vehicle's report.</p>
<h2>What we do</h2>
<p>We bring together tax and MOT information about UK vehicles so you can see a vehicle's current status in one place. Alongside the checker, we publish guides that explain the VED system in plain English, from the old engine-size bands to today's CO2-based first-year rates and the expensive car supplement.</p>
<h2>Our approach to information</h2>
<p>Car tax rules change every April. We take rates and rules from GOV.UK and link to the official source so you can confirm anything before you pay. We are not part of DVLA or the government; to actually tax a vehicle, you use the official GOV.UK service, a Post Office or the DVLA phone line.</p>
<h2>Get in touch</h2>
<p>Questions or feedback? Visit our <a href="/contact">contact page</a> or email <a href="mailto:support@checkcartax.com">support@checkcartax.com</a>.</p>""", kind="info")

page("car-tax-check-northern-ireland", "Car Tax Check Northern Ireland | Rules & Rates",
 "How car tax works in Northern Ireland: who manages it, the rates, Direct Debit insurance rules and how to check an NI vehicle is taxed.",
 "Car tax check in Northern Ireland", "Car Tax Check Northern Ireland",
 "Driving in Northern Ireland is different from the rest of the UK in several ways, but vehicle tax is broadly the same. Here's what NI drivers need to know.",
 f"""<h2>Who runs vehicle tax in Northern Ireland?</h2>
<p>Driver licensing and MOT testing in Northern Ireland are handled by the Driver and Vehicle Agency (DVA), and NI number plates use their own format. Vehicle tax, however, is administered by DVLA for the whole UK, so the rates and the way you check and pay are the same as in England, Scotland and Wales.</p>
<h2>From Road Fund Licence to VED</h2>
<p>Many people still call it the "road fund licence". Money from it was originally earmarked for roads, but that link ended long ago and it now goes into general taxation. Its official name is Vehicle Excise Duty (VED).</p>
<h2>What NI drivers pay</h2>
<p>NI vehicles use the same UK rate tables. For a car first registered from 1 April 2017, the standard rate is £200 a year from the second tax payment, with a £440 annual supplement for 5 years if the list price was over £40,000. Older cars pay by CO2 band or engine size; see <a href="/how-much-is-my-car-tax">how much is my car tax</a>.</p>
<h2>The key difference: insurance and Direct Debit</h2>
<p>GOV.UK states that if your vehicle is registered in Northern Ireland, you must also have insurance in place when your vehicle tax is due to renew by Direct Debit. You'll get a letter telling you if your insurance will have run out by then. As everywhere in the UK, the vehicle also needs a valid MOT when the tax starts.</p>
<h2>Checking an NI vehicle</h2>
<p>Enter the Northern Ireland registration exactly as it appears on the plate, for example in the "ABZ 1234" style. Our checker removes spaces automatically. If you're buying a car that has moved between NI and Great Britain, check that the tax status and keeper details look right before you hand over money.</p>
{DD}""",
 [("Is car tax different in Northern Ireland?", "The rates are the same across the UK and DVLA manages vehicle tax. The main difference is that NI vehicles need insurance in place for a Direct Debit renewal."),
  ("Who do I contact about vehicle tax in NI?", "DVLA handles vehicle tax for the whole UK. The DVA in Northern Ireland handles driving licences and MOT tests.")])

page("car-tax-info", "Car Tax Info: A Complete Guide to UK VED",
 "Everything about UK car tax: its history, how VED bands work, exemptions, Direct Debit, refunds and SORN, with rates from GOV.UK.",
 "A complete guide to car tax", "Car Tax Info",
 "Car tax, officially Vehicle Excise Duty and also called road tax, is older than the British motor industry. Here's how it started and how it works today.",
 f"""<h2>A brief history</h2>
<p>A duty on mechanically propelled vehicles goes back to the late 19th century, before cars were a common sight in Britain. In the early 20th century the idea took hold that motorists should pay for the roads, which is where the name "Road Fund Licence" came from. That link to road spending was eventually dropped and the money now goes into general taxation, but the nickname "road tax" has stuck.</p>
<p>For decades, cars paid a rate based on engine size. From 1 March 2001 new cars moved to a system based on CO2 emissions, and from 1 April 2017 a new structure brought in first-year rates, a flat standard rate and a supplement for expensive cars. The paper tax disc was abolished in 2014.</p>
<h2>The three systems in use today</h2>
<h3>Registered before 1 March 2001</h3><p>Rates depend on engine size.</p>{T_PRE01}
<h3>Registered 1 March 2001 to 31 March 2017</h3><p>Rates depend on CO2 emissions, shown on the V5C logbook.</p>{T_0117}
<h3>Registered on or after 1 April 2017</h3><p>You pay a CO2-based first-year rate, then the standard rate.</p>{T_STD}
<h2>Exempt vehicles</h2>
<p>Some vehicles don't pay, but must still be taxed (at £0). These include vehicles used by a disabled person (on one vehicle at a time), historic vehicles built before 1 January 1986, mobility vehicles, steam vehicles and some agricultural vehicles. From 1 April 2025, electric cars, vans and motorcycles lost their exemption and now pay vehicle tax.</p>
<h2>Paying, refunds and SORN</h2>
{DD}
<p>If you sell, scrap or declare a vehicle off the road (SORN), DVLA cancels the tax and refunds any full months left. You can't use a SORN vehicle on the road until you tax it again.</p>
{SRC}""",
 [("Is road tax the same as car tax?", "Yes. Road tax, car tax, vehicle tax and road fund licence all refer to Vehicle Excise Duty (VED)."),
  ("Which vehicles are exempt from car tax?", "Examples include vehicles used by a disabled person, historic vehicles built before 1 January 1986, mobility vehicles and steam vehicles. You must still tax an exempt vehicle."),
  ("Do I get a refund if I sell my car?", "Yes. When you tell DVLA you've sold the car, you'll get a refund for any full months of tax left.")])

page("car-tax-price-check", "Car Tax Price Check | How Much VED to Pay",
 "Work out what car tax costs for your vehicle. See current VED bands by registration date, CO2 and list price, using GOV.UK rates.",
 "Car tax price check", "Car Tax Price Check",
 "There's no single price for car tax. The amount depends on when the car was first registered, its CO2 emissions or engine size, and sometimes its list price.",
 f"""<h2>Step 1: find the first registration date</h2>
<p>This is on the V5C logbook. It decides which of the three rate systems applies to you.</p>
<h2>Step 2: find the right figure</h2>
<ul><li><strong>Before 1 March 2001:</strong> you need the engine size in cc.</li>
<li><strong>1 March 2001 to 31 March 2017:</strong> you need the CO2 figure in g/km.</li>
<li><strong>From 1 April 2017:</strong> after the first year, most cars pay the standard rate. You need to know whether the list price was over £40,000.</li></ul>
<h2>Step 3: check the table</h2>
<h3>Cars from 1 April 2017 (second payment onwards)</h3>{T_STD}
<h3>Cars from 1 March 2001 to 31 March 2017</h3>{T_0117}
<h3>Cars before 1 March 2001</h3>{T_PRE01}
<h2>Step 4: choose how to pay</h2>
<p>Paying 12 months in one go is cheapest. Monthly or 6-monthly Direct Debits add a 5% surcharge; for a standard-rate car that means £210 over 12 months instead of £200.</p>
<h2>Tip: list price is not what you paid</h2>
<p>The £40,000 test uses the car's published list price before its first registration, before any discounts, including options. A car you buy used for much less can still carry the supplement until 5 years after its second tax payment. Ask the dealer or seller if you're unsure.</p>
{SRC}""",
 [("How do I find my car's CO2 figure?", "It's printed on the V5C logbook. GOV.UK also offers an online lookup of emissions details."),
  ("Is it cheaper to pay car tax yearly?", "Yes. Paying 12 months at once, by card or Direct Debit, has no surcharge. Monthly and 6-monthly Direct Debits add 5%.")])

page("check-car-road-tax", "Check Car Road Tax | Is a Vehicle Taxed?",
 "Check road tax on any UK car by registration number. Learn what road tax covers, what you'll pay and what to do if a car is untaxed.",
 "Check car road tax", "Check Car Road Tax",
 "The internet has made car admin easier: you can tax a vehicle online and check the road tax status of any car, including one you're thinking of buying.",
 f"""<h2>What a road tax check shows</h2>
<p>A road tax check tells you whether a vehicle is currently <strong>taxed</strong>, <strong>untaxed</strong> or registered as off the road (<strong>SORN</strong>), and when the current tax expires. You only need the registration number.</p>
<h2>How road tax is calculated</h2>
<p>A common myth is that road tax was based on engine size until 2017. In fact, cars first registered from 1 March 2001 already paid by CO2 emissions; only cars registered before then are taxed on engine size. In April 2017 the system changed again for new cars, introducing a CO2-based first-year rate and a flat standard rate afterwards (£200 a year from 1 April 2026).</p>
<p>The cleanest older cars in bands A and B pay £20 a year, while the biggest emitters registered between 2001 and 2017 pay up to £790. Since April 2025, electric cars pay vehicle tax as well.</p>
<h2>If the car is untaxed</h2>
<ul><li>If it's yours, tax it on GOV.UK, by phone on 0300 123 4321 or at a Post Office that deals with vehicle tax.</li>
<li>If it's off the road, make sure a SORN is in place.</li>
<li>If you're buying it, remember tax never transfers: you'll need to tax it in your name before driving it away.</li></ul>
<h2>Before you tax</h2>
<p>The vehicle needs a valid MOT (if it requires one) when the tax starts, and you need a reference number from a V11 reminder, the V5C logbook in your name, or the green new keeper slip.</p>
{SRC}""",
 [("What documents do I need to tax a car?", "A reference number from a recent V11 reminder, the V5C logbook in your name, or the green new keeper slip if you've just bought the car."),
  ("Can I tax a car without an MOT?", "No, if the vehicle needs an MOT it must be valid when the tax starts.")])

page("check-car-tax", "Check Car Tax | See if a Car Is Taxed Today",
 "Check car tax status instantly with a registration number. See if a car is taxed, when tax is due, and how to renew on time.",
 "Check car tax", "Check Car Tax",
 "Checking car tax takes seconds. Here's why it's worth doing regularly and what the results mean.",
 f"""<h2>Reasons to check car tax</h2>
<ul><li><strong>Avoid driving untaxed.</strong> If a renewal reminder goes astray, or a Direct Debit fails, you might not realise your tax has lapsed.</li>
<li><strong>Check a car before you buy it.</strong> A seller's car may show as taxed, but that tax ends when they sell it.</li>
<li><strong>Confirm a recent change.</strong> GOV.UK says records can take up to 2 working days to update after you tax or SORN a vehicle.</li></ul>
<h2>Understanding the result</h2>
<p><strong>Taxed</strong> means VED has been paid (or the vehicle is exempt and taxed at £0) and shows the expiry date. <strong>Untaxed</strong> means it can't legally be used or kept on a public road. <strong>SORN</strong> means the keeper has declared it off the road; it can't be driven until it's taxed.</p>
<h2>Staying on top of renewals</h2>
<p>DVLA sends a V11 reminder before your tax runs out, unless you pay by Direct Debit, which renews automatically. If your Direct Debit is due to renew but the MOT will have expired, DVLA writes to you; once the car passes, the tax renews on the due date.</p>
{DD}""",
 [("How often should I check my car tax?", "It's worth checking whenever you buy a car, change payment method, or haven't received a reminder you expected."),
  ("What does SORN mean?", "Statutory Off Road Notification. It tells DVLA a vehicle is kept off the road, so it doesn't need tax but can't be driven.")])

page("check-car-tax-online", "Check Car Tax Online | Check and Pay in Minutes",
 "How to check car tax online and then tax your vehicle on GOV.UK. What you need, how long records take to update, and payment options.",
 "Check car tax online", "Check Car Tax Online",
 "You can check whether any vehicle is taxed online in seconds, and tax your own vehicle online too. Here's how the process works from start to finish.",
 f"""<h2>1. Check the tax status</h2>
<p>Enter the registration number in the box above. Spaces don't matter. You can check any vehicle, not only your own.</p>
<h2>2. Tax your vehicle online</h2>
<p>Use the official GOV.UK "Tax your vehicle" service with a reference number from one of these:</p>
<ul><li>a recent V11 reminder or "last chance" warning letter</li><li>your V5C logbook (it must be in your name)</li><li>the green new keeper slip if you've just bought the vehicle</li></ul>
<p>You can pay by Direct Debit, debit card or credit card. There's also a 24-hour phone line (0300 123 4321, no Direct Debit by phone) and Post Offices that deal with vehicle tax.</p>
<h2>3. Allow time for the record to update</h2>
<p>After taxing or making a SORN, GOV.UK says it can take up to 2 working days for the record to show the change. You can still drive a newly taxed vehicle during that time.</p>
<h2>Paying online by Direct Debit</h2>
{DD}
<p>Your first Direct Debit payment won't be taken until the tax has started, which can take up to 10 days. If you pay by Direct Debit, you won't receive a V11 reminder; don't tax the vehicle again or you'll be charged twice.</p>""",
 [("Can I tax a car online without the logbook?", "Yes, if you have a recent V11 reminder or the green new keeper slip. Otherwise you'll need to apply for a new V5C logbook."),
  ("How long does online car tax take to show?", "GOV.UK says up to 2 working days for records to update.")])

page("check-my-car-road-tax", "Check My Car Road Tax | When Is It Due?",
 "Check your own car's road tax: find your expiry date, understand reminders and Direct Debits, and what to do when you sell your car.",
 "Check my car road tax", "Check My Car Road Tax",
 "It's easy to lose track of when your own road tax runs out. A quick check of your registration shows the date, so you can renew in time.",
 f"""<h2>When does my road tax run out?</h2>
<p>Your tax covers a period of 6 or 12 months (or month by month with Direct Debit). The check above shows the date it expires. If you pay by Direct Debit, it renews automatically, as long as there's a keeper on DVLA's records and the MOT is valid.</p>
<h2>What if I've moved house?</h2>
<p>Reminders go to the address on your V5C. If you've moved, update your address with DVLA so you don't miss them. For Direct Debits, emails and letters go to the account holder.</p>
<h2>Selling, scrapping or taking the car off the road</h2>
<p>Tell DVLA when you sell, scrap or SORN your car. Your tax is cancelled, any Direct Debit stops, and you'll get a refund cheque for any full months left, sent to the name and address on the logbook. The 5% Direct Debit surcharge isn't refunded.</p>
<h2>Could I pay less?</h2>
<p>Paying yearly avoids the 5% surcharge on monthly and 6-monthly Direct Debits. You may also qualify for an exemption, for example if the vehicle is used by a disabled person or was built before 1 January 1986.</p>
{SRC}""",
 [("Will I get a reminder when my road tax is due?", "DVLA sends a V11 reminder, unless you pay by Direct Debit, which renews automatically."),
  ("Do I get money back if I sell my car?", "Yes, DVLA refunds any full months of remaining tax once you tell them you've sold it.")])

page("check-tax-on-car", "Check Tax on a Car Before You Buy",
 "Buying a used car? Check its tax status, understand that tax doesn't transfer, and estimate what you'll pay to tax it yourself.",
 "Check tax on a car before you buy", "Check Tax On Car",
 "If you're buying a used car, checking its tax is one of the simplest and most useful checks you can do.",
 f"""<h2>Tax doesn't come with the car</h2>
<p>Since the tax disc was abolished, vehicle tax no longer transfers with a car. When the seller tells DVLA they've sold it, their tax is cancelled. You must tax it yourself, using the green new keeper slip, before you drive it away.</p>
<h2>What to check</h2>
<ul><li><strong>Tax status:</strong> is it taxed, untaxed or SORN? A SORN car can't be driven to you on the road; it would need to be taxed first.</li>
<li><strong>First registration date:</strong> tells you which tax system applies.</li>
<li><strong>CO2 or engine size:</strong> needed to estimate the rate for older cars.</li>
<li><strong>List price:</strong> cars registered from April 2017 with a list price over £40,000 pay an extra £440 a year for 5 years from the second tax payment.</li></ul>
<h2>Estimate the cost</h2>
<p>For most cars registered from 1 April 2017, expect the £200 a year standard rate. A car registered between 2001 and 2017 could cost anything from £20 to £790 a year depending on its band. Since April 2025 electric cars pay too. See <a href="/car-tax-price-check">car tax price check</a> for the tables.</p>
<h2>Also check the MOT</h2>
<p>You can't tax a car that needs an MOT unless it has a valid one, so check MOT status alongside tax.</p>""",
 [("Can I drive a car home after buying it using the seller's tax?", "No. Tax doesn't transfer. You must tax it in your name before driving it."),
  ("What do I need to tax a car I've just bought?", "The green new keeper slip from the V5C logbook.")])

page("check-van-tax", "Check Van Tax | UK Van VED Rates Explained",
 "Check van tax by registration and see current UK van VED rates, including Euro 4 and Euro 5 vans and electric vans from April 2025.",
 "Check van tax", "Check Van Tax",
 "For many people a van is a tool of the trade. Keeping its tax up to date avoids unnecessary costs and keeps your business on the road.",
 f"""<h2>How van tax is calculated</h2>
<p>Unlike cars, most vans (light goods vehicles up to 3,500kg) don't pay by CO2 emissions. Vans registered on or after 1 March 2001 pay a flat rate, with lower rates for certain Euro 4 and Euro 5 vans. Vans registered before 1 March 2001 pay according to engine size.</p>
{T_VAN}
<h2>Electric vans</h2>
<p>From 1 April 2025, electric vans pay vehicle tax; GOV.UK lists zero emission vans in the same TC39 rate as other light goods vehicles registered from 1 March 2001.</p>
<h2>Heavier vehicles</h2>
<p>Vehicles over 3,500kg revenue weight are taxed under different rules (heavy goods vehicle rates, which can include the HGV levy). Check GOV.UK for your vehicle's class.</p>
<h2>Tips for van owners</h2>
<ul><li>Check tax status when buying a used van; tax doesn't transfer to you.</li>
<li>If a van is laid up, make a SORN to get a refund of full months remaining.</li>
<li>Pay yearly to avoid the 5% surcharge on monthly or 6-monthly Direct Debits.</li></ul>
{SRC}""",
 [("How much is van tax?", "For most vans up to 3,500kg registered from 1 March 2001 it's £360 a year (TC39). Eligible Euro 4 and Euro 5 vans pay £140."),
  ("Do electric vans pay tax?", "Yes, from 1 April 2025.")])

page("contact", "Contact Check Car Tax | Support & Enquiries",
 "Contact the CheckCarTax.com team by email with questions, comments or feedback about our vehicle tax checks and reports.",
 "Contact us", "Contact Us",
 "We're here to keep you on four wheels. Get in touch with any questions, comments or feedback about our products.",
 """<h2>Email</h2><p><a href="mailto:support@checkcartax.com">support@checkcartax.com</a></p>
<h2>Opening hours</h2><p>9am to 6pm on weekdays, 9am to 5pm at weekends.</p>
<h2>Already bought a report?</h2><p>You can <a href="https://secure.checkmot.com/user-area/login" rel="noopener">log in to your account</a> to view it.</p>
<h2>Postal address</h2><p>Check MOT, Apt 29509, Chynoweth House, Trevissome Park, Truro, TR4 8UN.</p>
<h2>Questions about taxing your vehicle?</h2><p>We aren't DVLA. To tax a vehicle, make a SORN or ask about a refund, use GOV.UK or call the DVLA vehicle tax line on 0300 123 4321.</p>""", kind="info")

page("how-much-is-my-car-tax", "How Much Is My Car Tax? 2026/27 UK VED Rates",
 "Find out how much your car tax should be. Full 2026/27 VED tables for first-year, standard, pre-2017 and pre-2001 cars from GOV.UK.",
 "How much is my car tax?", "How Much Is My Car Tax",
 "A tax check shows whether a car is taxed and when it's due, but not what you'll pay. These tables, based on GOV.UK rates from 1 April 2026, help you work it out.",
 f"""<h2>Why is it so complicated?</h2>
<p>Successive governments have changed how VED is charged: first by engine size, then by CO2 emissions from March 2001, then a new structure from April 2017. Cars stay on the system they were first registered under, so three systems run side by side.</p>
<h2>Cars registered from 1 April 2017</h2>
<h3>First tax payment</h3><p>Paid when the car is first registered, based on CO2. It covers 12 months and is usually included in a new car's on-the-road price.</p>{T_FIRST}
<p class="note">Diesel cars that don't meet the RDE2 nitrogen oxide standard pay the higher column.</p>
<h3>Second payment onwards</h3>{T_STD}
<h2>Cars registered 1 March 2001 to 31 March 2017</h2>{T_0117}
<h2>Cars registered before 1 March 2001</h2>{T_PRE01}
<h2>Electric and hybrid cars</h2>
<p>Since 1 April 2025, electric cars pay vehicle tax. Hybrids and other alternative fuel cars were already taxable and use the same tables as petrol and diesel.</p>
<h2>Classic cars</h2>
<p>Vehicles built before 1 January 1986 can be exempt from 1 April 2026 under the historic vehicle rules, but you must apply for the historic tax class.</p>
{SRC}""",
 [("How much is car tax for a car registered after April 2017?", "From the second tax payment it's £200 a year at the standard rate, or £640 a year for 5 years if the list price was over £40,000."),
  ("How much is car tax for a car registered between 2001 and 2017?", "It depends on its CO2 band, from £20 a year (bands A and B) to £790 a year (band M)."),
  ("How much is tax on a pre-2001 car?", "£230 a year if the engine is 1,549cc or less, and £375 a year if it's larger.")])

page("free-car-tax-check/", "Free Car Tax Check | Tax Status by Number Plate",
 "Run a free car tax check by number plate. See whether a UK vehicle is taxed or SORN and when its tax runs out.",
 "Free car tax check", "Free Car Tax Check",
 "Want to know a vehicle's tax status? Enter its registration number above to run a free check.",
 """<h2>What you'll see</h2>
<ul><li>Whether the vehicle is taxed, untaxed or SORN</li><li>When the current tax expires</li><li>The vehicle's MOT status</li></ul>
<h2>How it works</h2>
<ol><li>Type the number plate. Spaces and lower case are fine.</li><li>Press <strong>Check tax</strong>.</li><li>View the results for the vehicle.</li></ol>
<h2>Next steps</h2>
<p>If your vehicle is due, tax it on GOV.UK. Unsure of the cost? See <a href="/how-much-is-my-car-tax">how much is my car tax</a>.</p>
<p>Help us keep this service free by leaving a review.</p>""", kind="info")

for path, title, desc, h1 in [
 ("cookie-policy", "Cookie Policy | Check Car Tax", "How CheckCarTax.com uses cookies and similar technologies, and how you can control them in your browser.", "Cookie policy"),
 ("privacy-policy", "Privacy Policy | Check Car Tax", "How CheckCarTax.com collects, uses and protects your personal information when you use our vehicle tax check service.", "Privacy policy"),
 ("terms-and-conditions", "Terms and Conditions | Check Car Tax", "The terms and conditions that apply when you use CheckCarTax.com and order vehicle tax and MOT reports.", "Terms and conditions")]:
    page(path, title, desc, h1, h1.capitalize(), "", "LEGAL:" + path, kind="legal")
