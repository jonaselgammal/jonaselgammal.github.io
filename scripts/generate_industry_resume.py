from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/files/Jonas_El_Gammal_industry_resume.pdf"

INK = colors.HexColor("#182328")
MUTED = colors.HexColor("#626B6B")
PETROL = colors.HexColor("#527A7B")
LINE = colors.HexColor("#CDD2CF")
PAPER = colors.HexColor("#F4F1EA")

doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    leftMargin=15 * mm,
    rightMargin=15 * mm,
    topMargin=12 * mm,
    bottomMargin=12 * mm,
    title="Jonas El Gammal - Quantitative Researcher and Scientific Software Developer",
    author="Jonas El Gammal",
    subject="Industry resume for quantitative research, machine learning, AI systems, data science, and scientific software engineering roles.",
    keywords="quantitative researcher, machine learning, AI agents, data science, scientific software engineer, Python, JAX, PyTorch, TensorFlow, C++, Bayesian inference, probabilistic machine learning, Gaussian processes, active learning, uncertainty quantification, Monte Carlo, numerical optimisation, time-series analysis, FastAPI, REST API, Docker, CI/CD, HPC, GPU computing",
)

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22, leading=24, textColor=INK, spaceAfter=1.5 * mm),
    "tag": ParagraphStyle("tag", fontName="Helvetica", fontSize=10.2, leading=13, textColor=PETROL, spaceAfter=1.5 * mm),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=7.6, leading=9, textColor=MUTED),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=8.3, leading=10, textColor=PETROL),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9, leading=11, textColor=INK),
    "date": ParagraphStyle("date", fontName="Helvetica", fontSize=7.9, leading=10.5, textColor=MUTED, alignment=TA_RIGHT),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=8.35, leading=10.8, textColor=INK, spaceAfter=1.3 * mm),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.1, leading=10.4, textColor=INK, leftIndent=3.5 * mm, firstLineIndent=-2.5 * mm, spaceAfter=.9 * mm),
    "small": ParagraphStyle("small", fontName="Helvetica", fontSize=7.7, leading=9.8, textColor=INK),
}


def p(text, style="body"):
    return Paragraph(text, styles[style])


def section(title):
    band = Table([[p(title.upper(), "section")]], colWidths=[175 * mm])
    band.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E5E8E4")),
        ("BOX", (0, 0), (0, 0), 0, colors.transparent),
        ("LINEBEFORE", (0, 0), (0, 0), 2.2, PETROL),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 1.4 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2 * mm),
    ]))
    band.spaceBefore = 3.2 * mm
    band.spaceAfter = 1.7 * mm
    return band


def bullet(text):
    return p(f"• {text}", "bullet")


def role(title, date):
    table = Table([[p(title, "role"), p(date, "date")]], colWidths=[145 * mm, 30 * mm])
    table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return table


story = [
    p("Jonas El Gammal", "name"),
    p("Quantitative researcher | Scientific software developer | PhD in physics", "tag"),
    p('<link href="mailto:jonas.el.gammal@rwth-aachen.de" color="#527A7B">jonas.el.gammal@rwth-aachen.de</link>  |  Tallinn, Estonia  |  <link href="https://jonaselgammal.github.io" color="#527A7B">jonaselgammal.github.io</link>  |  <link href="https://github.com/jonaselgammal" color="#527A7B">GitHub</link>  |  <link href="https://www.linkedin.com/in/jelgammal/" color="#527A7B">LinkedIn</link>', "contact"),
    section("Profile"),
    p("Quantitative researcher and scientific software developer working across probabilistic machine learning, Bayesian inference, and computational physics. I turn expensive mathematical models into tested, documented tools for inference and decision-making under uncertainty. My work spans method development, numerical implementation, validation, publication, and open-source delivery."),
    section("Selected technical impact"),
    bullet("Developed <b>GPry</b>, an active-learning Gaussian-process framework that reduced expensive posterior evaluations by roughly two orders of magnitude in published benchmark problems."),
    bullet("Built and maintained open-source Python/JAX packages for surrogate inference, differentiable gravitational-wave modelling, astrophysical population simulation, and sampler interoperability."),
    bullet("Build tool-using AI agents and agent loops with structured plans, deterministic validation, traceable execution, and bounded repair."),
    bullet("Designed analyses that connect statistical assumptions to observable consequences, including calibrated tests of non-Gaussianity in pulsar-timing-array data."),
    bullet("Teach and communicate technical material from Python and numerical methods to Bayesian inference and gravitational-wave data analysis."),
    section("Experience"),
    role("Postdoctoral Researcher - KBFI / NICPB, Tallinn", "2026-present"),
    bullet("Research in gravitational-wave inference, cosmology, and scientific machine learning; develop reusable computational methods alongside domain analyses."),
    role("Postdoctoral Researcher - University of Insubria", "2025-2026"),
    bullet("Developed GPU-accelerated and differentiable pulsar-timing-array inference with JAX in the EPTA collaboration."),
    role("Visiting Researcher - CERN", "2024"),
    bullet("Developed a data-analysis pipeline for LISA, the ESA-led space-based gravitational-wave mission with NASA as a major partner."),
    section("Selected projects"),
]

