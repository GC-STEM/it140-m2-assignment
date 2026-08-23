<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Software Requirements Specification

* Course: IT 140 - *Introduction to Scripting*
* Activity: 2-3: Module Two Assignment
* Program Name: `name_age`

## 0. General Description

The `name_age` program is a simple Python program that asks the user for their name and age. The program calculates the user's approximate birth year and displays a personalized message containing the user's name and calculated birth year.

For this simplified introductory program, the birth year is calculated by subtracting the user's age from the current calendar year. The program does not ask for the user's exact birthdate or if they have had their birthdate this year.

This SRS describes the requirements and constraints for the `name_age.py` programming deliverable. Requirements include both functional (what the program must do) and nonfunctional (how the program must be structured or behave). Constraints focus on technology and quality expectations.

## 1. Functional Requirements

The program shall:

* [Input] **1.1** Prompt the user to enter their name using the prompt "`What is your name?` ".

* [Input] **1.2** Prompt the user to enter their age using the prompt "`How old are you?` ".

* [Processing] **1.3** Treat the entered age as an integer (i.e., a whole number) that can be used in an arithmetic calculation.

* [Processing] **1.4** Calculate the user's approximate birth year by subtracting the entered age from the current calendar year.

* [Output] **1.5** Display a personalized result using the user's name and calculated birth year in this format:

  `Hello {name}! You were born in {year}.`

## 2. Nonfunctional Requirements

The program shall:

* [Code Quality] **2.1** Follow the programming best practices introduced in zyBooks 1.5: Style guidelines, including appropriate variable names, whitespace, and comments.

* [Code Quality] **2.2** Use appropriate Python statements without unnecessary code, steps, or procedures.

* [Readability] **2.3** Be organized and formatted so that the program logic is easy to read and understand.

## 3. Technology Constraints

The program shall:

* [Language] **3.1** Be implemented as a Python source-code file named `name_age.py`.

* [Input/Output] **3.2** Receive user input and display program output through the program's console.

* [Environment] **3.3** Run using the Python environment provided by the IT 140 course IDE.

## 4. Quality of Service Constraints

The program shall:

* [Correctness] **4.1** Complete without a Python error when given the valid input described in this SRS.

* [Correctness] **4.2** Produce the correct result for the provided acceptance test cases.

No input-validation, security, or performance requirements are specified for this introductory program.

## Sample Input and Output

The birth year depends on the current calendar year when the program runs. The example below assumes that the current year is **2026**. Do **NOT** hardcode the current year in your program. 

User-entered values appear after each program prompt.

### Sample Run 1

```text
What is your name? Pat
How old are you? 31

Hello Pat! You were born in 1995.
```

### Sample Run 2

```text
What is your name? Casey
How old are you? 23

Hello Casey! You were born in 2003.
```

## Acceptance Test Cases

The acceptance tests use the current calendar year so that the expected result changes depending on when the test is run.

| Test | Requirement(s) | Current Year | User Input | Expected Result | Pass Criteria |
| ---- | -------------- | -----------: | ---------- | --------------- | ------------- |
| 1. Typical adult age | 1.1–1.5 | 2026 | Name: `Jordan`; Age: `25` | `Hello Jordan! You were born in 2001.` | The program accepts both inputs, calculates `2001`, and displays the expected personalized result. |
| 2. Different adult name and age | 1.1–1.5 | 2026 | Name: `Casey`; Age: `42` | `Hello Casey! You were born in 1984.` | The program uses the entered values rather than values specific to Test 1 and displays the correct result. |
| 3. Zero age edge case | 1.1–1.5 | 2026 | Name: `Morgan`; Age: `0` | `Hello Morgan! You were born in 2026.` | The program correctly performs the required calculation when the age is zero. |
| 4. Negative age edge case | 1.1–1.5 | 2026 | Name: `Riley`; Age: `-5` | `Hello Riley! You were born in 2031.` | The program applies the required calculation to a negative integer without adding input-validation behavior that is not required by the assignment. |
| 5. Age over 100 edge case | 1.1–1.5 | 2026 | Name: `Taylor`; Age: `105` | `Hello Taylor! You were born in 1921.` | The program correctly performs the required calculation for an age greater than 100. |

Invalid-input test cases are not included because the assignment does not require the program to validate or recover from invalid user input.
