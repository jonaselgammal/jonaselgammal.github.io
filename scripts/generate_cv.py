from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/files/CV_jonas_el_gammal.pdf"
INK = colors.HexColor("#182328")
MUTED = colors.HexColor("#626B6B")
PETROL = colors.HexColor("#527A7B")
PAPER = colors.white
BAND = colors.HexColor("#E5E8E4")
LINE = colors.HexColor("#CDD2CF")

doc = BaseDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    leftMargin=16 * mm,
    rightMargin=16 * mm,
    topMargin=12 * mm,
    bottomMargin=14 * mm,
    title="Jonas El Gammal - Academic CV",
    author="Jonas Elias El Gammal",
    subject="Academic curriculum vitae: cosmology, gravitational-wave astronomy, Bayesian inference, scientific machine learning, publications, teaching, and open-source software.",
    keywords="academic CV, cosmology, gravitational waves, Bayesian inference, probabilistic machine learning, scientific machine learning, Gaussian processes, active learning, uncertainty quantification, JAX, Python, computational statistics, scientific software, pulsar timing arrays, LISA, publications",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22, leading=24, textColor=INK, spaceAfter=1.2 * mm),
    "tag": ParagraphStyle("tag", fontName="Helvetica", fontSize=10.2, leading=12.5, textColor=PETROL, spaceAfter=1.2 * mm),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=7.7, leading=9, textColor=MUTED, spaceAfter=1.5 * mm),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=8.4, leading=10, textColor=PETROL),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=8.5, leading=10, textColor=INK),
    "date": ParagraphStyle("date", fontName="Helvetica", fontSize=7.8, leading=10, textColor=MUTED, alignment=TA_RIGHT),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=7.75, leading=9.25, textColor=INK, spaceAfter=.65 * mm),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=7.65, leading=9.15, textColor=INK, leftIndent=3.5 * mm, firstLineIndent=-2.5 * mm, spaceAfter=.35 * mm),
    "paper": ParagraphStyle("paper", fontName="Helvetica", fontSize=7.55, leading=9, textColor=INK, spaceAfter=.75 * mm),
    "software": ParagraphStyle("software", fontName="Helvetica", fontSize=7.65, leading=9.15, textColor=INK, spaceAfter=.5 * mm),
}

def p(text, style="body"):
    return Paragraph(text, styles[style])

def section(title):
    band = Table([[p(title.upper(), "section")]], colWidths=[173 * mm])
    band.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), BAND), ("LINEBEFORE", (0, 0), (0, 0), 2.2, PETROL), ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm), ("TOPPADDING", (0, 0), (-1, -1), .7 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), .55 * mm)]))
    band.spaceBefore = 1.4 * mm
    band.spaceAfter = .6 * mm
    return band

def role(title, date):
    table = Table([[p(title, "role"), p(date, "date")]], colWidths=[143 * mm, 30 * mm])
    table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), .5 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), .2 * mm)]))
    return table

def bullet(text):
    return p(f"• {text}", "bullet")

def page(canvas, document):
    canvas.saveState()
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.line(16 * mm, 9 * mm, 194 * mm, 9 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 6.8)
    canvas.drawString(16 * mm, 5.5 * mm, "Jonas El Gammal - Academic CV")
    canvas.drawRightString(194 * mm, 5.5 * mm, f"Page {document.page}  |  Updated October 2026")
    canvas.restoreState()

doc.addPageTemplates(PageTemplate(id="cv", frames=[frame], onPage=page))

