# ERP AI Curator — Resource Curation Pilot V3

> Purpose: test the part the Product Owner originally cares about most: **can the Curator consistently discover and compress noisy internet material into a small, share-worthy package of AI Skills / Tools / tutorials / field practices for generalized ERP practitioners?**

This pilot is for **explicit resource-discovery tasks**. It does not re-run the full A/B/C leverage diagnosis for every topic.

Authority:

- `docs/PROJECT_NORTH_STAR.md`
- `docs/AI_LEVERAGE_MODEL_V3.md`
- `docs/SOURCE_STRATEGY_V3.md`
- `docs/validation/PROTOCOL_V3.md`

## 1. What this pilot tests

Not:

- how many websites were searched;
- whether official docs were found;
- whether a GitHub repo has many stars;
- whether the Agent can produce a long research report.

It tests whether the final package is:

1. **task-fit** — directly helps the ERP practitioner do the requested job;
2. **practical** — contains enough steps/examples/output to be usable;
3. **trustworthy** — current/high-risk facts are anchored appropriately;
4. **well-curated** — weak/adjacent resources are removed;
5. **source-balanced by evidence role** — not official-only, but also not community-noise driven;
6. **share-worthy** — the Owner would send it to colleagues;
7. **efficient** — research stops when further searching is unlikely to improve the decision.

## 2. Blind-test discipline

Each topic should run in a fresh local-Agent session when possible.

Before searching, the Agent may read only the current authority documents listed above.

Until the final recommendation is produced, do **not** read candidate-answer/history documents such as:

- `docs/discovery/STARTER_PACK_V0.md`;
- `docs/validation/OWNER_REAL_BATCH_01.md`;
- `docs/validation/OWNER_REAL_DEV_BATCH_02.md`;
- prior resource-curation outputs;
- old Phase 2/3 candidate lists.

Reason: these files contain known candidates and would anchor the test.

After the local result is returned, cloud review may compare it with known candidates and previous research.

## 3. Source behavior under test

Search by evidence need, not platform quota.

Possible sources include:

- original/official docs and repositories;
- GitHub Skills / MCPs / tools;
- WeChat public-account articles;
- Xiaohongshu practical posts;
- Bilibili / YouTube tutorials;
- Zhihu / Juejin / CSDN / personal blogs;
- independent comparisons and issue/discussion evidence.

Important:

- official is not automatically the recommendation;
- practitioner content is not automatically better;
- no platform must be searched merely to tick a box;
- if WeChat/Xiaohongshu/Bilibili or another platform is inaccessible, report the coverage gap rather than using snippets as evidence;
- final recommended community content must have been actually opened/read in sufficiently complete form.

## 4. Research sequence

For each topic:

### Step 1 — Restate the real job

In one sentence, state what the target ERP practitioner actually wants to accomplish.

Do not turn the task into a broad AI-topic taxonomy.

### Step 2 — Discover serious candidates

Search both:

- original implementations / current capability evidence;
- practical practitioner evidence when it could materially help adoption.

Chinese and English can compete.

### Step 3 — Read originals

For finalists:

- repo: README + task-relevant examples/docs/issues when needed;
- article/post: original full-enough content, not snippet;
- video: actual video/transcript/notes sufficient to judge content;
- official: the pages needed to verify relevant facts.

### Step 4 — Falsify

For a non-trivial adoption recommendation, look once for evidence that might reverse it:

- limitation;
- issue;
- failed attempt;
- stale maintenance;
- privacy/security concern;
- compatibility caveat;
- evidence the claimed advantage is not real.

Do not turn this into a fixed query-count Gate.

### Step 5 — Curate

Prefer one main recommendation.

Add a practical companion only if it materially helps the user apply the main recommendation.

Add a second solution only when it serves a meaningfully different capability boundary.

Stop when further searching is unlikely to change the package.

## 5. Required output

```text
## Task
<original task>

## Main recommendation
Resource:
Type:
Why it wins for this task:
What the user can actually do/get:
Who it fits:
Important limitation:
Original link:

## Fact anchor (optional)
Use only when a current/native/volatile fact needs confirmation.
Explain what fact this source anchors.

## Practical companion (optional, default 0–1)
Resource:
Why this practical content is worth the user's time:
What concrete steps/examples/lessons it adds beyond the main resource:
Original link:

## Second solution (optional)
Only if it serves a meaningfully different use case.

## Important rejected candidates
At most 3. One-line rejection reason each.

## Coverage gaps
Platforms/source classes that could not actually be accessed or read.
Do not hide them.

## Curation conclusion
- Would I send this package to an ERP colleague? yes / maybe / no
- What is the package's strongest practical value?
- What remains uncertain?
```

Do not output a giant research log.

## 6. First blind batch

Do not reuse the already-contaminated draw.io topic as the first test.

Start with three fresh tasks:

### T01 — Rapid reviewable prototype

> Find the best current AI Skill / Tool / practical method for an implementation consultant or product manager to turn ERP requirements into a reviewable interactive prototype quickly. Include practical Chinese material if it genuinely improves adoption.

### T02 — ERP requirement / Fit-Gap work

> Find strong AI Skills / Tools / methods / practical guides that can help generalized ERP consultants improve requirement discovery, Fit-Gap / Fit-to-Standard, solution design or requirement documentation. Do not restrict the search to SAP/Oracle official material.

### T03 — Unfamiliar module / system learning

> Find strong AI methods / Skills / practical guides that help an ERP consultant quickly understand an unfamiliar module or custom enterprise system: business process, configuration/logic chain, key objects/data, integrations, common issues and how to verify understanding.

Only if these three show useful curation behavior, expand to:

### T04 — Codebase / architecture understanding

> Find strong AI Skills / Tools / practical methods for a product manager, consultant or developer to understand a Java/custom ERP codebase architecture, dependencies and execution relationships.

### T05 — Current coding-agent cost/model routing

> Find current reliable ways and practical field guidance for using Claude Code / Codex with lower-cost or third-party model routes, clearly separating officially/currently supported facts from practitioner workarounds.

## 7. Cloud adversarial review after each result

The local Agent does not grade itself.

Cloud review attacks:

1. Did it default to official pages because they were easy to verify?
2. Did it include a community link merely for source variety?
3. Did it actually open/read the practical source?
4. Is the practical companion better than the official manual for adoption?
5. Did it miss a strong GitHub/open-source candidate?
6. Did popularity replace evidence?
7. Did it hide platform access gaps?
8. Did it search too long after the decision was already stable?
9. Did it include two recommendations that really do the same job?
10. Would the Owner actually forward the package to colleagues?

Only repeated failure patterns should change the product rules.

## 8. Pilot decision

After T01–T03, decide among:

- **KEEP DIRECTION** — packages are genuinely useful/shareable; continue T04–T05;
- **TUNE DISCOVERY** — source mix or selection is weak but product value is visible;
- **RETHINK** — outputs remain official-link-heavy, generic, noisy or not worth forwarding.

No numeric PASS threshold.
