# P07 Codebase Understanding Result 02

Date: 2026-08-30

> Fresh rerun from the survey-derived P07 job. `P07_CODEBASE_UNDERSTANDING_RESULT_01.md` remains invalidated and was not used as evidence or as a search prior.

## Verdict

> **CLOSE P07 — TRACEABLE READ-ONLY REPO EXPLORATION IS THE DEFAULT; UPGRADE TO SEMANTIC/LSP NAVIGATION OR ERP-NATIVE MCP ONLY WHEN CONTEXT RETRIEVAL OR SYSTEM ACCESS IS THE REAL BOTTLENECK**

For an ERP / enterprise-information-system consultant or developer inheriting an SAP / Oracle / custom-system codebase:

- do not begin by installing a “code understanding” tool;
- begin with one concrete business/technical question and a read-only, evidence-linked exploration of the repository;
- use a competent repo-aware coding Agent as the default for ordinary local Git repositories;
- add LSP/symbol/semantic tooling only when text search becomes noisy or cross-symbol/cross-module navigation is materially expensive;
- add a system-native connector/MCP when the relevant source, metadata, tests or runtime evidence do not live in the local repository — SAP ABAP is a clear example;
- never treat code explanation as proof of business intent, and never treat model agreement or passing generated tests as proof that the engineer actually understands the implementation.

A generic specialist Skill is not mandatory for P07.

## Real job and acceptance boundary

