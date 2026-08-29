# ERP AI Curator — Delivery Scenario Validation V3

Date: 2026-08-29

## 1. Correction

Validation must stay anchored to **what ERP / enterprise-system practitioners actually do in delivery**, not broad capability labels.

A prompt such as `requirements analysis`, `data processing` or `PPT creation` is still too abstract.

The useful unit is a concrete delivery job:

```text
project situation
+ real input artifacts
+ next required deliverable
+ time/review/privacy constraints
→ AI working approach
→ external resources worth using
```

Current practical job authority:

- `DELIVERY_JOB_MAP_V3.md`

This job map is a validation aid, not a permanent taxonomy.

## 2. Mainline jobs

High-value representative jobs are:

### J02 — Post-workshop requirements package

A consultant has workshop notes/transcript, As-Is process material, RFP/requirement list, attachments and screenshots. The next morning they must deliver a reviewable package with requirements, provenance, open questions, conflicts/assumptions, As-Is→To-Be change points, preliminary Fit/Gap with verification boundary and a traceability foundation.

Current execution protocol:

- `DELIVERY_J02_POST_WORKSHOP_REQUIREMENTS.md`

### J04 — Data cleaning / mapping / reconciliation

A consultant receives multiple Excel/CSV/system exports and must produce cleaned data, mapping, duplicates/missing/invalid records, cross-table reconciliation, exception list and repeatable checks without destroying raw data.

### J05 — Customer / steering PPT

The team has real requirements/solution/status/data/issue material and must turn it into an editable, evidence-consistent review deck quickly.

### J06 — Reviewable prototype

Confirmed requirements/rules must become a clickable prototype containing roles, fields, states, validation and exceptions for customer review. Historical T01 evidence already exists; do not repeat without a fresh question.

### J10 — Codex / WorkBuddy adoption for delivery

The practitioner does not need a feature tour. They need the shortest reliable path from setup to one real delivery job, with current official instructions, practical examples, limits and data/safety boundaries.

## 3. Adjacent jobs

Other recurring jobs include:

- workshop preparation;
- solution / blueprint design;
- test/UAT/defect analysis;
- weekly issue/action closure;
- training / handover.

Use them when a real user/survey problem makes them relevant.

Do not test them merely to fill coverage.

## 4. Practicality rule

A recommended resource is strong only if its original evidence lets us answer most of:

1. What real project input goes in?
2. What exact workflow does the practitioner follow?
3. What usable project artifact/result comes out?
4. What must still be verified by consultant/customer/system evidence?
5. What adoption/privacy/setup cost exists?
6. Why is this better than ordinary ChatGPT use?

Resources that cannot answer these are usually too abstract.

## 5. Resource-source behaviour

Useful evidence may come from:

- official/original documentation;
- GitHub Tool/Skill/project;
- practitioner article/case;
- video/tutorial;
- workshop/template;
- community failure/counter-evidence.

No platform quota.

For current product facts, prefer current original/official evidence.

For adoption and project use, practitioner evidence is valuable when it contains actual steps, inputs/outputs, screenshots/templates, constraints or failure modes.

Chinese content is useful only when it adds this practical value.

## 6. Tool-onboarding rule

Codex, WorkBuddy and similar tools are tested through delivery tasks.

A useful package should answer:

- how to set up currently;
- the first project job to try;
- exact input/output example;
- how to review the result;
- safety/privacy boundary;
- when another tool or plain ChatGPT is enough.

Do not build tutorial catalogs.

## 7. Adapter policy

Source adapters remain optional acquisition capabilities.

Current pilot chain:

- WeChat search → original article reader.

Use only when a practitioner-evidence gap could materially improve the package.

Do not mechanically search every installed platform.

Bilibili/Xiaohongshu remain non-blocking.

## 8. Output boundary

Return a small share-worthy package.

External resources and Curator synthesis must be clearly separated.

A good result should make a colleague think:

> **I can use this on tomorrow's project work.**

Not merely:

> `I learned that AI can help with this topic.`

## 9. Current next test

Execute **J02 Post-Workshop Requirements Package** only.

This is a curation-quality test, not an adapter A/B test.

After J02, cloud reviews whether the package is actually useful before selecting another job.

Do not automatically advance through all jobs.

## 10. Anti-drift

Stop if work turns into:

- generic ERP module learning as the mainline;
- broad ability labels detached from actual delivery artifacts;
- generic prompt libraries;
- feature catalogs;
- mandatory platform coverage;
- endless validation variants;
- measuring link count rather than delivery usefulness;
- one Skill per job;
- more validation documents without better resources.

The goal is to accumulate a small number of genuinely reusable AI delivery resources and practices around real project work.