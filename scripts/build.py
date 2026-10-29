"""Rebuild the dependency-free GitHub Pages site: python3 scripts/build.py."""
import json
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'content.json').read_text())
PUBS = DATA['publications']
PUB = {p['id']: p for p in PUBS}
STREAMS = DATA['streams']
STREAM = {s['id']: s for s in STREAMS}
SITE = 'https://jiani19980225.github.io/'
ARROW = '<span class="arrow" aria-hidden="true">↗</span>'
NEW_TAB = '<span class="sr-only"> (opens in a new tab)</span>'

ICONS = {
    'scholar': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 3 1 9l11 6 9-4.91V17h2V9L12 3Z"/><path d="M5 13.18v3.6C5 18.6 8.13 20.5 12 20.5s7-1.9 7-3.72v-3.6L12 17l-7-3.82Z"/></svg>',
    'linkedin': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.75h4V21H3V9.75Zm6.5 0h3.83v1.54h.06c.53-1 1.84-2.06 3.79-2.06 4.05 0 4.8 2.67 4.8 6.13V21h-4v-4.98c0-1.19-.02-2.72-1.66-2.72-1.66 0-1.92 1.3-1.92 2.63V21h-4V9.75Z"/></svg>',
    'github': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5C5.65.5.5 5.65.5 12a11.5 11.5 0 0 0 7.86 10.92c.58.1.79-.25.79-.56v-2c-3.2.7-3.87-1.37-3.87-1.37-.53-1.33-1.28-1.69-1.28-1.69-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.68 0-1.26.45-2.28 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.83 1.19 3.09 0 4.41-2.69 5.39-5.25 5.67.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5Z"/></svg>',
    'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/></svg>',
    'file': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8l-5-5Z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg>',
    'sun': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4m0-14.2-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>',
    'copy': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2.5"/><path d="M5 15H4.5A1.5 1.5 0 0 1 3 13.5v-9A1.5 1.5 0 0 1 4.5 3h9A1.5 1.5 0 0 1 15 4.5V5"/></svg>',
}


def external(url, label, cls=''):
    return f'<a href="{e(url)}" class="{cls}" target="_blank" rel="noopener noreferrer">{label}{NEW_TAB}</a>'


def arrow_link(url, label):
    return f'<a class="link-arrow" href="{e(url)}">{label} {ARROW}</a>'


def eyebrow(text, num=''):
    return f'<p class="eyebrow">{f"<span class=num>{num}</span>" if num else ""}{text}</p>'


def profile_buttons(cv=True):
    buttons = [
        external(DATA['scholar'], f'{ICONS["scholar"]}Google Scholar', 'btn btn-primary'),
        external(DATA['linkedin'], f'{ICONS["linkedin"]}LinkedIn', 'btn btn-soft'),
        external(DATA['github'], f'{ICONS["github"]}GitHub', 'btn btn-soft'),
        f'<a class="btn btn-soft" href="mailto:{DATA["email"]}">{ICONS["mail"]}Email</a>',
    ]
    if cv:
        buttons.append(f'<a class="btn btn-gold" href="assets/Jiani_He_CV.pdf" download>{ICONS["file"]}CV (PDF)</a>')
    return f'<div class="profile-links">{"".join(buttons)}</div>'


def header(current):
    links = [('index.html', 'Home', 'home'), ('research.html', 'Research', 'research'),
             ('publications.html', 'Publications', 'publications'), ('experience.html', 'Experience', 'experience'),
             ('index.html#verto-mind', 'Verto Mind', 'verto'), ('cv.html', 'CV', 'cv')]
    nav = ''.join(f'<a href="{url}"' + (' aria-current="page"' if key == current else '') + f'>{label}</a>' for url, label, key in links)
    tools = (external(DATA['scholar'], ICONS['scholar'] + '<span class="sr-only">Google Scholar</span>', 'icon-btn')
             + external(DATA['linkedin'], ICONS['linkedin'] + '<span class="sr-only">LinkedIn</span>', 'icon-btn'))
    return f'''<a class="skip" href="#main-content">Skip to main content</a>
<header class="site-header"><div class="wrap header-inner">
<a class="wordmark" href="index.html" aria-label="Jiani (Elva) He — home"><span class="monogram" aria-hidden="true">JH</span><span class="brand-name">Jiani (Elva) He<span class="brand-sub">Data science · Operations research · Applied AI</span></span></a>
<nav class="primary-nav" id="primary-navigation" aria-label="Primary">{nav}</nav>
<div class="header-tools">{tools}<button class="icon-btn theme-toggle" aria-label="Switch to dark theme" aria-pressed="false">{ICONS['sun']}</button><button class="icon-btn menu-toggle" aria-expanded="false" aria-controls="primary-navigation" aria-label="Open menu"><span class="bars" aria-hidden="true"></span></button></div>
</div></header>'''


