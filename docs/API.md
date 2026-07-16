# API Reference

## Overview

Единый API для вызова скиллов платформы. FastAPI-приложение, которое сканирует директории со скиллами, парсит SKILL.md и предоставляет REST API для их вызова.

Базовый URL: `/api`

## Endpoints

### GET /api/skills

Список всех доступных скиллов.

**Response:**
```json
{
  "skills": [
    {
      "id": "documentation.new-project",
      "name": "new-project",
      "description": "Проводит AI-бриф проекта..."
    }
  ],
  "total": 3
}
```

### GET /api/skills/{skill_id}

Детальная информация о скилле.

**Response:** `SkillInfo` — name, description, version, category, inputs, outputs, capabilities, spec, references, license, compatibility, metadata, allowed_tools.

### GET /api/skills/{skill_id}/references/{ref_name}

Содержимое reference-файла скилла (markdown, yaml).

### POST /api/skills/{skill_id}/generate

Генерация файлов из шаблонов скилла.

**Request:**
```json
{
  "project_spec": {
    "project": { "name": "...", "description": "..." },
    "technology": { "language": "...", "framework": "..." }
  }
}
```

**Response:**
```json
{
  "files": {
    "README.md": "# ...",
    "ARCHITECTURE.md": "# ..."
  }
}
```
