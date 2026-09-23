from dataclasses import dataclass


@dataclass
class Task:
    id:int
    title:str
    description:str
    priority:str
    completed:bool
    created_at:str


task1=Task(1,"Learning Python","with context manager and exceptions","High",False,"4-08-26")

print(task1.priority)