def footer():
    links = (external(DATA['scholar'], f'{ICONS["scholar"]}Google Scholar')
             + external(DATA['linkedin'], f'{ICONS["linkedin"]}LinkedIn')
             + external(DATA['github'], f'{ICONS["github"]}GitHub')
             + f'<a href="assets/Jiani_He_CV.pdf" download>{ICONS["file"]}CV (PDF)</a>')
    return f'''<footer class="site-footer" id="contact"><div class="wrap"><div class="footer-card"><div><p class="footer-title">Let’s connect.</p><p class="footer-description">Open to research collaboration and conversations about supply-chain analytics, operations research, and thoughtful AI products.</p><a class="footer-email" href="mailto:{DATA['email']}">{ICONS['mail']}{DATA['email']}</a></div><nav class="footer-links" aria-label="Profiles">{links}</nav></div><div class="footer-bottom"><span>© 2026 {DATA['name']} · {DATA['location']}</span><span>Updated {DATA['updated']} · <a href="#main-content">Back to top ↑</a></span></div></div></footer>'''


def page(filename, title, description, body, current='', extra=''):
    canonical = SITE + ('' if filename == 'index.html' else filename)
    full_title = f'{title} | {DATA["name"]}' if title else f'{DATA["name"]} — Data Science, Research & Applied AI'
    person = {'@context': 'https://schema.org', '@type': 'Person', 'name': DATA['name'], 'url': SITE,
              'email': 'mailto:' + DATA['email'], 'jobTitle': 'Data Science Consultant',
              'worksFor': {'@type': 'Organization', 'name': 'Accenture'},
              'address': {'@type': 'PostalAddress', 'addressLocality': 'Seattle', 'addressRegion': 'WA'},
              'sameAs': [DATA['scholar'], DATA['linkedin'], DATA['github']],
              'knowsAbout': ['Demand forecasting', 'Operations research', 'Causal decision support',
                             'Reverse logistics', 'Supply-chain analytics', 'Applied AI'],
              'alumniOf': [{'@type': 'CollegeOrUniversity', 'name': 'Massachusetts Institute of Technology'},
                           {'@type': 'CollegeOrUniversity', 'name': 'Purdue University'}]}
    html = f'''<!doctype html>
<html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(full_title)}</title><meta name="description" content="{e(description)}"><meta name="author" content="{DATA['name']}"><meta name="theme-color" content="#EBF5FD"><link rel="canonical" href="{canonical}"><meta property="og:type" content="profile"><meta property="og:site_name" content="{DATA['name']}"><meta property="og:title" content="{e(full_title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{SITE}assets/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="assets/apple-touch-icon.png"><script>document.documentElement.classList.remove('no-js');try{{const t=localStorage.getItem('jiani-theme');if(t==='dark'||t==='light')document.documentElement.dataset.theme=t;}}catch(_){{}}</script><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&amp;display=swap"><link rel="stylesheet" href="assets/styles.css"><script src="assets/site.js" defer></script><script type="application/ld+json">{json.dumps(person)}</script></head><body>{header(current)}<main id="main-content" tabindex="-1">{body}</main>{footer()}{extra}</body></html>
'''
    (ROOT / filename).write_text(html)


# ---------- shared fragments ----------

def authors_html(p):
    return ', '.join(f'<strong class="me">{e(a)}</strong>' if a == 'Jiani He' else e(a) for a in p['authors'])


