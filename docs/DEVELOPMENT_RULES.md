# Development Rules

## General

Do not create duplicate functionality.

## Architecture

Business logic belongs in services. Repositories work only with data access. Controllers do not contain business logic.

Each skill is a self-contained directory with SKILL.md + references/ + assets/.

## Errors

All exceptions must inherit from application errors.

## Logging

Do not use print. Use project logger.

## Configuration

No hardcoded secrets.
