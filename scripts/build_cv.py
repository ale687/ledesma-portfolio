from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'portfolio/static/portfolio/assets/cv/CV_Claudio_Ledesma.pdf'
for name, file in [('Arial', 'arial.ttf'), ('Arial-Bold', 'arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(Path('C:/Windows/Fonts') / file)))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='Arial-Bold', italic='Arial', boldItalic='Arial-Bold')
navy = colors.HexColor('#15243c')
blue = colors.HexColor('#2856cc')
body = ParagraphStyle('Body', fontName='Arial', fontSize=9.2, leading=12, textColor=navy, spaceAfter=4)
small = ParagraphStyle('Small', parent=body, fontSize=8.6, leading=11.8)
header = ParagraphStyle('Header', parent=body, fontName='Arial-Bold', fontSize=22, leading=26, alignment=TA_CENTER, spaceAfter=4)
subtitle = ParagraphStyle('Subtitle', parent=body, fontSize=11, leading=15, alignment=TA_CENTER)
contact = ParagraphStyle('Contact', parent=small, alignment=TA_CENTER)
heading = ParagraphStyle('Heading', parent=body, fontName='Arial-Bold', fontSize=10.7, leading=14, textColor=blue, spaceBefore=6, spaceAfter=3)
story = []
def p(text, style=body):
    story.append(Paragraph(text, style))
def section(title):
    p(title, heading)
    story.append(HRFlowable(width='100%', thickness=.5, color=colors.HexColor('#d7deea'), spaceAfter=4))
def project(title, stack, description, repo):
    p(f'<b>{title}</b> | {stack}')
    p(description)
    p(f'<link href="https://github.com/ale687/{repo}" color="#2856cc">github.com/ale687/{repo}</link>', small)
    story.append(Spacer(1, 3))

p('CLAUDIO LEDESMA', header)
p('Python Backend Developer Jr. | FastAPI | SQL', subtitle)
p('Buenos Aires, CABA | 11 7112-9739 | <link href="mailto:clledesma@frba.utn.edu.ar">clledesma@frba.utn.edu.ar</link>', contact)
p('<link href="https://www.linkedin.com/in/claudio-alejandro-ledesma-48b65a365/" color="#2856cc">LinkedIn</link> · <link href="https://github.com/ale687" color="#2856cc">GitHub</link> · <link href="https://ledesma-portfolio.onrender.com/" color="#2856cc">Portfolio</link>', contact)
section('PERFIL PROFESIONAL')
p('Estudiante de Ingeniería en Sistemas de Información en la UTN, orientado al desarrollo backend con Python. Desarrollo proyectos con FastAPI, Django y SQL, integrando APIs externas y bases de datos relacionales. Busco mi primera oportunidad como Python Backend Developer Jr.')
section('HABILIDADES TÉCNICAS')
p('<b>Lenguajes:</b> Python, SQL.<br/><b>Backend:</b> FastAPI, Django, APIs REST, Pydantic, Requests.<br/><b>Bases de datos:</b> SQL Server, SQLite, MySQL y modelado relacional.<br/><b>Procesamiento de datos:</b> Pandas, extracción de PDFs con PyMuPDF y Tabula.<br/><b>Herramientas:</b> Git, GitHub, Linux, VS Code, DBeaver y DB Browser for SQLite.<br/><b>Fundamentos:</b> programación orientada a objetos, manejo de archivos, JSON, variables de entorno, manejo de errores y logging.')
section('PROYECTOS')
project('News Aggregator API', 'Python · FastAPI · Requests', 'API para obtener titulares y buscar noticias de un servicio externo. Filtrado y normalización de respuestas, validación de parámetros, manejo de errores y separación entre endpoints y servicios.', 'news-aggregator-api')
project('Football Data Pipeline', 'Python · FastAPI · SQL · SQLite', 'Extracción de datos de football-data.org y almacenamiento en SQLite. Consultas SQL para analizar partidos y exposición de resultados mediante endpoints REST con FastAPI.', 'football_data_pipeline')
project('PDF Data Extractor', 'Python · Pandas · PyMuPDF · Tabula', 'Herramienta para extraer texto y tablas de múltiples archivos PDF. Procesamiento de datos y exportación a TXT y CSV para su posterior uso y análisis.', 'pdf-data-extractor')
section('EXPERIENCIA LABORAL')
p('<b>Ejército Argentino | Soldado Voluntario</b><br/>Octubre de 2022 - Actualidad')
for text in ['Control y seguimiento de materiales, recursos y registros administrativos.', 'Elaboración de informes y uso de Excel para organizar y controlar información.', 'Trabajo bajo procedimientos establecidos y apoyo administrativo y operativo.']:
    p('• ' + text)
section('EDUCACIÓN')
p('<b>Ingeniería en Sistemas de Información</b> | Universidad Tecnológica Nacional (UTN)<br/>En curso')
section('FORMACIÓN COMPLEMENTARIA')
p('Diplomatura en Python | UTN FRBA, Centro de e-Learning | Finalizada<br/>Diplomatura en Bases de Datos | UTN FRBA, Centro de e-Learning | 2026<br/>Ingeniería de Datos | UTN FRBA, Centro de e-Learning | 2026<br/>Data Analytics | Coderhouse | 2024')
section('IDIOMAS')
p('<b>Español:</b> nativo. <b>Inglés:</b> intermedio, en formación.')
doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=40, leftMargin=40, topMargin=26, bottomMargin=26, title='Claudio Ledesma | Python Backend Developer Jr.', author='Claudio Ledesma')
doc.build(story)
print(OUTPUT)