def badges(p, code=True):
    out = '<span class="badge badge-first">★ First author</span>' if p['first_author'] else ''
    kind = 'review' if p['group'] == 'review' else 'accepted'
    out += f'<span class="badge badge-{kind}">{e(p["status"])}</span>'
    if code and p['code']:
        out += '<span class="badge badge-code">Open code</span>'
    return f'<div class="badges">{out}</div>'


def pub_title(p, href=None):
    href = href or p['url']
    if not href:
        return e(p['title'])
    if href.startswith('http'):
        return external(href, e(p['title']))
    return f'<a href="{href}">{e(p["title"])}</a>'


def pub_links(p, cite=True):
    links = []
    if p['url']:
        label = 'SSRN preprint' if 'ssrn' in p['url'] else 'arXiv preprint'
        links.append(external(p['url'], f'{label} {ARROW}', 'primary'))
    if p['doi']:
        links.append(external('https://doi.org/' + p['doi'], f'DOI {ARROW}'))
    if p['code']:
        links.append(external(p['code'], f'{ICONS["github"]}Code {ARROW}'))
    if cite and p['bibtex']:
        links.append(f'<button class="cite-button" data-cite="{p["id"]}" aria-label="Cite {e(p["title"])}">Cite · BibTeX</button>')
    return f'<div class="pub-links">{"".join(links)}</div>' if links else ''


def citation_extra(pubs):
    citations = json.dumps({p['id']: p['bibtex'] for p in pubs if p['bibtex']}).replace('<', '\\u003c')
    return f'''<dialog class="citation-dialog" aria-labelledby="citation-title"><div class="dialog-top"><h2 id="citation-title">BibTeX citation</h2><button class="dialog-close" autofocus>Close</button></div><pre tabindex="0"></pre><button class="btn btn-primary copy-citation">{ICONS['copy']}Copy citation</button><p class="copy-status" role="status"></p></dialog><script type="application/json" id="citation-data">{citations}</script>'''


def stream_count(sid):
    n = sum(1 for p in PUBS if p['stream'] == sid)
    return f'{n} paper' + ('' if n == 1 else 's')


def experience_items():
    items = []
    for x in DATA['experience']:
        context = f'<p class="xp-context">{e(x["context"])}</p>' if x['context'] else ''
        bullets = ''.join(f'<li>{e(b)}</li>' for b in x['bullets'])
        items.append(f'''<article class="card xp"><p class="xp-when"><strong>{e(x['dates'])}</strong><br>{e(x['place'])}</p><div><h3>{e(x['org'])}</h3><p class="xp-role">{e(x['role'])}</p>{context}<ul class="xp-list">{bullets}</ul></div></article>''')
    return f'<div class="xp-stack">{"".join(items)}</div>'


def education_items():
    items = ''.join(f'''<article class="card edu"><p class="edu-when">{e(x['date'])} · {e(x['place'])}</p><h3>{e(x['school'])}</h3><p class="edu-degree">{e(x['degree'])}</p><p class="edu-gpa">{e(x['gpa'])}</p><p class="edu-detail">{e(x['detail'])}</p></article>''' for x in DATA['education'])
    return f'<div class="edu-grid">{items}</div>'


def skills_grid():
    groups = ''.join(f'<div class="skill-group"><h3>{e(s["area"])}</h3><div class="chips">{"".join(f"<span class=chip>{e(i)}</span>" for i in s["items"])}</div></div>' for s in DATA['skills'])
    return f'<div class="skills-grid">{groups}</div>'


def stats_band():
    cards = ''.join(f'<div class="stat"><span class="stat-value">{e(s["value"])}</span><span class="stat-label">{e(s["label"])}</span></div>' for s in DATA['stats'])
    return f'<section class="band band-navy band-stats" aria-label="Achievements at a glance"><div class="wrap stats">{cards}</div></section>'


# ---------- pages ----------

