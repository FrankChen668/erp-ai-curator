# Standard ERP Module Diagnostic 01

Date: 2026-08-29

## 1. Question

> When the work is specifically about learning an unfamiliar standard ERP module, does qualified WeChat practitioner evidence add material value beyond normal authoritative Web/GitHub discovery?

This test exists because the previous mixed task was dominated by custom-system/codebase archaeology.

## 2. Raw task

Use exactly:

> 你是一名此前没有做过 SAP EWM 的泛 ERP / 企业信息化顾问。现在需要快速理解 SAP EWM 的入库收货与上架（inbound receiving and putaway）场景。请寻找少量真正值得学习或分享的 AI Skill、Tool、方法、教程和实战资源，帮助建立：端到端流程、关键角色、主要业务对象/单据、核心配置边界、与采购/库存/自动化设备等上下游集成、常见异常，以及如何用权威资料或系统证据验证自己的理解。不要只给概念介绍，也不要让 AI 凭记忆解释。

The module is specific intentionally. Do not broaden it to generic warehouse management.

## 3. Phase A — Baseline

Use normal Web/GitHub discovery only.

Do not call WeChat/Bilibili/Xiaohongshu adapters.

Produce and freeze a small curation package:

### Main recommendation
- Resource
- Type
- Why worth learning/sharing
- What the consultant can actually learn/do
- Important limitations
- Original link

### Practical companion
At most one.

### Second resource
Only if materially different.

### Rejected candidates
At most three.

### Coverage gaps

### Acquisition trace
Observable sources only.

After freezing Phase A, do not do more ordinary Web/GitHub discovery.

## 4. Phase B — Adapter delta only

Continue from the frozen baseline package.

New acquisition capability allowed:

- `wechat-article-search`
- `wechat-article-reader`

Do not run additional ordinary Web/GitHub searches except opening an already-known authoritative page only when needed to verify a factual claim introduced by WeChat evidence.

WeChat is optional, not mandatory.

If a material practitioner-evidence gap exists, use:

```text
search
→ real mp.weixin.qq.com candidate
→ reader
→ original article body
→ Curator judgement
```

Stop after enough evidence exists to decide whether the frozen package should change.

## 5. Delta output

Do not rewrite everything unless evidence justifies a revision.

Output:

### Baseline package
Frozen Phase A result.

### WeChat evidence acquired
For each actual original article used:

- title
- account/author
- date when available
- original URL
- what concrete implementation/practice detail it adds
- source limitation

If none:

`No useful WeChat practitioner evidence acquired`

### Package changes attributable to WeChat
Only list:

- ADD
- REMOVE
- REPLACE
- STRENGTHEN

Each change must point to the specific WeChat evidence that caused it.

If none:

`No package change attributable to WeChat`

### Delta conclusion
Local Agent must not make the final product verdict.

Only report one factual state:

- `adapter evidence changed package`
- `adapter evidence strengthened package without changing resources`
- `adapter evidence produced no package change`
- `adapter was not used because baseline was sufficient`

## 6. Integrity rules

- same local model/config throughout;
- no old T01/T02/Phase 4 answers;
- no Bilibili/Xiaohongshu;
- no new Skill/MCP install;
- no repo modification;
- search snippet is not original evidence;
- do not force Chinese content into the package;
- official SAP material can remain the best resource if practitioner content adds no value;
- Curator-created advice must be labelled synthesis, not a discovered resource.

## 7. Stop condition

Stop after the delta is observable.

Do not run another task.
Do not change V3 rules.
Do not declare adapter architecture PASS/FAIL.
