# Contributing Guidelines

## Table of Contents
- [1. Git Guide](#1-git)
  - [Branch Structure](#branch-structure)
  - [Setup](#setup-first-time)
  - [Creating & Switching Branches](#creating--switching-branches)
  - [Keeping Your Branch Updated](#keeping-your-branch-updated)
  - [Committing & Pushing Changes](#committing--pushing-changes)
  - [Pulling the Latest Changes](#pulling-the-latest-changes-every-time-you-start)
  - [Merging & Creating Pull Request](#merging--creating-a-pull-request)
  - [Resolving Merge Conflicts](#resolving-merge-conflicts)
  - [Deleting a Merged Branch](#deleting-a-merged-branch)
  - [Branch Best Practices](#branch-best-practices)
- [2. Commit Message Guidelines](#2-commit-messages)
- [3. Comment Guidelines](#3-comments)


# 1. Git

## Branch Structure
- **main** – No direct commits.
- **feature-xxx** – Each feature has its own branch (e.g., `feature-upload`, `feature-ai`).
- **bugfix-xxx** – For fixing bugs (e.g., `bugfix-ui-fix`).
- **test-xxx** – For testing-related changes (e.g., `test-accessibility`).
- **dev** – Staging branch where feature branches are merged before `main`.

---

## Setup (First Time)
1. Clone the repository:
   ```sh
   git clone <repo-url>
   ```
2. Move into the project folder:
   ```sh
   cd project-folder
   ```
3. Check existing branches:
   ```sh
   git branch -r
   ```

---

## Creating & Switching Branches
1. Create a new feature branch from `dev`:
   ```sh
   git checkout dev
   git pull origin dev
   git checkout -b feature-xxx
   ```
2. Push the branch to remote:
   ```sh
   git push -u origin feature-xxx
   ```

---

## Keeping Your Branch Updated
1. Fetch latest changes:
   ```sh
   git fetch origin
   ```
2. Merge `dev` into your branch:
   ```sh
   git checkout feature-xxx
   git merge origin/dev
   ```
   *(Resolve conflicts if needed, then commit and push.)*

---

## Committing & Pushing Changes
 If through command line:
1. Check modified files:
   ```sh
   git status
   ```
2. Stage changes:
   ```sh
   git add .
   ```
3. Commit with a message:
   ```sh
   git commit -m "type(SCRUM-XXX): short description"
   ```
4. Push to remote:
   ```sh
   git push origin feature-xxx
   ```

---

## Pulling the Latest Changes (Every Time You Start)
1. Fetch latest changes:
   ```sh
   git fetch origin
   ```
2. Pull latest changes for `dev`:
   ```sh
   git checkout dev
   git pull origin dev
   ```
3. Pull latest changes for your feature branch:
   ```sh
   git checkout feature-xxx
   git pull origin feature-xxx
   ```

---

## Merging & Creating a Pull Request
1. Make sure your feature branch is **up to date** with `dev`:
   ```sh
   git checkout feature-xxx
   git merge origin/dev
   ```
2. Push any resolved conflicts:
   ```sh
   git push origin feature-xxx
   ```
3. Open a **Pull Request** in GitHub to merge `feature-xxx` → `dev`.
4. You can name your pull request the same as your commit message.
5. Review your pull request before merging.

### Merge Commit Guidelines

When merging a pull request, edit the default merge commit message to match the pull request title.

#### **How to Edit the Merge Commit Message:**
1. When merging a PR on GitHub, you’ll see a default message like:
   ```plaintext
   Merge pull request #X from user/branch
   ```
2. Edit it to match the PR title:
   ```plaintext
   type(SCRUM-XXX): short description
   ```

#### **Example:**
- Instead of:
  ```plaintext
  Merge pull request #2 from Shelly855/contributing-guide
  ```
- Use:
  ```plaintext
  docs(SCRUM-62): update instructions for deleting merged branch
  ```

---

## Resolving Merge Conflicts
1. When conflicts occur, Git will show a message after merging.
2. Open conflicted files in VS Code, look for:
   ```diff
   <<<<<<< HEAD
   (your branch's code)
   =======
   (incoming code from dev)
   >>>>>>> origin/dev
   ```
3. Choose the correct version, save the file.
4. Stage and commit:
   ```sh
   git add .
   git commit -m "Resolved merge conflicts"
   ```
5. Push changes:
   ```sh
   git push origin feature-xxx
   ```

---

## Deleting a Merged Branch
Once a branch is merged, it's good practice to delete it to keep the repository clean, **unless it's a long-lived branch** like `main` or `dev`, or if you need to continue working on the branch.

### 1. Use GitHub UI
- After merging a pull request, click the **"Delete branch"** button that GitHub provides. This will remove the branch from the remote repository.

### 2. Alternative Method: Delete Locally and Remotely
If you missed the GitHub UI button, you can manually delete the branch:

- **Delete locally:**
  ```sh
  git branch -d feature-xxx
  ```
  *(Replace `feature-xxx` with your branch name.)*

- **Delete remotely:**
  ```sh
  git push origin --delete feature-xxx
  ```
  *(This removes the branch from the remote repository.)*
---

## Branch Best Practices
- Pull latest changes **before starting work**.
- Always **merge `dev` into your branch** before creating a PR.  
- **Never push directly to `main`**  

---

# 2. Commit Messages
**Format:** `type(SCRUM-XXX): short description`

---

## Examples:
```text
feat(SCRUM-24): add edit button to profile page
fix(SCRUM-23): fix broken image on homepage
docs(SCRUM-45): update README with setup instructions
```
---

## General Rules
- Add **Jira issue key** (if applicable)
  - If no Jira issue is attached, you don't need to add a key
    - **Example:** `fix: resolve form validation error`
- Avoid including multiple unrelated changes in a single commit - when you've made a single change, commit it
- Start with a **verb** (e.g., `add`, `fix`, `update`)
- Use **lowercase**, except for Jira issue keys.
- No punctuation at the end
- Be **specific** but keep it **short**

---

## Commit Types
- **feat** – Adding a new feature.
  - Example: `feat(SCRUM-352): add search functionality`
  
- **fix** – Fixing a bug or issue.
  - Example: `fix(SCRUM-122): resolve form validation error`
    
- **docs** – Updating documentation (README, guides, inline comments).
  - Example: `docs(SCRUM-222): update API documentation`
    
- **refactor** – Restructuring code without changing functionality.
  - Example: `refactor(SCRUM-77): simplify function logic`
    
- **chore** – Maintenance tasks (e.g., dependency updates, build scripts).
  - Example: `chore(SCRUM-12): update npm dependencies`
    
- **test** - Adding or improving test cases, refactoring test structure.
  - Example: `test(SCRUM-100): add unit tests for authentication`
    
- **style** – Code formatting and whitespace fixes (no functional changes).
  - Example: `style(SCRUM-234): fix indentation`
    
- **build** – Changes related to build system, dependencies, or package managers.
  - Example: `build(SCRUM-67): upgrade Laravel to latest version`
    
- **perf** – Performance optimisations, improving speed and efficiency.
  - Example: `perf(SCRUM-45): enable gzip compression`
    
- **revert** – Reverting a previous commit.
  - Example: `revert(SCRUM-33): revert "feat: add checkout page"`

---

# 3. Comments
- Keep comments **short & up to date**
- Example:  
  ```js
  // Calculates the total cost of items in a cart
  ```
- Shortcut: Press **Ctrl + /** after selecting text or when the cursor is at the end of the line