def home():
    if DATA['photo']:
        avatar = f'<img src="{e(DATA["photo"])}" width="148" height="148" alt="Portrait of {DATA["name"]}">'
    else:
        avatar = '<span aria-hidden="true">JH</span>'
    profile_card = f'''<aside class="profile-card" aria-label="Profile summary"><div class="avatar"><div class="avatar-inner">{avatar}</div></div><p class="profile-name">{DATA['name']}</p><p class="profile-role">Data Science Consultant, Accenture<br>{DATA['location']}</p><ul class="facts"><li><span>Research</span><strong>Forecasting · Causal decision support · Reverse logistics</strong></li><li><span>Education</span><strong>MIT, MS Business Analytics<br>Purdue, BS Industrial Engineering</strong></li><li><span>Service</span><strong>Peer reviewer, 10+ journal manuscripts</strong></li></ul></aside>'''
    highlights = ''.join(f'<li>{h}</li>' for h in DATA['highlights'])
    streams = ''.join(f'''<article class="card stream"><span class="stream-num">{i:02d}</span><p class="stream-label">{e(s['label'])}</p><h3>{e(s['question'])}</h3><div class="chips">{"".join(f"<span class=chip>{e(k)}</span>" for k in s['problems'][:3])}</div><a class="link-arrow" href="research.html#{s['id']}">{stream_count(s['id'])} {ARROW}</a></article>''' for i, s in enumerate(STREAMS, 1))
    selected = ''.join(f'''<article class="card pub-row"><div>{badges(p)}<h3>{pub_title(p, 'publications.html#' + p['id'])}</h3><p class="authors">{authors_html(p)}</p></div>{pub_links(p, cite=False)}</article>''' for p in (PUB['ssads'], PUB['dacri'], PUB['forecasting'], PUB['planning']))
    role = f'<p class="verto-role">{e(DATA["verto_role"])}</p>' if DATA['verto_role'] else ''
    body = f'''<section class="band band-hero" aria-labelledby="home-title"><div class="wrap hero"><div class="hero-copy"><p class="kicker"><span class="dot" aria-hidden="true"></span>Data scientist · Independent researcher</p><h1 id="home-title">Jiani He <span class="alt">(Elva)</span></h1><p class="hero-statement">I study how evidence becomes <em>better operational decisions</em>, from demand forecasting to supply-chain intervention and AI-assisted reverse logistics.</p><p class="hero-affil">Data Science Consultant at <strong>Accenture</strong> · MS, <strong>MIT</strong> · BS, <strong>Purdue</strong></p>{profile_buttons()}</div>{profile_card}</div></section>
{stats_band()}
<section class="band" id="about" aria-label="About"><div class="wrap brief"><div class="card bio-card">{eyebrow('Short bio', '01')}<h2>In brief.</h2><p id="bio-text" class="bio">{e(DATA['bio'])}</p><div class="bio-actions"><button class="btn btn-soft copy-bio" data-copy="#bio-text">{ICONS['copy']}Copy bio</button><p class="copy-status bio-status" role="status"></p></div></div><div class="card highlight-card">{eyebrow('Highlights', '02')}<h2>Selected achievements.</h2><ul class="highlights">{highlights}</ul></div></div></section>
<section class="band band-sky" aria-labelledby="focus-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Research program', '03')}<h2 id="focus-title">Evidence for operational decisions.</h2><p class="section-lead">Three connected questions about when analytics and AI actually improve the decisions organizations make.</p></div>{arrow_link('research.html', 'Explore the research program')}</div><div class="streams">{streams}</div></div></section>
<section class="band" aria-labelledby="selected-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Selected publications', '04')}<h2 id="selected-title">Recent papers.</h2></div>{arrow_link('publications.html', f'All {len(PUBS)} papers')}</div><div class="pub-list">{selected}</div></div></section>
<section class="band band-champagne" id="verto-mind" aria-labelledby="verto-title"><div class="wrap verto"><div class="verto-copy">{eyebrow('Building beyond research', '05')}<h2 id="verto-title">Verto Mind</h2>{role}<p class="verto-lead">A little space.<br>A different perspective.</p><p>An AI-powered cognitive-reframing app that guides people from a stressful thought toward a more balanced perspective, ending with a personalized Verto Card to revisit.</p><ol class="verto-steps"><li><strong>Name the thought.</strong> Begin with a specific worry.</li><li><strong>Explore a new perspective.</strong> A structured, AI-assisted reframing process.</li><li><strong>Keep the insight.</strong> Reveal a personalized Verto Card.</li></ol><div class="verto-actions">{external(DATA['testflight'], 'Join the TestFlight beta ' + ARROW, 'btn btn-primary')}<span class="beta-note">iOS · TestFlight beta</span></div></div><figure class="phone-figure"><div class="phone" aria-hidden="true"><div class="phone-screen"><span class="phone-notch"></span><span class="phone-brand">Verto Mind</span><span class="phone-card"><i></i><i></i><i></i><i></i></span><span class="phone-cta">POUR IT OUT</span><span class="phone-tabbar"><i></i><i></i><i></i></span></div></div><figcaption>Illustration in the Verto Mind palette</figcaption></figure></div></section>'''
    page('index.html', '', 'Jiani (Elva) He is a Seattle-based data scientist and independent researcher working on demand forecasting, causal decision support, and AI-assisted reverse logistics. Data Science Consultant at Accenture; MIT and Purdue alumna.', body)


