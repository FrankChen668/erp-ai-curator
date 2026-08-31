#!/usr/bin/env python3
"""Deterministic repository-contract checks for ERP AI Curator.

This script checks only machine-verifiable current structure and evidence-lane
boundaries. It intentionally does not duplicate semantic project state,
historical migration assertions, or version strings across documentation.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRACTICE_SKILL_DIR = ROOT / "skills" / "curating-erp-ai-resources"
ADVISOR_SKILL_DIR = ROOT / "skills" / "advising-erp-ai-capabilities"
RUNTIME_SKILL_DIRS = [PRACTICE_SKILL_DIR, ADVISOR_SKILL_DIR]
RUNTIME_SKILLS = [path / "SKILL.md" for path in RUNTIME_SKILL_DIRS]

RUNTIME_REFERENCES = [
    PRACTICE_SKILL_DIR / "references" / "practitioner-discovery.md",
    ADVISOR_SKILL_DIR / "references" / "evidence-and-safety.md",
]

CURRENT_REQUIRED = [
    ROOT / "README.md",
    ROOT / "docs" / "PROJECT_MAP.md",
    ROOT / "docs" / "PROJECT_NORTH_STAR.md",
    ROOT / "docs" / "OWNER_EXECUTION_RULES.md",
    ROOT / "docs" / "CURRENT_EXECUTION_PLAN_V3.md",
    ROOT / "docs" / "validation" / "EVIDENCE_STATUS.md",
    ROOT / "docs" / "REAL_USER_PILOT_V1.md",
    ROOT / "docs" / "USER_TRIAL_GUIDE_V1.md",
    ROOT / "docs" / "SESSION_HANDOFF_CURRENT.md",
    *RUNTIME_SKILLS,
    *RUNTIME_REFERENCES,
]

CURATION_CASE_DIR = ROOT / "docs" / "curation-cases"

errors: list[str] = []
versions: set[str] = set()


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


for path in CURRENT_REQUIRED:
    check(path.is_file(), f"missing current required file: {path.relative_to(ROOT)}")

for skill_dir in RUNTIME_SKILL_DIRS:
    skill = skill_dir / "SKILL.md"
    if not skill.is_file():
        continue

    text = skill.read_text(encoding="utf-8")
    name_match = re.search(r"(?m)^name:\s*([^\n]+)$", text)
    version_match = re.search(r'(?m)^\s*version:\s*"?([^"\n]+)"?\s*$', text)
    check(bool(name_match), f"{skill.relative_to(ROOT)} missing frontmatter name")
    check(bool(version_match), f"{skill.relative_to(ROOT)} missing metadata.version")

    if name_match:
        skill_name = name_match.group(1).strip().strip("\"'")
        check(
            skill_name == skill_dir.name,
            f"skill name {skill_name!r} != directory {skill_dir.name!r}",
        )

    if version_match:
        versions.add(version_match.group(1).strip())

    referenced = set(re.findall(r"\(references/([^\)]+\.md)\)", text))
    for ref in referenced:
        check(
            (skill_dir / "references" / ref).is_file(),
            f"{skill.relative_to(ROOT)} references missing file: references/{ref}",
        )

check(len(versions) == 1, f"runtime Skill versions must match, found: {sorted(versions)}")
version = next(iter(versions), "")

if CURATION_CASE_DIR.is_dir():
    for case in sorted(CURATION_CASE_DIR.glob("CASE_*.md")):
        body = case.read_text(encoding="utf-8")
        check(
            "NOT USER-USE EVIDENCE" in body,
            f"curation case lacks explicit evidence boundary: {case.relative_to(ROOT)}",
        )

map_path = ROOT / "docs" / "PROJECT_MAP.md"
if map_path.is_file():
    map_text = map_path.read_text(encoding="utf-8")
    links = re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", map_text)
    for raw in links:
        if "://" in raw:
            continue
        target = (map_path.parent / raw).resolve()
        check(target.is_file(), f"broken local Markdown link in PROJECT_MAP.md: {raw}")

readme = ROOT / "README.md"
if readme.is_file():
    readme_text = readme.read_text(encoding="utf-8")
    check(
        "CONTROLLED USER TRIAL" in readme_text.upper(),
        "README missing controlled-user-trial release boundary",
    )
    check(
        "curating-erp-ai-resources" in readme_text,
        "README missing Practice Curator entry",
    )
    check(
        "advising-erp-ai-capabilities" in readme_text,
        "README missing Capability Advisor entry",
    )

if errors:
    print("PROJECT CONTRACT: FAIL")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print("PROJECT CONTRACT: PASS")
print(f"- runtime version (from Skill metadata): {version or 'unknown'}")
print(f"- current required files: {len(CURRENT_REQUIRED)}")
print(f"- runtime skills: {len(RUNTIME_SKILLS)}")
print(f"- runtime references: {len(RUNTIME_REFERENCES)}")
print("- Project Map local Markdown links: valid")
print("- existing curation cases: explicit NOT USER-USE EVIDENCE boundary")
