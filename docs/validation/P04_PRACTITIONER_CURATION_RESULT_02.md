# P04 Practitioner Curation Result 02

Date: 2026-08-30

## Verdict

> **CLOSE P04 — RECOMMENDATION STABLE, WITH EXPLICIT COVERAGE GAPS**

This delta did not rerun draw.io capability, static safety, official facts, or runtime testing. It only challenged the missing practitioner layer from Result 01.

The recommendation is now stable enough to close P04: additional search is unlikely to change what an ERP / enterprise-information-system colleague should learn first, which implementation is worth trying, or which caveats matter.

## What materially changed

Two practitioner sources added evidence that Result 01 was missing:

1. a direct product-manager walkthrough from requirements text to editable Draw.io;
2. a recent real product-workflow retrospective showing why diagram quality depends on prior logic clarification, iteration, and human correction rather than one-shot generation.

This is enough to correct the earlier over-reliance on author self-practice without turning independent third-party evidence into a mandatory gate.

## Retained practical package

### 1. Primary practitioner workflow / judgement guide

**冰冰酱 —《从一张白纸到交付PRD：我的全自动 AI 产品工作流》**  
https://www.woshipm.com/ai/6422053.html

Evidence role: **independent practitioner workflow evidence** relative to Draw.io / process-builder.

Why retain:

- recent product-manager workflow based on the author's actual work rather than a generic feature demo;
- starts by clarifying business rules, permissions, state, data and boundaries before asking AI to generate deliverables;
- reports a real multi-role / multi-site SaaS requirement iterating from v0.1 to v0.9, including substantial rework after the underlying entity structure was initially wrong;
- reports repeated review/correction rather than one-shot generation;
- explicitly uses Draw.io in the toolchain and explains the switch from Mermaid for more PM-like layout/readability;
- also admits remaining defects such as line crossings, which is more useful than a polished success-only demo.

Practical implication:

> For real enterprise requirements, first make the process semantics explicit; then let AI produce/edit the diagram; treat the first diagram as a review artifact, not as the truth.

Limitation:

- Draw.io is one part of a broader AI product workflow, so this is not the best step-by-step Draw.io tutorial by itself.

### 2. Direct low-friction walkthrough

**健彬的产品Live / 北沐而川 —《3分钟绘制流程图！这个AI+绘图工具的神仙组合》**  
https://www.woshipm.com/share/6190538.html

Evidence role: **independent practitioner-style operational guide** relative to Draw.io and process-builder.

Observed workflow:

```text
CRM / product requirement text
→ ask DeepSeek to organize the flow and output XML
→ save the XML
→ import into Draw.io
→ manually adjust details
→ keep an editable Draw.io artifact
```

Why retain:

- directly matches the P04 job: requirement/business text → editable diagram;
- uses a concrete CRM product-text example rather than only a generic login flow;
- demonstrates a no-Skill / low-install-cost path that colleagues can understand immediately;
- makes manual adjustment after generation explicit.

Limitations:

- the demo is shallow and does not show complex exception handling or serious iteration;
- claims such as “3 minutes” or “standard flowchart” are promotional/self-reported and are not treated as validated outcome evidence;
- 2025 DeepSeek UI/setup details are version-coupled and should not be treated as current fact authority.

### 3. Strong task-fit implementation / method

**Castaldo-Solutions/process-builder**  
https://github.com/Castaldo-Solutions/process-builder

Evidence role: **author self-practice + original implementation**, not independent validation.

Retain because it remains the strongest enterprise-process-specific method found:

- interview-first reconstruction;
- actors / order / tools / decisions made explicit before drawing;
- structured JSON intermediate representation;
- editable `.drawio` swimlane output;
- AS-IS / pain-point / TO-BE support;
- explicit no-guessing discipline when process facts are missing.

The new practitioner evidence does not replace this implementation; it prevents us from overstating the author's own write-up as independent proof.

### 4. Official implementation/current-fact anchor

**jgraph/drawio-mcp** remains the supporting current-fact / implementation anchor.

Do not rerun the already-completed capability/static/runtime research unless a later real adoption decision exposes a new material risk.

### 5. Anttu article

Keep as an **optional technical operation/troubleshooting companion** only. It is no longer carrying the burden of completing the practitioner layer.

## Bilibili delta

The earlier recall failure was real: ordinary public Web discovery surfaced multiple relevant videos.

### Useful but not decision-changing

**AI辅导员小宇 — Cursor + draw.io**  
https://www.bilibili.com/video/BV1yFgCzBEgq/

Publicly visible material shows:

- Cursor + AI generating Draw.io XML;
- text → flowchart;
- screenshot → editable/reconstructed diagram;
- templates and direct Draw.io editing.

This is a useful video-format tutorial, but it is more general AI-office operation than business-process consulting evidence, and its efficiency claims are promotional. It does not materially improve the retained package above.

### Coverage gap, not absence evidence

`产品老兵杰哥` public search surfaces several highly relevant PM / ERP-adjacent items, including:

- “一句话生成专业的流程图/架构图，能用 draw.io 二次编辑”;
- “流程类图片一键变成可编辑的 draw.io 文件”;
- “把 AI 生成的流程图一键导入 Draw.io 二次编辑”.

However, full original-page/transcript access remained intermittent (412). Search titles/snippets are not sufficient evidence to assert the detailed workflow or outcome.

Record this as a **Bilibili full-content coverage gap**. It does not justify more local acquisition work for P04 because the user decision is already stable.

## Adversarial rejection

A 2026 CSDN/AI Agent article titled **《AI生成可编辑流程图：DeepSeek+Draw.io实战指南》** looked highly task-matched, but it was not retained.

Reasons:

- multiple unsupported quantitative claims (for example success-rate and team-usage numbers) without evidence;
- internally inconsistent setup statements;
- sample code omits part of the claimed conversion path while presenting the end-to-end workflow as directly runnable;
- mixes stable practice advice with version/pricing/setup claims that should be fact-checked before reuse.

Lesson: apparent detail density is not practitioner-evidence quality.

## Final P04 recommendation

For an ERP / enterprise-information-system colleague:

1. **Read the 2026 product-workflow retrospective first** to understand the quality boundary: clarify semantics, then generate, review and iterate.
2. **Use the 2025 CRM → XML → Draw.io guide as the lowest-friction first trial** when the task is simply turning a clear requirement description into an editable diagram.
3. **Use `process-builder` when the work is true enterprise process mapping** involving actors, handoffs, decisions, AS-IS/TO-BE and pain points.
4. **Use official draw.io material only for current capability/setup facts**; do not make it the primary learning resource.
5. **Use Anttu or the Bilibili operation video only when a colleague needs technical drawing-operation help.**

## Stop decision

P04 is closed because the recommendation package is now decision-complete:

- real business/product input: covered;
- actual operation/workflow: covered;
- editable output: covered;
- correction/rework: covered;
- failure/quality boundary: covered;
- low-cost adoption path: covered;
- deeper enterprise-process method: covered;
- evidence roles: correctly separated;
- remaining platform acquisition gap: explicit.

Further search could still find more links, but is unlikely to change what a colleague should learn or use first.

## Next project action

Return to demand evidence and select the next real Problem Card. Do not carry P04's Draw.io-specific details into a new permanent framework.
