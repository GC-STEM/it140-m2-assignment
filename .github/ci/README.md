<!-- To see this file in a clean, formatted view, select ▼ in the upper-right corner of the editor pane, then select "Markdown Preview". -->

# IT 140 Module Two Assignment | GitHub Continuous Integration Guide

This guide explains how **continuous integration (CI)** works in the IT 140 Module Two Assignment repository.

It is written for:

* **Students** who want to understand the feedback GitHub provides.
* **Faculty** who help students interpret that feedback.
* **Maintainers** who update the course repository and its CI files.

> [!IMPORTANT]
> **GitHub CI provides feedback. It does not grade or submit the assignment.**
>
> Students submit the required assignment files in **D2L Brightspace**. The assignment rubric in D2L Brightspace determines the grade.

<!-- omit from toc -->
## Table of Contents

* [About CI](#about-ci)
  * [1. What Is CI?](#1-what-is-ci)
  * [2. Terms Used in This Guide](#2-terms-used-in-this-guide)
  * [3. Why We Use CI in This Assignment](#3-why-we-use-ci-in-this-assignment)
* [Student CI](#student-ci)
  * [4. What the Python Program Check Does](#4-what-the-python-program-check-does)
  * [5. When the Python Program Check Runs](#5-when-the-python-program-check-runs)
  * [6. Understanding the Python Program Check](#6-understanding-the-python-program-check)
  * [7. How Students Should Use CI Feedback](#7-how-students-should-use-ci-feedback)
  * [8. How to View CI Feedback on GitHub](#8-how-to-view-ci-feedback-on-github)
* [When Something Fails](#when-something-fails)
  * [9. A Failed Acceptance Test Is Usually Normal Development Feedback](#9-a-failed-acceptance-test-is-usually-normal-development-feedback)
  * [10. Do Not Change the Acceptance Tests to Make Them Pass](#10-do-not-change-the-acceptance-tests-to-make-them-pass)
  * [11. When a CI Result May Be a Cause for Concern](#11-when-a-ci-result-may-be-a-cause-for-concern)
* [Faculty Guidance](#faculty-guidance)
  * [12. How Faculty Can Use Student CI Feedback](#12-how-faculty-can-use-student-ci-feedback)
  * [13. Using CI for Faculty Troubleshooting](#13-using-ci-for-faculty-troubleshooting)
* [Course Repository CI](#course-repository-ci)
  * [14. Course Repository Check](#14-course-repository-check)
  * [15. README Command Checks](#15-readme-command-checks)
  * [16. External Link Checks](#16-external-link-checks)
  * [17. Why Course and Student CI Are Different](#17-why-course-and-student-ci-are-different)
* [Maintainer Guidance](#maintainer-guidance)
  * [18. When a Course Repository Check Fails](#18-when-a-course-repository-check-fails)
  * [19. When a README Command Check Fails](#19-when-a-readme-command-check-fails)
  * [20. When to Re-run a Workflow](#20-when-to-re-run-a-workflow)
  * [21. CI Design Notes for Maintainers](#21-ci-design-notes-for-maintainers)
  * [22. CI Is One Part of the Learning Process](#22-ci-is-one-part-of-the-learning-process)
* [Summary](#summary)
  * [23. Key Points](#23-key-points)

## About CI

### 1. What Is CI?

**CI** stands for **continuous integration**.

CI uses software to check changes after they are saved to GitHub. In this repository, **GitHub Actions** provides CI.

For example, after a student saves Python changes to a personal GitHub repository, GitHub Actions can:

1. Check whether the Python program has a syntax error.
2. Run the provided acceptance tests.
3. Provide Code style feedback.

The course repository also uses CI to protect the assignment template itself, including repository files, documentation links, starter artifacts, README shell commands, and external links.

### 2. Terms Used in This Guide

| Term | Meaning |
| --- | --- |
| **course repository** | The `GC-STEM/it140-m2-assignment` repository that provides the assignment starter files. |
| **personal repository** | The private GitHub repository a student creates from the course repository template. |
| **workflow** | Instructions in `.github/workflows/` that tell GitHub Actions what to do. |
| **workflow run** | One execution of a workflow. |
| **job** | A group of related steps in a workflow run. |
| **step** | One task within a job. |
| **Python program check** | The student-facing job that checks `name_age.py`. |
| **Python syntax check** | Checks whether Python can read the structure of `name_age.py`. |
| **acceptance tests** | Tests that verify `name_age.py` meets the provided acceptance test cases documented in the SRS and referenced by the SDD. |
| **Code style feedback** | Ruff feedback about basic Python code style and possible code problems. |
| **Course repository check** | The maintainer job that validates the course assignment package and starter files. |
| **README command checks** | Course-repository checks that validate README shell commands on Linux/Bash, macOS/zsh, and Windows/Git Bash. |
| **smoke test** | A lightweight execution check used to confirm that a documented command sequence behaves as intended in a disposable test environment. |

### 3. Why We Use CI in This Assignment

The CI design follows these rules:

1. **KISS — Keep It Super Simple.**
2. Student feedback should focus on the Python program.
3. A problem in a Markdown assignment file should not cause the student Python program check to fail.
4. Feedback should tell students what happened and what to do next.
5. Students should be able to improve their program and try again.
6. Code style feedback should help students learn without controlling the Python program check result.
7. Course-repository CI should catch template and documentation problems before they affect students.
8. CI supports learning and maintenance; it does not replace instructor feedback or the assignment rubric.

## Student CI

### 4. What the Python Program Check Does

The **Python program check** is used in a student's personal repository. It checks only:

`Part-A/src/name_age.py`

It does **not** check:

* `Part-A/name_age_sdw.md`
* `Part-B/ide_features.md`

The Python program check has three parts:

| Part | What it does | Can it make the result fail? |
| --- | --- | :---: |
| **Python syntax check** | Checks whether Python can read the program. | Yes |
| **Acceptance tests** | Runs the five provided acceptance test cases. | Yes |
| **Code style feedback** | Uses Ruff to provide basic code style feedback. | No |

Under normal operation, the Python program check turns red only when the Python syntax check or acceptance tests fail. GitHub Actions or setup problems can also cause a workflow run to fail; see [When a CI Result May Be a Cause for Concern](#11-when-a-ci-result-may-be-a-cause-for-concern).

### 5. When the Python Program Check Runs

The Python program check runs after a student pushes work to a personal repository.

#### If `name_age.py` Changed

GitHub runs:

1. **Python syntax check**
2. **Acceptance tests**, if the syntax check passes
3. **Code style feedback**, if the syntax check passes

#### If `name_age.py` Did Not Change

GitHub reports:

> **No Python program check was needed.**

For example, changes only to the SDW, IDE Features Reflection, or another Markdown file do not need a Python program check.

#### When a Personal Repository Is First Created

The original starter version of `name_age.py` is intentionally incomplete. GitHub does **not** treat that untouched starter program as a student programming error.

Students should not receive a failed Python program check simply because they created their personal repository.

### 6. Understanding the Python Program Check

#### ✅ Python Syntax Check: Passed

Python was able to read the structure of `name_age.py`. The acceptance tests check program behavior next.

#### ❌ Python Syntax Check: Failed

Python found a syntax error. The workflow summary identifies the location when Python can determine it, for example:

```text
Line: 35
Column: 18
Problem: expected ':'
```

Start with the line shown in the feedback. Fix the syntax error, run the program again, and then save the corrected program to GitHub. The acceptance tests cannot run until the syntax check passes.

#### ✅ Acceptance Tests: Passed

The program passed all five provided acceptance test cases.

> [!IMPORTANT]
> **Passing all acceptance tests does not mean the assignment is complete or that it will receive full credit.**

Students must still follow the assignment directions, complete all required work, review the rubric, and submit the required files in D2L Brightspace.

#### ❌ Acceptance Tests: Failed

One or more acceptance test cases did not pass. This is normal feedback during development.

Use the feedback to identify which test failed, what the test was checking, and what part of the program may need to change. Fix one problem at a time, retest locally, save the corrected program to GitHub, and review the new workflow run.

#### ✅ Code Style Feedback: Ruff Found No Suggestions

Ruff did not find a problem covered by the code style rules used for this assignment. No action is needed.

#### ℹ️ Code Style Feedback: Ruff Found Suggestions

Review the suggestions and use them to improve your Python code.

> **Code style feedback does not change the Python program check result.**

Code quality may still be part of the assignment rubric.

#### ℹ️ Code Style Feedback: Ruff Was Not Available

GitHub could not run Ruff. This does **not** mean the student's program is wrong and does not change the Python program check result.

### 7. How Students Should Use CI Feedback

A recommended workflow is:

1. **Write** a small part of the program.
2. **Run** the program in VS Code.
3. **Test** the program using the [Test Phase guide](../../Part-A/tests/README.md).
4. **Fix** problems you find.
5. **Save** your work to your personal GitHub repository.
6. **Review** the Python program check.
7. **Improve** the program if needed.

> **Write → Run → Test → Save to GitHub → Review Feedback → Improve**

### 8. How to View CI Feedback on GitHub

In a personal repository:

1. Select the **Actions** tab.
2. Select the most recent **IT 140 Checks** workflow run.
3. Open **Python program check**.
4. Read the workflow summary first.

If more information is needed, open the applicable step:

* **Python syntax check**
* **Acceptance tests**
* **Code style feedback**

Focus on the first problem that needs to be fixed.

## When Something Fails

### 9. A Failed Acceptance Test Is Usually Normal Development Feedback

Programming includes finding and fixing errors. During development, it is normal for the syntax check or one or more acceptance tests to fail.

A failed Python program check is **feedback about the current version of the program**, not a grade.

When the check fails:

1. Read the workflow summary.
2. Identify whether the problem is syntax or program behavior.
3. Fix one problem at a time.
4. Run the program locally.
5. Run the acceptance tests locally.
6. Save the corrected program to GitHub.
7. Review the new workflow run.

Do not repeatedly re-run the same failed workflow after changing code only on your computer. An existing workflow run checks the version already saved to GitHub.

### 10. Do Not Change the Acceptance Tests to Make Them Pass

Students should change:

`Part-A/src/name_age.py`

to make the acceptance tests pass.

Students should **not** change:

`Part-A/tests/test_name_age.py`

to make an incorrect program appear correct.

The student workflow restores the original provided acceptance tests from the personal repository's starter history before checking the program.

### 11. When a CI Result May Be a Cause for Concern

Students should report a possible repository or CI problem when, for example:

* a brand-new personal repository reports a Python program failure before `name_age.py` is edited;
* changing only the SDW or IDE Features Reflection causes the Python program check to fail;
* a GitHub setup step fails before the Python syntax check begins;
* GitHub reports that the Python program check could not finish; or
* the workflow feedback clearly does not match the current `name_age.py` stored on GitHub.

Before reporting a problem, confirm that the expected `name_age.py` version is saved in the personal GitHub repository.

> [!WARNING]
> The course repository's GitHub Issues and Discussions are public. Do **not** post assignment code, credentials, access tokens, or private identifying information.

Use the help options in the [Module Two Assignment README](../../README.md) for additional support.

## Faculty Guidance

### 12. How Faculty Can Use Student CI Feedback

CI is **formative feedback**. It helps identify the type of problem while the student is developing the program. It is not a replacement for grading.

* **Python syntax check failed:** Help the student interpret Python's line, column, and problem message and correct the syntax.
* **Acceptance tests failed:** Help the student connect the failed test to the SRS, provided design, expected input, and expected output.
* **Code style feedback has suggestions:** Treat Ruff as advisory feedback; the rubric remains the authority for grading code quality.
* **Python program check passed:** Remember that the result covers only `name_age.py`, not the complete assignment or rubric.

### 13. Using CI for Faculty Troubleshooting

| Result | Most likely area to investigate |
| --- | --- |
| Python syntax check failed | Python syntax |
| Acceptance tests failed | Program behavior |
| Code style feedback has suggestions | Python code style |
| No Python program check was needed | `name_age.py` did not change in that push |
| GitHub setup step failed | GitHub Actions or repository problem |
| Python program check could not finish | GitHub Actions or repository problem |

If several students report the same GitHub setup failure, consider a course-repository or GitHub Actions problem before assuming the students made the same programming mistake.

## Course Repository CI

### 14. Course Repository Check

The **Course repository check** protects the assignment starter and support files in `GC-STEM/it140-m2-assignment`.

It validates areas such as:

* required repository files;
* provided Markdown structure and local links;
* the Draw.io and pseudocode artifacts;
* repository JSON and TOML configuration;
* the social preview image;
* Python syntax and code style;
* the provided acceptance tests; and
* the intentionally incomplete assignment starter.

Supporting files include:

* [`tests.yml`](../workflows/tests.yml) — main GitHub Actions workflow.
* [`check_repository.py`](./check_repository.py) — repository and artifact checks.
* [`check_starter.py`](./check_starter.py) — starter-state checks.
* [`test_name_age.py`](../../Part-A/tests/test_name_age.py) — five provided acceptance tests.

### 15. README Command Checks

The [`readme-commands.yml`](../workflows/readme-commands.yml) workflow protects executable shell instructions in README files. It runs only in the **course repository**, not in personal student repositories.

The workflow uses three hosted environments:

| Environment | Shell being checked |
| --- | --- |
| Linux | Bash |
| macOS | zsh |
| Windows | Git Bash from Git for Windows |

[`check_readme_commands.py`](./check_readme_commands.py) performs two levels of checking.

#### Static Checks for README Shell Blocks

Every fenced `bash`, `sh`, or `shell` block in README-style documentation is checked for shell syntax on each platform. The checker also rejects patterns that conflict with the course's cross-platform command conventions, including:

* Command Prompt `%USERPROFILE%` syntax in Bash blocks;
* PowerShell `$env:` syntax in Bash blocks;
* Windows drive paths in cross-platform Bash blocks;
* backslashes used with `~` or `$HOME`; and
* opening a `~/Repos/...` path directly with `code` instead of using `cd ...` followed by `code .`.

The checker scans files named `README.md` plus the intentionally named [`.github/RЕADME.md`](../README.md).

#### Smoke Tests for Selected Command Sequences

Procedural command blocks that are safe to exercise are marked with an invisible Markdown comment immediately before the block:

```text
<!-- ci:command-test id=open-part-a fixture=existing-repo expect=repo -->
```

The marker contains:

* `id` — a unique test name shown in CI output;
* `fixture` — the starting disposable environment;
* `expect` — the expected working directory after the sequence finishes.

Supported fixtures are:

* `empty-repos` — creates only `~/Repos`;
* `existing-repo` — creates a simulated `~/Repos/it140-m2-assignment` clone with the directories needed by the documented commands.

Supported expectations are:

* `repos` — finish in `~/Repos`;
* `repo` — finish in `~/Repos/it140-m2-assignment`;
* `part-a` — finish in `~/Repos/it140-m2-assignment/Part-A`.

The smoke tests replace commands that would cause external effects with harmless shims. Current shims cover `gh`, `git`, `code`, and `python3`. This allows CI to verify items such as:

* `~` expansion;
* `cd` behavior and relative paths;
* command ordering;
* creation or use of the expected repository directory;
* the course convention `code .`; and
* references to documented files such as `tests/test_name_age.py`.

The smoke tests do **not** create or modify GitHub repositories, push commits, launch VS Code, authenticate to GitHub, or run a student's assignment program.

> [!NOTE]
> A README command smoke test confirms the documented shell sequence in the disposable test environment. It does not replace testing the actual GitHub CLI, Git service, VS Code application, network, or student program behavior.

#### Which README Blocks Are Marked

The current smoke tests cover the student command sequences for:

* creating the personal assignment repository;
* opening Part A and Part B in VS Code;
* opening an existing local clone;
* cloning an existing personal repository;
* inspecting a local remote;
* saving work before switching devices;
* synchronizing a second device; and
* running the optional local acceptance tests.

The hidden `ci:command-test` comments do not appear in rendered Markdown.

### 16. External Link Checks

[`external-links.yml`](../workflows/external-links.yml) checks external links used by the course repository. It is a course-maintenance workflow and is separate from the student Python program check.

A failed external-link check can indicate a moved page, temporary remote-site problem, authentication requirement, rate limit, or another link-specific issue. Maintainers should verify the destination before changing course documentation.

### 17. Why Course and Student CI Are Different

The course repository provides the assignment, so its CI protects the **entire assignment package**. A broken README, test, workflow, artifact, or configuration file could affect many students.

A personal repository is where a student develops the assignment, so its CI focuses narrowly on the **Python program**. This keeps student feedback useful and avoids turning unrelated Markdown work into a programming failure.

## Maintainer Guidance

### 18. When a Course Repository Check Fails

Before merging or releasing a course-repository change:

1. Open the failed workflow run.
2. Read the workflow summary.
3. Find the first failed step.
4. Read the failure message.
5. Correct the underlying problem.
6. Commit and push the correction.
7. Confirm the new check passes.

A failed Course repository check is a cause for concern because it can indicate a problem in the shared assignment template.

### 19. When a README Command Check Fails

A README command failure means the documentation should be reviewed before release.

#### Static Failure

Look for:

* invalid Bash/zsh syntax;
* PowerShell or Command Prompt syntax accidentally placed in a Bash block;
* a platform-specific path that violates the course's cross-platform command convention;
* backslashes used with `~` or `$HOME`; or
* a direct `code ~/Repos/...` command that should use `cd ...` and `code .`.

#### Smoke-Test Failure

Look at the test ID, platform, and command log. Determine whether:

* the documented `cd` path is incorrect;
* a required earlier command did not create the expected directory;
* `code .` is being called from the wrong working directory;
* a referenced file path is wrong; or
* the fixture/expect metadata no longer matches the documented procedure.

Do not weaken the checker merely to make a documentation error pass. Update the documentation or, when the intended procedure has genuinely changed, update the test fixture/checker with it.

#### Adding or Changing a Testable README Command Block

When a procedural Bash block should be smoke-tested:

1. Keep the command sequence compatible with Bash and zsh unless the instructions explicitly require another shell.
2. Require **Git Bash** for Windows-facing Bash instructions.
3. Add a unique `ci:command-test` marker immediately before the code fence.
4. Choose the smallest fixture that represents the documented starting state.
5. Set the expected final working directory.
6. Confirm **README Command Checks** passes on Linux, macOS, and Windows before merging.

Maintainers can run the Linux/Bash version locally from the repository root:

```bash
python .github/ci/check_readme_commands.py --shell bash --platform linux
```

On macOS, the equivalent local zsh check is:

```bash
python .github/ci/check_readme_commands.py --shell zsh --platform macos
```

### 20. When to Re-run a Workflow

Usually, fix the underlying problem and create a **new workflow run** by pushing the correction.

Re-running the same workflow is most useful when the failure appears unrelated to repository content, such as a temporary GitHub Actions service problem, package download failure, runner problem, or external-site failure.

> Re-running a workflow uses the same saved version of the repository.

If the files changed, push the new files instead of re-running the old workflow.

### 21. CI Design Notes for Maintainers

#### Separate Course and Student Purposes

The Course repository check protects the complete assignment package. The Python program check provides focused student programming feedback.

#### Keep Student Failures Actionable

A red student result should point to something the student can reasonably act on in `name_age.py`. Markdown work is kept out of the Python program check.

#### Use Workflow Summaries First

Important feedback is written to GitHub workflow summaries so routine results are readable without searching technical logs.

#### Keep Code Style Feedback Advisory

Ruff provides useful feedback, but Ruff suggestions do not cause the student Python program check to fail. The Ruff version is pinned for consistent feedback.

#### Protect the Acceptance Tests

The student workflow restores the original `test_name_age.py` from the personal repository's starter history before checking the program.

#### Test Documentation as Code

README command blocks are part of the student workflow. Selected commands are therefore smoke-tested across the supported shell environments rather than relying only on visual documentation review.

#### Use Read-Only Repository Permission

The workflows use read-only repository content permission where write access is not needed:

```yaml
permissions:
  contents: read
```

#### Protect the CI Files Themselves

[`check_repository.py`](./check_repository.py) requires the important workflow, checker, and CI-documentation files to be present and nonempty. The workflow that owns each checker executes that checker as part of CI, so a broken support script causes the applicable course-repository check to fail.

### 22. CI Is One Part of the Learning Process

Students should still learn to read requirements, design solutions, write code in small steps, run programs locally, read error messages, debug problems, test locally, review code quality, and ask for help when needed.

GitHub CI adds timely feedback. It does not replace those skills.

## Summary

### 23. Key Points

For students:

> **Write → Run → Test → Save to GitHub → Review Feedback → Improve**

For faculty:

> **Use CI to help identify the type of programming problem, not to determine the assignment grade.**

For maintainers:

> **Keep the course repository green and its documented commands cross-platform before releasing changes to students.**

And for everyone:

> **Keep It Super Simple.**
