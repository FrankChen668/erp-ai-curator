# ERP AI Curator — Adversarial Release Readiness Review

Date: 2026-08-30
Status: **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**
Skill: `curating-erp-ai-resources` `0.7.0`

## 1. Decision under attack

The claim being tested is:

> “ERP AI Curator 0.7.0 is ready to give to users and the planned product goal is complete.”

Adversarial verdict:

> **Half true. Controlled real-user trial is ready. The North Star outcome goal is not complete/validated. Broad organization/public release is premature.**

## 2. Goal-by-goal verdict

### Goal A — Build a coherent Curator method

**PASS for pilot.**

The project now has a stable method:

`real task + current baseline + hard constraints → capability gap → practitioner/implementation/current facts → compact adoption recommendation`.

A/B/C boundaries are coherent enough to expose to real users.

### Goal B — Package the method as a reusable Skill

**PASS for pilot.**

0.7.0 has:

- a bounded trigger;
- progressive-disclosure references;
- no scenario taxonomy/resource database/scoring Gate;
- deterministic project-contract checks outside the judgment workflow;
- explicit evidence/safety/permission boundaries.

### Goal C — Demonstrate discrimination across real-origin ERP problems

**PASS for pre-user readiness, not product value.**

Curation Pack 01 contains:

- B — ERP manual capture/maintenance capability;
- B — Oracle EBS context engineering;
- A — weekly report consolidation, no new Tool/Skill;
- A → conditional B — SAP bug diagnosis depending on system evidence access.

This is enough to stop internal pack expansion.

### Goal D — Make the Skill consumable by a normal trial user

**PASS after adding `docs/USER_TRIAL_GUIDE_V1.md`, with compatibility limits.**

The user no longer needs to understand project history/validation docs. The trial guide explains package contents, natural input, expected output, Web/security boundaries and feedback expectations.

Compatibility is **not** proven across all hosts.

Historical internal regression exercised a prior Skill version in isolated Codex contexts. That supports Codex as a credible pilot host path but does not prove 0.7.0 works identically in ChatGPT, WorkBuddy, Qoder, Claude Code or every Agent Skills host.

### Goal E — Prove Curator creates more user value than ordinary AI/self-search

**FAIL / NOT YET TESTED BY REAL USE.**

Current evidence does not establish:

- repeatable time savings;
- less search/selection effort;
- fewer wrong-tool decisions;
- less downstream rework;
- higher trust;
- repeat usage;
- stable uplift over ordinary AI/self-search.

This is the actual North Star outcome gap.

## 3. Strongest reasons NOT to broad-release yet

### R1 — No REAL_USER_USE evidence

Survey demand and Cloud-curated real-origin cases are not user adoption/outcome evidence.

### R2 — Cross-host behavior is unvalidated

A Skill is not useful if the actual employee host cannot import references, access Web, trigger reliably or respect the same permissions. Do not infer compatibility from the format alone.

### R3 — External evidence acquisition varies by host

B-class recommendations often need Web/search/fetch. A host without usable network access can still frame A/B/C or analyze supplied resources, but cannot honestly claim current internet curation.

### R4 — Domain/version/environment diversity is large

SAP/Oracle/ERP recommendations are sensitive to version, deployment model, enterprise policy, system access and customer-data boundaries. 0.7.0 correctly exposes these as constraints, but real use is still required to test whether users provide enough context and whether the Skill notices what matters.

### R5 — Public/open-source distribution is not yet legally packaged

The repository is public but currently has no repository `LICENSE` file.

This does **not** block a controlled internal/user trial where access/use terms are otherwise clear. It does mean a clean public/open-source release should not be declared complete until the Owner deliberately chooses the licensing approach. The project must not silently invent that choice.

## 4. Strongest reasons a controlled user trial IS justified

- method skeleton has converged across heterogeneous tasks;
- known over/under-tooling regressions led to narrow Harness fixes;
- Pack 01 demonstrates both “do not add a tool” and “specialized capability is justified” behavior;
- evidence roles and strong-language boundaries are explicit;
- runtime/system access is conditional and read-only first;
- project facts are mechanically checked;
- more internal testing now has declining information value compared with actual user use.

## 5. Release classes

### GO — Controlled trial

Use 0.7.0 with a small number of real ERP/enterprise-information-system users in a known/approved host.

Do not prescribe benchmark tasks. Let users ask natural questions.

### HOLD — Organization-wide standard

Do not yet designate Curator as the standard way all colleagues must choose AI methods.

Wait for repeated real-user evidence and host compatibility observations.

### HOLD — Public/open-source release claim

Before calling the repository a clean open-source release, Owner must decide licensing and public distribution expectations.

## 6. What completion now means

The **build/readiness milestone** is complete when this release-readiness change is merged and project contract passes.

The **product/North Star outcome milestone** is not complete until REAL_USER_USE answers:

> **Is Curator's recommendation consistently more useful/trustworthy/lower-noise than the user's ordinary AI or self-search, enough that users would return?**

These two milestones must never be collapsed again.

## 7. Next phase

After merge:

> **CONTROLLED REAL_USER USE — no more pre-user Skill polishing by default.**

Collect natural user signals only. Change Skill 0.7.0 only for concrete recurring defects or compatibility blockers.