story = [
    p("Jonas Elias El Gammal", "name"),
    p("Cosmologist | Scientific machine-learning researcher | Scientific software developer", "tag"),
    p('<link href="mailto:jonas.el.gammal@kbfi.ee" color="#527A7B">jonas.el.gammal@kbfi.ee</link>  |  Tallinn, Estonia  |  <link href="https://jonaselgammal.github.io" color="#527A7B">jonaselgammal.github.io</link>  |  <link href="https://github.com/jonaselgammal" color="#527A7B">GitHub</link>  |  <link href="https://orcid.org/0009-0005-4833-4266" color="#527A7B">ORCID</link>', "contact"),
    section("Profile"),
    p("Postdoctoral researcher and technology founder working across cosmology, Bayesian inference, scientific machine learning, and software. I develop validated computational methods and lead the translation of data, automation, and AI into operational systems."),
    section("Professional and research experience"),
    role("Co-founder, Managing Director &amp; CTO - Bright Interface GmbH", "2026-present"),
    bullet("Lead product and technology strategy for a healthcare-software platform combining data integration, workflow automation, operational analytics, and applied AI."),
    role("Postdoctoral Researcher - KBFI / NICPB, Tallinn", "2026-present"),
    bullet("KOHTO grant recipient; research in cosmology, gravitational-wave inference, scientific ML, and computational methods."),
    role("Postdoctoral Researcher - University of Insubria", "2025-2026"),
    bullet("Developed GPU-accelerated and differentiable pulsar-timing-array inference with JAX in the EPTA collaboration."),
    role("Visiting Researcher - CERN", "2024"),
    bullet("Developed a LISA analysis pipeline for scalar-induced gravitational waves."),
    section("Education"),
    role("PhD in Physics - University of Stavanger", "2021-2025"),
    p("Developed data-analysis methods for LISA, including Gaussian-process-accelerated Bayesian inference and reconstruction of primordial curvature perturbations from scalar-induced gravitational waves."),
    role("Erasmus Exchange - Grenoble INP, PHELMA", "2019-2020"),
    p("Specialisation in nuclear engineering."),
    role("MSc in Physics - RWTH Aachen University", "2018-2020"),
    p("Grade 1.3 (approximately 3.7/4.0 GPA). Thesis: <i>Accelerating Bayesian Inference of Expensive Likelihoods with Gaussian Processes</i>."),
    role("BSc in Physics - RWTH Aachen University", "2015-2018"),
    p("Grade 1.7 (approximately 3.3/4.0 GPA). Focus on astroparticle physics and cosmology."),
    section("Teaching"),
    p("<b>Numerical Methods</b>, University of Stavanger - full bachelor-level course (2023, 2024): Python, numerical differentiation and integration, ODEs, and PDEs."),
    p("<b>Electromagnetism and Special Relativity</b>, University of Stavanger - full bachelor-level course (2023)."),
    p("<b>Physics and data-processing tutorials</b>, RWTH Aachen University (2017-2019)."),
    section("Methods and technology"),
    p("<b>Research:</b> Bayesian inference, Gaussian processes, active learning, uncertainty quantification, Monte Carlo methods, numerical optimisation, stochastic simulation, time-series analysis, cosmology, and gravitational-wave data analysis."),
    p("<b>AI systems:</b> LLM agents, tool use, agent loops, multi-agent workflows, typed planning, structured outputs, validation, repair, tracing, evaluation, and reproducible experimentation."),
    p("<b>Software:</b> Python, JAX, NumPy, SciPy, scikit-learn, PyTorch, TensorFlow, C++, Git, Docker, Linux, SLURM, HPC/GPU computing, CI/CD, testing, documentation, and package development."),
    section("Languages"),
    p("<b>German</b> - native  |  <b>English</b> - near-native  |  <b>French</b> - B2/C1"),
    section("Publications"),
]

publications = [
    ("Are PTA measurements sensitive to gravitational wave non-Gaussianities?", "C. Cecchini, J. El Gammal, G. Franciolini, M. Pieroni", "2026 - accepted for publication in Physical Review Letters; arXiv:2605.05157", "https://arxiv.org/abs/2605.05157"),
    ("Accelerating LISA inference with Gaussian processes", "J. El Gammal, R. Buscicchio, G. Nardini, J. Torrado", "2025 - Physical Review D 112, 063010", "https://doi.org/10.1103/c66v-rl3w"),
    ("Reconstructing primordial curvature perturbations via scalar-induced gravitational waves with LISA", "J. El Gammal et al. (LISA Cosmology Working Group)", "2025 - JCAP 05, 062", "https://doi.org/10.1088/1475-7516/2025/05/062"),
    ("Parallelized Acquisition for Active Learning using Monte Carlo Sampling", "J. Torrado, N. Schoeneberg, J. El Gammal", "2023 - arXiv:2305.19267", "https://arxiv.org/abs/2305.19267"),
    ("Fast and robust Bayesian inference using Gaussian processes with GPry", "J. El Gammal, N. Schoeneberg, J. Torrado, C. Fidler", "2023 - JCAP 10, 021", "https://doi.org/10.1088/1475-7516/2023/10/021"),
]
for title, authors, record, url in publications:
    story.append(p(f'<link href="{url}" color="#527A7B"><b>{title}</b></link><br/><font color="#626B6B">{authors} - {record}</font>', "paper"))

story.extend([section("Current research and development"),
    bullet("High-dimensional GP surrogate inference using gradient-based NUTS acquisition, with emphasis on numerical robustness, reproducible benchmarking, and scalable active learning."),
    bullet("GPU-accelerated JAX likelihoods and reversible-jump inference for continuous gravitational-wave searches with pulsar timing arrays."),
    bullet("PROSECCO: differentiable surrogate refitting of physical stochastic-background models against model-independent LISA reconstructions (in development)."),
    section("Open-source software")])

software = [
    ("GPry", "https://github.com/jonaselgammal/GPry", "Gaussian-process surrogate modelling and active learning for Bayesian inference with expensive likelihoods."),
    ("SIGWAY", "https://github.com/jonaselgammal/SIGWAY", "JAX framework for scalar-induced gravitational-wave simulation and inference."),
    ("discoverysamplers", "https://github.com/jonaselgammal/discoverysamplers", "Consistent interfaces connecting Discovery PTA models to multiple Bayesian inference backends."),
    ("fastropop", "https://github.com/jonaselgammal/fastropop", "JAX-backed simulation of supermassive black-hole-binary populations and their nanohertz signals."),
    ("Graphsmith", "https://github.com/jonaselgammal/Graphsmith", "Typed graph planning with deterministic compilation, validation, local repair, and traceable execution."),
]
for name, url, description in software:
    story.append(p(f'<link href="{url}" color="#527A7B"><b>{name}</b></link> - {description}', "software"))

doc.build(story)
print(OUTPUT)
