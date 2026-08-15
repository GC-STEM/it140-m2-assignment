# Software Design Document

* **Course:** IT 140 - *Introduction to Scripting*
* **Activity:** 2-3: Module Two Assignment
* **Program Name:** `name_age`

## 0. General Description

The `name_age` program will use a simple, sequential design. The program will obtain the current calendar year, ask the user for their name and age, calculate the user's approximate birth year, and display a personalized result.

The design implements the requirements in the [Software Requirements Specification (SRS)](../analysis/name_age_srs.md) using programming concepts appropriate for Module Two. The provided starter code supplies program structure and system-date functionality that students have not yet studied.

## 1. Design Goals and Constraints

The design shall:

* **1.1** Keep the student-completed program logic simple, readable, and appropriate for an introductory programming course.

* **1.2** Use programming concepts introduced through Module Two for student-completed code, including console input and output, variables, integer conversion, arithmetic expressions, and string formatting.

* **1.3** Use the exact user prompts and output format specified in the SRS.

* **1.4** Use the current calendar year obtained from the system rather than a year entered by the user or hard-coded into the program.

* **1.5** Apply the required birth-year calculation to any integer age without adding age-range validation or other input-validation behavior that is not required by the SRS.

* **1.6** Preserve the provided `name_age.py` program structure, including the system-date import, `CURRENT_YEAR` constant, `main()` function, and main guard.

## 2. Solution Overview

The program uses a **sequential design**, meaning each step occurs once in order from beginning to end.

The solution will:

1. Obtain the current calendar year from the system date.
2. Prompt the user for their name.
3. Prompt the user for their age and treat the entered age as an integer.
4. Subtract the user's age from the current year to calculate the approximate birth year.
5. Display the user's name and calculated birth year using the required output format.

The program does not require decisions or repetition.

### Design Artifacts

* **Flowchart:** [`name_age.drawio`](./name_age.drawio)
* **Pseudocode:** [`name_age.pseudo`](./name_age.pseudo)

The flowchart, pseudocode, and this SDD represent the same planned solution.

## 3. Program Structure

The complete program is contained in one Python source file, [`name_age.py`](../src/name_age.py).

The starter file provides program structure that students are not expected to create during Module Two. Students complete only the introductory program logic inside the provided `main()` function and the required documentation.

| # | Component | Responsibility | Input | Output | SRS Requirement(s) |
| - | --------- | -------------- | ----- | ------ | ------------------ |
| 1 | Provided program setup | Import system-date functionality, obtain the current year, and provide the program entry structure | System date | `CURRENT_YEAR` | 1.4, 3.1, 3.3 |
| 2 | Student-completed program logic | Get user input, calculate the approximate birth year, and display the result | `CURRENT_YEAR`, user name, user age | Personalized console message | 1.1–1.5 |

## 4. Data Design

The program requires four important data values.

| # | Data Name | Type | Purpose | Initial Value or Source | Valid Values or Rules |
| - | --------- | ---- | ------- | ----------------------- | --------------------- |
| 1 | `CURRENT_YEAR` | Integer | Store the current calendar year used in the birth-year calculation | Current year from the system date | Provided by the starter code |
| 2 | `user_name` | String | Store the name entered by the user | Console input | No validation requirement is specified |
| 3 | `user_age` | Integer | Store the user's age for use in arithmetic | Console input converted to an integer | Any value that can be converted to an integer; no age-range validation is required |
| 4 | `birth_year` | Integer | Store the calculated approximate birth year | `CURRENT_YEAR - user_age` | Integer result of the required calculation |

## 5. Interface and Input/Output Design

The user interacts with the program through the console. The program does not use files, APIs, graphical interfaces, or other user-facing interfaces.

| # | Interface or I/O Element | Source or Destination | Format | Validation or Processing | Related Requirement(s) |
| - | ------------------------ | --------------------- | ---------------------------------------------- | ------------------------------------------------------------------------- | ---------------------- |
| 1 | Current calendar year | System date | Integer year | Obtained by provided starter code | 1.4 |
| 2 | Name prompt | User through console | `What is your name?` | Store entered text as a string | 1.1 |
| 3 | Age prompt | User through console | `How old are you?` | Convert entered text to an integer | 1.2, 1.3 |
| 4 | Personalized result | Console display | `Hello {name}! You were born in {birth_year}.` | Insert the user's name and calculated birth year into the required format | 1.5 |

See the SRS `## Sample Input and Output` section for complete examples of the user interaction.

## 6. Program Logic and Control Flow

The program follows one path from start to finish. Each operation occurs once and in sequence.

