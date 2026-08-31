# Source Acquisition Pilot — Cloud Adversarial Review

Date: 2026-08-31
Status: **CLOUD REVIEW COMPLETE — P3 XIAOHONGSHU NEXT / RUNTIME 0.9.1 REMAINS FROZEN**

## 1. Evidence reviewed

Reviewed final remote evidence branch `validation/source-acquisition-pilot-review-20260831` through commit `d3933a5`:

- `P0_TARGETED_WEB_RESULT.md`
- `P1_WECHAT_RESULT.md`
- `P2_BILIBILI_RESULT.md`
- `FINAL_SOURCE_ACQUISITION_COMPARISON.md`

The two earlier local commits (`6091c3c` and `df4261c`) are linear, not divergent. `d3933a5` correctly preserves the later Bilibili no-credential evidence and removes unsupported value claims about untested Xiaohongshu.

## 2. Cloud status decisions

The Local Agent statuses are proposals. Cloud owns the architecture/promotion decision.

### Targeted normal Web — BASELINE / KEEP

Observed value:

- broad Web missed multiple Chinese practitioner ecosystems;
- targeted `site:` queries materially improved Bilibili and, in one run, Zhihu recall;
- WeChat and Xiaohongshu remained zero-recall through normal Web;
- Bilibili readability varied by run: metadata/description could be read in one run, while direct opens returned 412 in another.

Decision:

> Keep targeted normal Web as the lowest-cost first fallback. It is not sufficient as the only acquisition path.

### WeChat adapter — PILOT (strong positive), not yet APPROVED

Direct positive evidence is strong:

- normal Web returned zero WeChat candidates;
- pinned `wechat-article-search` returned fresh, task-matched candidates in two local executions;
- URL resolution succeeded on tested samples;
- multiple original public-account articles were successfully read;
- acquired evidence added product-manager/process-management/tool-builder perspectives absent from P0;
- no user credentials or social write actions were required.

However, `APPROVED` is too strong at this point because:

1. qualification is still from one task family (AI flowchart practice), not repeated cross-task material value;
2. one installation reported a high-severity transitive npm vulnerability whose exact production significance has not been independently closed;
3. full original-content reading depended on a separate read-only public-article reader in addition to the discovery Skill;
4. the P1 file contains two local executions with different proposed labels (`APPROVED` in the earlier record and `PILOT` in the later appendix). The factual results are consistent; only the promotion label is inconsistent.

Cloud decision:

> **PILOT — STRONG POSITIVE.** Eligible for another real task / source-acquisition comparison. Do not yet make it a permanent Runtime dependency.

Promotion to `APPROVED` requires at minimum one additional materially different real ERP/ToB task showing that WeChat acquisition changes the serious candidate pool or decision, plus acceptable dependency/security review.

### Bilibili adapter — CONDITIONAL

Confirmed no-credential capabilities:

- `get_video_metadata` works for known BVIDs;
- `get_video_comments` works and adds practitioner counter-evidence;
- `get_video_chapters` works where available.

Credential-gated capabilities:

- `search_bilibili_videos`;
- `get_video_info`;
- `get_video_transcript`.

Normal targeted Web already discovers Bilibili candidates, while the no-credential adapter enriches known candidates. The most decision-changing adapter capabilities — new candidate search and transcript-level inspection — still require Owner-local credentials and client reconnection.

Cloud decision:

> **CONDITIONAL.** Do not require Owner credential setup yet. Revisit only when transcript/search evidence is likely to change a live curation decision.

### Xiaohongshu adapter — NOT QUALIFIED / NEXT PILOT PRIORITY

No P3 evidence exists. Therefore no value or safety conclusion is allowed.

However, P0 produced zero Xiaohongshu recall in both broad/targeted normal-Web paths, and Xiaohongshu is one of the practitioner ecosystems whose absence triggered this source-acquisition investigation.

Cloud decision:

> **NOT QUALIFIED — NEXT PILOT PRIORITY.** If the Owner accepts the local QR/login action, qualify read-only Xiaohongshu search + detail next. This is higher priority than adding Bilibili credentials because Bilibili already has partial normal-Web discovery plus anonymous enrichment, while Xiaohongshu currently has no usable acquisition path at all.

## 3. What the pilot has actually proven

Supported:

1. broad Web alone is not sufficient for the Chinese practitioner ecosystem this Curator targets;
2. targeted normal Web is a useful low-cost recall correction but still misses closed/semi-closed sources;
3. a narrow source adapter can materially expand the candidate pool and provide inspectable original evidence (demonstrated for WeChat);
4. source-specific capability can be layered: Bilibili anonymous enrichment is useful even before full credentialed search/transcript;
5. acquisition success and recommendation quality remain separate — more links alone are not success.

Not yet supported:

- permanent multi-adapter Runtime architecture;
- mandatory platform coverage;
- WeChat adapter APPROVED for all task classes;
- credentialed Bilibili search/transcript value;
- any Xiaohongshu value/safety conclusion;
- product value validation versus ordinary AI/self-search.

## 4. Architecture implication

Do not modify Runtime 0.9.1 yet.

The emerging acquisition strategy is:

```text
normal broad Web
→ targeted normal-Web recall when obvious ecosystem is missing
→ already-qualified read-only source capability only when the missing source could change the decision
→ Curator independently evaluates acquired evidence
```

This is still a pilot composition model, not a permanent adapter framework.

## 5. Next action

Highest-value next evidence:

1. qualify Xiaohongshu read-only search/detail if Owner accepts QR/login;
2. do not configure Bilibili credentials merely to complete the matrix;
3. after P3, reassess whether a compact source-adapter routing reference is justified;
4. independently, use WeChat PILOT on one materially different real ERP/ToB task before promotion to APPROVED.

No Runtime Skill patch is justified from the current evidence.
