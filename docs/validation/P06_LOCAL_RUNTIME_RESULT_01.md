# P06 Local Runtime Delta — Result 01

Date: 2026-08-30
Candidate: `alchaincyf/huashu-excel` at `9348581a87cc03ed8d0b30706631088e922c6027`

## Verdict Proposal

> **PLAIN CODE-FIRST ENOUGH**

For this bounded ERP-style reconciliation, Huashu produced one material extra finding—the legacy `TOTAL` was wrong by 10—but it did not improve any record-level match, duplicate, missing-record, key-normalization, field-change, ambiguity, row-count, amount, or replay result. The extra finding came from a useful control-total habit, not from an advantage that required this Skill; a capable code-first Agent can add the same check directly with small incremental logic. Huashu is therefore useful as an optional checklist for recurring/high-consequence work, but this run does not justify mandatory Skill adoption over plain code-first execution.

## Experiment boundary

- Inputs were synthetic only: one messy ERP legacy `.xlsx`, one reordered target `.csv`, and one explicit plant mapping `.csv`.
- The fixture contained title/header offset, text-formatted currency, whitespace/case differences, numeric leading-zero differences, one exact duplicate, one missing target, one target-only row, one amount change, one status change, and one two-source-to-one-target ambiguous key.
- Source detail population: 10 rows / 11,530; target: 8 rows / 9,985.
- Legacy control rows stated `WH01=6,400`, `WH02=3,900`, `WH03=1,230`, `TOTAL=11,540`; detail truth is `TOTAL=11,530`.
- Baseline and with-Skill ran in separate fresh directories with byte-identical input copies. The hidden truth was outside both contexts until both outputs existed.
- Both reconciliation CSVs were stable across a second run; each produced SHA-256 `D0BE37781BCDF52292968ADD7A2C991E2B60913325F4C35F669F6264E7B89C9A`.

Compact fixture and run evidence: [`evidence/p06/`](evidence/p06/).

## Baseline actual approach and result

The fresh plain code-first context used explicit Python with no Huashu reference. It detected the header by column names, excluded rows labelled `SUBTOTAL` / `TOTAL` / `NOTE`, normalized only trim/case/numeric leading-zero differences, applied `plant_mapping.csv`, indexed both sides by normalized document key, and routed non-unique candidates to review.

It correctly returned all nine expected key outcomes:

- 3 `MATCH`;
- 1 amount mismatch (`456`, target +5);
- 1 status mismatch (`321`);
- 1 duplicate-source review (`888`);
- 1 ambiguous-source review (`77`);
- 1 missing target (`777`);
- 1 target-only (`999`).

Its explicit source/target row and amount totals were correct. Its material omission was that it excluded control rows without comparing them back to detail. Consequently, the incorrect `TOTAL=11,540` was not surfaced. There was no record-level silent error, but there was one silent control-coverage gap and no rework pass.

Artifact: [`baseline_result.json`](evidence/p06/baseline_result.json), [`baseline_reconciliation.csv`](evidence/p06/baseline_reconciliation.csv).

## With-Skill actual approach and result

The fresh with-Skill context read the pinned `SKILL.md` and ran `profile_table.py`, `verify_numbers.py`, and `clean_table.py`, then inspected their output before performing the keyed reconciliation.

Huashu changed behavior in four real ways:

1. Raw-cell profiling surfaced the title/header offset, text-formatted amounts, whitespace, exact duplicate at source row 9, and the `TOTAL` control row before flattening.
2. `verify_numbers.py` failed its master check instead of allowing the stated total to pass. Its first calculation was inflated because the pinned script did not classify `SUBTOTAL WH01/02/03` as summary rows; the labels exceed its 12-character summary-label heuristic.
3. Following the Skill’s “read the output and do not guess” method, the Agent manually reclassified those three subtotal rows and retained the corrected finding: detail `11,530` versus stated total `11,540`, difference `10`.
4. `clean_table.py` emitted a replayable cleaned CSV and preserved duplicates; after the manual subtotal correction, the same 10 detail rows were reconciled with source-row traceability.

