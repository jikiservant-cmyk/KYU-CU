#!/usr/bin/env python3
"""Generate the static KYU-CU website. Run: python3 tools/build.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import head, header, footer, banner, band, hero_slideshow, gallery, quote, table, meta, SITE, SITE_URL
import content as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = {}


def paras(items):
    return "".join(f"<p>{item}</p>" for item in items)


def ul(items):
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def cards(items):
    return '<div class="cards">' + "".join(f'<article class="card reveal"><h3>{title}</h3>{body}</article>' for title, body in items) + '</div>'


def page(name, title, desc, body):
    PAGES[name] = head(title, desc, "/" + name) + header("/" + name) + body + footer()


def standard(title, sub, desc, image, content, short=True):
    return banner(title, sub, desc, image, short=short) + f'<section class="section"><div class="wrapper">{content}</div></section>'


def build_home():
    body = [hero_slideshow(C.SLIDES)]
    body.append('''<nav class="index-nav" aria-label="Section navigation"><div class="index-nav__inner"><a href="#welcome">Welcome</a><a href="#story">Our Story</a><a href="#fellowship">Fellowship</a><a href="#worship">Campus Worship</a><a href="#connect">Connect</a></div></nav>''')
    body.append(f'''<section class="section" id="welcome"><div class="wrapper"><p class="section-heading center">Welcome to campus</p><h1 class="center" style="max-width:900px;margin:0 auto 30px">A place for faith, friendship and service.</h1><p class="lead center" style="max-width:780px;margin:0 auto 34px">{C.ABOUT_INTRO}</p>{quote(C.MISSION, "A simple invitation")}{paras(C.ABOUT_MORE)}<p class="center" style="margin-top:32px"><a class="btn btn--dark" href="/about.html">About KYU-CU</a></p></div></section>''')
    body.append(band("Find your place", "Start a conversation and ask about the current student fellowship schedule.", "kyu-chapel-community.jpg", anchor_id="fellowship"))
    fellowship_cards = [(title, ul(copy)) for title, copy in C.FELLOWSHIP_TYPES]
    body.append(f'''<section class="section section--alt"><div class="wrapper"><p class="section-heading center">Getting connected</p><h1 class="center">Fellowship at Kyambogo</h1><p class="lead center">{C.FELLOWSHIP_INTRO}</p>{cards(fellowship_cards)}<p class="center" style="margin-top:36px"><a class="btn btn--dark" href="/fellowships.html">Fellowship guide</a></p></div></section>''')
    body.append(banner("Our story", "Rooted in the Kyambogo campus community", "", "kyu-st-kakumba-chapel.jpg", short=True, anchor="story"))
    body.append(f'''<section class="section"><div class="wrapper"><h1 class="center">A growing university, a campus community</h1>{paras(C.HISTORY)}{meta(C.MILESTONES)}<p class="center" style="margin-top:32px"><a class="btn btn--dark" href="/history.html">Read our story</a></p></div></section>''')
    body.append(banner("Campus worship", "A diverse campus with places to worship", "", "kyu-chapel-archbishop.jpg", short=True, anchor="worship"))
    body.append(f'''<section class="section section--alt"><div class="wrapper"><h1 class="center">Explore worship on campus</h1><p class="lead center">{C.CHAPLAINCY}</p>{gallery([("kyu-st-kakumba-chapel.jpg", "St. Kakumba Chapel on the Kyambogo University campus"),("kyu-chapel-archbishop.jpg", "Archbishop Stephen Kaziimba at a St. Kakumba Chapel service, University report, December 2025"),("kyu-chapel-community.jpg", "University leaders and chapel community at a campus worship service, University report, December 2025")])}<p class="center" style="margin-top:30px"><a class="btn btn--dark" href="/worship.html">See campus worship information</a></p></div></section>''')
    body.append(band("A next step", "Ask the University how to connect with current KYU-CU student representatives.", "kyu-chapel-consecration.jpg", anchor_id="connect", actions='<a class="btn" href="/contact.html">Get Connected</a>'))
    body.append('''<section class="section section--dark center"><div class="wrapper"><h1>Come as you are</h1><p class="lead" style="max-width:680px;margin:0 auto 34px">Whether you are new to campus or looking for a Christian community, we can help you find the right place to ask.</p><a class="btn btn--solid" href="/contact.html">Start here</a></div></section>''')
    page("index.html", SITE, "Kyambogo Christian Union — faith, fellowship and service at Kyambogo University in Kampala, Uganda.", "".join(body))


def build_about():
    content = f'<h1>Who we are</h1><p class="lead">{C.ABOUT_INTRO}</p>{paras(C.ABOUT_MORE)}{quote(C.VISION, "Our hope")}{quote(C.BELIEF, "Our faith")}'
    content += '<h2>Values we seek to live by</h2>' + ul(C.VALUES)
    content += '<h2>What we can confirm</h2><p>This website is an independent introduction to Kyambogo Christian Union. Current Union meeting times, office holders, affiliation details and direct contact channels were not verifiable in the public sources we reviewed. We label campus chapel information and official University material separately to avoid confusion.</p>'
    content += gallery([("kyu-st-kakumba-chapel.jpg", "St. Kakumba Chapel, Kyambogo University"),("kyu-chapel-archbishop.jpg", "A St. Kakumba Chapel service reported by Kyambogo University in December 2025")])
    page("about.html", "About", "About Kyambogo Christian Union, a student faith community at Kyambogo University.", standard("About KYU-CU", "Faith, fellowship and service", C.TAGLINE, "kyu-chapel-community.jpg", content))


def build_history():
    content = '<h1>Our story</h1>' + paras(C.HISTORY) + meta(C.MILESTONES)
    content += quote("We welcome verified memories, documents and photographs from KYU-CU members and alumni.", "Help us tell the story")
    content += '<p>Kyambogo University was established in 2003 through the merger of Uganda Polytechnic Kyambogo, the Institute of Teacher Education Kyambogo and the Uganda National Institute of Special Education. This is University history, not a founding date for the Christian Union.</p>'
    content += '<p><a href="/sources.html">See the sources and evidence notes</a>.</p>'
    content += gallery([("kyu-st-kakumba-chapel.jpg", "St. Kakumba Chapel on the Kyambogo University campus"),("kyu-chapel-consecration.jpg", "Uganda Martyrs Chapel consecration, Kyambogo University, as reported in 2025")])
    page("history.html", "Our Story", "What we can verify about Kyambogo Christian Union and the wider Kyambogo University campus.", standard("Our Story", "The story continues", "Verified campus context and a careful note on what is not yet confirmed.", "kyu-st-kakumba-chapel.jpg", content))


def build_fellowships():
    entries = [(title, ul(copy)) for title, copy in C.FELLOWSHIP_TYPES]
    content = f'<h1>Find Christian fellowship</h1><p class="lead">{C.FELLOWSHIP_INTRO}</p>{cards(entries)}'
    content += '<h2>Before you visit</h2><p>Times and locations may change. Please confirm the schedule directly with the University or a current Union representative; the details listed above are from published University student information and are not a KYU-CU programme timetable.</p><p><a href="/contact.html">How to get connected &rarr;</a></p>'
    page("fellowships.html", "Fellowship", "A practical guide to finding Christian fellowship and campus worship at Kyambogo University.", standard("Fellowship", "Find your community", C.FELLOWSHIP_INTRO, "kyu-chapel-archbishop.jpg", content))


def build_ministry(slug, title, subtitle, image, copy, desc):
    content = '<h1>' + title + '</h1>' + paras(copy)
    content += '<h2>Find out what is happening now</h2><p>Ask a current KYU-CU representative or the University student support office which groups and activities are active this semester.</p><p><a href="/contact.html">Get connected &rarr;</a></p>'
    page(slug + ".html", title, desc, standard(title, subtitle, "", image, content))


def build_gatherings():
    rows = "".join(f'<article class="card reveal"><h3>{name}</h3><p><strong>{when}</strong> &middot; {time}</p><p>{desc}</p></article>' for name, when, time, desc in C.WEEKLY)
    content = '<h1>Gather with us</h1><p class="lead">No verified KYU-CU weekly schedule was publicly available when this site was prepared. Use this page as a prompt to check current University notices and ask the student support office.</p><div class="cards">' + rows + '</div>'
    content += '<h2>Campus worship information</h2><p>The University Academic Registrar lists Sunday services at St. Kakumba Chapel at 8:00 a.m., 9:30 a.m. and 10:00 a.m. These are chapel service times, not a confirmed Christian Union meeting schedule. Check the official student affairs page for current information.</p><p><a href="https://ar.kyu.ac.ug/students-affairs/" target="_blank" rel="noopener">Open University Student Affairs &rarr;</a></p>'
    page("lunch-hour.html", "Gatherings", "Check how to connect with current KYU-CU student gatherings and campus worship.", standard("Gatherings", "Stay in the loop", "Check current University notices and confirm details before visiting.", "kyu-chapel-archbishop.jpg", content))


def build_events():
    content = '<h1>Events and campus life</h1><p class="lead">This page does not list unconfirmed KYU-CU events. Contact a current representative or follow official University notices for dates, locations and access information.</p>'
    content += cards([(name, f'<p><strong>{place}</strong></p><p>{copy}</p>') for name, place, copy in C.EVENTS])
    content += '<p class="table-note">The photos on this website come from public University or news coverage and should not be read as photos of KYU-CU-organised events.</p>'
    page("events.html", "Events", "Find current event information and campus notices for Kyambogo Christian Union and worship communities.", standard("Campus Events", "What's on at Kyambogo", "Check current University notices for confirmed dates and details.", "kyu-chapel-community.jpg", content))


def build_night():
    content = '<h1>Community gatherings</h1><p class="lead">We found no reliable public listing for an event called “Night of Redemption” hosted by KYU-CU. This page is kept as a useful gathering guide, not as an announcement of a confirmed event.</p>'
    content += '<p>For current worship nights, prayer meetings, conferences or student fellowship events, ask the University or a verified Union representative. Do not rely on an old flyer or an unverified social account for time, location or payment details.</p>'
    content += '<p><a class="btn btn--dark" href="/contact.html">Ask about upcoming gatherings</a></p>'
    page("night-of-redemption.html", "Community Gatherings", "How to check for confirmed Christian student gatherings at Kyambogo University.", standard("Community Gatherings", "Come together", "Find current, verified event information before you go.", "kyu-chapel-consecration.jpg", content))


def build_leadership():
    content = '<h1>Leadership and service</h1><p class="lead">' + C.LEADERSHIP_INTRO + '</p>' + cards([(title, f'<p>{description}</p>') for title, description in C.DOCKETS])
    content += '<h2>Want to help update this page?</h2><p>Send a link to an official announcement or contact us with a verified leadership roster and the dates it applies to. We will not publish personal phone numbers without consent.</p><p><a href="/contact.html">Contact information &rarr;</a></p>'
    page("leadership.html", "Leadership", "Leadership information for Kyambogo Christian Union; current office holders are not listed without verification.", standard("Leadership", "Serving the campus community", "", "kyu-chapel-community.jpg", content))


def build_affiliations():
    content = '<h1>Campus and community links</h1><p class="lead">These links point to public University information and an external student ministry resource. They are not presented as confirmed organisational partners or as proof of KYU-CU affiliation.</p>'
    content += cards([(f'<a href="{title_url}" target="_blank" rel="noopener">{title}</a>', ul(copy)) for title, title_url, copy in C.AFFILIATIONS])
    content += '<h2>University places of worship</h2>' + paras([C.CHAPLAINCY])
    page("affiliations.html", "Campus Links", "Official campus information and external resources, with organisational affiliations clearly qualified.", standard("Campus Links", "Connected in community", "Official University links and helpful resources.", "kyu-st-kakumba-chapel.jpg", content))


def build_give():
    content = '<h1>Support the work</h1><p class="lead">' + C.GIVING_INTRO + '</p>' + ul(C.GIVING_USES)
    content += '<p>If a verified KYU-CU representative provides approved payment details, confirm the recipient and purpose directly through an official University or Union channel. This website has no payment form.</p>'
    page("give.html", "Giving", "Giving safely to Kyambogo Christian Union: no unverified payment details are published here.", standard("Giving", "Give with confidence", "Only use payment details confirmed through an official channel.", "kyu-chapel-community.jpg", content))


def build_news():
    posts = []
    for title, date, image, copy in C.POSTS:
        posts.append(f'<article class="post reveal"><img class="post__img" src="/assets/img/{image}" alt="{title}" loading="lazy"><p class="post__date">{date} · University News</p><h2 class="post__title">{title}</h2>{paras(copy)}</article>')
    content = '<h1>News and updates</h1><p class="lead">University and campus worship news, clearly distinguished from KYU-CU announcements.</p>' + ''.join(posts)
    page("news.html", "News", "Campus and chapel news relevant to Christian life at Kyambogo University, with sources identified.", standard("News", "From the campus community", "Official and sourced updates.", "kyu-chapel-archbishop.jpg", content))


def build_contact():
    content = f'''<div class="contact-grid"><div><h1>Get connected</h1><p class="lead">{C.CONTACT_INTRO}</p><p><strong>University:</strong><br><a href="{C.WEBSITE}" target="_blank" rel="noopener">Kyambogo University official website</a></p><p><strong>General switchboard:</strong><br><a href="tel:{C.PHONE.replace(' ', '')}">{C.PHONE}</a></p><p><strong>Academic Registrar's office email:</strong><br><a href="mailto:{C.EMAIL}">{C.EMAIL}</a><br><small>This is a general University contact, not a verified KYU-CU address.</small></p><p><strong>Campus:</strong><br>{C.LOCATION}</p><p><strong>Online:</strong><br><a href="{C.WEBSITE}" target="_blank" rel="noopener">kyu.ac.ug</a></p></div><div><h2>Plan a visit</h2>{ul(C.VISIT)}<h2>Suggested first step</h2><p>Contact the University and ask to be directed to the current Christian Union student representative or campus chaplaincy office. Confirm the meeting point and time before travelling.</p><a class="btn btn--dark" href="https://ar.kyu.ac.ug/students-affairs/" target="_blank" rel="noopener">Open Student Affairs</a></div></div>'''
    page("contact.html", "Contact", "How to connect with Kyambogo Christian Union using verified University contacts.", standard("Contact", "Start a conversation", "University contacts are general contacts, not a direct KYU-CU line.", "kyu-st-kakumba-chapel.jpg", content))


def build_structure():
    content = '<h1>A simple guide, not an official directory</h1><p class="lead">We have not found a published KYU-CU structure, chapter list or membership figures. Rather than invent them, this guide points you to confirmed University worship information and explains how to ask about the student Union.</p>'
    content += cards([(title, ul(copy)) for title, copy in C.FELLOWSHIP_TYPES])
    content += quote("For current fellowship contacts, meeting times and locations, please check directly with Kyambogo University.", "Please verify before visiting")
    content += '<p><a class="btn btn--dark" href="/contact.html">How to get connected</a></p>'
    page("structure.html", "Fellowship Guide", "A cautious campus worship and fellowship guide; no unverified KYU-CU structure or membership counts.", standard("Fellowship Guide", "A place to begin", "A transparent guide to what is publicly confirmed.", "kyu-chapel-archbishop.jpg", content))


def build_sources():
    rows = [(f'<a href="{url}" target="_blank" rel="noopener">{title}</a>', note) for title, url, note in C.SOURCES]
    content = '<h1>Sources and image credits</h1><p class="lead">We used public University and ministry sources to check campus facts. Where we could not confirm KYU-CU-specific information, we say so instead of guessing.</p>'
    content += table(["Source", "What it supports"], rows)
    content += '<h2>Photographs</h2><p>Images are from public University or news pages and illustrate campus chapels and services. They are not represented as KYU-CU gatherings or as photographs of Union members. Please contact the respective publisher about permission for reuse.</p>'
    content += table(["Image", "Source / caption"], [(f'<code>{name}</code>', source) for name, source in C.PHOTO_SOURCES.items()])
    content += '<h2>Corrections</h2><p>If you can provide official Union material, an approved contact, current meeting details or photo permissions, please share the source so this site can be updated accurately.</p>'
    page("sources.html", "Sources & Photo Credits", "Source notes, verified facts and image credits for the Kyambogo Christian Union website.", standard("Sources & Credits", "Clear, sourced information", "Help us keep this site accurate.", "kyu-chapel-community.jpg", content))


def build_404():
    content = '<h1>Let’s get you back on track</h1><p>The page may have moved, or the address may be incorrect.</p><div class="cards"><article class="card"><h3>About</h3><p>Learn what this site can confirm.</p><a href="/about.html">About KYU-CU &rarr;</a></article><article class="card"><h3>Fellowship</h3><p>Find verified campus worship information.</p><a href="/fellowships.html">Fellowship guide &rarr;</a></article><article class="card"><h3>Contact</h3><p>Ask the University how to connect.</p><a href="/contact.html">Get connected &rarr;</a></article></div>'
    page("404.html", "Page Not Found", "The requested page could not be found.", standard("Page Not Found", "404", "This page does not exist.", "kyu-st-kakumba-chapel.jpg", content))


def write_seo_files():
    urls = []
    for name in PAGES:
        if name == "404.html":
            continue
        loc = "/" if name == "index.html" else "/" + name[:-5]
        urls.append(f'  <url><loc>{SITE_URL}{loc}</loc><changefreq>monthly</changefreq><priority>{"1.0" if name == "index.html" else "0.7"}</priority></url>')
    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    if SITE_URL:
        sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(sitemap)
    elif os.path.exists(sitemap_path):
        os.remove(sitemap_path)
    robots = "User-agent: *\nAllow: /\nDisallow: /404.html\nDisallow: /tools/\n"
    if SITE_URL:
        robots += f"\nSitemap: {SITE_URL}/sitemap.xml\n"
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)


def main():
    build_home()
    build_about()
    build_history()
    build_fellowships()
    build_ministry("discipleship", "Discipleship", "Grow in faith together", "kyu-chapel-archbishop.jpg", C.DISCIPLESHIP, "Ways to explore Christian discipleship and fellowship at Kyambogo University.")
    build_ministry("evangelism", "Evangelism & Service", "Faith expressed with care", "kyu-chapel-community.jpg", C.EVANGELISM, "Information about Christian witness and service opportunities at Kyambogo University.")
    build_ministry("worship", "Campus Worship", "Places to worship at Kyambogo", "kyu-st-kakumba-chapel.jpg", C.WORSHIP, "University-published information about Christian places of worship at Kyambogo University.")
    build_ministry("prayer", "Prayer", "A place for prayer and pastoral support", "kyu-chapel-archbishop.jpg", C.PRAYER, "Find current prayer gatherings and pastoral support through Kyambogo University chaplaincies.")
    build_gatherings()
    build_night()
    build_events()
    build_leadership()
    build_affiliations()
    build_give()
    build_news()
    build_contact()
    build_structure()
    build_sources()
    build_404()
    for name, html in PAGES.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"{name:28} {len(html):>8,} bytes")
    write_seo_files()
    seo = "sitemap.xml and robots.txt" if SITE_URL else "robots.txt (set SITE_URL to generate sitemap.xml)"
    print(f"Generated {len(PAGES)} pages and {seo}")


if __name__ == "__main__":
    main()
