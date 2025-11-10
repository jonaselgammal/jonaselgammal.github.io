---
layout: page
title: Research
permalink: /research/
---

Here you find an overview of my research interests and projects that I have been working on. There is a bunch of other stuff in the pipeline that I haven't had time to write up yet, so check back later for updates!
I am currently working on three main topics:

---

### Machine Learning for Bayesian Inference

![GP surrogate and Active Learning procedure](/assets/img/Figure1.jpg)

Bayesian inference is central to much of modern astrophysics, yet its application to complex models with expensive likelihoods can be computationally prohibitive. To address this, I have been working on a series of methods that use **Gaussian Processes** (GPs) as surrogate models to accelerate Bayesian analysis, particularly in the context of cosmological and gravitational wave data (though the approach is general and can be applied to any expensive likelihood).
I have developed a software package called [**GPry**](https://github.com/jonaselgammal/GPry), which implements these methods and is designed to be a user-friendly and efficient drop-in replacement for existing samplers. The project has been developed with in collabroation with [**Jesús Torrado**](https://jesustorrado.github.io), [**Nils Schöneberg**](https://schoeneberg.github.io), [**Christian Fidler**](https://www.physik.rwth-aachen.de/cms/physik/die-fachgruppe/institute-und-lehrstuehle/~bbxnga/mitarbeiter-campus-/?gguid=PER-7PFRSMS&allou=1), [**Riccardo Buscicchio**](https://riccardobuscicchio.com/about/), and [**Germano Nardini**](https://www.uis.no/en/profile/germano-nardini) and has resulted in three papers:

#### [1] [Surrogate Posterior for Bayesian Inference](https://arxiv.org/abs/2211.02045)

In our foundational work, we introduce a method for emulating the *posterior* distribution using a **Gaussian Processes Regressor as surrogate model**. This innovation allows for direct posterior reconstruction with far fewer function evaluations than traditional MC based methods. We used **active learning** to sample new training points based on the regions where the GP emulation is most uncertain or informative. This method demonstrated how GPs could serve as an efficient surrogate model for Bayesian posteriors, enabling **fast and accurate inference**, especially in problems with expensive likelihoods. We test the methods on a variety of synthetic and real-world problems.

#### [2] [Parallel Acquisition for Active Learning](https://arxiv.org/abs/2305.19267)

Building on previous work, we tackle a key limitation in the active learning step: the sequential nature of **acquisition function optimization**. We propose a parallel approach using Monte Carlo sampling and develop the **NORA** algorithm, which enables the batched proposal of new sample points using a **nested sampler**. Our method allows for efficient batch acquisition using a **ranked pool strategy** that maintains near-optimal information gain while being orders of magnitude more scalable. 

#### [3] [Application to LISA Inference](https://arxiv.org/abs/2503.21871)

Finally, we apply this framework to a concrete and highly demanding application: parameter inference for sources in the upcoming **LISA** gravitational wave observatory. Using [**GPry**](https://github.com/jonaselgammal/GPry), we demonstrate inference speed-ups of **up to two orders of magnitude** compared to state-of-the-art nested sampling algorithms like [nessai](https://nessai.readthedocs.io/en/latest/). This is achieved without compromising on inference accuracy, particularly in regimes where likelihood evaluations are slow (e.g., due to expensive waveform models) as is the case for supermassive black hole binaries.

<img src="/assets/img/gpry_animation.gif" alt="GIF showing the GPry Algorithm" style="max-width: 65%; display:block; margin:auto;">

#### What's next?
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

#### What's next?
We are currently working on extending the analysis to include **non-standard thermal histories** for both constant and changing equation of state which allows for a more realistic modeling of the early universe and its impact on the SIGW background. In addition, we are applying the same analysis to determine whether the **PTA signal** can be explained by a SIGW background.

---

### Fast PTA inference

I recently started working on PTA data analysis as part of EPTA, where I am trying to speed up Bayesian inference for PTAs using the jax-enabled PTA likelihood from [**discovery**](https://github.com/nanograv/discovery). As part of this, I have written a number of interfaces to samplers that I am collecting [**here**](https://github.com/jonaselgammal/discoverysamplers). Currently supported samplers are:
- [nessai](https://nessai.readthedocs.io/en/latest/): Nested sampling with normalizing flows
- [eryn](https://github.com/mikekatz04/Eryn): RJMCMC sampler with parallel tempering
- [GPry](https://gpry.readthedocs.io/en/latest/): See above for details

In addition, I am working on interfacing with [blackjax](https://blackjax-devs.github.io/blackjax/) to enable end-to-end jax-based PTA inference.
