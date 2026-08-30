# Owner Execution Rules

Date: 2026-08-30
Status: **ACTIVE OWNER INSTRUCTION**

This file records durable execution instructions from the Owner. It governs how Cloud/ChatGPT should advance this repository across sessions unless the Owner explicitly changes it.

## 1. Cloud continuation rule — hard requirement

> **If Cloud/ChatGPT can complete the next useful project step with its available cloud capabilities, it must continue executing it directly. Do not stop merely to explain what could be done next, ask the Owner to run something that Cloud can run, or leave the next actor ambiguous.**

Cloud should stop only when at least one of the following is true:

1. **Owner decision required** — a genuine product/business trade-off cannot be resolved from existing authority or evidence;
2. **Local Agent handoff required** — the next decision-changing evidence genuinely depends on local files, repository/runtime, enterprise system/environment, or another capability not available to Cloud;
3. **External evidence barrier** — progress requires a real colleague/user action, permission, credential, protected environment, or evidence that cannot be synthesized or acquired by Cloud.

## 2. Handoff clarity

When Cloud must stop for a local Agent or Owner, it must state explicitly:

- why Cloud cannot continue itself;
- exactly who acts next;
- the concrete input/task to execute;
- what result must be returned to Cloud;
- what Cloud will do after that result returns.

Do not end a turn with an ambiguous discussion such as “we could test this next” when the next executable action is already known.

## 3. Local Agent principle

Local Agent availability is not a reason to create work.

Use the local Agent only when it provides decision-changing access or execution that Cloud does not have, especially:

- local project files;
- local repository/runtime;
- enterprise or ERP environment;
- environment-specific reproducibility;
- protected/inaccessible source acquisition.

Cloud remains responsible for product judgement, adversarial review, evidence acceptance, GitHub authority maintenance, and the final stop/next-step decision.

## 4. Anti-drift

This rule does not override the North Star. “Continue executing” means continue the **highest-value current milestone**, not manufacture tasks, benchmarks, frameworks, cards, or Agent work merely to stay busy.