After that repair, the with-Skill reconciliation returned exactly the same nine expected key outcomes and the same stable CSV as baseline. It added no record-level accuracy or ambiguity improvement beyond baseline.

Artifacts: [`with_skill_result.json`](evidence/p06/with_skill_result.json), [`with_skill_reconciliation.csv`](evidence/p06/with_skill_reconciliation.csv), [`with_skill_verify_numbers.json`](evidence/p06/with_skill_verify_numbers.json), [`with_skill_clean_output.txt`](evidence/p06/with_skill_clean_output.txt).

## Ground Truth comparison

Independent verification read the hidden truth only after both runs and compared the output CSVs, not just the reported counts. Baseline and with-Skill each matched all 9 expected statuses; neither emitted an extra or unrecognized key. Both correctly handled key formatting, mapping, duplicate/ambiguous isolation, missing/target-only records, changed amount/status, counts, and totals.

The only truth-level delta was the legacy control row: baseline did not test it; with-Skill found it after one manual correction. No side guessed an ambiguous match.

Evidence: [`ground_truth.json`](evidence/p06/ground_truth.json), [`independent_verification.json`](evidence/p06/independent_verification.json).

## Omissions, silent errors, and rework

| Aspect | Baseline | With-Skill |
|---|---|---|
| Record-level silent error | None observed | None observed |
| Control-total coverage | Omitted; wrong 11,540 passed unchallenged | Found; corrected detail scope exposed 10 difference |
| Duplicate / ambiguous handling | Correct review routing | Same review routing |
| Replayability | Deterministic script/run | Cleaned CSV plus deterministic script/run |
| Rework | None | One subtotal-classification repair; UTF-8 output setting on Windows |

## Adoption Cost

- Baseline used the existing local Python runtime and one small deterministic script; no Skill checkout or special environment setting was needed.
- With-Skill required a temporary pinned checkout, reading a large method document, running three scripts, interpreting their outputs, manually repairing subtotal classification, and setting `PYTHONIOENCODING=utf-8` because the scripts failed on the default Windows console encoding when emitting `¥` / checkmark JSON.
- The candidate’s practical dependency surface is light (`openpyxl` for `.xlsx`), and the checkout was isolated and not installed globally. The main cost is workflow and method overhead, not package size.
- The unique control-total benefit is straightforward to reproduce in the baseline’s existing code: compare each captured control row against the scoped detail sum and fail the master check. This is a small method addition, not a demonstrated need for a new runtime dependency.

## Strongest argument against the apparent winner

The strongest argument against `PLAIN CODE-FIRST ENOUGH` is that the hidden 10-unit control error is exactly the kind of low-visibility ERP reconciliation defect that an auditor or reviewer needs surfaced. If the baseline is routinely written without control-total checks, Huashu’s master-check discipline can prevent a real silent failure and may be worth standardizing for high-consequence recurring jobs. This evidence supports carrying that discipline forward; it does not isolate the benefit to Huashu itself.

## Stop Rationale

The stop condition is met: both methods were equally correct on every record-level risk in the fixture, while the only unique Skill delta is one control-total omission exposed by a check that can be added directly to plain code-first. Further cases would be unlikely to change the adoption recommendation without testing a broader family of summary-label structures or showing repeated Skill-specific catches, which would exceed this bounded P06 delta. Keep Huashu’s control-total / no-guessing practices as optional guidance, not as a mandatory dependency.

## Owner / Cloud Decision Needed

`None`

## Task Envelope self-check

- Started from the freshly synchronized GitHub `main` and created `validation/p06-local-runtime-delta`.
- Candidate was checked out only in a temporary detached checkout at the pinned commit.
- Used synthetic ERP-like data only; no credentials, SaaS accounts, production/customer data, or global installation.
- Baseline did not receive Huashu instructions or candidate files; both contexts had identical input copies and hidden truth remained inaccessible until completion.
- No broad Web search, governance/principle/Loop changes, other Problem Card, benchmark framework, new Gate, unrelated Skill/MCP/Adapter, or merge to `main`.
