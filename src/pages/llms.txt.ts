export const prerender = true;

export function GET() {
  return new Response(`# Jonas El Gammal

> Quantitative researcher and scientific software developer with a background in cosmology, working in Bayesian inference, probabilistic machine learning, gravitational-wave astronomy, and open-source scientific software.

Jonas El Gammal is a postdoctoral researcher at the National Institute of Chemical Physics and Biophysics (KBFI / NICPB) in Tallinn, Estonia. He holds a PhD in physics from the University of Stavanger and degrees in physics from RWTH Aachen University.

## Primary pages

- [Profile and overview](https://jonaselgammal.github.io/): current role, research profile, quantitative methods, and selected technical work.
- [Research](https://jonaselgammal.github.io/research/): scientific machine learning, Bayesian inference, pulsar timing arrays, early-universe gravitational waves, and reliable AI systems.
- [Research software](https://jonaselgammal.github.io/software/): GPry, SIGWAY, fastropop, discoverysamplers, and Graphsmith.
- [Résumé and academic CV](https://jonaselgammal.github.io/resume/): human-readable experience, education, publications, technical methods, and direct document downloads.
- [Interactive research lab](https://jonaselgammal.github.io/lab/): demonstrations of active learning, primordial-spectrum reconstruction, and astrophysical population simulation.
- [Resources](https://jonaselgammal.github.io/resources/): PhD thesis, MSc thesis, and teaching material.

## Main software

- [GPry](https://jonaselgammal.github.io/gpry/): Gaussian-process surrogate modelling and active learning for Bayesian inference with expensive likelihoods.
- [SIGWAY](https://jonaselgammal.github.io/software/sigway/): JAX framework for scalar-induced gravitational-wave calculations and inference from primordial curvature perturbations.
- [fastropop](https://jonaselgammal.github.io/software/fastropop/): JAX-backed simulation of supermassive black-hole binary populations and nanohertz gravitational-wave signals.
- [discoverysamplers](https://jonaselgammal.github.io/software/discoverysamplers/): consistent interfaces between Discovery PTA models and several inference backends.
- [Graphsmith](https://jonaselgammal.github.io/projects/): experimental typed graph planning, deterministic validation, repair, and execution.

## Résumé documents

- [Industry résumé (PDF)](https://jonaselgammal.github.io/assets/files/Jonas_El_Gammal_industry_resume.pdf): concise one-page résumé for quantitative research, machine learning, AI systems, data science, and scientific software engineering roles.
- [Academic curriculum vitae (PDF)](https://jonaselgammal.github.io/assets/files/CV_jonas_el_gammal.pdf): research appointments, education, teaching, publications, current research and development, methods, and open-source software.

## Professional capabilities

Bayesian inference; probabilistic machine learning; Gaussian processes; active learning; uncertainty quantification; Monte Carlo methods; numerical optimisation; time-series and signal analysis; stochastic simulation; differentiable programming; LLM agents and agent loops; structured planning, validation, repair, tracing, and evaluation; Python; JAX; NumPy; SciPy; scikit-learn; PyTorch; TensorFlow; C++; FastAPI; REST APIs; Docker; Git; Linux; CI/CD; HPC and GPU computing; scientific software development; cosmology; gravitational-wave astronomy; pulsar timing arrays; LISA.

## Authoritative identity links

- [ORCID](https://orcid.org/0009-0005-4833-4266)
- [INSPIRE-HEP](https://inspirehep.net/authors/2902073)
- [GitHub](https://github.com/jonaselgammal)
- [LinkedIn](https://www.linkedin.com/in/jelgammal/)
`, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
}
