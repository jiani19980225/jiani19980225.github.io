"""Build the public CV PDF from content.json. Requires reportlab; the website itself has no dependencies."""
import json
from html import escape
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'content.json').read_text())
INK, STEEL, GOLD, MUTED = '#252829', '#285F96', '#C8963E', '#5D6468'
WIDTH = letter[0] - 92 - 12  # page margins plus the frame's 6pt side padding


def style(name, font='Helvetica', size=9, leading=13, color=INK, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=leading, textColor=colors.HexColor(color), **kw)


S = {
    'name': style('name', 'Times-Roman', 28, 32, spaceAfter=4),
    'subtitle': style('subtitle', size=9, leading=13.5, color=MUTED, spaceAfter=4),
    'section': style('section', 'Helvetica-Bold', 9.5, 13, STEEL, spaceBefore=13, spaceAfter=7, keepWithNext=1),
    'role': style('role', 'Helvetica-Bold', 9.8, 13),
    'meta': style('meta', size=8.6, leading=12, color=STEEL),
    'right': style('right', size=8.6, leading=12, color=MUTED, alignment=2),
    'body': style('body', spaceAfter=4),
    'bullet': style('bullet', leftIndent=11, firstLineIndent=-8, spaceAfter=2.5),
    'sub': style('sub', 'Helvetica-Bold', 9, 13, spaceBefore=5, spaceAfter=3, keepWithNext=1),
    'pub': style('pub', size=8.8, leading=12.4, leftIndent=14, firstLineIndent=-14, spaceAfter=5),
}
story = []


def add(text, kind='body'):
    story.append(Paragraph(text, S[kind]))


def section(title):
    add(title.upper(), 'section')


def row(left, right, lk='role', rk='right'):
    t = Table([[Paragraph(left, S[lk]), Paragraph(right, S[rk])]], colWidths=[WIDTH * .72, WIDTH * .28], hAlign='LEFT')
    t.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 1), ('VALIGN', (0, 0), (-1, -1), 'BOTTOM')]))
    return t


def link(url, label):
    return f'<link href="{escape(url)}" color="{STEEL}">{escape(label)}</link>'


add(escape(DATA['name']), 'name')
add(f"{escape(DATA['headline'])}<br/>{escape(DATA['location'])} | {escape(DATA['email'])} | "
    f"{link('https://jiani19980225.github.io', 'jiani19980225.github.io')} | {link(DATA['linkedin'], 'LinkedIn')} | {link(DATA['scholar'], 'Google Scholar')}", 'subtitle')

section('Research interests')
add('Demand-forecast stability and planning value; causal decision support under partial information; trustworthy deployment of AI systems; AI-assisted reverse logistics.')
add('Related areas on the U.S. Critical and Emerging Technologies List (2026): AI and Autonomy (research), and Semiconductors and Microelectronics (through data center hardware supply chains).')

section('Professional experience')
for x in DATA['experience']:
    block = [row(escape(x['org']), escape(x['dates'].replace('—', '-'))), row(escape(x['role']), escape(x['place']), 'meta')]
    if x['context']:
        block.append(Paragraph(f'<i>{escape(x["context"])}</i>', S['body']))
    block += [Paragraph('• ' + escape(b), S['bullet']) for b in x['bullets']]
    story.append(KeepTogether(block + [Spacer(1, 6)]))

section('Education')
for x in DATA['education']:
    story.append(KeepTogether([row(escape(x['school']), escape(x['date'])), row(f"{escape(x['degree'])} | {escape(x['gpa'])}", escape(x['place']), 'meta'),
                               Paragraph(escape(x['detail']), S['body']), Spacer(1, 4)]))

section('Research & publications')
n = 0
for g in DATA['groups']:
    if not any(p['group'] == g['id'] for p in DATA['publications']):
        continue
    add(escape(g['title']), 'sub')
    for p in (p for p in DATA['publications'] if p['group'] == g['id']):
        n += 1
        authors = ', '.join(f'<b>{escape(a)}</b>' if a == 'Jiani He' else escape(a) for a in p['authors'])
        record = link(p['url'], p['record']) if p['url'] else escape(p['record'])
        story.append(KeepTogether([Paragraph(f'{n}. {authors}. {p["year"]}. “{escape(p["title"])}.” <i>{escape(p["venue"])}</i>. {record}. '
                                             f'<font color="{GOLD}"><b>{escape(p["status"] + ("; " + p["proceedings"].lower() if p["proceedings"] else ""))}</b></font>', S['pub'])]))

section('Service & mentoring')
add('• Peer reviewer for 10+ journal manuscripts.', 'bullet')
add('• Mentored five junior analysts across Accenture roles; led onboarding and team training, including AI-assisted analysis.', 'bullet')

section('Skills')
for s in DATA['skills']:
    add(f'<b>{escape(s["area"])}:</b> {escape(", ".join(s["items"]))}')


def footer(canvas, doc):
    canvas.setStrokeColor(colors.HexColor(GOLD))
    canvas.setLineWidth(.7)
    canvas.line(52, 39, 560, 39)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor(MUTED))
    canvas.drawString(52, 26, f"{DATA['name']} | Curriculum vitae | {DATA['updated']}")
    canvas.drawRightString(560, 26, str(doc.page))


doc = SimpleDocTemplate(str(ROOT / 'assets/Jiani_He_CV.pdf'), pagesize=letter, rightMargin=46, leftMargin=46, topMargin=40, bottomMargin=52,
                        title=f"{DATA['name']} - Curriculum Vitae", author=DATA['name'])
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print('Built assets/Jiani_He_CV.pdf')
