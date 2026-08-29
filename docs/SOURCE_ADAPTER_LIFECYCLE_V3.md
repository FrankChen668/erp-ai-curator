# ERP AI Curator — Source Adapter Lifecycle V3

> Status: design contract for pilot and future Skill packaging. This document defines how a Curator-style orchestration Skill may depend on other Skills/MCPs without becoming an auto-installing plugin manager.

## 1. Positioning

ERP AI Curator is becoming a **bounded orchestration / curator Skill**.

It may rely on external source-acquisition capabilities such as WeChat, Xiaohongshu or Bilibili Skills/MCPs, but it does not own those implementations.

The responsibility split is:

```text
ERP AI Curator
  ├─ understand task
  ├─ decide what evidence is missing
  ├─ choose whether a source-specific capability is worth using
  ├─ route to an approved installed adapter when useful
  └─ evaluate returned evidence and make the final recommendation

Source adapter
  ├─ discover / read one source class
  └─ return original-content evidence + provenance + access limitations
```

This is "meta-Skill-like" behavior, but deliberately bounded to the Curator's evidence-acquisition job.

## 2. Core lifecycle principle

Separate **runtime use** from **dependency maintenance**.

### Runtime curation task

Allowed:

- inspect which approved adapters are already available;
- invoke an installed adapter when it fills a concrete evidence gap;
- fall back to normal Web/GitHub when the adapter is absent or fails;
- report a coverage gap when neither path can obtain the source.

Not allowed by default:

- discover arbitrary new third-party Skills during the user's curation task and install them immediately;
- update an adapter to `latest` mid-task;
- enable new write/account capabilities because a source adapter exposes them;
- silently change a pinned dependency.

### Adapter maintenance task

Installation and update are explicit maintenance operations. They may be performed by a capable local Agent, but they are separate from ordinary resource curation.

This separation makes results reproducible and reduces third-party supply-chain risk.

## 3. Capability-based routing, not product-name routing

The Curator should reason in capabilities such as:

```text
wechat_discover_public_articles
wechat_read_public_article
bilibili_search_public_videos
bilibili_read_transcript
xiaohongshu_search_public_notes
xiaohongshu_read_public_note
```

Do not write product logic such as:

> Always use repository X for every Chinese-source task.

A specific implementation is an **approved provider for a capability**, not the product definition.

This allows an adapter to be replaced later without rewriting the Curator's task logic.

## 4. Minimal adapter registry

Do not build a database.

A small maintained reference is sufficient. For each approved/pilot adapter record only:

```text
Capability
Provider / repository
Pinned commit or release
Install type: Skill / MCP / both
Supported environment
Read-only operations allowed for Curator
Credential requirement
Known limitations
Qualification status: PILOT / APPROVED / CONDITIONAL / REMOVED
Last qualification date
```

The registry is configuration / maintenance evidence, not a resource recommendation catalog.

During the current pilot, the source-adapter architecture and candidate validation docs serve this role. A final Skill may later carry a compact `references/source-adapter-routing.md` instead.

## 5. Installation contract

Installation is only justified after the adapter fills a repeated or material acquisition gap.

Before installation:

1. identify the exact capability gap;
2. select a candidate implementation;
3. pin repository + commit/release;
4. inspect Skill/MCP instructions, manifests, scripts and executable entry points;
5. identify network targets, file writes and credential storage;
6. identify all write/account/social actions;
7. verify supported local environment;
8. run a read-only smoke test with public, non-sensitive content.

Installation succeeds only when the Agent can show:

- what was installed;
- exact pinned version/commit;
- where it was installed/configured;
- which read-only capabilities work;
- which capabilities are intentionally disabled/not used;
- whether login/restart/manual action remains necessary.

Do not install an adapter only because the Curator mentions that platform.

## 6. Update contract

No automatic updates during normal curation.

An adapter update should be an explicit maintenance action:

```text
current pin
   ↓
check upstream changes
   ↓
review diff / release notes / security-relevant changes
   ↓
re-run qualification smoke tests
   ↓
advance pin only if evidence supports it
```

For an update, inspect especially:

- install script changes;
- new dependencies/binaries;
- credential or browser-profile handling changes;
- new network destinations;
- new write actions;
- breaking API/tool-name changes;
- fixes for platform anti-bot or compatibility failures.

If an update is not needed, keep the current qualified pin.

`latest` may be used only as an exploration signal, not as the controlled production/pilot dependency identity.

## 7. Invocation contract

At runtime the Curator follows this sequence:

