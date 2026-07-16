# Architecture

## Pattern

modular (router-based)

## Technology Stack

| Component | Choice |
|-----------|--------|
| Language  | Python 3.14 |
| Framework | FastAPI |
| Database  | — |

## Deployment

Vercel (serverless)

## Structure

```
api/              # FastAPI приложение
  main.py         # Точка входа, CORS
  router.py       # REST-роуты (/api/skills/*)
  schemas.py      # Pydantic модели
  registry.py     # Поиск/кэширование скиллов из SKILL.md
  generator.py    # Шаблонизатор
documentation/    # Скиллы категории documentation
  update-docs/    # Обновление документации
  new-project/    # Документация нового проекта
engineering/      # Скиллы категории engineering
  bug-hunt/       # Поиск багов
```

## Discovery Flow

1. При старте registry сканирует `documentation/` и `engineering/`
2. В каждой поддиректории ищет `SKILL.md`
3. Парсит YAML frontmatter и body
4. Кэширует результат в `_skill_cache`
5. Роутер отдаёт данные через REST API
