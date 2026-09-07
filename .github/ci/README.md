<!-- To see this file in a clean, formatted view, select "Text Editor ▼" in the upper-right corner of the editor, then select "Markdown Preview". -->

# IT 140 Module Two Assignment | GitHub Continuous Integration (CI) Guide

This guide explains how **continuous integration (CI)** works in the IT 140 Module Two Assignment repository.

It is written for:

* **Students** who want to understand the feedback GitHub provides.
* **Faculty** who help students understand that feedback.
* **Maintainers** who update the course repository and its CI files.

> [!IMPORTANT]
> **GitHub CI provides feedback. It does not grade or submit the assignment.**
>
> Students submit the required assignment files in **D2L Brightspace**. The assignment rubric in D2L Brightspace determines the grade.

<!-- omit from toc -->
## Table of Contents

* [About CI](#about-ci)
* [Student CI](#student-ci)
* [When Something Fails](#when-something-fails)
* [Faculty Guidance](#faculty-guidance)
* [Course Repository CI](#course-repository-ci)
* [Maintainer Guidance](#maintainer-guidance)
* [Summary](#summary)

## About CI

### 1. What Is CI?

**CI** stands for **continuous integration**.

CI uses software to check changes after they are saved to GitHub. In this repository, **GitHub Actions** provides CI.

For example, after a student saves Python changes to their personal GitHub repository, GitHub Actions can:

1. Check whether the Python program has a syntax error.
2. Run the provided acceptance tests.
3. Provide Code style feedback.

This gives students feedback soon after they save their work to GitHub.

CI is useful during development because students can:

> **write → run → test → save to GitHub → review feedback → improve**

Students can repeat this process as they develop their program.

### 2. Terms Used in This Guide

This guide uses the following terms consistently.

| Term | Meaning |
| ---- | ------- |
| **course repository** | The `GC-STEM/it140-m2-assignment` repository that provides the assignment starter files. |
| **personal repository** | The private GitHub repository a student creates from the course repository template. |
| **acceptance tests** | Tests that a program meets functional requirements listed in the [SRS](../../Part-A/analysis/name_age_srs.md) and [SDD](../../Part-A/design/name_age_sdd.md). |
| **workflow** | Instructions that tell GitHub Actions what to do. |
| **workflow run** | One time GitHub runs a workflow. |
| **job** | A group of related steps in a workflow run. |
| **step** | One task within a job. |
| **Python program check** | The student-facing job that checks `name_age.py`. |
| **Python syntax check** | Checks whether Python can read the structure of `name_age.py`. |
| **Code style feedback** | Ruff feedback about basic Python code style and possible code problems. |
| **Course repository check** | The maintainer job that checks the course repository and its starter files. |

### 3. Why We Use CI in This Assignment

The main purpose of CI in this assignment is to provide **useful feedback while students are learning to program**.

The CI design follows these rules:

1. **KISS** – Keep It Super Simple.
2. Student feedback should focus on the Python program.
3. A problem in a Markdown file should not cause the Python program check to fail.
4. Feedback should tell students what happened and what to do next.
5. Students should be able to improve their program and try again.
6. Code style feedback should help students learn, but it should not cause the Python program check to fail.
7. CI feedback should support learning, not replace instructor feedback or the assignment rubric.

## Student CI

### 4. What the Python Program Check Does

The **Python program check** is used in a student's personal repository.

It checks only:

`Part-A/src/name_age.py`

It does **not** check:

* `Part-A/name_age_sdw.md`
* `Part-B/ide_features.md`

A problem in the SDW or IDE Features Reflection will therefore **not** cause the Python program check to fail.

#### The Python Program Check Has Three Parts

| Part | What it does | Can it make the result fail? |
| ---- | ------------ | :--------------------------: |
| **Python syntax check** | Checks whether Python can read the program. | Yes |
| **acceptance tests** | Runs the acceptance test cases. | Yes |
| **Code style feedback** | Uses Ruff to provide basic code style feedback. | No |

A red result is therefore reserved for a problem that affects the Python program.

### 5. When the Python Program Check Runs

The Python program check is designed to provide feedback after a student pushes work to their personal repository.

#### If `name_age.py` Changed

GitHub runs:

1. **Python syntax check**
2. **acceptance tests**, if the Python syntax check passes
3. **Code style feedback**, if the Python syntax check passes

#### If `name_age.py` Did Not Change

GitHub reports:

> **No Python program check was needed.**

For example, a student might save changes only to:

* the SDW;
* the IDE Features Reflection; or
* another Markdown file.

Those changes do not need a Python program check.

#### When a Personal Repository Is First Created

The original starter version of `name_age.py` is intentionally incomplete.

GitHub does **not** treat that untouched starter program as a student programming error.

Students should not receive a failed Python program check simply because they created their personal repository.

### 6. Understanding the Python Program Check

#### ✅ Python Syntax Check: Passed

Python was able to read the structure of `name_age.py`.

This does **not** mean the program produces the correct results. The acceptance tests check program behavior next.

#### ❌ Python Syntax Check: Failed

Python found a syntax error.

The workflow summary identifies the location when Python can determine it:

```text
Line: 35
Column: 18
Problem: expected ':'
```

Start with the line shown in the feedback.

Fix the syntax error, run the program again, and then save the corrected program to GitHub.

The acceptance tests cannot run until the Python syntax check passes.

#### ✅ acceptance tests: Passed

The program passed all acceptance test cases.

This is good evidence that the program produces the required results for those cases.

However:

> [!IMPORTANT]
> **Passing all acceptance tests does not mean the assignment is complete or that it will receive full credit.**

The acceptance tests do not grade every assignment requirement.

Students must still:

* follow the assignment directions;
* complete all required work;
* review the rubric; and
* submit the required files in D2L Brightspace.

#### ❌ acceptance tests: Failed

One or more of the acceptance test cases did not pass.

This is normal feedback during program development.

A failed acceptance test means the program's result did not match the expected result for that test case.

Use the feedback to identify:

1. which test did not pass;
2. what the test was checking; and
3. what part of the program may need to change.

Fix one problem at a time.

Then:

1. Run the program again.
2. Run the acceptance tests locally.
3. Save the corrected program to GitHub.
4. Review the new workflow run.

#### ✅ Code Style Feedback: Ruff Found No Suggestions

Ruff did not find a problem covered by the code style rules used for this assignment.

No action is needed.

#### ℹ️ Code Style Feedback: Ruff Found Suggestions

Ruff found one or more code style suggestions.

Review the suggestions and use them to improve your Python code.

> **Code style feedback does not change the Python program check result.**

A Ruff suggestion cannot turn an otherwise successful Python program check red.

Code quality may still be part of the assignment rubric. Students should review the rubric before submitting the assignment.

#### ℹ️ Code Style Feedback: Ruff Was Not Available

GitHub could not run Ruff.

This does **not** mean the student's program is wrong.

It also does **not** change the Python program check result.

### 7. How Students Should Use CI Feedback

Use CI as another development tool.

A recommended workflow is:

1. **Write** a small part of the program.
2. **Run** the program in VS Code.
3. **Test** the program using the directions in the [Test Phase guide](../../Part-A/tests/README.md).
4. **Fix** problems you find.
5. **Save** your work to your personal GitHub repository.
6. **Review** the Python program check.
7. **Improve** the program if needed.

Do not wait until the assignment is finished before testing your program.

Frequent testing usually makes programming problems easier to find.

### 8. How to View CI Feedback on GitHub

In your personal repository:

1. Select the **Actions** tab.
2. Select the most recent **IT 140 Checks** workflow run.
3. Open **Python program check**.
4. Read the workflow summary first.

The workflow summary is designed to show the most important information without requiring students to read technical GitHub logs.

If more information is needed, open the step that did not pass:

* **Python syntax check**
* **acceptance tests**
* **Code style feedback**

Focus on the first problem that needs to be fixed.

## When Something Fails

### 9. A Failed Acceptance Test Is Usually Not a Cause for Concern

Programming includes finding and fixing errors.

During development, it is normal for:

* the Python syntax check to fail;
* one or more acceptance tests to fail; or
* Ruff to provide Code style feedback.

These results are part of the programming process.

A failed Python program check or acceptance test is **feedback about the current version of the program**, not a grade.

#### Recommended Response

When the Python program check fails:

1. Read the workflow summary.
2. Identify whether the problem is in the Python syntax check or acceptance tests.
3. Fix one problem at a time.
4. Run the program locally.
5. Run the acceptance tests locally.
6. Save the corrected program to GitHub.
7. Review the new workflow run.

Do **not** repeatedly re-run the same failed workflow run after changing code on your computer.

A workflow run checks the version of the files that was already saved to GitHub. It does not know about newer changes that have not been pushed.

### 10. Do Not Change the Acceptance Tests to Make Them Pass

The provided acceptance tests describe expected program behavior.

Students should change:

`Part-A/src/name_age.py`

to make the acceptance tests pass.

Students should **not** change:

`Part-A/tests/test_name_age.py`

to make an incorrect program appear correct.

The GitHub workflow protects against this problem by using the original provided acceptance tests when it checks a student's program.

Changing the test file in a personal repository therefore does not change the acceptance tests used by CI.

### 11. When a CI Result May Be a Cause for Concern

Some failures may indicate a problem with GitHub or the course repository rather than a problem with student code.

#### Students Should Report a Possible CI Problem When

* A brand-new personal repository reports a Python program failure before the student edits `name_age.py`.
* Changing only the SDW or IDE Features Reflection causes the Python program check to fail.
* A GitHub setup step fails before the Python syntax check begins.
* GitHub says that the Python program check could not finish.
* The same GitHub-related failure happens again after a later push.
* The workflow feedback clearly does not match the current `name_age.py` file stored on GitHub.

Before reporting a problem, open `name_age.py` in the personal repository on GitHub and make sure the expected version of the program is there.

If the current program is not on GitHub, the student may need to save and push the latest work first.

#### Do Not Post Assignment Code Publicly

The course repository's GitHub Issues and Discussions are public.

Do **not** paste assignment code into a public GitHub Issue or Discussion.

For a possible repository or CI problem, provide information such as:

* the name of the failed step;
* the error message;
* what action caused the workflow run; and
* a screenshot that does not show assignment code.

Use the help options in the [Module Two Assignment README](../../README.md) for additional support.

## Faculty Guidance

### 12. How Faculty Can Use Student CI Feedback

CI is best used as **formative feedback**: feedback that helps a student improve work while they are still developing it.

It is not a replacement for grading.

When helping a student, first identify the result shown in the workflow summary.

#### Python Syntax Check Failed

Help the student:

1. Find the line and column identified in the summary.
2. Read Python's problem message.
3. Look carefully at that line and the lines immediately before it.
4. Correct the syntax.
5. Run the program locally before saving it to GitHub again.

Avoid solving the programming task for the student when the error message provides enough information for the student to continue independently.

#### acceptance tests Failed

Help the student connect the failed test to:

* the Software Requirements Specification (SRS);
* the provided design;
* the expected program input; and
* the expected program output.

Encourage the student to fix one problem and test again.

#### Code Style Feedback Contains Suggestions

Treat Ruff as feedback, not as a CI failure.

Ruff suggestions may help students improve code quality, but they do not determine whether the Python program check passes.

The assignment rubric remains the authority for grading code quality.

#### Python Program Check Passed

A green Python program check means only that:

* Python could read the program; and
* the program passed the five provided acceptance tests.

It does **not** mean:

* the full assignment is complete;
* every rubric requirement is satisfied;
* the SDW is complete;
* the IDE Features Reflection is complete;
* the assignment has been submitted; or
* the assignment has been graded.

### 13. Using CI for Faculty Troubleshooting

CI can help faculty quickly separate different kinds of problems.

| Result | Most likely area to investigate |
| ------------------------------------- | ----------------------------------------- |
| Python syntax check failed | Python syntax |
| acceptance tests failed | Program behavior |
| Code style feedback has suggestions | Python code style |
| No Python program check was needed | `name_age.py` did not change in that push |
| GitHub setup step failed | GitHub Actions or repository problem |
| Python program check could not finish | GitHub Actions or repository problem |

If several students report the same GitHub setup failure, consider a course repository or GitHub Actions problem before assuming the students made the same programming mistake.

Report reproducible repository or CI problems through the course repository's GitHub Issues.

## Course Repository CI

### 14. What the Course Repository Check Does

The **Course repository check** is different from the student-facing Python program check.

It protects the assignment starter and support files in:

`GC-STEM/it140-m2-assignment`

The course repository contains many files students are not expected to maintain. These files need broader CI coverage so maintainers can detect accidental changes before they affect students.

The Course repository check validates areas such as:

* required repository files;
* provided Markdown structure;
* local Markdown links;
* the provided Draw.io file;
* provided pseudocode;
* repository configuration;
* the social preview image;
* Python syntax;
* Python code style;
* the provided acceptance tests; and
* the intentionally incomplete assignment starter.

The supporting CI files are:

* [`tests.yml`](../workflows/tests.yml) — defines the GitHub Actions workflow.
* [`check_repository.py`](./check_repository.py) — checks repository files and provided artifacts.
* [`check_starter.py`](./check_starter.py) — checks the intentional assignment starter state.
* [`test_name_age.py`](../../Part-A/tests/test_name_age.py) — contains the five provided acceptance tests.

### 15. Why Course and Student CI Are Different

The course repository and a student's personal repository have different purposes.

#### Course Repository

The course repository provides the assignment.

Its CI protects the **entire assignment package**.

A broken README, provided test, Draw.io file, configuration file, or CI file could affect many students.

Those problems should cause the Course repository check to fail so maintainers can correct them.

#### Personal Repository

A personal repository is where a student develops the assignment.

Its CI focuses on the **Python program**.

A problem in a student's SDW or IDE Features Reflection should not interfere with feedback about the Python program.

This separation keeps student feedback focused on the main programming task while preserving stronger quality controls for the course repository.

## Maintainer Guidance

### 16. When a Course Repository Check Fails

A failed Course repository check **is a cause for concern**.

Before merging or releasing a course repository change:

1. Open the failed workflow run.
2. Read the workflow summary.
3. Find the first failed step.
4. Read the failure message.
5. Correct the underlying problem.
6. Commit and push the correction.
7. Confirm that the new Course repository check passes.

Do not ignore a Course repository check failure simply because the assignment appears to work manually.

The purpose of the Course repository check is to catch problems that may not be obvious during a quick manual review.

### 17. When to Re-run a Workflow

Usually, fix the underlying problem and create a **new workflow run** by pushing the correction.

Re-running the same workflow is most useful when the failure appears unrelated to repository content, such as:

* a temporary GitHub Actions service problem;
* a package download failure;
* a temporary runner problem; or
* another external problem that may succeed without changing repository files.

Remember:

> Re-running a workflow uses the same saved version of the repository.

If the files changed, push the new files instead of re-running the old workflow.

### 18. CI Design Notes for Maintainers

The CI design intentionally follows several simple rules.

#### Separate Course and Student Purposes

The Course repository check protects the complete assignment package.

The Python program check provides focused student programming feedback.

#### Keep Student Failures Actionable

A red student result should point to something the student can reasonably act on in `name_age.py`.

Markdown work is kept out of the Python program check.

#### Use the Workflow Summary First

Important feedback is written to the GitHub workflow summary so students and faculty do not need to search technical logs for routine problems.

Logs remain available when more detail is needed.

#### Keep Code Style Feedback Advisory

Ruff provides useful feedback, but a Ruff suggestion does not cause the Python program check to fail.

The Ruff version is pinned so students receive consistent feedback throughout the course release.

#### Protect the acceptance tests

The student workflow uses the original provided `test_name_age.py` from the personal repository's starter history.

This keeps the acceptance tests consistent even if the test file in a personal repository is changed.

#### Use Read-Only Repository Permission

The workflow uses:

```yaml
permissions:
  contents: read
```

The workflow needs to read assignment files but does not need permission to modify repository contents.

#### Keep the Workflow Small

The student workflow checks only what is needed to provide useful programming feedback.

This follows the IT 140 CI principle:

> **Keep It Super Simple.**

### 19. CI Is One Part of the Learning Process

CI works best when it supports, rather than replaces, normal programming practices.

Students should still learn to:

* read requirements;
* design a solution;
* write code in small steps;
* run their own program;
* read error messages;
* test locally;
* debug problems;
* review code quality; and
* ask for help when needed.

GitHub CI adds another source of timely feedback.

It does not replace those skills.

## Summary

### 20. Key Points

For students:

> **Write → Run → Test → Save to GitHub → Review Feedback → Improve**

For faculty:

> **Use CI to help identify the type of programming problem, not to determine the assignment grade.**

For maintainers:

> **Keep the course repository green before releasing changes to students.**

And for everyone:

> **Keep It Super Simple.**
