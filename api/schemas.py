from pydantic import BaseModel
from typing import Any


class SkillSummary(BaseModel):
    id: str
    name: str
    description: str


class SkillList(BaseModel):
    skills: list[SkillSummary]
    total: int


class SkillInfo(BaseModel):
    id: str
    name: str
    description: str
    version: str
    category: str
    author: str
    inputs: dict[str, Any]
    outputs: dict[str, Any]
    capabilities: list[str]

    license: str | None = None
    compatibility: str | None = None
    metadata: dict[str, Any] = {}
    allowed_tools: str | None = None

    spec: str | None = None
    references: list[str] = []


class GenerateRequest(BaseModel):
    project_spec: dict[str, Any]


class GenerateResponse(BaseModel):
    files: dict[str, str]
