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
             ('philosophy.html', 'Philosophy', 'philosophy'), ('cv.html', 'CV', 'cv')]
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
    return f'''<footer class="site-footer" id="contact"><div class="wrap"><div class="footer-card"><div><p class="footer-title">Let’s connect.</p><p class="footer-description">Open to research collaboration and conversations about supply-chain analytics, operations research, and trustworthy applied AI.</p><a class="footer-email" href="mailto:{DATA['email']}">{ICONS['mail']}{DATA['email']}</a></div><nav class="footer-links" aria-label="Profiles">{links}</nav></div><div class="footer-bottom"><span>© 2026 {DATA['name']} · {DATA['location']}</span><span>Updated {DATA['updated']} · <a href="#main-content">Back to top ↑</a></span></div></div></footer>'''


def page(filename, title, description, body, current='', extra=''):
    canonical = SITE + ('' if filename == 'index.html' else filename)
    full_title = f'{title} | {DATA["name"]}' if title else f'{DATA["name"]} — Data Science, Research & Applied AI'
    person = {'@context': 'https://schema.org', '@type': 'Person', 'name': DATA['name'], 'url': SITE,
              'email': 'mailto:' + DATA['email'], 'jobTitle': 'Data Science Consultant',
              'worksFor': {'@type': 'Organization', 'name': 'Accenture'},
              'address': {'@type': 'PostalAddress', 'addressLocality': 'Seattle', 'addressRegion': 'WA'},
              'sameAs': [DATA['scholar'], DATA['linkedin'], DATA['github']],
              **({'image': SITE + DATA['photo']} if DATA['photo'] else {}),
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
    names = []
    for a in p['authors']:
        name = e(a) + ('*' if a in p['equal'] else '')
        names.append(f'<strong class="me">{name}</strong>' if a == 'Jiani He' else name)
    note = ' <span class="equal-note">*Equal contribution</span>' if p['equal'] else ''
    return ', '.join(names) + note


def badges(p):
    out = '<span class="badge badge-first">★ First author</span>' if p['first_author'] else ''
    if p['co_first']:
        out += '<span class="badge badge-first">★ Co-first author</span>'
    kind = 'review' if p['group'] == 'review' else 'accepted'
    out += f'<span class="badge badge-{kind}">{e(p["status"])}</span>'
    if p['proceedings']:
        out += f'<span class="badge badge-note">{e(p["proceedings"])}</span>'
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


def paper_links(ids):
    return ''.join(f'<a href="publications.html#{i}">{e(PUB[i]["short"])}</a>' for i in ids)


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
    portrait = f'<img src="{e(DATA["photo"])}" width="640" height="800" alt="Portrait of {DATA["name"]}">' if DATA['photo'] else '<span class="portrait-mono" aria-hidden="true">JH</span>'
    mission = e(DATA['mission']).replace('go to waste', '<em>go to waste</em>')
    creds = ''.join(f'<li>{e(c)}</li>' for c in DATA['credentials'])
    directions = ''.join(f'''<article class="card direction"><span class="direction-num">{i:02d}</span><p class="direction-label">{e(s['label'])}</p><h3>{e(s['title'])}</h3><p>{e(s['short'])}</p><a class="link-arrow" href="research.html#{s['id']}">{stream_count(s['id'])} {ARROW}</a></article>''' for i, s in enumerate(STREAMS, 1))
    cet_chips = ''.join(f'<span class="chip">{e(r["area"])}</span>' for r in DATA['importance']['cet_rows'])
    cet_strip = f'<div class="cet-strip"><div><p class="cet-strip-label">National priorities · U.S. Critical and Emerging Technologies List (2026)</p><div class="chips">{cet_chips}</div></div>{arrow_link("research.html#cet", "How the work aligns")}</div>'
    signature = ''.join(f'''<article class="card signature">{badges(p)}<h3>{pub_title(p, 'publications.html#' + p['id'])}</h3><p class="signature-text">{e(p['summary'])}</p><p class="authors">{authors_html(p)}</p>{pub_links(p, cite=False)}</article>''' for p in PUBS if p['group'] == 'first')
    beyond = ''.join(f'<li>{e(b)}</li>' for b in DATA['beyond'])
    body = f'''<section class="band band-hero" aria-labelledby="home-title"><div class="wrap hero"><div class="hero-copy"><p class="kicker"><span class="dot" aria-hidden="true"></span>Data scientist · Operations researcher · Seattle</p><h1 id="home-title">Jiani He <span class="alt">(Elva)</span></h1><p class="hero-mission">{mission}</p><p class="hero-sub">{e(DATA['positioning'])}</p>{profile_buttons()}</div><figure class="portrait">{portrait}</figure></div><div class="wrap"><ul class="credentials" aria-label="Education and experience">{creds}</ul></div></section>
{stats_band()}
<section class="band" aria-labelledby="work-title"><div class="wrap"><div class="section-head"><div>{eyebrow('What I work on', '01')}<h2 id="work-title">Three decisions I help get right.</h2></div>{arrow_link('research.html', 'Research')}</div><div class="directions">{directions}</div>{cet_strip}</div></section>
<section class="band band-sky" aria-labelledby="signature-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Signature work', '02')}<h2 id="signature-title">Lead-author papers.</h2></div>{arrow_link('publications.html', f'All {len(PUBS)} papers')}</div><div class="signatures">{signature}</div></div></section>
<section class="band band-champagne" aria-labelledby="beyond-title"><div class="wrap beyond"><div>{eyebrow('Beyond the work', '03')}<h2 id="beyond-title">The person behind the papers.</h2>{arrow_link('philosophy.html', 'Read my stories')}</div><ul class="beyond-list">{beyond}</ul></div></section>
<section class="band" aria-labelledby="kit-title"><div class="wrap"><div class="card kit"><div class="kit-copy"><h2 id="kit-title">Short bio &amp; CV</h2><p>A brief professional introduction and a downloadable CV.</p></div><div class="kit-actions"><button class="btn btn-primary copy-bio" data-copy="#bio-text">{ICONS['copy']}Copy short bio</button><a class="btn btn-soft" href="assets/Jiani_He_CV.pdf" download>{ICONS['file']}CV (PDF)</a><p class="copy-status bio-status" role="status"></p></div><details class="kit-bio"><summary>Read the short bio</summary><p id="bio-text">{e(DATA['bio'])}</p></details></div></div></section>'''
    page('index.html', '', 'Jiani (Elva) He researches AI-assisted reverse logistics and resource recovery, with industry experience in data center supply chains. Explore research, publications, and the ideas behind the work.', body)


def research():
    rh = DATA['research_hero']
    ledger = []
    paper_labels = {
        'ssads': 'Inspection and recovery from return notes',
        'dacri': 'DACRI: ranking supply-chain interventions',
        'planning': 'Testing the value of a planning addition',
        'late-delivery': 'Early warning from weak delivery signals',
        'forecasting': 'Accuracy and forecast-path stability',
        'routing': 'Evidence for LLM-routing deployment',
    }
    for i, s in enumerate(STREAMS, 1):
        reps = ''.join(f'<li><a href="publications.html#{p["id"]}" title="{e(p["title"])}">{e(paper_labels[p["id"]])}</a><span>{"First author · " if p["first_author"] else "Co-first author · " if p["co_first"] else ""}{e(p["status"])}</span></li>' for p in PUBS if p['stream'] == s['id'])
        ledger.append(f'''<article class="card question" id="{s['id']}"><header><p class="qlabel">Direction {i:02d} · {e(s['label'])}</p><h3>{e(s['title'])}</h3><p class="qstream">{e(s['short'])}</p></header><dl class="q-rows"><div><dt>The question</dt><dd>{e(s['motivation'])}</dd></div><div><dt>Industry context</dt><dd>{e(s['practice'])}</dd></div><div><dt>Research setting</dt><dd>{e(s['evidence'])}</dd></div><div><dt>Related papers</dt><dd><ul class="rep-list">{reps}</ul></dd></div></dl></article>''')
    featured = next(p for p in PUBS if p['id'] == 'ssads')
    f = DATA['research_feature']
    contribution = f'<div class="study-contribution"><h3>My contribution</h3><p>{e(f["contribution"])}</p></div>' if f['contribution'] else ''
    study = f'''<section class="band band-flush" id="featured-study" aria-labelledby="study-title"><div class="wrap"><article class="card featured-study"><div class="study-heading">{eyebrow('A closer look', '02')}<p class="study-role">First &amp; corresponding author · AIBThings 2026</p><h2 id="study-title">{e(f['title'])}</h2></div><div class="study-copy"><p class="study-intro">{e(f['intro'])}</p><ol class="study-path" aria-label="Simplified SSADS pipeline"><li><span>01</span><strong>Read the note</strong><small>Condition + signal quality</small></li><li><span>02</span><strong>Allocate inspection</strong><small>Shared labor budget</small></li><li><span>03</span><strong>Choose recovery</strong><small>Expected value + capacity</small></li></ol>{contribution}<div class="study-finding"><h3>What we found</h3><p>{e(f['finding'])}</p></div><details class="study-evidence"><summary>Scope &amp; limits of the evaluation</summary><p>{e(f['boundary'])}</p></details><div class="pub-links">{external(featured['url'], 'Read the paper ' + ARROW, 'primary')}{external(featured['code'], ICONS['github'] + 'Code & benchmark ' + ARROW)}<a href="publications.html#ssads">Full publication record</a></div></div></article></div></section>'''
    imp = DATA['importance']
    cet_rows = ''.join(f'<div><dt><span class="cet-tag">{e(r["kind"])}</span>{e(r["area"])}</dt><dd><p>{e(r["detail"])}</p>{paper_links(r["papers"])}</dd></div>' for r in imp['cet_rows'])
    sources = ''.join(f'<li>{external(s["url"], e(s["label"]) + " " + ARROW)}</li>' for s in imp['sources'])
    implementation = DATA['research_implementation']
    factors = ''.join(f'<div class="practice-factor"><h3>{e(x["title"])}</h3><p>{e(x["text"])}</p></div>' for x in implementation['factors'])
    body = f'''<section class="band band-hero"><div class="wrap page-hero">{eyebrow('Research', '01')}<h1>{e(rh['title'])}</h1><p class="lead">{e(rh['lead'])}</p><p class="research-scope">{e(rh['scope'])}</p><div class="hero-buttons"><a class="btn btn-primary" href="#featured-study">Start with one study</a><a class="btn btn-soft" href="publications.html">All publications</a>{external(DATA['scholar'], ICONS['scholar'] + 'Google Scholar', 'btn btn-soft')}</div></div></section>
{study}
<section class="band" aria-labelledby="directions-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Research directions', '03')}<h2 id="directions-title">The questions connecting the papers.</h2></div></div><div class="ledger">{''.join(ledger)}</div></div></section>
<section class="band band-sky research-context" aria-labelledby="context-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Putting ideas to work', '04')}<h2 id="context-title">{e(implementation['title'])}</h2><p class="section-lead">{e(implementation['intro'])}</p></div></div><div class="practice-grid">{factors}</div><div class="practice-goal"><p>{e(implementation['goal'])}</p><p>{e(implementation['invitation'])}</p>{arrow_link('mailto:' + DATA['email'] + '?subject=Reverse-logistics%20implementation', 'Discuss an implementation question')}</div><p class="small-note">External industry context: {external(implementation['industry_source'], 'Microsoft’s circular datacenter hardware white paper ' + ARROW)} discusses component value, limited supply alternatives, testing, and internal reuse.</p><details class="card policy-details" id="cet"><summary>U.S. technology priorities: context &amp; sources</summary><div class="cet"><div class="cet-head"><h3>Alignment with the U.S. Critical and Emerging Technologies List</h3><p>{e(imp['cet_intro'])}</p><p>{e(imp['policy'])}</p><ul class="cet-sources">{sources}</ul></div><dl class="cet-map">{cet_rows}</dl><p class="cet-note">{e(imp['cet_note'])}</p></div></details></div></section>
<section class="band band-champagne" aria-labelledby="human-title"><div class="wrap research-personal"><div>{eyebrow('Beyond the model', '05')}<h2 id="human-title">Why I keep returning to this.</h2></div><div><p>I want fewer useful things to go to waste. That belief is why I chose operations research, and it is the mission behind my interest in reverse logistics.</p><p>I care about long-term thinking: knowing what a project serves, and what belief will sustain the effort.</p>{arrow_link('philosophy.html', 'More about what shapes me')}</div></div></section>'''
    page('research.html', 'Research', 'Research by Jiani (Elva) He: forecasting, causal decision support, AI deployment assurance, and reverse logistics. Explore representative studies, evaluation settings, and findings.', body, 'research')


def publications():
    groups, n = [], 0
    for g in DATA['groups']:
        cards = []
        for p in (p for p in PUBS if p['group'] == g['id']):
            n += 1
            meta = f'<div><dt>Venue</dt><dd>{e(p["venue"])}</dd></div><div><dt>Public record</dt><dd>{e(p["record"])}</dd></div>'
            cards.append(f'''<article class="card pub" id="{p['id']}" data-stream="{p['stream']}"><div class="pub-index"><span class="pub-num">{n:02d}</span><span class="pub-year">{p['year']}</span></div><div class="pub-body">{badges(p)}<h3>{pub_title(p)}</h3><p class="authors">{authors_html(p)}</p><p class="pub-summary">{e(p['summary'])}</p><dl class="pub-meta">{meta}</dl>{pub_links(p)}</div></article>''')
        count = len(cards)
        if not count:
            continue
        groups.append(f'''<section class="pub-group" aria-labelledby="group-{g['id']}"><div class="group-head"><div>{eyebrow(g['eyebrow'])}<h2 id="group-{g['id']}">{e(g['title'])}</h2></div><span class="group-count">{count} paper{'' if count == 1 else 's'}</span></div><div class="pub-stack">{''.join(cards)}</div></section>''')
    body = f'''<section class="band band-hero"><div class="wrap page-hero">{eyebrow('Publications', '01')}<h1>Publications &amp; preprints.</h1><p class="lead">{sum(p['group'] in ('first', 'accepted') for p in PUBS)} papers accepted at international conferences in 2026, {sum(p['group'] == 'first' for p in PUBS)} as lead author. My name is underlined in each author list.</p><div class="hero-buttons">{external(DATA['scholar'], ICONS['scholar'] + 'Google Scholar profile', 'btn btn-primary')}<a class="btn btn-soft" href="research.html">How the papers connect</a></div></div></section>
<section class="band band-flush" aria-label="Papers"><div class="wrap">{''.join(groups)}<p class="small-note">Last checked {DATA['updated']}. Accepted papers were accepted at international conferences that have already taken place; their proceedings are forthcoming. arXiv and SSRN links point to public preprints; one accepted paper is awaiting posting on SSRN.</p></div></section>'''
    page('publications.html', 'Publications', f'Publications and preprints by Jiani (Elva) He: {len(PUBS)} papers on demand forecasting, causal decision support, LLM deployment assurance, and reverse logistics, with code and BibTeX.', body, 'publications', citation_extra(PUBS))


def experience():
    service = [('10+', 'Journal manuscripts peer-reviewed', 'Reviews across operations, analytics, and applied AI.'),
               ('5', 'Junior analysts mentored', 'SQL, business problem solving, and client communication across both Accenture roles.')]
    service_html = ''.join(f'<article class="card service-card"><span class="stat-value">{v}</span><h3>{t}</h3><p>{d}</p></article>' for v, t, d in service)
    body = f'''<section class="band band-hero"><div class="wrap page-hero">{eyebrow('Experience & education', '01')}<h1>{e(DATA['experience_hero']['title'])}</h1><p class="lead">{e(DATA['experience_hero']['lead'])}</p></div></section>
<section class="band" aria-labelledby="practice-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Professional experience', '02')}<h2 id="practice-title">Experience.</h2></div>{arrow_link('cv.html', 'Full CV')}</div>{experience_items()}</div></section>
<section class="band band-sky" aria-labelledby="education-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Education', '03')}<h2 id="education-title">An engineering lens, an analytics toolkit.</h2></div></div>{education_items()}</div></section>
<section class="band band-navy" aria-labelledby="service-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Service & mentoring', '04')}<h2 id="service-title">Giving back.</h2></div></div><div class="service-grid">{service_html}</div></div></section>
<section class="band" aria-labelledby="skills-title"><div class="wrap"><div class="section-head"><div>{eyebrow('Skills', '05')}<h2 id="skills-title">Tools for the question at hand.</h2></div></div>{skills_grid()}</div></section>'''
    page('experience.html', 'Experience & Education', 'Jiani (Elva) He: Data Science Consultant at Accenture, BMW Group dynamic-pricing capstone, MIT MS in Business Analytics (Operations Research Center), and Purdue BS in Industrial Engineering.', body, 'experience')


def cv():
    def cv_pub(p):
        authors = ', '.join(f'<strong>{e(a)}*</strong>' if a == 'Jiani He' and a in p['equal'] else f'<strong>{e(a)}</strong>' if a == 'Jiani He' else e(a) + ('*' if a in p['equal'] else '') for a in p['authors'])
        if p['equal']:
            authors += ' (*equal contribution)'
        link = f' <a href="{e(p["url"])}">{e(p["record"])}</a>.' if p['url'] else f' {e(p["record"])}.'
        status = p['status'] + (' · ' + p['proceedings'].lower() if p['proceedings'] else '')
        return f'<li>{authors}. {p["year"]}. “{e(p["title"])}.” <em>{e(p["venue"])}</em>.{link} <span class="cv-status">{e(status)}</span></li>'
    pub_sections = ''.join(f'<h3 class="cv-sub">{e(g["title"])}</h3><ol class="cv-pubs">{"".join(cv_pub(p) for p in PUBS if p["group"] == g["id"])}</ol>' for g in DATA['groups'] if any(p['group'] == g['id'] for p in PUBS))
    xp = ''.join(f'''<div class="cv-entry"><div class="cv-row"><strong>{e(x['org'])}</strong><span>{e(x['dates'])}</span></div><div class="cv-row cv-meta"><em>{e(x['role'])}</em><span>{e(x['place'])}</span></div>{f'<p class="cv-context">{e(x["context"])}</p>' if x['context'] else ''}<ul>{"".join(f"<li>{e(b)}</li>" for b in x['bullets'])}</ul></div>''' for x in DATA['experience'])
    edu = ''.join(f'''<div class="cv-entry"><div class="cv-row"><strong>{e(x['school'])}</strong><span>{e(x['date'])}</span></div><div class="cv-row cv-meta"><em>{e(x['degree'])} · {e(x['gpa'])}</em><span>{e(x['place'])}</span></div><p>{e(x['detail'])}</p></div>''' for x in DATA['education'])
    skills = ''.join(f'<p><strong>{e(s["area"])}:</strong> {e(", ".join(s["items"]))}</p>' for s in DATA['skills'])
    body = f'''<section class="band band-hero cv-hero"><div class="wrap page-hero">{eyebrow('Curriculum vitae', '01')}<h1>Curriculum vitae.</h1><p class="lead">A web version of my CV, kept in sync with the publication list on this site.</p><div class="hero-buttons"><a class="btn btn-primary" href="assets/Jiani_He_CV.pdf" download>{ICONS['file']}Download PDF</a><button class="btn btn-soft print-button">Print this page</button></div></div></section>
<section class="band band-flush" aria-label="CV document"><div class="wrap"><article class="card cv-doc"><header class="cv-head"><h2>{DATA['name']}</h2><p>{DATA['headline']}</p><p>{DATA['location']} · <a href="mailto:{DATA['email']}">{DATA['email']}</a> · <a href="{SITE}">jiani19980225.github.io</a> · <a href="{e(DATA['linkedin'])}">LinkedIn</a> · <a href="{e(DATA['scholar'])}">Google Scholar</a></p></header>
<section class="cv-section"><h2>Research interests</h2><p>AI-assisted reverse logistics and resource recovery · Inspection and disposition under uncertainty · Causal decision support · Forecast stability and planning value · AI deployment assurance</p><p>Related areas on the U.S. Critical and Emerging Technologies List (2026): AI and Autonomy (research), and Semiconductors and Microelectronics (through data center hardware supply chains).</p></section>
<section class="cv-section"><h2>Professional experience</h2>{xp}</section>
<section class="cv-section"><h2>Education</h2>{edu}</section>
<section class="cv-section"><h2>Research &amp; publications</h2>{pub_sections}</section>
<section class="cv-section"><h2>Service &amp; mentoring</h2><ul><li>Peer reviewer for 10+ journal manuscripts.</li><li>Mentored five junior analysts across Accenture roles; led onboarding and team training, including AI-assisted analysis.</li></ul></section>
<section class="cv-section"><h2>Skills</h2>{skills}</section>
</article><p class="small-note">Updated {DATA['updated']}. For the latest papers, see my <a href="{e(DATA['scholar'])}">Google Scholar profile</a>.</p></div></section>'''
    page('cv.html', 'Curriculum Vitae', 'Curriculum vitae of Jiani (Elva) He: professional experience, education, publications, service, and skills. Download the PDF or print this page.', body, 'cv')


def philosophy():
    ph = DATA['philosophy']
    portrait = f'<img src="{e(DATA["photo"])}" width="220" height="220" alt="Portrait of {DATA["name"]}">' if DATA['photo'] else '<span aria-hidden="true">JH</span>'
    pr = ph['practice']
    moments = ''.join(f'<article class="moment"><h3>{e(m["title"])}</h3><p>{e(m["text"])}</p></article>' for m in pr['items'])
    practice = f'''<section class="band" id="in-practice" aria-labelledby="title-practice"><div class="wrap"><div class="section-head"><div>{eyebrow(e(pr['eyebrow']), '03')}<h2 id="title-practice">{e(pr['title'])}</h2><p class="section-lead">{e(pr['intro'])}</p></div></div><div class="moments">{moments}</div></div></section>'''
    stories = ''
    if ph['stories']:
        cards = ''.join(f'<article class="story"><h3>{e(s["title"])}</h3>{"".join(f"<p>{e(x)}</p>" for x in s["text"])}</article>' for s in ph['stories'])
        stories = f'''<section class="band band-sky" id="life-stories" aria-labelledby="title-stories"><div class="wrap philo-group"><header>{eyebrow('Life stories', '02')}<h2 id="title-stories">What shapes me.</h2></header><div class="stories">{cards}</div></div></section>'''
    body = f'''<section class="band band-hero" aria-labelledby="philo-title"><div class="wrap philo-hero"><div>{eyebrow('Philosophy', '01')}<h1 id="philo-title">What I believe.</h1><p class="philo-intro">{e(ph['intro'])}</p></div><figure class="philo-portrait"><div class="avatar"><div class="avatar-inner">{portrait}</div></div><figcaption>{DATA['name']} · {DATA['location']}</figcaption></figure></div></section>
{stories}
{practice}'''
    page('philosophy.html', 'Philosophy', 'Stories from Jiani (Elva) He: choosing optimization, always learning, asking one more question, and a life decision that ended in a tie.', body, 'philosophy')


home()
research()
publications()
experience()
philosophy()
cv()
page('404.html', 'Page not found', 'Find research, publications, and contact information for Jiani (Elva) He.', f'<section class="band band-hero"><div class="wrap page-hero">{eyebrow("404 · Page not found")}<h1>Let’s find the right page.</h1><p class="lead">This address isn’t available. Try one of these instead.</p><div class="hero-buttons"><a class="btn btn-primary" href="index.html">Home</a><a class="btn btn-soft" href="research.html">Research</a><a class="btn btn-soft" href="publications.html">Publications</a></div></div></section>')
pages = ['', 'research.html', 'publications.html', 'experience.html', 'philosophy.html', 'cv.html']
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{SITE}{f}</loc></url>' for f in pages) + '</urlset>\n')
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
print(f'Built {len(pages)} pages, 404 page, sitemap, and robots.txt.')
