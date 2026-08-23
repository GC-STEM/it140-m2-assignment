<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# IT 140 Module Two Assignment | Start Here

- **Course:** IT 140 - *Introduction to Scripting*
- **Activity:** 2-3 Module Two Assignment
- **Activity Type:** Required, graded, with two submissions
  - **Part A:** Name and Age Program (`name_age.py`)
  - **Part B:** IDE Features Reflection (`ide_features.md`)

**Assignment progress:** **0 Start Here** → [1 Part A](./Part-A/README.md) → [2 Part B](./Part-B/README.md) → [3 Submit](#submit-your-assignment)

## Table of Contents

- [IT 140 Module Two Assignment | Start Here](#it-140-module-two-assignment--start-here)
  - [Table of Contents](#table-of-contents)
  - [0. Meet the Prerequisites](#0-meet-the-prerequisites)
  - [1. Setup the Assignment](#1-setup-the-assignment)
  - [2. Complete the Assignment](#2-complete-the-assignment)
  - [3. Submit Your Assignment](#3-submit-your-assignment)
  - [4. Get Help and Support](#4-get-help-and-support)

## 0. Meet the Prerequisites

- [ ] **Required**. To start this assignment, you must have completed the [GitHub](https://github.com/GC-STEM/it140-m1-setup-tasks/tree/main/github) and [Codio](https://github.com/GC-STEM/it140-m1-setup-tasks/tree/main/codio) sections of the [Module One Setup Tasks](https://github.com/GC-STEM/it140-m1-setup-tasks). If you have not done so, please complete those tasks now. Return here after completing those tasks.

- [ ] **Recommended**. Complete all Module One and Two zyBooks activities (Participation and Lab) in [D2L Brightspace](https://learn.snhu.edu/). These activities introduce you to the skills you will use in this assignment.

## 1. Setup the Assignment

We strongly recommend that you complete this first assignment using the Codio Virtual Desktop (CVD). The CVD provides a consistent user experience regardless of your local computer's operating system.

1. Launch the CVD now and carry out the remaining instructions from within the CVD.

2. Open a browser and point it to the [Module Two Assignment Repository](https://github.com/GC-STEM/it140-m2-assignment).

3. Open a terminal window.

4. Arrange your screen so that you can see both this browser and the terminal window at the same time.

5. In the CVD terminal window, type `update_it140.sh` and press **Enter**. This will update the course IDE to the latest version. If using a local computer, type the appropriate update script name for your operating system:
   - Windows: `update_it140.ps1`
   - macOS  : `update_it140.zsh`
   - Linux  : `update_it140.sh`

6. Copy the following command block and paste it into a new terminal window. Press **Enter** to run.

    ```bash
    cd ~/Repos 
    gh auth setup-git 
    gh api --method PUT /user/starred/GC-STEM/it140-m2-assignment 
    gh repo create it140-m2-assignment --template GC-STEM/it140-m2-assignment --private --clone 
    cd it140-m2-assignment
    git remote -v
    ```

7. Review the output of the last command. You should see two lines that look like this:

## 2. Complete the Assignment

1. In a terminal window, copy and paste the following command to open the assignment repository in VS Code. Press **Enter** to run.

    ```bash
    code ~/Repos/it140-m2-assignment
    ```

2. Right-click the `README.md` file in the **Explorer** pane of VS Code and choose **Open to the side**. This will open a clean, formatted view of this same README file in VS Code.

3. Click on the **> Part-A** folder in the **Explorer** pane of VS Code to expand it so you see its contents.

4. Click [here](./Part-A/README.md) to open the `Part-A/README.md`.

    1. Click anywhere in the **Welcome** tab of VS Code to make it active.
    2. In the **Explorer** pane of VS Code, expand the `Part-A` folder.
    3. 
    4. Follow the step-by-step instructions to complete the `name_age.py` program.
    5. When done, 

## 3. Submit Your Assignment

After completing Part A and Part B, return to the *Module Two Assignment Guidelines and Rubric* in [D2L Brightspace](https://learn.snhu.edu/).

Confirm that:

- You completed all required Part A work.
- You completed all required Part B work.
- Your work meets the grading rubric criteria.
- You are submitting the correct files and file formats.
- Your final files are saved.
- Your latest work is backed up in your personal GitHub repository.

Follow the **What to Submit** instructions in the *Module Two Assignment Guidelines and Rubric* to submit your assignment in D2L Brightspace.

Do not submit working files, provided design documents, test files, README files, or your GitHub repository unless the Module Two Assignment Guidelines and Rubric specifically instruct you to do so.

**GitHub does not submit your assignment for grading.**

## 4. Get Help and Support
