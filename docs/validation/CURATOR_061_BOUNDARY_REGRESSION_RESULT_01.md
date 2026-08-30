# Minimal Curator V0.1 / Skill 0.6.1 — Boundary Regression Result 01

Date: 2026-08-30
Status: **CLOSED — KEEP 0.6.1 UNCHANGED; RETURN TO REAL_USER PILOT**

Authority / plan:

- `docs/validation/CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`
- Skill under test: `skills/curating-erp-ai-resources/SKILL.md` version `0.6.1`
- tested main baseline: `f8f5711f6ebc6e74f0b90a6ca2e9b47e63714a5c`

## 1. Execution integrity

The Local Agent created 11 isolated Codex contexts:

- 5 Baseline runs;
- 5 Curator 0.6.1 runs;
- 1 fresh independent evaluator.

Each execution run used a separate detached worktree and no shared conversation history. Repository files were not modified. Runtime was not used. External search occurred only in Case 5 Baseline.

This satisfies the planned isolation requirement well enough for a bounded internal regression.

## 2. Cases

Survey-derived cases:

- 65 — project weekly report integration;
- 8 — large ERP operating-manual generation/maintenance;
- 5 — Oracle EBS development AI working method;
- 75 — non-ABAP consultant bug localization;
- 38 — ETL/system diagnosis, performance and automatic remediation.

## 3. Main observations

### No over-tooling signal

Curator 0.6.1 did not force Tool / Skill / MCP adoption in any case. This confirms that the General-AI-first guardrail remains strong.

### Under-tooling signal exists, but attribution is limited

The evaluator found the clearest under-tooling in:

- **Case 5** — Baseline retained Oracle EBS official documentation/project context as a useful specialized capability, while Curator returned no specialized resource;
- **Case 38** — Baseline retained a read-only diagnostic Tool/MCP layer for logs/code/database metadata/execution plans/monitoring, while Curator returned no specialized resource.

Case 8 showed a lighter version of the same conservatism around high-volume screenshot/manual maintenance.

However, the current Skill already contains the permanent rules needed to reach the stronger branches:

- upgrade by a concrete capability gap;
- system/repository access can be a real bottleneck;
- permissions/data boundaries matter;
- a specialized capability is justified when its observable benefit exceeds adoption cost.

`references/decision-boundaries.md` also explicitly says real codebase/ERP-object access can justify Tool/MCP escalation.

Therefore the observed misses are better classified as **execution sensitivity / model variance under an already-present rule**, not as proof that the permanent Skill lacks that rule.

### `C` misuse was not confirmed

The first local pass raised a concern that `C` was being used as a synonym for missing information. The isolated regression did not confirm that as a recurring defect. Runs generally paired low-cost trial recommendations with named upgrade conditions.

### Multi-problem decomposition defect was not confirmed

Case 8 correctly separated three different problems and focused the detailed scenario on the operating-manual task. Case 38 compressed several related operations concerns, but this did not recur strongly enough to justify a permanent new decomposition rule.

## 4. Curator vs ordinary Agent

No case showed a clear, repeatable adoption-decision advantage for Curator over Baseline.

Observed pattern:

- Case 65 / 8 / 75: decisions were broadly similar;
- Case 5 / 38: Curator was in places more conservative than Baseline;
- Curator preserved good safety and low-cost trial discipline, but did not demonstrate a strong incremental adoption advantage in this bounded exercise.

This matters: the regression does **not** validate Curator product value over ordinary Agent use.

## 5. Adversarial attribution review

Why not patch `SKILL.md` now:

1. the strongest misses are already covered by current permanent rules;
2. only one frozen run per arm was executed, so stochastic execution variance remains plausible;
3. Case 5 had asymmetric research behavior — Baseline independently chose external research while Curator did not — which is a real behavioral difference but also increases single-run variance;
4. Case 38 is a cleaner under-tooling signal because neither arm used external research, yet the missing branch is already explicitly described in the current Skill/reference;
5. adding another permanent rule would risk wording inflation without evidence that the rule itself is absent.

Therefore the correction target is **not the Skill text** at this point.

## 6. Decision

> **KEEP SKILL 0.6.1 UNCHANGED.**

Do not add:

- another under-tooling rule;
- another scenario example;
- a mandatory “must recommend a resource” check;
- a scoring/Gate mechanism;
- more internal regression cases by default.

The bounded regression has answered its question sufficiently:

- over-tooling: not observed;
- under-tooling: observed in some runs;
- permanent-rule defect: not established;
- `C` semantic defect: not established;
- broad internal validation: not justified.

## 7. Evidence boundary

This result is **internal bounded regression evidence only**.

It is not:

- REAL_USER adoption evidence;
- proof of time savings or lower rework;
- proof that Curator outperforms an ordinary Agent;
- product validation.

The next decision-changing evidence remains real colleague action on a real work task.

## 8. Stop decision

This regression is closed.

> **Return to `docs/REAL_USER_PILOT_V1.md`. Do not run another internal boundary test unless real use exposes a new concrete blocker/defect.**
