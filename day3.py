# import utils                   
# from utils import greet       
# from utils import greet as say_hello  

# print(utils.add(5, 3))
# print(greet("Alex"))
# print(say_hello("Sam"))


# def calculate_area(length: float, width: float) -> float:
#     return length * width

# ------------------------------------------------------------------------------------------------------------------------------


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="My First GenAI API", version="0.1.0")

# Shared in-memory state (lost when the server restarts — that is OK for Day 3)
learned_skills = ["java", "python", "fastapi"]


class SkillIn(BaseModel):
    skill: str = Field(min_length=1, max_length=50)


@app.get("/")
def home():
    return {"message": "Welcome to my GenAI Developer journey!"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Keep going."}


@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}


@app.get("/learner/{name}")
def learner(name: str):
    return {
        "name": name,
        "day": 3,
        "track": "GenAI Developer",
    }


@app.get("/skills")
def list_skills():  
    return {"skills": learned_skills, "count": len(learned_skills)}


@app.post("/add-skill")
def add_skill(payload: SkillIn):
    skill = payload.skill.strip().lower()

    if skill in learned_skills:
        raise HTTPException(
            status_code=409,
            detail=f"Skill '{skill}' already exists",
        )

    learned_skills.append(skill)
    return {
        "message": f"Skill '{skill}' added successfully",
        "skills": learned_skills,
    }