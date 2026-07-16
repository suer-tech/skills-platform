---
name: code-dev
description: >
  End-to-end development workflow with mandatory artifact creation.
  Use for ANY code change: it forces you to plan, spec, design, implement,
  test, and archive — in that order, with checkable artifacts at each step.
metadata:
  id: engineering.code-dev
  version: "0.1.0"
  category: engineering
  author: skills-platform
  inputs:
    request:
      required: true
      description: "What needs to be done"
    project_path:
      required: true
      description: "Path to the project"
  outputs:
    artifacts:
      type: files
      description: "All created artifacts (brief, proposal, spec, design, tasks, reports, archive)"
  capabilities:
    - spec_driven_development
    - multi_agent_orchestration
    - project_planning
    - spec_generation
    - task_decomposition
    - code_implementation
    - testing
    - bug_detection
    - iterative_refinement
    - documentation_generation
---

# Code Development — Strict Protocol

## RULES (you MUST follow every rule)

### Gate 1: No code before plan
YOU MUST create ALL of these files BEFORE writing any code:
1. `brief.md`
2. `proposal.md`
3. `spec.md`
4. `design.md`
5. `tasks.md`
6. `handoff.md`

If any of these files does not exist, you are NOT allowed to write code.

### Gate 2: No closure without testing
YOU MUST create ALL of these files BEFORE declaring done:
1. `test-plan.md`
2. `test-report.md`
3. `archive.md`

### Gate 3: Bugs must be fixed
If `bug-report.md` exists and has open items, you MUST fix them and re-test. Do NOT skip to archive.

### Gate 4: One file at a time
Create files in the order listed below. Do NOT skip ahead.

---

## EXACT SEQUENCE

### Step 1 — brief.md

Create `brief.md` from [the template](assets/templates/brief.md).

Fill in: project name, goal, scope, constraints. Ask the user questions if anything is unclear. Show the brief to the user and get confirmation before proceeding.

### Step 2 — proposal.md

Create `proposal.md` from [the template](assets/templates/proposal.md).

List at least 2 solution options. Explain pros/cons. Recommend one. Show to user and get confirmation.

### Step 3 — spec.md

Create `spec.md` from [the template](assets/templates/spec.md).

Write functional requirements with acceptance criteria. Each requirement must be testable. Mark any unknowns as `TODO / NEEDS CONFIRMATION`.

### Step 4 — design.md

Create `design.md` from [the template](assets/templates/design.md).

Describe architecture, components, data flow, and file changes. Be specific about which files will be modified.

### Step 5 — tasks.md

Create `tasks.md` from [the template](assets/templates/tasks.md).

Decompose the work into atomic tasks. Each task must have: scope, files, dependencies, acceptance criteria. Tasks must be small enough that one agent can complete one task in a single session.

### Step 6 — handoff.md

Create `handoff.md` from [the template](assets/templates/handoff.md).

Summarize what will be implemented. Include all tasks and acceptance criteria. This is the implementation plan.

### Step 7 — status.md

Create `status.md` from [the template](assets/templates/status.md).

Set phase to `implementation`. Mark which tasks are pending.

### Step 8 — Implementation

Implement tasks ONE BY ONE from `tasks.md`. After each task, update `status.md` and `handoff.md` (implementation log).

Do NOT modify files outside the task scope. Do NOT skip tasks.

### Step 9 — test-plan.md

Create `test-plan.md` from [the template](assets/templates/test-plan.md).

Write test cases covering all acceptance criteria from spec.md.

### Step 10 — test-report.md

Create `test-report.md` from [the template](assets/templates/test-report.md).

Execute the test plan. Record pass/fail for each test case.

### Step 11 — bug-report.md (if needed)

If any tests fail, create `bug-report.md` from [the template](assets/templates/bug-report.md).

List each defect with severity. Go back to Step 8, fix the bugs, then re-test (repeat Step 9-11 until all pass).

### Step 12 — archive.md

Create `archive.md` from [the template](assets/templates/archive.md).

Summarize everything: what was changed, test results, lessons learned, follow-up tasks.

Update `status.md` — phase: `done`.

---

## ROLES (switch between them)

This skill defines 4 roles. YOU play all of them, one at a time, in order:

| Step | Role | What you do |
|------|------|-------------|
| 1–2 | **Orchestrator** | Talk to user, gather context, confirm |
| 2–6 | **Planner** | Research, plan, decompose |
| 7–8 | **Developer** | Write code, update artifacts |
| 9–11 | **Tester** | Test, report bugs, verify fixes |
| 12 | **Orchestrator** | Archive and deliver |

When you switch roles, say which role you are now playing. Example: *"Switching to Tester role — writing test-plan.md"*

---

## ARTEFACT CHECKLIST (final verification)

Before declaring done, verify ALL of these exist:

- [ ] `brief.md` — confirmed by user
- [ ] `proposal.md` — confirmed by user
- [ ] `spec.md` — requirements + acceptance criteria
- [ ] `design.md` — architecture + file changes
- [ ] `tasks.md` — atomic tasks
- [ ] `handoff.md` — implementation plan + log
- [ ] `status.md` — phase tracking
- [ ] `test-plan.md` — test cases
- [ ] `test-report.md` — results
- [ ] `archive.md` — final summary

If any file is missing, you are NOT done.
