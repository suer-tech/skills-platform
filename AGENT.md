# Project Context

## Project

Skills Platform

## Purpose

Единый API для вызова скиллов платформы. FastAPI-приложение, которое сканирует директории со скиллами, парсит SKILL.md и предоставляет REST API для их вызова.

## Stack

Python 3.14, FastAPI, Pydantic, PyYAML, Uvicorn

## Architecture

FastAPI-приложение с роутером /api/skills/*. Скиллы хранятся в директориях documentation/ и engineering/. Каждый скилл содержит SKILL.md с YAML frontmatter + body. API автоматически сканирует и кэширует скиллы при старте.

## Rules

См. [docs/DEVELOPMENT_RULES.md](docs/DEVELOPMENT_RULES.md)

## Documentation

- Architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- Project Map: [docs/PROJECT_MAP.md](docs/PROJECT_MAP.md)
- API: [docs/API.md](docs/API.md)
- Roadmap: [docs/ROADMAP.md](docs/ROADMAP.md)
- Decisions: [docs/adr/](docs/adr/)