The [flowchart](./name_age.drawio) provides a visual representation of this sequence, and the [pseudocode](./name_age.pseudo) describes the same sequence as written steps.

### 6.1 Main Processing Steps

1. Obtain the current calendar year from the system date and store it as `CURRENT_YEAR`.
2. Display the name prompt and store the user's response as `user_name`.
3. Display the age prompt, convert the user's response to an integer, and store it as `user_age`.
4. Calculate `birth_year` by subtracting `user_age` from `CURRENT_YEAR`.
5. Display the personalized message containing `user_name` and `birth_year`.
6. End the program.

### 6.2 Decisions and Repetition

* **Decisions:** None. The program does not need conditional logic because the SRS does not require different behavior for different input values.
* **Repetition:** None. Each program step occurs once.

## 7. Error and Exception Handling

No custom input validation or error handling is required for this activity.

The design assumes that the user enters an age that Python can convert to an integer. If the age cannot be converted to an integer, Python may produce an error. Handling that condition is outside the requirements for this introductory program.

The program shall not add age-range checks. Values such as zero, negative integers, and ages greater than 100 are processed using the same required calculation.

## 8. Design Decisions and Rationale

| # | Design Decision | Rationale | Alternative Considered |
| - | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 1 | Use a sequential solution | The problem requires only a short series of steps and does not require decisions or repetition. This keeps the solution appropriate for Module Two. | Adding branches or loops; not needed |
| 2 | Obtain the current year from the system date | The result should be based on the calendar year when the program runs rather than a fixed year. | Hard-code a year; rejected because it would become outdated |
| 3 | Convert the user's age to an integer when reading it | Console input is initially text, but the age must be used in an arithmetic expression. | Keep the age as a string; would not support the required subtraction |
| 4 | Use one subtraction for all integer ages | The SRS requires the same calculation and does not require age validation. This also supports the provided edge cases. | Add age-range validation; not required |
| 5 | Use formatted string output for the result | String formatting allows the program to insert the user's name and calculated birth year into the required output message clearly. | Build the output with several separate statements; unnecessary |
| 6 | Provide advanced program structure in the starter code | Students can focus on concepts introduced through Module Two without having to create system-date or function structure they have not yet studied. | Require students to create the full structure; not appropriate for this module |

## 9. Requirements Traceability

The design connects each SRS requirement to the part of the solution that implements it.

| SRS Requirement | Design Component or Section | Supporting Artifact |
| --------------- | --------------------------- | ------------------- |
| 1.1 | §5 name input; §6.1 step 2 | Flowchart: User name; pseudocode: name prompt and input |
| 1.2 | §5 age input; §6.1 step 3 | Flowchart: User age; pseudocode: age prompt and input |
| 1.3 | §4 `user_age`; §5 age processing; §6.1 step 3 | Pseudocode and starter code |
| 1.4 | §4 `CURRENT_YEAR` and `birth_year`; §6.1 steps 1 and 4 | Flowchart: Initialize current year and Calculate birth year; pseudocode |
| 1.5 | §5 personalized result; §6.1 step 5 | Flowchart: Welcome message and birth year; pseudocode |
| 2.1–2.3 | §1 design goals; §3 program structure; §8 design decisions | Starter code |
| 3.1 | §3 one-file Python program structure | `name_age.py` |
| 3.2 | §5 console input/output design | Flowchart and pseudocode |
| 3.3 | §1 and §3 provided course-IDE-compatible structure | `name_age.py` |
| 4.1 | §6 sequential control flow; §7 valid-input assumption | SRS acceptance test cases |
| 4.2 | §6 program logic; §7 edge-case handling | SRS acceptance test cases and provided automated tests |

## 10. Design Review Checklist

Before beginning construction, confirm that:

* [x] **10.1** The design addresses every applicable SRS requirement.
* [x] **10.2** The program uses a simple structure appropriate for this activity.
* [x] **10.3** Important data names, types, sources, and purposes are defined.
* [x] **10.4** The input, processing, and output steps are complete and consistent.
* [x] **10.5** The design identifies that no decisions or repetition are required.
* [x] **10.6** The design does not add error-handling or validation requirements that are outside the SRS.
* [x] **10.7** The SDD, flowchart, and pseudocode describe the same solution.
* [x] **10.8** Student-completed code can use programming concepts introduced through Module Two.
* [x] **10.9** The design can be checked using the SRS acceptance test cases.

## 11. References

GC STEM. (n.d.). *Software requirements specification: name_age* [Course artifact]. [`../analysis/name_age_srs.md`](../analysis/name_age_srs.md)

Southern New Hampshire University. (n.d.). *IT 140 Module Two Assignment guidelines and rubric* [Course assignment].
