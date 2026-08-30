# Curator 0.7.1 — Practitioner Discovery Patch

Date: 2026-08-30
Status: **REAL CONTROLLED-USE DEFECT — PATCHED / CLOUD REGRESSION PASSED / ORIGINAL-HOST RE-RUN OPTIONAL EVIDENCE**

## 1. Triggering real-use prompt

Owner used the actual Skill with:

> `使用下这个skill 给我找下做流程图的最佳实践`

Observed answer behavior under 0.7.0:

- conclusion: ordinary AI + editable drawing tool is enough;
- sources: mainly OMG BPMN, Camunda, Microsoft, ASQ;
- output: flowchart type table, 8 generic drawing rules, ERP workflow suggestion, generated prompt and risks;
- missing: Bilibili / WeChat / Xiaohongshu / PM / ToB / ERP-adjacent practitioner tutorials and practical creator links.

Owner expected Curator to surface high-signal practical learning resources from the Chinese practitioner ecosystem, not re-author a generic flowchart tutorial.

This is accepted as REAL_USER_USE negative behavior evidence.

## 2. First-principles defect

The product is a Curator. For an explicit “find best practices/tutorials” request, product value is primarily:

```text
find existing strong practical content
→ filter noise
→ inspect concrete content
→ choose what is worth watching/learning
→ verify implementation/current facts
→ compress decision
```

The observed answer instead behaved like:

```text
decide A/no-new-tool
→ official/standard docs
→ model writes tutorial
```

The answer may be educational, but it does not materially outperform generic AI on the Curator North Star.

## 3. Root cause

0.7.0 correctly used A/B/C to decide whether specialized capability should be adopted.

But it also said under A:

> external resources default `0`.

That is valid for “should I install another Tool/Skill?” but ambiguous for an explicit “find me best practices/tutorials” request.

The runtime could therefore collapse two independent decisions:

1. **Do I need a new specialized capability?**
2. **Did the user explicitly ask me to find existing practice/tutorial resources?**

Correct relation:

> `A = no new specialized capability` does **not** imply `no practitioner discovery`.

## 4. Evidence that resource scarcity was not the cause

A bounded Cloud search after the failure found multiple high-match public Bilibili candidates immediately.

### Candidate family A — product-manager / ToB-adjacent

`产品老兵杰哥` currently has a practical AI Product Manager / Skill series containing:

- `精选Skills：一句话生成专业的流程图|架构图，能用drawio二次编辑。`
- `精选Skills：流程类图片一键变成可编辑的draw.io文件`
- `Ai生成的流程图搞到Visio中无法编辑？看教程！`
- `教程|把AI生成的流程图一键导入Draw.io二次编辑。`

The same creator has B-end / supply-chain / ERP/WMS/MES/OMS content, making the role/domain prior materially stronger than generic flowchart pages.

Public discovery evidence:

- https://www.bilibili.com/video/BV1NZwezbEqa/
- Bilibili search pages for related draw.io/Visio content.

Boundary: individual tutorial items need specific-content inspection; creator/domain fit is a discovery prior, not proof of tutorial quality.

### Candidate family B — direct drawio-skill author practice

Agents365 drawio-skill author videos:

- 2026-04 update: about 7.7万 plays / 1671 likes / 668 coins / 5895 favorites in the acquired page;
- 2026-07 update: about 9.5万 plays, demonstrates newer drawio-skill capabilities including BPMN, cross-functional swimlanes, image→editable draw.io and exports.

URLs:

- https://www.bilibili.com/video/BV12moMBrELB/
- https://www.bilibili.com/video/BV1bcNZ6xEK3/

Implementation anchor:

- https://github.com/Agents365-ai/drawio-skill

Current GitHub verification during patch: public repo, active, MIT, created 2026-03, pushed 2026-08-28, about 8610 stars / 604 forks; repo description includes flowchart/BPMN and image→editable diagram support.

Boundary: these videos are **author self-practice**, not independent proof that the Skill is objectively best.

### Candidate family C — independent general workplace practice

`AI辅导员小宇`:

