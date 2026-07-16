# Example Workflow

## Scenario

Пользователь просит: *"Добавить валидацию email в форму регистрации"*

## Phase 1 — Intake (Orchestrator)

1. Принимает запрос
2. Записывает [brief.md](../assets/templates/brief.md) с контекстом
3. Передаёт Planner

## Phase 2 — Planning (Planner)

1. Изучает проект: находит форму регистрации, текущую валидацию
2. Пишет [proposal.md](../assets/templates/proposal.md):
   - A: inline-валидация в контроллере
   - B: отдельный валидатор-сервис
   - C: библиотечная валидация (рекомендовано)
3. Пользователь подтверждает proposal
4. Пишет [spec.md](../assets/templates/spec.md):
   - FR-1: валидация формата email (regex)
   - FR-2: проверка MX-записи (опционально)
   - FR-3: человекочитаемая ошибка
5. Пишет [design.md](../assets/templates/design.md):
   - email_validator.py → validate_email()
   - Форма вызывает validate_email при submit
6. Декомпозирует в [tasks.md](../assets/templates/tasks.md):
   - T-1: Создать email_validator.py с функцией validate_email
   - T-2: Встроить валидацию во view формы
   - T-3: Добавить тесты
7. Пишет [handoff.md](../assets/templates/handoff.md)

## Phase 3 — Implementation (Developer)

1. Берёт T-1: создаёт email_validator.py
2. Берёт T-2: добавляет вызов валидатора во view
3. Берёт T-3: пишет unit-тесты
4. Отмечает статус в status.md
5. Сообщает Orchestrator

## Phase 4 — Verification (Tester)

1. Пишет [test-plan.md](../assets/templates/test-plan.md):
   - TC-1: корректный email → pass
   - TC-2: email без @ → fail с ошибкой
   - TC-3: пустое поле → pass (не обязательное)
2. Выполняет тесты
3. Находит баг: TC-3 падает с 500 ошибкой
4. Пишет [bug-report.md](../assets/templates/bug-report.md):
   - B-1: пустой email вызывает AttributeError

## Phase 5 — Feedback Loop (Orchestrator → Developer → Tester)

1. Orchestrator читает test-report и bug-report
2. Возвращает Developer с B-1
3. Developer исправляет: добавить проверку на None
4. Tester перепроверяет: TC-3 → pass
5. Tester обновляет test-report: все тесты пройдены

## Phase 6 — Closure (Orchestrator)

1. Собирает все артефакты
2. Пишет [archive.md](../assets/templates/archive.md):
   - Summary: добавлена валидация email
   - 1 feedback loop, 3 файла изменено
   - Follow-up: добавить валидацию на фронтенде
3. Отдаёт результат пользователю
