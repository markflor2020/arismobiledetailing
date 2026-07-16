#!/usr/bin/env python3
"""Generate Ari's Mobile Detailing service-area pages (local SEO).

Creates:
  - areas.html               (hub page linking to every city)
  - detailing-<slug>.html    (one landing page per city)

Also patches the existing top-level pages to add an "Areas" nav link.
Re-run any time to regenerate. Output is plain static HTML.
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).parent
PHONE = "+14025159157"

# (City, slug, hero blurb, second paragraph, nearby areas string)
CITIES = [
    ("Omaha", "omaha",
     "From Dundee and Benson to Aksarben and West Omaha, we bring the full detailing shop to your driveway — no need to fight traffic or lose your Saturday.",
     "As a locally owned Omaha business, we know the city's roads chew up paint with salt in winter and dust all summer. We come to your home or office anywhere in town and restore that showroom shine on the spot.",
     "Midtown, Dundee, Benson, Aksarben and West Omaha"),
    ("Bellevue", "bellevue",
     "Mobile auto detailing for Bellevue families and Offutt-area drivers — we come to you, so a busy schedule never means a dirty car.",
     "Whether you're near Fontenelle Forest, Twin Creek, or out by the base, we arrive fully equipped and detail your vehicle right where it's parked.",
     "Twin Creek, Fontenelle Forest and the Offutt AFB area"),
    ("Papillion", "papillion",
     "Papillion is one of the best places to live in Nebraska — and we help keep its driveways spotless with detailing that comes to you.",
     "From Shadow Lake to Midlands, we bring professional interior and exterior detailing to your home so your ride always looks its best.",
     "Shadow Lake, Midlands and Halleck Park"),
    ("La Vista", "la-vista",
     "Mobile detailing across La Vista — from City Centre to Central Park — done in your own driveway while you get on with your day.",
     "No drop-off, no waiting room. We pull up with everything we need and leave your vehicle looking better than the day you bought it.",
     "La Vista City Centre, Central Park and Southport"),
    ("Elkhorn", "elkhorn",
     "West-metro Elkhorn detailing at your home or office — premium results without driving across town.",
     "Indian Creek, The Ridges, and the surrounding neighborhoods trust us for swirl-free paint, fresh interiors, and long-lasting protection.",
     "Indian Creek, The Ridges and Skyline Ranches"),
    ("Gretna", "gretna",
     "Fast-growing Gretna gets the same showroom finish without leaving home — we bring the detailing studio to your driveway.",
     "Near Nebraska Crossing, Remington, or Tributary, our fully mobile setup means a flawless detail with zero hassle for you.",
     "Nebraska Crossing, Remington and Tributary"),
    ("Bennington", "bennington",
     "Bennington and the northwest metro — detailed in your driveway with a self-contained setup that needs nothing from you.",
     "From Newport Landing to the Lake Cunningham area, we deliver deep interior cleans, exterior decontamination, and protection that lasts.",
     "Newport Landing and the Lake Cunningham area"),
    ("Ralston", "ralston",
     "Ralston's tight-knit community gets full-service detailing brought right to the door — convenient, insured, and eco-friendly.",
     "Near the Ralston Arena or anywhere in town, we treat every vehicle like our own and don't call it done until you're grinning.",
     "the Ralston Arena and Hinge Park"),
    ("Millard", "millard",
     "Southwest Omaha's Millard — Mannheim, Cimarron, and beyond — gets premium mobile detailing at home or the office.",
     "Skip the line at the car wash. We bring pro-grade tools and premium products to your driveway and restore that deep, even shine.",
     "Mannheim, Cimarron and Montclair"),
    ("Yutan", "yutan",
     "We proudly serve Yutan and the Saunders County area with rural-friendly mobile detailing that travels to you.",
     "Out-of-the-way driveways are no problem — our setup is fully self-contained, so distance never gets between your vehicle and a spotless finish.",
     "Yutan and the wider Saunders County area"),
]

NAV_ITEMS = [
    ("Home", "index.html"),
    ("Services", "services.html"),
    ("Packages", "packages.html"),
    ("Results", "results.html"),
    ("Areas", "areas.html"),
    ("Reviews", "reviews.html"),
    ("Contact", "contact.html"),
]

CHEV_PHONE = '<svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path d="M13.8 16.6a1 1 0 0 0 1.2-.3l.4-.5a2 2 0 0 1 1.6-.8h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.5.4a1 1 0 0 0-.3 1.2 14 14 0 0 0 6.4 6.4"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'


def nav(active):
    out = []
    for label, href in NAV_ITEMS:
        cls = ' class="is-active"' if href == active else ""
        out.append(f'      <a href="{href}"{cls}>{label}</a>')
    return "\n".join(out)


def drawer(active):
    out = []
    for label, href in NAV_ITEMS:
        cls = ' class="is-active"' if href == active else ""
        out.append(f'    <a href="{href}"{cls}>{label}</a>')
    return "\n".join(out)


def footer_nav():
    return "\n".join(f'      <a href="{href}">{label}</a>' for label, href in NAV_ITEMS)


def footer_areas():
    links = "\n".join(
        f'      <a href="detailing-{slug}.html">{name}</a>'
        for name, slug, *_ in CITIES
    )
    return f"""  <div class="wrap footer__areas">
    <span class="footer__areas-label">Areas we serve</span>
    <nav class="footer__areas-links" aria-label="Service areas">
{links}
      <a href="areas.html" class="footer__areas-all">All areas →</a>
    </nav>
  </div>"""


def shell(title, desc, body, active):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="icon" href="assets/logo.svg" />
<link rel="stylesheet" href="styles.css" />
</head>
<body data-page="areas">
<div class="grain" aria-hidden="true"></div>

<div class="utilbar">
  <div class="wrap utilbar__inner">
    <a class="utilbar__phone" href="tel:{PHONE}">{CHEV_PHONE}(402) 515-9157</a>
    <span class="utilbar__sep">·</span>
    <span class="utilbar__note">Quote back within the hour</span>
    <span class="utilbar__spacer"></span>
    <a href="https://www.instagram.com/aris_mobile_detailing/" target="_blank" rel="noreferrer" aria-label="Instagram" class="utilbar__soc"><svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><rect width="20" height="20" x="2" y="2" rx="5"/><path d="M16 11.4A4 4 0 1 1 12.6 8 4 4 0 0 1 16 11.4z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg></a>
    <a href="https://www.facebook.com/p/Aris-Mobile-Detailing-100068821100332/" target="_blank" rel="noreferrer" aria-label="Facebook" class="utilbar__soc"><svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
  </div>
</div>

<header class="header" id="top">
  <div class="wrap header__inner">
    <a class="brand" href="index.html" aria-label="Ari's Mobile Detailing — home">
      <span class="brand__medallion"><img src="assets/logo.svg" alt="" width="44" height="44" /></span>
      <span class="brand__name">
        <span class="brand__line1">Ari's <em>Mobile</em></span>
        <span class="brand__line2">Detailing · Omaha, NE</span>
      </span>
    </a>
    <nav class="nav" id="nav" aria-label="Primary">
{nav(active)}
    </nav>
    <div class="header__cta">
      <a class="btn btn--ghost" href="tel:{PHONE}">{CHEV_PHONE}<span>Call</span></a>
      <a class="btn btn--red" href="contact.html">Get a Quote</a>
    </div>
    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>

<div class="drawer" id="drawer" aria-hidden="true">
  <nav class="drawer__nav" aria-label="Mobile">
{drawer(active)}
  </nav>
  <div class="drawer__cta">
    <a class="btn btn--red btn--block" href="contact.html">Get a Quote</a>
    <a class="btn btn--ghost btn--block" href="tel:{PHONE}">Call (402) 515-9157</a>
  </div>
</div>

{body}

<footer class="footer">
  <div class="wrap footer__inner">
    <div class="footer__brand">
      <span class="brand__medallion brand__medallion--sm"><img src="assets/logo.svg" alt="" width="34" height="34" /></span>
      <div>
        <div class="footer__name">Ari's Mobile Detailing</div>
        <div class="footer__loc">Omaha, NE &amp; the metro · (402) 515-9157</div>
      </div>
    </div>
    <nav class="footer__nav" aria-label="Footer">
{footer_nav()}
    </nav>
  </div>
{footer_areas()}
  <div class="wrap footer__base">
    <span>© <span id="year">2026</span> Ari's Mobile Detailing. All rights reserved. · <a href="privacy.html">Privacy Policy</a></span>
    <span class="footer__made">Showroom shine, driveway convenience.</span>
  </div>
</footer>

<div class="mobar">
  <a class="mobar__btn" href="sms:{PHONE}"><svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path d="M22 17a2 2 0 0 1-2 2H6.8a2 2 0 0 0-1.4.6l-2.2 2.2A.7.7 0 0 1 2 21.3V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2z"/></svg>Text</a>
  <a class="mobar__btn" href="tel:{PHONE}">{CHEV_PHONE}Call</a>
  <a class="mobar__btn mobar__btn--red" href="contact.html"><svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path d="M8 2v4M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/></svg>Quote</a>
</div>

<script src="script.js"></script>
</body>
</html>
"""


