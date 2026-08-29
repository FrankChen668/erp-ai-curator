# Adversarial Review — Source Adapter Architecture V3

> Purpose: attack the proposal that ERP AI Curator should compose with installed WeChat / Xiaohongshu / Bilibili Skills or MCPs.

## 1. Strongest argument for the architecture

T01/T02 repeatedly showed a mismatch:

- Curator judgement was improving;
- normal Web/GitHub retrieval disproportionately surfaced official docs, GitHub and Reddit;
- some Chinese practitioner platforms were discoverable but not reliably readable by the local path.

A source-specific adapter directly addresses a real capability gap: **content acquisition**.

That makes this proposal more aligned with V3 than forcing one general browser to handle every platform.

## 2. Attack: are we solving the wrong problem with more tools?

Possible failure:

> High-quality ERP+AI Chinese material may genuinely be scarce, so installing source Skills only retrieves more generic noise.

Resolution:

- do not judge success by search count or number of Chinese links;
- compare the final recommendation before/after adapter evidence;
- if no material recommendation uplift occurs, do not retain the adapter as a Curator dependency.

## 3. Attack: does “Skill calling Skill” actually work reliably?

The design can fail if Codex does not consistently route from Curator instructions into another installed Skill/MCP.

Resolution:

- treat orchestration as an explicit pilot question;
- first test with a direct instruction naming the installed source capability;
- then test whether a Curator-style trigger causes the same capability to be selected without the user naming it;
- do not implement permanent Curator Skill routing until both behaviors are understood.

The architecture should rely on Codex runtime composition, not invent a custom nested-Skill API that may not exist.

## 4. Attack: adapter sprawl recreates the old architecture failure

Possible path:

```text
WeChat skill
Xiaohongshu skill
Bilibili skill
Zhihu skill
Juejin skill
CSDN skill
Douyin skill
YouTube skill
...
```

Then Curator becomes a giant router and the old resource-system complexity returns.

Resolution:

- no general platform catalog;
- first pilot is limited to the three repeated coverage gaps already observed;
- add another adapter only after repeated evidence that normal access fails and the missing source materially affects decisions.

## 5. Attack: installed social Skills have excessive permissions

Xiaohongshu MCPs commonly include publish, comment, like, favorite, follow and account functions.

For Curator these are unnecessary and increase:

- accidental write risk;
- account safety risk;
- credential exposure;
- maintenance surface.

Resolution:

- read-only by product policy;
- expose/search only the minimum tool subset if the runtime permits it;
- if a candidate cannot be constrained safely, reject it for Curator even if retrieval quality is good.

## 6. Attack: supply-chain risk is larger than the content problem

A third-party Skill may include:

- install scripts;
- npm/pip dependencies;
- browser extensions;
- prebuilt binaries;
- local cookie access;
- arbitrary shell execution.

Resolution:

- pinned commits;
- local static review before installation;
- no blind `npx ... -y` installation from floating HEAD in the controlled pilot;
- record package/binary hashes where practical;
- separate “adapter is useful” from “adapter is safe enough to standardize.”

## 7. Attack: platform anti-bot makes the architecture inherently unstable

Xiaohongshu and Bilibili can change risk controls, routes or page structures.

Resolution:

- source adapters are optional capabilities, not guaranteed product dependencies;
- fallback is report coverage gap, not fabricate content;
- maintain adapter version/pin as volatile infrastructure information;
- do not promise complete platform coverage.

## 8. Attack: adapter output can silently bias Curator selection

Platform Skills may sort by likes, views or “hot” ranking.

That can cause Curator to overvalue popular content.

Resolution:

- ranking is discovery only;
- final evaluation uses original-content evidence and task fit;
- popularity remains a weak signal.

## 9. Attack: too much acquired source content creates copyright / repository pollution

Persisting full WeChat articles, Xiaohongshu posts and video transcripts in the project would turn Curator into a scraped corpus.

Resolution:

- raw acquisition stays local/temporary;
- repo stores only URLs, metadata, concise evidence notes and our independent judgement;
- no bulk source corpus by default.

## 10. Attack: user login/account becomes a hidden prerequisite

Xiaohongshu and some Bilibili capabilities may depend on login state.

Resolution:

- adapter must declare whether login is required;
- do not silently use the user's personal account for write operations;
- use read-only/test account where practical;
- if login burden is high relative to curation value, reject the adapter.

## 11. Attack: why not simply use WorkBuddy?

WorkBuddy may already have stronger Chinese-platform browsing.

Using it remains a valid alternative, but making it the permanent external acquisition layer would introduce a separate handoff and different runtime.

Decision rule:

- first test native Codex composition with installed source Skills/MCPs;
- if native composition cannot achieve reliable access or is too costly, compare WorkBuddy as an alternative acquisition backend.

Do not choose either architecture by preference alone.

## 12. Additional problem exposed by T02: recommendation maturity

T02 found a highly task-fit Business Analyst Skill, but the repository has little external usage evidence.

This reveals a second independent problem:

> **task fit and resource maturity are different dimensions.**

A tiny repository can contain an excellent method, but Curator should not describe it as mature/proven without evidence.

Correction for future curation:

- distinguish `strong method candidate` from `proven mature solution`;
- repository popularity is not a quality score, but maintenance/adoption evidence affects confidence;
- when maturity is weak, recommend a small trial rather than production adoption.

Do not create a numeric maturity score.

## 13. Additional problem exposed by T01/T02: practical companion provenance

A practical guide can contain excellent steps but weak author/provenance evidence.

Correction:

- content usefulness and provenance confidence are separate;
- weak provenance does not automatically discard a transferable method;
- but it should be labelled as method inspiration, not high-trust field evidence.

## 14. Net decision after adversarial review

The architecture survives the attack **as a pilot**, with these corrections:

1. source adapters are conditional capabilities, not mandatory lanes;
2. first pilot only WeChat, Xiaohongshu and Bilibili;
3. read-only acquisition is mandatory for Curator;
4. local supply-chain/security review precedes installation;
5. multi-Skill routing itself must be tested;
6. success is final recommendation uplift, not acquisition volume;
7. no custom adapter framework, resource DB or crawler is built yet;
8. T02 also adds two curation checks: maturity confidence and provenance confidence.

Next step is a controlled local adapter qualification + smoke test, then a fresh curation task with adapters available.
