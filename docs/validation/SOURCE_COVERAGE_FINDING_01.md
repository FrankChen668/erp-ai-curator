# Source Coverage Finding 01 — Chinese practitioner sources

> Status: evidence note, not a new product Gate.

## 1. What triggered this finding

During Resource Curation Pilot T01/T02, the local Codex path repeatedly returned relatively few Chinese practitioner sources and reported access problems on Bilibili/Xiaohongshu and weak retrievability for WeChat-style content.

Independent cloud review showed that this must not be collapsed into the claim "Chinese resources are scarce".

Three different causes are mixed together:

1. **Acquisition/access gap** — some platforms are hard for a given browser/search stack because of dynamic rendering, login, anti-bot responses or weak indexing.
2. **Discovery/index bias** — global web/GitHub search more reliably surfaces official docs, GitHub and Reddit than WeChat/Xiaohongshu-style content.
3. **True domain scarcity / quality mismatch** — highly specific "ERP consultant + AI + Fit-Gap/Fit-to-Standard/Solution Design" practical material is genuinely less common than generic AI product-management or prompt content.

These causes require different responses.

## 2. Evidence from T01/T02

- T01 local search reported Bilibili pages returning HTTP 412, yet independent cloud search could read multiple current Bilibili pages about Figma Make, AI prototypes and product-manager workflows.
- T02 local search found no strong Chinese ERP Fit-Gap companion. Independent review could find abundant Chinese AI product-manager / requirements material, but much of it was generic, job-training oriented or not ERP-specific.
- Current SAP Chinese/official material exists for Fit-to-Standard and AI-assisted requirement generation, but this does not substitute for independent Chinese practitioner evidence.

Therefore:

> **"not found by the current Agent" is not equivalent to "does not exist", while "Chinese content exists" is not equivalent to "high-quality ERP-specific evidence exists".**

## 3. Product implication

Do not add a rule requiring every task to search WeChat, Xiaohongshu or Bilibili.

Instead separate two responsibilities:

### A. Curation / judgement

The Curator decides:

- what evidence is needed;
- which candidates are serious;
- what is trustworthy and practically useful;
- what should be recommended.

### B. Source acquisition

A source-specific collector/browser may be used only to obtain content that the main search path cannot reliably access.

The collector does **not** decide recommendation quality.

This preserves the V3 principle: specialised tooling should fill a real capability gap rather than become the workflow by default.

## 4. Proposed two-lane experiment

Do not change the permanent architecture yet. Test it first on a fresh task.

### Lane 1 — normal Curator search

Use the current Codex/web/GitHub path and record:

- serious candidates found;
- Chinese practitioner candidates found;
- platforms inaccessible;
- final package.

### Lane 2 — China-native acquisition supplement

Only after Lane 1 is complete, use a China-capable collector/browser for targeted acquisition from sources that Lane 1 could not reliably read, such as:

- WeChat public accounts;
- Xiaohongshu;
- Bilibili when the primary browser path fails;
- other Chinese practitioner platforms when relevant.

Export only raw evidence needed for evaluation:

- title;
- author/account if available;
- publication date if available;
- original URL;
- full text / transcript / sufficiently complete content;
- screenshots or examples when they are part of the evidence;
- access limitations.

Then let the same Curator evaluate the added material under `SOURCE_STRATEGY_V3.md`.

## 5. What the experiment should answer

The key question is not whether a collector can scrape more pages.

It is:

> **Does China-native acquisition materially improve the final share-worthy recommendation package?**

Useful delta examples:

- finds a practical Chinese guide that materially reduces ERP colleague learning cost;
- exposes a real failure/limitation absent from official/GitHub material;
- discovers a strong local Skill/workflow missed by global search;
- changes or strengthens the final recommendation.

Non-value examples:

- more links but no better recommendation;
- promotional reposts;
- generic AI tutorials unrelated to the ERP work outcome;
- content that only repeats official documentation.

## 6. Decision after the experiment

Possible outcomes:

- **NO EXTRA LANE NEEDED** — normal search already finds enough good evidence.
- **CONDITIONAL CHINA LANE** — use a China-native collector only when Chinese practitioner evidence is important and current access coverage is weak.
- **DEDICATED ACQUISITION ADAPTER WORTHWHILE** — repeated tasks show material recommendation uplift that justifies a stable acquisition integration.

Do not build a crawler/database before this is proven.
