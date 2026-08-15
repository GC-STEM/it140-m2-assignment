# Software Development Worksheet (SDW)

**Activity:** {{activity_number_and_title}}

Use this worksheet as working notes while you move through the Analyze and Design phases of the SDLC. Your notes do not need to be formal or polished. Their purpose is to help you understand the requirements and plan your solution before you begin constructing it.

**This worksheet is not a deliverable.** Do not submit it in D2L Brightspace for grading.

> **Tip:** Keep your answers brief and write them in your own words. Refer to the provided Software Requirements Specification (SRS), Software Design Document (SDD), and test cases when you need more detail.

## 1. Document Review

Before planning your solution, review the provided activity files:

* [ ] [Software Requirements Specification (SRS)](./name_age_srs.md) — describes what the program must do and includes the sample input and output (I/O) and acceptance test cases.

* [ ] [Software Design Document (SDD)](../design/name_age_sdd.md) — describes the planned solution.

* [ ] [Flowchart](../design/name_age.drawio) — shows the planned program logic visually.

* [ ] [Pseudocode](../design/name_age.pseudo) — describes the planned program logic as step-by-step instructions.

* [ ] [Starter Code](../src/name_age.py) — provides the Python file you will complete during the Construct phase.

* [ ] [Automated Tests](../tests/test_name_age.py) — provide tests you will use during the Test phase to check your completed program.

{{Add, remove, or rename files as appropriate for the activity. Keep files grouped in the repository folder that corresponds to their SDLC phase.}}

## 2. Program Purpose

*In one sentence, summarize the program's purpose **in your own words**. It is important to use your own words rather than copying the SRS or asking AI to generate the answer. If you cannot clearly and concisely explain the purpose, you may not understand the requirements and, thus, will not be able to construct correct Python code. You will need this purpose summary when you write your program documentation string (docstring)*

TODO: What is this program or solution supposed to do for its user?

## 3. Inputs, Processing, and Outputs

Think about the solution as three basic parts:

> **Input → Processing → Output** or "IPO"

### Inputs

What information does the solution receive? 

* TODO: Identify an input and where it comes from.
* TODO: Identify another input, if needed.

What data type or format should each input use?

* TODO: Identify the expected type or format for each input, if specified.

### Processing

What must happen to the input before the solution produces its output?

* TODO: Describe the main calculation, conversion, decision, repetition, or other processing.
* TODO: Add additional processing as needed.

### Outputs

What information must the solution produce?

* TODO: Identify an output and where it goes.
* TODO: Identify another output, if needed.

Does the output need to follow a particular format?

* TODO: Record any required wording, spacing, formatting, or other output requirements.

## 4. Requirements in My Own Words

Review the important requirements in the SRS. For each one, briefly explain what it means **in your own words**.

* **SRS requirement {{requirement_number}}:** {{TODO: What does this requirement mean?}}
* **SRS requirement {{requirement_number}}:** {{TODO: What does this requirement mean?}}
* **SRS requirement {{requirement_number}}:** {{TODO: What does this requirement mean?}}

{{Add or remove requirements as appropriate. Focus on understanding the requirements rather than copying the SRS.}}

## 5. Plan the Solution

Use the provided Software Design Document (SDD), flowchart, pseudocode, or other design materials to identify the major steps the solution should follow.

For early activities, think about the steps as **get input → process information → produce output**.

1. TODO: What should happen first?
2. TODO: What should happen next?
3. TODO: What should happen next?
4. TODO: What should happen last?

{{Add or remove steps as appropriate. Describe what the solution needs to do without worrying about exact programming-language syntax.}}

### Program Structure

{{Include this subsection only when students need to understand or plan multiple functions, classes, files, or other program components. Remove it when it is not needed.}}

* TODO: Identify a provided or planned function, class, file, or other component and briefly describe its job.
* TODO: Add other components as needed.

## 6. Check the Plan With an Example

Choose one provided test case and follow your planned solution by hand before constructing it.

**Test case:** TODO: Identify the test case you are using.

**Input:**

* TODO: Record the test input values.

**Processing:**

1. TODO: Apply the first relevant step using the test values.
2. TODO: Continue the processing as needed.

**Expected output:**

* TODO: Record the result your plan should produce.

Compare your result with the expected result in the provided test case.

* [ ] My result matches the expected result.
* [ ] My result does not match. I need to review the SRS, SDD, or my plan before continuing.

## 7. Important Constraints and Special Cases

Review the SRS, SDD, starter files, and test cases for rules or limits that affect your solution.

### Constraints

* TODO: Record any required programming concepts, tools, formats, or techniques.
* TODO: Record anything the solution must not do or use, if specified.
* TODO: Record other important constraints.

### Special or Edge Cases

* TODO: Record any special, boundary, or unusual cases identified in the SRS or test cases.
* TODO: Add additional cases as needed.
* TODO: If no special cases are specified, enter "None stated."

### Invalid Input or Error Cases

* TODO: Record any invalid-input or error-handling behavior specifically required by the SRS.
* TODO: If no error-handling behavior is required, enter "None stated." Do not add requirements that are not in the SRS.

## 8. Questions or Unclear Requirements

Record anything you do not understand or need to confirm before continuing.

* TODO: Record a question or unclear requirement.
* TODO: Add additional questions as needed.
* TODO: If everything is clear, enter "None."

## 9. Ready to Construct

Before continuing to the Construct phase, make sure:

* [ ] I can explain in my own words what the solution must accomplish.
* [ ] I understand the required inputs, processing, and outputs.
* [ ] I understand the important requirements in the SRS.
* [ ] I reviewed the provided design and understand its major steps.
* [ ] I checked my plan using at least one provided test case.
* [ ] My plan agrees with the SRS and SDD.
* [ ] I identified important constraints and special cases.
* [ ] I recorded or resolved anything that is unclear.
* [ ] I am ready to use the provided starter template to construct the solution.

<!-- Scaffolding Notes

This SDW is designed to provide substantial guidance during early IT 140 activities. As students gain experience with programming and the SDLC, prompts may be shortened or removed while keeping the same general worksheet structure.

Possible scaffold reduction:

* Early course:
  * Provide explicit document-review checklist.
  * Separate Input, Processing, and Output prompts.
  * Provide guided numbered solution-plan prompts.
  * Provide a structured test-case trace.
  * Provide detailed Ready to Construct checklist.

* Middle course:
  * Reduce IPO prompts.
  * Remove most explanatory text.
  * Require students to identify the major solution steps with less prompting.
  * Reduce the test-case trace to input, expected processing, and expected output.

* Late course:
  * Replace detailed IPO prompts with a brief data-flow summary.
  * Allow students to select which SRS requirements require planning notes.
  * Use a largely free-form solution plan.
  * Reduce the readiness checklist to a few key checks.

-->

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: {{activity_number_and_title}} | Software Development Worksheet
* Artifact Type: Working notes; not submitted for grading unless otherwise specified
* Artifact Purpose: Help students understand provided requirements and designs and plan a solution before construction.
* Artifact Description: A scaffolded SDLC worksheet for recording program purpose, inputs, processing, outputs, requirements, solution planning, test-case tracing, constraints, special cases, questions, and construction readiness.
* Artifact Version: {{semantic_version_number}}
* Artifact Date: {{artifact_date_in_YYYY-MM-DD_format}}
* Development Status: {{development_status}}

-->
