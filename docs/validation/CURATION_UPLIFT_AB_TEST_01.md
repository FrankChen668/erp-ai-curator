# Curation Uplift A/B Test 01

Date: 2026-08-29

## 1. Test question

This test answers one narrow product question:

> **Does access to a qualified practitioner-source adapter materially improve the final ERP AI Curator recommendation package compared with normal Web/GitHub discovery alone?**

This is not a test of search volume, platform coverage, or whether multi-Skill routing is technically possible. Routing was already demonstrated for the WeChat chain.

## 2. Fresh task

Use the same raw task in both runs:

> 请为泛 ERP / 企业信息化从业者寻找：能够帮助实施顾问、产品经理或开发人员借助 AI 快速理解一个陌生 ERP 模块或定制企业系统的优秀 Skill、Tool、方法和实战资源。目标包括快速建立端到端业务流程、角色/单据/主数据、配置或代码逻辑、接口上下游、异常场景的认识，并能验证自己的理解，而不是让 AI 凭记忆解释。最终只保留真正值得采用、学习或分享给同事的少量资源。

Do not reveal an expected recommendation, expected Mode, expected platform, or old OWNER_REAL answer.

## 3. Paired-run discipline

Run A and Run B must use:

- the same raw task;
- the same model family/configuration where controllable;
- the same repository commit;
- the same date/time window as closely as practical;
- fresh isolated sessions with no conversation history from T01/T02/routing tests;
- the same output contract.

Freeze Run A before starting Run B.

Do not let Run B read Run A output.

The local Agent does not judge which run is better. Cloud review does that after both outputs are frozen.

## 4. Run A — normal discovery baseline

Allowed:

- ordinary Web search;
- GitHub search/read;
- official/original sources;
- normally reachable public community pages.

Unavailable for this run:

- `wechat-article-search`;
- `wechat-article-reader`;
- Bilibili/Xiaohongshu source adapters;
- any newly installed source adapter.

The point is to capture the best package the current normal path can produce.

## 5. Run B — qualified adapter available

Same raw task and output contract.

Allowed:

- everything allowed in Run A;
- already-qualified WeChat discovery + original-article reader chain.

Important:

- Do **not** force WeChat use.
- Invoke it only if a concrete evidence gap matters to the final recommendation.
- Do not install or upgrade anything.
- Bilibili and Xiaohongshu remain unavailable for this test.
- If WeChat adds no meaningful evidence, the valid result is no material uplift.

## 6. Output contract for both runs

### Task

Repeat the raw task.

### Main recommendation

- Resource
- Type
- Why it wins for this task
- What the ERP practitioner can actually do/get
- Best fit
- Important limitations
- Original link

### Fact anchor

Only when current capability/version/compatibility facts require it.

### Practical companion

At most one.

Must explain:

- why it is worth the colleague's time;
- what concrete workflow/example/prompt/failure/adoption evidence it adds;
- source trust/limitations;
- original link.

If none:

`No strong practical companion found`

### Second solution

Only for a materially different use boundary.

### Important rejected candidates

At most three, one decisive rejection reason each.

### Coverage gaps

State access gaps honestly; do not use snippets as full-text evidence.

### Curation conclusion

1. Would I send this package to an ERP colleague? Yes / Maybe / No
2. Strongest practical value
3. Strongest unresolved uncertainty

### Acquisition trace

No hidden reasoning. Only observable research actions relevant to the comparison:

- source types actually used;
- source adapters actually invoked, if any;
- whether original/full content was obtained;
- stop point.

## 7. Cloud comparison dimensions

Do not calculate a total score.

Cloud reviews only material delta:

### Discovery delta

- Did B find a serious candidate/practical companion absent from A?
- Was the new item actually better for this task, not merely more Chinese or more numerous?

### Evidence delta

- Did B obtain original/full practitioner evidence that A lacked?
- Did that evidence clarify workflow, limitations, adoption cost or real fit?

### Decision delta

- Did Main Recommendation change for a defensible reason?
- If it did not change, was confidence/limitation/practical guidance materially strengthened?

### User-value delta

- Is B more worth directly sharing with an ERP colleague?
- Does the gain justify adapter maintenance/setup cost?

### Research-cost delta

- Did B create excessive search overhead?
- Was the adapter called only when useful and stopped after enough evidence?

## 8. Adversarial checks

Cloud must attack the apparent uplift:

1. **Chinese-content halo** — is the new evidence actually better, or just Chinese?
2. **More-links illusion** — did B add volume without changing user value?
3. **Adapter-forcing** — did B use WeChat merely because it was available?
4. **Weak baseline** — was A artificially under-researched?
5. **Content/source confusion** — is a polished article being treated as authoritative without provenance/limitations?
6. **Recommendation drift** — did B over-weight practitioner anecdotes over current product facts?
7. **Cost blindness** — does the gain justify installation/maintenance/anti-bot risk?
8. **Topic-specific uplift** — even if B wins, do not generalize from one task.

## 9. Decision after Test 01

Choose one:

### MATERIAL UPLIFT

B produces a clearly more useful/share-worthy recommendation package because of adapter-acquired evidence.

Next: repeat on 1–2 different fresh tasks before making the adapter permanent.

### LIMITED UPLIFT

B adds useful evidence but does not materially change adoption/recommendation quality.

Next: keep WeChat conditional; do not expand adapter footprint yet.

### NO MATERIAL UPLIFT

B adds links/content but not user value, or setup/research cost dominates.

Next: do not promote the source-adapter layer merely because routing works.

### INVALID TEST

Isolation, same-task discipline, source availability, or baseline fairness was not preserved.

Repeat only the invalid portion; do not reinterpret noise as product evidence.

## 10. What this test does not decide

- whether Bilibili should be retained;
- whether Xiaohongshu needs an adapter;
- whether a production ERP AI Curator Skill should be implemented;
- independent-user value;
- whether every resource-curation task should search Chinese platforms.
