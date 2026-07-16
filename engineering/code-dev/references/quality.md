# Quality Standards

## Predictability

- Каждый шаг следует за предыдущим без пропусков
- Артефакты создаются в порядке, указанном в workflow
- Переходы контролируются Orchestrator

## Traceability

- Каждый артефакт ссылается на источник (brief → proposal → spec → design → tasks)
- Каждая задача связана с acceptance criteria
- Каждый дефект связан с задачей и тестом
- status.md всегда отражает текущую фазу

## Completeness

- Нет незавершённых секций (TODO помечать явно)
- Все acceptance criteria проверены
- test-report покрывает все задачи
- archive.md включает summary, изменения, follow-up

## Modularity

- Агенты читают только свои артефакты (Planner → spec, Developer → tasks)
- Артефакты независимы — можно переиспользовать spec в другом контексте
- Легко добавить нового агента (например, security-reviewer)
- Легко добавить новую фазу (например, deployment)

## Iteration Handling

- Каждый feedback loop увеличивает iteration counter
- bug-report хранит все найденные дефекты (старые + новые)
- Developer исправляет только то, что в bug-report
- После фикса tester перепроверяет всё, включая ранее пройденное
