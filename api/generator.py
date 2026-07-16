from pathlib import Path
from typing import Any

from api.registry import get_skill_dir


def flatten_dict(data: dict[str, Any], prefix: str = "") -> dict[str, str]:
    result: dict[str, str] = {}
    for key, value in data.items():
        full_key = f"{prefix}_{key}" if prefix else key
        if isinstance(value, dict):
            result.update(flatten_dict(value, full_key))
        elif isinstance(value, list):
            result[full_key.upper()] = "\n".join(f"- {v}" for v in value)
        else:
            result[full_key.upper()] = str(value)
    aliases = {}
    for k, v in result.items():
        short = k.split("_", 1)[-1]
        if short != k and short not in result:
            aliases[short] = v
    result.update(aliases)
    return result


def generate_docs(skill_id: str, project_spec: dict[str, Any]) -> dict[str, str]:
    skill_dir = get_skill_dir(skill_id)
    if not skill_dir:
        raise ValueError(f"Skill '{skill_id}' not found")

    templates_dir = skill_dir / "assets" / "templates"
    if not templates_dir.exists():
        return {}

    variables = flatten_dict(project_spec)

    files: dict[str, str] = {}
    for template_file in sorted(templates_dir.rglob("*")):
        if not template_file.is_file():
            continue
        relative_path = str(template_file.relative_to(templates_dir))
        content = template_file.read_text(encoding="utf-8")
        for var_name, var_value in variables.items():
            content = content.replace("{{" + var_name + "}}", var_value)
        files[relative_path] = content

    return files
