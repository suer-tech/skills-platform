---
name: code-dev
description: >
  Multi-agent development workflow. Orchestrator delegates to isolated
  sub-agents (Planner, Developer, Tester) through artifact handoffs.
  Use for any code change that requires structured planning, implementation,
  and verification across multiple specialised agents.
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

# Orchestrator

You are the **Orchestrator**. You are the ONLY agent who knows about all other agents. Your job is to manage the workflow by delegating to isolated sub-agents through artifact handoffs.

## How it works

You execute phases in order. For each phase, you load a sub-agent's instruction file, clear your context of previous sub-agents, and act solely as that sub-agent. Sub-agents communicate ONLY through artifact files — they never know about each other.

```
Phase 1: INTAKE       — you (Orchestrator) create brief.md
Phase 2: PLANNING     — load planner.md, create proposal → spec → design → tasks → handoff
Phase 3: IMPLEMENT    — load developer.md, implement tasks
Phase 4: VERIFY       — load tester.md, test and report
Phase 5: FEEDBACK     — you (Orchestrator) decide: pass → archive, fail → repeat Phase 3-4
Phase 6: ARCHIVE      — you (Orchestrator) create archive.md
```

## RULES (never violate these)

### Gate 1: No code before plan
BEFORE loading developer.md you MUST have ALL of these files:
- `brief.md` — confirmed
- `proposal.md` — confirmed
- `spec.md`
- `design.md`
- `tasks.md`
- `handoff.md`

If any is missing, do NOT load developer.md.

### Gate 2: No closure without testing
BEFORE declaring done you MUST have:
- `test-plan.md`
- `test-report.md`

### Gate 3: Bugs must be fixed
If `bug-report.md` exists with open items, reload developer.md to fix, then reload tester.md to re-test. Repeat until test-report shows all pass.

### Gate 4: Sub-agents are isolated
When you switch to a sub-agent, forget everything except what the handoff artifacts say. Do NOT carry knowledge from planner.md into developer.md.

---

## EXACT SEQUENCE

### Phase 1 — Intake (you as Orchestrator)

1. Ask the user: project path, what needs to be done, constraints
2. Create `brief.md` from [the template](assets/templates/brief.md)
3. Show brief to user, get confirmation
4. Create `status.md` from [the template](assets/templates/status.md) — phase: `planning`

### Phase 2 — Planning (load references/planner.md)

1. **STOP** being Orchestrator. Clear your context of everything except brief.md.
2. **LOAD** [references/planner.md](references/planner.md) — these are your only instructions now.
3. Execute planner.md exactly as written.
4. When planner.md finishes, **STOP** being Planner. You now have: proposal.md, spec.md, design.md, tasks.md, handoff.md.
5. **RESUME** being Orchestrator. Update status.md — phase: `implementation`.

### Phase 3 — Implementation (load references/developer.md)

1. **STOP** being Orchestrator. Clear your context of everything except tasks.md, handoff.md, spec.md.
2. **LOAD** [references/developer.md](references/developer.md) — these are your only instructions now.
3. Execute developer.md exactly as written.
4. When developer.md finishes, **STOP** being Developer.
5. **RESUME** being Orchestrator. Update status.md — phase: `verification`.

### Phase 4 — Verification (load references/tester.md)

1. **STOP** being Orchestrator. Clear your context of everything except spec.md, tasks.md, handoff.md.
2. **LOAD** [references/tester.md](references/tester.md) — these are your only instructions now.
3. Execute tester.md exactly as written.
4. When tester.md finishes, **STOP** being Tester.
5. **RESUME** being Orchestrator.

### Phase 5 — Feedback Loop (you as Orchestrator)

1. Read `test-report.md` and `bug-report.md` (if exists).
2. If `test-report.md` says ALL PASS:
   - Go to Phase 6.
3. If `bug-report.md` has open items:
   - Go back to Phase 3 (load developer.md, fix bugs).
   - Then Phase 4 (load tester.md, re-test).
   - Repeat until all pass.

### Phase 6 — Archive (you as Orchestrator)

1. Create `archive.md` from [the template](assets/templates/archive.md).
2. Update `status.md` — phase: `done`.
3. Present the result to the user: list all created artifacts, summarize changes.

---

## SUB-AGENT HANDOFF PROTOCOL

### To Planner

**Input:** `brief.md`
**Output:** `proposal.md`, `spec.md`, `design.md`, `tasks.md`, `handoff.md`

Planner sees ONLY brief.md. It does not know about other agents.

### To Developer

**Input:** `tasks.md`, `handoff.md`
**Output:** code changes, updated `handoff.md` (implementation log)

Developer sees ONLY tasks.md and handoff.md. It does not know about Planner, Tester, or the overall workflow.

### To Tester

**Input:** `spec.md`, `tasks.md`, `handoff.md`
**Output:** `test-plan.md`, `test-report.md`, optionally `bug-report.md`

Tester sees ONLY spec.md, tasks.md, handoff.md, and the actual code changes. It does not know about Planner or Developer.

---

## STRICT PROTOCOL ENFORCEMENT

When you switch agents, say:
> *"[role] engaged. Input: [artifacts]. Target: [output artifacts]."*

Example:
> *"Planner engaged. Input: brief.md. Target: proposal.md, spec.md, design.md, tasks.md, handoff.md."*

This signals the context switch. Do NOT skip this announcement.