def research():
    pmap = ''.join(f'<li><span class="qnum">Q{i:02d}</span><div><p>{e(s["question"])}</p><small>{e(s["name"])}</small></div></li>' for i, s in enumerate(STREAMS, 1))
    ledger = []
    for i, s in enumerate(STREAMS, 1):
        reps = ''.join(f'<li><a href="publications.html#{p["id"]}">{e(p["title"])}</a><span>{"First author · " if p["first_author"] else ""}{e(p["status"])}</span></li>' for p in PUBS if p['stream'] == s['id'])
        chips = ''.join(f'<span class="chip">{e(k)}</span>' for k in s['problems'])
        ledger.append(f'''<article class="card question" id="{s['id']}"><header><p class="qlabel">Question {i:02d}</p><h3>{e(s['question'])}</h3><p class="qstream">{e(s['name'])}</p></header><dl class="q-rows"><div><dt>Motivation</dt><dd>{e(s['motivation'])}</dd></div><div><dt>Origin in practice</dt><dd>{e(s['practice'])}</dd></div><div><dt>Representative problems</dt><dd><div class="chips">{chips}</div></dd></div><div><dt>Research</dt><dd><ul class="rep-list">{reps}</ul></dd></div></dl></article>''')
    journey = [
        ('01', 'Purdue University · 2020', 'Engineering foundations', 'Industrial engineering supplied a language for systems, constraints, and trade-offs. LSTM forecasting models and reinforcement learning for sensor placement were a first experience of research.'),
        ('02', 'MIT · 2021', 'Analytical expansion', 'At the Operations Research Center: robust optimization, interpretable classification, and an NLP admissions pipeline for AdmitHub. A BMW Group capstone modeled demand and cross-price elasticity for dynamic vehicle pricing.'),
        ('03', 'Accenture · 2021–present', 'Questions from practice', 'Five years in forward and reverse logistics for a technology client kept raising the same problems: unstable demand signals, inventory imbalances, and asset-recovery decisions made under uncertainty.'),
        ('04', 'Independent research · 2026', 'A connected program', f'{len(PUBS)} papers with collaborators on forecast stability, causal intervention ranking, trustworthy AI deployment, and AI-assisted reverse logistics, including a first-author paper.'),
    ]
    steps = ''.join(f'<li class="card step"><span class="step-num">{n}</span><p class="step-when">{w}</p><h3>{t}</h3><p>{d}</p></li>' for n, w, t, d in journey)
    methods = ['Machine learning & forecasting', 'Causal inference', 'Robust optimization', 'NLP & LLM systems', 'Synthetic benchmarks with ground truth', 'Decision & value analysis']
    body = f'''<section class="band band-hero"><div class="wrap program-hero"><div class="program-copy">{eyebrow('Research program', '01')}<p class="program-name">Evidence for Operational Decisions</p><h1>When does better evidence lead to better decisions?</h1><div class="program-thesis"><p>My research begins with questions that keep recurring in operations: forecasts that are accurate but unstable, disruptions that are detected but not resolved, and returned assets whose condition is uncertain.</p><p>I don’t judge models only by their predictive accuracy. I evaluate them by the decisions they change. That means paying attention to constraints, costs, delays, partial information, and whether people can trust and review the evidence behind an action.</p></div><div class="hero-buttons">{external(DATA['scholar'], ICONS['scholar'] + 'Google Scholar', 'btn btn-primary')}<a class="btn btn-soft" href="publications.html">All publications</a></div></div><figure class="card program-map"><figcaption>{eyebrow('One program, three questions')}</figcaption><ol class="map-list">{pmap}</ol><div class="map-converge"><strong>Operational decisions</strong><span>Models judged by the decisions they change</span></div></figure></div></section>
<section class="band" aria-labelledby="streams-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Research streams', '02')}<h2 id="streams-title">Three connected questions.</h2><p class="section-lead">Each stream starts from a problem met in practice and asks what evidence a better decision needs.</p></div></div><div class="ledger">{''.join(ledger)}</div></div></section>
<section class="band band-sky" aria-labelledby="journey-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Research journey', '03')}<h2 id="journey-title">From engineering to operational decision research.</h2></div>{arrow_link('experience.html', 'Experience & education')}</div><ol class="journey">{steps}</ol></div></section>
<section class="band band-navy" aria-labelledby="methods-title"><div class="wrap cta-band"><div>{eyebrow('Methods', '04')}<h2 id="methods-title">Methods in service of the question.</h2><div class="chips chips-lg">{''.join(f"<span class=chip>{e(m)}</span>" for m in methods)}</div></div><div class="cta-actions"><a class="btn btn-primary" href="publications.html">Read the papers {ARROW}</a>{external(DATA['scholar'], 'Google Scholar ' + ARROW, 'btn btn-soft')}</div></div></section>'''
    page('research.html', 'Research', 'Research program of Jiani (Elva) He: when better evidence leads to better operational decisions — forecasting and planning value, causal decision support and trustworthy AI, and AI-assisted reverse logistics.', body, 'research')


