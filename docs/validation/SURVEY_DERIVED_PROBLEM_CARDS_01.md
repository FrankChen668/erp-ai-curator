# Survey-derived Delivery Problem Cards 01

Date: 2026-08-30
Source: `调查数据统计-泛ERP项目管理AI应用训前调研-文本_20260828133530.xlsx`

## 1. Evidence boundary

This export may contain platform-side summarization or wording cleanup. Therefore:

- closed-choice questions are treated as direct aggregate evidence;
- individual free-text answers are treated as semantic evidence, not necessarily verbatim user voice;
- verbose or polished wording is not trusted by itself;
- repeated work patterns across respondents carry more weight than any single polished answer;
- no personal names, accounts, emails or other identifiers are retained here.

The workbook contains 83 responses. Under Q18, 78 respondents supplied at least one non-empty concrete-work-problem entry after excluding obvious `无 / - / blank` values, yielding 224 non-empty issue slots. These counts are analysis aids, not product scores.

## 2. Strong aggregate signals

### Audience

- Implementation consultant: 37 / 83 (44.58%)
- Project manager: 30 / 83 (36.14%)
- Developer: 8 / 83 (9.64%)
- Presales: 5 / 83 (6.02%)

### Current AI usage

- Frequent use: 51.81%
- AI already a daily work tool: 27.71%
- Current common uses: research/Q&A 93.98%, document writing/summarization 81.93%, PPT/reporting 71.08%, requirements/solution support 55.42%, data analysis 51.81%.

This means the training problem is not primarily “introduce AI”. Many respondents already use it; the problem is converting AI use into reliable delivery output.

### Main friction

- AI output quality unstable: 63.86%
- membership/cost issue: 49.40%
- lack of real project cases and methods: 44.58%
- data security/environment constraints: 38.55%

### What respondents most want from training

- AI in project implementation: 84.34%
- AI in project management: 62.65%
- Agent working methods and practice: 50.60%

### Typical project inputs

- Word/PDF: 85.54%
- PPT: 65.06%
- Excel: 60.24%
- meeting minutes / transcript: 59.04%
- system screenshots: 40.96%
- code / logs: 26.51%

First-principles implication:

> The core product unit should be **project material → concrete work action → reviewable delivery artifact**, not an abstract AI capability category.

## 3. Repeated survey-derived problem cards

These are normalized problem cards derived from repeated semantics in the free-text responses. They are not a permanent taxonomy.

### P01 — Meeting / workshop → requirement package

**Situation**

A consultant finishes a customer workshop and has recordings/minutes, existing process documents, RFP/requirement lists and attachments.

**Job**

Turn them into:

- structured requirement list;
- open questions;
- omissions/conflicts;
- current-state problems;
- preliminary Fit/Gap / blueprint inputs;
- traceable source references.

**Observed pain**

Manual consolidation is slow; AI summaries omit context or hallucinate; long conversations lose context.

**Resource search should target**

Source-grounded requirement extraction, BA/PM Skills, requirements-interviewer methods, traceability workflows, project-practice tutorials and reusable templates.

---

### P02 — Requirements → high-quality PRD / FS / functional design

**Situation**

Requirements are roughly understood, but a consultant/PM needs a reviewable PRD, FS or functional-design document.

**Job**

Generate a structured first draft while preserving business rules, exceptions, permissions, states, open decisions and source evidence.

**Observed pain**

Simple prompts produce generic documents; some respondents report PRDs taking weeks and AI output still requiring heavy rewriting.

**Resource search should target**

PM/BA Skills, PRD workflows, requirements-to-spec methods, review checklists, prompt templates with source grounding, practitioner examples.

---

### P03 — Requirements / rules → clickable prototype / UI demo

**Situation**

The project needs a clickable prototype for requirement clarification or solution review.

**Job**

Turn requirements, fields, roles, states and exceptions into an interactive prototype that can be reviewed and iterated.

**Observed pain**

Consultants know AI can generate UI but do not know which tools/Skills/workflows produce deliverable prototypes rather than pretty mockups.

**Resource search should target**

Figma Make / Lovable / local-Agent HTML prototype workflows, PM prototype Skills, Chinese practical tutorials, review/iteration methods.

---

### P04 — Business logic → editable process / architecture diagram

**Situation**

Consultants repeatedly need business process diagrams, end-to-end flows, architecture diagrams or Visio/draw.io deliverables.

**Job**

Generate an editable diagram from requirements/blueprints or reuse and adapt prior-project diagrams.

**Observed pain**

Manual drag/resize/formatting consumes time; prior diagrams exist but are hard to reuse consistently.

