#!/usr/bin/env python3
"""Generate Ari's Mobile Detailing service-area pages (local SEO).

Creates:
  - areas.html               (hub page linking to every city)
  - detailing-<slug>.html    (one landing page per city)

Also patches the existing top-level pages to add an "Areas" nav link.
Edit city copy in area_content.py, then re-run. Output is plain static HTML.
"""
import re
import html
import pathlib

ROOT = pathlib.Path(__file__).parent
PHONE = "+14025159157"

# Per-city copy (intro, local cards, FAQ, meta description) lives in area_content.py.
from area_content import CITIES, REVIEWS

NAV_ITEMS = [
    ("Home", "/"),
    ("Services", "services"),
    ("Packages", "packages"),
    ("Results", "results"),
    ("Areas", "areas"),
    ("Reviews", "reviews"),
    ("Contact", "contact"),
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
        f'      <a href="detailing-{c["slug"]}">{c["name"]}</a>'
        for c in CITIES
    )
    return f"""  <div class="wrap footer__areas">
    <span class="footer__areas-label">Areas we serve</span>
    <nav class="footer__areas-links" aria-label="Service areas">
{links}
      <a href="areas" class="footer__areas-all">All areas →</a>
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
    <a class="brand" href="/">
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
      <a class="btn btn--red" href="contact">Get a Quote</a>
    </div>
    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>

<div class="drawer" id="drawer" aria-hidden="true" inert>
  <nav class="drawer__nav" aria-label="Mobile">
{drawer(active)}
  </nav>
  <div class="drawer__cta">
    <a class="btn btn--red btn--block" href="contact">Get a Quote</a>
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
    <span>© <span id="year">2026</span> Ari's Mobile Detailing. All rights reserved. · <a href="privacy">Privacy Policy</a></span>
    <span class="footer__made">Showroom shine, driveway convenience.</span>
  </div>
</footer>

<div class="mobar">
  <a class="mobar__btn" href="sms:{PHONE}"><svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path d="M22 17a2 2 0 0 1-2 2H6.8a2 2 0 0 0-1.4.6l-2.2 2.2A.7.7 0 0 1 2 21.3V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2z"/></svg>Text</a>
  <a class="mobar__btn" href="tel:{PHONE}">{CHEV_PHONE}Call</a>
  <a class="mobar__btn mobar__btn--red" href="contact"><svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path d="M8 2v4M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/></svg>Quote</a>
</div>

<script src="script.js"></script>
</body>
</html>
"""


ICONS = {  # Lucide-style line icons for the local cards
    "calendar": '<path d="M8 2v4M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.7 9a1 1 0 0 1-.7 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1.2 1.2 0 0 1 1.5 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1z"/>',
    "star": '<path d="M11 2 9 7l-5 .8 3.6 3.5L7 16l4-2 4 2-.6-4.7L18 7.8 13 7z"/>',
    "pin": '<path d="M20 10c0 5-5.5 10.2-7.4 11.8a1 1 0 0 1-1.2 0C9.5 20.2 4 15 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "truck": '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
    "sparkles": '<path d="M9.94 15.5A2 2 0 0 0 8.5 14.06l-6.14-1.58a.5.5 0 0 1 0-.96L8.5 9.94A2 2 0 0 0 9.94 8.5l1.58-6.14a.5.5 0 0 1 .96 0l1.58 6.14a2 2 0 0 0 1.44 1.44l6.14 1.58a.5.5 0 0 1 0 .96l-6.14 1.58a2 2 0 0 0-1.44 1.44l-1.58 6.14a.5.5 0 0 1-.96 0z"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "briefcase": '<rect width="20" height="14" x="2" y="7" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
}


def esc(text):
    """Plain-text copy -> safe HTML (apostrophes left readable)."""
    return html.escape(text, quote=False)