Demand authority: `SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

The actual job is broader than “summarize code”:

```text
concrete task/question
→ global system/repository map
→ relevant business flow / entry point
→ cross-file call and data path
→ validations / permissions / side effects / exceptions
→ tests / logs / docs / runtime evidence where available
→ observed facts vs inference vs unknown
→ reviewable logic/FS/defect hypothesis
```

The critical boundary is:

> **Code can provide evidence of implemented behavior. It often cannot prove why a business rule exists, whether the current behavior is intended, or what the customer actually requires.**

Reverse-generated functional logic must therefore distinguish implemented facts from inferred intent and unresolved business decisions.

## Evidence retained

### 1. Professional code-comprehension research — actually read

**Gao et al. — “Understanding Codebase like a Professional! Human–AI Collaboration for Code Comprehension” (ICPC 2026)**  
https://doi.org/10.1145/3794763.3794822

Evidence role: **current empirical workflow evidence**.

The study interviewed eight professional code-auditing practitioners who had both manual and LLM-assisted experience, then evaluated a hierarchical CodeMap prototype with experienced and novice developers.

Material observations:

- professional comprehension is hierarchical rather than “read every file”: global project/business/call structure → local components/dependencies → detailed code verification;
- practitioners use LLMs effectively for explanations, extraction and confirmation, but still face repetitive decomposition, irrelevant answers and weak cross-file relationship support;
- the paper explicitly treats business/process understanding and cross-file relationships as areas where plain conversational interaction can be insufficient;
- the evaluated hierarchical map reduced dependence on long LLM responses and helped users switch between global/local/detail views.

Why it matters:

> The useful product insight is the **exploration shape** — global → local → detail with explicit relationship evidence — not a mandate to install the paper’s prototype.

Limitations:

- small practitioner sample;
- evaluation focuses heavily on usability/perceived comprehension rather than verified ERP business-rule correctness;
- retrieval and LLM hallucination remain acknowledged limitations.

### 2. Experienced-developer success/failure evidence — actually read

**r/ExperiencedDevs — “Being called out as slow first time in my career.”**  
https://www.reddit.com/r/ExperiencedDevs/comments/1lyuhk0/

Evidence role: **independent practitioner workflow + failure evidence**.

Retained signals from experienced commenters:

- AI can be valuable for explaining unfamiliar code, but using it to implement before understanding the codebase/framework creates poor or wrong code and additional debugging;
- first identify relevant modules and a high-level control/sequence flow, validate it with someone knowledgeable, then use AI on smaller scoped context;
- business-specific assumptions made by AI must be checked rather than accepted as explanation.

Limitation: community anecdotes, not controlled outcome evidence.

**r/ExperiencedDevs — “New codebase + AI code smells”**  
https://www.reddit.com/r/ExperiencedDevs/comments/1vvj60z/

Evidence role: **recent counter-evidence against output-as-understanding**.

The author describes Claude/Codex converging on an implementation with passing tests while the author still did not understand why substantial parts of the code existed.

Practical implication:

> Model agreement and green tests are useful signals, but neither substitutes for a human-readable causal model of the implementation.

Limitation: one self-reported case.

### 3. Chinese practical workflow — actually read

**火山引擎开发者社区 —《[实战指南] 如何用 Cursor 高效理解陌生代码库》**  
https://developer.volcengine.com/articles/7582491056462102574

Evidence role: **Chinese practical workflow evidence**.

Material workflow:

- keep exploration read-only first;
- ask the Agent to plan how it will understand the repository;
- decompose architecture/frontend/backend/user journey into persistent Markdown notes rather than relying on one long chat;
- add architecture visualization only when complexity warrants it;
- repeatedly review findings and retain key implementation notes/file references.

Why retain:

- directly matches colleagues who must onboard to an unfamiliar codebase without first becoming experts in a new code-analysis product;
- reinforces scoped exploration + persistent evidence rather than one-shot repository summary.

Limitation: practitioner/community tutorial, not controlled validation.

### 4. Large-repository Agent workflow — current vendor implementation facts, actually read

**Anthropic — “How Claude Code works in large codebases: best practices and where to start”**  
https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start

Evidence role: **current agent-harness / large-repository practice anchor**.

Material current guidance:

- start from repository files, traversal, search and references rather than ingesting the entire repository into context;
- keep project instructions lean and layered;
- scope exploration to relevant subdirectories;
- use subagents to isolate exploration when useful;
- introduce LSP/symbol-based navigation when grep returns too many matches;
- excessive context can degrade performance.

This supports a conditional upgrade model:

> **Large repository ≠ automatically install a semantic code system. Upgrade when ordinary repository retrieval becomes the concrete bottleneck.**

Limitation: vendor guidance, not independent productivity proof.

**OpenAI — “Harness engineering: leveraging Codex in an agent-first world”**  
https://openai.com/index/harness-engineering/

Evidence role: **current repository-legibility / harness evidence**.

Material implication: agent performance depends heavily on what repository-local context and executable checks are legible and available to the Agent. Versioned architecture notes, schemas, tests and explicit boundaries are part of the engineering surface, not optional decoration.

Limitation: OpenAI internal/new-project experience; it should not be generalized as controlled proof for arbitrary legacy ERP estates.

### 5. Serena — serious semantic-navigation implementation, actually inspected

**oraios/serena @ `7fcbca7e62555ec2287ddb2f083caee805848ea6`**  
https://github.com/oraios/serena

Evidence role: **original implementation inspection**.

Current capabilities include:

- symbol-level semantic retrieval and references;
- LSP-backed support for many languages;
- symbol-aware editing/refactoring and diagnostics;
- MCP integration with coding Agents;
- optional project memory;
- JetBrains-backed deeper code intelligence as a paid option.

Why it is not the default recommendation:

- the project’s own positive evaluation is largely Agent self-evaluation rather than independent user outcome evidence;
- independent practitioner reports are mixed: some users find symbol/reference navigation highly valuable on large repositories, while others report little incremental value over improved native Agents or loss of useful context during debugging.

Representative counter-evidence:

**Serena issue #449 — context filtering can hurt debugging**  
https://github.com/oraios/serena/issues/449

**r/ClaudeAI — “Serena MCP on large monolith” discussion**  
https://www.reddit.com/r/ClaudeAI/comments/1mp6di0/

Practical implication:

> Serena is a reasonable **conditional trial** when symbol/reference navigation is repeatedly expensive; it is not evidence that every ERP codebase needs an extra MCP layer.

### 6. CodeGraph — promising implementation, insufficient independent evidence for default adoption

**codegraph-ai/CodeGraph**  
https://github.com/codegraph-ai/CodeGraph

Evidence role: **original implementation inspection / emerging candidate**.

The project builds a tree-sitter semantic graph and exposes call graphs, dependency graphs, impact analysis, related tests, architecture-doc generation and MCP tools across many languages.

Why not recommend as default now:

- its capability surface is highly task-relevant, but the project is new and most performance/retrieval claims are author-provided;
- no independent evidence found in this rerun showed enough decision-changing advantage over native repo-aware Agent + conditional LSP/semantic navigation.

Keep as a future candidate when a real repository exposes a graph-navigation bottleneck.

### 7. SAP ABAP — system-native context is a real capability gap

**SAP — “With Agentic AI, ABAP Takes Evolution to the Next Level”**  
https://news.sap.com/2026/08/with-agentic-ai-abap-takes-evolution-to-the-next-level/

Evidence role: **current SAP adoption/risk anchor**.

SAP explicitly warns that AI-generated code may look plausible while containing subtle errors, and that preserving business logic during legacy transformation is critical. Human review and testing remain required.

**SAP Help — Model Context Protocol Tools**  
https://help.sap.com/docs/abap-cloud/abap-development-tools-user-guide/model-context-protocol-tools

Evidence role: **official current capability anchor**.

Current ADT MCP tooling exposes SAP-native repository/test/analysis operations such as repository objects, activation, transports/diffs, ABAP Unit and ATC. This is materially different from a generic local-repository Skill because the Agent gains access to system-native objects and checks that may not exist as local files.

**SAP Help — Security Recommendations and Considerations**  
https://help.sap.com/docs/abap-cloud/abap-development-tools-for-visual-studio-code/security-recommendations-and-considerations

Evidence role: **official security boundary**.

SAP warns that MCP/client/environment compromise can expose connected capabilities and that additional MCP servers must be understood and governed.

**SAP Help — SAP-ABAP-1 example payloads**  
https://help.sap.com/docs/sap-ai-core/generative-ai/example-payloads-for-inferencing-sap-abap-1

Evidence role: **domain-model/current fact companion**.

Current guidance itself notes that long/incomplete/erroring ABAP context can produce suboptimal explanation. A domain model can improve ABAP syntax/context handling, but it is not proof of business intent.

### 8. Community ABAP FS — concrete live-system implementation inspected

**marcellourbani/vscode_abap_remote_fs — MCP server docs @ `646eb6f1b127bb0efa34a3fd9c08106db84805ec`**  
https://github.com/marcellourbani/vscode_abap_remote_fs/blob/646eb6f1b127bb0efa34a3fd9c08106db84805ec/docs/mcp-server.md

Evidence role: **original implementation / adoption-boundary evidence**.

Verified current capabilities include SAP object search/source retrieval, where-used analysis, ABAP Unit, ATC, SQL and diagnostics through a local MCP bridge.

Important risk:

- write support exists;
- edits are immediately synchronized to SAP;
- the documented workflow has no keep/undo UI.

Therefore for code-understanding work the safe default is **read-only / Plan-mode / least-privilege access**, not “connect the Agent and let it change SAP”.

Use official SAP tooling where organizational support/policy permits; community ABAP FS is a practical alternative/companion, not a universal prerequisite.

## Recommended colleague workflow

### Default — ordinary local repository

Use a competent repo-aware coding Agent and keep the first pass read-only.

1. Start from a concrete question or deliverable, not “understand the whole repository”.
2. Establish the repository evidence base:
   - build/test/run commands;
   - top-level modules and likely ownership;
   - entry points;
   - schemas/tables/configuration;
   - external integrations;
   - tests and relevant design/requirement docs.
3. Pick one business flow/use case and trace it:
   - entry/API/job/UI event;
   - controller/interface;
   - service/domain logic;
   - persistence/integration;
   - validations, permissions, side effects and errors;
   - related tests/logs.
4. For every material statement, label it:
   - **Observed code fact** — file/symbol/test/log evidence;
   - **Inference** — supported interpretation, not fact;
   - **Unknown / business confirmation required**.
5. Produce the review artifact: flow/call map + rules/branches + source references + open questions.
6. Only after the model is reviewed should modification begin. Keep changes small, diffable and test-backed.

### Reverse-generate FS / functional logic

- describe **implemented behavior**, not invented intent;
- keep source references for each important rule/branch;
- flag contradictory/dead/ambiguous logic;
- compare code with tests, tickets/docs and runtime evidence when available;
- send unresolved business meaning back to a domain owner rather than letting the model guess.

### Defect analysis

AI output is a hypothesis until verified by at least one appropriate mechanism:

- reproducible test;
- log/trace;
- static analyzer/compiler/ATC;
- runtime observation;
- database/query evidence.

### Performance analysis

Do not promote a “code smell” into a performance defect without measurements such as profiling, query plan, runtime metrics or load evidence.

## Upgrade triggers

### Add LSP / semantic navigation when

- grep/text search returns too many irrelevant matches;
- symbol references/implementations are expensive to reconstruct manually;
- cross-module call chains dominate the task;
- repeated codebase onboarding makes the setup cost worthwhile.

Prefer native Agent/IDE code-intelligence integration first. Trial a dedicated tool such as Serena only when the bottleneck is observable.

### Add graph-oriented tooling when

- call/dependency/blast-radius questions recur and cannot be answered economically by native navigation;
- a real repository test can establish that the graph reduces review/retrieval effort without hiding critical context.

Do not introduce CodeGraph merely because a repository is “large”.

### Add ERP/system-native MCP when

- the authoritative source/metadata/runtime is not present as normal local files;
- system-native where-used/test/static-analysis/transport information changes the answer.

SAP ABAP is the clearest current example. Use least privilege and read-only exploration by default.

## Adversarial checks

### Rejected: “larger codebase → install a specialist MCP”

Large size alone is not an adoption criterion. Native Agents already traverse/search repositories, and current vendor guidance itself recommends semantic/LSP escalation when ordinary search becomes noisy.

### Rejected: “AI explained it, therefore we understand the business logic”

Explanation is not intent evidence. Legacy implementation can encode obsolete rules, accidental behavior or undocumented edge cases. Reverse-generated FS must separate observed behavior from inferred business meaning.

### Rejected: “two models agree / tests pass, therefore the implementation is understood”

Recent practitioner evidence directly contradicts this. Tests may validate only what the generated tests assert, and two models can converge on the same unnecessary design.

### Rejected: “SAP MCP access means Agent autonomy should increase”

The opposite risk exists: live SAP connectors can expose write/activation capabilities. P07 is an understanding task, so privilege should stay below the maximum capability available.

### Rejected: “semantic retrieval is always better context”

Serena counter-evidence shows aggressive context narrowing can omit information needed for difficult debugging. Semantic tools are retrieval aids, not correctness authorities.

## Coverage gaps

- no independent controlled ERP benchmark compares native Codex/Claude Code/Cursor vs Serena/CodeGraph on the same large legacy repository;
- no supplied real customer repository was available for a representative runtime comparison;
- Oracle/custom-system estates vary substantially in how much authoritative runtime/configuration lives outside Git, so SAP’s system-native boundary should not be blindly generalized to every ERP product.

These gaps are explicit but do not block the current adoption decision.

## Runtime decision

> **No synthetic local/runtime A/B required for P07 now.**

A benchmark on this repository or an invented legacy project would not resolve the important uncertainty: whether a real colleague’s large/legacy/system-native estate has a retrieval or access bottleneck that native Agent tooling cannot handle economically.

Current evidence is sufficient to set the upgrade rule:

- ordinary local repo → scoped read-only repo-aware Agent first;
- concrete symbol/call retrieval bottleneck → LSP/semantic tool trial;
- authoritative code/system evidence outside local files → system-native MCP;
- business intent uncertainty → human/domain evidence, not more tooling.

A future runtime comparison is justified only on a real representative repository and a concrete unresolved choice, for example native search vs Serena on a large monorepo or plain local Agent vs SAP-native MCP on live ABAP analysis.

## Stop decision

P07 is decision-complete because it now covers:

- professional comprehension workflow;
- independent practitioner success and failure evidence;
- Chinese practical workflow;
- current large-repository Agent guidance;
- serious semantic/graph implementation inspection;
- SAP-specific live-system capability and security boundary;
- business-intent/correctness limitations;
- explicit upgrade triggers;
- explicit reason not to manufacture a synthetic runtime test.

Further tool search is unlikely to change what a colleague should do first.

## Next project action

Reassess the trustworthy heterogeneous evidence base as a whole. Only now decide whether the Curator method is stable enough to package a minimal user-facing Curator and enter a bounded real-user adoption pilot.