**Resource search should target**

Draw.io/BPMN/Visio Skills, MCPs, reusable diagram prompts/workflows, diagram-from-text methods, practical examples with editable output.

---

### P05 — Requirements / blueprint / project status → customer-ready PPT

**Situation**

A consultant/PM must produce a presales solution deck, blueprint deck, phase report, steering report or test-report presentation.

**Job**

Turn actual source material into a concise, logically correct, editable presentation with appropriate diagrams/screenshots/data.

**Observed pain**

“One-click PPT” is often visually or semantically weak; users spend substantial time rewriting content and beautifying slides.

**Resource search should target**

AI PPT tools, editable-slide workflows, storyline methods, prompt/Skill examples, practitioner cases, diagram/chart generation and quality-review methods.

---

### P06 — Excel / CSV / system export → clean, reconcile, validate

**Situation**

Project teams receive master data, migration data, reports or extracts across multiple files.

**Job**

Deduplicate, clean, map fields, compare datasets, generate SQL/Excel reconciliation logic, locate exceptions and produce an auditable result.

**Observed pain**

Formula/SQL writing is repetitive; migration validation and cross-file checking are time-consuming; correctness must be reviewable.

**Resource search should target**

Codex/Agent spreadsheet workflows, Python/data Skills, reconciliation templates, Excel/CSV best practices, reproducibility and data-safety guidance.

---

### P07 — Codebase / program → understand logic, generate FS, find defects

**Situation**

A consultant/developer inherits an existing SAP/Oracle/custom-system codebase or enhancement.

**Job**

Understand structure, business logic, call chains, classes/functions, potential enhancements, bugs and performance issues; sometimes reverse-generate functional logic/specification.

**Observed pain**

Manual code reading is slow; generic chat requires repeatedly supplying dependent functions/files; business issues may be hard to reproduce.

**Resource search should target**

Codex/Claude Code workflows, codebase exploration Skills/MCPs, architecture mapping, debugging methods, SAP/EBS-specific developer practice when available.

---

### P08 — Error/log/screenshot → root cause and official evidence

**Situation**

During implementation/operations, teams face SAP standard errors, interface failures, SQL/data issues, logs or screenshots.

**Job**

Identify likely root cause, narrow investigation, locate official/current evidence and propose verification steps.

**Observed pain**

Troubleshooting depends heavily on scarce technical experts; AI may hallucinate fixes or miss environment context.

**Resource search should target**

Log-analysis workflows, SAP/Oracle support-search methods, screenshot/OCR issue analysis, evidence-grounded troubleshooting, safe agent automation.

---

### P09 — Blueprint / design → completeness and adversarial review

**Situation**

A solution/blueprint exists but must be reviewed before customer sign-off or development handoff.

**Job**

Check missing scenarios, business rules, interfaces, data, permissions, exceptions, dependencies and unresolved decisions.

**Observed pain**

Output depends on personal experience; AI can sound plausible while missing business-critical gaps.

**Resource search should target**

Solution-review Skills, architecture/design-review methods, Fit-Gap checklists, adversarial review prompts with real-source grounding, practitioner frameworks.

---

### P10 — Requirement / blueprint → test scenarios, test cases, test data

**Situation**

UAT/SIT planning must cover many customer-specific business details.

**Job**

Generate realistic scenarios/cases/data, preserve traceability to requirements and help classify/analyze defects.

**Observed pain**

Manual test design misses cases; generic AI cases are too shallow; customer-specific details can number in the hundreds.

**Resource search should target**

Requirements-to-test Skills, UAT generation methods, test-data workflows, automation tutorials and practitioner cases.

---

### P11 — System screenshots / steps → operation manual / training material

**Situation**

Before go-live, consultants prepare department-specific manuals, training PPTs and FAQs.

**Job**

Capture/organize screenshots, annotate steps, generate descriptions and keep text/images synchronized as the system changes.

**Observed pain**

Manual screenshot/annotation/layout is repetitive; version drift between screenshots and text creates rework.

**Resource search should target**

Screenshot-to-document workflows, SOP/manual generation tools, annotation automation, document-maintenance methods and training-content generation.

---

### P12 — Daily project inputs → weekly report / progress / risk / action closure

**Situation**

PMs collect updates from multiple consultants, meeting actions, issue lists and plans.

**Job**

Generate weekly/monthly reports, progress summaries, risk/issues, task decomposition and follow-up actions while checking data consistency.

**Observed pain**

Manual consolidation is repetitive; important actions are forgotten; quality varies across contributors.

