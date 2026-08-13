from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/files/CV_jonas_el_gammal.pdf"

INK = colors.HexColor("#20242A")
MUTED = colors.HexColor("#59636E")
ACCENT = colors.HexColor("#8F292F")
RULE = colors.HexColor("#D7DCE1")


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.line(18 * mm, 13 * mm, 192 * mm, 13 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 8.5 * mm, "Jonas El Gammal")
    canvas.drawRightString(192 * mm, 8.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


doc = BaseDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    leftMargin=18 * mm,
    rightMargin=18 * mm,
    topMargin=12 * mm,
    bottomMargin=16 * mm,
    title="Jonas El Gammal CV",
    author="Jonas Elias El Gammal",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates(PageTemplate(id="cv", frames=[frame], onPage=footer))

base = getSampleStyleSheet()
styles = {
    "name": ParagraphStyle("name", parent=base["Title"], fontName="Helvetica-Bold", fontSize=21, leading=24, textColor=INK, alignment=TA_CENTER, spaceAfter=2),
    "tag": ParagraphStyle("tag", parent=base["Normal"], fontName="Helvetica", fontSize=9.6, leading=12, textColor=MUTED, alignment=TA_CENTER, spaceAfter=3),
    "links": ParagraphStyle("links", parent=base["Normal"], fontName="Helvetica", fontSize=8.1, leading=10, textColor=MUTED, alignment=TA_CENTER, spaceAfter=5),
    "section": ParagraphStyle("section", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=11.3, leading=13, textColor=ACCENT, spaceBefore=5, spaceAfter=3, borderPadding=(0, 0, 1, 0), borderWidth=0, keepWithNext=True),
    "role": ParagraphStyle("role", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.6, leading=10.3, textColor=INK, spaceBefore=1.5, spaceAfter=0.5, keepWithNext=True),
    "body": ParagraphStyle("body", parent=base["Normal"], fontName="Helvetica", fontSize=8.1, leading=10.2, textColor=INK, spaceAfter=1.5),
    "bullet": ParagraphStyle("bullet", parent=base["Normal"], fontName="Helvetica", fontSize=8, leading=10, textColor=INK, leftIndent=10, firstLineIndent=-6, bulletIndent=0, spaceAfter=0.8),
}


def p(text, style="body"):
    return Paragraph(text, styles[style])


def section(title):
    return [p(title, "section")]


def role(title, dates, detail=None):
    items = [p(f"{title} <font color='#59636E'>| {dates}</font>", "role")]
    if detail:
        items.append(p(detail))
    return items


def bullet(text):
    return Paragraph(f"• {text}", styles["bullet"])


story = [
    p("Jonas Elias El Gammal", "name"),
    p("Cosmologist and scientific machine-learning researcher", "tag"),
    p(
        '<link href="mailto:jonas.el.gammal@rwth-aachen.de" color="#8F292F">jonas.el.gammal@rwth-aachen.de</link>'
        '  |  <link href="https://jonaselgammal.github.io" color="#8F292F">jonaselgammal.github.io</link>'
        '  |  <link href="https://github.com/jonaselgammal" color="#8F292F">GitHub</link>'
        '  |  <link href="https://orcid.org/0009-0005-4833-4266" color="#8F292F">ORCID</link>',
        "links",
    ),
]

story += section("PROFILE")
story += [p("Postdoctoral researcher working at the intersection of cosmology, gravitational-wave astronomy, Bayesian inference, and scientific machine learning. Developer of open-source tools for accelerating expensive likelihood-based inference and modelling gravitational-wave signals.")]

story += section("RESEARCH EXPERIENCE")
story += role('<link href="https://kbfi.ee/en/" color="#20242A">National Institute of Chemical Physics and Biophysics (KBFI/NICPB)</link> - Postdoctoral Researcher', "2026-present", "Tallinn, Estonia")
story += role('<link href="https://www.uninsubria.eu" color="#20242A">University of Insubria</link> - Postdoctoral Researcher', "2025-2026")
story += [bullet("Accelerated Pulsar Timing Array inference using GPUs and differentiable programming with JAX as part of the EPTA collaboration.")]
story += role('<link href="https://theory.cern/" color="#20242A">CERN Theory Department</link> - Visiting Researcher', "2024")
story += [bullet("Developed a LISA data-analysis pipeline for second-order scalar-induced gravitational waves from inflation with M. Pieroni and G. Franciolini.")]

story += section("EDUCATION")
story += role("University of Stavanger - PhD in Physics", "2021-2025", "Thesis: <i>Cutting edge data analysis for gravitational wave detection with LISA</i>.")
story += role("Grenoble INP, PHELMA - Erasmus Exchange", "2019-2020", "Specialisation in nuclear engineering.")
story += role("RWTH Aachen University - MSc Physics", "2018-2020", "Grade 1.3. Thesis: <i>Accelerating Bayesian Inference of Expensive Likelihoods with Gaussian Processes</i>.")
story += role("RWTH Aachen University - BSc Physics", "2015-2018", "Grade 1.7. Focus on astroparticle physics and cosmology.")

story += section("SELECTED PUBLICATIONS")
publications = [
    ("Are PTA measurements sensitive to gravitational wave non-Gaussianities?", "C. Cecchini, J. El Gammal, G. Franciolini, M. Pieroni", "2026", "https://arxiv.org/abs/2605.05157"),
    ("Accelerating LISA inference with Gaussian processes", "J. El Gammal, R. Buscicchio, J. Torrado, G. Nardini", "2025", "https://arxiv.org/abs/2503.21871"),
    ("Reconstructing Primordial Curvature Perturbations via Scalar-Induced Gravitational Waves with LISA", "LISA Cosmology Working Group", "2025", "https://arxiv.org/abs/2501.11320"),
    ("Parallelized Acquisition for Active Learning using Monte Carlo Sampling", "J. Torrado, N. Schöneberg, J. El Gammal", "2023", "https://arxiv.org/abs/2305.19267"),
    ("Fast and Robust Bayesian Inference using Gaussian Processes with GPry", "J. El Gammal et al.", "2022", "https://arxiv.org/abs/2211.02045"),
]
for title, authors, year, url in publications:
    story.append(p(f'<link href="{url}" color="#8F292F"><b>{title}</b></link> ({year})<br/><font color="#59636E">{authors}</font>'))

story += section("OPEN-SOURCE SOFTWARE")
software = [
    ("GPry", "https://github.com/jonaselgammal/GPry", "Bayesian inference for expensive likelihoods using Gaussian-process surrogate modelling and active learning."),
    ("SIGWAY", "https://github.com/jonaselgammal/SIGWAY", "Simulation and inference tools for second-order scalar-induced gravitational waves from inflation."),
    ("discoverysamplers", "https://github.com/jonaselgammal/discoverysamplers", "Unified interfaces connecting Discovery PTA models to multiple sampling backends."),
    ("fastropop", "https://github.com/jonaselgammal/fastropop", "JAX-enabled simulation of supermassive black-hole-binary populations and nanohertz gravitational-wave signatures."),
]
for name, url, description in software:
    story.append(p(f'<link href="{url}" color="#8F292F"><b>{name}</b></link> - {description}'))

story += section("TEACHING")
story += [
    p("<b>Numerical Methods</b>, University of Stavanger - full bachelor-level course (2023, 2024). Python programming; numerical differentiation, integration, ODEs, and PDEs."),
    p("<b>Electromagnetism and Special Relativity</b>, University of Stavanger - full bachelor-level course (2023)."),
    p("<b>Physics and data-processing tutorials</b>, RWTH Aachen University (2017-2019)."),
]

story += section("SKILLS")
story += [
    p("<b>Research:</b> Bayesian inference, Gaussian processes, uncertainty quantification, active learning, time-series analysis, cosmology, and gravitational-wave data analysis."),
    p("<b>Software:</b> Python, JAX, NumPy, SciPy, scikit-learn, PyTorch, TensorFlow, SQL, C++, Git, Docker, Linux, SLURM, HPC, CI/CD, and scientific package development."),
    p("<b>Languages:</b> German (native), English (near-native), French (B2/C1)."),
]

doc.build(story)
print(OUTPUT)
