# Curator 0.9.0 — Runtime Responsibility Split

Date: 2026-08-31
Status: **ARCHITECTURE CHANGE IMPLEMENTED — CONTROLLED USE REQUIRED**

## 1. Trigger

The same natural practice request repeatedly exposed a stable failure pattern:

> “使用这个 skill 给我找下做流程图的最佳实践”

Observed progression:

- 0.7.x: official/standard sources + model-authored generic tutorial;
- 0.8.1: practitioner discovery improved, but selection promoted a Japanese Qiita article and then recommended an SVG-oriented Skill with an install command;
- 0.8.2: despite explicit `no incidental install` guardrails, a fresh run returned `mermaid-visualizer`, installs/stars/security metadata, and an install command as the main answer.

The 0.8.2 answer is strong negative execution evidence because it violates the central boundary already present in the Skill body:

> a best-practice/tutorial request alone does not justify an installable Tool/Skill recommendation.

## 2. First-principles diagnosis

The product legitimately has two user jobs:

1. **Practice curation** — find how practitioners actually do a repeatable task and which tutorials/cases/resources are worth learning first;
2. **Capability adoption** — decide whether the current toolchain has a concrete gap and whether a Tool/Skill/MCP/plugin/Agent/workflow is worth adding.

These jobs share upstream task context but have different default outputs and different failure costs.

When both jobs are placed in one Runtime Skill, the always-visible skill metadata/description contains strong Tool/Skill/MCP adoption language. In repeated controlled use, that language appears to pull practice-only prompts toward marketplace/tool selection even when the body later says not to do so.

The failure therefore is no longer best modeled as a missing guardrail. It is a **runtime responsibility / trigger-boundary problem**.

## 3. External design principle

Current Agent Skills / Skill Creator guidance treats `name + description` as the primary trigger layer. An over-broad description can trigger a Skill when it should not; the body is only read after triggering.

Therefore the correction should reduce overlap at metadata level rather than keep adding downstream prohibitions.

## 4. 0.9.0 architecture

One product, two single-responsibility Runtime Skills.

### 4.1 `curating-erp-ai-resources`

Purpose: **practice/resource curation only**.

Triggers:

- best practices;
- tutorials;
- real workflows/cases;
- practitioner resources;
- “how others do this with AI”.

It may mention a Tool/Skill that appears inside a practitioner workflow, but it must not convert that observation into an installation/adoption decision.

Runtime reference:

- `references/practitioner-discovery.md`

### 4.2 `advising-erp-ai-capabilities`

Purpose: **capability adoption only**.

Triggers:

- is the current toolchain enough?;
- should I add/install a Tool/Skill/MCP/plugin/Agent?;
- which capability should I choose/compare?;
- what is the smallest useful upgrade?;
- should the Agent get system/repo/database access?

It starts from a concrete capability gap and can legally conclude “do not add anything”.

Runtime reference:

- `references/evidence-and-safety.md`

## 5. Why no Router Skill

A third router would add another runtime component, another trigger surface, and another place for intent drift.

The descriptions are designed to be mutually exclusive for ordinary prompts. When the user explicitly asks both jobs in one message, both Skills may apply; that is a legitimate combined request rather than a routing failure.

## 6. Migration choice

The existing directory/name `curating-erp-ai-resources` is retained for practice curation to avoid breaking the current trial path used by the Owner.

Capability adoption moves to the new `advising-erp-ai-capabilities` Skill.

This is a behavior change and therefore uses product/runtime version `0.9.0`, not another 0.8.x patch.

## 7. Adversarial review

### Attack A — Are we splitting one product into two products?

No. North Star remains one product with two user jobs. The split is only at Runtime responsibility/trigger level.

### Attack B — Does this create unnecessary packaging complexity?

There is one extra `SKILL.md`, but the former single Skill already carried two incompatible default behaviors. The added file removes cross-intent rules and reduces runtime cognitive conflict.

### Attack C — Will users have to know which Skill to invoke?

Normal Agent Skills hosts use descriptions for triggering. Trial documentation also explains the two direct intents. Manual invocation remains possible when the host requires it.

### Attack D — What if the user wants both practice and capability advice?

Both Skills may apply. No router or taxonomy is required. Practice curation answers “what practitioners do”; capability advice separately answers “should I add anything”.

### Attack E — Are Tool/Skill resources banned from practice curation?

No. A real practitioner workflow can include a Tool/Skill. Practice Curator may describe that fact, but must not infer adoption merely from occurrence.

### Attack F — Does Capability Advisor become a tool catalogue?

No. It must first name a concrete capability gap. Without a gap, the correct answer is “current toolchain is enough”.

### Attack G — Are we overfitting to one flowchart case?

The specific case repeated across multiple versions, and the failure mechanism is generic: practice intent repeatedly collapses into installable capability selection. The architecture boundary is task-agnostic.

## 8. Minimal routing sanity check

These are implementation sanity checks, not product-value evidence:

| Natural request | Expected Runtime |
|---|---|
| “给我找下做流程图的最佳实践” | Practice Curator only |
| “有没有产品经理用 AI 做流程图的实操教程？” | Practice Curator only |
| “我现在 ChatGPT + draw.io 够不够，要不要装 Skill？” | Capability Advisor only |
| “帮我比较这两个 MCP 哪个值得接” | Capability Advisor only |
| “先找最佳实践，再看看要不要装新的 Skill” | both may apply |
| “直接帮我画这个流程图” | neither by default |

## 9. Acceptance boundary

0.9.0 architecture is ready for controlled use if:

- both Skill descriptions are narrow and mutually clear;
- Project Contract recognizes both Runtime Skills;
- practice package contains only practitioner discovery reference;
- capability package contains only evidence/safety reference;
- no third router, A/B/C runtime framework, scoring/Gate, platform quota, or marketplace ranking is introduced;
- current authority docs consistently describe one product / two Runtime responsibilities.

This does **not** prove 0.9.0 works in Codex Desktop or that product value exceeds ordinary AI/self-search.

## 10. Next evidence

Use natural controlled requests again after syncing 0.9.0.

Highest-value observation:

> Does the original practice-only flowchart prompt now stay inside practitioner curation instead of selecting/installing a Skill?

If it still fails, collect host trigger/load/search evidence before changing Runtime again. Do not return to patch-on-patch behavior.
