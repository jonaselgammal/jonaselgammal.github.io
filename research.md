---
layout: page
title: Research
description: Research by Jonas El Gammal in scientific machine learning, Bayesian inference, cosmology, LISA, and Pulsar Timing Array analysis.
permalink: /research/
---

<p class="page-lede">My research connects cosmology and gravitational-wave astronomy with Bayesian inference, scientific machine learning, and high-performance scientific software.</p>

<nav class="section-nav" aria-label="Research topics">
  <strong>On this page</strong>
  <a href="#machine-learning-for-bayesian-inference">Machine learning for Bayesian inference</a>
  <a href="#reconstructing-curvature-perturbations-via-scalar-induced-gws">Scalar-induced gravitational waves</a>
  <a href="#fast-pta-inference">Fast PTA inference</a>
  <a href="#statistical-diagnostics-for-the-pta-gravitational-wave-background">PTA statistical diagnostics</a>
</nav>

---

### Machine Learning for Bayesian Inference

![GP surrogate and Active Learning procedure](/assets/img/Figure1.jpg)

Bayesian inference is central to much of modern astrophysics, yet its application to complex models with expensive likelihoods can be computationally prohibitive. To address this, I have been working on methods that use **Gaussian processes** (GPs) as surrogate models to accelerate Bayesian analysis, particularly for cosmological and gravitational-wave data. The approach is general and can be applied to other expensive likelihoods.

