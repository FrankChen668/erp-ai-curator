# P06 — Excel / CSV / system export → reconcile and validate

Date: 2026-08-30
Status: **ACTIVE — cloud curation complete enough to justify one bounded local runtime delta**

## 1. Real job

A generalized ERP / enterprise-information-system consultant has several Excel / CSV exports from a legacy system, target system, migration template or reference mapping.

By the next review they need a reproducible result that can answer:

- which records match / do not match;
- which fields changed and why;
- duplicates / missing rows / abnormal values;
- whether mapping rules were applied consistently;
- which ambiguous cases require human review;
- whether counts / totals / key fields reconcile back to source;
- how the result can be rerun when a new export arrives.

This is not a generic “AI data analysis” or “Excel formula” task.

Core question:

> **For recurring ERP-style multi-file reconciliation, what AI working method is worth adopting, and when is plain spreadsheet AI enough versus a code-first / Skill-based workflow?**

## 2. Current cloud evidence

### Independent practitioner signal — direct chat is fragile for recurring reconciliation

A July 2026 SME practitioner retrospective reports that repeatedly pasting bank CSVs / memos into ChatGPT or Claude chat was unstable because monthly columns and instructions changed. The useful shift was to freeze the procedure in a reusable file, generate an Excel report, and route ambiguous same-date / same-amount cases to a `Needs Review` sheet rather than guessing.

Source:

- https://note.com/kincapi_claude/n/n4e32c1e8da39

A separate 2026 practitioner failure report describes a three-file reconciliation where conversational transformation produced fabricated / inconsistent output until the task was forced into actual Python execution. The eventual repeatable solution was a Python script plus explicit validation checks.

Source:

- https://www.reddit.com/r/ChatGPT/comments/1r08l15/alert_data_comparison_reconciliation_task_chatgpt/

Older but still useful Excel-practitioner comparison reaches a similar boundary: one-off reconciliation can be faster conversationally, while recurring reconciliation benefits from repeatable Excel / Power Query logic and an audit trail.

Source:

- https://www.excel-university.com/excel-vs-chatgpt/

### Current fact anchor — spreadsheet-native AI is now materially stronger

Current OpenAI material confirms ChatGPT for Excel / Google Sheets can inspect, update and explain workbooks; current desktop Codex can also work with an open Excel workbook through the Excel integration where available. Outputs still require review.

Source:

- https://help.openai.com/en/articles/20001063-chatgpt-for-excel

This means P06 must not assume the only valid path is `local Python + Skill`.

### Strong implementation/method candidate — Huashu-Excel

`alchaincyf/huashu-excel` is a recent MIT-licensed Skill focused on auditable spreadsheet work rather than generic analysis.

Current inspected commit:

- `9348581a87cc03ed8d0b30706631088e922c6027`

Observed design signals:

- inspect workbook structure before flattening;
- preserve / use totals and subtotals as validation signals rather than blindly discarding them;
- cleaning steps are intended to be replayable;
- reconciliation includes count / amount / source-reference checks;
- ambiguous or unproven conclusions are meant to be surfaced rather than guessed;
- independent re-computation / review is part of the method;
- repository contains scripts and documented failure fixes from its own pressure testing.

Evidence role:

> **author-created method + implementation + author-run pressure testing; not independent field validation.**

Sources:

- https://github.com/alchaincyf/huashu-excel
- https://www.woshipm.com/ai/6453768.html

## 3. Cloud preliminary judgement

Do **not** recommend a dedicated Skill merely because the task involves Excel.

Current decision boundary:

- low-risk / one-off exploration: spreadsheet-native AI can be a reasonable first move if the user can inspect the result;
- recurring or high-consequence reconciliation: the important upgrade is **deterministic execution + explicit validation + exception routing + replayability**, not merely a better prompt;
- Huashu-Excel is currently the strongest discovered packaged method matching that boundary, but it is new and self-authored enough that one local delta can materially change whether it deserves recommendation over plain code-first Agent work.

Therefore one local runtime comparison is justified.

## 4. Local Task Envelope

### Objective — fixed

Determine whether Huashu-Excel materially improves an ERP-style reconciliation result compared with a competent plain code-first local Agent.

The test is **not** “can Huashu-Excel run?” and not “which Agent is smarter?”.

It must answer:

> **Would an ERP colleague gain enough accuracy, auditability or lower rework from using this Skill that we should tell them to adopt it instead of simply asking a capable Agent to write/run deterministic reconciliation code?**

