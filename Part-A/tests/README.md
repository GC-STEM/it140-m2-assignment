<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Test Phase

**SDLC progress:** [0 Start Here](../README.md) → [1 Analyze](../analysis/README.md) → [2 Design](../design/README.md) → [3 Construct](../src/README.md) → **4 Test** → [5 Submit](https://learn.snhu.edu/)

## Purpose

During the Test phase, you check whether your completed program behaves as required before submitting it for grading.

You have already done some testing:

* During **Design**, you traced one acceptance test case by hand in your [Software Development Worksheet (SDW)](../name_age_sdw.md).

* During **Construct**, you ran your program after making small changes and corrected Python errors.

Now you can test the completed program against the assignment requirements.

The official course feedback method is the **2-3 Instant Feedback Tool** accessible from D2L Brightspace. You may also run the provided Python acceptance tests in VS Code to learn how automated software testing works.

## Deliverable

**This phase does not produce a separate deliverable.**

You may make corrections to [`name_age.py`](../src/name_age.py) while testing. Your completed `name_age.py` file remains the programming deliverable you will submit in **D2L Brightspace**.

Do not submit:

* The SDW
* `test_name_age.py`
* Test output
* Sense feedback

The Module Two Assignment also includes a separate **IDE Features Reflection** deliverable.

## What You Will Use

Use the following resources during this phase:

* [`name_age.py`](../src/name_age.py) — the program you are testing and correcting.
* [Software Requirements Specification (SRS)](../analysis/name_age_srs.md) — defines the required behavior and shared acceptance test cases.
* [Software Development Worksheet (SDW)](../name_age_sdw.md) — includes your earlier hand trace of an acceptance test case.
* [`test_name_age.py`](./test_name_age.py) — provides optional automated tests for the shared SRS acceptance cases.
* **2-3 Instant Feedback Tool: Software Development Introduction** in [D2L Brightspace](https://learn.snhu.edu/) — provides the official course-specific Sense feedback for this assignment.

## What You Will Do

### 1. Make Sure Your Program Runs

Before using either feedback method, run `name_age.py` yourself in VS Code.

Your program should:

1. Ask for a name.
2. Ask for an age.
3. Calculate the approximate birth year.
4. Display the required personalized result.
5. Finish without a Python error.

If the program does not run, return to the [Construct phase](../src/README.md) and correct the problem before continuing.

### 2. Use the Sense Instant Feedback Tool

**Sense is the official course feedback method for this assignment. Using it is encouraged but not required.**

In D2L Brightspace:

1. Open **2-3 Instant Feedback Tool: Software Development Introduction**.
2. Select **Software Development Introduction**.
3. Follow the on-screen instructions to provide your completed program to Sense.
4. Review the feedback about how well your program meets the assignment requirements.
5. Return to VS Code and correct `name_age.py` if needed.
6. Run your program again after making changes.
7. You may return to Sense and request feedback again as many times as needed before submitting your assignment.

> **Important:** Sense provides feedback, but it does **not** submit your assignment for grading. You must still submit the required deliverables to the Module Two Assignment in D2L Brightspace.

#### Python Version in Sense

Sense currently runs **Python 3.8**.

The provided `name_age.py` starter file and the Python concepts required for this assignment are compatible with Python 3.8. If you complete only the provided TODO lines using the Module One and Module Two concepts identified in the [Construct instructions](../src/README.md), you do not need to make any changes for Sense.

Avoid adding unnecessary code or Python features beyond the assignment requirements.

### 3. Optional: Learn to Use Automated Tests

The provided [`test_name_age.py`](./test_name_age.py) file gives you another way to check your program.

**Using this test file is optional.** You have not studied Python testing yet, and you are not expected to understand or modify the test code.

An **automated test** is code that:

1. Runs another program with known inputs.
2. Captures what the program produces.
3. Compares the actual result with the expected result.
4. Reports whether the check passed or failed.

The provided test file repeats this process for the shared acceptance cases in the SRS.

Automated testing is useful because the same tests can be run again after every code change. The tests also remain with this repository, while Sense is tied to this specific D2L course activity and may not be available after your course ends.

The local tests **supplement Sense; they do not replace the course-specific feedback Sense provides**.

### 4. Recognize the Test File Structure

Open [`test_name_age.py`](./test_name_age.py).

The file contains Python concepts you have not learned yet. **Do not change the test file.**

You only need a general idea of what its major sections do.

#### Imports

The test file imports tools from the **Python Standard Library**. No additional Python packages need to be installed for these tests.

#### Constants

The file identifies:

* The repository root
* The location of your `src/name_age.py` program

This allows the tests to find and run your program.

#### Test Class

You will see:

```python
class NameAgeAcceptanceTests(unittest.TestCase):
```

A **class** can group related data and behaviors together. You will study classes later in **Module Eight**.

For now, you only need to know that this class groups the acceptance tests for `name_age.py`.

Each method whose name begins with `test_` represents one acceptance test:

```text
test_1_typical_adult_age
test_2_different_adult_name_and_age
test_3_zero_age_edge_case
test_4_negative_age_edge_case
test_5_age_over_100_edge_case
```

These correspond to the shared acceptance test cases in the SRS.

#### Helper Function

The test file also contains a helper function named `run_program()`.

It starts your `name_age.py` file as a separate Python process, supplies test input, and captures the program's output so that the test can examine it.

You do not need to understand how this function works yet.

#### Main Guard

Like your `name_age.py` file, the test file ends with a main guard:

```python
if __name__ == "__main__":
    unittest.main(verbosity=2)
```

When you run `test_name_age.py` directly, this starts the automated tests.

You do not need to change or fully understand this code.

### 5. Optional: Run the Automated Tests

Run the test file from the repository root using the **VS Code integrated terminal**.

In VS Code, select:

```text
Terminal > New Terminal
```

The terminal should normally open in or near your course repository.

#### Codio Virtual Desktop (CVD) / macOS / Linux / Git Bash

Run:

```bash
cd ~/Repos/it140-m2-assignment
python3 tests/test_name_age.py
```

#### Windows PowerShell

Run:

```powershell
cd ~/Repos/it140-m2-assignment
py tests/test_name_age.py
```

If you cloned the repository somewhere other than `~/Repos`, change the path in the `cd` command to match your repository location.

### 6. Interpret the Test Results

The test runner reports the result of each acceptance test.

#### All Tests Pass

When a test passes, its result ends with:

```text
... ok
```

When all five tests pass, the summary ends with:

```text
Ran 5 tests in ...

OK
```

`OK` means your program passed all five **local acceptance tests**.

It does not guarantee a particular assignment grade. Your program must also meet the other requirements in the assignment Guidelines and Rubric.

#### A Test Fails

A failed test is reported with:

```text
FAIL
```

A failure means your program's behavior did not match what that test expected.

Read:

1. The name of the test that failed.
2. The failure information printed below the test summary.
3. The corresponding acceptance test case in the [SRS](../analysis/name_age_srs.md).

Then:

1. Return to `name_age.py`.
2. Find the part of your code related to that requirement.
3. Correct **one problem at a time**.
4. Run `name_age.py` yourself.
5. Run the automated tests again.

Do **not** change `test_name_age.py` to make a failing test pass. Correct your program instead.

#### Your Program Has a Python Error

If `name_age.py` cannot run because of a Python error, the test output may include:

```text
Program ended with an error:
```

followed by Python error information.

Read the last part of the error message and use the VS Code **Problems** panel and the [Construct instructions](../src/README.md) to help locate the problem.

Correct the error in `name_age.py`, run your program again, and then rerun the tests.

#### The Test File Reports an ERROR

If the test runner reports:

```text
ERROR
```

rather than `FAIL`, the automated test itself could not complete normally.

First make sure:

* You ran the command from the `it140-m2-assignment` repository.
* `src/name_age.py` still exists in its original location.
* `tests/test_name_age.py` still exists in its original location.
* You did not modify the provided test file.

If the problem continues, use the support options below.

### 7. Correct and Retest

Testing is an iterative process:

> **Test → Find a problem → Correct the program → Test again**

Continue until you are satisfied that `name_age.py` meets the requirements.

If you use both testing methods, a useful order is:

1. Run `name_age.py` yourself.
2. Run the optional local automated tests.
3. Correct any problems.
4. Use Sense for course-specific feedback.
5. Correct any remaining problems.
6. Retest before submitting.

> **IDE Features Reflection reminder:** As you test, notice how the VS Code integrated terminal, Problems panel, syntax highlighting, and error indicators help you find and understand problems. Your observations may be useful when you complete the separate [IDE Features Reflection](../../Part-B/ide_features.md).

<!-- FUTURE: GitHub Actions

## Optional: Run Tests with GitHub Actions

{{Maintainer: Add student-facing instructions after the GitHub Actions workflow is implemented. Explain where students can see the automated check, how to interpret pass/fail status, and that GitHub Actions supplements rather than replaces Sense feedback.}}

-->

## Check Your Work

Before continuing to Submit, make sure:

* [ ] I can run `name_age.py` without a Python error.
* [ ] I compared my program's behavior with the SRS requirements.
* [ ] I corrected problems I found during testing.
* [ ] I ran my program again after making corrections.
* [ ] If I used Sense, I reviewed its feedback and made appropriate corrections.
* [ ] If I used the local automated tests, I understand whether all five tests passed.
* [ ] I did not modify the provided `test_name_age.py` file.
* [ ] My final `name_age.py` file is saved and ready to submit.
* [ ] I also completed the separate IDE Features Reflection deliverable.

## Help and Support

If you have difficulty completing this phase:

* Review the [SRS acceptance test cases](../analysis/name_age_srs.md#acceptance-test-cases) to see the expected behavior.
* Review the [Construct instructions](../src/README.md) if your program has a Python syntax or runtime error.
* See the [Module Two Assignment Wiki](https://github.com/GC-STEM/it140-m2-assignment/wiki) for supplemental testing and course-IDE guidance.
* Use [GitHub Discussions](https://github.com/GC-STEM/it140-m2-assignment/discussions) for questions about using the repository or understanding the provided local testing tools.
* Use [GitHub Issues](https://github.com/GC-STEM/it140-m2-assignment/issues) to report a technical problem with the provided repository files or automated tests.
* Contact your instructor through D2L Brightspace for questions about Sense, assignment requirements, grading, or feedback.

## Next Steps

When your program has been tested and both Module Two deliverables are ready, continue to [Submit](https://learn.snhu.edu/) in D2L Brightspace.

Remember: **Sense feedback and local test results do not submit your assignment for you.**

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: 2-3 Module Two Assignment | Test Phase
* Artifact Type: Required assignment guidance; no separate Test-phase deliverable
* Artifact Purpose: Guide students through checking the Module Two name_age program using the official Sense feedback activity and optional local automated acceptance tests.
* Artifact Description: Students test and revise name_age.py, use the encouraged Sense Instant Feedback Tool in D2L Brightspace, optionally run provided standard-library acceptance tests in VS Code, and interpret testing feedback before submission.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
