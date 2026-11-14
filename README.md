# Kyambogo Christian Union (KYU-CU)

A responsive, multi-page website for Kyambogo Christian Union, adapted from the design and static-site structure of [MUK-CU](https://github.com/jikiservant-cmyk/MUK-CU). The navigation, page patterns, slideshow, mobile menu, image gallery, and locally hosted fonts have been retained; the copy, branding, colour palette, and photography have been replaced for Kyambogo.

## Run locally

```bash
npm start
# or: node server.js
```

The server listens on `0.0.0.0:3000` (or the `PORT` environment variable), which works with the Arena live preview. No dependency install is needed.

Regenerate the static pages and SEO files with:

```bash
npm run build
# or: python3 tools/build.py
SITE_URL=https://your-domain.example python3 tools/build.py
```

The editable copy lives in `tools/content.py`; shared layout and navigation are in `tools/layout.py`; page generation is in `tools/build.py`. `robots.txt` is always generated; `sitemap.xml` is only generated when `SITE_URL` is supplied, so it never contains invalid relative URLs. Generated pages can also be hosted on any static host.

## Pages

Home · About · Our Story · Fellowship · Discipleship · Evangelism & Service · Campus Worship · Prayer · Gatherings · Community Gatherings · Events · Leadership · Campus Links · Giving · News · Contact · Fellowship Guide · Sources & Photo Credits · 404.

## Research and accuracy

There is limited, current, publicly verifiable information about the Christian Union itself. I did **not** find a reliable KYU-CU official website or public source confirming its founding date, leadership roster, direct email/phone/social accounts, current fellowship timetable, chapter list, payment details, or affiliation. Those details are intentionally not invented. The “History,” “Leadership,” “Giving,” “Gatherings,” and “Fellowship Guide” pages explain these limits and direct visitors to confirm current information with Kyambogo University.

Verified campus context used on the site:

- Kyambogo University Student Affairs lists campus places of worship, including St. Kakumba Chapel, Uganda Martyrs Chaplaincy, the SDA Chapel, and the University Mosque; published schedules are labelled as campus worship information, **not** as a KYU-CU programme.
- Kyambogo University's official chapel report covers a St. Kakumba Chapel service on 30 November 2025, published on 18 December 2025. It is University news, not a KYU-CU event announcement.
- The general University switchboard and Academic Registrar's email shown on Contact are public University contacts, not direct Christian Union contacts.
- FOCUS-Uganda is shown only as an external resource. KYU-CU's current affiliation has not been verified.

The relevant links and page-level notes are available at `/sources.html`. Key sources:

- [Kyambogo University Academic Registrar — Student Affairs / Places of Worship](https://ar.kyu.ac.ug/students-affairs/)
- [Kyambogo University — official 2022 recruitment notice with institutional background](https://kyu.ac.ug/vacancy-announcement-external-advert-no-1-2022/)
- [Kyambogo University — St. Kakumba Chapel worship report](https://kyu.ac.ug/god-with-us-archbishop-kaziimba-preaches-reconciliation-and-renewal-at-kyambogo-university/)
- [FOCUS-Uganda](https://focusuganda.org/) (resource only; affiliation unverified)

## Photography and branding

All photos are Kyambogo campus chapel or worship context obtained from the University website and news coverage; they are **not** presented as photographs of KYU-CU members or Union-hosted events. Per-file source and context notes are in `tools/kyu_image_sources.json`, and visible image credits are on `/sources.html`. Source attribution is not the same as a reuse licence: please confirm permission from each publisher before public/commercial deployment. The small KYU-CU emblem in `assets/img/kyu-cu-mark*.svg` is an original site mark, not an official University or Union logo.

## Before launch

- Confirm the Union's preferred name, official mark, current leadership and direct contact channel.
- Add the current timetable, meeting venue and active fellowship/chapter details only after confirmation.
- Confirm any official FOCUS-Uganda affiliation before describing it as a partner.
- Obtain photo reuse permissions or replace the current campus-context images with photographs supplied by KYU-CU.
- Confirm approved giving methods before publishing any payment details.