def publications():
    filters = [('all', 'All')] + [(s['id'], s['label']) for s in STREAMS]
    filter_html = ''.join(f'<button class="filter-button" data-filter="{k}" aria-pressed="{str(k == "all").lower()}">{e(label)}</button>' for k, label in filters)
    groups, n = [], 0
    for g in DATA['groups']:
        cards = []
        for p in (p for p in PUBS if p['group'] == g['id']):
            n += 1
            meta = f'<div><dt>Venue</dt><dd>{e(p["venue"])}</dd></div><div><dt>Public record</dt><dd>{e(p["record"])}</dd></div><div><dt>Research stream</dt><dd><a href="research.html#{p["stream"]}">{e(STREAM[p["stream"]]["name"])}</a></dd></div>'
            cards.append(f'''<article class="card pub" id="{p['id']}" data-stream="{p['stream']}"><div class="pub-index"><span class="pub-num">{n:02d}</span><span class="pub-year">{p['year']}</span></div><div class="pub-body">{badges(p)}<h3>{pub_title(p)}</h3><p class="authors">{authors_html(p)}</p><p class="pub-summary">{e(p['summary'])}</p><dl class="pub-meta">{meta}</dl>{pub_links(p)}</div></article>''')
        count = len(cards)
        groups.append(f'''<section class="pub-group" aria-labelledby="group-{g['id']}"><div class="group-head"><div>{eyebrow(g['eyebrow'])}<h2 id="group-{g['id']}">{e(g['title'])}</h2></div><span class="group-count">{count} paper{'' if count == 1 else 's'}</span></div><div class="pub-stack">{''.join(cards)}</div></section>''')
    accepted = sum(1 for p in PUBS if p['group'] in ('first', 'accepted'))
    coded = sum(1 for p in PUBS if p['code'])
    summary = f'<ul class="summary-chips"><li><strong>{len(PUBS)}</strong> papers</li><li><strong>{accepted}</strong> accepted at conferences</li><li><strong>1</strong> first-author</li><li><strong>{coded}</strong> with open code</li></ul>'
    body = f'''<section class="band band-hero"><div class="wrap page-hero">{eyebrow('Publications', '01')}<h1>Publications &amp; preprints.</h1><p class="lead">Papers with collaborators on demand forecasting, causal decision support, trustworthy AI deployment, and AI-assisted reverse logistics. My name is underlined in each author list.</p>{summary}<div class="hero-buttons">{external(DATA['scholar'], ICONS['scholar'] + 'Google Scholar profile', 'btn btn-primary')}<a class="btn btn-soft" href="research.html">How the papers connect</a></div></div></section>
<section class="band band-flush" aria-label="Papers"><div class="wrap"><div class="filter-bar" role="group" aria-label="Filter by research stream">{filter_html}<span class="count" aria-live="polite">{len(PUBS)} papers</span></div>{''.join(groups)}<p class="small-note">Last checked {DATA['updated']}. Conference labels describe acceptance or presentation and do not imply that final proceedings have been published. arXiv and SSRN links point to public preprints; one accepted manuscript is not yet publicly available.</p><aside class="card service-note">{eyebrow('Academic service')}<h2>Peer review.</h2><p>Peer reviewer for more than ten journal manuscripts across operations, analytics, and applied AI.</p></aside></div></section>'''
    page('publications.html', 'Publications', f'Publications and preprints by Jiani (Elva) He: {len(PUBS)} papers on demand forecasting, causal decision support, LLM deployment assurance, and reverse logistics, with code and BibTeX.', body, 'publications', citation_extra(PUBS))


