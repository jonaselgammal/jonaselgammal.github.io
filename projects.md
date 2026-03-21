---
layout: page
title: Projects
permalink: /projects/
---

Here I write about personal projects that I've been working on outside of my main research.

---

## Graphsmith: A Semantic Planner and Compiler for Graph-Based AI Workflows

<a href="https://github.com/jonaselgammal/Graphsmith" style="text-decoration: none;">
  <img src="https://img.shields.io/badge/GitHub-Graphsmith-blue?logo=github" alt="GitHub"/>
</a>

### Motivation

Large language models are remarkably good at understanding what you want to do, but surprisingly unreliable when asked to produce structured artifacts directly. If you ask an LLM to generate a JSON workflow graph — with typed nodes, directed edges, and specific port-level wiring — it will often produce something that *looks* right but fails on details: edges pointing to nonexistent nodes, self-loops, invented types, outputs wired to the wrong ports.

This is a well-known problem in program synthesis: the gap between *understanding intent* and *producing correct structure*. Traditional compilers solved this decades ago by separating concerns — a human writes high-level code, and the compiler handles register allocation, memory layout, and instruction selection. But when we ask LLMs to plan workflows, we tend to skip the compiler entirely and ask the model to emit final executable output in one shot.

I built Graphsmith to explore a different approach: what if we treat the LLM as a *semantic planner* and add a deterministic compiler between intent and execution?

### The core idea

Graphsmith is a system for composing typed, executable skill graphs from natural language goals. The key architectural insight is a clean separation between what the LLM is good at (semantic reasoning) and what it's bad at (structural correctness):

![Graphsmith pipeline](/assets/img/graphsmith_pipeline.svg){: style="max-width: 580px; display: block; margin: 1.5em auto;" }

1. **Semantic decomposition** — An LLM analyzes the goal and classifies it into content transforms (normalize, summarize, extract keywords, ...) and presentation intent (plain output, list, header). This makes semantic decisions explicit before any graph is constructed.

2. **IR generation** — The LLM produces multiple candidate plans as a *semantic intermediate representation* (IR) — a compact structured format that describes steps, data flow, and configuration, but *not* graph-level details like edge addresses or node IDs.

3. **Deterministic scoring** — A rule-based scorer ranks candidates by penalizing unnecessary steps, rewarding required transformations, and checking consistency with the decomposition.

4. **Compilation** — A deterministic compiler lowers the winning IR into a fully-formed executable graph: generating node IDs, constructing edges with correct addressing, mapping outputs, sanitizing types, and validating the DAG structure.

The LLM never touches raw graph syntax. It only reasons about *what to do*, not *how to wire it*.

### What Graphsmith does

The system works end-to-end:

- **Retrieves** candidate skills from a local registry based on the goal
- **Decomposes** the goal into semantic intent
- **Generates** multiple IR candidates (typically 3)
- **Scores and selects** the best candidate deterministically
- **Compiles** the IR into a validated executable graph
- **Validates** structural properties (types, DAG, bindings, outputs)
- **Executes** the graph on a topological runtime with a flat value store

The skill library currently includes 15 skills covering text processing (normalization, summarization, keyword extraction, title casing, word counting, sentiment classification), JSON operations (reshape, field extraction), and formatting (line joining, template rendering, prefix lines).

### Main findings

The development went through roughly 40 sprints, which revealed a clear progression:

**Direct graph emission was brittle.** The first version asked the LLM to produce complete graph JSON directly. This worked for simple cases but broke systematically on multi-step goals. Common failures included invalid edge scopes (`graph_outputs.X` used as a destination), self-loops, invented types, and multi-source port conflicts. These are *structural* errors that no amount of prompt engineering can fully prevent, because they arise from asking the model to serialize a format it doesn't deeply understand.

**Introducing a semantic IR and deterministic compiler was the biggest single improvement.** By separating intent (IR) from structure (compiled graph), an entire class of failures became impossible. Invalid edge addresses, self-loops, type errors, and binding conflicts were eliminated at the architecture level, not by better prompting.

**Candidate reranking helped significantly.** Generating 3 IR candidates instead of 1 and selecting the best via deterministic scoring improved results substantially. The scorer penalizes over-composition (adding formatting steps when not requested), rewards required transformations, and checks output naming consistency. On Llama 3.1 8B, reranking alone improved total pass rate from ~61% to ~92%.

**Decomposition solved the remaining systematic failures.** Even with reranking, some goals failed because all 3 candidates made the same semantic mistake (e.g., using `join_lines` for a "header" task). Adding a decomposition stage — where the LLM first classifies the goal into content transforms and presentation intent — regularized these cases by making the contract explicit before IR generation.

### Empirical results

The evaluation uses 36 goals across three sets of increasing difficulty:

| Set | Goals | Claude Haiku | Llama 3.1 8B |
|-----|-------|-------------|--------------|
| Benchmark | 9 | 9/9 | 8-9/9 |
| Holdout | 15 | 15/15 | 12-14/15 |
| Challenge | 12 | 12/12 | 10-12/12 |
| **Total** | **36** | **36/36 (100%)** | **~31-34 (86-94%)** |

On Claude Haiku, the system achieves perfect accuracy: every goal produces a valid, semantically correct plan. On Llama 3.1 8B, the architecture still works well but hits a noise floor — remaining failures are stochastic output-naming errors that vary between runs.

A candidate-level analysis showed that on both models, the deterministic scorer already makes the optimal selection among available candidates. The reranking headroom is effectively zero — meaning the bottleneck is upstream semantic planning quality, not downstream selection. This strongly suggests that the next improvement would need to come from better models or learned planning components, not from more hand-written rules.

### Reflection

This project started as an exploration of whether LLMs could work directly with graph-structured programs — composing typed, executable workflows from natural language. The answer turned out to be *yes, but only if you don't ask the LLM to produce the graphs directly*.

The most important lesson was architectural: the LLM should reason about semantics while a deterministic system handles structure. This isn't a novel insight in the abstract — it's essentially what compilers have always done — but applying it to LLM-based planning required building the right intermediate representation, the right compilation rules, and the right evaluation infrastructure to measure what actually worked.

By the end, the system looked much more like a compiler toolchain than a one-shot prompt:

- A *front-end* (decomposition) that analyzes intent
- An *IR* that captures semantics without committing to structure
- *Optimization passes* (scoring, reranking) that select the best plan
- A *back-end* (compiler) that lowers IR to an executable target
- *Validation* that catches structural errors before execution

Some directions I'd like to explore next:

- **Weak-model optimization** — the 86-94% range on Llama suggests room for learned decomposition or scoring components
- **Broader skill libraries** — the current 15 skills cover text and JSON; extending to network, storage, and multi-modal skills would test the architecture's generality
- **Program editing** — currently plans are generated from scratch each time; incremental editing of existing plans would be more practical for real use
- **Learned planning** — the candidate-level dataset pipeline is in place; training a small model to improve decomposition or scoring is a natural next step

The code is available at [github.com/jonaselgammal/Graphsmith](https://github.com/jonaselgammal/Graphsmith).
