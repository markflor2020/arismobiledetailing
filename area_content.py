"""Copy for the service-area pages (detailing-<slug>.html). Edit here, then run
`python3 generate_areas.py` to rebuild the pages.

Every city gets its own intro, local cards, FAQ and meta description so the pages
aren't near-duplicates (Google skips pages that are mostly the same text).
Keep claims factual: prices must match packages.html, and local details should be
things a local would recognize. Plain text only — the generator HTML-escapes it.

Card icons: calendar, shield, star, pin, clock, truck, sparkles, users,
briefcase, sun, wrench.  `review` picks one of REVIEWS below.  `neighbors` are
slugs of other city pages to link to.
"""

# The 4 Google reviews approved for the site (quoted verbatim — don't "fix" them).
REVIEWS = [
    ("Nadia Dix", "I highly recommend this mobile detailing service! They did an excellent job cleaning up my van and you can tell they take real pride in their work. Ari was very meticulous about our van especially since I have small children, he did everything exactly the way we asked. They were professional, thorough, flexible with our timing, and their prices were excellent. It’s not often you find a service that checks every box, but they definitely did. The van looks fantastic, and we’ll absolutely be using them again!"),
    ("Miguel Espinoza", "I chose Arian as my detailer Because I saw a lot of people trusted him with their vehicles and always like the outcome, now that I’ve been a client of his for over a year, I can confidently say he’s a master of his craft! I work construction, and my truck is always dirty and Arian always comes in clutch and brings my truck back to life. Very friendly guy he’s easy to communicate with making my overall experience a 10/10"),
    ("Lindy Kyzer", "Before Ari arrived my vehicles had enough food stored in the crevices to survive a zombie apocalypse and pet hair to sew an afghan. Rather than screaming and running away, Ari did a fantastic job - polite, professional, and so nice to be able to get everything done while I’m working."),
    ("Ben Craig", "Ari provided the best detail that I’ve gotten. My family and I all got our cars detailed, some of them looking a disaster, and he made them all look pristine and new. The service was amazing and he was very professional, commutative, and reliable throughout the entire process. I would highly recommend Ari’s Detailing to anyone!"),
]

