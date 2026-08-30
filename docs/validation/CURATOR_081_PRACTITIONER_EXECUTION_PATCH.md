# Curator 0.8.1 — Practitioner Execution Patch

Date: 2026-08-30
Status: **PATCH IMPLEMENTED — CLEAN ORIGINAL-HOST RE-RUN STILL REQUIRED**

## 1. Trigger

A Codex Desktop execution log was provided for the natural request:

> “使用这个 skill 给我找下做流程图的最佳实践”

The resulting answer again centered on generic flowchart guidance and official/standard sources instead of the expected AI-enabled practitioner ecosystem.

## 2. Evidence boundary

This run is **not** a clean isolated 0.8.0 evaluation.

Execution sequence included:

1. local Skill 0.6.1 loaded;
2. a proposed local 0.6.2 edit was made;
3. an initial official-heavy search batch ran;
4. user interrupted and required GitHub sync;
5. repository fetched `main` at `d6165fa`;
6. Skill package restored to exact 0.8.0 Git blobs;
7. 0.8.0 SKILL + both references were read;
8. a second search batch ran in the same context.

Therefore the full final answer cannot be attributed to fresh 0.8.0 behavior alone.

## 3. What the post-sync logs directly prove

### 3.1 Skill/reference loading worked

After sync, the local hashes matched `origin/main` for:

- `SKILL.md 0.8.0`;
- `references/practitioner-discovery.md`;
- `references/evidence-and-safety.md`.

The practitioner reference was explicitly read before the second search batch.

So the primary failure is not “reference never loaded”.

### 3.2 Search intent drift occurred

The second search batch included queries such as:

- `流程图 最佳实践 业务流程 泳道 决策 分支 可读性 实操`
- `企业流程图 画法 最佳实践 业务分析 泳道图 复核`
- `BPMN process modeling best practices official notation readable maintainable`
- `Mermaid flowchart best practices version control render official GitHub`

The original product intent—**AI/Agent/Tool applied by product/ToB/ERP practitioners to improve flowchart work**—was largely lost.

This is the strongest direct runtime defect signal.

### 3.3 Practitioner pools were named in the loaded reference but not executed

The loaded reference explicitly listed Bilibili, WeChat, Xiaohongshu, Zhihu, 人人都是产品经理, 掘金/CSDN and practitioner blogs.

Actual platform-targeted search in this run:

- Bilibili: no;
- WeChat: no;
- Xiaohongshu: no;
- Zhihu: no;
- 人人都是产品经理: no;
- 掘金/CSDN: no.

This does not justify platform quotas. It proves only that the practitioner discovery instruction did not translate into high-signal search actions.

### 3.4 Practitioner candidate investigation failed

The second search result set did contain Chinese creator/practitioner-style candidates, including items from 墨刀, 简道云, ProcessOn, 博客园 and others.

Most were not opened. The final answer instead used Microsoft, WCO, ISO, Mermaid and GitHub Docs.

Final source roles contained no independent practitioner and no author self-practice recommendation.

So the second direct defect is:

> **candidate discovery did not become candidate investigation.**

## 4. Separate host/Harness risks — not yet Curator rules

### H1 — source-policy conflict

Codex Web policy exposed a rule equivalent to:

> technical questions → rely on primary sources.

This can potentially conflict with Curator's practitioner-first product goal if the host classifies the request as technical.

The log does **not** prove this policy caused the final output, so 0.8.1 does not attempt to override or work around host policy.

### H2 — Skill collision

`graph-engineering` was additionally loaded because the task was treated as multi-step.

This appears unrelated to the user's request and suggests a host Skill-routing/over-triggering issue. It is not patched inside Curator.

### H3 — source-acquisition fallback

Browser/Chrome capabilities existed but were not used.

The log does not establish whether using them would have materially improved Bilibili/WeChat/Xiaohongshu acquisition, so 0.8.1 does not mandate browser escalation.

## 5. First-principles correction

The Curator's differentiating value is not “know more flowchart rules”. It is:

```text
preserve the user's AI-workflow problem
→ discover real practitioner methods in that context
→ investigate serious candidates
→ verify only the facts needed to trust/adopt them
→ select a few
```

Two execution requirements are therefore justified by direct evidence.

## 6. 0.8.1 runtime changes

### Change A — query intent preservation

If the user asks how AI/Agent/Tool improves a task, at least one serious discovery query must keep both:

- AI/tool dimension;
- role/industry/artifact context.

A discovery batch that collapses into pure domain search is intent drift.

### Change B — practitioner candidate investigation

For an explicit best-practice/tutorial request:

- inspect at least one practitioner/creator candidate before synthesis;
- if host source policy, search coverage or access controls prevent this, report `coverage/policy gap`;
- do not silently substitute official documentation and claim practitioner curation complete.

## 7. Adversarial review of the patch

### Attack A — Does this re-create a rigid framework?

No. No new categories, scoring, Gate, reference file or output taxonomy is added.

### Attack B — Does “at least one practitioner” force low-quality secondary sources?

No. The requirement is to **inspect**, not blindly recommend. If inspection shows poor fit, it can be rejected. If host policy prevents inspection, report the gap.

### Attack C — Does this force Bilibili/WeChat/Xiaohongshu every time?

No. There is no platform quota. The requirement is to preserve AI-workflow intent and investigate a serious practitioner candidate where the request explicitly asks for practices/tutorials.

### Attack D — Are we trying to override a host system policy from a Skill?

No. 0.8.1 explicitly treats host policy as a compatibility boundary. Higher-priority host rules remain authoritative.

### Attack E — Should Browser/Chrome be mandatory fallback?

Not yet. The provided log did not first exhaust a correct AI/role practitioner search, so browser escalation is not yet proven necessary.

### Attack F — Should Graph Engineering exclusion be added to Curator?

No. Skill collision belongs to host routing or the other Skill's trigger/description, not Curator runtime.

## 8. Acceptance boundary

0.8.1 is accepted for controlled trial if:

- Project Contract passes;
- runtime remains structurally simple;
- no removed 0.8.0 taxonomy/reference returns;
- Current docs consistently identify 0.8.1 and the evidence boundary above.

This does **not** prove the patch works in Codex Desktop.

## 9. Next evidence

Run the same natural prompt once in a **fresh Codex Desktop context** after syncing current `main`:

> “使用这个 skill 给我找下做流程图的最佳实践”

Do not pre-seed expected platforms or desired links. Do not modify the Skill.

Capture only observable execution facts:

- loaded Skill/version/references;
- actual search queries;
- practitioner candidates opened;
- final source roles;
- any explicit host policy/coverage failure.

That run determines whether the remaining problem is Curator instruction execution, host source policy, search coverage, Skill collision or source acquisition.
