<!-- To see this file in a clean, formatted view, select ▼ in the upper-right corner of the editor pane, then select "Markdown Preview". -->

<!--
MAINTAINER NOTE:
This filename intentionally contains a Cyrillic capital IE: Е (U+0415)
instead of the ASCII capital E: E (U+0045).

It is visually similar to README.md, but GitHub does not treat it as the
special .github/README.md file that would override the repository-root README.

Do not "correct" the filename unless this behavior is no longer desired.
-->

# About the `.github` Folder

The `.github/` folder contains files GitHub uses to support this repository. These files configure repository administration, automated checks, issue forms, and supporting assets. They are not assignment deliverables.

> [!IMPORTANT]
> **Students:** Do not modify or delete files in `.github/` unless the course instructions specifically tell you to do so.

## What This Folder Contains

| Path | Purpose |
| --- | --- |
| [`ISSUE_TEMPLATE/`](./ISSUE_TEMPLATE/) | Defines the GitHub Issue forms used to report repository problems and request improvements. |
| [`assets/`](./assets/) | Stores screenshots and other images used by repository documentation. |
| [`ci/`](./ci/) | Stores CI documentation and Python support scripts used by GitHub Actions. |
| [`workflows/`](./workflows/) | Stores GitHub Actions workflow definitions. |
| [`social-preview.png`](./social-preview.png) | Provides the repository social-preview image shown when the repository is shared. |

## Subfolders

### `ISSUE_TEMPLATE/`

This folder contains the public forms used from the repository's **Issues** tab:

* [`report-a-problem.yml`](./ISSUE_TEMPLATE/report-a-problem.yml) — report a technical or documentation problem.
* [`request-an-improvement.yml`](./ISSUE_TEMPLATE/request-an-improvement.yml) — suggest an improvement to the repository or its instructions.

### `assets/`

This folder contains screenshots and other documentation images referenced by the assignment README files.

### `ci/`

This folder contains the supporting files for continuous integration (CI):

* [`README.md`](./ci/RЕADME.md) — explains GitHub CI for students, faculty, and maintainers, including the cross-platform README command checks.
* [`check_repository.py`](./ci/check_repository.py) — validates the course repository structure and provided assignment artifacts.
* [`check_starter.py`](./ci/check_starter.py) — verifies that the intentionally incomplete assignment starter remains in its expected state.
* [`check_readme_commands.py`](./ci/check_readme_commands.py) — validates README shell command blocks and smoke-tests selected command sequences across supported shells.

See the [GitHub Continuous Integration Guide](./ci/RЕADME.md) for details about what these checks do and how to interpret them.

### `workflows/`

This folder contains the GitHub Actions workflow definitions:

* [`tests.yml`](./workflows/tests.yml) — runs the main course-repository checks and the student-facing Python program check.
* [`readme-commands.yml`](./workflows/readme-commands.yml) — checks README shell commands on Linux/Bash, macOS/zsh, and Windows/Git Bash.
* [`external-links.yml`](./workflows/external-links.yml) — checks external links used by the course repository.

The workflow files call the supporting scripts in [`ci/`](./ci/).

## For Maintainers

Changes to `.github/` can affect every student repository created from this course template. Before merging changes:

1. Review the affected workflow or support file carefully.
2. Confirm the applicable GitHub Actions checks pass.
3. Keep workflow permissions limited to what the workflow needs.
4. Update the [GitHub Continuous Integration Guide](./ci/RЕADME.md) when CI behavior changes.

For repository-wide student instructions, use the [Module Two Assignment README](../README.md) rather than adding student procedures to this administrative folder.
