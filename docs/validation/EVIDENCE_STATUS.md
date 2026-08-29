# Current Evidence Status

Date: 2026-08-29

> Current product model is `AI_LEVERAGE_MODEL_V3.md`. Current execution authority is `CURRENT_EXECUTION_PLAN_V3.md`.

## 1. Supported by evidence

### Product problem

泛 ERP / 企业信息化从业者存在两个相邻问题：

1. 当前真实工作应该怎样用 AI；
2. 当需要外部能力时，哪些 Skill / Tool / 方法 / 教程真正值得采用。

V3 therefore uses:

`真实任务 → AI leverage diagnosis → Mode A/B/C → 必要时定向发现`

rather than the superseded resource-first flow.

### Curation findings

T01/T02 support these observations:

- official/original sources are useful fact anchors, not automatic recommendation winners;
- GitHub/practitioner/community content can add more practical adoption value;
- T01 exposed discovery-recall risk;
- T02 exposed task-fit vs dependency-maturity risk;
- `Practical Companion` must add actual workflow/example/prompt/failure/adoption evidence, not merely source diversity;
- Chinese practitioner coverage must distinguish access gap, index bias and true domain scarcity.

### Adapter lifecycle

First controlled Windows + Codex qualification produced real provider decisions:

- WeChat discovery: `CONDITIONAL`;
- WeChat original-article reader: `KEEP FOR PILOT`;
- first Bilibili provider: `CONDITIONAL`, credential-blocked;
- first Xiaohongshu provider: `REMOVE` because the exposed tool surface failed the research-only boundary.

This supports the value of qualification/pinning/read-only review as a dependency boundary.

### Bounded multi-Skill composition

Phase 3A WeChat routing test: **PASS**.

Observed in one task:

```text
Curator evidence need
→ wechat-article-search
→ original mp.weixin.qq.com candidate
→ wechat-article-reader
→ original article body + metadata
→ Curator judgement
→ stop
```

Unrelated adapters were not invoked. Search snippets were distinguished from original content.

This supports:

> **Codex can compose the approved WeChat discovery + reader capabilities conditionally in one Curator-style task.**

It does not prove arbitrary Skill orchestration.

See `SOURCE_ADAPTER_ROUTING_RESULT_01.md`.

## 2. Current provider state

```text
WeChat discovery
  zjp1997720/wechat-article-search
  status: CONDITIONAL

WeChat original article reader
  Githun1314/agent-wechat-reader
  status: KEEP FOR PILOT

Bilibili
  XZXZZX-Ai/bilibili-mcp
  status: CONDITIONAL — credential blocked

  sandraschi/bilibili-mcp
  status: cloud-reviewed alternative; separate local qualification later

Xiaohongshu
  xpzouying/xiaohongshu-mcp
  status: REMOVED

  replacement
  status: none approved
```

Do not infer that platform coverage itself is a product requirement.

## 3. What remains unproven

The next major unknown is **incremental user value**, not routing feasibility.

Still unproven:

- WeChat adapter evidence materially improves the final recommendation package over normal Web/GitHub discovery;
- the gain, if any, justifies adapter installation/maintenance/anti-bot cost;
- the same pattern generalizes to different ERP tasks;
- Bilibili can be covered through a sufficiently low-friction provider;
- Xiaohongshu needs/has an acceptable provider;
- V3 is consistently better for independent real users;
- V3 should be packaged as a production Skill;
- a resource database, automatic refresh, scoring, scenario taxonomy or adapter package manager is needed.

## 4. Current validation phase

**Status: Phase 4 paired curation uplift A/B test.**

Protocol:

`CURATION_UPLIFT_AB_TEST_01.md`

Run A:

- fresh isolated session;
- same raw task/model/config/repo state as B;
- normal Web/GitHub only;
- source adapters unavailable.

Run B:

- separate fresh isolated session;
- same raw task;
- same normal sources;
- qualified WeChat chain available conditionally;
- adapter use not forced.

Both outputs are frozen before comparison.

Local Codex reports the outputs and observable acquisition traces only. Cloud performs the adversarial comparison.

Possible Phase 4 verdicts:

- `MATERIAL UPLIFT`
- `LIMITED UPLIFT`
- `NO MATERIAL UPLIFT`
- `INVALID TEST`

## 5. Evidence asset state

| Asset | Evidence type | Current status |
|---|---|---|
| Phase 1 representative Skill study | design research | keep |
| old Phase 2/3 resource-first design | historical hypothesis | superseded for current decisions |
| V0.2–V0.4 | failure evidence | archive only |
| Starter Pack V0 | discovery memory | search prior only |
| OR01–OR06 original problems | OWNER_REAL input | keep |
| V3 owner/boundary replay | design falsification | useful, not independent validation |
| T01 prototype curation | OWNER_REAL behaviour evidence | exposed recall issue |
| T02 requirements/Fit-Gap curation | OWNER_REAL behaviour evidence | exposed fit-vs-maturity issue |
| Source Adapter Qualification 01 | local runtime evidence | provider-level decisions proven |
| Source Adapter Routing Result 01 | local runtime evidence | WeChat bounded composition PASS |
| Curation Uplift A/B Test 01 | paired value test | next |
| Independent REAL_USER results | primary validation | insufficient |

## 6. Main risks

### Over-tooling

Every AI question becomes another Tool/Skill recommendation.

### Adapter sprawl

Every access failure becomes a permanent platform adapter.

### Platform checklist drift

Installed adapters are searched mechanically on every topic.

### Permission erosion

Coverage pressure weakens read-only/security boundaries.

### Chinese-content halo

Chinese practitioner content is treated as better merely because it is local-language/community content.

### Weak-baseline A/B

Run A is intentionally under-researched so Run B appears better.

### More-links illusion

Adapter value is inferred from content/link volume rather than a more useful final recommendation.

### Self-validation

Local Agent PASS or OWNER_REAL evidence is mistaken for independent-user validation.

### Rebuilding governance

A failure triggers new Gates, scoring, database or automation rather than fixing the actual decision problem.

## 7. Mainline

1. run Phase 4 paired A/B on the fresh unfamiliar-module/system task;
2. cloud adversarially compare frozen A/B outputs;
3. only if material uplift exists, repeat on 1–2 different fresh tasks;
4. keep Bilibili replacement qualification non-blocking;
5. keep Xiaohongshu as a Coverage Gap until a justified low-risk provider exists;
6. only after repeated evidence decide whether to package a minimal Curator Skill.

Do not implement a production Skill merely because multi-Skill routing works.
