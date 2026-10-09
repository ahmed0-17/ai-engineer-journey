from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class Student(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=16, le=40)
    course: str = Field(min_length=2)
    email: EmailStr

students = {}
next_id = 1


@app.get("/students")
def get_students():
    return students


@app.post("/students")
def add_student(student: Student):
    global next_id

    students[next_id] = student.model_dump()
    created_student = {
        "id": next_id,
        **students[next_id]
    }

    next_id += 1
    return created_student


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": student_id,
        **students[student_id]
    }