# Curation Pack 01 — Adversarial Review

Date: 2026-08-30
Status: **CLOSED — CONTROLLED USER TRIAL READY, PRODUCT VALUE UNVALIDATED**
Skill: `curating-erp-ai-resources` `0.7.0`

## 1. Review question

This review does **not** ask whether the four outputs look polished.

It asks whether the current Curator method is sufficiently coherent and bounded to expose to real users without first adding more internal rules/tests.

Pack 01:

- Case 001 — ERP operating manual — B;
- Case 002 — Oracle EBS AI-assisted development — B;
- Case 003 — weekly report consolidation/data accuracy — A;
- Case 004 — SAP bug diagnosis/system evidence access — A → conditional B.

All four are REAL_USER_ORIGIN inputs. None are REAL_USER_USE evidence.

## 2. Strongest attacks

### Attack 1 — Is Curator still just a tool recommender?

No recurring signal in Pack 01.

- Case 003 recommends **zero** new external resources because the capability gap is not a new AI tool.
- Case 004 keeps current AI when exported evidence is sufficient and upgrades only for missing system evidence access.
- Case 001/002 recommend reusable working patterns before product names.

Bounded conclusion: over-tooling is not the dominant failure in this pack.

### Attack 2 — Has General-AI-first become under-tooling?

No recurring signal in Pack 01.

- Case 001 identifies capture/maintenance capability as a genuine gap.
- Case 002 identifies persistent EBS project context as a gap and preserves heavier system access as an upgrade boundary.
- Case 004 explicitly upgrades when runtime/system evidence cannot be obtained through the current baseline.

This does not prove under-tooling can never happen; it means the 0.7.0 consistency guardrail behaves coherently across these cases.

### Attack 3 — Are weak sources being overstated as “best practice”?

Improved but still a product risk.

- Case 001 uses community discussion plus original capability checks and labels the final pattern as curator synthesis.
- Case 002 explicitly labels JMJ Cloud as author self-practice, not independent validation.
- Case 003 does not manufacture external evidence when none is necessary.
- Case 004 relies primarily on SAP source/system facts for the evidence-access boundary and does not pretend Joule adoption is independently proven.

No current case should be described as universally “industry best”. The defensible language is **current-task priority recommendation under acquired evidence**.

### Attack 4 — Are we secretly turning users into testers?

No in current outputs.

Case 001 historical drift was corrected. Cases 003/004 do not ask the user to run an experiment for the project's benefit. C only remains a low-complexity adoption state, not a test-coordinator mode.

### Attack 5 — Does Pack 01 prove Curator is better than ordinary AI/search?

**No. This is the strongest unresolved attack.**

Pack 01 demonstrates method behavior on real-origin problems. It does not demonstrate:

- faster user decision-making;
- less search effort;
- fewer wrong-tool choices;
- lower setup/rework;
- higher trust;
- return usage;
- repeatable uplift over ordinary AI/self-search.

Any claim that “the product goal is complete” would exceed the evidence.

### Attack 6 — Is the runtime Skill now too large/rigid?

No material new signal.

0.7.0 remains a judgment-oriented Skill with three focused references and no scenario taxonomy, scoring system, resource database or mandatory runtime pipeline.

The remaining risk is not rule scarcity. More internal rules before user use would likely increase ceremony/context cost faster than product value.

## 3. Case-specific residual risks

### Case 001

Residual risk: independent practitioner evidence is limited; tool/vendor landscape can change quickly.

No immediate Skill change justified.

### Case 002

Residual risk: “context engineering” may be valuable generic coding practice rather than a Curator-specific insight; user may already know it.

This is exactly the type of issue REAL_USER_USE feedback must resolve.

### Case 003

Residual risk: A can flip to B when repeated cross-system data movement is the real bottleneck. Upgrade signals are explicit, so no current defect.

### Case 004

Residual risk: SAP product/version/access diversity is high. The correct recommendation must remain conditional on actual system evidence/permissions and must not generalize current Joule/ABAP MCP capabilities to every SAP environment.

## 4. Cross-case verdict

Pack 01 provides enough discrimination to stop internal curation expansion:

- clear A/no-new-tool behavior exists;
- B is tied to observable capability gaps;
- system-access boundary is explicit;
- author self-practice is separated from independent evidence;
- Curator/execution-coach boundary is preserved;
- no new Gate/scoring/taxonomy is required.

Therefore:

> **STOP INTERNAL PACK EXPANSION. MOVE TO CONTROLLED REAL-USER USE.**

## 5. What “ready” means

### Ready

- give Skill 0.7.0 to a small number of real ERP/enterprise-information-system users;
- let them ask their natural reusable-AI-working-method questions;
- allow the Skill to return A/B/C without forcing a resource;
- capture natural acceptance/rejection/missed-constraint feedback.

### Not yet ready to claim

- validated product;
- proven productivity gain;
- proven superiority to ordinary AI/search;
- organization-wide standard;
- universally best ERP AI practice engine.

## 6. No further pre-user Skill changes

Do not change Skill 0.7.0 before controlled user use unless a concrete release blocker is found.

Any 0.7.x/0.8 change should now be triggered by one of:

- real-user trigger failure;
- real-user over/under-tooling;
- evidence-role misclassification;
- missed security/permission/version constraint;
- user cannot understand/action the recommendation;
- repeated host/runtime compatibility problem.

## 7. Next evidence

The next high-value evidence is REAL_USER_USE:

```text
natural user problem
→ Skill 0.7.0 recommendation
→ user accepts / modifies / rejects / ignores
→ concrete reason
→ optionally actual downstream use/result
```

Do not manufacture a user test script to obtain this evidence.
