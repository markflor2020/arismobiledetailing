# Ari's Mobile Detailing

Marketing website for Ari's Mobile Detailing (mobile auto detailing, Omaha, NE & metro).
Static HTML/CSS/JS — no build step.

## Run locally

```bash
python3 serve.py 8080
# then open http://localhost:8080
```

`serve.py` is a tiny no-cache dev server so edits show up without hard-refreshing.

## Structure

- `index.html` — home
- `services.html`, `packages.html`, `results.html`, `reviews.html`, `contact.html`
- `areas.html` + `detailing-<city>.html` — service-area pages (local SEO)
- `styles.css` — all styles (CSS variables at top)
- `script.js` — nav drawer, scroll reveals, before/after slider, quote form
- `assets/` — logo + photos
- `generate_areas.py` — regenerates the area pages and keeps the "Areas" nav/footer
  links in sync. Edit city blurbs there and re-run: `python3 generate_areas.py`
  (it runs `seo.py` automatically afterward).
- `seo.py` — injects canonical/OG/Twitter/geo meta + LocalBusiness JSON-LD into
  every page and writes `sitemap.xml` + `robots.txt`. Idempotent; re-run any time.
- `sitemap.xml`, `robots.txt` — generated; don't edit by hand.

## SEO

Run `python3 seo.py` after content changes (or just run `generate_areas.py`, which
calls it). It builds per-page Open Graph/Twitter tags, geo meta, a sitewide
`AutoWash` LocalBusiness schema (services, area served, hours, social links,
5.0 rating + the real reviews), plus the sitemap and robots files.

**⚠️ Domain:** `seo.py` uses a PLACEHOLDER domain
(`https://www.arismobiledetailing.com`). Once a real domain is registered, edit the
`DOMAIN` constant at the top of `seo.py` and re-run — that updates canonicals, OG
URLs, the schema, and the sitemap everywhere.

Off-site (do these too): set up / claim the **Google Business Profile**, and keep the
name + phone + city identical across the site, Google, and Facebook.

## Quote form

The contact form (`#qform`) emails Ari **and** offers a pre-filled text.
- Get a free access key at <https://web3forms.com> (enter Ari's email — submissions
  arrive there). Paste it into `WEB3FORMS_KEY` near the top of the form handler in
  `script.js`.
- Until a key is set, the form falls back to opening a pre-filled SMS to
  (402) 515-9157, so it works regardless.

## Brand

Navy `#333B60`, crimson `#BC1E2C`, silver `#B4B8C6`. Fonts: Clash Display + Switzer.

## Deploy

Push this folder's repo to GitHub and connect a host (Cloudflare Pages / Netlify /
GitHub Pages). Pushes auto-deploy. Keep edits local until approved, then push.

Contact: (402) 515-9157 · Instagram @aris_mobile_detailing
