<!-- To see this file in a clean, formatted view, select "Text Editor ▼" in the upper-right corner of the editor, then select "Markdown Preview". -->

# IT 140 Module Two Assignment | Software Development Introduction

---

> [!IMPORTANT]
> **GitHub repository options**
>
> **Do not select Fork or Use this template.** These options will interfere with the repository setup commands later in this README.
>
> - 🚫 **Fork — Do not use**
> - 🚫 **Use this template — Do not use**
> - ⭐ **Star** — The setup commands later in this README will bookmark this repository for you.
> - 👁️ **Watch**
>   - **Students:** Not recommended. Watching is not needed and may generate unnecessary notifications.
>   - **Faculty:** Consider selecting **Watch → Custom → Releases + Issues** to receive major repository updates and follow reported issues.

---

> [!NOTE]
> **🆕 New for 2026 C-5:** IT 140 now uses GitHub repositories to provide assignment starter files, development resources, and supporting documentation.
>
> If you find a problem with this GitHub repository or its instructions, or have a suggestion for improvement, please open [GitHub Issues](https://github.com/GC-STEM/it140-m2-assignment/issues) to review existing issues or create a new issue.

---

- **Course**: IT 140 - *Introduction to Scripting*
- **Task Title**: 2-3: Software Development Introduction
- **Task Type**: Required, graded, one submission required
- **Repository Version**: 1.0.3
- **Repository Version DTG**: 2026-09-02-09-37

<!-- omit from toc -->
## Table of Contents

Complete the following tasks in order to complete the Module Two assignment. Each task is described in detail below.

- [0. Meet the Prerequisites](#0-meet-the-prerequisites)
- [1. Setup the Assignment](#1-setup-the-assignment)
- [2. Complete Part A](#2-complete-part-a)
- [3. Complete Part B](#3-complete-part-b)
- [4. Submit Your Assignment](#4-submit-your-assignment)
- [Get Help and Support](#get-help-and-support)

## 0. Meet the Prerequisites

- [ ] **Required**. To start this assignment, you must have completed the [GitHub](https://github.com/GC-STEM/it140-m1-setup-tasks/tree/main/github) and [Codio](https://github.com/GC-STEM/it140-m1-setup-tasks/tree/main/codio) sections of the [Module One Setup Tasks](https://github.com/GC-STEM/it140-m1-setup-tasks). If you have not done so, please complete those tasks now. Return here after completing those tasks.

- [ ] **Recommended**. Complete all Module One and Two zyBooks activities (Participation and Lab) in [D2L Brightspace](https://learn.snhu.edu/). These activities introduce you to the skills you will use in this assignment.

## 1. Setup the Assignment

We strongly recommend that you complete this first assignment using the Codio Virtual Desktop (CVD). The CVD provides a consistent user experience regardless of your local computer's operating system. If you do choose to use your local computer, start at Step 2 below.

1. Launch the CVD now and carry out the remaining instructions from within the CVD.
   - If you bookmarked the CVD, open that link.
   - If not, open the CVD from within [D2L Brightspace](https://learn.snhu.edu/). Follow the [Launch the CVD](https://github.com/GC-STEM/it140-m1-setup-tasks/blob/main/codio/README.md#1-launch-the-cvd) instructions if you need a refresher.

2. Click the browser icon on the taskbar to open a browser. Then, point the browser to `https://github.com/GC-STEM/it140-m2-assignment`. Arrange the browser window on one side of your screen, as shown below.

3. Click the terminal icon on the taskbar to open a terminal window. Arrange it on the other side of your screen from the browser window, as shown below.

   ![Terminal and browser window in split screen](./.github/assets/13_split_screen_terminal_browser.png)

4. In the CVD terminal window, type `update_it140.sh` and press **Enter**. This will update the course IDE to the latest version. Be patient. It may take a few minutes to complete. If using a local computer, use the appropriate script extension for your operating system:
   - Windows: `update_it140.ps1`
   - macOS  : `update_it140.zsh`
   - Linux  : `update_it140.sh`

5. Review the output of the update script. You are mainly interested in `Failures: 0` and the `Restart required:` message.
   - If `Failures` is greater than `0`, review the [**Get Help and Support**](#get-help-and-support) section.
   - If `Restart required: No`, type `exit` and press **Enter** to close the terminal window.
   - If `Restart required: Yes`, click the **RESTART VM** button on the Codio taskbar and wait for the CVD to restart.

   ![Update summary in split screen](./.github/assets/15_split_screen_update_summary.png)

6. Open a new terminal window and copy the following command block and paste it into the new terminal window. If prompted about a "Potentially Unsafe Paste", click the **Paste** button. Press **Enter** to run the commands.

    ```bash
    cd ~/Repos
    gh auth setup-git
    gh api --method PUT /user/starred/GC-STEM/it140-m2-assignment
    gh repo create it140-m2-assignment --template GC-STEM/it140-m2-assignment --private --clone
    cd it140-m2-assignment
    git remote -v
    ```

    *Note*. The above commands only work the first time you run them successfully. If you want to update your repository later or start over, see the [**Get Help and Support**](#get-help-and-support) section.

7. Review the output of the last command. You should see output similar to the what is shown below, except with your GitHub username in place of `petey-penmen`.

   ![Git remote output](./.github/assets/17_gh_repo_setup.png)

8. Determine if you want to continue to Part A now or if you want to stop and continue later.
   - If you want to continue to Part A now, type `code .` and press **Enter**. Skip to Step 3 in **2. Complete Part A**.
   - If done for now, type `exit` and press **Enter** to close the terminal window. Bookmark the CVD page in your local browser, if you have not already, so you can return to it later without going through D2L Brightspace.

## 2. Complete Part A

1. Launch the CVD and carry out the remaining instructions from within the CVD.

2. Open a terminal window. Copy and paste the following command to open the assignment repository in VS Code. Press **Enter** to run.

    ```bash
    code ~/Repos/it140-m2-assignment
    ```

   *Reminder*. **Path shortcuts**: In terminal commands, **`~`** means your home folder, and **`.`** means your current folder. For example:
     - `cd ~/Repos` means change directory to the `Repos` folder inside your home folder.
     - `code .` opens the current folder in VS Code.

3. If the **Chat** pane opens in VS Code, click the **X** in the upper right corner for that pane to close it. Do NOT click the **X** to close the entire VS Code window right above it.

   ![Close Chat pane in VS Code](./.github/assets/23_vscode_close_chat_pane.png)

4. In the **Explorer** pane of VS Code"
   - Click **> it140-m2-assignment** to expand the folder, if needed.
   - Click **> Part-A** to expand the folder, if needed.

   ![Expand Part-A folder in VS Code](./.github/assets/24_vscode_explorer_expand.png)

5. Right-click on the `Part-A/README.md` file and select **Open to the Side**.

   ![Open Part-A README to the Side in VS Code](./.github/assets/25_vscode_explorer_open_side.png)

6. You will now follow instructions in the `Part-A/README.md` file. When ready, maximize the VS Code window by clicking the **Maximize** button in the upper right corner of the VS Code window. Look for the green box in the previous screenshot.

## 3. Complete Part B

1. If not already running, launch the CVD and carry out the remaining instructions from within the CVD.

2. Open a terminal window. Copy and paste the following command to open the assignment repository in VS Code. Press **Enter** to run.

    ```bash
    code ~/Repos/it140-m2-assignment
    ```

3. If the **Chat** pane opens in VS Code, click the **X** in the upper right corner for that pane to close it. Do NOT click the **X** to close the entire VS Code window.

   ![Close Chat pane in VS Code](./.github/assets/23_vscode_close_chat_pane.png)

4. In the **Explorer** pane of VS Code"
   - Click **> it140-m2-assignment** to expand the folder, if needed.
   - Click **> Part-B** to expand the folder, if needed.

   ![Expand Part-B folder in VS Code](./.github/assets/34_vscode_explorer_expand.png)

5. Right-click on the `Part-B/README.md` file and select **Open to the Side**.

   ![Open Part-B README to the Side in VS Code](./.github/assets/35_vscode_explorer_open_side.png)

6. You will now follow instructions in the `Part-B/README.md` file. When ready, maximize the VS Code window by clicking the **Maximize** button in the upper right corner of the VS Code window right above it. Look for the green box in the previous screenshot.

## 4. Submit Your Assignment

In your IT 140 course in [D2L Brightspace](https://learn.snhu.edu/), go to the **Course Menu** and select **Assignments**. Click on the **2-3 Assignment: Software Development Introduction** link. Follow the instructions to submit your assignment. Submit the following files in Brightspace as one submission:

- Graded files:
  - [`name_age.py`](./Part-A/src/name_age.py)
  - [`ide_features.md`](./Part-B/ide_features.md)

- Ungraded files:
  - [`name_age_sdw.md`](./Part-A/name_age_sdw.md)

## Get Help and Support

### The course IDE Update reports a failure

If Step 5 reports `Failures` greater than `0`, stop before continuing to Step 6. Follow the **Action required** and **Next step** shown in the Update summary.

If the problem is not resolved, see **[Setup Problems and Support](https://github.com/GC-STEM/it140-m1-setup-tasks/wiki/Setup-Problems-and-Support)**. That page explains what information to collect and where to ask for help with course IDE setup and lifecycle-script problems.

Before asking for help, save the exact Update summary and error message. The lifecycle scripts also save a diagnostic log under `~/it140/logs/` or the corresponding `it140/logs` folder in your user profile.

> [!WARNING]
> Do not attempt manual `sudo`, package-manager, system, or course-file repairs unless the course instructions or technical support specifically direct you to do so.

### Your Module Two assignment already exists somewhere

Your Module Two assignment will have several related copies:

- **Public course template on GitHub:** `GC-STEM/it140-m2-assignment`. This is the course-provided starting point. You cannot modify this copy.

- **Your personal GitHub repository:** `it140-m2-assignment` in your own GitHub account. This stores the work you "push" (upload) to GitHub.

- **A local clone on a device:** Usually `~/Repos/it140-m2-assignment` on the CVD or your local computer. This is the copy you open in VS Code and edit.

Step 6 creates your personal GitHub repository and then creates a local clone on the device where you run the commands.

Choose the situation below that matches what you see.

#### Your personal GitHub repository and local clone both exist on this device

For example, you created your personal GitHub repository while working on the CVD, and `~/Repos/it140-m2-assignment` also exists on that CVD.

Do not run the Step 6 setup commands again.

Open the local clone on your current device:

```bash
code ~/Repos/it140-m2-assignment
```

#### Your personal GitHub repository exists, but there is no local clone on this device

For example, you created your personal GitHub repository and local clone on the CVD, but now you are using your local computer for the first time.

Do **not** create another personal GitHub repository from the public course template.

Instead, create a local clone of your existing personal GitHub repository on the current device:

```bash
cd ~/Repos
gh auth setup-git
gh repo clone "$(gh api user --jq .login)/it140-m2-assignment"
cd it140-m2-assignment
git remote -v
```

Then open the new local clone on the current device in VS Code:

```bash
code .
```

#### A local clone exists on this device, but you are not sure about your personal GitHub repository

Do not delete the local clone on this device and do not run the Step 6 setup commands again. The local clone may contain assignment work that has not yet been pushed to your personal GitHub repository.

From the device that contains the local clone, run:

```bash
cd ~/Repos/it140-m2-assignment
git remote -v
```

This shows which GitHub repository the local clone is connected to.

If you are unsure what the output means, or your expected personal GitHub repository is missing, ask for help before deleting or replacing the local clone or anything in your GitHub account.

### Working on the assignment from more than one device

> [!IMPORTANT]
> **We highly recommend completing IT 140 work on just one device.** Using one device for the course helps avoid Git and GitHub complications that can occur when the same personal GitHub repository is cloned onto more than one device.
>
> If you are already comfortable working with Git and GitHub, you may work from more than one device. Follow the instructions below carefully to keep your copies synchronized.

A single personal GitHub repository can have a local clone on more than one device. For example:

- **First device:** Your CVD
- **Second device:** Your local computer

Before leaving the first device, save your changes in the local clone on that first device and push them to your personal GitHub repository.

**On the first device, before switching:**

```bash
cd ~/Repos/it140-m2-assignment
git status
git add -A
git commit -m "Save work before switching devices"
git push
```

After moving to the second device, update the local clone on that second device from your personal GitHub repository before making any new changes.

**On the second device, before starting work:**

```bash
cd ~/Repos/it140-m2-assignment
git pull --ff-only
git status
code .
```

> [!IMPORTANT]
> The second command block assumes that a local clone already exists on the second device. If there is no `~/Repos/it140-m2-assignment` folder on the second device, follow **Your personal GitHub repository exists, but there is no local clone on this device** above instead.

If `git push` on the first device or `git pull --ff-only` on the second device reports an error, stop and ask for help before making additional changes on either device.

### You intentionally want to start over

Starting over may involve one or more separate copies:

- Your **personal GitHub repository** in your GitHub account
- Your **local clone on your CVD**
- Your **local clone on your local computer**

Deleting one copy does not necessarily delete the others.

Before deleting or replacing anything, make sure you have saved any work you want to keep. If you have already started the assignment or are unsure which copy is safe to replace, ask for help before continuing.

For more information about these different copies, see **[Course Repositories](https://github.com/GC-STEM/it140/wiki/Course-Repositories)**.

### Other technical problems

For a current course-wide technical problem, check **[Course Status](https://github.com/GC-STEM/it140/wiki/Course-Status)**.

If you find a problem with the **public course template or its instructions**, review existing reports or open a new **[GitHub Issue](https://github.com/GC-STEM/it140-m2-assignment/issues)**.

> [!WARNING]
> Never post passwords, authentication or verification codes, recovery codes, access tokens, private identifying information, or complete solutions to graded assignments in a public GitHub issue or discussion.
