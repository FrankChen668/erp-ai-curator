# OWNER_REAL Dev-Adjacent Batch 02 — Agent Project Visualization

Date: 2026-08-29

Purpose: use a real owner-origin problem to separate three easily-confused jobs: **static architecture understanding, runtime observability, and graph-governed workflow design**.

This is an OWNER_REAL case. The role is product manager / Agent project owner, developer-adjacent; it must **not** be counted as independent developer-user validation.

## OR06 — “我 Vibe Coding 了 Agent 项目，想看清它的架构和运行路径；Graph Engineering 是不是装进去画一下就行？”

**Source:** OWNER_REAL  
**Role:** product manager / Agent project owner  
**Need external resource?** yes, once the question becomes “有什么现成 Skill / Tool 适合做这件事？”

## 1. First-principles split

The phrase “看 Agent 的 graph” can mean three different things:

### A. Static structure / architecture map

Question:

> 这个 repo 由哪些模块组成？依赖怎么连？API / DB / route 在哪里？

This is mostly read-only codebase understanding.

### B. Runtime trace / observability

Question:

> 一次真实请求进来后，Agent 调了哪个模型、哪个 Tool、哪个子 Agent、在哪里重试、耗时和 token 在哪里？

This requires runtime telemetry/tracing. A static code map cannot prove it.

### C. Governed workflow / work-contract graph

Question:

> 我想把合法下一步、完成证据、恢复路径、人审 Gate 固化成一个显式 graph，让 Agent 按事实路由。

This changes how work is modeled and executed. It is architecture/governance, not passive visualization.

**These three jobs must never be merged into one recommendation.**

---

## 2. If the real goal is “I don't code; help me understand the existing repo visually”

### Recommendation 1 — fadhlirahim/codebase-map

https://github.com/fadhlirahim/codebase-map

**Why it fits**

- explicitly built for “map this codebase / visualize this repo / help me understand this codebase visually”;
- outputs one self-contained interactive HTML file;
- architecture tab maps module dependencies;
- file explorer provides LOC treemap;
- stack-specific facets can expose API, DB, routes and jobs;
- no server/CDN required for the generated map;
- it reads the existing repo rather than asking the user to redesign the workflow first.

**Critical limitation**

- young/small project; maturity is not yet proven by broad adoption;
- it maps **code structure**, not actual runtime Agent behavior;
- the agent-written module descriptions still depend on model reading quality.

**Current position:** high task fit, medium trust/maturity.

### Recommendation 2 — Agents365-ai/drawio-skill

https://github.com/Agents365-ai/drawio-skill

Use this instead when the desired output is a durable **editable draw.io architecture artifact**.

**Why it is differentiated**

- active, broader community footprint;
- can extract import graphs from Python / JS-TS / Go / Rust codebases;
- supports Terraform / Kubernetes / docker-compose / SQL and other architecture inputs;
- outputs editable `.drawio` and can auto-layout / refine visuals.

**Critical limitation**

- heavier than a passive HTML codebase atlas;
- still primarily reconstructs architecture from code/dependencies; it does not automatically show runtime model/tool/sub-agent traces.

### Adjacent candidate — rta-lab/codebase-summary-skill

https://github.com/rta-lab/codebase-summary-skill

Useful when the primary output is a **technical written summary + Mermaid architecture + API inventory** rather than an interactive visual map.

It runs parallel research agents and schema validation, so it is more process-heavy. It is not the default choice for a non-coder whose main goal is simply “让我看懂这个项目”。

---

## 3. If the real goal is “show me what the Agent actually did at runtime”

### Resource direction — OpenTelemetry GenAI tracing / Langfuse Agent Graphs

OpenTelemetry current GenAI observability guidance:
https://opentelemetry.io/blog/2026/genai-observability/

Langfuse Agent Graphs:
https://langfuse.com/docs/observability/features/agent-graphs

**Why this is a different job**

Runtime observability records actual spans/events such as model calls, tool calls, timings, token usage and nested operations. Langfuse can infer/display an Agent Graph from trace observations.

**Critical limitation**

This is not “install a Skill and draw the repo”. The application/runtime has to emit useful telemetry or be instrumented through a supported SDK/integration/OpenTelemetry path.

Therefore a user who only wants passive architecture understanding should not be sent here first.

---

## 4. If the goal is “formalize the Agent workflow as a graph”

### Conditional recommendation — context4ai/agent-graph

https://github.com/context4ai/agent-graph

**What it actually is**

The project describes itself as a **work-contract layer for Agent Skills**. A graph defines legal steps; runtime facts determine the next Route; Actions/Gates/Outcomes/evidence define execution and completion. It explicitly says it coordinates work, not Agents, and never calls a model itself.

**Why it is not a passive visualizer**

Adopting it means defining/integrating:

- Provider / graph contract;
- Skill binding;
- host-supplied facts;
- route/gate/outcome handling.

The repository itself says installation alone does not make an existing Agent follow a workflow.

So for an existing Vibe-Coded project, this is **architecturally invasive in the sense of workflow modeling/integration**, even though it does not itself execute models or mutate the codebase automatically.

**When it becomes appropriate**

Use it only when the problem has moved from:

> “我想看懂现在是什么样”

into:

> “我想把下一步、完成证据、恢复和人审机制正式治理起来。”

---

## 5. Decision for OR06

For the owner's current “先看懂现有 Agent 项目” need:

1. **Start with a read-only/static map**, not Graph Engineering governance.
2. `codebase-map` is the cleanest conceptual fit for interactive understanding, but its maturity should be treated cautiously.
3. `Agents365-ai/drawio-skill` is the stronger option when editable diagrams and broader architecture extraction matter.
4. If the question is about actual execution history, use tracing/observability instead.
5. Only consider `agent-graph` after deciding to redesign/govern the workflow itself.

## 6. Product lesson for ERP AI Curator

Certain labels are overloaded. A resource should not be matched by label alone.

Before searching terms such as:

- graph engineering
- agent graph
- architecture visualization
- observability

first identify the **job**:

`static understanding / runtime evidence / workflow governance`

This is a task-understanding lesson, not a new taxonomy that every request must fill in.
