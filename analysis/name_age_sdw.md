<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Software Development Worksheet (SDW)

* **Course:** IT 140 - *Introduction to Scripting*
* **Activity:** 2-3: Module Two Assignment
* **Program:** `name_age`

Use this worksheet as working notes while you move through the **Analyze** and **Design** phases of the Software Development Life Cycle (SDLC).

Your notes do not need to be formal or polished. Keep your answers brief and write them in your own words. The purpose of the SDW is to help you understand the requirements and provided design before you begin constructing your program.

**This worksheet is not a deliverable.** Do not submit it in D2L Brightspace for grading.

## Analyze Phase

**SDLC progress:** [0 Start Here](../README.md) → **1 Analyze** → [2 Design](../design/README.md) → [3 Construct](../src/README.md) → [4 Test](../tests/README.md) → [5 Submit](https://learn.snhu.edu/)

During the Analyze phase, focus on **what the program must do**. Use the Software Requirements Specification (SRS) as your primary source.

### 1. Review the Requirements

Before completing the Analyze sections of this worksheet, review:

* [ ] [Software Requirements Specification (SRS)](./name_age_srs.md)
  * `## 0. General Description`
  * `## 1. Functional Requirements`
  * `## 2. Nonfunctional Requirements`
  * `## 3. Technology Constraints`
  * `## 4. Quality of Service Constraints`
  * `## Sample Input and Output`
  * `## Acceptance Test Cases`

### 2. Program Purpose

In one sentence, summarize the program's purpose **in your own words**.

Do not copy the SRS or ask AI to generate your answer. You will use your understanding of the program's purpose when you write the documentation string (docstring) in your Python program.

> **Where to look:** [SRS](./name_age_srs.md) → `## 0. General Description`

*What is this program supposed to do for its user?*

**TODO:** Replace this line with your answer.

### 3. Inputs, Processing, and Outputs

Think about the solution as three basic parts:

> **Input → Processing → Output** or **IPO**

#### IPO: Inputs

> **Remember:** Inputs are not limited to information a user types. They can also include data loaded from files or API calls and values the program obtains or sets internally, such as values stored in variables or constants.

*What information does the program receive or obtain?*

> **Where to look:** [SRS](./name_age_srs.md) → `## 0. General Description` and `## 1. Functional Requirements`, especially requirements **1.1–1.4**

* **TODO:** Identify each input or internally obtained value the program needs and where it comes from.

*What data type or format does each input need?*

> **Where to look:** [SRS](./name_age_srs.md) → `## 1. Functional Requirements`, especially requirement **1.3**. If a data type or format is not specified, write **Not specified**.

* **TODO:** Identify the required data type or format for each input when specified.

#### IPO: Processing

*What must happen to the inputs before the program produces its output?*

> **Where to look:** [SRS](./name_age_srs.md) → `## 0. General Description` and `## 1. Functional Requirements`, especially requirements **1.3–1.4**

* **TODO:** Describe the required processing in your own words.

#### IPO: Outputs

*What information must the program produce?*

> **Where to look:** [SRS](./name_age_srs.md) → `## 1. Functional Requirements`, especially requirement **1.5**

* **TODO:** Identify the required output and where it is displayed.

*Does the output need to follow a particular format?*

> **Where to look:** [SRS](./name_age_srs.md) → `## 1. Functional Requirements`, requirement **1.5**, and `## Sample Input and Output`

* **TODO:** Record the required output format.

### 4. Requirements in My Own Words

A few important requirements from the SRS are listed below. For each one, briefly explain **in your own words** what the requirement means. Do not copy the requirement or ask AI to generate your answer. The goal is to make sure you understand what the program must do before you begin constructing it.

> **Where to look for all four requirements:** [SRS](./name_age_srs.md) → `## 1. Functional Requirements`

* **SRS requirement 1.2 — Get the user's age**
  * **TODO:** Explain what requirement 1.2 means in your own words.

* **SRS requirement 1.3 — Use the age in an arithmetic calculation**
  * **TODO:** Explain what requirement 1.3 means in your own words.

* **SRS requirement 1.4 — Calculate the approximate birth year**
  * **TODO:** Explain what requirement 1.4 means in your own words.

* **SRS requirement 1.5 — Display the personalized result**
  * **TODO:** Explain what requirement 1.5 means in your own words.

### 5. Constraints and Special Cases

Requirements can include more than what a program does. They can also specify how the program should be written, where it should run, and what conditions it must handle.

#### Important Constraints

> **Where to look:** [SRS](./name_age_srs.md) → `## 2. Nonfunctional Requirements`, `## 3. Technology Constraints`, and `## 4. Quality of Service Constraints`

*Identify two or three important constraints you need to remember when constructing or testing the program.*

* **TODO:** List the important constraints here.

#### Special or Edge Cases

An **edge case** uses an unusual or boundary value that can help reveal problems in a solution.

> **Where to look:** [SRS](./name_age_srs.md) → `## Acceptance Test Cases`, especially the tests identified as edge cases

*Identify the edge cases the program will be tested with.*

* **TODO:** List the edge cases here.

### 6. Analyze Checkpoint

Before continuing to the Design phase, make sure:

* [ ] I can explain the program's purpose in my own words.
* [ ] I identified the program's inputs, processing, and outputs.
* [ ] I understand the selected functional requirements.
* [ ] I identified important constraints and edge cases.
* [ ] I did not add requirements that are not stated in the SRS.

When these checks are complete, continue to the [Design phase](../design/README.md).

## Design Phase

**SDLC progress:** [0 Start Here](../README.md) → [1 Analyze](../analysis/README.md) → **2 Design** → [3 Construct](../src/README.md) → [4 Test](../tests/README.md) → [5 Submit](https://learn.snhu.edu/)

During the Design phase, focus on **how the program will meet the requirements**. The design has already been provided for you. Your job is to understand it well enough to use it when you construct the program.

### 7. Review the Design

Before completing the Design sections of this worksheet, review:

* [ ] [Software Design Document (SDD)](../design/name_age_sdd.md)
  * `## 2. Solution Overview`
  * `## 4. Data Design`
  * `## 5. Interface and Input/Output Design`
  * `## 6. Program Logic and Control Flow`
  * `### 6.1 Main Processing Steps`
* [ ] [Flowchart](../design/name_age.drawio) → **Flowchart** page; follow the path from **Start** to **End**
* [ ] [Pseudocode](../design/name_age.pseudo) → read the algorithm from **START name_age** through **END name_age**

Remember:

> **SRS = what the program must do**  
> **SDD, flowchart, and pseudocode = how the program is planned to do it**

### 8. Plan the Solution

Use the provided design to summarize the program's major steps **in your own words**. Do not copy the pseudocode and do not worry about exact Python syntax yet.

> **Where to look:**
>
> * [SDD](../design/name_age_sdd.md) → `## 6. Program Logic and Control Flow` and `### 6.1 Main Processing Steps`
> * [Flowchart](../design/name_age.drawio) → **Flowchart** page
> * [Pseudocode](../design/name_age.pseudo) → **START name_age** through **END name_age**

1. *What information or values must the program obtain or set before it can perform the calculation?*
   1. **TODO:** List your answer(s) here.

2. *What information must the program get from the user?*
   1. **TODO:** List your answer(s) here.

3. *What processing or calculation(s) must the program perform?*
   1. **TODO:** List your answer(s) here.

4. *What result(s) must the program produce?*
   1. **TODO:** List your answer(s) here.

### 9. Check the Plan With an Example

Before writing Python code, follow the planned solution by hand using one provided test case.

For this activity, use **Test 1: Typical adult age**.

#### Test Input

> **Where to look:** [SRS](./name_age_srs.md) → `## Acceptance Test Cases` → **Test 1. Typical adult age**

* **TODO:** Record the current year and user input values from Test 1.

#### Test Processing

Use the values from Test 1 and follow the calculation described by the design.

> **Where to look:**
>
> * [SRS](./name_age_srs.md) → `## 1. Functional Requirements`, requirement **1.4**
> * [SDD](../design/name_age_sdd.md) → `## 6. Program Logic and Control Flow`
> * [Pseudocode](../design/name_age.pseudo) → the step that calculates the birth year

* **TODO:** Show the calculation using the Test 1 values.

#### Expected Output

> **Where to look:** [SRS](./name_age_srs.md) → `## Acceptance Test Cases` → **Test 1. Typical adult age**

* **TODO:** Record the expected output for Test 1.

Compare your hand-calculated result with the expected result:

* [ ] My result matches the expected result.
* [ ] My result does not match. I need to review the SRS and design before continuing.

### 10. Questions or Unclear Information

Before constructing the program, make sure the requirements and design make sense together.

If something seems missing, unclear, or inconsistent, record it here rather than guessing.

> **Where to look:** Compare:
>
> * [SRS](./name_age_srs.md) → `## 1. Functional Requirements`
> * [SDD](../design/name_age_sdd.md) → `## 2. Solution Overview` through `## 6. Program Logic and Control Flow`
> * [Flowchart](../design/name_age.drawio) → **Flowchart** page
> * [Pseudocode](../design/name_age.pseudo) → **START name_age** through **END name_age**

* **TODO:** Record any question, unclear requirement, or difference you notice between the requirements and design. If everything is clear and consistent, write **None**.

### 11. Ready to Construct

Your analysis and design notes will help you complete the provided Python starter file.

Before continuing, open [`name_age.py`](../src/name_age.py) and notice how your SDW work connects to the starter code:

* Your **Program Purpose** notes will help with the first line of the module docstring.
* Your **Inputs, Processing, and Outputs** notes will help with the `Input:`, `Process:`, and `Output:` sections of the module docstring.
* Your **Plan the Solution** notes will help you understand the Step 1, Step 2, and Step 3 placeholders in `main()`.
* Your understanding of the **SRS requirements** will help you determine whether your completed code does what is required.

> **Where to look:** [Starter Code](../src/name_age.py) → the module docstring at the top of the file and the TODO comments inside `main()`

Before continuing to the Construct phase, make sure:

* [ ] I can explain what the program must accomplish.
* [ ] I understand its inputs, processing, and outputs.
* [ ] I understand the major steps in the provided design.
* [ ] I checked the design using a provided acceptance test case.
* [ ] I recorded or resolved anything that was unclear.
* [ ] I am ready to use the starter code to construct the program.

When these checks are complete, continue to the [Construct phase](../src/README.md).

<!-- Scaffolding Notes

This SDW provides substantial guidance because Module Two is the student's first course assignment using the simplified SDLC.

As students progress through IT 140, scaffolding can be reduced while preserving the Analyze → Design → Construct workflow.

Possible scaffold reduction:

* Early course:
  * Provide exact file and section references for each task.
  * Separate Input, Processing, and Output prompts.
  * Select 2–4 SRS requirements for students to explain.
  * Provide guided solution-plan prompts.
  * Select a test case for students to trace.
  * Provide detailed Analyze and Ready to Construct checkpoints.

* Middle course:
  * Keep file and section references but reduce explanatory text.
  * Combine IPO prompts.
  * Reduce the number of guided solution-plan questions.
  * Allow students to choose which provided test case to trace.
  * Shorten phase checkpoints.

* Late course:
  * Point students to the appropriate source documents without identifying every section.
  * Ask students to identify the most important requirements themselves.
  * Replace detailed IPO prompts with a concise data-flow summary.
  * Use a largely free-form solution plan.
  * Ask students to select an appropriate test case to trace.
  * Use minimal phase checkpoints.

-->

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: 2-3 Module Two Assignment | Software Development Worksheet
* Artifact Type: Working notes; not submitted for grading
* Artifact Purpose: Help students understand the provided requirements and design before constructing the Module Two program.
* Artifact Description: A scaffolded SDLC worksheet that guides students through Analyze and Design by connecting each task to the specific provided source document and section needed to complete it.
* Artifact Version: {{semantic_version_number}}
* Artifact Date: {{artifact_date_in_YYYY-MM-DD_format}}
* Development Status: {{development_status}}

-->
