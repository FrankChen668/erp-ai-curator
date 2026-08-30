# Tests directory status

Current status: **no active recommendation-quality test suite**.

`tests/fixtures/v0.4-regression/` contains historical V0.4 fixtures only. They are retained for repository history and must not be interpreted as the current Curator eval contract.

Current deterministic repository/Harness checks live in:

- `scripts/check_project_contract.py`
- `.github/workflows/project-contract.yml`

Those checks validate project facts and wiring only. They do not score recommendation quality or substitute for REAL_USER_USE evidence.
