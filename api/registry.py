import re
import yaml
from pathlib import Path
from api.schemas import SkillInfo


SKILLS_DIR = Path(__file__).resolve().parent.parent


def _parse_skill_md(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return {}, content
    frontmatter = yaml.safe_load(match.group(1)) or {}
    body = match.group(2).strip()
    return frontmatter, body


def _skill_dir_from_id(skill_id: str) -> Path | None:
    for category_dir in SKILLS_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith((".", "_", "api")):
            continue
        for skill_dir in category_dir.iterdir():
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            frontmatter, _ = _parse_skill_md(skill_md)
            meta = frontmatter.get("metadata", {})
            if meta.get("id") == skill_id:
                return skill_dir
    return None


def _read_text(path: Path) -> str | None:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def get_skill_dir(skill_id: str) -> Path | None:
    return _skill_dir_from_id(skill_id)


def get_reference_names(skill_id: str) -> list[str]:
    d = get_skill_dir(skill_id)
    if not d:
        return []
    refs_dir = d / "references"
    if not refs_dir.exists():
        return []
    return sorted(p.name for p in refs_dir.iterdir() if p.is_file())


def get_reference(skill_id: str, ref_name: str) -> str | None:
    d = get_skill_dir(skill_id)
    if not d:
        return None
    return _read_text(d / "references" / ref_name)


def _discover_skills() -> dict[str, SkillInfo]:
    skills: dict[str, SkillInfo] = {}

    for category_dir in SKILLS_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith((".", "_", "api")):
            continue

        for skill_dir in category_dir.iterdir():
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue

            frontmatter, body = _parse_skill_md(skill_md)
            meta = frontmatter.get("metadata", {})

            skill_id = meta.get("id", skill_dir.name)

            refs_dir = skill_dir / "references"
            ref_names = sorted(p.name for p in refs_dir.iterdir() if p.is_file()) if refs_dir.exists() else []

            skills[skill_id] = SkillInfo(
                id=skill_id,
                name=frontmatter.get("name", skill_dir.name),
                description=frontmatter.get("description", ""),
                version=meta.get("version", "0.0.0"),
                category=meta.get("category", category_dir.name),
                author=meta.get("author", ""),
                inputs=meta.get("inputs", {}),
                outputs=meta.get("outputs", {}),
                capabilities=meta.get("capabilities", []),
                spec=body,
                references=ref_names,
                license=frontmatter.get("license"),
                compatibility=frontmatter.get("compatibility"),
                metadata=meta,
                allowed_tools=frontmatter.get("allowed-tools"),
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
