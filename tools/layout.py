"""Shared page chrome for the Kyambogo Christian Union website."""
import os

SITE = "Kyambogo Christian Union"
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")

NAV = [
    ("About", "/about.html", [("Who We Are", "/about.html"), ("Our Story", "/history.html"), ("Leadership", "/leadership.html")]),
    ("Fellowship", "/fellowships.html", [("Campus Fellowship", "/fellowships.html"), ("Campus Worship", "/worship.html"), ("Fellowship Guide", "/structure.html")]),
    ("Ministry", "/discipleship.html", [("Discipleship", "/discipleship.html"), ("Evangelism", "/evangelism.html"), ("Prayer", "/prayer.html"), ("Worship", "/worship.html")]),
    ("Gatherings", "/lunch-hour.html", [("Weekly Gatherings", "/lunch-hour.html"), ("Campus Events", "/events.html"), ("Night Gatherings", "/night-of-redemption.html")]),
    ("News", "/news.html", []),
    ("Contact", "/contact.html", []),
]


def head(title, desc, path="/index.html"):
    full = title if title == SITE else f"{title} — {SITE}"
    canonical = ""
    if SITE_URL:
        slug = "" if path == "/index.html" else path[:-5]
        canonical = f'<link rel="canonical" href="{SITE_URL}{slug or "/"}">\n'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="/assets/img/kyu-st-kakumba-chapel.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#20242a">
{canonical}<link rel="icon" type="image/svg+xml" href="/assets/img/kyu-cu-mark.svg">
<link rel="apple-touch-icon" href="/assets/img/kyu-cu-mark.svg">
<link rel="preload" href="/assets/fonts/jost-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/source-sans-3-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body data-page="{path}">
"""


def header(active="/index.html"):
    desktop = []
    for label, href, kids in NAV:
        cls = " is-active" if href == active else ""
        if kids:
            links = "".join(f'<a href="{url}">{text}</a>' for text, url in kids)
            desktop.append(f'<div class="nav__item"><a class="nav__link nav__link--caret{cls}" href="{href}">{label}</a><div class="folder">{links}</div></div>')
        else:
            desktop.append(f'<div class="nav__item"><a class="nav__link{cls}" href="{href}">{label}</a></div>')
    desktop.append('<div class="nav__item"><a class="nav__link nav__cta" href="/contact.html">Get Connected</a></div>')
    mobile = []
    for label, href, kids in NAV:
        if kids:
            links = "".join(f'<li><a href="{url}">{text}</a></li>' for text, url in kids)
            mobile.append(f'<li><button class="mobile-nav__toggle" type="button">{label}</button><ul class="sub">{links}</ul></li>')
        else:
            mobile.append(f'<li><a href="{href}">{label}</a></li>')
    mobile.append('<li><a href="/contact.html">Get Connected</a></li>')
    return f"""<div class="announcement">New to Kyambogo? <a href="/contact.html">Start here and find out how to connect</a></div>
<header class="header"><div class="header__inner">
  <a class="brand" href="/index.html"><img class="brand__mark" src="/assets/img/kyu-cu-mark.svg" alt="" width="48" height="48"><span class="brand__text">Kyambogo<br>Christian Union</span></a>
  <nav class="nav" aria-label="Main navigation">{''.join(desktop)}</nav>
  <button class="burger" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
