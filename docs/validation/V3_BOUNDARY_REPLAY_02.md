# V3 Boundary Replay 02 — Real owner work, not scenario inventory

Date: 2026-08-29

Purpose: replay several work requests that have actually appeared in the owner's project work and test whether V3 incorrectly expands into a universal AI consultant.

The descriptions below are reconstructed from project context rather than presented as verbatim quotes.

## B01 — Research a domain/business question

### Work need

Analyze the difference between trade-remedy / anti-dumping style requirements and compliance traceability, and whether a traceability system can provide supporting evidence.

### V3 decision

**Do not trigger the Curator.**

This is a direct domain research / analysis request. The right behavior is to answer the business question, using current sources where needed.

The fact that Web research may be required does not turn this into AI-work-method navigation.

---

## B02 — Turn an existing product briefing into our own project introduction

### Work need

Read an existing product briefing document, understand its structure, then create a project-specific introduction / blueprint.

### V3 decision

**Do not trigger the Curator.**

This is direct document analysis + writing. The user wants the artifact, not a reusable AI method selection.

If later the user asks “what Skill / workflow should our team standardize for repeatedly producing these briefings?”, that becomes a V3 task.

---

## B03 — Design a Slide Reconstruction capability

### Work need

Decide how an existing product should reconstruct an image / scene into editable PowerPoint, including whether to use direct PowerPoint creation, SVG, or an existing exporter.

### V3 decision

**Usually do not trigger.**

If the user is asking for product architecture / SPEC design, this is direct solution design.

Only trigger V3 if the question becomes:

> “Is there an existing AI Skill / Tool / open-source method worth adopting instead of building this ourselves?”

### Additional lesson

Before external discovery, check the **existing stack**.

If the user already has an internal exporter, coding Agent, design pipeline or enterprise-approved tool that can satisfy the capability gap, the product should compare against that baseline before recommending another external dependency.

This is a general leverage principle, not a Slide Reconstruction scenario rule.

---

## B04 — Understand Graph Engineering / Agent architecture

### Work need

Understand whether Graph Engineering is just a way to visualize an existing Agent project or an invasive workflow-governance mechanism, and what is appropriate for understanding a Vibe-Coded project.

### V3 decision

**Trigger AI-work-method navigation.**

The user is choosing among reusable technical approaches.

The correct first step is not to search “Graph Engineering tools”, but to identify the required visibility:

- static structure;
- runtime trace;
- governed workflow.

Default is **Mode C first**: use the lowest-cost inspection that answers the immediate question; only adopt workflow governance when governance is actually needed.

---

## B05 — Design an internal AI training questionnaire

### Work need

Design a short survey for consultants / PMs / developers to capture actual AI use and real work problems for later training.

### V3 decision

**Do not trigger the Curator.**

This is direct product / research design. The correct response is to design the questionnaire.

The answers collected by that questionnaire may later become V3 inputs.

---

## B06 — Find practical AI methods/resources for ERP practitioners

### Work need

Find high-quality existing Skills, Tools, tutorials or working methods that ERP practitioners can actually use, rather than building a large generic tool list.

### V3 decision

**Trigger.**

This is explicitly a reusable AI-work-method / resource-selection problem.

But V3 still does not begin with a resource catalog. It first asks what real work problem the practitioner is trying to improve, then chooses Mode A/B/C.

---

# Findings

## 1. Broadening the audience does not mean broadening the trigger to everything

Generalized ERP scope includes standard ERP, extensions, Java/custom enterprise systems and project/development work.

But most direct work requests still **do not** trigger the Curator.

The trigger is about choosing a reusable AI working approach, not about whether the task belongs to ERP or uses external information.

## 2. Existing-stack sufficiency belongs before external-resource discovery

The V3 question should be:

> “Can general AI **or the user's existing toolchain** already solve this well enough?”

not merely:

> “Can general AI solve this?”

A new external Tool / Skill must beat the real current baseline, including adoption cost.

## 3. This replay supports the V3 boundary but is not user validation

These are owner-origin work requests and reconstructed descriptions. They are useful falsification evidence, not independent REAL_USER proof.