- `【Cursor+draw.io】AI轻松生成专业流程图，工作效率提升20倍！`
- acquired page: about 3.0万 plays / 731 likes / 419 coins / 2077 favorites;
- shows draw.io + AI/Cursor workflow and editable XML path.

URL:

- https://www.bilibili.com/video/BV1yFgCzBEgq/

Boundary: “20倍” is a promotional claim and must not be repeated as validated efficiency evidence.

## 5. What a compliant Curator answer should have done

For this prompt, a strong answer should have looked approximately like:

1. `A/B judgement` only for whether a new specialized Tool/Skill is necessary;
2. because the user explicitly asked to **find best practices**, continue practitioner discovery even if A;
3. first return 1–3 high-signal practical resources from role/domain-relevant ecosystems;
4. say which one to watch first and why;
5. identify author self-practice / promotion / stale-version boundaries;
6. verify drawio-skill/current feature facts against the repo/official source;
7. only then synthesize a few recurring practices.

It should not lead with an 8-rule self-authored flowchart tutorial and use official standards as the main curation evidence.

## 6. 0.7.1 changes

### Runtime Skill

- separate `specialized-capability adoption` from `explicit practice-resource intent`;
- A no longer means external-practice discovery stops;
- explicit best-practice/tutorial intent triggers practitioner discovery;
- link-first tutorial output before Curator synthesis;
- official-only + model-authored tutorial explicitly identified as failure for this intent.

### New progressive-disclosure reference

`skills/curating-erp-ai-resources/references/practitioner-discovery.md`

Defines:

- task × role × industry × artifact × AI/tool query expansion;
- Chinese Bilibili / WeChat / Xiaohongshu / PM / ToB practitioner discovery;
- engagement signals as discovery priors only;
- candidate-admission conditions;
- 1–3 resource link-first output;
- coverage-gap / optional read-only adapter routing;
- final failure check.

## 7. Bounded Cloud regression

Same intent was re-run as a bounded discovery exercise after the patch.

### Acceptance criteria

- [x] practitioner ecosystem searched before official synthesis;
- [x] actual practical Bilibili candidates surfaced;
- [x] role/domain relevance used (product manager / B-end / supply chain adjacency);
- [x] high engagement used only as discovery prior;
- [x] author self-practice explicitly separated from independent evidence;
- [x] current implementation checked against Agents365 GitHub repo;
- [x] official/implementation source returned to verification role;
- [x] output can clearly prioritize what to watch first;
- [x] no need to generate a long replacement tutorial to complete curation;
- [x] WeChat/Xiaohongshu weak normal-Web coverage can be stated as coverage gap rather than silently replaced by official docs.

Result:

> **CLOUD REGRESSION PASS — 0.7.1 corrects the observed product-logic failure in the Cloud path.**

## 8. Adversarial check

### Are we now forcing platform quotas?

No. Bilibili/WeChat/Xiaohongshu are high-signal feeder ecosystems for Chinese practitioner tasks, not mandatory quotas.

### Are likes/saves now recommendation scores?

No. They decide what to inspect first. Specific content still decides recommendation.

### Are we activating the Source Adapter architecture by default?

No. Normal Web found enough Bilibili evidence for this task. WeChat/Xiaohongshu adapters remain conditional and only justified if the inaccessible content could materially change the recommendation.

### Are we turning A into forced resource search for every query?

No. Resource discovery is required when the user explicitly requested best practices/tutorials/resources, or when practitioner evidence is necessary for adoption judgement.

### Is the corrected Skill now proven better in the original host?

Not yet. Cloud regression confirms the instruction/harness correction is coherent and executable with public Web. A re-run in the exact original host would add cross-host/runtime evidence, but is not required to recognize and patch the logic defect.

## 9. Product conclusion

This defect materially sharpens the North Star:

> **The Curator's differentiator is not “give better general advice”. It must do the search/filter/selection work the user otherwise has to do across practitioner ecosystems.**

If future controlled use repeatedly returns polished self-authored advice but fails to surface the best available external practical resources, that is a product failure even when the advice is factually reasonable.
