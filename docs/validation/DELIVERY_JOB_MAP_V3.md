# ERP AI Curator — Real Delivery Job Map V3

Date: 2026-08-29

## 1. Purpose

This is not a permanent taxonomy. It is a practical map of recurring ERP / enterprise-information-system delivery jobs used to keep resource curation grounded in actual work.

The unit of validation is not a broad capability label such as `requirements analysis` or `PPT`.

The unit is a concrete job:

> **Given specific project inputs, what must the practitioner produce next, under what constraints, and what AI method/resource can materially improve that delivery?**

A useful validation prompt should normally contain:

- real project context;
- actual input artifacts;
- required output/deliverable;
- time/review constraint;
- verification expectation;
- confidentiality/editability constraints when relevant.

## 2. What generalized ERP delivery people actually do

The following jobs recur across SAP / Oracle / custom enterprise systems. They are representative delivery work, not role quotas.

### J01 — Before a customer workshop

Inputs:

- project scope / RFP;
- existing process or policy documents;
- prior meeting notes;
- system screenshots / forms / sample data.

Need to produce:

- interview/workshop agenda;
- questions by process step / role / exception;
- assumptions and known gaps;
- evidence checklist for the meeting.

AI value to test:

- prepare better questions from actual material;
- detect missing evidence;
- avoid generic interview questionnaires.

### J02 — After a customer interview / workshop

Inputs:

- meeting transcript / notes;
- process diagram;
- RFP / requirement list;
- sample forms / attachments.

Need to produce:

- structured requirement list;
- requirement source / quote / owner;
- open questions and conflicts;
- decisions vs assumptions;
- As-Is / To-Be change points;
- preliminary Fit / Partial / Gap;
- handoff-ready requirement package.

AI value to test:

- extract and cross-check rather than merely summarize;
- preserve provenance;
- expose uncertainty;
- produce reusable delivery artifacts.

### J03 — Turn requirements into a reviewable solution

Inputs:

- confirmed requirements;
- standard-product capability evidence / sandbox observations;
- integration constraints;
- existing architecture / master-data rules.

Need to produce:

- process / system-boundary proposal;
- configuration vs extension vs integration decisions;
- interface / data / role / exception design;
- decision log and unresolved issues;
- reviewable solution document / blueprint.

AI value to test:

- trace requirements to design;
- challenge missing scenarios;
- separate proposal from confirmed fact;
- generate editable diagrams/spec artifacts where useful.

### J04 — Clean and reconcile project data

Inputs:

- Excel / CSV exports;
- master-data templates;
- mapping tables;
- old/new system extracts.

Need to produce:

- cleaned data;
- field mapping;
- duplicate / missing / invalid records;
- cross-table reconciliation;
- exception list;
- repeatable check logic and summary.

AI value to test:

- safely generate scripts/formulas/workflows;
- preserve raw data;
- make checks reproducible and auditable;
- identify when Python/Codex is better than manual Excel/chat.

### J05 — Prepare a customer / steering / internal review deck

Inputs:

- project status;
- requirements / solution content;
- issue/risk list;
- KPI / test / data results;
- prior deck/template.

Need to produce:

- storyline;
- concise management message;
- editable slides;
- diagrams/charts;
- evidence-consistent wording;
- review-ready version quickly.

AI value to test:

- turn source material into structure before beautification;
- preserve editability;
- avoid inventing business claims;
- speed slide iteration.

### J06 — Build a reviewable prototype

Inputs:

- requirements;
- role / state / field rules;
- process / exception scenarios;
- reference UI when available.

Need to produce:

- clickable prototype;
- key states / validations / exceptions;
- review questions;
- revision loop;
- optionally portable/editable artifact.

AI value to test:

- accelerate business clarification, not just visual generation.

### J07 — Prepare test cases / UAT and analyze defects

Inputs:

- confirmed requirements;
- solution design;
- configuration / interface rules;
- test data;
- defect logs / screenshots / traces.

Need to produce:

- test scenarios and expected results;
- requirement-to-test traceability;
- missing edge cases;
- defect triage / evidence summary;
- regression scope.

AI value to test:

- derive tests from evidence;
- cluster defects;
- identify likely missing conditions without claiming root cause without proof.

### J08 — Weekly project coordination / issue closure

Inputs:

- meeting notes;
- issue/action log;
- emails / chat extracts;
- plan and milestone status.

Need to produce:

- decisions;
- actions / owner / due date;
- risks / blockers;
- changes since last review;
- concise status update / follow-up communication.

AI value to test:

- reduce coordination/admin work while preserving accountability and source context.

### J09 — Training / handover / operating material

Inputs:

- final process / configuration / solution;
- system screenshots;
- SOP / issue history;
- test scenarios.

Need to produce:

- training outline;
- user guide / SOP;
- scenario-based exercises;
- FAQ / troubleshooting;
- role-specific operating notes.

AI value to test:

- reuse project evidence into maintainable training artifacts instead of regenerating generic content.

### J10 — Learn and adopt an AI delivery tool

Examples:

- Codex;
- WorkBuddy;
- another Agent/tool only when it changes delivery work.

Need to produce:

- shortest path from setup to one real delivery task;
- current official instructions;
- one or two practical examples;
- safety / data / permission boundary;
- when not to use it.

AI Curator value to test:

- official truth + practical adoption resource;
- avoid feature-tour/tutorial dumping.

## 3. What is not the mainline

The following may still matter, but should not dominate validation unless a real user problem requires them:

- generic ERP module learning with no immediate delivery output;
- AI news collection;
- generic prompt libraries;
- tool feature catalogs;
- broad productivity lists;
- technology research detached from a project task.

## 4. Resource-curation acceptance test

For any delivery job, the final package should help a colleague answer:

1. **What can I use tomorrow on a real project?**
2. **What inputs do I need?**
3. **What output will I get?**
4. **What must still be checked by me / the system / the customer?**
5. **Where is the original tutorial/Skill/tool/method?**
6. **Why is this resource worth my time compared with just asking ChatGPT normally?**

If the package cannot answer these, it is probably too abstract.

## 5. Validation rule

Do not validate every job mechanically.

Prefer:

- real survey/user problems when available;
- otherwise 3–5 high-frequency representative jobs with different artifact types.

Current high-value validation set:

1. J02 — post-workshop requirements package;
2. J04 — data cleaning / reconciliation;
3. J05 — project/customer PPT;
4. J06 — reviewable prototype (existing evidence already available);
5. J10 — Codex and WorkBuddy adoption for delivery.

J03 solution design should follow once J02 evidence is stable because it consumes requirement outputs.

## 6. Anti-drift

Do not turn this map into:

- a fixed product menu;
- one Skill per job;
- a mandatory scenario taxonomy;
- a checklist requiring all jobs to be tested;
- a reason to recommend external tools for every task.

The map exists only to keep ERP AI Curator anchored to real project work.