#!/usr/bin/env python3
"""Build checkcartax.com static site. Usage: python3 build.py  (writes HTML into repo root)."""
import json, os, html, datetime, pathlib, sys, re
sys.path.insert(0, "src")
from content import PAGES

BASE = "https://checkcartax.com"
LASTMOD = os.environ.get("LASTMOD", datetime.date.today().isoformat())
GA_ID = os.environ.get("GA_ID", "")            # live site had no GA/GTM IDs; set to enable (loaded after page load)
GSC = os.environ.get("GSC_VERIFICATION", "")    # Google Search Console HTML-tag token, optional
ROOT = pathlib.Path(__file__).parent
CHECK_URL = "https://secure.checkmot.com/mot/search"
esc = html.escape

CSS = open(ROOT / "src/style.css").read()
JS = """document.querySelectorAll('form.plate').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();var r=f.reg.value.toUpperCase().replace(/\\s+/g,'');if(!r){f.reg.focus();return}location.href='https://secure.checkmot.com/mot/search?id=checkmotv2&reg='+encodeURIComponent(r)})});"""
GA = f"""<script>window.addEventListener('load',function(){{var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id={GA_ID}';document.head.appendChild(s)}});window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA_ID}');</script>""" if GA_ID else ""

NAV = [("/check-car-tax", "Check car tax"), ("/how-much-is-my-car-tax", "Tax rates"), ("/check-van-tax", "Van tax"), ("/car-tax-info", "Guide")]
FOOT_GUIDES = [("car-tax-check-northern-ireland", "Car Tax Check Northern Ireland"), ("car-tax-price-check", "Car Tax Price Check"),
 ("check-car-road-tax", "Check Car Road Tax"), ("check-car-tax", "Check Car Tax"), ("check-car-tax-online", "Check Car Tax Online"),
 ("check-my-car-road-tax", "Check My Car Road Tax"), ("check-tax-on-car", "Check Tax On Car"), ("check-van-tax", "Check Van Tax"),
 ("how-much-is-my-car-tax", "How Much Is My Car Tax"), ("car-tax-info", "Car Tax Info"), ("free-car-tax-check/", "Free Car Tax Check")]
FOOT_ABOUT = [("about", "About Us"), ("contact", "Contact Us"), ("terms-and-conditions", "Terms & Conditions"), ("privacy-policy", "Privacy Policy"), ("cookie-policy", "Cookie Policy")]

def plate(i, label="Enter a registration number"):
    return f"""<form class="plate" action="{CHECK_URL}" method="get" role="search">
<input type="hidden" name="id" value="checkmotv2"><label for="reg{i}" class="sr">{label}</label>
<div class="pl"><span class="gb" aria-hidden="true">UK</span><input id="reg{i}" name="reg" type="text" placeholder="ENTER REG" autocomplete="off" autocapitalize="characters" spellcheck="false" maxlength="10" required></div>
<button type="submit">Check tax</button></form>"""

ORG = {"@type": "Organization", "@id": BASE + "/#org", "name": "Check Car Tax", "legalName": "Outbound BPO Ltd", "url": BASE + "/",
       "logo": BASE + "/assets/cct-logo.svg", "email": "support@checkcartax.com",
       "sameAs": ["https://www.facebook.com/MOTCheckUK/", "https://www.instagram.com/checkmotinsta/", "https://twitter.com/MotCheckUK"]}

def ldjson(p, url):
    g = [ORG, {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "Check Car Tax", "publisher": {"@id": BASE + "/#org"}, "inLanguage": "en-GB"}]
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"}]
    if p["path"]:
        crumbs.append({"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url})
    g.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
    if p["faqs"]:
        g.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

def links(items):
    return "".join(f'<li><a href="/{h}">{esc(t)}</a></li>' for h, t in items)

def head(title, desc, url, ld="", robots=""):
    return f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">{'<link rel="canonical" href="'+url+'">' if url else ''}{robots}
{('<meta name="google-site-verification" content="'+esc(GSC)+'">') if GSC else ''}
<meta property="og:type" content="website"><meta property="og:site_name" content="Check Car Tax"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">{'<meta property="og:url" content="'+url+'">' if url else ''}<meta property="og:image" content="{BASE}/assets/hero-960.webp"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#4B8EFF"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32x32.png"><link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16x16.png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png"><link rel="mask-icon" href="/assets/safari-pinned-tab.svg" color="#4B8EFF"><link rel="manifest" href="/site.webmanifest">
<style>{CSS}</style>{'<script type="application/ld+json">'+ld+'</script>' if ld else ''}{GA}</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="w"><a href="/" class="logo"><img src="/assets/cct-logo.svg" alt="Check Car Tax" width="144" height="45"></a>
<nav aria-label="Main"><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)}</ul></nav></div></header>"""

def foot():
    return f"""<footer class="foot"><div class="w"><div class="cta"><p class="h">Check a vehicle's tax status now</p>{plate('f', 'Registration number')}</div>
