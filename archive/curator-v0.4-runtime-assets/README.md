# Curator V0.4 Runtime Assets Archive

Archived during Minimal Curator V0.1 Skill hardening (`0.6.1`).

These files belong to the earlier resource-curation-system phase and include historical Gate/scoring/taxonomy/data-model rules, validators, scripts and adversarial eval assets. They remain useful for historical audit or targeted regression, but they are **not current runtime authority** for the Minimal Curator.

Reason for archiving:

- current product method is real-task-first and General-AI-first;
- fixed Gate/scoring/taxonomy mechanisms are explicitly outside the default product path;
- retaining these files inside the distributable Skill creates a risk that future Agents or contributors reload obsolete V0.4 behavior;
- Git history and this archive preserve the evidence without polluting runtime progressive disclosure.

Pre-hardening baseline commit:

- `377d3bca86dbdf1408b2a5ef9b603653e8e6cac9`

Current runtime authority:

- `skills/curating-erp-ai-resources/SKILL.md`
- `skills/curating-erp-ai-resources/references/decision-boundaries.md`
- `skills/curating-erp-ai-resources/references/evidence-and-safety.md`

Do not restore archived rules into the permanent Skill unless real-user evidence exposes a recurring defect that cannot be handled more simply.
