# Practitioner Discovery

Read this only when the user wants best practices, tutorials, real workflows, practitioner cases, or learning resources.

## Start fresh

Normal external curation starts with a fresh search for the current request.

Project validation files, old Curation Pack results, local repo notes, bookmarks, and previous recommendation lists are **historical leads**, not current external evidence. They may contribute names or search terms, but they must not decide today's candidate pool or ranking by themselves.

If an old project document points to a promising resource, rediscover/open the external resource in the current run before recommending it. If it cannot be reopened, label the coverage gap instead of treating the historical judgement as fresh verification.

## Keep explicit source intent intact

A named platform/source can be either a hard constraint or a preference.

Treat wording such as “去小红书上找 / 只看知乎 / 从公众号里找” as a **hard source constraint**. Treat wording such as “最好有小红书 / 优先知乎 / 有的话看看公众号” as a **source preference**.

For a hard source constraint, the requested source is part of the task definition. If search, login, dynamic rendering, anti-bot limits, host policy, or access prevents inspecting that source after a reasonable targeted attempt:

- state the `coverage/policy gap`;
- do not claim the source-constrained curation is complete;
- do not silently replace the task with a generic cross-platform answer;
- off-source material may be offered only as clearly labeled supplementary reference.

For a source preference, fallback to stronger inspectable evidence is allowed when the preferred source is unavailable, but say so explicitly.

## What to search

This reference belongs to an **AI work-practice Curator**. Unless the user explicitly asks for domain-only guidance, keep AI/Agent/tool-enabled work in the discovery scope even when the shorthand request only says “最佳实践”.

Build a few targeted queries from the actual task:

```text
task / artifact × AI or tool
role × task × AI
industry / work context × task × AI
specific workflow × tutorial / case / review / failure
```

A query batch that drops AI/Agent/Tool entirely and searches only the domain topic is intent drift.

For Chinese ERP / ToB / product / project / consultant work, useful discovery pools often include:

- Bilibili;
- WeChat public accounts;
- Xiaohongshu;
- Zhihu / 人人都是产品经理 / 掘金 / CSDN / practitioner blogs;
- GitHub repos/examples connected to the practitioner workflow.

Do not search every platform by quota. Instead inspect the **serious candidate pool** before stopping.

Run one targeted recall correction against the 1–2 additional practitioner pools most likely to change the answer when either condition is true:

- a Chinese practitioner task has serious candidates from only one accessible Chinese practitioner pool; or
- the rest of the serious candidates are dominated by official docs, vendor content, implementation repos, or global/English sources.

This is a **candidate-pool concentration trigger**, not a diversity target. If the existing pool already contains several direct, inspectable, task-matched practitioner candidates, stop.

A platform returning zero useful results or being inaccessible does not prove it lacks useful practitioner content. If that missing pool could plausibly change the final ranking, label a `coverage/policy gap`; do not install or build a platform adapter merely to complete coverage.

## Freshness

AI work practices, Agents, Skills, MCPs, model capabilities, and tool workflows can change quickly.

When freshness can change the recommendation:

- actively search for recent/current practitioner material, not only evergreen keywords;
- inspect publication/update dates when available;
- check whether the demonstrated workflow/tool/version still exists and is usable;
- compare newer evidence with older high-quality practice rather than automatically replacing it.

**Newest is not automatically best.** A durable older workflow can remain the strongest recommendation when its task fit, real evidence, and reproducibility are better. But an older source should not win simply because it was already present in project history.

Do not use “latest/current” language unless the search actually covered recent material sufficiently to support it.

## What deserves inspection

Popularity is only a discovery hint. Prefer content that shows several of these:

- a role/work context close to the user;
- concrete input → operation → output;
- the artifact the user actually needs, especially editable deliverables;
- real screenshots/examples/templates/prompts/commands/workflow steps;
- failures, rework, limitations, or long-term usage experience;
- a current and reproducible workflow.

For Bilibili/Xiaohongshu, saves, coins, and substantive comments can help decide what to inspect first; they do not prove quality.

When search results contain plausible practitioner/creator candidates, open the strongest one or few before spending answer budget on official standards or product pages.

Every resource that appears in the final recommendation should have been inspected in the current run unless the user explicitly requested reuse of a prior curated pack.

## How to choose among inspected candidates

Prefer **audience/work-context fit + required-artifact fit + direct practice evidence + current applicability** before generic polish, global popularity, or novelty.

If the user's language, region, or professional ecosystem is clear, prefer practitioner evidence from that ecosystem when quality is comparable. Cross-language material is valuable when materially stronger or when local coverage has a real gap.

Check the actual deliverable. Editable draw.io is not equivalent to SVG/PNG unless the workflow preserves editability; apply the same rule to PPTX, Word, BPMN, Visio, Markdown, code, or other required artifacts.

Do not let an adjacent task outrank the actual task merely because it has a stronger SAP/ERP/tool label. For example, an SAP BTP architecture-diagram workflow is not automatically a top resource for a business-process-flow request. Keep adjacent-task material secondary unless it contributes a decision-changing method absent from direct-task candidates.

## Source roles

Practitioner content answers **how people actually work**.

Original repos/tools can confirm **what a demonstrated workflow really uses or produces**.

Official sources answer current facts and product-specific constraints such as format semantics, version, compatibility, UI standards, or supported behavior. They are usually capability/constraint verification rather than practitioner practice and should not be used simply to fill a Top 1–3 list.

For a standards/constraint question, or a niche product-specific task where no inspectable practitioner evidence exists, official material may still be the strongest available domain-specific anchor. Label it explicitly as official constraint/verification rather than practitioner practice.

Internal project validation/history answers **what this project previously concluded**. It is not independent current practitioner evidence and should not be surfaced as an external recommendation source unless the user explicitly asks about project history.

If several creators repeat the same upstream demo, treat them as one evidence family unless someone adds a new real input, failure case, constraint, or more reproducible workflow.

If original content cannot be read because of login, dynamic rendering, anti-bot limits, host source policy, or search-tool restrictions, say `coverage/policy gap`. Do not silently replace inaccessible practitioner evidence with official documentation or internal historical judgement and call the curation complete.

## Output discipline

For explicit tutorial/best-practice requests, normally keep 1–3 resources and say:

- what it is and where to open it;
- why it matches this user's role/context/task/artifact;
- why it outranks other serious candidates;
- which one to start with;
- when freshness matters, the publication/update/currentness boundary;
- any material author/promotion/language/access boundary.

Do not force three resources. One or two strong practitioner resources plus a separately labeled official capability check is better than mixing source roles to fill a list.

Then add only the short synthesis needed to connect the resources.

Do not convert a resource that happens to use a Tool/Skill into an install recommendation. Capability adoption is a separate decision handled by `advising-erp-ai-capabilities`.

Final check:

> If my own explanation and all internal project files disappeared, would the freshly inspected external resources still justify what I am recommending now?

If not, the curation is probably not finished.
