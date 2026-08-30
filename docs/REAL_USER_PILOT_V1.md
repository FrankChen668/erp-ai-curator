# ERP AI Curator — Real User Pilot V1

Date: 2026-08-30
Status: **READY TO START — requires real colleague tasks**

## 1. Pilot objective

Do not prove that the Skill can produce polished answers.

Test the product question that internal validation cannot answer:

> **When a real ERP / enterprise-information-system colleague has a real work task, does the Curator help them choose a better AI working method and actually start/complete the work with less wrong-tool selection, search/setup effort or avoidable rework?**

## 2. Pilot input

Use real colleague work only.

Each run should start from the smallest useful task description:

```text
role / project context
+ actual materials available
+ concrete action/problem
+ expected deliverable
+ material constraints
```

Do not require the user to classify the task into P01–P14.

Do not upload confidential artifacts unless the organization’s data policy permits the selected AI/tool path. Descriptions or redacted samples are acceptable when necessary.

## 3. Minimal pilot shape

Start small: a few colleagues with one real task each are enough to expose the first adoption failures.

Prefer natural diversity from actual work rather than quotas. Useful variation may include consultant/PM/developer work, document/visual/data/code tasks, cloud/local constraints and tasks where the correct answer is “do not install another tool”.

Do not manufacture tasks merely to cover categories.

## 4. What the Curator returns

Use `skills/curating-erp-ai-resources/SKILL.md`.

The recommendation should remain compact:

1. conclusion — ordinary AI enough / specialized option worth it / low-cost trial first;
2. why — only decision-changing reasons;
3. `input → operation → output → review` workflow;
4. 0–1 primary external resource by default, second only for a materially different boundary;
5. major risk/constraint;
6. immediate trial action.

## 5. What to capture after the colleague acts

Do not create a long survey. Capture only evidence that can change the product:

### Before action

- real task in the colleague’s own words;
- materials/constraints that affected the recommendation;
- Curator recommendation actually given.

### After action

- what the colleague actually tried;
- whether they followed, modified or rejected the recommendation, and why;
- what usable artifact/result they reached;
- where the recommendation saved search/setup/rework, if anywhere;
- where it caused confusion, wrong-tool adoption, missing capability or extra work;
- any material enterprise/privacy/permission issue missed by the Curator;
- whether they would use this type of recommendation again for another real task.

Short free-text is preferable to artificial scoring.

## 6. Pilot evidence hierarchy

Strong evidence:

- colleague actually used the recommendation on a real task;
- concrete artifact/workflow/result exists;
- observed correction/rework or adoption decision is attributable enough to inspect.

Weaker but still useful:

- colleague rejects the recommendation before trying it and gives a concrete reason such as setup cost, wrong environment, missing permission or task mismatch.

Not product evidence:

- Curator answers an invented prompt successfully;
- Owner or Agent says the recommendation “looks good”;
- another synthetic benchmark passes;
- more resource links are collected without colleague action.

## 7. Failure signals to act on immediately

A single real case can justify correction when it exposes a clear method defect, for example:

- Curator searches for tools although ordinary AI was obviously enough;
- important task input/constraint was ignored;
- recommended resource cannot actually handle the supplied artifact/environment;
- recommendation depends on model memory for ERP business truth;
- privacy/write/permission boundary was missed;
- user cannot tell what to do next;
- recommendation adds more setup/search effort than it saves;
- source evidence was overstated or not actually acquired.

Fix the narrow recurring defect. Do not create a new framework for one unusual case.

## 8. What success looks like

Do not declare PASS from a numeric threshold in advance.

The pilot is moving in the right direction when real colleagues repeatedly show that:

- the recommendation makes the next action clearer;
- they can start from their actual project materials;
- unnecessary Tool/Skill adoption is avoided;
- specialized capability is recommended for an observable reason;
- important limitations are surfaced before they create rework;
- the result is useful enough that they would bring another real task.

The strongest negative signal is repeated non-use: recommendations are technically reasonable but colleagues do not act because the workflow is too heavy, too generic or not sufficiently better than asking their existing AI directly.

## 9. Current cloud/local responsibility

Cloud/ChatGPT can continue to:

- run Curator recommendations for submitted real tasks;
- research current resources when needed;
- inspect evidence and update the method;
- maintain GitHub authorities.

A local Agent is used only when a real pilot task genuinely needs local files/repository/runtime evidence.

## 10. Stop / next decision

Do not return to internal card accumulation while real pilot evidence is available.

After several genuine uses, reassess from observed patterns:

- keep V0.1 unchanged;
- make a narrow method correction;
- add one reusable support artifact because users repeatedly need it;
- or conclude that Curator adds too little value over ordinary Agent use.

## 11. External dependency

Cloud preparation is complete when this document and the pilot Skill are merged.

Actual pilot evidence requires a **real colleague to submit/use a real work task**. That is the next evidence source and cannot be synthesized internally.