def city_page(c):
    name, slug = c["name"], c["slug"]
    names = {x["slug"]: x["name"] for x in CITIES}
    intro = "\n".join(f"      <p>{esc(p)}</p>" for p in c["intro"])
    cards = "\n".join(
        f"""      <div class="why__item reveal" data-d="{i}">
        <div class="why__icon"><svg viewBox="0 0 24 24" class="ico" aria-hidden="true">{ICONS[icon]}</svg></div>
        <h3>{esc(title)}</h3>
        <p>{esc(text)}</p>
      </div>"""
        for i, (icon, title, text) in enumerate(c["cards"]))
    faqs = "\n".join(
        f"""      <details class="faq__item">
        <summary>{esc(q)}<span class="faq__plus"></span></summary>
        <div class="faq__a">{esc(a)}</div>
      </details>"""
        for q, a in c["faqs"])
    nearby_links = ", ".join(f'<a href="detailing-{n}">{names[n]}</a>' for n in c["neighbors"])
    rv_name, rv_text = REVIEWS[c["review"]]

    body = f"""<section class="phero">
  <div class="wrap phero__inner">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><a href="areas">Areas</a><span>{name}</span></nav>
    <span class="eyebrow reveal" data-d="0">Service area</span>
    <h1 class="phero__title reveal" data-d="1">Mobile Auto Detailing in {name}, NE</h1>
    <p class="phero__sub reveal" data-d="2">{esc(c["hero"])}</p>
  </div>
</section>

<main>
<section class="section section--alt">
  <div class="wrap area__grid">
    <div class="area__text reveal">
      <span class="eyebrow">We come to you</span>
      <h2 class="sec-title">Detailing that comes to {name}.</h2>
{intro}
      <p>Proudly serving {name} and nearby {esc(c["nearby"])}.</p>
      <div class="about__points">
        <span>{CHECK}100% mobile — we travel to {name}</span>
        <span>{CHECK}Fully insured &amp; eco-friendly products</span>
        <span>{CHECK}Quote back within the hour</span>
      </div>
      <a class="btn btn--red btn--lg" href="contact">Get a quote in {name}</a>
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
      <a class="btn btn--ghost btn--block" href="services">See all services</a>
      <a class="btn btn--ghost btn--block" href="packages">View packages &amp; pricing</a>
    </aside>
  </div>
</section>

<section class="section why">
  <div class="wrap">
    <div class="sec-head reveal">
      <div>
        <span class="eyebrow">Local know-how</span>
        <h2 class="sec-title">Made for {name} drivers.</h2>
      </div>
    </div>
    <div class="why__grid">
{cards}
    </div>
  </div>
</section>

<section class="section section--alt reviews">
  <div class="wrap reviews__grid">
    <div class="reviews__summary reveal">
      <span class="eyebrow">Trusted locally</span>
      <div class="reviews__score">5.0</div>
      <div class="reviews__stars" aria-hidden="true">★★★★★</div>
      <p class="reviews__meta">Rated 5.0 on Google by drivers across the Omaha metro.</p>
      <a class="btn btn--ghost" href="reviews">Read the reviews {ARROW}</a>
    </div>
    <figure class="quote quote--feature reveal" data-d="1">
      <div class="quote__stars" aria-hidden="true">★★★★★</div>
      <blockquote>{esc(rv_text)}</blockquote>
      <figcaption><strong>{esc(rv_name)}</strong><span>Google review</span></figcaption>
    </figure>
  </div>
</section>

<section class="section faq">
  <div class="wrap faq__grid">
    <div class="faq__intro reveal">
      <span class="eyebrow">Good to know</span>
      <h2 class="sec-title">{name} questions, answered.</h2>
      <p class="sec-sub">Also serving nearby {nearby_links}. Anything else? Text us at <a href="tel:{PHONE}">(402) 515-9157</a>.</p>
    </div>
    <div class="faq__list reveal" data-d="1">
{faqs}
    </div>
  </div>
</section>

<section class="section section--alt cta-band">
  <div class="wrap cta-band__inner reveal">
    <h2 class="sec-title">Ready for a spotless ride in <span class="text-red">{name}?</span></h2>
    <p>Text us your vehicle and we'll come to you anywhere in {name} — with a tailored quote back within the hour.</p>
    <div class="cta-band__actions">
      <a class="btn btn--red btn--lg" href="contact">Get a quote</a>
      <a class="btn btn--ghost btn--lg" href="tel:{PHONE}">Call (402) 515-9157</a>
    </div>
  </div>
</section>
</main>"""
    title = f"Mobile Auto Detailing in {name}, NE — Ari's Mobile Detailing"
    return shell(title, html.escape(c["desc"]), body, "areas")


def hub_page():
    cards = []
    for c in CITIES:
        name, slug, blurb = c["name"], c["slug"], esc(c["hero"])
        cards.append(f"""      <a class="area-card spotlight reveal" href="detailing-{slug}">
        <h3>{name}, NE</h3>
        <p>{blurb}</p>
        <span class="teaser__cta">View {name} {ARROW}</span>
      </a>""")
    grid = "\n".join(cards)
    body = f"""<section class="phero">
  <div class="wrap phero__inner">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>Areas</span></nav>
    <span class="eyebrow reveal" data-d="0">Where we work</span>
    <h1 class="phero__title reveal" data-d="1">Areas we serve across the Omaha metro.</h1>
    <p class="phero__sub reveal" data-d="2">Ari's Mobile Detailing is 100% mobile — we bring the detailing shop to driveways all over the metro. Find your city below, or just <a href="contact">text us</a> and ask.</p>
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
      <a class="btn btn--red btn--lg" href="contact">Get a quote</a>
      <a class="btn btn--ghost btn--lg" href="tel:{PHONE}">Call (402) 515-9157</a>
    </div>
  </div>
</section>
</main>"""
    title = "Areas We Serve — Mobile Detailing Across the Omaha Metro | Ari's Mobile Detailing"
    desc = "Ari's Mobile Detailing serves Omaha, Bellevue, Papillion, La Vista, Elkhorn, Gretna, Bennington, Ralston, Millard and Yutan, NE. Mobile detailing that comes to you."
    return shell(title, desc, body, "areas")


def patch_existing_nav():
    """Add an 'Areas' link after every 'Results' link in the hand-written pages."""
    pages = ["index.html", "services.html", "packages.html",
             "results.html", "reviews.html", "contact.html"]
    # match a Results anchor on its own line, capturing its indentation
    pat = re.compile(r'^([ \t]*)(<a href="results"[^>]*>Results</a>)$', re.M)
    for p in pages:
        fp = ROOT / p
        html = fp.read_text()
        if 'href="areas"' in html:
            print(f"  {p}: already has Areas link, skipping")
            continue
        html = pat.sub(lambda m: f'{m.group(1)}{m.group(2)}\n{m.group(1)}<a href="areas">Areas</a>', html)
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
    for c in CITIES:
        (ROOT / f"detailing-{c['slug']}.html").write_text(city_page(c))
        print(f"  detailing-{c['slug']}.html ({c['name']})")
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