def city_page(name, slug, blurb, blurb2, nearby):
    body = f"""<section class="phero">
  <div class="wrap phero__inner">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><a href="areas.html">Areas</a><span>{name}</span></nav>
    <span class="eyebrow reveal" data-d="0">Service area</span>
    <h1 class="phero__title reveal" data-d="1">Mobile Auto Detailing in {name}, NE</h1>
    <p class="phero__sub reveal" data-d="2">{blurb}</p>
  </div>
</section>

<main>
<section class="section section--alt">
  <div class="wrap area__grid">
    <div class="area__text reveal">
      <span class="eyebrow">We come to you</span>
      <h2 class="sec-title">Detailing that comes to {name}.</h2>
      <p>{blurb2}</p>
      <p>Every detail is performed right in your driveway with a fully self-contained setup — no water or power hookups needed. Proudly serving {name} and nearby {nearby}.</p>
      <div class="about__points">
        <span>{CHECK}100% mobile — we travel to {name}</span>
        <span>{CHECK}Fully insured &amp; eco-friendly products</span>
        <span>{CHECK}Quote back within the hour</span>
      </div>
      <a class="btn btn--red btn--lg" href="contact.html">Get a quote in {name}</a>
    </div>
    <aside class="area__card reveal" data-d="1">
      <h3>What we offer in {name}</h3>
      <ul class="area__list">
        <li>Interior &amp; exterior detailing</li>
        <li>Full detail packages from $180</li>
        <li>Ceramic coating &amp; paint correction</li>
        <li>Engine bay detailing</li>
        <li>Maintenance plans from $30/wash</li>
      </ul>
      <a class="btn btn--ghost btn--block" href="services.html">See all services</a>
      <a class="btn btn--ghost btn--block" href="packages.html">View packages &amp; pricing</a>
    </aside>
  </div>
</section>

<section class="section reviews">
  <div class="wrap reviews__grid">
    <div class="reviews__summary reveal">
      <span class="eyebrow">Trusted locally</span>
      <div class="reviews__score">5.0</div>
      <div class="reviews__stars" aria-hidden="true">★★★★★</div>
      <p class="reviews__meta">Rated 5.0 by drivers across the Omaha metro.</p>
      <a class="btn btn--ghost" href="reviews.html">Read the reviews {ARROW}</a>
    </div>
    <figure class="quote quote--feature reveal" data-d="1">
      <div class="quote__stars" aria-hidden="true">★★★★★</div>
      <blockquote>Our Explorer carries around 4 kids under the age of 7 on a daily basis and Ari makes it look like new every time he shows up. Always on time, great attitude and customer service and always has a smile on his face. Great pricing and outstanding work.</blockquote>
      <figcaption><strong>Cody Buscher</strong><span>Facebook recommendation · Jul 2024</span></figcaption>
    </figure>
  </div>
</section>

<section class="section section--alt cta-band">
  <div class="wrap cta-band__inner reveal">
    <h2 class="sec-title">Ready for a spotless ride in <span class="text-red">{name}?</span></h2>
    <p>Text us your vehicle and we'll come to you anywhere in {name} — with a tailored quote back within the hour.</p>
    <div class="cta-band__actions">
      <a class="btn btn--red btn--lg" href="contact.html">Get a quote</a>
      <a class="btn btn--ghost btn--lg" href="tel:{PHONE}">Call (402) 515-9157</a>
    </div>
  </div>
</section>
</main>"""
    title = f"Mobile Auto Detailing in {name}, NE — Ari's Mobile Detailing"
    desc = f"Mobile auto detailing in {name}, NE. Interior & exterior detailing, ceramic coating, paint correction & maintenance plans — done at your home or office. Quote within the hour."
    return shell(title, desc, body, "areas.html")