**Resource search should target**

Meeting/action automation, project-report workflows, structured project-management Skills, spreadsheet/task integration and real PM cases.

---

### P13 — Existing materials / experience → reusable local knowledge and Skills

**Situation**

Individuals have historical project documents, templates, solutions and personal experience but reuse is weak.

**Job**

Organize knowledge locally, build reusable Skills/templates and retrieve historical problems/solutions without exposing restricted data.

**Observed pain**

Knowledge remains personal; respondents ask how to create/train Skills and how to organize a local knowledge base.

**Resource search should target**

Codex/Claude/WorkBuddy Skill authoring, local knowledge workflows, RAG/file-context patterns, update/versioning and enterprise-data boundaries.

---

### P14 — Tool onboarding only when tied to a delivery job

Survey respondents explicitly ask for Agent examples, Agent teams, WorkBuddy/Coding-Agent practice and better ERP-development tools.

The Curator must not answer with a generic product tutorial catalog.

Correct framing examples:

- “How do I use Codex to reconcile five migration Excel files safely?”
- “How do I use Codex to understand an inherited EBS code module?”
- “How do I use WorkBuddy to collect practitioner material and turn it into a project brief?”
- “Which PM Skills help turn requirements into PRD/prototype?”

Tool learning is subordinate to a real delivery job.

## 4. Adversarial findings

### A. Do not overfit to the survey's option structure

The questionnaire itself grouped work into project management, requirements, blueprint, design, development, testing and delivery. Those categories are useful for coverage but should not become the product ontology.

The free-text answers repeatedly cross stages: one real task may start from meeting notes and end in a PRD, process diagram and PPT.

### B. Do not mistake “generate X” for the real need

Users often say “generate PPT / generate PRD / generate solution”. The real acceptance condition is usually:

- based on their project material;
- business-correct;
- editable;
- reviewable;
- not generic/AI-flavored;
- low rework;
- traceable to facts;
- safe for enterprise data.

Therefore resource evaluation must include output quality and correction cost, not only generation capability.

### C. Existing AI adoption is already substantial

Because most respondents already use AI frequently, a beginner feature tour is unlikely to solve the main problem. The stronger need is **reliable workflows, Skills, examples and verification methods**.

### D. “AI output quality unstable” is the central product challenge

The Curator should prioritize resources that reduce uncertainty through:

- source grounding;
- editable artifacts;
- explicit verification;
- repeatable workflows;
- narrow specialized Skills when justified;
- real practitioner examples;
- known failure modes.

### E. Adapter/source strategy should be problem-driven

Survey evidence strengthens the case for Chinese practitioner content, especially for PM/PPT/prototype/WorkBuddy/Skill workflows. It does not justify searching WeChat/Bilibili/Xiaohongshu for every problem.

## 5. Current priority problem cards

Do not attempt to curate all 14 at once.

Recommended first wave because they are frequent, highly practical, and represent distinct resource types:

1. **P01 Meeting/workshop → requirement package**
2. **P02 Requirements → PRD/FS/functional design**
3. **P03 Requirements → interactive prototype**
4. **P04 Business logic → editable process/architecture diagram**
5. **P05 Source materials → customer-ready PPT**
6. **P06 Excel/CSV → reconciliation/validation**
7. **P07 Codebase → logic/FS/debug**
8. **P10 Requirement → test scenarios/cases**

Second wave:

- P08 troubleshooting;
- P09 design completeness review;
- P11 manuals/training;
- P12 PM reporting;
- P13 knowledge/Skills;
- tool-onboarding questions bound to one of the above jobs.

Priority is provisional. A real supplied project artifact can override it.

## 6. Product unit going forward

Use **Problem Cards**, not broad scenario labels.

Each card should contain only what is needed to search and judge resources:

```text
Problem
Trigger / situation
Typical inputs
Concrete job
Expected deliverable
Acceptance criteria
Current pain / workaround
Important constraints
Candidate resource types
```

This is not a scoring schema or permanent taxonomy. It is a compact representation of a real work problem.

## 7. Implication for the next local task

The next local curation test should not be “requirements analysis” generically.

Use P01 or P02 at concrete work-unit granularity. Example:

> A consultant has a 2-hour customer workshop transcript, existing process document and Excel requirement list. By tomorrow morning they must deliver a first reviewable requirement package: requirements, open questions, omissions/conflicts and traceable source references. Find a small number of external Skills/Tools/tutorials/practitioner methods that can be learned tonight and used on real project material tomorrow.

Success means the resources can plausibly reduce real delivery effort/rework, not that the answer contains many links.
