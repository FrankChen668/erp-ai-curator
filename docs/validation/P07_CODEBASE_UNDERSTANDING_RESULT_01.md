# P07 — Codebase / Program → Understand Logic, Support FS, Locate Defects

Date: 2026-08-30

## Verdict

> **CLOSED — REPO-AWARE CODE AGENT DEFAULT; SPECIALIZED CODE-UNDERSTANDING SKILL NOT REQUIRED BY DEFAULT**

For ERP / enterprise-information-system work, a capable repository-aware coding Agent (Codex, Claude Code or equivalent) is already the default tool for:

- understanding an unfamiliar codebase;
- locating where a business behavior is implemented;
- tracing an execution path across modules;
- translating implementation into business/functional explanation;
- supporting FS / technical design documentation;
- reproducing and locating defects;
- writing/running tests and reviewing changes.

The durable value comes from **source-grounded investigation and verification**, not from adding a separate architecture/graph/code-understanding Skill by default.

## Recommended working method

```text
real business question / defect / FS need
→ scope the relevant subsystem
→ locate entry points and authoritative implementation
→ trace control/data flow through code
→ separate observed code facts from inference
→ produce business-rule / flow / interface explanation with source pointers
→ verify critical claims with tests / logs / runtime evidence when available
→ independent review for high-consequence conclusions
```

Do not begin by generating a whole-repository architecture diagram or asking the Agent to summarize everything.

## Evidence

### Large-codebase practice

Current Claude Code guidance for large repositories emphasizes:

- navigating the filesystem / references rather than loading everything;
- lean layered repository guidance;
- scoping the Agent to the relevant subdirectory/domain;
- starting broad only enough to orient, then narrowing to concrete code paths;
- tracing a feature from entry point through interacting components.

This is directly aligned with the ERP job: answer a concrete business/functional question from implementation, not create a generic repo encyclopedia.

### OpenAI harness-engineering practice

OpenAI's Codex engineering experience emphasizes:

- give the Agent a map, not a giant instruction manual;
- keep repository knowledge versioned and locally discoverable;
- make application behavior, logs, metrics and tests legible to the Agent;
- enforce boundaries/invariants mechanically where possible;
- use review/test/feedback loops rather than assuming first-pass correctness.

This supports a source-grounded Agent workflow rather than a separate mandatory code-understanding product layer.

### Practitioner / community evidence

Current Codex practitioner workflows converge on:

- plan and understand before broad edits;
- keep scope small and repository context explicit;
- use tests / manual verification / review artifacts;
- separate planning/review from blind execution when the task is consequential.

Counter-evidence is equally important: users report Agents declaring work complete while later reviews still find real bugs, and patches can introduce adjacent regressions. Therefore Agent explanation/review is not self-validating evidence.

### Legacy-system documentation practice

Current legacy-system documentation guidance treats AI as a way to reverse-engineer business rules, architecture, data flows and interfaces into reviewable artifacts, with domain-expert validation as the gate. This is a strong fit for ERP codebases where business meaning is distributed across old code, schemas and integrations.

## ERP colleague recommendation

### Understand a business behavior

Ask a repo-aware Agent to:

1. locate the relevant entry point using business/domain language;
2. identify authoritative files/classes/functions and data models;
3. trace the path through validation, domain/service logic, persistence and integrations;
4. produce a rule table including condition → action → exception → source location;
5. mark every uncertain interpretation explicitly;
6. point to file/line or symbol evidence for material claims.

### Generate / recover FS or functional explanation

Generate from traced implementation, not model memory:

- purpose / trigger;
- actors or callers;
- inputs / fields;
- validations;
- processing rules;
- state changes;
- outputs;
- integration calls;
- error/exception paths;
- unresolved questions.

Label this as **implementation-recovered behavior** until a business owner validates intended behavior.

### Find a defect

Prefer:

```text
symptom / log / failing scenario
→ reproduce if possible
→ trace responsible path
→ identify root cause and adjacent invariants
→ propose minimal fix
→ run targeted tests + relevant regression checks
→ independent review for consequential changes
```

Do not accept “I found the bug” without concrete repository/runtime evidence.

## When specialist capability may help

A dedicated code-intelligence / graph / architecture capability is justified only if it changes the decision, for example:

- repo scale or language tooling makes normal navigation materially ineffective;
- cross-repository dependency tracing is the actual bottleneck;
- exact symbol/reference analysis is required;
- repeated onboarding/impact-analysis workload makes a maintained architecture index worthwhile.

Even then, it is a navigation accelerator, not a truth source.

## Why no local runtime A/B

The current adoption decision is already stable:

- both major code-agent ecosystems directly support codebase exploration, tracing, debugging and tests;
- large-codebase practice establishes the required context/navigation pattern;
- practitioner counter-evidence establishes the reliability boundary;
- a synthetic local codebase comparison would mostly benchmark transient model performance, not change whether a specialized Skill is required.

Run a local delta only when a real repository presents a specific unresolved navigation, language, permission or reproducibility constraint.

## Stop rationale

P07 answers the colleague decision:

- **Do I need a special code-understanding Skill?** Usually no.
- **What should I use?** A repo-aware code Agent grounded in actual code/tests/logs.
- **How should I produce FS/business explanation?** Trace implementation first, then structure it into reviewable rules and flows with source pointers.
- **What is the main failure mode?** Confident explanations/reviews that are not actually verified and fixes that miss adjacent invariants.

Further generic tool comparison is unlikely to change this recommendation.