I developed [**GPry**](/gpry/), which implements these methods as a user-friendly alternative to conventional samplers when likelihood evaluations dominate the computational cost. The project was developed in collaboration with [**Jesús Torrado**](https://jesustorrado.github.io), [**Nils Schöneberg**](https://schoeneberg.github.io), [**Christian Fidler**](https://www.physik.rwth-aachen.de/cms/physik/die-fachgruppe/institute-und-lehrstuehle/~bbxnga/mitarbeiter-campus-/?gguid=PER-7PFRSMS&allou=1), [**Riccardo Buscicchio**](https://riccardobuscicchio.com/about/), and [**Germano Nardini**](https://www.uis.no/en/profile/germano-nardini), and has resulted in three papers:

#### [1] [Surrogate Posterior for Bayesian Inference](https://arxiv.org/abs/2211.02045)

In our foundational work, we introduce a method for emulating the *posterior* distribution using a **Gaussian Processes Regressor as surrogate model**. This innovation allows for direct posterior reconstruction with far fewer function evaluations than traditional MC based methods. We used **active learning** to sample new training points based on the regions where the GP emulation is most uncertain or informative. This method demonstrated how GPs could serve as an efficient surrogate model for Bayesian posteriors, enabling **fast and accurate inference**, especially in problems with expensive likelihoods. We test the methods on a variety of synthetic and real-world problems.

#### [2] [Parallel Acquisition for Active Learning](https://arxiv.org/abs/2305.19267)

Building on previous work, we tackle a key limitation in the active learning step: the sequential nature of **acquisition function optimization**. We propose a parallel approach using Monte Carlo sampling and develop the **NORA** algorithm, which enables the batched proposal of new sample points using a **nested sampler**. Our method allows for efficient batch acquisition using a **ranked pool strategy** that maintains near-optimal information gain while being orders of magnitude more scalable. 

#### [3] [Application to LISA Inference](https://arxiv.org/abs/2503.21871)

Finally, we apply this framework to a concrete and highly demanding application: parameter inference for sources in the upcoming **LISA** gravitational wave observatory. Using [**GPry**](https://github.com/jonaselgammal/GPry), we demonstrate inference speed-ups of **up to two orders of magnitude** compared to state-of-the-art nested sampling algorithms like [nessai](https://nessai.readthedocs.io/en/latest/). This is achieved without compromising on inference accuracy, particularly in regimes where likelihood evaluations are slow (e.g., due to expensive waveform models) as is the case for supermassive black hole binaries.

<img src="/assets/img/gpry_animation.gif" alt="GIF showing the GPry Algorithm" style="max-width: 65%; display:block; margin:auto;">

#### Current direction
The GPry framework is still in its early stages, and there are many avenues for future work. Some potential directions include:
- **Speeding up the GP model**: We are currently using a simple GP implementation which is based on [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html), but which does not fully take advantage of hardware acceleration like thread parallelization and GPUs. We are currently working on implementing the core functionality of the GPR in [jax](https://github.com/jax-ml/jax), which natively supports GPU and TPU acceleration.
- **Interfacing**: Although [**GPry**](https://github.com/jonaselgammal/GPry) is designed to be a drop-in replacement for existing samplers, we are currently working on interfacing it with codes that are widely used in the community.

---

### Reconstructing Curvature Perturbations via scalar-induced GWs

<img src="/assets/img/detector_sensitivity.svg" alt="Detector Sensitivity to USR phase" style="max-width: 85%; display:block; margin:auto;">

A central goal in modern cosmology is to probe the physics of the very early universe, especially inflation, through indirect observables. One promising avenue is the study of **scalar-induced gravitational waves (SIGWs)**, which can carry imprints of enhanced primordial **curvature perturbations**. In this context, our recent work explores how upcoming gravitational wave experiments, such as LISA, can be used to reconstruct the **small-scale curvature power spectrum** and constrain early-universe models.

In [**this paper**](https://arxiv.org/abs/2501.11320), which was produced for the **LISA Cosmology Working Group**, we explore how the Laser Interferometer Space Antenna (LISA) can be used to reconstruct small-scale primordial curvature perturbations by observing the scalar-induced gravitational wave (SIGW) background. These gravitational waves originate from enhanced scalar fluctuations generated during non-standard inflationary phases, such as **ultra-slow-roll**.

We propose and compare three different reconstruction strategies:

- **Agnostic (binned)**: A flexible method that reconstructs the curvature power spectrum in frequency bins without assuming a specific model.
- **Template-based**: Uses physically motivated templates based on common inflationary scenarios.
- **Ab initio (first-principles)**: Directly infers inflationary parameters using theoretical models like single-field ultra-slow-roll inflation.

Our study also considers extensions such as non-standard thermal histories and primordial non-Gaussianities. The analysis is implemented in the open-source **[SIGWAY](https://github.com/jonaselgammal/SIGWAY)** package, which interfaces with gravitational wave data pipelines for signal inference.

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem;">
  <img src="/assets/img/usr_posterior_predictive_potential.svg" alt="Posterior Predictives Inflaton Potential" style="max-width: 100%; height: auto; width: 330px;">
  <img src="/assets/img/usr_posterior_predictive_pzeta.svg" alt="Posterior Predictives Pzeta" style="max-width: 100%; height: auto; width: 330px;">
  <img src="/assets/img/usr_posterior_predictives_omega_gw.svg" alt="Posterior Predictives Omega GW" style="max-width: 100%; height: auto; width: 330px;">
</div>

#### Current direction
We are currently working on extending the analysis to include **non-standard thermal histories** for both constant and changing equation of state which allows for a more realistic modeling of the early universe and its impact on the SIGW background. In addition, we are applying the same analysis to determine whether the **PTA signal** can be explained by a SIGW background.

---

### Fast PTA inference

Pulsar Timing Arrays (PTAs) are a powerful tool for detecting low-frequency gravitational waves by monitoring the precise timing of millisecond pulsars. However, Bayesian inference for PTA data is notoriously expensive, often requiring millions of likelihood evaluations due to the high dimensionality of the parameter space and the complexity of the noise models involved.

To address this, I have developed [**discoverysamplers**](https://github.com/jonaselgammal/discoverysamplers), a Python package that provides lightweight bridge interfaces connecting [**Discovery**](https://github.com/nanograv/discovery) (a JAX-enabled PTA likelihood code developed by NANOGrav) to various state-of-the-art sampling backends. The package is designed to be modular and easy to use, allowing researchers to seamlessly switch between different samplers while maintaining a consistent interface.

Currently supported samplers include:
- [**Eryn**](https://github.com/mikekatz04/Eryn): Ensemble MCMC with parallel tempering and reversible-jump support
- [**Nessai**](https://nessai.readthedocs.io/en/latest/): Flow-based nested sampling with importance sampling
- [**JAX-NS**](https://github.com/Joshuaalbert/jaxns): Pure JAX nested sampling with native GPU support
- [**GPry**](https://gpry.readthedocs.io/en/latest/): Gaussian process emulation via the Cobaya framework (see above)

The package uses a unified prior specification format and handles all the necessary transformations between Discovery's callable interface and each sampler's expected API. This makes it straightforward to benchmark different sampling strategies and identify the most efficient approach for a given PTA dataset.

#### Current direction
We are currently working on extending discoverysamplers to support additional backends, including [blackjax](https://blackjax-devs.github.io/blackjax/) for end-to-end JAX-based inference with gradient-based samplers like NUTS. The goal is to fully leverage hardware acceleration (GPUs/TPUs) to achieve significant speed-ups in PTA parameter estimation.

---

### Statistical diagnostics for the PTA gravitational-wave background

One of the central open questions in PTA science is whether the observed nanohertz gravitational-wave background is of **astrophysical** origin, most likely a population of supermassive black hole binaries, or whether it could instead be sourced by the **early Universe**. In current work with **Chiara Cecchini**, **Gabriele Franciolini**, and **Mauro Pieroni**, I study whether this question can be answered directly from the **statistics of the signal** rather than from detailed population or cosmological modeling.

The paper makes two closely related points. First, PTA data must be **whitened** before any statistical test is meaningful. The built-in Hellings-Downs correlations otherwise generate false positives even under a perfectly Gaussian and isotropic null hypothesis. Second, after whitening, the PTA response itself becomes the main limitation: because each pulsar averages the signal over a broad region of the sky, the response rapidly **Gaussianizes** the signal, even when the underlying source population is discrete and intrinsically non-Gaussian.

In practice, this means that once the overall signal amplitude is estimated from the same realization, simple model-agnostic tests of non-Gaussianity lose almost all of their discriminatory power. What remains is mostly a mismatch in the overall variance, and that information is removed by the scale fit itself. Our conclusion is therefore fairly negative but important: in an idealized signal-dominated setup, PTAs are largely **insensitive to non-Gaussianity** in a model-agnostic sense, precisely because the broad antenna patterns wash the signal out. The current preprint is available on [arXiv:2605.05157](https://arxiv.org/abs/2605.05157).

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; align-items: flex-start;">
  <div style="max-width: 360px; text-align: center;">
    <a href="/assets/img/pta_whitening_qq.pdf">
      <img src="/assets/img/pta_whitening_qq.png" alt="QQ plot showing false positives without whitening and good calibration after whitening" style="max-width: 100%; height: auto;">
    </a>
    <p style="font-size: 0.92rem; margin-top: 0.5rem;">Without whitening, even a Gaussian isotropic null produces miscalibrated p-values. Whitening restores the expected null behavior.</p>
  </div>
  <div style="max-width: 360px; text-align: center;">
    <a href="/assets/img/pta_scale_estimation_hist_multisrc.pdf">
      <img src="/assets/img/pta_scale_estimation_hist_multisrc.png" alt="Scale estimation and antenna-pattern broadening wash out non-Gaussian signal information in PTAs" style="max-width: 100%; height: auto;">
    </a>
    <p style="font-size: 0.92rem; margin-top: 0.5rem;">After scale normalization, the broad true PTA antenna pattern drives the whitened distributions close to the Gaussian null, while narrower synthetic responses retain more visible non-Gaussian structure.</p>
  </div>
</div>
