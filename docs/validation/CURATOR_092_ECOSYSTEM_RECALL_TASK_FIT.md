# Curator 0.9.2 — Ecosystem Recall / Task-Fit Correction

Date: 2026-08-31
Status: **DECISION-CHANGING RUNTIME DEFECT — PATCH IMPLEMENTED**

## 1. Trigger

A fresh 0.9.1-style flowchart curation result correctly avoided generic Skill installation and returned a Chinese practitioner resource, a SAP BTP draw.io implementation, and official draw.io documentation.

The answer was usable, but adversarial review found two linked defects:

1. the serious Chinese practitioner candidate pool stopped after one visible pool (Bilibili), while Zhihu/Xiaohongshu and other likely Chinese practitioner pools were absent;
2. an adjacent SAP BTP architecture-diagram implementation was promoted into the Top 3 for a business-process-flow task, while official draw.io documentation was also presented as a peer recommendation rather than capability verification.

## 2. Cloud reproduction

On 2026-08-31, targeted current Web discovery for the same AI + editable-flowchart / product-manager / ToB task immediately surfaced recent Zhihu candidates that were absent from the returned candidate set, including current 2026 practitioner-style Mermaid / editable visual-workflow material.

Those candidates were materially closer to the requested business/process-flow artifact than the SAP BTP architecture implementation.

A targeted Xiaohongshu pass did not return inspectable current results through normal Web. This remains a coverage fact, not evidence that Xiaohongshu lacks useful content.

## 3. Why this changes the decision

This is not a request for platform completeness.

The defect is decision-changing because targeted ecosystem recall can change which resources deserve Top recommendation. The problem is therefore not "Xiaohongshu must appear"; it is **premature candidate-pool convergence**.

Likewise, the SAP BTP resource is not bad. It is a useful adjacent technical-architecture example. The defect is allowing a nearby artifact to outrank more direct practitioner evidence simply because it carries strong SAP/ERP specificity.

## 4. 0.9.2 correction

Practice Curator now adds two narrow rules.

### 4.1 Candidate-pool concentration trigger

For Chinese ERP / ToB / product / project / consultant tasks, before concluding:

- if serious candidates come from only one accessible Chinese practitioner pool; or
- if the remaining serious candidates are mainly official/vendor/implementation/global sources;

run one targeted recall pass against the 1–2 additional practitioner pools most likely to change the ranking.

Stop when the candidate pool is strong enough. This is not a Bilibili + Zhihu + Xiaohongshu + WeChat quota.

Zero recall or access failure is recorded as `coverage/policy gap` only when material. It does not justify installing or building a platform adapter by default.

### 4.2 Task-fit anti-dilution

Adjacent deliverables cannot displace the actual requested artifact merely because they have a stronger SAP/ERP/tool label.

Examples:

- SAP BTP architecture diagram ≠ ERP business process flow;
- SVG/PNG output ≠ editable draw.io;
- generic BPMN standard page ≠ practitioner AI workflow.

Adjacent material can remain specialist/secondary evidence when it contributes a method missing from direct candidates.

Official documentation normally stays in a separately labeled capability-verification role rather than filling a practitioner Top 1–3 list.

## 5. Xiaohongshu / Zhihu boundary

0.9.2 does **not** hard-code mandatory Xiaohongshu or Zhihu results.

Current project evidence already shows:

- targeted normal Web can improve some Bilibili/Zhihu recall;
- WeChat/Xiaohongshu can remain weak or zero-recall;
- the previously inspected Xiaohongshu MCP was removed because its permission surface, browser/runtime/setup cost and operational burden were disproportionate.

Therefore the correct product behavior is:

> try the cheapest decision-changing recall correction first; if a likely ecosystem remains inaccessible, state the coverage gap and continue with the best inspectable evidence.

## 6. Capability Advisor

No behavior change. Its metadata version moves to 0.9.2 only to keep the two-Skill Runtime package version aligned.

## 7. Evidence boundary

This patch is supported by:

- the supplied fresh flowchart answer;
- adversarial task-fit review;
- same-day targeted current Web discovery showing omitted Zhihu candidates that could change ranking;
- existing project source-acquisition evidence that Xiaohongshu normal-Web coverage remains unresolved.

It does not prove:

- 0.9.2 works correctly in every host;
- Xiaohongshu coverage is solved;
- mature source-composition Skills are effective;
- product value is validated.

## 8. Next evidence

Do not start a new synthetic matrix.

Use 0.9.2 in controlled real-user use. If a real task still shows premature practitioner-pool convergence or task-fit dilution, collect the actual search/open logs and make the narrowest correction.

Lane B remains the product-value authority.
