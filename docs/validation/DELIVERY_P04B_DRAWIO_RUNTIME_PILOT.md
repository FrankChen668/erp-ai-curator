# P04B — Pinned draw.io Codex Skill Runtime Pilot

Date: 2026-08-30

## 1. Purpose

P04A found a strong candidate but only from documentary evidence.

P04B tests one narrow question:

> **Can the pinned official draw.io Codex Skill actually produce and revise a useful editable ERP business-process diagram in the current local Windows/Codex environment with acceptable operational cost?**

This is a runtime qualification, not a new curation search.

## 2. Candidate

Repository:

- https://github.com/jgraph/drawio-mcp

Pinned commit:

- `14b318b19cc37b159f841227b9d11fbd18ce18ea`

Plugin:

- marketplace: `drawio`
- plugin: `drawio@drawio`
- path: `plugins/codex/drawio`

Do not install from moving `main` for this pilot.

## 3. Environment protection

Before changing plugin state:

- record `codex --version`;
- record `codex plugin list --json`;
- record `codex plugin marketplace list --json`;
- copy the current Codex config file to a temporary backup and record its hash;
- do not modify or remove built-in/OpenAI marketplaces;
- do not hand-edit Codex plugin configuration unless cleanup cannot be performed by supported commands.

Windows Codex plugin/marketplace state has had configuration/reconciliation bugs. Treat cleanup as part of the test.

If the required `codex plugin` commands are unavailable, stop and report the exact CLI/version blocker.

## 4. Pinned install

Clone `jgraph/drawio-mcp` into a temporary directory and checkout exactly:

`14b318b19cc37b159f841227b9d11fbd18ce18ea`

Verify HEAD matches exactly.

Register that **local pinned clone** as the marketplace, then install:

```text
codex plugin marketplace add <PINNED_LOCAL_CLONE>
codex plugin add drawio@drawio
```

Record actual command output and installed plugin path.

Do not upgrade or sync the marketplace during the pilot.

After install, use a fresh Codex session so plugin discovery is not inherited from the pre-install session.

## 5. Test input

Use this synthetic-but-representative ERP process. Do not add business facts not listed here.

### Scenario — Purchase requisition to purchase order with exception

Roles / lanes:

- Requesting Department
- Procurement
- Department Manager
- ERP System

Confirmed flow:

1. Requesting Department creates a purchase requisition in ERP.
2. ERP checks whether the requisition amount is greater than CNY 100,000.
3. If amount is greater than CNY 100,000, Department Manager approval is required.
4. If Manager rejects, requisition returns to Requesting Department for revision.
5. If Manager approves, flow continues to Procurement.
6. If amount is not greater than CNY 100,000, flow goes directly to Procurement.
7. Procurement reviews supplier and commercial information.
8. If supplier information is incomplete, Procurement returns the requisition to Requesting Department for supplementation.
9. If information is complete, Procurement creates the purchase order in ERP.
10. ERP records the PO number and process ends.

Known system/document handoffs:

- Purchase Requisition (`PR`)
- Purchase Order (`PO`)
- ERP is the system of record for PR and PO

Unknown / not supplied:

- exact transaction code;
- exact approval workflow technology;
- supplier master approval process;
- budget-check process.

These unknowns must not be invented.

## 6. Generation task

Ask the installed draw.io Skill to create a **native editable `.drawio`** business-process diagram.

Required representation:

- four lanes/roles;
- amount gateway with both branches labelled;
- manager rejection loop;
- supplier-information exception loop;
- PR and PO labels;
- ERP handoffs / system touchpoints;
- unknown items not invented;
- title and readable labels.

The first run may use Mermaid or XML according to the Skill's own routing.

Do not force XML merely because P04A guessed it would be better.

Record which authoring path the Skill actually chose and why, if observable.

## 7. Artifact checks

The run is only technically useful if:

- a `.drawio` file is actually created;
- the file is parseable / structurally valid enough for draw.io;
- every required lane/decision/exception/handoff above is visible in the artifact;
- no unsupported business fact is added;
- labels are readable;
- the artifact can be opened in draw.io Desktop or an official draw.io browser path.

If Desktop is installed, open it and confirm editability.

If Desktop is not installed, do not install Desktop automatically. Use the Skill's supported XML/browser path and report the limitation.

A PNG/SVG preview is optional; the `.drawio` is the primary artifact.

## 8. Revision test

After the first diagram is produced, make exactly this change:

> Change the approval threshold from CNY 100,000 to CNY 200,000. Do not change any other process semantics.

Ask the Skill to revise the existing diagram.

Verify:

- threshold changed in the diagram;
- all other nodes/branches remain materially unchanged;
- artifact remains editable;
- no new unsupported process step appears.

This tests whether the workflow supports realistic consultant correction rather than only one-shot generation.

## 9. Semantic distinction

Do not claim BPMN 2.0 compliance unless the artifact is actually BPMN 2.0 XML and validated as such.

A draw.io diagram using BPMN-like shapes is a review diagram, not automatically a semantically validated BPMN model.

## 10. Runtime dependency observations

Record whether the Skill attempts network access to retrieve its shared GitHub references during use.

Record:

- whether generation works offline after install;
- whether GitHub access is required at runtime;
- any error/fallback when references cannot be fetched;
- any dependency on draw.io Desktop / Node / browser.

Do not alter network policy merely to force success.

## 11. Cleanup

After evidence is captured:

```text
codex plugin remove drawio@drawio
codex plugin marketplace remove drawio
```

Then record again:

- `codex plugin list --json`;
- `codex plugin marketplace list --json`;
- Codex config hash/diff against the pre-test state.

Do not remove unrelated plugins/marketplaces.

If cleanup leaves unexpected state, stop and report it. Do not hide it by destructive config replacement.

## 12. Final output only

### Runtime result
`PASS / PARTIAL / FAIL`

### Environment
- Codex version
- OS
- draw.io Desktop present: Yes/No

### Pin / install
- exact repo SHA
- install result
- installed path

### First artifact
- `.drawio` path
- opened successfully: Yes/No
- lanes present: Yes/No
- gateways/branches present: Yes/No
- exception loops present: Yes/No
- system/document handoffs present: Yes/No
- unsupported business facts invented: Yes/No

### Revision artifact
- threshold changed only: Yes/No
- still editable: Yes/No
- unintended semantic changes: Yes/No

### Runtime dependencies
- network/reference fetch observed
- Desktop dependency observed
- other dependencies/errors

### Cleanup
- plugin removed: Yes/No
- marketplace removed: Yes/No
- unrelated Codex state changed: Yes/No

### Main failure
Only if PARTIAL/FAIL.

### Product implication
Choose one:

- `KEEP FOR PRACTICAL PILOT`
- `KEEP WITH RUNTIME CAVEAT`
- `DO NOT RECOMMEND YET`

Then stop.

Do not search for new tools.
Do not run P02/P03/P05/P06.
Do not modify ERP AI Curator repository.
