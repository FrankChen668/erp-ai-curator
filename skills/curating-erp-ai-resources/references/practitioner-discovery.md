# Practitioner Discovery

Read this only when the user wants best practices, tutorials, real workflows, practitioner cases, or learning resources.

## What to search

Build a few targeted queries from the actual task:

```text
task / artifact × AI or tool
role × task × AI
industry / work context × task × AI
specific workflow × tutorial / case / review / failure
```

If the original request is about **using AI/Agent/Tool to improve a task**, keep that dimension alive. A query batch that drops AI/Agent/Tool entirely and searches only the domain topic is intent drift.

For Chinese ERP / ToB / product / project / consultant work, useful discovery pools often include:

- Bilibili;
- WeChat public accounts;
- Xiaohongshu;
- Zhihu / 人人都是产品经理 / 掘金 / CSDN / practitioner blogs;
- GitHub repos/examples connected to the practitioner workflow.

Do not search every platform by quota. Use the pools most likely to contain high-signal practical evidence.

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

## How to choose among inspected candidates

Prefer **audience/work-context fit + required-artifact fit + direct practice evidence** before generic polish, global popularity, or novelty.

If the user's language, region, or professional ecosystem is clear, prefer practitioner evidence from that ecosystem when quality is comparable. Cross-language material is valuable when materially stronger or when local coverage has a real gap.

Check the actual deliverable. Editable draw.io is not equivalent to SVG/PNG unless the workflow preserves editability; apply the same rule to PPTX, Word, BPMN, Visio, Markdown, code, or other required artifacts.

## Source roles

Practitioner content answers **how people actually work**.

Original repos/tools can confirm **what a demonstrated workflow really uses or produces**.

Official sources answer only the current facts needed to understand a practice, such as format semantics, version, compatibility, or standard behavior.

If several creators repeat the same upstream demo, treat them as one evidence family unless someone adds a new real input, failure case, constraint, or more reproducible workflow.

If original content cannot be read because of login, dynamic rendering, anti-bot limits, host source policy, or search-tool restrictions, say `coverage/policy gap`. Do not silently replace inaccessible practitioner evidence with official documentation and call the curation complete.

## Output discipline

For explicit tutorial/best-practice requests, normally keep 1–3 resources and say:

- what it is and where to open it;
- why it matches this user's role/context/task/artifact;
- why it outranks other serious candidates;
- which one to start with;
- any material author/promotion/version/language/access boundary.

Then add only the short synthesis needed to connect the resources.

Do not convert a resource that happens to use a Tool/Skill into an install recommendation. Capability adoption is a separate decision handled by `advising-erp-ai-capabilities`.

Final check:

> If my own explanation disappeared, would the external resources I selected still tell the user what is most worth learning and why?

If not, the curation is probably not finished.