```text
1. What evidence is missing?
2. Can normal Web/GitHub already obtain it reliably?
3. Is an approved installed adapter available for this capability?
4. If yes, invoke only the read operations needed.
5. Validate returned provenance / original-content status.
6. Return evidence to Curator judgement.
7. Stop using the adapter when the evidence need is satisfied.
```

Examples:

### WeChat

```text
need Chinese practitioner evidence
→ normal Web cannot reliably discover/read WeChat
→ use wechat discovery capability
→ obtain direct mp.weixin.qq.com candidate
→ use public-article reader capability
→ evaluate actual article in Curator
```

### Bilibili

```text
need detailed practitioner tutorial
→ normal Web finds title but not complete content
→ use Bilibili search/transcript capability
→ read transcript for serious candidate only
→ evaluate tutorial quality in Curator
```

### Xiaohongshu

```text
need practitioner field notes and normal Web coverage is weak
→ use search/read capability only
→ do not invoke publish/like/favorite/comment/follow functions
→ return note evidence to Curator
```

## 8. Multi-Skill composition rule

The Curator should not assume it can directly execute another `SKILL.md` as a nested function.

The expected model is:

```text
Curator instructions
→ Codex runtime sees installed Skills/MCP tools
→ Curator states the missing capability / routing intent
→ runtime invokes matching available capability
→ result returns to Curator reasoning
```

Therefore the pilot must test actual multi-Skill/MCP routing in the target Codex environment.

If automatic routing is unreliable, the next escalation is a small explicit routing reference or tool-selection instruction—not immediately a custom orchestration framework.

## 9. Missing-adapter behavior

If a useful adapter is not installed during a normal user task:

Preferred behavior:

1. continue with normal Web/GitHub if possible;
2. state the coverage gap if material;
3. optionally recommend an adapter setup as a separate follow-up action.

Do **not** block the answer only because an optional adapter is missing.

Do **not** silently install third-party executable dependencies mid-task.

## 10. Failure / fallback behavior

If an installed adapter fails:

- do not loop retries indefinitely;
- distinguish login failure, anti-bot failure, version incompatibility and source-not-found;
- try the normal Web path when useful;
- preserve the candidate URL/provenance already obtained;
- report the coverage gap;
- do not downgrade evidence standards just to fill the Practical Companion slot.

Adapter failure is an acquisition failure, not proof that no useful content exists.

## 11. Permission boundary

For Curator use, adapters are read-only research dependencies.

Default allowed:

- search;
- read public detail/body/transcript;
- metadata/provenance;
- public comments when specifically needed as counter-evidence.

Default denied:

- publish;
- edit/delete;
- like/favorite/follow;
- comment/reply/message;
- account administration;
- uploading project/customer material.

If a third-party MCP cannot practically expose a read-only subset, treat it as higher risk and keep it CONDITIONAL until the local qualification proves safe operation.

## 12. Credential boundary

Where login is unavoidable:

- credentials remain local;
- do not put cookies/tokens/passwords into Curator prompts, project docs or Git history;
- prefer tool-native local setup flows;
- use a low-risk/test account where practical;
- record only that credentials are configured, never their values.

A credentialed adapter should never become the only path to produce a useful Curator answer.

## 13. Removal / deprecation

An adapter should be removable without changing the Curator's product logic.

Remove or downgrade it when:

- upstream is abandoned;
- read capability becomes unreliable;
- platform or authentication changes materially;
- security posture worsens;
- another simpler provider fills the capability better;
- repeated tests show no material improvement to recommendation quality.

The Curator should then fall back to the next qualified provider or normal Web coverage.

## 14. What belongs in the future Skill

The main `SKILL.md` should contain only a small routing principle:

> When external discovery needs evidence from a source that normal Web/GitHub cannot reliably acquire, use an already-installed approved source adapter for the missing capability, read-only, then return the evidence to Curator evaluation. Do not install or update third-party adapters during normal curation.

A progressive-disclosure reference such as `references/source-adapter-routing.md` can contain:

- supported capability names;
- approved/pilot providers and pins;
- installation/qualification procedure;
- update procedure;
- invocation examples;
- failure/fallback rules.

Do not put platform-specific installation manuals into the main Skill body.

## 15. Should there be scripts?

Not yet by default.

A deterministic helper such as `adapter-doctor` may become justified if repeated pilots show that checking installed versions, pins and tool availability is error-prone.

Until that failure is observed, avoid adding a package manager, updater or adapter framework merely because the Skill is orchestration-like.

## 16. Success condition

This lifecycle model is useful only if it produces all of the following:

- better source coverage;
- better final recommendation packages;
- controlled third-party dependency risk;
- reproducible local behavior;
- low operational complexity.

If the adapter layer requires constant maintenance or adds mostly low-quality links, reduce it rather than expanding it.
