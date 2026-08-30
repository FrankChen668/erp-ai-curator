# P04 Practitioner-First Curation Result 01

Date: 2026-08-30

## Verdict

**USEFUL WITH GAPS / GOAL NOT YET COMPLETE**

This run found a strong task-matched implementation/method candidate and performed solid implementation/fact/safety verification, but it did **not** complete the project's primary P04 objective: finding a sufficiently strong **third-party practitioner-first** resource package that an ERP consultant would immediately want to learn from.

## What the P04 objective actually is

The goal is not to prove whether “AI can one-click generate enterprise-grade BPMN”.

The real user question is:

> Given customer requirements / notes / business rules, how are practitioners actually using AI to produce an editable process diagram quickly, what techniques work, what fails, and which Skill/Tool is worth using?

A strong package should normally contain:

1. a practitioner guide / review / walkthrough worth watching or reading first;
2. the actual Skill / Tool / method behind it;
3. only the current official/original facts needed to avoid stale adoption;
4. important limits / correction cost.

## What the run did well

### Strong task-fit candidate

`Castaldo-Solutions/process-builder` is highly relevant to enterprise-process work:

- interview-first reconstruction;
- explicit actors / order / tools / decisions;
- structured JSON before diagram generation;
- editable `.drawio` output;
- AS-IS / TO-BE / pain-point mapping;
- no intentional guessing when process facts are missing.

This is worth retaining as a **strong implementation/method candidate**.

### Strong implementation and fact verification

The run correctly traced practical claims to:

- the actual `process-builder` repository;
- current official `@drawio/mcp` material;
- editable `.drawio` capability;
- current setup / data / offline facts;
- lightweight static safety boundaries.

### Evidence-role discipline improved

The run correctly distinguished:

- author self-practice;
- independent practitioner content;
- official fact anchors;
- derivative reposts / weak evidence.

## Why the goal is not yet complete

### 1. The main “practical guide” is not third-party evidence

The Castaldo article is useful, but it is the tool/method author's own consulting write-up.

It can prove:

- the intended workflow;
- how the author says it is used;
- what the implementation is designed to do.

It does **not** by itself prove that independent practitioners find the method effective.

Therefore it should not be treated as the completed practitioner-first layer.

### 2. The independent companion is too technical and not task-matched enough

The Anttu article is useful for:

- MCP operation;
- create/read/modify/export mechanics;
- troubleshooting.

But it is primarily a technical draw.io MCP usage article, not a business-process / ERP-consulting walkthrough.

It does not fully answer the consultant's core question:

> How do I turn real business material into a reviewable process map with roles, decisions, exceptions and handoffs?

### 3. Discovery recall stopped too early

A cloud falsification search immediately surfaced relevant Bilibili material through ordinary public Web, including:

- `产品老兵杰哥` series containing “一句话生成专业的流程图/架构图，能用 draw.io 二次编辑”, “流程类图片一键变成可编辑 draw.io”, and “把 AI 生成的流程图一键导入 Draw.io 二次编辑”;
- `AI辅导员小宇` practical Cursor + draw.io workflow;
- multiple current drawio-skill walkthroughs.

Therefore the statement that Bilibili did not yield enough strong practical evidence is **not yet supported**.

The run encountered one 412 path and then stopped too early instead of continuing ordinary Web discovery.

This is exactly the already-known boundary:

> access failure on one path ≠ platform evidence absence.

### 4. The opening conclusion overstates one author's method

The run generalized:

> “the most reliable path is interview → JSON → local program → draw.io.”

Current evidence only supports:

> this is one promising, task-matched method implemented by Castaldo Solutions.

There is not yet enough independent comparative evidence to promote it to a universal “most reliable path”.

### 5. The run partially reframed the user problem into a harder strawman

The user problem was not:

> “Can AI one-click produce directly reviewable enterprise-grade BPMN?”

The user problem was:

> “How can practitioners use AI to quickly produce editable process diagrams, what practical techniques exist, and what should they learn/use?”

Rejecting the stronger one-click BPMN claim is reasonable, but it should not become the main success criterion.

## Retained assets

### Retain

- `Castaldo-Solutions/process-builder`
  - role: strong task-fit implementation/method candidate;
  - evidence: author/practitioner self-use, not independent validation;
  - status: **KEEP / needs independent practitioner companion**.

- official `jgraph/drawio-mcp`
  - role: implementation/current fact anchor;
  - status: **KEEP AS SUPPORTING TOOL/FACT SOURCE**.

### Conditional

- Anttu draw.io MCP article
  - role: independent technical operation/troubleshooting companion;
  - status: **USEFUL BUT NOT SUFFICIENT AS PRIMARY ERP PRACTICE GUIDE**.

## Next action — delta only, do not rerun P04 from scratch

Do **not** repeat repository/static/runtime verification already completed.

Only fill the missing practitioner layer:

1. inspect 2–4 high-signal Bilibili / Chinese practitioner candidates already discoverable via normal Web;
2. prioritize independent PM / consultant / enterprise-workflow walkthroughs over tool-author demos;
3. use WeChat Search → Reader only if a concrete high-value article candidate needs full-text acquisition;
4. compare the practical learning value against Castaldo + Anttu;
5. retain at most one primary practical guide and one materially different companion.

Stop after the practitioner layer is either filled or explicitly shown to remain a coverage gap.

## Product-level lesson

No new framework is needed.

The existing source strategy was correct; execution did not fully follow it.

The correction is operational:

> practitioner-first means the run should not stop at a strong self-authored implementation guide when obvious independent-practice discovery paths remain unexplored.
