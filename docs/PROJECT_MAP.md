# Project Map

## Skills Platform

```
skills-platform/
├── api/                    # FastAPI backend
│   ├── main.py            # Entry point
│   ├── router.py          # API routes
│   ├── schemas.py         # Data models
│   ├── registry.py        # Skill discovery & cache
│   └── generator.py       # Template engine
├── documentation/         # Documentation skills
│   ├── update-docs/       # SKILL.md + references/
│   └── new-project/       # SKILL.md + references/ + assets/
├── engineering/           # Engineering skills
│   └── bug-hunt/          # SKILL.md + references/
├── docs/                  # Project documentation
├── AGENT.md
├── README.md
├── requirements.txt
└── vercel.json
```

## Modules

### api (Python package)
- **main** — FastAPI app, CORS middleware
- **router** — endpoints: `/api/skills`, `/api/skills/{id}`, `/api/skills/{id}/references/{name}`, `/api/skills/{id}/generate`
- **schemas** — Pydantic models: SkillInfo, SkillSummary, GenerateRequest/Response
- **registry** — discovery and caching of skills from SKILL.md files
- **generator** — template variable substitution (`{{VAR}}`)

### Skills
- **documentation.new-project** — AI-бриф, project spec, генерация документации
- **documentation.update-docs** — аудит и обновление существующей документации
- **engineering.bug-hunt** — статический анализ и поиск багов