projects = [
    [p("GPry", "role"), p("Probabilistic ML", "small"), p("Gaussian-process surrogate modelling, failure classification, active learning, convergence diagnostics, and parallel acquisition for expensive Bayesian inference.", "small")],
    [p("SIGWAY", "role"), p("Differentiable modelling", "small"), p("Modular JAX framework connecting primordial physics, cosmological kernels, numerical integration, and Bayesian reconstruction.", "small")],
    [p("fastropop", "role"), p("Stochastic simulation", "small"), p("Reproducible simulation of black-hole-binary populations, spectra, and skymaps for population-level statistical studies.", "small")],
    [p("Graphsmith", "role"), p("Reliable AI systems", "small"), p("Experimental typed graph planning with deterministic compilation, validation, local repair, and traceable execution.", "small")],
]
project_table = Table(projects, colWidths=[27 * mm, 37 * mm, 111 * mm], repeatRows=0)
project_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LINEABOVE", (0, 0), (-1, 0), .5, LINE),
    ("LINEBELOW", (0, 0), (-1, -1), .5, LINE),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
    ("TOPPADDING", (0, 0), (-1, -1), 1.5 * mm),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5 * mm),
]))
story.extend([
    project_table,
    section("Methods and technology"),
    p("<b>Methods:</b> Bayesian inference, Gaussian processes, active learning, uncertainty quantification, Monte Carlo methods, numerical optimisation, stochastic simulation, time-series and signal analysis, MCMC, nested sampling, differentiable programming, model validation."),
    p("<b>AI systems:</b> LLM agents, tool use, agent loops, multi-agent workflows, planning and execution, structured outputs, prompt and context design, validation, repair, tracing, and evaluation harnesses."),
    p("<b>Engineering:</b> Python, JAX, NumPy, SciPy, scikit-learn, PyTorch, TensorFlow, and C++; FastAPI and REST APIs; Svelte; Docker; OAuth/OIDC; encrypted data workflows; Git, Linux, CI/CD, HPC/GPU computing, testing, documentation, and releases."),
    section("Education"),
    role("PhD in Physics - University of Stavanger", "2021-2025"),
    p("Developed Gaussian-process-accelerated Bayesian inference and primordial-spectrum reconstruction methods for LISA; taught full courses in Numerical Methods and Electromagnetism."),
    role("MSc and BSc in Physics - RWTH Aachen University", "2015-2020"),
    p("Astroparticle physics and cosmology; MSc thesis on Gaussian-process acceleration of expensive Bayesian inference."),
    section("Languages"),
    p("<b>German</b> - native  |  <b>English</b> - near-native  |  <b>French</b> - B2/C1"),
])


def page(canvas, _doc):
    canvas.saveState()
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.line(15 * mm, 9 * mm, 195 * mm, 9 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 6.8)
    canvas.drawString(15 * mm, 5.5 * mm, "Jonas El Gammal - concise quantitative and technology resume")
    canvas.drawRightString(195 * mm, 5.5 * mm, "Updated August 2026")
    canvas.restoreState()


doc.build(story, onFirstPage=page, onLaterPages=page)
print(OUTPUT)
