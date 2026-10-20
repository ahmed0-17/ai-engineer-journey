from fastapi import FastAPI,Depends,HTTPException,Header
from typing import Annotated
from pydantic import BaseModel


app=FastAPI(title="Task Api")

class Task(BaseModel):
    title:str
    completed:bool


tasks={1:{
          "title":"Learn FAST API",
          "completed":True
          },
          2:{
              "title":"Become AI Engineer",
             "completed":False
             }}


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "my-secret-token":
        raise HTTPException(
            status_code=401,
            detail="Invalid token authentication failed"
        )
      
@app.get("/tasks/",response_model=list[Task],dependencies=[Depends(verify_token)])
def get_tasks():
  
    return list(tasks.values())


@app.get("/tasks/{task_id}",response_model=Task,dependencies=[Depends(verify_token)])
def get_task(task_id:int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail=f"Product not found with id {task_id}"
        )
    return tasks[task_id] 

