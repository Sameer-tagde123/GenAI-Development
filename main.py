import json
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="My First GenAI API", version="0.2.0")

DATA_FILE = Path("skills.json")


class SkillIn(BaseModel):
    skill: str = Field(min_length=1, max_length=50)


class SkillOut(BaseModel):
    skills: list[str]
    count: int


class MessageOut(BaseModel):
    message: str
    skills: list[str]


def load_skills() -> list[str]:
    """Read skills from disk. Missing file → empty list."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="skills.json is corrupted",
        )

    if not isinstance(data, list):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="skills.json must be a JSON list",
        )
    return data


def save_skills(skills: list[str]) -> None:
    """Write the full list back to disk."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as f:
            json.dump(skills, f, indent=2)
    except OSError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Could not save skills: {e}",
        )


@app.get("/")
def home():
    return {"message": "Day 4 — persistence + Pydantic"}


@app.get("/learner/{name}")
def learner(name: str):
    return {"name": name, "day": 4, "track": "GenAI Developer"}


@app.get("/skills", response_model=SkillOut)
def list_skills():
    skills = load_skills()
    return SkillOut(skills=skills, count=len(skills))


@app.post(
    "/add-skill",
    response_model=MessageOut,
    status_code=status.HTTP_201_CREATED,
)
def add_skill(payload: SkillIn):
    skill = payload.skill.strip().lower()

    if not skill:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Skill cannot be empty",
        )

    skills = load_skills()

    if skill in skills:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Skill '{skill}' already exists",
        )

    skills.append(skill)
    save_skills(skills)

    return MessageOut(
        message=f"Skill '{skill}' added",
        skills=skills,
    )


@app.delete("/skills/{skill}", response_model=MessageOut)
def delete_skill(skill: str):
    skill = skill.strip().lower()
    skills = load_skills()

    if skill not in skills:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Skill '{skill}' not found",
        )

    skills = [s for s in skills if s != skill]
    save_skills(skills)

    return MessageOut(message=f"Skill '{skill}' removed", skills=skills)


from fastapi import FastAPI
from pydantic import BaseModel, Field

from github_client import get_github_user

app = FastAPI(title="My First GenAI API", version="0.3.0")


class GithubUserOut(BaseModel):
    login: str
    name: str | None
    public_repos: int
    followers: int
    bio: str | None


@app.get("/github/{username}", response_model=GithubUserOut)
def github_user(username: str):
    raw = get_github_user(username)

    # Pick only fields we want — never dump the whole upstream JSON
    return GithubUserOut(
        login=raw.get("login", username),
        name=raw.get("name"),
        public_repos=raw.get("public_repos", 0),
        followers=raw.get("followers", 0),
        bio=raw.get("bio"),
    )