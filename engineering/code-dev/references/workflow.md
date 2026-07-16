# Workflow Reference

Полное описание жизненного цикла. Для быстрого ориентирования.

## Pipeline

```
User Request
    │
    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  PHASE 1: INTAKE                      Actor: Orchestrator           │
│  ─────────────────────────────────────────────────────────────────── │
│  Записать brief.md                                                   │
└─────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  PHASE 2: PLANNING                    Actor: Planner                │
│  ─────────────────────────────────────────────────────────────────── │
│  proposal.md → spec.md → design.md → tasks.md → handoff.md          │
└─────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  PHASE 3: IMPLEMENTATION              Actor: Developer              │
│  ─────────────────────────────────────────────────────────────────── │
│  Выполнить tasks.md, изменения в коде, status.md                    │
└─────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  PHASE 4: VERIFICATION                Actor: Tester                 │
│  ─────────────────────────────────────────────────────────────────── │
│  test-plan.md → test-report.md → bug-report.md (если дефекты)       │
└─────────────────────────────────────────────────────────────────────┘
    │
    ├── pass ─────────────────────────────────────────► PHASE 6
    │
    └── fail ───► PHASE 5: FEEDBACK LOOP
                      Actor: Orchestrator → Developer → Tester
                      └── повторять, пока pass
    │
    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  PHASE 6: CLOSURE                      Actor: Orchestrator          │
│  ─────────────────────────────────────────────────────────────────── │
│  archive.md, status.md → done, финальный ответ пользователю          │
└─────────────────────────────────────────────────────────────────────┘
```

## Artefact Dependencies

```
brief.md        → proposal.md
proposal.md     → spec.md
spec.md         → design.md + tasks.md
tasks.md        → handoff.md
handoff.md      → implementation (Developer)
                → verification (Tester)
test-report.md  → archive.md (если pass)
                → bug-report.md → Developer (если fail)
bug-report.md   → fix → re-test → test-report.md
```

## Status File

`status.md` — единственный источник правды о текущем состоянии.

```markdown
# Status

## Phase
planning | implementation | verification | done

## Current Task
Task ID or "—"

## Iteration
1, 2, 3...

## Blockers
—

## Last Updated
YYYY-MM-DD HH:MM
```
