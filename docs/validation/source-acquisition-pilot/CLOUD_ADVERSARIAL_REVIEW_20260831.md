# Source Acquisition Pilot — Cloud Adversarial Review

Date: 2026-08-31
Status: **P0–P3 PILOT REVIEW COMPLETE / RUNTIME 0.9.1 REMAINS FROZEN**

## 1. Evidence reviewed

Cloud reviewed the final staged Source Acquisition evidence:

- `P0_TARGETED_WEB_RESULT.md`
- `P1_WECHAT_RESULT.md`
- `P2_BILIBILI_RESULT.md`
- `FINAL_SOURCE_ACQUISITION_COMPARISON.md`
- `P3_XIAOHONGSHU_RESULT.md`

P3 remote evidence branch: `validation/source-acquisition-pilot-p3-xiaohongshu`, commit `2b92eebe`.

Important distinction:

> Provider qualification and platform-value qualification are separate. A provider may be removed even when the platform remains an unresolved coverage gap.

## 2. Cloud status decisions

The Local Agent statuses are evidence inputs. Cloud owns architecture/promotion decisions.

### Targeted normal Web — BASELINE / KEEP

Observed value:

- broad Web missed multiple Chinese practitioner ecosystems;
- targeted `site:` queries materially improved Bilibili and, in one run, Zhihu recall;
- WeChat and Xiaohongshu remained zero-recall through normal Web;
- Bilibili readability varied by run.

Decision:

> Keep targeted normal Web as the lowest-cost first fallback. It is useful but not sufficient as the only acquisition path.

### WeChat adapter — PILOT (strong positive), not yet APPROVED

Direct evidence is strong:

- normal Web returned zero WeChat candidates;
- pinned `wechat-article-search` returned fresh task-matched candidates in two local executions;
- URL resolution succeeded on tested samples;
- multiple original public-account articles were successfully read;
- acquired evidence added product-manager/process-management/tool-builder perspectives absent from P0;
- no user credentials or social write actions were required.

`APPROVED` remains too strong because:

1. qualification is still from one task family (AI flowchart practice);
2. one installation reported a high-severity transitive npm vulnerability whose practical significance has not been independently closed;
3. full original-content reading depended on a separate read-only public-article reader;
4. repeatable material value across a second ERP/ToB task has not yet been shown.

Cloud decision:

> **PILOT — STRONG POSITIVE.** This is the highest-value adapter candidate for one additional materially different real task. Do not yet make it a permanent Runtime dependency.

Promotion to `APPROVED` requires at minimum one additional materially different ERP/ToB task showing that WeChat acquisition changes the serious candidate pool or decision, plus acceptable dependency/security review.

### Bilibili adapter — CONDITIONAL

Confirmed no-credential capabilities:

- `get_video_metadata` works for known BVIDs;
- `get_video_comments` works and adds practitioner counter-evidence;
- `get_video_chapters` works where available.

Credential-gated capabilities:

- `search_bilibili_videos`;
- `get_video_info`;
- `get_video_transcript`.

Normal targeted Web already discovers Bilibili candidates, while the no-credential adapter enriches known candidates. The most decision-changing capabilities still require Owner-local credentials and client reconnection.

Cloud decision:

> **CONDITIONAL.** Do not require Owner credential setup merely to complete qualification. Revisit only when search/transcript evidence is likely to change a live curation decision.

Comments are enrichment/counter-evidence, not a substitute for the video's actual practitioner content.

### Xiaohongshu provider `xpzouying/xiaohongshu-mcp` — REMOVED

P3 did not reach QR/login, search or detail inspection. The provider-level evidence is nevertheless sufficient to reject this provider for the current bounded architecture:

- exact-pin source build required a temporary Go 1.24 toolchain on a host without Go;
- first-run execution additionally required a roughly 190 MB custom browser runtime;
- the browser runtime is downloaded from the provider-declared third-party CDN and its checksum manifest comes from the same distribution origin;
- the server exposes a broad tool surface including publish/comment/like/favorite and other mutation capabilities, with no demonstrated practical read-only allowlist in the target host;
- the isolated browser acquisition timed out before QR/login and automatically entered retry behavior;
- no Xiaohongshu content evidence was acquired.

These are operational/supply-chain/permission costs, not evidence that Xiaohongshu lacks useful content.

Cloud decision:

> **PROVIDER REMOVED.** Do not reinstall, promote, fork, or keep retrying this provider for the current Curator architecture.

Platform status remains:

> **XIAOHONGSHU COVERAGE GAP — UNQUALIFIED.** A future provider should only be considered if a live task makes the missing source decision-changing and a substantially simpler, enforceably read-only acquisition path exists.

Do not create a replacement-provider search project merely to complete platform coverage.

## 3. What P0–P3 actually proved

Supported:

1. broad Web alone is not sufficient for the Chinese practitioner ecosystem this Curator targets;
2. targeted normal Web is a useful low-cost recall correction but still misses closed/semi-closed sources;
3. a narrow source adapter can materially expand the candidate pool and provide inspectable original evidence — demonstrated for WeChat;
4. source-specific capability can be layered — demonstrated by Bilibili anonymous metadata/comments enrichment;
5. provider operational/security cost can outweigh potential source value — demonstrated by the Xiaohongshu provider qualification;
6. acquisition success and recommendation quality remain separate — more links alone are not success.

Not supported:

- permanent multi-adapter Runtime architecture;
- mandatory platform coverage;
- WeChat adapter `APPROVED` across task classes;
- credentialed Bilibili search/transcript value;
- Xiaohongshu platform content value or absence;
- product value validation versus ordinary AI/self-search.

## 4. Architecture implication

Do not modify Runtime 0.9.1 yet.

The evidence supports a deliberately asymmetric acquisition strategy:

```text
normal broad Web
→ targeted normal-Web recall when obvious ecosystem is missing
→ use a qualified low-cost read-only source capability only when it can change the decision
→ Curator independently evaluates acquired evidence
```

Current provider posture:

```text
WeChat        → PILOT / strong positive
Bilibili      → CONDITIONAL / anonymous enrichment only by default
Xiaohongshu   → current provider REMOVED; platform gap remains
Zhihu         → normal-Web-first
```

Do not build a platform-complete adapter matrix. Different source ecosystems are allowed to have different acquisition strategies.

## 5. Next action

Highest-value next evidence is no longer another platform qualification.

1. run the WeChat PILOT on one materially different real ERP/ToB task;
2. compare whether it changes the serious candidate pool, ranking, rejection reason or confidence versus normal/targeted Web;
3. independently close the reported dependency vulnerability enough to judge practical pilot safety;
4. do not configure Bilibili credentials unless a live task makes transcript/search evidence decision-changing;
5. do not seek a replacement Xiaohongshu provider unless a live task makes that coverage gap materially decision-changing.

Only after the second-task WeChat result should Cloud decide whether a compact `source-adapter-routing` reference is justified.

No Runtime Skill patch is justified from the current P0–P3 evidence.
