---
layout: page
title: GPry — Bayesian Inference for Expensive Likelihoods
description: GPry is an open-source Python framework that uses Gaussian-process surrogate modelling and active learning to accelerate Bayesian inference with computationally expensive likelihoods.
permalink: /gpry/
schema_type: SoftwareSourceCode
software_name: GPry
repository: https://github.com/jonaselgammal/GPry
---

<p class="page-lede"><strong>GPry</strong> is an open-source Python framework for Bayesian inference with computationally expensive likelihoods. It uses Gaussian-process surrogate modelling and active learning to reduce the number of likelihood evaluations needed to reconstruct posterior distributions and estimate model evidence.</p>

<div class="action-row">
  <a class="button-link button-link--primary" href="https://gpry.readthedocs.io/en/latest/">Read the documentation</a>
  <a class="button-link" href="https://github.com/jonaselgammal/GPry">View the source</a>
  <a class="button-link" href="https://pypi.org/project/gpry/">Install from PyPI</a>
</div>

```bash
python -m pip install gpry
```

## What problem does GPry solve?

Conventional Monte Carlo methods can require many evaluations of a likelihood or posterior. When each evaluation is slow—for example because it calls a cosmological solver or gravitational-wave waveform model—the resulting inference can become prohibitively expensive.

GPry learns a Gaussian-process surrogate of the log-posterior. An active-learning loop chooses new evaluations where they are most useful, progressively improving the surrogate until its convergence criteria are met. The reconstructed posterior can then be sampled at much lower cost than repeatedly evaluating the original function.

![Animated progress of the GPry active-learning algorithm](/assets/img/gpry_animation.gif){: .figure-contained }

## When is it a good fit?

GPry is designed primarily for:

- deterministic, sufficiently smooth log-likelihood or log-posterior functions;
- problems where individual likelihood evaluations are expensive enough for surrogate construction to pay off;
- low- to moderate-dimensional parameter spaces;
- marginal posterior inference and model-evidence estimation.

It is less suitable for strongly stochastic likelihoods, very high-dimensional spaces, or difficult widely separated modes without additional problem-specific care. These limitations are part of choosing the method responsibly, not implementation footnotes.

## Minimal interface

```python
from gpry import Runner

runner = Runner(log_likelihood, bounds, checkpoint="output/")
runner.run()
```

GPry also integrates with [Cobaya](https://cobaya.readthedocs.io/) for richer model definitions and established cosmology workflows.

## Evidence and publications

The framework and its applications are documented in three primary papers:

1. [Fast and Robust Bayesian Inference using Gaussian Processes with GPry](https://arxiv.org/abs/2211.02045) — the core surrogate-posterior method.
2. [Parallelized Acquisition for Active Learning using Monte Carlo Sampling](https://arxiv.org/abs/2305.19267) — NORA, the parallel batch-acquisition method.
3. [Accelerating LISA inference with Gaussian processes](https://arxiv.org/abs/2503.21871) — validation on expensive LISA source inference, including comparisons with nested sampling.

Performance gains depend on dimensionality, posterior geometry, likelihood cost, convergence settings, and the comparison method. The papers provide the relevant experimental conditions; GPry should not be read as a universal replacement for MCMC or nested sampling.

## People and citation

GPry was developed by [Jonas El Gammal](/), [Jesús Torrado](https://jesustorrado.github.io/), [Nils Schöneberg](https://schoeneberg.github.io/), and [Christian Fidler](https://www.physik.rwth-aachen.de/). If you use GPry, please cite the core method and the relevant acquisition or application paper. The repository contains current citation guidance and release information.

<p class="last-updated">Last reviewed: August 2026</p>
