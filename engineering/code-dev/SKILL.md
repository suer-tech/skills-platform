---
name: code-dev
description: >
  End-to-end management of code changes through multi-agent orchestration.
  Use when a task requires planning, implementation, testing, and iterative
  refinement across multiple specialised AI agents.
metadata:
  id: engineering.code-dev
  version: "0.1.0"
  category: engineering
  author: skills-platform
  inputs:
    request:
      required: true
      description: "Описание запроса на разработку"
    project_path:
      required: true
      description: "Путь к проекту"
  outputs:
    archive:
      type: markdown
      description: "Финальный архив с итогами"
    artifacts:
      type: files
      description: "Все созданные артефакты (brief, spec, design, tasks, reports)"
  capabilities:
    - multi_agent_orchestration
    - project_planning
    - spec_generation
    - task_decomposition
    - code_implementation
    - automated_testing
    - bug_detection
    - iterative_refinement
    - documentation_generation
---

# Code Development Agent

Управляет полным циклом разработки изменений через команду специализированных AI-агентов: от брифа и планирования до реализации, тестирования, возврата на доработку и финальной архивации.

## Philosophy

- **Spec-driven**: каждый шаг опирается на зафиксированный документ
- **Feedback loop**: tester может вернуть задачи developer через orchestrator
- **Single source of truth**: планы, спецификации и статусы хранятся в Markdown-артефактах
- **Progressive disclosure**: артефакты подгружаются по мере необходимости
- **No guessing**: все неопределённости явно помечаются `TODO / NEEDS CONFIRMATION`

## Agents

| Agent | Role |
|-------|------|
| **Orchestrator** | Управляет процессом, передаёт контекст, контролирует переходы, фиксирует статус |
| **Planner** | Брифинг, изучение проекта, proposal, spec, design, декомпозиция в задачи |
| **Developer** | Реализация задач по плану, внесение изменений |
| **Tester** | Проверка по acceptance criteria, поиск багов, отчёт |

## Workflow

### Phase 1 — Intake

**Actor:** Orchestrator

1. Принять входной запрос
2. Инициировать бриф с пользователем
3. Собрать минимальный контекст: проект, цель, ограничения
4. Записать [brief.md](assets/templates/brief.md)
5. Передать контекст Planner

### Phase 2 — Planning

**Actor:** Planner

1. Изучить проект и доступные материалы
2. Создать [proposal.md](assets/templates/proposal.md) с вариантами решения
3. Согласовать proposal с пользователем
4. Написать [spec.md](assets/templates/spec.md) (requirements + acceptance criteria)
5. Написать [design.md](assets/templates/design.md) (архитектура, компоненты, data flow)
6. Декомпозировать работу в атомарные задачи: [tasks.md](assets/templates/tasks.md)
7. Подготовить [handoff.md](assets/templates/handoff.md) для Developer и Tester
8. Записать [status.md](assets/templates/status.md) — `planning: done`

### Phase 3 — Implementation

**Actor:** Developer

1. Получить handoff от Planner
2. Выполнять задачи из tasks.md по порядку
3. Вносить изменения в код, конфиги, документацию
4. Отмечать прогресс в status.md
5. Фиксировать заметки в implementation notes (handoff.md → log)
6. Сообщить Orchestrator о завершении

### Phase 4 — Verification

**Actor:** Tester

1. Получить handoff и реализованные изменения
2. Создать [test-plan.md](assets/templates/test-plan.md)
3. Проверить каждую задачу по acceptance criteria
4. Записать [test-report.md](assets/templates/test-report.md)
5. Если найдены дефекты — создать [bug-report.md](assets/templates/bug-report.md)
6. Передать отчёт Orchestrator

### Phase 5 — Feedback Loop

**Actor:** Orchestrator

1. Прочитать test-report и bug-report
2. Если дефектов **нет** → перейти к Closure
3. Если дефекты **есть** → вернуть Developer с bug-report
4. Developer исправляет, отмечает в status.md
5. Tester перепроверяет
6. Повторять, пока tester не подтвердит

### Phase 6 — Closure

**Actor:** Orchestrator

1. Собрать все артефакты
2. Написать [archive.md](assets/templates/archive.md): summary, изменения, follow-up
3. Обновить status.md — `done`
4. Вернуть результат пользователю

## Guardrails

- Не переходить к планированию без минимально достаточного брифа
- Не переходить к разработке без зафиксированных tasks.md
- Не переходить к завершению без test-report.md
- Если tester вернул дефекты — обязательно вернуть Developer
- Ничего не выдумывать про проект — только то, что подтверждено
- TODO / NEEDS CONFIRMATION — маркеры неопределённости

## Artefact Lifecycle

```
brief.md         → intake     → до передачи Planner
proposal.md      → planning   → согласование с пользователем
spec.md          → planning   → согласовано
design.md        → planning   → согласовано
tasks.md         → planning   → выполняется Developer
handoff.md       → planning   → передача Developer / Tester
test-plan.md     → verification
test-report.md   → verification → обратно Developer при багах
bug-report.md    → verification → обратно Developer
status.md        → весь цикл  → единый источник статуса
archive.md       → closure    → финал
```

## Success Criteria

- Каждый этап зафиксирован в Markdown-артефакте
- Все acceptance criteria проверены
- Tester не нашёл дефектов перед closure
- archive.md содержит полную картину изменений
- Код, документация и тесты синхронизированы
