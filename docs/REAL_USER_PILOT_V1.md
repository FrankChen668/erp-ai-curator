# ERP AI Curator — Real User Pilot V1

Date: 2026-08-30
Status: **ACTIVE — best-practice curation on real colleague tasks**

## 1. Pilot objective

Do not prove that the Skill can produce polished answers or that users can follow a tool-test protocol.

Test the actual product question:

> **When a real ERP / enterprise-information-system colleague has a real work problem, can the Curator find and compress the best existing AI practices/resources into a small recommendation that is more useful than noisy self-search or generic AI advice?**

User adoption/modification/rejection is then used to validate that curation.

## 2. Pilot input

Use real colleague work only.

Each run starts from:

```text
role / project context
+ actual materials available
+ concrete action/problem
+ expected deliverable
+ material constraints
```

Do not require the user to classify the task into P01–P14.

Do not upload confidential artifacts unless organizational policy permits it. Descriptions or redacted samples are acceptable when sufficient for curation.

## 3. Minimal pilot shape

Start with a few genuine colleague problems. Prefer natural diversity rather than quotas.

Do not manufacture tasks merely to cover categories.

## 4. What the Curator returns

Use `skills/curating-erp-ai-resources/SKILL.md`.

The default output is **best-practice / existing-resource curation**, not an execution SOP.

Keep it compact:

1. conclusion — ordinary AI enough / specialized option worth it / low-cost adoption first;
2. best practice — the most useful existing workflow/method pattern;
3. why — practitioner evidence + capability/constraint evidence that changes the choice;
4. 0–1 primary external resource by default, second only for a materially different boundary;
5. applicability/risk boundary;
6. how to start learning/adopting from that resource or method.

Do not automatically turn the answer into “run this experiment and report back”. A test protocol is only appropriate if the user explicitly asks for testing/validation or if a decision-changing technical uncertainty genuinely requires minimal runtime validation.

## 5. What to capture after the colleague receives/uses the curation

Do not create a long survey. Capture only evidence that can change the product.

### Before / at recommendation

- real task in the colleague’s own words;
- materials/constraints that affected the recommendation;
- best-practice/resource recommendation actually given.

### After natural user response/use

- which part/resource they found useful, useless or wrong;
- whether they learned, adopted, modified or rejected it, and why;
- whether it reduced search/selection/setup effort;
- whether it caused wrong-tool adoption, missing capability or extra work;
- any enterprise/privacy/permission issue missed by the Curator;
- whether they would bring another real task to Curator.

If they later use the method on real work, artifact/result and downstream rework are stronger evidence, but the Curator does not require them to become a tester first.

## 6. Pilot evidence hierarchy

Strong evidence:

- real colleague says the curated practice/resource materially improved a real decision or real work path;
- the colleague actually adopts/modifies it and concrete result/rework can be inspected;
- the curation clearly saved search/selection/setup effort.

Useful negative evidence:

- colleague rejects the recommendation with a concrete reason: outdated practice, wrong environment, missing permission, poor resource quality, excessive setup, or better existing practice.

Not product evidence:

- Curator answers an invented prompt successfully;
- Owner/Agent says the answer “looks good”;
- another synthetic benchmark passes;
- user is made to execute a test primarily so Curator can claim validation;
- links are collected without a real user problem.

## 7. Failure signals to act on immediately

A real case can justify correction when it exposes a clear product defect, for example:

- Curator becomes a workflow coach/test coordinator instead of finding best practices;
- Curator searches for tools although ordinary AI is obviously enough;
- practitioner evidence is skipped and vendor feature lists dominate;
- important task input/constraint is ignored;
- recommended resource cannot handle the actual artifact/environment;
- privacy/write/permission boundary is missed;
- user still does not know which practice/resource is worth their attention;
- curation adds more search/selection effort than it saves;
- source evidence is overstated or not actually acquired.

Fix the narrow recurring defect. Do not create a new framework for one unusual case.

## 8. What success looks like

Do not declare PASS from a numeric threshold in advance.

The pilot is moving in the right direction when real colleagues repeatedly show that:

- the Curator surfaces practices/resources they would not easily find themselves;
- the recommendation is small enough to act on;
- noisy or irrelevant tools are filtered out;
- practitioner limitations are visible before adoption;
- specialized capability is recommended for an observable reason;
- the result is useful enough that they would bring another real problem.

The strongest negative signal is repeated “this is no better than asking my existing AI or searching myself”.

## 9. Current cloud/local responsibility

Cloud/ChatGPT can continue to:

- curate current best practices/resources for submitted real tasks;
- research practitioner evidence, original implementations and current facts;
- inspect user feedback and update the method;
- maintain GitHub authorities.

A local Agent is used only when a curation decision genuinely depends on local files/repository/runtime or an enterprise environment.

## 10. Stop / next decision

Do not return to internal card accumulation while real-user curation opportunities exist.

After several genuine cases, reassess from observed patterns:

- keep V0.1 unchanged;
- make a narrow method/Harness correction;
- add one reusable support artifact because users repeatedly need it;
- or conclude that Curator adds too little value over ordinary AI/search.

## 11. External dependency

Cloud can complete the curation work itself for tasks whose evidence is publicly accessible.

Actual product-validation evidence still depends on real colleagues' feedback/adoption/rejection and cannot be synthesized internally.
