# Source Composition — Uncertainty / Owner Challenge

Date: 2026-08-31
Status: **OPEN QUESTION — DO NOT TREAT AS A CLOSED ARCHITECTURE VERDICT**

## 1. Trigger

A local P5 mature-Skill composition run was reported after the `reuse-before-build` architecture correction.

Owner-reported summary:

- `last30days-cn` added five Bilibili candidates;
- those candidates did not become inspectable original evidence in that run;
- Xiaohongshu / Zhihu / WeChat produced no effective gain in that run;
- `web-access` was not exercised because the existing Chrome instance did not have CDP enabled;
- Runtime Skills were not changed and no new platform Adapter/MCP was developed;
- the Local Agent proposed `CONDITIONAL`, discovery-only use.

At the time of this note, the corresponding P5 result file/commit had not yet been independently reviewed by Cloud from the remote repository. Treat the summary above as Owner-reported execution evidence, not a fully accepted evidence package.

## 2. Owner challenge

Owner explicitly does **not** accept the stronger Cloud inference that this run proves mature-Skill composition is insufficient or that the project should close the source-acquisition problem and move on.

That stronger inference is therefore withdrawn as a project conclusion.

## 3. Why the evidence is currently inconclusive

The reported P5 run does not establish that mature-Skill composition works, because:

- no serious new candidate was converted into inspected original evidence;
- no final recommendation delta was demonstrated;
- several target source classes produced no effective gain.

But it also does not establish that mature-Skill composition fails, because:

- Candidate A was primarily a discovery/recall layer and did add new Bilibili candidates;
- Candidate B was the original-page reading fallback and was **not actually exercised** due the CDP boundary;
- therefore the intended composition path `discovery → original-page reading → Curator judgement` was not completed end to end;
- one bounded task/run is insufficient to reject the broader reuse-before-build strategy.

## 4. Current project position

The correct status is:

> **MATURE-SKILL COMPOSITION EFFECTIVENESS — INCONCLUSIVE / OPEN.**

Do not record either of these as established:

- “mature Skills solve the Chinese-source acquisition problem”;
- “mature Skills do not solve it, so source acquisition should be abandoned.”

The reusable architectural principle remains:

> **Reuse before build.** Prefer an existing mature capability over ERP-owned source infrastructure when it can satisfy the task at proportionate cost.

This principle is separate from the unresolved empirical question of whether the current candidate combination is good enough.

## 5. Boundaries while the question remains open

Do not:

- patch Runtime 0.9.1 based on the reported P5 result;
- resume one-provider-per-platform engineering merely because P5 was inconclusive;
- mark `last30days-cn` or `web-access` as permanent Runtime dependencies;
- mark the source-acquisition problem as closed;
- require platform-complete coverage;
- turn the uncertainty into another synthetic benchmark loop solely to fill evidence slots.

Further evidence should be collected only when it can materially resolve the open question, preferably in a real ERP/ToB task where source discovery and original inspection can both affect the final recommendation.

## 6. Authority implication

This note supersedes any informal same-session statement that P5 alone justifies stopping Source Acquisition work.

It does **not** supersede:

- the P0–P4 evidence about real Chinese-source recall/access gaps;
- the rejection of disproportionate ERP-owned platform engineering;
- the `reuse-before-build` architecture direction;
- the requirement that final recommendations rely on inspectable current evidence.
