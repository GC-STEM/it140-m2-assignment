# Software Design Document

- **Course**: IT 140 - Introduction to Scripting
- **Activity**: {{ModNum}}-{{ActNum}}: {{ActivityTitle}}
- **Program Name**: {{Program-Name}}

## 0. General Description

{{TODO: Replace with a brief description of the planned solution. Explain how the design will meet the Software Requirements Specification (SRS), who will use the program, and the program's main purpose. Focus on how the program will be organized rather than repeating all requirements.}}

## 1. Design Goals and Constraints

The design shall:

- [ ] 1.1 {{TODO: Replace with the main design goal, such as keeping the solution simple, readable, and appropriate for the course module.}}

- [ ] 1.2 {{TODO: Replace with important design constraints derived from the SRS and the assignment guidelines and rubric (G&R), such as required programming concepts, file structure, libraries, or input and output rules.}}

- [ ] 1.x {{TODO: Add any activity-specific design goals or constraints.}}

## 2. Solution Overview

{{TODO: Describe the solution at a high level. Summarize the major steps the program will perform from start to finish. Identify the design approach used, such as a sequence of steps, function-oriented design, object-oriented design, event-driven design, or another approach appropriate for the activity.}}

### Design Artifacts

- **Flowchart**: [`activity_name.drawio`](./activity_name.drawio)
- **Pseudocode**: [`activity_name.pseudo`](./activity_name.pseudo)

{{TODO: Confirm that the flowchart and pseudocode represent the same planned solution described in this document.}}

## 3. Program Structure

{{TODO: Divide the program into logical components. A component may be the main program, a function, a class, or another meaningful section of the solution. Use only the component types introduced in the course by this activity.}}

| # | Component | Responsibility | Input | Output | SRS Requirement(s) |
| - | --------- | -------------- | ----- | ------ | ------------------ |
| 1 | {{TODO: Name}} | {{TODO: State what this component does}} | {{TODO: Identify data received}} | {{TODO: Identify data produced or returned}} | {{TODO: Add requirement ID(s)}} |

## 4. Data Design

{{TODO: Identify the important data the program will use. Include only data that helps explain the design, such as key variables, constants, collections, objects, or files. Use clear and descriptive planned names.}}

| # | Data Name | Type or Structure | Purpose | Initial Value or Source | Valid Values or Rules |
| - | --------- | ----------------- | ------- | ----------------------- | --------------------- |
| 1 | {{TODO: Name}} | {{TODO: Type}} | {{TODO: Purpose}} | {{TODO: Initial value or source}} | {{TODO: Valid values, range, or format}} |

## 5. Interface and Input/Output Design

{{TODO: Describe how users or other systems will interact with the program. Include prompts, expected input, validation rules, output formatting, files, application programming interfaces (APIs), or hardware interfaces as applicable. Refer to the SRS sample input and output rather than copying it unless additional design detail is needed.}}

| # | Interface or I/O Element | Source or Destination | Format | Validation or Processing | Related Requirement(s) |
| - | ------------------------ | --------------------- | ------ | ------------------------ | ---------------------- |
| 1 | {{TODO: Prompt, output, file, API, or device}} | {{TODO: User, file, system, or device}} | {{TODO: Expected format}} | {{TODO: Validation or processing rule}} | {{TODO: Add requirement ID(s)}} |

## 6. Program Logic and Control Flow

{{TODO: Explain the program's behavioral design. Describe the planned sequence, decisions, loops, function calls, events, or state changes. The description must be consistent with the flowchart and pseudocode.}}

### 6.1 Main Processing Steps

1. {{TODO: Describe the first major processing step.}}
2. {{TODO: Describe the next major processing step.}}
3. {{TODO: Continue until the program reaches its expected end state.}}

### 6.2 Decisions and Repetition

- **Decisions**: {{TODO: Identify important conditions and the action taken for each possible result.}}
- **Repetition**: {{TODO: Identify any repeated processing, its stopping condition, and how the design prevents an unintended infinite loop. Delete if not applicable.}}

## 7. Error and Exception Handling

{{TODO: Describe how the design will prevent, detect, and respond to invalid input, missing data, unavailable resources, or other expected errors. Keep the strategy appropriate for the course module and the requirements.}}

| # | Error or Invalid Condition | Detection Method | Planned Response | Related Requirement(s) |
| - | -------------------------- | ---------------- | ---------------- | ---------------------- |
| 1 | {{TODO: Condition}} | {{TODO: How the program detects it}} | {{TODO: Message, correction, retry, or safe exit}} | {{TODO: Add requirement ID(s)}} |

## 8. Design Decisions and Rationale

{{TODO: Record the most important design choices and explain why each choice is appropriate. Consider simplicity, readability, maintainability, correctness, usability, security, performance, or reuse as applicable. Include meaningful alternatives that were considered when relevant.}}

| # | Design Decision | Rationale | Alternative Considered |
| - | --------------- | --------- | ---------------------- |
| 1 | {{TODO: Decision}} | {{TODO: Explain how this choice supports the requirements and design goals}} | {{TODO: Alternative or "None"}} |

## 9. Requirements Traceability

{{TODO: Show how each SRS requirement is addressed by the design. Every applicable functional requirement and constraint should connect to at least one design component or artifact.}}

| SRS Requirement | Design Component or Section | Supporting Artifact |
| --------------- | --------------------------- | ------------------- |
| {{TODO: Requirement ID}} | {{TODO: Component name or SDD section}} | {{TODO: Flowchart step, pseudocode section, or other artifact}} |

## 10. Design Review Checklist

Before beginning construction, confirm that:

- [ ] 10.1 The design addresses every applicable SRS requirement.
- [ ] 10.2 The program structure separates the solution into clear, manageable parts.
- [ ] 10.3 The data names, types, sources, and validation rules are defined.
- [ ] 10.4 The input, processing, and output steps are complete and consistent.
- [ ] 10.5 Decisions, loops, functions, events, or state changes are described as applicable.
- [ ] 10.6 Expected errors and invalid inputs have planned responses.
- [ ] 10.7 The SDD, flowchart, and pseudocode describe the same solution.
- [ ] 10.8 The design is simple enough to implement using concepts introduced by this activity.
- [ ] 10.9 The design can be tested using the SRS acceptance test cases.
- [ ] 10.x {{TODO: Add any activity-specific design review checks derived from the G&R.}}

## 11. References

{{TODO: List any references in APA7 Style used to create the design, such as the SRS, assignment guidelines, textbooks, or online resources.}}