### What success means

The evidence should let cloud review judge:

- whether all source rows remain traceable;
- whether duplicates / missing / mismatched records are surfaced correctly;
- whether ambiguous matches are isolated instead of guessed;
- whether the reconciliation can be rerun consistently;
- whether the output contains explicit checks proving row / amount / key-field coverage;
- what extra setup / token / workflow cost the Skill adds;
- whether the Skill changes the recommendation or only documents good practices a plain Agent already follows.

No numeric score is required.

### Execution freedom

Within the hard boundaries below, the local Agent may choose:

- exact synthetic ERP-like fixture design;
- Python / openpyxl / pandas implementation details;
- output workbook / CSV / Markdown evidence format;
- additional checks that genuinely expose a material difference;
- how many internal iterations are useful.

Do not stop to ask for minor execution choices.

### Minimal comparison shape

Use isolated fresh contexts for the two runs so evidence does not leak between them.

**Baseline:** plain local Agent with code execution, given only the P06 job + test input files. Do not expose Huashu-Excel or its rules.

**With Skill:** fresh context, same job + same input files, allowed to read the pinned Huashu-Excel repository / `SKILL.md` and use its bundled scripts where useful.

A separate fixture-builder step may create synthetic data and a hidden ground-truth record. The run contexts must not see that ground truth before producing their outputs.

The fixture should be realistic enough to include several materially different reconciliation problems, for example:

- renamed / reordered columns;
- whitespace / casing / leading-zero key differences;
- duplicates;
- missing records;
- changed field values;
- an ambiguous duplicate-key or same-value match that should go to review;
- one transformation / mapping rule;
- at least one source count or total that can act as a deterministic check.

Do not optimize the fixture to match Huashu-Excel's README demo.

### Hard boundaries

Local Agent must not:

- modify ERP AI Curator principles, North Star, source strategy or Loop policy;
- broaden into P03 / P05 / other Problem Cards;
- search the Web again unless a runtime-blocking implementation fact is genuinely missing;
- globally install Huashu-Excel or modify global Agent configuration;
- use confidential / customer / production data;
- add credentials or external SaaS accounts;
- install unrelated Skills / MCPs / adapters;
- turn this into a benchmark framework or generalized scoring system;
- treat author pressure tests as independent validation;
- judge success by output polish alone.

For the candidate, prefer a temporary isolated clone / checkout at:

`9348581a87cc03ed8d0b30706631088e922c6027`

Running repository scripts from that isolated copy is allowed after a quick dependency / mutation check. Do not persist installation after the test.

### Stop condition

Stop as soon as the comparison can answer one of these:

1. Huashu-Excel adds a material, reusable advantage over plain code-first Agent work;
2. plain code-first Agent already achieves the same important controls with lower adoption cost;
3. results are genuinely inconclusive and one specific unresolved risk would change the recommendation.

Do not run more variants merely because more tests are possible.

### Escalate only if

- a test requires credentials / account login;
- the candidate unexpectedly performs risky system / network mutations;
- a new external installation is necessary beyond ordinary existing Python dependencies;
- the P06 real-job definition itself appears wrong;
- the evidence points to a product-direction decision rather than an execution detail.

Everything else: decide locally and continue.

## 5. Local evidence return contract

Return one compact evidence package:

### Verdict proposal

`HUASHU MATERIAL ADVANTAGE` / `PLAIN CODE-FIRST ENOUGH` / `INCONCLUSIVE`

### Baseline result

- approach actually used;
- important checks present / absent;
- errors or rework observed;
- artifact paths.

### With-Skill result

- which Huashu guidance/scripts materially changed behavior;
- important checks present / absent;
- errors or rework observed;
- artifact paths.

### Ground-truth comparison

- what each run got right;
- what each missed;
- any silent errors;
- how ambiguous cases were handled.

### Adoption cost

- setup;
- dependencies;
- workflow overhead;
- portability observations.

### Adversarial finding

The strongest reason **not** to adopt the apparent winner.

### Stop rationale

Why another runtime variant is or is not likely to change the recommendation.

### Owner/cloud decision needed

`None` unless one of the escalation conditions was actually hit.

## 6. Cloud review after local return

Cloud will not blindly rerun the local experiment.

Cloud will:

- inspect the evidence package and key artifacts;
- challenge the recommendation with the already-collected practitioner evidence;
- decide the final P06 package and stop point;
- update repository evidence status.
