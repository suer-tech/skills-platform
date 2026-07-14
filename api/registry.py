import yaml
from pathlib import Path
from api.schemas import SkillInfo


SKILLS_DIR = Path(__file__).resolve().parent.parent


def _skill_dir_from_id(skill_id: str) -> Path | None:
    for category_dir in SKILLS_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith((".", "_", "api")):
            continue
        for skill_dir in category_dir.iterdir():
            if not (skill_dir / "skill.yaml").exists():
                continue
            with open(skill_dir / "skill.yaml", encoding="utf-8") as f:
                raw = yaml.safe_load(f)
            if raw.get("id") == skill_id:
                return skill_dir
    return None


def _read_text(path: Path) -> str | None:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def get_skill_dir(skill_id: str) -> Path | None:
    return _skill_dir_from_id(skill_id)


def get_prompt_names(skill_id: str) -> list[str]:
    d = get_skill_dir(skill_id)
    if not d:
        return []
    prompts_dir = d / "prompts"
    if not prompts_dir.exists():
        return []
    return sorted(p.name for p in prompts_dir.iterdir() if p.suffix == ".md")


def get_prompt(skill_id: str, prompt_name: str) -> str | None:
    d = get_skill_dir(skill_id)
    if not d:
        return None
    return _read_text(d / "prompts" / prompt_name)


def get_spec(skill_id: str) -> str | None:
    d = get_skill_dir(skill_id)
    if not d:
        return None
    return _read_text(d / "SKILL_SPEC.md")


def _discover_skills() -> dict[str, SkillInfo]:
    skills: dict[str, SkillInfo] = {}

    for category_dir in SKILLS_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith((".", "_", "api")):
            continue

        for skill_dir in category_dir.iterdir():
            skill_yaml = skill_dir / "skill.yaml"
            if not skill_yaml.exists():
                continue

            with open(skill_yaml, encoding="utf-8") as f:
                raw = yaml.safe_load(f)

            skill_id = raw.get("id", f"{category_dir.name}.{skill_dir.name}")
            skills[skill_id] = SkillInfo(
                id=skill_id,
                name=raw.get("name", skill_dir.name),
                version=raw.get("version", "0.0.0"),
                category=raw.get("category", category_dir.name),
                description=raw.get("description", ""),
                author=raw.get("author", ""),
                inputs=raw.get("inputs", {}),
                outputs=raw.get("outputs", {}),
                capabilities=raw.get("capabilities", []),
                spec=get_spec(skill_id),
                prompts=get_prompt_names(skill_id),
            )

    return skills


_skill_cache: dict[str, SkillInfo] | None = None


def get_all_skills() -> dict[str, SkillInfo]:
    global _skill_cache
    if _skill_cache is None:
        _skill_cache = _discover_skills()
    return _skill_cache


def get_skill(skill_id: str) -> SkillInfo | None:
    return get_all_skills().get(skill_id)


def refresh_cache():
    global _skill_cache
    _skill_cache = _discover_skills()