<div class="cols"><div><p class="h">Car tax guides</p><ul>{links(FOOT_GUIDES)}</ul></div>
<div><p class="h">About</p><ul>{links(FOOT_ABOUT)}</ul></div>
<div><p class="h">Contact</p><p><a href="mailto:support@checkcartax.com">support@checkcartax.com</a></p><ul class="soc"><li><a href="https://www.facebook.com/MOTCheckUK/" rel="noopener">Facebook</a></li><li><a href="https://www.instagram.com/checkmotinsta/" rel="noopener">Instagram</a></li><li><a href="https://twitter.com/MotCheckUK" rel="noopener">Twitter</a></li></ul></div></div>
<p class="small">© {datetime.date.today().year} Outbound BPO Limited. Registered in England and Wales, company number 05940797, 1 Primrose Street, London EC2A 2EX. CheckCarTax.com is not affiliated with DVLA or GOV.UK.</p></div></footer>
<script>{JS}</script></body></html>"""

def render(p):
    url = BASE + "/" + p["path"]
    body = p["body"]
    if body.startswith("LEGAL:"):
        body = open(ROOT / f"src/legal/{body[6:]}.html").read()
    hero_img = """<picture><img src="/assets/hero-480.webp" srcset="/assets/hero-480.webp 480w, /assets/hero-960.webp 960w" sizes="(min-width:900px) 460px, 92vw" width="480" height="193" alt="Car tax check illustration" fetchpriority="high"></picture>""" if p["kind"] == "home" else ""
    crumb = "" if not p["path"] else f'<nav class="bc" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">{esc(p["crumb"])}</li></ol></nav>'
    intro = f'<p class="lead">{esc(p["intro"])}</p>' if p["intro"] else ""
    steps = """<section class="steps w"><h2>How it works</h2><ol><li><img src="/assets/step-one.svg" alt="" width="56" height="57" loading="lazy"><h3>Enter the reg</h3><p>Type the vehicle's number plate into the yellow box.</p></li><li><img src="/assets/step-two.svg" alt="" width="56" height="57" loading="lazy"><h3>Search</h3><p>Press Check tax. Spaces and lower case are fine.</p></li><li><img src="/assets/step-three.svg" alt="" width="56" height="57" loading="lazy"><h3>View results</h3><p>See the vehicle's current tax and MOT status.</p></li></ol></section>""" if p["kind"] == "home" else ""
    faq = ""
    if p["faqs"]:
        faq = '<section class="faq"><h2>Frequently asked questions</h2>' + "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in p["faqs"]) + "</section>"
    return (head(p["title"], p["desc"], url, ldjson(p, url)) +
        f"""<main id="main"><section class="hero{' home' if hero_img else ''}"><div class="w">{crumb}<div class="hg"><div><h1>{esc(p['h1'])}</h1>{intro}{plate(0)}</div>{hero_img}</div></div></section>
{steps}<article class="w prose">{body}{faq}</article></main>""" + foot())

def relativize(doc, depth):
    """Make site-internal URLs relative so pages work both at / and under a github.io project path."""
    pre = "../" * depth or "./"
    doc = re.sub(r'(href|src)="/(?!/)', lambda m: f'{m.group(1)}="{pre}', doc)
    doc = re.sub(r'(srcset="|, )/assets/', lambda m: m.group(1) + pre + "assets/", doc)
    return doc.replace(f'href="{pre}"', f'href="{pre}"')

def main():
    errs = []
    titles, descs, h1s = set(), set(), set()
    for p in PAGES:
        if len(p["title"]) >= 60: errs.append(f"title too long ({len(p['title'])}): {p['title']}")
        if len(p["desc"]) >= 155: errs.append(f"desc too long ({len(p['desc'])}): {p['path']}")
        for s, v in ((titles, p["title"]), (descs, p["desc"]), (h1s, p["h1"])):
            if v in s: errs.append("duplicate: " + v)
            s.add(v)
        out = ROOT / ("index.html" if p["path"] == "" else (p["path"] + "index.html" if p["path"].endswith("/") else p["path"] + ".html"))
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(relativize(render(p), p["path"].count("/")))
    if errs: sys.exit("\n".join(errs))
    nf = head("Page not found | Check Car Tax", "Sorry, we couldn't find that page. Check a vehicle's tax status or browse our UK car tax guides.", "", "", '<meta name="robots" content="noindex">')
    nf += f"""<main id="main"><section class="hero"><div class="w"><h1>Page not found</h1><p class="lead">Sorry, that page doesn't exist or has moved. You can still check a vehicle's tax below, or go to the <a href="/">homepage</a>.</p>{plate(0)}</div></section>
<article class="w prose"><h2>Popular pages</h2><ul>{links(FOOT_GUIDES[:9])}</ul></article></main>""" + foot()
    (ROOT / "404.html").write_text(nf)
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"<url><loc>{BASE}/{p['path']}</loc><lastmod>{LASTMOD}</lastmod></url>\n" for p in PAGES) + "</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sm)
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    (ROOT / "site.webmanifest").write_text(json.dumps({"name": "Check Car Tax", "short_name": "CheckCarTax", "icons": [{"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"}], "theme_color": "#4B8EFF", "background_color": "#ffffff", "display": "standalone", "start_url": "/"}))
    (ROOT / ".nojekyll").write_text("")
    print(f"built {len(PAGES)} pages + 404, lastmod {LASTMOD}")

if __name__ == "__main__":
    main()