</div></header>
<div class="scrim"></div><nav class="mobile-nav" aria-label="Mobile navigation"><button class="mobile-nav__close" type="button" aria-label="Close menu">&times;</button><ul>{''.join(mobile)}</ul></nav>
"""


def banner(title, sub, desc, img, short=False, cue=False, actions="", pos="center center", anchor=None):
    cls = "banner banner--short" if short else "banner"
    aid = f' id="{anchor}"' if anchor else ""
    subhtml = f'<p class="banner__sub">{sub}</p>' if sub else ""
    deschtml = f'<div class="banner__desc">{desc}</div>' if desc else ""
    acthtml = f'<div class="banner__actions">{actions}</div>' if actions else ""
    cuehtml = '<a class="scroll-cue" href="#what-we-do-content">Scroll Down</a>' if cue else ""
    return f'''<section class="{cls}"{aid}><div class="banner__media" style="background-image:url('/assets/img/{img}');background-position:{pos}"></div><div class="banner__inner"><h1 class="banner__title">{title}</h1>{subhtml}{deschtml}{acthtml}</div>{cuehtml}</section>'''


def hero_slideshow(slides, cue=True):
    layers, texts = [], []
    for i, (img, title, sub, desc, label, href) in enumerate(slides):
        on = " is-active" if i == 0 else ""
        layers.append(f'<div class="hero__bg{on}" data-slide="{i}" style="background-image:url(\'/assets/img/{img}\')"></div>')
        subhtml = f'<p class="banner__sub">{sub}</p>' if sub else ""
        texts.append(f'<div class="hero__text{on}" data-slide="{i}"><h1 class="banner__title">{title}</h1>{subhtml}<div class="banner__desc">{desc}</div><div class="banner__actions"><a class="btn" href="{href}">{label}</a></div></div>')
    dots = "".join(f'<button class="hero__dot{" is-active" if i == 0 else ""}" type="button" data-goto="{i}" aria-label="Go to slide {i+1}"></button>' for i in range(len(slides)))
    cuehtml = '<a class="scroll-cue" href="#welcome">Scroll Down</a>' if cue else ""
    return f'<section class="banner hero" id="what-we-do" data-hero><div class="hero__stack">{"".join(layers)}</div><div class="hero__curtain"></div><div class="banner__inner hero__inner">{"".join(texts)}</div><div class="hero__dots">{dots}</div>{cuehtml}</section>'


def band(title, desc, img, tall=False, actions="", pos="center center", anchor_id=None):
    cls = "band band--tall" if tall else "band"
    aid = f' id="{anchor_id}"' if anchor_id else ""
    dh = f'<div class="band__desc">{desc}</div>' if desc else ""
    ah = f'<div class="band__actions">{actions}</div>' if actions else ""
    th = f'<h2 class="band__title">{title}</h2>' if title else ""
    return f'<section class="{cls}"{aid}><div class="band__bg" style="background-image:url(\'/assets/img/{img}\');background-position:{pos}"></div><div class="band__inner">{th}{dh}{ah}</div></section>'


def gallery(images, cols=3):
    cls = "gallery" if cols == 3 else f"gallery gallery--{cols}"
    figs = "".join(f'<figure><img src="/assets/img/{fn}" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>' for fn, cap in images)
    return f'<div class="{cls}">{figs}</div>'


def table(headers, rows, caption=None, num_cols=(), index=False, foot=None):
    cap = f"<caption>{caption}</caption>" if caption else ""
    th = ['<th class="idx" scope="col">No.</th>'] if index else []
    for i, value in enumerate(headers):
        cls = ' class="num"' if i in num_cols else ''
        th.append(f'<th scope="col"{cls}>{value}</th>')
    body = []
    for n, row in enumerate(rows, 1):
        tds = [f'<td class="idx">{n}</td>'] if index else []
        for i, value in enumerate(row):
            cls = ' class="num"' if i in num_cols else ''
            tds.append(f'<td{cls}>{value}</td>')
        body.append('<tr>' + ''.join(tds) + '</tr>')
    tf = ''
    if foot:
        cells = ['<td></td>'] if index else []
        for i, value in enumerate(foot):
            cls = ' class="num"' if i in num_cols else ''
            cells.append(f'<td{cls}>{value}</td>')
        tf = '<tfoot><tr>' + ''.join(cells) + '</tr></tfoot>'
    return f'<div class="table-wrap"><table class="data">{cap}<thead><tr>{"".join(th)}</tr></thead><tbody>{"".join(body)}</tbody>{tf}</table></div>'


def meta(items):
    return '<div class="meta-grid">' + ''.join(f'<div class="meta reveal"><span class="meta__n">{n}</span><span class="meta__l">{label}</span></div>' for n, label in items) + '</div>'


def quote(text, cite=None, plain=False):
    cls = "quote quote--plain" if plain else "quote"
    c = f"<cite>&mdash; {cite}</cite>" if cite else ""
    return f'<blockquote class="{cls}"><p>{text}</p>{c}</blockquote>'


def person(img, name, role, bio):
    return f'<article class="person reveal"><img class="person__photo" src="/assets/img/{img}" alt="{name}" loading="lazy"><h3 class="person__name">{name}</h3><p class="person__role">{role}</p><div class="person__bio">{"".join(f"<p>{p}</p>" for p in bio)}</div></article>'


def footer():
    import content as C
    return f'''<footer class="footer"><div class="wrapper"><div class="footer__grid">
  <div><div class="footer__brand"><img src="/assets/img/kyu-cu-mark-white.svg" alt="" width="42" height="42"><span>Kyambogo<br>Christian Union</span></div><p>{C.TAGLINE}</p><p>Kyambogo Hill, Kampala, Uganda</p></div>
  <div><h4>Explore</h4><ul><li><a href="/about.html">About the Union</a></li><li><a href="/fellowships.html">Fellowship</a></li><li><a href="/events.html">Events</a></li><li><a href="/news.html">News</a></li><li><a href="/sources.html">Sources &amp; photo credits</a></li></ul></div>
  <div><h4>Helpful links</h4><ul><li><a href="https://kyu.ac.ug/" target="_blank" rel="noopener">Kyambogo University</a></li><li><a href="https://ar.kyu.ac.ug/students-affairs/" target="_blank" rel="noopener">Student Affairs</a></li></ul><p><strong>University switchboard</strong><br><a href="tel:{C.PHONE.replace(' ', '')}">{C.PHONE}</a></p><p><a href="/contact.html">Ask about connecting with KYU-CU &rarr;</a></p></div>
</div><div class="footer__bottom"><span>&copy; <span data-year>2026</span> {C.NAME}</span><span>Campus information and photo credits are linked on this site.</span></div></div></footer>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer"><button class="lightbox__close" type="button" aria-label="Close">&times;</button><button class="lightbox__nav lightbox__prev" type="button" aria-label="Previous">&#8249;</button><img alt=""><button class="lightbox__nav lightbox__next" type="button" aria-label="Next">&#8250;</button><div class="lightbox__cap"></div></div>
<script src="/assets/js/site.js"></script></body></html>'''
