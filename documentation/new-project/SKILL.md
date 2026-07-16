---
name: new-project
description: >
  Проводит AI-бриф проекта, создает Project Specification
  и генерирует базовую архитектурную документацию нового проекта.
metadata:
  id: documentation.new-project
  version: "0.1.0"
  category: documentation
  author: skills-platform
  inputs:
    project_name:
      required: false
      description: "Название проекта"
    project_description:
      required: false
      description: "Краткое описание проекта"
  outputs:
    project_spec:
      type: yaml
    documentation:
      type: files
  capabilities:
    - project_interview
    - architecture_planning
    - documentation_generation
    - agent_context_creation
---

# New Project Documentation

## Purpose

Создать правильный фундамент нового проекта:
- документацию;
- архитектуру;
- правила разработки;
- контекст для AI-агентов.

## Philosophy

Skill работает как технический архитектор. Он не должен сразу создавать файлы. Сначала он понимает проект.

## Workflow

1. **Interview** — провести AI-интервью с пользователем. См. [discovery_agent](references/discovery_agent.md).
2. **Spec** — собрать требования и создать Project Specification в формате [project_spec.yaml](references/project_spec.yaml).
3. **Review** — показать пользователю результат и получить подтверждение.
4. **Generate** — создать документацию по шаблонам из [assets/templates/](assets/templates/).

## Generated Files

- `AGENT.md`
- `README.md`
- `docs/ARCHITECTURE.md`
- `docs/PROJECT_MAP.md`
- `docs/DEVELOPMENT_RULES.md`
- `docs/MODULE_INDEX.md`
- `docs/API.md`
- `docs/ROADMAP.md`
- `docs/adr/NNN-title.md`

См. пример в [examples/tender-ai-project.yaml](examples/tender-ai-project.yaml).

## Success Criteria

После выполнения:
- новый разработчик понимает проект;
- AI-агент получает контекст;
- архитектурные решения зафиксированы.
