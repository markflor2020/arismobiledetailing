#!/usr/bin/env python3
"""Inject technical SEO into every page + generate sitemap.xml and robots.txt.

Idempotent: strips the tags it manages and re-inserts them, so run it any time
(and always after generate_areas.py). Adds per-page canonical, Open Graph,
Twitter, geo + theme-color meta, and a sitewide LocalBusiness JSON-LD block.

⚠️  DOMAIN: set DOMAIN below to the real domain once you have one, then re-run.
"""
import re
import glob
import datetime
import pathlib

ROOT = pathlib.Path(__file__).parent

# ── EDIT ME once you register a domain, then re-run this script ──────────────
DOMAIN = "https://arismobiledetailing.com"   # live custom domain — no trailing slash
# ────────────────────────────────────────────────────────────────────────────

BUSINESS = "Ari's Mobile Detailing"
PHONE = "+1-402-515-9157"
OG_IMAGE = f"{DOMAIN}/assets/img/hero-corvette.jpg"
INSTAGRAM = "https://www.instagram.com/aris_mobile_detailing/"
FACEBOOK = "https://www.facebook.com/p/Aris-Mobile-Detailing-100068821100332/"
CITIES = ["Omaha", "Bellevue", "Papillion", "La Vista", "Elkhorn",
          "Gretna", "Bennington", "Ralston", "Millard", "Yutan"]

REVIEWS = [
    ("Cody Buscher", "Our Explorer carries around 4 kids under the age of 7 on a daily basis and Ari makes it look like new every time he shows up. Always on time, great attitude and customer service and always has a smile on his face. Great pricing and outstanding work."),
    ("Gavrella Buscher", "If you need your car detailed, 10/10 recommend Ari's Mobile Detailing!! So convenient, didn't even have to leave our house! Reasonably priced and had it done fast!"),
    ("Meghan Mendick", "I have 3 kids, a dog, and a VERY HAIRY dog. Ari did such an amazing job getting all the food, hair, and smells out of everything!!!"),
    ("Taylor Spurgeon", "Absolutely amazing work!!!"),
]

# sitemap priority / changefreq by page
PRIORITY = {"index.html": ("1.0", "weekly"), "privacy.html": ("0.2", "yearly")}
DEFAULT_MAIN = ("0.8", "monthly")
AREA = ("0.7", "monthly")


def page_url(fname):
    # Cloudflare serves clean URLs (/packages, not /packages.html), so canonical
    # + sitemap URLs drop the .html to match the served, redirect-free address.
    if fname == "index.html":
        return DOMAIN + "/"
    return DOMAIN + "/" + fname[:-5]  # strip ".html"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def jsonld_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def local_business_jsonld():
    areas = ", ".join(f'{{"@type":"City","name":"{c}, NE"}}' for c in CITIES)
    reviews = ", ".join(
        '{{"@type":"Review","author":{{"@type":"Person","name":"{n}"}},'
        '"reviewRating":{{"@type":"Rating","ratingValue":"5","bestRating":"5"}},'
        '"reviewBody":"{b}"}}'.format(n=jsonld_escape(n), b=jsonld_escape(b))
        for n, b in REVIEWS
    )
    return (
        '<script type="application/ld+json" id="ld-business">'
        '{'
        '"@context":"https://schema.org","@type":"AutoWash",'
        f'"name":"{BUSINESS}",'
        f'"image":"{OG_IMAGE}",'
        f'"url":"{DOMAIN}/",'
        f'"telephone":"{PHONE}",'
        '"priceRange":"$$",'
        '"description":"Mobile auto detailing serving Omaha, NE and the metro. Interior & exterior detailing, ceramic coating, paint correction and maintenance plans, performed at your home or office.",'
        '"address":{"@type":"PostalAddress","addressLocality":"Omaha","addressRegion":"NE","addressCountry":"US"},'
        '"geo":{"@type":"GeoCoordinates","latitude":41.2565,"longitude":-95.9345},'
        f'"areaServed":[{areas}],'
        f'"sameAs":["{INSTAGRAM}","{FACEBOOK}"],'
        '"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"18:00"}],'
        '"aggregateRating":{"@type":"AggregateRating","ratingValue":"5.0","reviewCount":"4","bestRating":"5"},'
        f'"review":[{reviews}]'
        '}'
        '</script>'
    )