def hub_page():
    cards = []
    for name, slug, blurb, *_ in CITIES:
        cards.append(f"""      <a class="area-card spotlight reveal" href="detailing-{slug}.html">
        <h3>{name}, NE</h3>
        <p>{blurb}</p>
        <span class="teaser__cta">View {name} {ARROW}</span>
      </a>""")
    grid = "\n".join(cards)
    body = f"""<section class="phero">
  <div class="wrap phero__inner">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>Areas</span></nav>
    <span class="eyebrow reveal" data-d="0">Where we work</span>
    <h1 class="phero__title reveal" data-d="1">Areas we serve across the Omaha metro.</h1>
    <p class="phero__sub reveal" data-d="2">Ari's Mobile Detailing is 100% mobile — we bring the detailing shop to driveways all over the metro. Find your city below, or just <a href="contact.html">text us</a> and ask.</p>
  </div>
</section>

<main>
<section class="section section--alt">
  <div class="wrap">
    <div class="area-cards">
{grid}
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap cta-band__inner reveal">
    <h2 class="sec-title">Don't see your town?</h2>
    <p>We cover the whole Omaha metro and beyond. If you're nearby, there's a good chance we'll come to you — just ask.</p>
    <div class="cta-band__actions">
      <a class="btn btn--red btn--lg" href="contact.html">Get a quote</a>
      <a class="btn btn--ghost btn--lg" href="tel:{PHONE}">Call (402) 515-9157</a>
    </div>
  </div>
</section>
</main>"""
    title = "Areas We Serve — Mobile Detailing Across the Omaha Metro | Ari's Mobile Detailing"
    desc = "Ari's Mobile Detailing serves Omaha, Bellevue, Papillion, La Vista, Elkhorn, Gretna, Bennington, Ralston, Millard and Yutan, NE. Mobile detailing that comes to you."
    return shell(title, desc, body, "areas.html")


