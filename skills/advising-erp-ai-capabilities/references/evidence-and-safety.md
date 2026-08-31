# Evidence and Safety

Read this when an adoption recommendation depends on executable third-party resources, system access, volatile external claims, or meaningful permission/privacy risk.

## Evidence roles

Keep these distinct:

- **independent practitioner** — real adoption, review, or failure experience;
- **author self-practice** — creator/vendor/maintainer demonstrating their own approach;
- **implementation** — original Tool/Skill/MCP/repo;
- **official fact** — current version, compatibility, price, permission, privacy, license, or standard semantics;
- **Advisor synthesis** — the adoption conclusion from acquired evidence.

Author self-practice can show how something works; it is not independent proof that it is objectively better. Search snippets, titles, installs, stars, and engagement metadata are discovery hints only.

## Claim calibration

Trace decision-changing claims to content actually opened/read.

Prefer task-relative language such as:

- current best fit for this concrete gap;
- smallest capability worth adding;
- strongest direct candidate currently found.

Use “best / unique / validated / industry standard” only when the acquired evidence supports that scope.

## Executable-resource checks

Before recommending installation or execution of a Skill, MCP, plugin, script, or integration, check proportionately:

- install/runtime dependencies;
- accounts, credentials, and secret handling;
- filesystem, shell, browser, network, or enterprise-system permissions;
- write/destructive actions and data egress;
- maintenance/current compatibility;
- price/license when material.

For understanding and diagnosis, prefer read-only and minimum necessary access. A capability being able to write does not justify granting write access.

Use runtime/local testing only when static evidence is insufficient and the result could materially change the recommendation.

## Business-truth boundary

AI-generated diagrams, documents, code explanations, and workflows are proposals, not ERP/system truth.

When the decision depends on real system behavior, ground it in the user's actual materials, project docs, code/config/tests/logs, ERP metadata, or trustworthy original facts. Keep fact, inference, and unknowns separate.
