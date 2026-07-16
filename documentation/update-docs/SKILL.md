---
name: update-docs
description: >
  Синхронизирует документацию проекта с его текущим состоянием.
  Используй, когда код изменился, а документация устарела.
metadata:
  id: documentation.update-docs
  version: "0.1.0"
  category: documentation
  author: skills-platform
  inputs:
    project_path:
      required: true
      description: "Путь к проекту"
  outputs:
    summary:
      type: yaml
      description: "Что было изменено"
  capabilities:
    - code_analysis
    - documentation_update
---

# Update Documentation

## Purpose

Синхронизировать документацию проекта с его текущим состоянием.

Проект имеет структуру:
- `AGENT.md`
- `README.md`
- `docs/ARCHITECTURE.md`
- `docs/PROJECT_MAP.md`
- `docs/DEVELOPMENT_RULES.md`
- `docs/MODULE_INDEX.md`
- `docs/API.md`
- `docs/ROADMAP.md`
- `docs/adr/`

Со временем код меняется, документация устаревает. Этот скилл приводит документацию в актуальное состояние.

## Philosophy

Скилл работает в два этапа: сначала аудит, потом обновление.

**Аудит** — без изменений. Только анализ.

**Обновление** — только то, что действительно изменилось. Не переписывать документацию целиком, а точечно править.

## Workflow

1. **Audit** — прочитать код и документацию, найти расхождения. См. [инструкцию аудита](references/doc_audit.md).
2. **Update** — исправить устаревшие разделы, добавить новое, удалить лишнее. См. [инструкцию обновления](references/doc_updater.md).
3. **Summary** — вернуть отчёт: какие файлы изменены и что именно.

## Updated Files

Обновляются существующие файлы из шаблонов new-project:

- `AGENT.md` (стек, архитектура, правила)
- `README.md` (описание, зависимости)
- `docs/ARCHITECTURE.md` (паттерны, компоненты)
- `docs/PROJECT_MAP.md` (структура папок)
- `docs/DEVELOPMENT_RULES.md` (если изменились)
- `docs/MODULE_INDEX.md` (новые/удалённые модули)
- `docs/API.md` (эндпоинты)
- `docs/ROADMAP.md` (прогресс)
- `docs/adr/` (новые ADR при необходимости)

Формат отчёта об изменениях — [doc_diff.yaml](references/doc_diff.yaml).

## Success Criteria

После выполнения:
- каждый документ отражает реальное состояние кода;
- нет устаревшей информации;
- разработчик может положиться на документацию.