def seo_block(title, desc, url):
    # title/desc are extracted from <title>/<meta> which are ALREADY HTML-escaped,
    # so use them as-is (re-escaping would double-encode & -> &amp;amp;).
    t, d = title, desc
    return "\n".join([
        '<!-- SEO:start (managed by seo.py) -->',
        f'<link rel="canonical" href="{url}" />',
        '<meta name="robots" content="index, follow" />',
        '<meta name="theme-color" content="#0e1322" />',
        '<meta name="geo.region" content="US-NE" />',
        '<meta name="geo.placename" content="Omaha, Nebraska" />',
        '<meta name="ICBM" content="41.2565, -95.9345" />',
        '<meta property="og:type" content="website" />',
        '<meta property="og:site_name" content="Ari&#39;s Mobile Detailing" />',
        f'<meta property="og:title" content="{t}" />',
        f'<meta property="og:description" content="{d}" />',
        f'<meta property="og:url" content="{url}" />',
        f'<meta property="og:image" content="{OG_IMAGE}" />',
        '<meta name="twitter:card" content="summary_large_image" />',
        f'<meta name="twitter:title" content="{t}" />',
        f'<meta name="twitter:description" content="{d}" />',
        f'<meta name="twitter:image" content="{OG_IMAGE}" />',
        local_business_jsonld(),
        '<!-- SEO:end -->',
    ])


# lines/blocks we manage and must strip before re-inserting (idempotency)
STRIP_LINE = re.compile(
    r'^[ \t]*(<link[^>]+rel="canonical"[^>]*>|'
    r'<meta[^>]+(property="og:|name="twitter:|name="geo\.|name="ICBM"|name="theme-color"|name="robots")[^>]*>)[ \t]*\n',
    re.M)
STRIP_BLOCK = re.compile(r'[ \t]*<!-- SEO:start.*?<!-- SEO:end -->\n?', re.S)
STRIP_LD = re.compile(r'[ \t]*<script type="application/ld\+json" id="ld-business">.*?</script>\n?', re.S)


def process_page(fp):
    html = fp.read_text()
    # remove previously-managed tags
    html = STRIP_BLOCK.sub("", html)
    html = STRIP_LD.sub("", html)
    html = STRIP_LINE.sub("", html)

    title_m = re.search(r"<title>(.*?)</title>", html, re.S)
    desc_m = re.search(r'<meta name="description" content="(.*?)"\s*/?>', html, re.S)
    title = (title_m.group(1).strip() if title_m else BUSINESS)
    desc = (desc_m.group(1).strip() if desc_m else "")
    url = page_url(fp.name)

    block = seo_block(title, desc, url)
    html = html.replace("</head>", block + "\n</head>", 1)
    fp.write_text(html)
    return url


def build_sitemap(urls_by_file):
    today = datetime.date.today().isoformat()
    rows = []
    for fname, url in urls_by_file:
        if fname in PRIORITY:
            prio, freq = PRIORITY[fname]
        elif fname.startswith("detailing-") or fname == "areas.html":
            prio, freq = AREA
        else:
            prio, freq = DEFAULT_MAIN
        rows.append(
            f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>"
        )
    body = "\n".join(rows)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{body}\n</urlset>\n")
    (ROOT / "sitemap.xml").write_text(xml)


def build_robots():
    txt = ("User-agent: *\n"
           "Allow: /\n\n"
           f"Sitemap: {DOMAIN}/sitemap.xml\n")
    (ROOT / "robots.txt").write_text(txt)


def main():
    pages = sorted(p for p in ROOT.glob("*.html"))
    urls = []
    for fp in pages:
        url = process_page(fp)
        urls.append((fp.name, url))
        print(f"  SEO -> {fp.name}")
    build_sitemap(urls)
    build_robots()
    print(f"  sitemap.xml ({len(urls)} urls) + robots.txt written")
    print(f"  domain: {DOMAIN}")
    if "arismobiledetailing.com" in DOMAIN and DOMAIN.startswith("https://www.aris"):
        print("  NOTE: placeholder domain in use — edit DOMAIN in seo.py and re-run once registered.")


if __name__ == "__main__":
    main()