def patch_existing_nav():
    """Add an 'Areas' link after every 'Results' link in the hand-written pages."""
    pages = ["index.html", "services.html", "packages.html",
             "results.html", "reviews.html", "contact.html"]
    # match a Results anchor on its own line, capturing its indentation
    pat = re.compile(r'^([ \t]*)(<a href="results\.html"[^>]*>Results</a>)$', re.M)
    for p in pages:
        fp = ROOT / p
        html = fp.read_text()
        if 'href="areas.html"' in html:
            print(f"  {p}: already has Areas link, skipping")
            continue
        html = pat.sub(lambda m: f'{m.group(1)}{m.group(2)}\n{m.group(1)}<a href="areas.html">Areas</a>', html)
        fp.write_text(html)
        print(f"  {p}: added Areas nav link")


def patch_footers():
    """Add the 'Areas we serve' link row to the footer of hand-written pages."""
    pages = ["index.html", "services.html", "packages.html",
             "results.html", "reviews.html", "contact.html"]
    block = footer_areas()
    marker = '  <div class="wrap footer__base">'
    for p in pages:
        fp = ROOT / p
        html = fp.read_text()
        if "footer__areas" in html:
            print(f"  {p}: already has footer areas, skipping")
            continue
        html = html.replace(marker, block + "\n" + marker, 1)
        fp.write_text(html)
        print(f"  {p}: added footer areas row")


def main():
    print("Patching existing pages:")
    patch_existing_nav()
    patch_footers()
    print("Generating area pages:")
    (ROOT / "areas.html").write_text(hub_page())
    print("  areas.html (hub)")
    for name, slug, blurb, blurb2, nearby in CITIES:
        (ROOT / f"detailing-{slug}.html").write_text(city_page(name, slug, blurb, blurb2, nearby))
        print(f"  detailing-{slug}.html ({name})")
    # re-apply SEO tags + rebuild sitemap so regenerated pages stay optimized
    seo_py = ROOT / "seo.py"
    if seo_py.exists():
        import subprocess
        import sys as _sys
        print("Refreshing SEO (seo.py):")
        subprocess.run([_sys.executable, str(seo_py)], check=False)
    print("Done.")


if __name__ == "__main__":
    main()
