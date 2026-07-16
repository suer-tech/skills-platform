---
name: bug-hunt
description: >
  Анализирует проект на наличие багов, влияющих на работоспособность.
  Находит логические ошибки, проблемы обработки ошибок,
  нулевые ссылки, гонки и другие критические дефекты.
metadata:
  id: engineering.bug-hunt
  version: "0.1.0"
  category: engineering
  author: skills-platform
  inputs:
    project_path:
      required: true
      description: "Путь к проекту"
    fix:
      required: false
      description: "Автоматически исправить найденные баги (true/false)"
  outputs:
    report:
      type: yaml
      description: "Отчёт с найденными багами и рекомендациями"
  capabilities:
    - static_analysis
    - bug_detection
    - code_review
---

# Bug Hunt

## Purpose

Найти в проекте баги, которые влияют на работоспособность: логические ошибки, падения, необработанные ошибки, проблемы с типами, гонки, утечки и т.д.

## Philosophy

Скилл ищет только реальные баги, не code style. Каждый баг должен воспроизводиться или быть очевидным по логике кода. Без ложных срабатываний.

## Workflow

1. **Scan** — прочитать проект, составить карту зависимостей и потоков данных.
2. **Detect** — найти потенциальные проблемы. См. [инструкцию по анализу](references/bug_analysis.md).
3. **Verify** — проверить каждый кандидат: это действительно баг?
4. **Report** — сформировать отчёт в формате [bug_report.yaml](references/bug_report.yaml).
5. **Fix** (опционально) — если `fix=true`, исправить баги.

## Success Criteria

- найденные баги — реальные, а не гипотетические;
- для каждого бага указан файл, строка и причина;
- если `fix=true` — код исправлен и не сломал тесты.
