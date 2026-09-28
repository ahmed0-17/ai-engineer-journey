from dataclasses import dataclass


@dataclass
class Task:
    id:int
    title:str
    description:str
    priority:str
    completed:bool
    created_at:str