def experience():
    service = [('10+', 'Journal manuscripts peer-reviewed', 'Reviews across operations, analytics, and applied AI.'),
               ('5', 'Junior analysts mentored', 'SQL, business problem solving, and client communication across both Accenture roles.'),
               ('AI', 'Enablement lead', 'Standardized prompts and analytical queries for enterprise LLM assistants; wrote reusable guides and trained analysts.')]
    service_html = ''.join(f'<article class="card service-card"><span class="stat-value">{v}</span><h3>{t}</h3><p>{d}</p></article>' for v, t, d in service)
    body = f'''<section class="band band-hero"><div class="wrap page-hero">{eyebrow('Experience & education', '01')}<h1>Where analysis meets operations.</h1><p class="lead">From industrial engineering to business analytics and five years of data science consulting, my work turns complex operational questions into analyses people can use.</p>{profile_buttons()}</div></section>
<section class="band" aria-labelledby="practice-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Professional experience', '02')}<h2 id="practice-title">Experience.</h2></div>{arrow_link('cv.html', 'Full CV')}</div>{experience_items()}</div></section>
<section class="band band-sky" aria-labelledby="education-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Education', '03')}<h2 id="education-title">An engineering lens, an analytics toolkit.</h2></div></div>{education_items()}</div></section>
<section class="band band-navy" aria-labelledby="service-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Service & leadership', '04')}<h2 id="service-title">Giving back.</h2></div></div><div class="service-grid">{service_html}</div></div></section>
<section class="band" aria-labelledby="skills-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Skills', '05')}<h2 id="skills-title">Tools for the question at hand.</h2></div></div>{skills_grid()}</div></section>'''
    page('experience.html', 'Experience & Education', 'Jiani (Elva) He: Data Science Consultant at Accenture, BMW Group dynamic-pricing capstone, MIT MS in Business Analytics (Operations Research Center), and Purdue BS in Industrial Engineering.', body, 'experience')


