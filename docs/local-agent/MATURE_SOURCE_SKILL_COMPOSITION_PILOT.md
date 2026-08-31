# Mature Source Skill Composition Pilot

Date: 2026-08-31
Status: **LOCAL QUALIFICATION TASK — REUSE BEFORE BUILD**

## Goal

Test whether existing mature Skills can provide the Chinese-platform evidence acquisition the Curator needs, without ERP AI Curator owning platform crawlers/MCP implementations.

Do not modify either Runtime Skill.

Do not invoke unrelated engineering Skills merely because this is a multi-step task.

## Architecture under test

```text
Curator
→ normal Web / GitHub
→ last30days-cn for Chinese-platform candidate discovery when recall is weak
→ web-access only if a serious candidate requires dynamic/login-state original reading
→ Curator evaluates evidence independently
```

External Skill ranking is discovery-only. Do not copy its ranking into the Curator answer.

## Candidate A — cross-platform discovery

Repository:

`Jesseovo/last30days-skill-cn`

Controlled commit:

`1a8a04c3c347defbcdbb8da26d7cf1a531426b1f`

Role:

- discover current Chinese-platform practitioner candidates;
- especially Bilibili / Xiaohongshu / Zhihu / WeChat when normal Web coverage is weak;
- return compact evidence/provenance for Curator inspection.

### Phase A1 — static/read-only qualification

Check only what is needed to run it as a Skill:

- exact pinned commit;
- license;
- `SKILL.md`;
- script entry point;
- documented runtime dependencies;
- documented credential/browser requirements;
- obvious write/account/social actions.

Do not re-audit every platform implementation line by line. This pilot tests a mature external Skill as a black-box dependency, not each underlying site connector as our code.

### Phase A2 — minimal isolated run

Use existing host Python if available. Do not install system Python/SDK/package managers.

Do **not** install Playwright or a separate Chromium at the start.

First run the Skill's diagnostic path using only already-available runtime/dependencies. Record which sources are usable without additional setup.

Then use this real task:

> `AI ERP/ToB 需求访谈 会议纪要 需求分析 PRD FS 最佳实践 实操`

Run the mature Skill with a reasonable recent window and compact/JSON output. Prefer explicit source selection for the practitioner ecosystems likely to matter.

Record:

- sources attempted;
- sources actually returning candidates;
- top serious candidate titles/URLs/authors/dates;
- whether Xiaohongshu / Bilibili / Zhihu / WeChat contribute anything normal Web missed;
- setup time and operational friction.

If a source requires optional credentials or Playwright, record that boundary. Do not configure credentials or install a browser merely to fill the matrix.

### Phase A3 — Curator comparison

Compare the new leads with the existing P4 Web-only package.

A mature Skill is useful only if it provides at least one serious new lead or a materially clearer coverage boundary at proportionate cost.

Do not accept metadata-only content as a final recommendation. Serious external candidates still require original inspection.

## Candidate B — original-page reading fallback

Repository:

`eze-is/web-access`

Controlled commit:

`33eef84a55b1919396a80e7a55650a07bb83f590`

Role:

- read a serious dynamic/login-state original page using the Owner's existing Chrome/Edge browser;
- avoid a platform-specific custom browser/runtime.

### Trigger

Do not install/test Candidate B unless Candidate A or normal Web produces a **serious candidate that cannot otherwise be inspected** and original inspection could change the Curator decision.

If no such candidate exists, mark Candidate B `NOT NEEDED IN THIS RUN` and stop.

### Phase B1 — boundary check

Before use, confirm:

- Node.js requirement is already satisfied; no system runtime install;
- Chrome/Edge already exists;
- no new separate Chromium download is required;
- CDP/remote-debugging setup is the only Owner-local browser boundary;
- the Skill can create its own background tab rather than mutate an existing user tab.

### Phase B2 — read-only use only

Allowed:

- open/navigate/search;
- read DOM/text/metadata;
- scroll only when necessary to load public content;
- close the Skill-created tab when done.

Forbidden:

- publish/upload;
- comment/reply;
- like/favorite/follow;
- message;
- form submission that changes account/site state;
- reading unrelated user tabs/history/cookies;
- exporting credentials/session data.

If browser remote debugging requires Owner action, stop and provide the minimum instruction. Do not change browser launch flags/profile automatically.

## Evidence output

Create:

`docs/validation/source-acquisition-pilot/P5_MATURE_SKILL_COMPOSITION_RESULT.md`

Required sections:

1. exact task and host;
2. Candidate A pinned version and diagnostic result;
3. normal Web baseline reference;
4. mature-Skill discovery results by source;
5. serious new candidates and whether original pages were inspected;
6. Candidate B used / not needed / blocked;
7. recommendation delta versus Web-only;
8. setup/maintenance/security cost;
9. final local proposal:
   - `USE AS COMPOSED DISCOVERY CAPABILITY`
   - `CONDITIONAL`
   - `NOT MATERIAL`
   - `REMOVED`

Cloud owns the final architecture decision.

## Stop rules

Stop rather than engineer around the external Skill when any of these occurs:

- it requires system-wide runtime/SDK/package-manager installation;
- it requires building/forking/modifying its platform connectors;
- it requires a new large browser runtime merely to qualify a source;
- the only gain is more metadata links with no inspectable evidence;
- a provider-specific failure would require us to patch upstream code;
- the test starts turning into a new adapter framework.

## Success condition

The composition hypothesis passes only if:

> mature Skills provide materially better Chinese-platform evidence coverage at lower ownership/maintenance cost than the P0–P4 per-platform adapter path.

If not, report the gap and stop. Do not fall back to building our own platform stack by default.
