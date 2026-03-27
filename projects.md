---
layout: page
title: Projects
permalink: /projects/
---

Here I write about personal projects that I've been working on outside of my main research.

---

## Graphsmith: AI-Native Planning and Execution with Graph-Based Programs

<a href="https://github.com/jonaselgammal/Graphsmith" style="text-decoration: none;">
  <img src="https://img.shields.io/badge/GitHub-Graphsmith-blue?logo=github" alt="GitHub"/>
</a>

### Motivation

Large language models are very good at understanding what you want, but still unreliable when asked to directly emit a complete structured artifact such as a workflow graph, a typed JSON program, or a large plan with precise wiring. They often produce something that looks plausible while still being wrong in subtle but important ways: missing bindings, inconsistent ports, invalid control flow, invented capabilities, or outputs that do not match the intended contract.

Graphsmith explores a different approach. Instead of asking the model to directly serialize executable structure, it treats the model as a semantic planner and surrounds it with a deterministic planning and execution substrate. The model proposes intent. Graphsmith compiles, validates, repairs, executes, traces, and learns reusable structure from the result.

### The core idea

Graphsmith turns natural-language goals into typed executable graphs. The key architectural move is to separate semantic reasoning from structural correctness:

![Graphsmith pipeline](/assets/img/graphsmith_pipeline.svg){: style="max-width: 760px; display: block; margin: 1.5em auto;" }

The flow is now roughly this:

1. **Goal policy and decomposition** — the system derives policy constraints and a coarse semantic decomposition before building any executable structure.
2. **Candidate retrieval** — Graphsmith searches both local and remote skill registries for reusable capabilities.
3. **IR planning** — the model proposes candidate plans in a typed intermediate representation rather than directly emitting raw graph structure.
4. **Deterministic compilation and repair** — Graphsmith lowers IR into a graph, normalizes it, validates it, and performs bounded structural repair where possible.
5. **Execution and tracing** — the runtime executes guarded branches and lowered loop regions while recording traces for inspection.
6. **Closed-loop reuse** — missing capabilities can trigger bounded skill generation, promotion, and re-entry into planning.

This makes the system feel much more like a compiler toolchain than a one-shot prompting setup.

### What Graphsmith does now

The current architecture supports:

- typed IR planning rather than raw graph emission
- guarded execution and structural branch handling
- bounded loop lowering and execution
- deterministic graph validation and normalization
- local region repair and runtime-trace-guided repair
- bounded closed-loop skill generation
- promotion signals mined from traces
- local registries and a hosted remote skill registry foundation
- frontier and stress harnesses for probing generalization limits

The important point is that Graphsmith is no longer only a planner for a narrow text-processing benchmark. It is becoming a substrate for AI-native program construction where the graph is easy for a model to inspect at multiple levels: whole-plan intent, a branch or loop region, or an individual skill contract.

### Why this is interesting

What I find most promising is not just that Graphsmith can sometimes produce a good graph. It is that the graph representation is inspectable and editable in a way that seems much more model-friendly than raw source code or raw execution traces.

A model can:

- look at the full graph and understand the broad intent
- zoom into one region and inspect only the relevant substructure
- reason about a skill contract without re-reading the entire program
- repair a local failure without regenerating everything
- eventually reuse or promote working subgraphs as new skills

That suggests a path toward systems where planning, reuse, and repair become increasingly compositional instead of being repeated from scratch for every task.

### Where it is now

Graphsmith is already a serious experimental substrate, but it is not yet a truly general-purpose programming system.

It still works best when:

- the task can be decomposed into bounded reusable skills
- repair can be local rather than global
- the runtime semantics are simple enough to stay inspectable
- missing capabilities can be bridged by bounded synthesis or reuse

What is still missing for real open-ended generalization is richer graph-native skill synthesis, stronger region-level repair, a more expressive runtime for state and effects, and deeper integration with real code and tool environments.

### Future direction

The long-term vision is not "add one more heuristic for one more benchmark task." It is to make Graphsmith into a genuinely AI-native programming substrate.

The next major steps I care about are:

- **Graph-native skill synthesis** — generated skills should become reusable subgraphs with tests and contracts, not mostly one-step templates.
- **Region-level repair** — loops, branches, and failing subplans should be regenerated locally as a normal part of execution.
- **Richer runtime semantics** — bindings, structured errors, state, effects, and reusable subgraphs need to become first-class.
- **Tool and code integration** — files, tests, shell commands, APIs, and code edits should become native planning/execution environments.
- **Trust-aware remote reuse** — a shared skill network should eventually use provenance, validation history, and policy, not just retrieval.

That is the direction that would move Graphsmith from “interesting structured planner” toward “tell it to build something real, and it can plan, compose, synthesize, debug, and reuse its own intermediate work.”

The code is available at [github.com/jonaselgammal/Graphsmith](https://github.com/jonaselgammal/Graphsmith).