def cv():
    def cv_pub(p):
        authors = ', '.join(f'<strong>{e(a)}</strong>' if a == 'Jiani He' else e(a) for a in p['authors'])
        link = f' <a href="{e(p["url"])}">{e(p["record"])}</a>.' if p['url'] else f' {e(p["record"])}.'
        return f'<li>{authors}. {p["year"]}. “{e(p["title"])}.” <em>{e(p["venue"])}</em>.{link} <span class="cv-status">{e(p["status"])}</span></li>'
    pub_sections = ''.join(f'<h3 class="cv-sub">{e(g["title"])}</h3><ol class="cv-pubs">{"".join(cv_pub(p) for p in PUBS if p["group"] == g["id"])}</ol>' for g in DATA['groups'])
    xp = ''.join(f'''<div class="cv-entry"><div class="cv-row"><strong>{e(x['org'])}</strong><span>{e(x['dates'])}</span></div><div class="cv-row cv-meta"><em>{e(x['role'])}</em><span>{e(x['place'])}</span></div><ul>{"".join(f"<li>{e(b)}</li>" for b in x['bullets'])}</ul></div>''' for x in DATA['experience'])
    edu = ''.join(f'''<div class="cv-entry"><div class="cv-row"><strong>{e(x['school'])}</strong><span>{e(x['date'])}</span></div><div class="cv-row cv-meta"><em>{e(x['degree'])} · {e(x['gpa'])}</em><span>{e(x['place'])}</span></div><p>{e(x['detail'])}</p></div>''' for x in DATA['education'])
    skills = ''.join(f'<p><strong>{e(s["area"])}:</strong> {e(", ".join(s["items"]))}</p>' for s in DATA['skills'])
    body = f'''<section class="band band-hero cv-hero"><div class="wrap page-hero">{eyebrow('Curriculum vitae', '01')}<h1>Curriculum vitae.</h1><p class="lead">A web version of my CV, kept in sync with the publication list on this site.</p><div class="hero-buttons"><a class="btn btn-primary" href="assets/Jiani_He_CV.pdf" download>{ICONS['file']}Download PDF</a><button class="btn btn-soft print-button">Print this page</button></div></div></section>
<section class="band band-flush" aria-label="CV document"><div class="wrap"><article class="card cv-doc"><header class="cv-head"><h2>{DATA['name']}</h2><p>{DATA['headline']}</p><p>{DATA['location']} · <a href="mailto:{DATA['email']}">{DATA['email']}</a> · <a href="{SITE}">jiani19980225.github.io</a> · <a href="{e(DATA['linkedin'])}">LinkedIn</a> · <a href="{e(DATA['scholar'])}">Google Scholar</a></p></header>
<section class="cv-section"><h2>Research interests</h2><p>Demand-forecast stability and planning value · Causal decision support under partial information · Trustworthy deployment of AI systems · AI-assisted reverse logistics</p></section>
<section class="cv-section"><h2>Professional experience</h2>{xp}</section>
<section class="cv-section"><h2>Education</h2>{edu}</section>
<section class="cv-section"><h2>Research &amp; publications</h2>{pub_sections}</section>
<section class="cv-section"><h2>Service &amp; mentoring</h2><ul><li>Peer reviewer for 10+ journal manuscripts.</li><li>Mentored five junior analysts across Accenture roles; led onboarding and team training, including AI-assisted analysis.</li></ul></section>
<section class="cv-section"><h2>Skills</h2>{skills}</section>
</article><p class="small-note">Updated {DATA['updated']}. For the latest papers, see my <a href="{e(DATA['scholar'])}">Google Scholar profile</a>.</p></div></section>'''
    page('cv.html', 'Curriculum Vitae', 'Curriculum vitae of Jiani (Elva) He: professional experience, education, publications, service, and skills. Download the PDF or print this page.', body, 'cv')


home()
research()
publications()
experience()
cv()
page('404.html', 'Page not found', 'Find research, publications, and contact information for Jiani (Elva) He.', f'<section class="band band-hero"><div class="wrap page-hero">{eyebrow("404 · Page not found")}<h1>Let’s find the right page.</h1><p class="lead">This address isn’t available. Try one of these instead.</p><div class="hero-buttons"><a class="btn btn-primary" href="index.html">Home</a><a class="btn btn-soft" href="research.html">Research</a><a class="btn btn-soft" href="publications.html">Publications</a></div></div></section>')
pages = ['', 'research.html', 'publications.html', 'experience.html', 'cv.html']
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{SITE}{f}</loc></url>' for f in pages) + '</urlset>\n')
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
print(f'Built {len(pages)} pages, 404 page, sitemap, and robots.txt.')
