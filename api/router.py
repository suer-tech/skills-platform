from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from api.schemas import SkillInfo, SkillList, SkillSummary, GenerateRequest, GenerateResponse
from api.registry import get_all_skills, get_skill, get_reference, get_skill_dir
from api.generator import generate_docs

router = APIRouter(prefix="/api", tags=["skills"])


@router.get("/skills", response_model=SkillList)
def list_skills():
    skills = get_all_skills()
    summaries = [
        SkillSummary(id=s.id, name=s.name, description=s.description)
        for s in skills.values()
    ]
    return SkillList(skills=summaries, total=len(summaries))


@router.get("/skills/{skill_id}", response_model=SkillInfo)
def skill_detail(skill_id: str):
    skill = get_skill(skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail=f"Skill '{skill_id}' not found")
    return skill


@router.get("/skills/{skill_id}/references/{ref_name}")
def get_skill_reference(skill_id: str, ref_name: str):
    content = get_reference(skill_id, ref_name)
    if content is None:
        raise HTTPException(status_code=404, detail="Reference not found")
    return PlainTextResponse(content, media_type="text/markdown")


@router.post("/skills/{skill_id}/generate", response_model=GenerateResponse)
def generate(skill_id: str, body: GenerateRequest):
    skill = get_skill(skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail=f"Skill '{skill_id}' not found")
    try:
        files = generate_docs(skill_id, body.project_spec)
        return GenerateResponse(files=files)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
