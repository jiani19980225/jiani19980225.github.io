"""Build a concise public CV. Requires reportlab; website itself has no dependencies."""
import json
from html import escape
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'content.json').read_text())
NAVY, BLUE, MUTED = '#102d46', '#0077b6', '#4e6272'
styles = {
 'name': ParagraphStyle('name',fontName='Times-Roman',fontSize=30,leading=34,textColor=colors.HexColor(NAVY),spaceAfter=7),
 'subtitle': ParagraphStyle('subtitle',fontName='Helvetica',fontSize=9,leading=14,textColor=colors.HexColor(MUTED),spaceAfter=13),
 'section': ParagraphStyle('section',fontName='Helvetica-Bold',fontSize=10,leading=14,textColor=colors.HexColor(BLUE),spaceBefore=14,spaceAfter=9),
 'role': ParagraphStyle('role',fontName='Helvetica-Bold',fontSize=10,leading=14,textColor=colors.HexColor(NAVY),spaceAfter=3),
 'meta': ParagraphStyle('meta',fontName='Helvetica',fontSize=8.5,leading=12,textColor=colors.HexColor(MUTED),spaceAfter=6),
 'body': ParagraphStyle('body',fontName='Helvetica',fontSize=9,leading=13,textColor=colors.HexColor(NAVY),spaceAfter=6),
 'bullet': ParagraphStyle('bullet',fontName='Helvetica',fontSize=9,leading=13,leftIndent=11,firstLineIndent=-9,textColor=colors.HexColor(NAVY),spaceAfter=4),
 'pub': ParagraphStyle('pub',fontName='Helvetica-Bold',fontSize=9.5,leading=13,textColor=colors.HexColor(NAVY),spaceAfter=4),
}
story=[]
def p(text,kind='body'): return Paragraph(text,styles[kind])
def add(text,kind='body'): story.append(p(text,kind))
def bullet(text): add('- '+text,'bullet')
def section(title): add(title.upper(),'section')

add('Jiani (Elva) He','name')
add('Data Science Consultant | Independent Researcher<br/>Seattle, Washington | jiani19980225@gmail.com<br/><link href="https://jiani19980225.github.io" color="#0077b6">jiani19980225.github.io</link> | <link href="https://www.linkedin.com/in/jianihe" color="#0077b6">LinkedIn</link> | <link href="https://scholar.google.com/citations?user=QoV_NDIAAAAJ&amp;hl=en" color="#0077b6">Google Scholar</link>','subtitle')
section('Professional experience')
add('Accenture | Data Science Consultant','role')
add('Seattle, WA | Jun 2024 - Present','meta')
bullet('Lead planning analyses and client relationships; present recommendations to senior leaders.')
bullet('Analyze reverse-logistics cycle time and on-time delivery using SQL; support reuse, resale, recycling, and disposal decisions based on asset value and lifecycle stage.')
bullet('Analyze demand, stock targets, and inventory; use optimization to rebalance supply across sites.')
bullet('Plan quality-assurance component quantities using demand and bill-of-materials data; define service metrics and support inventory adjustments.')
bullet('Develop reusable prompt and query guides for enterprise LLM assistants; train analysts in AI-assisted analysis.')
story.append(Spacer(1,7))
add('Accenture | Data Science Senior Analyst','role')
add('Seattle, WA | Oct 2021 - May 2024','meta')
bullet('Built SQL dashboards and shortage alerts to compare inventory with demand and inform site transfers.')
bullet('Tracked reverse-logistics cycle times and delivery performance to support asset recovery scheduling.')
bullet('Investigated inventory imbalances and abnormal cycle times with statistical analysis; automated reporting and purchase-order workflows.')
bullet('Across both Accenture roles, mentored five junior analysts and led onboarding and team training.')
story.append(Spacer(1,7))
add('BMW Group | Data Scientist Intern, MIT Capstone','role')
add('Cambridge, MA | Feb - Aug 2021','meta')
bullet('Modeled vehicle demand and cross-price elasticity in Python to recommend discounts by customer segment and sales channel; built Tableau pricing dashboards.')
section('Education')
add('Massachusetts Institute of Technology','role')
add('MS, Business Analytics | Operations Research Center | Aug 2021 | GPA: 4.7/5.0','meta')
add('Classification trees for 40,000 news articles; robust bike allocation in Julia; NLP admissions Q&amp;A pipeline for AdmitHub, including response evaluation and human review.')
add('Purdue University','role')
add('BS, Industrial Engineering | May 2020 | Honors &amp; Distinction | GPA: 3.9/4.0','meta')
add('LSTM forecasting in Keras and reinforcement learning for sensor placement in Python/R.')
story.append(PageBreak())
add('Research, skills &amp; service','name')
add('Jiani (Elva) He | Curriculum vitae | Updated October 2026','subtitle')
section('Research & preprints')
for item in DATA['publications']:
 authors=', '.join(('<b>'+escape(a)+'</b>') if a=='Jiani He' else escape(a) for a in item['authors'])
 block=[p(escape(item['title']),'pub'),p(authors+'. '+str(item['year'])+'.','meta'),p(escape(item['status'])+'. '+escape(item['record'])+'.','meta'),p('<link href="'+escape(item['url'])+'" color="#0077b6">'+escape(item['url'])+'</link>','meta'),Spacer(1,9)]
 story.append(KeepTogether(block))
section('Technical & consulting skills')
add('<b>Tools:</b> SQL, Python, R, Julia, Keras, Tableau, AWS')
add('<b>Modeling:</b> Machine learning, forecasting, regression, classification, clustering, robust optimization')
add('<b>Analytics &amp; AI:</b> Statistical analysis, root-cause analysis, visualization, dashboards, KPI design, NLP, generative AI, LLM workflows, prompt and query design')
add('<b>Consulting:</b> Problem framing, client communication, stakeholder coordination, project delivery, mentoring')
section('Service & mentoring')
add('Peer-reviewed 10+ journal manuscripts. Mentored five junior analysts across Accenture roles in SQL, business problem solving, and client communication; led onboarding and team training.')

def footer(canvas,doc):
 canvas.setStrokeColor(colors.HexColor('#eb993f'));canvas.setLineWidth(.7);canvas.line(46,39,566,39)
 canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor(MUTED))
 canvas.drawString(46,26,'Jiani (Elva) He | Curriculum vitae | October 2026');canvas.drawRightString(566,26,str(doc.page))

doc=SimpleDocTemplate(str(ROOT/'assets/Jiani_He_CV.pdf'),pagesize=letter,rightMargin=46,leftMargin=46,topMargin=39,bottomMargin=51,title='Jiani (Elva) He - Curriculum Vitae',author='Jiani (Elva) He')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print('Built assets/Jiani_He_CV.pdf')