CITIES = [
    {
        "name": "Omaha", "slug": "omaha",
        "desc": "Mobile car detailing anywhere in Omaha — Dundee, Benson, Midtown, Aksarben & West Omaha. Interior, exterior & ceramic coating at your home or office.",
        "hero": "From Dundee and Benson to Aksarben and West Omaha, we bring the full detailing shop to your driveway — no fighting Dodge Street traffic to a drop-off bay.",
        "intro": [
            "Omaha is home turf for Ari's Mobile Detailing. Whether you live in an older Midtown neighborhood with street parking or on a West Omaha cul-de-sac, the routine is the same: we show up with our own water and power, detail the vehicle where it sits, and you never lose a morning to a waiting room.",
            "Omaha is hard on cars. Winter brine and road salt on I-80 and I-680 eat at lower panels and undercarriages, the older tree-lined neighborhoods drop sap and pollen every spring, and summer construction season coats everything in dust. A detail on a regular schedule keeps that grime from ever setting in.",
        ],
        "nearby": "Midtown, Dundee, Benson, Aksarben and West Omaha",
        "cards": [
            ("briefcase", "Detailed while you work", "Working downtown, in Aksarben Village or at an office park out west? Where the property allows it, we can detail your car in the lot while you're at your desk."),
            ("shield", "Undo an Omaha winter", "The Boujee Express ($280) includes an underbody wash, iron decontamination and a clay bar — the steps that pull road salt and brake dust off paint and wheels after winter."),
            ("calendar", "Clean on a schedule", "City commuting adds up fast. The Monthly Plan ($110/month) or Bi-Monthly Plan ($140 every two months) keeps your car clean without you having to remember to book."),
        ],
        "faqs": [
            ("Do you cover all of Omaha?", "Yes — North Omaha, Benson, Dundee, Midtown, Aksarben, Millard and West Omaha. Text us your address and we'll confirm a time."),
            ("Can you detail my car at work?", "Often, yes. We need permission to work on the vehicle there and room around it, so mention where you park when you request a quote."),
            ("What's best after a long Omaha winter?", "The Boujee Express — a full interior detail plus an exterior wash with underbody wash, iron decontamination, clay bar and ceramic spray sealant. Add Headlight Restoration ($65) if your lenses have yellowed."),
        ],
        "review": 3,
        "neighbors": ["millard", "ralston", "elkhorn"],
    },
    {
        "name": "Bellevue", "slug": "bellevue",
        "desc": "Mobile auto detailing in Bellevue, NE — Offutt AFB area, Olde Towne, Twin Creek & Fontenelle Forest. We come to you. Quote back within the hour.",
        "hero": "Mobile auto detailing for Bellevue families and Offutt-area drivers — we come to you, so a busy schedule never means a dirty car.",
        "intro": [
            "Bellevue is one of the oldest towns in Nebraska and home to Offutt Air Force Base, which means plenty of busy families, shift schedules and vehicles that get used hard. We work around all of it: pick a time, and we detail your vehicle in your driveway in Twin Creek, near Olde Towne, or anywhere else in town.",
            "Living near the Missouri River and Fontenelle Forest has its perks, but tree sap, pollen and bird droppings come with it — and they can etch paint if they sit. A clay bar and a protective sealant make your paint much easier to keep clean between visits.",
        ],
        "nearby": "Twin Creek, Olde Towne, Fontenelle Forest and the Offutt AFB area",
        "cards": [
            ("truck", "Getting ready to PCS?", "Selling a vehicle or shipping it to a new duty station? A full detail before it's listed or handed off helps it look its best. The Boujee Express covers inside and out in one visit."),
            ("clock", "Fits around shift work", "Base schedules and family schedules rarely line up with a shop's hours. Because we come to you, you book the time that works and keep the rest of your day."),
            ("users", "Family haulers welcome", "Crumbs, spills and car-seat messes are our specialty. The Interior Detail ($180) includes seat and carpet shampoo with extraction, steam-cleaned vents and trim, and an odor neutralizer."),
        ],
        "faqs": [
            ("Do you serve the Offutt AFB area?", "Yes — we detail at homes throughout Bellevue, including the neighborhoods around Offutt. If your vehicle is on base, text us first so we can work out a location that works."),
            ("Can you get kid and pet messes out?", "That's exactly what the Interior Detail is for — shampoo and extraction for seats and carpet, steam cleaning for hard surfaces, and an odor neutralizer. Add an Ozone Treatment ($50) for stubborn smells."),
            ("How far into Sarpy County do you go?", "All of Bellevue, plus neighboring Papillion and La Vista. Text us your address if you're not sure."),
        ],
        "review": 0,
        "neighbors": ["papillion", "la-vista"],
    },
    {
        "name": "Papillion", "slug": "papillion",
        "desc": "Mobile car detailing in Papillion, NE — Shadow Lake, Halleck Park, Midlands & Werner Park areas. Interior, exterior & ceramic coating at your home.",
        "hero": "Papillion is one of the best places to live in Nebraska — and we help keep its driveways spotless with detailing that comes to you.",
        "intro": [
            "Papillion's neighborhoods are full of family SUVs, minivans and trucks that do a lot of daily driving — school runs, practices, errands out to Shadow Lake. We bring professional interior and exterior detailing straight to your driveway, so the vehicle gets cleaned without the family losing a Saturday.",
            "Our setup is fully self-contained, so it works just as well in a newer subdivision as on an older street near downtown Papillion. No hose, no outlet, nothing needed from you.",
        ],
        "nearby": "Shadow Lake, Halleck Park, Midlands and the Werner Park area",
        "cards": [
            ("users", "End-of-season reset", "Muddy cleats, sunscreen and spilled drinks add up. After a season of games and practices, an Interior Detail ($180) brings the carpets, seats and cup holders back."),
            ("calendar", "Our best-value plan", "The Bi-Monthly Plan ($140 every two months) covers a quick interior wipe and vacuum plus an exterior wash with paint sealant, windows and wheels."),
            ("sparkles", "Protect the new car", "Just bought something new? A ceramic coating protects fresh paint from sun, salt and bird droppings and makes washing far easier. Text us the vehicle for a quote."),
        ],
        "faqs": [
            ("Do you serve all of Papillion?", "Yes — from downtown Papillion out to Shadow Lake, Halleck Park and the neighborhoods around Werner Park. We also cover neighboring La Vista and Bellevue."),
            ("How long will you be at my house?", "It depends on the package and the vehicle. A maintenance wash is quick, a full detail takes a few hours, and paint correction or coating can take most of a day. You'll get a time window with your quote."),
            ("Is ceramic coating worth it?", "If you plan to keep the vehicle a while, usually yes — it adds lasting gloss and protection, and dirt rinses off much more easily. Ari will tell you honestly whether it suits your paint when he quotes."),
        ],
        "review": 2,
        "neighbors": ["bellevue", "la-vista", "gretna"],
    },
    {
        "name": "La Vista", "slug": "la-vista",
        "desc": "Mobile auto detailing in La Vista, NE — City Centre, Central Park, Southport & near the Astro. We detail at your home or office. Quote within the hour.",
        "hero": "Mobile detailing across La Vista — from City Centre to Central Park — done in your own driveway while you get on with your day.",
        "intro": [
            "La Vista has changed fast. City Centre and the Astro have turned the 84th Street corridor into a destination, and Southport is packed with offices and hotels. What hasn't changed is how little time people have to get their car cleaned — and that's the problem we solve by coming to you.",
            "Whether you live near Central Park or work in Southport, we bring our own water and power and detail the vehicle right where it's parked.",
        ],
        "nearby": "La Vista City Centre, Central Park and Southport",
        "cards": [
            ("briefcase", "Detail during the workday", "If your workplace lot allows it, we can detail your car while you're at your desk — a good fit for Southport and the 84th Street offices."),
            ("shield", "Interstate grime, removed", "Daily miles on I-80 mean bugs, road film and brake dust. The Boujee Express includes iron decontamination and a clay bar to remove what a regular wash leaves behind."),
            ("calendar", "Weekly, no commitment", "Want it clean every week? Weekly Washes are $30 each — exterior wash with paint sealant, windows and wheels, and no contract."),
        ],
        "faqs": [
            ("Do you cover all of La Vista?", "Yes — City Centre, the neighborhoods around Central Park, Southport and the rest of La Vista, plus nearby Ralston and Papillion."),
            ("Can you detail my car at work?", "In many cases, yes. We need permission to work on the vehicle there and room around it — just tell us where you park when you request a quote."),
            ("What's included in a weekly wash?", "An exterior wash with paint sealant, plus windows and wheels, for $30 a wash with no commitment. If you'd like the interior done too, the Monthly and Bi-Monthly plans add a quick interior wipe and vacuum."),
        ],
        "review": 1,
        "neighbors": ["ralston", "papillion", "omaha"],
    },
    {
        "name": "Elkhorn", "slug": "elkhorn",
        "desc": "Mobile car detailing in Elkhorn, NE — Old Town, Indian Creek, Skyline Ranches & Village Pointe. Premium detailing & ceramic coating at your home.",
        "hero": "West-metro Elkhorn detailing at your home or office — premium results without driving across town.",
        "intro": [
            "Elkhorn has grown from a small town on Main Street into one of the busiest parts of the west metro, with new subdivisions going up every year. For a lot of families out here, the nearest detail shop means a drive east on Dodge and an afternoon of waiting. We skip all that by bringing the shop to your driveway.",
            "New construction nearby means dust, mud and the occasional tracked-in mess, and nicer vehicles mean more people want their paint protected. We handle both — deep interior cleaning and long-lasting ceramic protection, done at home.",
        ],
        "nearby": "Old Town Elkhorn, Indian Creek, Skyline Ranches and the Village Pointe area",
        "cards": [
            ("truck", "New-build dust and mud", "Living near active construction? Dust settles on paint and gets ground into carpets. An exterior wash with paint sealant plus a full interior shampoo resets everything."),
            ("sparkles", "Ceramic coating at home", "Ceramic coating and paint correction don't require a trip to a shop. We can protect your paint in your own driveway — text us the vehicle for a quote."),
            ("calendar", "Busy-family upkeep", "Between school, practices and work, the car rarely sits still. The Monthly Plan ($110/month) keeps it clean on a set schedule."),
        ],
        "faqs": [
            ("Do you come out to Elkhorn?", "Yes — Old Town Elkhorn, Indian Creek, Skyline Ranches, the Village Pointe area and the newer subdivisions further west. We also cover nearby Bennington and West Omaha."),
            ("Can you do paint correction in my driveway?", "Yes, weather permitting. Paint correction removes swirls and light scratches with machine polishing, and we usually pair it with a ceramic coating to lock in the result."),
            ("Do you detail trucks and large SUVs?", "Yes. Text us the year, make and model and we'll send an exact quote."),
        ],
        "review": 0,
        "neighbors": ["bennington", "millard", "omaha"],
    },
    {
        "name": "Gretna", "slug": "gretna",
        "desc": "Mobile auto detailing in Gretna, NE — near Nebraska Crossing, downtown & new neighborhoods along Highway 370. Detailing & ceramic coating at home.",
        "hero": "Fast-growing Gretna gets the same showroom finish without leaving home — we bring the detailing studio to your driveway.",
        "intro": [
            "Gretna is one of the fastest-growing cities in Nebraska, and much of that growth is brand-new homes along Highway 370 and around Nebraska Crossing. New neighborhood, new driveway — and often a newer vehicle worth protecting. We detail right there, no shop visit needed.",
            "Dust and gravel from ongoing construction, plus the I-80 drive for anyone commuting into Omaha, mean paint takes a beating out here. We focus on getting that grit off safely and putting protection back on.",
        ],
        "nearby": "downtown Gretna, Nebraska Crossing and the new neighborhoods along Highway 370",
        "cards": [
            ("sparkles", "Protect a new vehicle early", "The best time to ceramic coat is while the paint is new. A coating adds gloss and makes road grime and bird droppings rinse off easily."),
            ("truck", "Construction-zone grime", "The Boujee Express includes an underbody wash, iron decontamination and a clay bar — ideal when construction dust and gravel are part of the daily drive."),
            ("shield", "I-80 commuter upkeep", "Bugs and road film build up fast on the commute. Weekly Washes ($30) keep the exterior clean and sealed, with no commitment."),
        ],
        "faqs": [
            ("Do you serve all of Gretna?", "Yes — downtown Gretna, the newer neighborhoods along Highway 370, the area around Nebraska Crossing and out toward Schramm Park. Text us your address to confirm."),
            ("When should I ceramic coat a new car?", "As early as possible, before the paint picks up swirls and contamination. If it already has some, paint correction removes them first, then the coating locks in the finish."),
            ("Do you need anything from me?", "Just access to the vehicle. We carry our own water and power, so it works even at a new build that doesn't have landscaping or outdoor outlets yet."),
        ],
        "review": 1,
        "neighbors": ["papillion", "millard"],
    },
    {
        "name": "Bennington", "slug": "bennington",
        "desc": "Mobile detailing in Bennington, NE — Newport Landing, the Lake Cunningham area & nearby acreages. Interior, exterior & engine bay detailing at home.",
        "hero": "Bennington and the northwest metro — detailed in your driveway with a self-contained setup that needs nothing from you.",
        "intro": [
            "Bennington still has a small-town feel, with acreages and gravel roads just outside town and lake living at Newport Landing. That mix means vehicles here see more dust, mud and lake days than most — and the nearest detail shop isn't exactly around the corner.",
            "We bring everything with us — water, power, tools and products — so whether you're on a lot in town or out on an acreage, we do the job where your vehicle is parked.",
        ],
        "nearby": "Newport Landing, downtown Bennington and the Lake Cunningham area",
        "cards": [
            ("truck", "Gravel-road dust", "Fine gravel dust works into door jambs, vents and carpets. Our Interior Detail steam-cleans vents, doors and trim and includes the door jambs and trunk."),
            ("star", "Lake toys too", "We detail more than cars — our gallery includes a jet ski and a motorcycle. Text us what you've got and we'll quote it."),
            ("wrench", "Under the hood", "Trucks that work hard get dirty where you can't see. Add an Engine Bay Detail ($50) to any package for a clean, dressed engine compartment."),
        ],
        "faqs": [
            ("Do you travel to acreages outside Bennington?", "Yes. Our setup is fully self-contained, so we don't need a hose or an outlet — just room to park near the vehicle."),
            ("Do you detail jet skis or boats?", "We've detailed jet skis and motorcycles. Text us a photo and the size of what you have and we'll let you know what we can do and what it costs."),
            ("Do you serve Newport Landing?", "Yes — Newport Landing, the Lake Cunningham area, downtown Bennington and nearby Elkhorn."),
        ],
        "review": 2,
        "neighbors": ["elkhorn", "omaha"],
    },
    {
        "name": "Ralston", "slug": "ralston",
        "desc": "Mobile auto detailing in Ralston, NE — downtown, Main Street & the Liberty First Credit Union Arena area. We detail at your home. Quote within the hour.",
        "hero": "Ralston's tight-knit community gets full-service detailing brought right to the door — convenient, insured, and eco-friendly.",
        "intro": [
            "Ralston is a small city surrounded by Omaha and La Vista, with a real hometown feel — the kind of place where the Fourth of July parade is a big deal. Homes sit close together, driveways are often short, and plenty of people park on the street. None of that is a problem for us.",
            "Because we carry our own water and power, we can work in a tight driveway or at the curb where it's allowed. You don't need to clear out the garage or run a hose.",
        ],
        "nearby": "downtown Ralston, Main Street and the Liberty First Credit Union Arena area",
        "cards": [
            ("pin", "Tight driveway? Fine.", "Short driveways and street parking are normal here. All we need is room to work around the vehicle."),
            ("sparkles", "Show-ready shine", "Heading to a car show or just want the deepest gloss on the block? Paint correction and ceramic coating bring out a deep, even finish."),
            ("calendar", "Easy, regular upkeep", "The Bi-Monthly Plan ($140 every two months) keeps a daily driver clean without having to remember to book."),
        ],
        "faqs": [
            ("Do you serve all of Ralston?", "Yes — downtown and Main Street, the neighborhoods around the Liberty First Credit Union Arena and the rest of town, plus neighboring La Vista and Omaha."),
            ("What if I only have street parking?", "Text us where the vehicle is parked. As long as it's legal and safe to work there, we can usually detail it right at the curb."),
            ("Can you get a car ready for a show?", "Yes. A clay bar and paint correction remove contamination and swirls, and a ceramic coating or wax adds the final gloss. Text us the vehicle and the date of the show."),
        ],
        "review": 3,
        "neighbors": ["la-vista", "omaha"],
    },
    {
        "name": "Millard", "slug": "millard",
        "desc": "Mobile car detailing in Millard (Southwest Omaha) — Old Millard, Zorinsky Lake & Oak View areas. Detailing, ceramic coating & maintenance plans.",
        "hero": "Southwest Omaha's Millard — from Old Millard to the neighborhoods around Zorinsky Lake — gets premium mobile detailing at home or the office.",
        "intro": [
            "Millard was its own town until Omaha annexed it in 1971, and it still feels like its own part of the city — established neighborhoods, Millard Public Schools, and Zorinsky Lake as the backyard. It's also a drive from most detail shops, which is exactly why mobile detailing makes sense here.",
            "We come to your driveway in Millard, or to your office along the West Center Road and L Street corridors, with everything we need on board.",
        ],
        "nearby": "Old Millard, Zorinsky Lake and the Oak View area",
        "cards": [
            ("users", "Lake-day cleanup", "Sand, sunscreen and wet towels after a day at Zorinsky add up. An Interior Detail includes shampoo and extraction, steam-cleaned trim and an odor neutralizer."),
            ("calendar", "Clean, automatically", "On a schedule, your car never gets bad. Washes start at $30, or $110/month for interior and exterior upkeep."),
            ("sun", "Cloudy headlights?", "Older vehicles often have yellowed, hazy headlights that hurt visibility at night. Headlight Restoration is $65 and can be added to any package."),
        ],
        "faqs": [
            ("Is Millard part of your service area?", "Yes — all of Millard and Southwest Omaha, including Old Millard, the Zorinsky Lake area and the neighborhoods around Oak View. We also serve nearby Elkhorn and Gretna."),
            ("Do you offer recurring washes?", "Yes. Weekly Washes are $30 with no commitment, the Monthly Plan is $110/month, and the Bi-Monthly Plan is $140 every two months — both plans include a quick interior wipe and vacuum."),
            ("How do I book?", "Text (402) 515-9157 or use the quote form with your vehicle and address. We'll confirm a time and exact price within the hour."),
        ],
        "review": 3,
        "neighbors": ["omaha", "elkhorn", "gretna"],
    },
    {
        "name": "Yutan", "slug": "yutan",
        "desc": "Mobile detailing in Yutan, NE and Saunders County — trucks, farm vehicles and family cars detailed at your home. No hookups needed. Quote within the hour.",
        "hero": "We proudly serve Yutan and the Saunders County area with rural-friendly mobile detailing that travels to you.",
        "intro": [
            "Yutan sits about half an hour west of Omaha, out in Saunders County farm country. That's a long way to drive for a detail — and a long way to leave a vehicle sitting at a shop. So we make the trip instead, with everything we need on board.",
            "Gravel roads, field dust and mud are part of daily life here, and they're tough on paint, carpets and engine bays. Our self-contained setup means we don't need a hose or an outlet — we can work at a farmhouse, an acreage or a driveway in town.",
        ],
        "nearby": "Yutan and the wider Saunders County area",
        "cards": [
            ("shield", "Built for gravel roads", "The Boujee Express includes an underbody wash, iron decontamination and a clay bar, plus a ceramic spray sealant that helps dust rinse off later."),
            ("wrench", "Work trucks welcome", "Farm and work trucks get the same care as anything else. Add an Engine Bay Detail ($50) to clean up a dusty engine compartment."),
            ("truck", "Mud-season interiors", "Boots and mud are hard on carpets. Our Interior Detail shampoos and extracts carpets and seats and steam-cleans the rest."),
        ],
        "faqs": [
            ("Do you really come out to Yutan?", "Yes. Yutan and the surrounding Saunders County area are part of our service area. Text us your address and we'll confirm a time."),
            ("Do you need water or power at my place?", "No. We bring our own water and power, so it works at an acreage, a farm, or anywhere else the vehicle is parked."),
            ("Can you handle a really dirty truck?", "That's a normal day for us. Text us a photo and we'll recommend the right package and give you an exact price."),
        ],
        "review": 1,
        "neighbors": ["elkhorn", "bennington"],
    },
]
