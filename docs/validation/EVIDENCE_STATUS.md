# Current Evidence Status

Date: 2026-08-29

> Current execution authority: `CURRENT_EXECUTION_PLAN_V3.md`.

## 1. Supported by evidence

### Product / curation

- official/original sources are fact anchors, not automatic recommendation winners;
- T01 exposed discovery-recall risk;
- T02 exposed task-fit vs dependency-maturity risk;
- practical/community content is useful only when it adds real workflow/example/failure/adoption evidence;
- Chinese practitioner coverage must distinguish access, indexing and true quality/scarcity;
- Curator-created synthesis must not be presented as an externally discovered resource.

### Adapter lifecycle

Controlled Windows + Codex qualification:

- WeChat discovery: `CONDITIONAL`;
- WeChat original reader: `KEEP FOR PILOT`;
- first Bilibili provider: `CONDITIONAL / credential blocked`;
- first Xiaohongshu provider: `REMOVE`.

### Bounded routing

WeChat Search → Reader multi-Skill routing: **PASS**.

This proves the approved two-step chain can be composed conditionally in one task. It does not prove arbitrary Skill orchestration.

### Phase 4 paired test

`CURATION_UPLIFT_AB_TEST_01` completed.

Verdict for the exact mixed task:

> **NO MATERIAL UPLIFT**

Run B had the WeChat adapter available but did not invoke it. Therefore recommendation differences between Run A and Run B came from normal search/model variance, not adapter evidence.

Positive evidence:

- the Curator did not call WeChat just because it was installed;
- conditional-routing discipline held.

See `CURATION_UPLIFT_AB_RESULT_01.md`.

## 2. Test-design finding

The Phase 4 task combined:

- standard ERP module learning;
- custom enterprise-system/codebase understanding.

Both runs gravitated toward the custom-system/codebase path.

Therefore standard ERP module curation remains insufficiently tested.

Future validation separates these jobs.

## 3. Current provider state

```text
WeChat discovery → CONDITIONAL
WeChat reader → KEEP FOR PILOT
Bilibili first provider → CONDITIONAL / credential blocked
Bilibili alternative → cloud-reviewed, local test deferred
Xiaohongshu first provider → REMOVED
Xiaohongshu replacement → none approved
```

No adapter expansion is justified yet.

## 4. What remains unproven

- WeChat practitioner evidence materially improves standard ERP learning curation;
- source-adapter value generalizes across ERP tasks;
- Bilibili/Xiaohongshu need or justify additional providers;
- V3 is consistently better for independent real users;
- production Curator Skill packaging is justified.

## 5. Next validation

Run one **Standard ERP Module Diagnostic**.

Use a specific module, currently recommended:

> SAP EWM inbound receiving and putaway for a consultant unfamiliar with the module.

Primary design:

1. normal Web/GitHub baseline → freeze;
2. enable only WeChat Search → Reader as additional acquisition capability;
3. measure only evidence/recommendation delta attributable to the adapter.

This sequential incremental design avoids confusing ordinary search variance with adapter causality.

Valid delta outcomes:

- `MATERIAL DELTA`
- `LIMITED DELTA`
- `NO MATERIAL DELTA`
- `INVALID TEST`

## 6. Evidence asset state

| Asset | Evidence type | Current status |
|---|---|---|
| T01 prototype curation | OWNER_REAL behaviour evidence | recall issue exposed |
| T02 requirements/Fit-Gap curation | OWNER_REAL behaviour evidence | fit-vs-maturity issue exposed |
| Source Adapter Qualification 01 | local runtime evidence | provider decisions proven |
| Source Adapter Routing Result 01 | local runtime evidence | WeChat bounded composition PASS |
| Curation Uplift A/B Test 01 | paired value test | NO MATERIAL UPLIFT for mixed task |
| Curation Uplift A/B Result 01 | cloud interpretation | current |
| Standard ERP Module Diagnostic | next local test | pending |
| Independent REAL_USER results | primary validation | insufficient |

## 7. Main risks

- over-tooling;
- adapter sprawl;
- platform checklist drift;
- permission erosion;
- Chinese-content halo;
- weak baseline;
- more-links illusion;
- search/model variance mistaken for adapter uplift;
- Curator synthesis mistaken for discovered resource;
- local PASS mistaken for independent-user validation.

Do not implement a production Skill merely because routing works.
