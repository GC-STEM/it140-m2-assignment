"""Validate the Module Two repository structure and assignment artifacts."""

from __future__ import annotations

import argparse
import json
import re
import struct
import subprocess
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parents[2]

EDITABLE_PATHS = {
    "Part-A/name_age_sdw.md",
    "Part-A/src/name_age.py",
    "Part-B/ide_features.md",
}

REQUIRED_FILES = (
    ".gitattributes",
    ".gitignore",
    "README.md",
    "pyproject.toml",
    ".github/ISSUE_TEMPLATE/report-a-problem.yml",
    ".github/ISSUE_TEMPLATE/request-an-improvement.yml",
    ".github/ci/check_repository.py",
    ".github/ci/check_starter.py",
    ".github/social-preview.png",
    ".github/workflows/tests.yml",
    ".vscode/settings.json",
    "Part-A/README.md",
    "Part-A/name_age_sdw.md",
    "Part-A/analysis/README.md",
    "Part-A/analysis/name_age_srs.md",
    "Part-A/design/README.md",
    "Part-A/design/name_age.drawio",
    "Part-A/design/name_age.pseudo",
    "Part-A/design/name_age_sdd.md",
    "Part-A/src/README.md",
    "Part-A/src/name_age.py",
    "Part-A/tests/README.md",
    "Part-A/tests/test_name_age.py",
    "Part-B/README.md",
    "Part-B/ide_features.md",
)

PROVIDED_MARKDOWN = (
    "README.md",
    "Part-A/README.md",
    "Part-A/analysis/README.md",
    "Part-A/analysis/name_age_srs.md",
    "Part-A/design/README.md",
    "Part-A/design/name_age_sdd.md",
    "Part-A/src/README.md",
    "Part-A/tests/README.md",
    "Part-B/README.md",
)

STARTER_MARKDOWN = (
    "Part-A/name_age_sdw.md",
    "Part-B/ide_features.md",
)

# These markers intentionally focus on stable document structure rather than
# prose so routine wording edits do not require CI maintenance.
REQUIRED_TEXT_MARKERS = {
    "README.md": (
        "# IT 140 Module Two Assignment",
        "## 0. Meet the Prerequisites",
        "## 1. Setup the Assignment",
        "## 2. Complete Part A",
        "## 3. Complete Part B",
        "## 4. Submit Your Assignment",
        "## Get Help and Support",
    ),
    "Part-A/README.md": (
        "# Part A | Name and Age Program",
        "## Deliverables",
        "## Start Part A",
        "## Help and Support",
    ),
    "Part-A/analysis/README.md": (
        "# Analyze Phase",
        "## Purpose",
        "## Deliverable",
        "## Check Your Work",
        "## Help and Support",
    ),
    "Part-A/analysis/name_age_srs.md": (
        "# Software Requirements Specification",
        "## 1. Functional Requirements",
        "## 2. Nonfunctional Requirements",
        "## 3. Technology Constraints",
        "## 4. Quality of Service Constraints",
        "## Acceptance Test Cases",
    ),
    "Part-A/design/name_age_sdd.md": (
        "# Software Design Document",
        "## 2. Solution Overview",
        "## 6. Program Logic and Control Flow",
        "## 9. Requirements Traceability",
    ),
    "Part-A/name_age_sdw.md": (
        "# Software Development Worksheet (SDW)",
        "## How to Use This Worksheet",
        "## Analyze Phase",
        "## Design Phase",
        "### 11. Ready to Construct",
    ),
    "Part-A/src/README.md": (
        "# Construct Phase",
        "### Edit Only TODO Lines",
        "## Deliverable",
        "### 6. Recognize the Main Function",
    ),
    "Part-A/tests/README.md": (
        "# Test Phase",
        "## Purpose",
        "## Deliverable",
    ),
    "Part-B/README.md": (
        "# Part B | IDE Features Reflection",
        "## Deliverable",
        "## Help and Support",
    ),
}

