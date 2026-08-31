# Practitioner Discovery

Read this when external practitioner discovery is material to the curation request.

## Query construction

Keep the **AI-enabled work-practice** dimension in scope unless the user explicitly asks for domain-only guidance. Build a small set of queries from the real task, for example:

```text
task / artifact × AI or tool
role × task × AI
industry / work context × task × AI
specific workflow × tutorial / case / review / failure
```

A query batch that drops AI / Agent / Tool entirely and searches only the domain topic is intent drift.

## Recall correction

For Chinese ERP / ToB / product / project / consultant work, useful practitioner pools can include Bilibili, WeChat public accounts, Xiaohongshu, Zhihu, 人人都是产品经理, 掘金, CSDN, practitioner blogs, and GitHub workflows/examples.

Do not search platforms by quota. Use broad Web first. If results are concentrated in official docs, generic global sources, GitHub implementations, or one easy-to-index platform while the user's obvious practitioner ecosystem is missing, run targeted `site:` or source-qualified searches against the one or few pools most likely to change the candidate set.

This is a **recall correction**, not a diversity target.

## Freshness and currentness

AI workflows, Agents, Skills, MCPs, models, and tool behavior can change quickly.

When currentness can change the recommendation:

- actively include recent/current practitioner material;
- inspect publication/update dates when available;
- check whether the demonstrated workflow/tool/version still exists and is usable;
- compare newer evidence with older high-quality practice instead of using newest-wins.

An older resource may still lead when its task fit, direct evidence, and reproducibility are stronger. Do not use “latest/current” language unless the acquired evidence supports that scope.

## Candidate inspection

Popularity is a discovery hint only. Inspect candidates that show several of these:

- role/work context close to the user;
- concrete input → operation → output;
- the artifact the user actually needs, especially editable deliverables;
- screenshots, examples, templates, prompts, commands, or workflow steps;
- failures, rework, limitations, or long-term usage experience;
- a current and reproducible workflow.

For Bilibili/Xiaohongshu, saves, coins, comments, likes, or plays can help decide what to inspect first; they do not prove quality.

When plausible practitioner/creator candidates exist, inspect the strongest ones before spending answer budget on official product pages.

## Evidence roles

Keep source roles distinct:

- **independent practitioner** — real adoption, review, or failure experience;
- **author self-practice / vendor demo** — shows how the author's own approach works, not independent superiority;
- **implementation** — original repo/tool/workflow that confirms what is actually used or produced;
- **official fact** — current version, compatibility, format, or standard fact needed to interpret the practice;
- **Curator synthesis** — the conclusion drawn from acquired evidence.

If several creators repeat the same upstream demo, treat them as one evidence family unless someone adds new real inputs, failure cases, constraints, or a more reproducible workflow.

## Selection checks

Prefer audience/ecosystem fit, required-artifact fit, direct practice evidence, and current applicability before generic polish or popularity.

When the user's language, region, or professional ecosystem is clear, prefer comparable evidence from that ecosystem. Cross-language material should lead only when materially stronger or when local coverage has a real gap.

Check the actual deliverable: editable draw.io is not equivalent to SVG/PNG; PPTX is not image-only slides; a BPMN model is not a generic flowchart image. Apply the same rule to Word, Visio, Markdown, code, or other required artifacts.

## Access and provenance gaps

Search snippets, titles, engagement counts, and internal project history are not substitutes for opened original content.

If original content cannot be read because of login, dynamic rendering, anti-bot limits, host policy, or search-tool restrictions, state `coverage/policy gap`. Do not convert inaccessible leads into fully verified recommendations.

Final check:

> If my own explanation and all internal project files disappeared, would the freshly inspected external resources still justify the recommendation?

If not, the curation is not finished.
