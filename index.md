---
layout: home
---

<div style="font-size: 2.5em; font-weight: bold; text-align: center;">
  Hi, I'm Jonas!
</div>

<img src="/assets/img/me.jpg" alt="Me" style="height: 200px; width: 200px; border-radius: 50%; object-fit: cover; display: block; margin: auto;">

<div style="display: flex; gap: 20px; flex-wrap: wrap; margin-top: 20px; margin-bottom: 20px; justify-content: center;">

  <a href="mailto:jonas.el.gammal@rwth-aachen.de">
    <img src="/assets/icons/email.png" alt="Email" style="width: 40px; height: 40px;">
  </a>

  <a href="https://www.linkedin.com/in/jelgammal/" target="_blank">
    <img src="/assets/icons/linkedin.png" alt="LinkedIn" style="width: 40px; height: 40px;">
  </a>

  <a href="https://github.com/jonaselgammal" target="_blank">
    <img src="/assets/icons/github.png" alt="GitHub" style="width: 40px; height: 40px;">
  </a>

  <a href="https://inspirehep.net/authors/2902073" target="_blank">
    <img src="/assets/icons/inspire_BW.png" alt="InspireHEP" style="width: 194px; height: 40px;">
  </a>

  <a href="https://orcid.org/0009-0005-4833-4266" target="_blank">
    <img src="/assets/icons/orcid.svg" alt="OrcidID" style="width: 40px; height: 40px;">
  </a>

</div>

Welcome to my personal webpage.

I'm a cosmologist/astrophysicist, currently as a postdoc at the University of Insubria in Como, Italy. Before that I was a PhD student at the University of Stavanger in Norway (supervised by [Germano Nardini](https://www.uis.no/en/profile/germano-nardini)) and before that I studied at RWTH Aachen University in Germany. 

Most of the time I'm a pretty chill dude and I enjoy all kinds of outdoor and extreme sports, such as hiking, climbing, skiing, surfing, skydiving, you name it. I also love to travel and explore new places, especially in the mountains. 

---

Work-wise, what I'm doing can broadly be summarised as: I take slow-to-compute problems and make them fast. For this, I'm using machine learning and differentiable programming to speed up Bayesian inference for cosmology and gravitational wave detection. I also work on cosmological simulations and data analysis for Pulsar Timing Arrays (PTAs). I'm a member of the [LISA Consortium](https://www.lisamission.org), where I develop a simulation code to model the gravitational wave background from enhanced curvature perturbations arising during inflation and tools for accelerated Bayesian inference of astrophysical sources. I'm also a member of [EAS](https://eas.unige.ch) and [DPG](https://www.dpg-physik.de).

Currently, I am working on three main topics:

1. **[Machine learning for Bayesian Inference](research.md#machine-learning-for-bayesian-inference)**: I am developing [**GPry**](https://github.com/jonaselgammal/GPry), a new method to perform Bayesian inference using Gaussian Process Regression and active sampling to create a surrogate model of the posterior function. This method is particularly useful for slow likelihoods, such as those for CMB (Planck) and astrophysical sources in LISA.
2. **[Reconstructing Curvature Perturbations via SIGWs](research.md#reconstructing-curvature-perturbations-via-sigws)**: As part of the LISA Cosmology Working Group, I am developing [**SIGWAY**](https://github.com/jonaselgammal/SIGWAY), a simulation code to model the gravitational wave background from enhanced curvature perturbations from inflation. 
3. **[Fast PTA inference](research.md#fast-pta-inference)**: I recently started working on Pulsar Timing Array (PTA) data analysis as part of EPTA, where I am trying to speed up Bayesian inference for PTAs using the jax-enabled PTA likelihood from [**Discovery**](https://github.com/nanograv/discovery).

---

Explore:
- [research portfolio](research.md)
- [some useful resources](teaching.md)
- [my resume](resume.md)