REFLECTION_PLACEHOLDERS = (
    "TODO: Replace with your introduction text here.",
    "TODO: Replace with name of your Feature1",
    "TODO: Replace with your feature 1 text here.",
    "TODO: Replace with name of your Feature2",
    "TODO: Replace with your feature 2 text here.",
    "TODO: Replace with name of your Feature3",
    "TODO: Replace with your feature 3 text here.",
    "TODO: Replace with your conclusion text here.",
    (
        "TODO: Replace with your source citations here in APA style, if any. "
        "Delete section heading and this text if not used."
    ),
)

PROTECTED_SOURCE_MARKERS = (
    "from datetime import date",
    (
        "CURRENT_YEAR = date.today().year  "
        "# Get current year from system as integer"
    ),
    "def main() -> None:",
    '    """Run the name-age program."""',
    'if __name__ == "__main__":',
    "    main()",
)

SOURCE_DOCUMENTATION_MARKERS = (
    "Input:",
    "Process:",
    "Output:",
    "Typical usage example:",
)

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class Checks:
    """Collect check failures and print a single useful report."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.notes: list[str] = []

    def error(self, message: str) -> None:
        """Record a failing check."""
        self.errors.append(message)

    def note(self, message: str) -> None:
        """Record a successful or informational check."""
        self.notes.append(message)

    def finish(self) -> None:
        """Print results and exit nonzero if any checks failed."""
        for note in self.notes:
            print(f"PASS: {note}")

        if not self.errors:
            print("PASS: Repository and artifact checks completed.")
            return

        print("\nRepository checks failed:", file=sys.stderr)
        for error in self.errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def read_text(relative_path: str) -> str:
    """Read a repository text file as UTF-8."""
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def check_required_files(checks: Checks) -> None:
    """Verify required repository files exist and are not empty."""
    missing_or_empty = 0
    for relative_path in REQUIRED_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            checks.error(f"Required file is missing: {relative_path}")
            missing_or_empty += 1
            continue
        if path.stat().st_size == 0:
            checks.error(f"Required file is empty: {relative_path}")
            missing_or_empty += 1

    if missing_or_empty == 0:
        checks.note("Required repository files are present and nonempty.")


def check_json_and_toml(checks: Checks) -> None:
    """Parse the repository JSON and TOML configuration files."""
    settings_path = REPO_ROOT / ".vscode/settings.json"
    pyproject_path = REPO_ROOT / "pyproject.toml"

    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
        if not isinstance(settings, dict):
            checks.error(".vscode/settings.json must contain a JSON object.")
    except (OSError, json.JSONDecodeError) as exc:
        checks.error(f"Invalid .vscode/settings.json: {exc}")

    try:
        with pyproject_path.open("rb") as file_handle:
            pyproject = tomllib.load(file_handle)
        lint = pyproject.get("tool", {}).get("ruff", {}).get("lint", {})
        selected = set(lint.get("select", []))
        if not {"E", "F"}.issubset(selected):
            checks.error(
                "pyproject.toml must keep Ruff E and F checks enabled."
            )
    except (OSError, tomllib.TOMLDecodeError) as exc:
        checks.error(f"Invalid pyproject.toml: {exc}")


def check_required_text_markers(checks: Checks) -> None:
    """Verify major non-code documents keep their expected structure."""
    missing = 0
    for relative_path, markers in REQUIRED_TEXT_MARKERS.items():
        text = read_text(relative_path)
        for marker in markers:
            if marker not in text:
                checks.error(
                    f"Required section is missing from {relative_path}: "
                    f"{marker}"
                )
                missing += 1

    if missing == 0:
        checks.note("Major Markdown artifacts keep their expected sections.")


def check_drawio(checks: Checks) -> None:
    """Verify the provided Draw.io artifact is parseable XML."""
    path = REPO_ROOT / "Part-A/design/name_age.drawio"
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        relative_path = path.relative_to(REPO_ROOT)
        checks.error(f"Invalid Draw.io XML in {relative_path}: {exc}")
        return

    tag = root.tag.rsplit("}", maxsplit=1)[-1]
    if tag != "mxfile":
        checks.error("Part-A/design/name_age.drawio must have an mxfile root.")
        return

    diagrams = [
        node
        for node in root.iter()
        if node.tag.rsplit("}", maxsplit=1)[-1] == "diagram"
    ]
    if not diagrams:
        checks.error("Part-A/design/name_age.drawio contains no diagram.")
    else:
        checks.note("The Draw.io design file is parseable XML.")


def check_pseudocode(checks: Checks) -> None:
    """Verify the supplied pseudocode has its expected boundaries."""
    text = read_text("Part-A/design/name_age.pseudo")
    start = text.find("START name_age")
    end = text.find("END name_age")

    if start < 0:
        checks.error("Pseudocode is missing 'START name_age'.")
    if end < 0:
        checks.error("Pseudocode is missing 'END name_age'.")
    if start >= 0 and end >= 0 and start >= end:
        checks.error("Pseudocode START must appear before END.")
    if start >= 0 and end > start:
        checks.note("The pseudocode has the expected START/END structure.")


def without_code_fences(text: str) -> str:
    """Remove fenced code blocks before scanning Markdown links."""
    output: list[str] = []
    in_fence = False
    fence_marker = ""

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if not in_fence:
            output.append(line)

    return "\n".join(output)


def local_link_target(raw_target: str) -> str | None:
    """Return a local Markdown link path or None for external links."""
    target = raw_target.strip()
    if not target:
        return None

    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]

    if target.startswith("#"):
        return None

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None

    path = unquote(parsed.path)
    if not path or path.startswith("/"):
        return None
    return path


def check_markdown_links(checks: Checks) -> None:
    """Verify local links in supplied repository Markdown files."""
    markdown_files = list(PROVIDED_MARKDOWN)
    markdown_files.extend(STARTER_MARKDOWN)

    broken = 0
    repo_root = REPO_ROOT.resolve()

    for relative_path in markdown_files:
        file_path = REPO_ROOT / relative_path
        text = without_code_fences(file_path.read_text(encoding="utf-8"))

        for match in MARKDOWN_LINK.finditer(text):
            target = local_link_target(match.group(1))
            if target is None:
                continue

            resolved = (file_path.parent / target).resolve()
            try:
                resolved.relative_to(repo_root)
            except ValueError:
                checks.error(
                    f"Local link leaves the repository in {relative_path}: "
                    f"{target}"
                )
                broken += 1
                continue

            if not resolved.exists():
                checks.error(
                    f"Broken local link in {relative_path}: {target}"
                )
                broken += 1

    if broken == 0:
        checks.note("Local links in provided Markdown files resolve.")


def check_social_preview(checks: Checks) -> None:
    """Check the repository social-preview PNG signature, size, and ratio."""
    path = REPO_ROOT / ".github/social-preview.png"
    data = path.read_bytes()

    if len(data) > 1_048_576:
        checks.error(".github/social-preview.png must remain under 1 MiB.")
        return

    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        checks.error(".github/social-preview.png is not a valid PNG file.")
        return

    width, height = struct.unpack(">II", data[16:24])
    if width < 640 or height < 320:
        checks.error(
            "Social preview dimensions are unexpectedly small: "
            f"{width}x{height}."
        )
        return

    ratio = width / height
    if not 1.9 <= ratio <= 2.1:
        checks.error(
            "Social preview should remain approximately 2:1; "
            f"found {width}x{height}."
        )
        return

    checks.note(
        f"Social preview is valid ({width}x{height}, {len(data)} bytes)."
    )


def check_reflection_structure(checks: Checks, mode: str) -> None:
    """Validate the Part B reflection template or student completion."""
    text = read_text("Part-B/ide_features.md")
    required = (
        "## Introduction",
        "## Feature 1",
        "## Feature 2",
        "## Feature 3",
        "## Conclusion",
    )

    for heading in required:
        if not any(line.startswith(heading) for line in text.splitlines()):
            checks.error(
                f"Part-B/ide_features.md is missing section: {heading}"
            )

    if mode == "starter":
        missing = [
            item for item in REFLECTION_PLACEHOLDERS if item not in text
        ]
        for item in missing:
            checks.error(
                "Part B starter content changed unexpectedly; missing: "
                f"{item!r}"
            )
        if not missing:
            checks.note("The Part B starter placeholders are intact.")
        return

    remaining = [
        item for item in REFLECTION_PLACEHOLDERS if item in text
    ]
    for item in remaining:
        checks.error(
            "Part B still contains starter text that must be replaced: "
            f"{item!r}"
        )
    if not remaining:
        checks.note("The Part B starter placeholders have been replaced.")


def git_output(*args: str) -> str:
    """Run Git and return stripped standard output."""
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(message or "Git command failed.")
    return result.stdout.strip()


def check_student_change_scope(checks: Checks) -> None:
    """Ensure students changed only files the assignment allows."""
    try:
        roots = git_output("rev-list", "--max-parents=0", "HEAD").splitlines()
    except RuntimeError as exc:
        checks.error(f"Could not inspect repository history: {exc}")
        return

    if len(roots) != 1:
        checks.error(
            "Could not identify one initial template commit for this "
            "personal repository."
        )
        return

    try:
        changed_text = git_output(
            "diff",
            "--name-only",
            "--diff-filter=ACDMRTUXB",
            roots[0],
            "HEAD",
        )
    except RuntimeError as exc:
        checks.error(f"Could not compare with the template commit: {exc}")
        return

    changed = {line for line in changed_text.splitlines() if line}
    unexpected = sorted(changed - EDITABLE_PATHS)

    for path in unexpected:
        checks.error(
            "Provided repository file was added, removed, renamed, or "
            f"changed: {path}"
        )

    if not unexpected:
        checks.note(
            "Committed changes are limited to the three student working files."
        )


def check_student_source(checks: Checks) -> None:
    """Check completion while preserving the provided source scaffold."""
    text = read_text("Part-A/src/name_age.py")

    marker = "TODO: Replace"
    if marker in text:
        checks.error(
            "Part-A/src/name_age.py still contains starter 'TODO: Replace' "
            "text."
        )
    else:
        checks.note("The Part A starter TODO prompts have been replaced.")

    missing_scaffold = [
        item for item in PROTECTED_SOURCE_MARKERS if item not in text
    ]
    for item in missing_scaffold:
        checks.error(
            "Part-A/src/name_age.py changed provided program structure; "
            f"missing: {item!r}"
        )
    if not missing_scaffold:
        checks.note("The provided Part A Python scaffold remains intact.")

    missing_documentation = [
        item for item in SOURCE_DOCUMENTATION_MARKERS if item not in text
    ]
    for item in missing_documentation:
        checks.error(
            "Part-A/src/name_age.py is missing a required module-docstring "
            f"section: {item!r}"
        )
    if not missing_documentation:
        checks.note("The Part A module-docstring sections remain intact.")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        required=True,
        choices=("starter", "student"),
        help="Validate the course starter or a personal student repository.",
    )
    return parser.parse_args()


def main() -> None:
    """Run repository and artifact checks."""
    args = parse_args()
    checks = Checks()

    check_required_files(checks)
    if checks.errors:
        checks.finish()

    check_json_and_toml(checks)
    check_required_text_markers(checks)
    check_drawio(checks)
    check_pseudocode(checks)
    check_markdown_links(checks)
    check_social_preview(checks)
    check_reflection_structure(checks, args.mode)

    if args.mode == "student":
        check_student_change_scope(checks)
        check_student_source(checks)

    checks.finish()


if __name__ == "__main__":
    main()
