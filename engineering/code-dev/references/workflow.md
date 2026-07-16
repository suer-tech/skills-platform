# Workflow Diagram

Reference for Orchestrator. Not for sub-agents.

## Agent Isolation

```
Orchestrator ──brief.md──► Planner ──proposal.md──► Orchestrator
                                          spec.md
                                         design.md
                                         tasks.md
                                         handoff.md

Orchestrator ──tasks.md──► Developer ──code changes──► Orchestrator
               handoff.md    │          handoff.md (log)
                             │
                             └──► (if bugs) bug-report.md

Orchestrator ──spec.md────► Tester ──test-plan.md──► Orchestrator
               tasks.md              test-report.md
               handoff.md            bug-report.md (optional)
```

## Communication Matrix

| Agent | Reads | Writes |
|-------|-------|--------|
| Orchestrator | all artifacts | brief.md, status.md, archive.md |
| Planner | brief.md | proposal.md, spec.md, design.md, tasks.md, handoff.md |
| Developer | tasks.md, handoff.md | code changes, handoff.md (log) |
| Tester | spec.md, tasks.md, handoff.md | test-plan.md, test-report.md, bug-report.md |

## State Machine

```
INTAKE ──► PLANNING ──► IMPLEMENT ──► VERIFY ──► ──► ARCHIVE
                              ▲                  │
                              └── (bugs) ◄───────┘
```
