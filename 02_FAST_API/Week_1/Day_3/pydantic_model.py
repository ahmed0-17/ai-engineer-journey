from fastapi import FastAPI
from pydantic import BaseModel,Field,EmailStr

app=FastAPI()

class Student(BaseModel):
    name:str=Field(min_length=3,max_length=50)
    age:int=Field(ge=18,le=40)
    course:str=Field(min_length=2)
    email:EmailStr

@app.post("/students")
def add_student(student:Student):
    return{
        "student":student
    }
