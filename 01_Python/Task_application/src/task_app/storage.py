import json
from dataclasses import asdict
from manager import TaskManager
from models import Task



class Storage():

   

   def save_tasks(self,tasks):
    data=[asdict(task) for task in tasks]
    
    with open("tasks.json","w") as info:
        json.dump(data,info,indent=4)
        

   def load_tasks(self):
      with open("tasks.json","r") as info:
        data=json.load(info)
        tasks = [Task(**item) for item in data]
        return tasks
  


manager=TaskManager()
Task1=manager.create_task("Learn Python","with context manager","Medium")
Task2=manager.create_task("Learn JS","with context API","Medium")
storage=Storage()
storage.save_tasks(manager.get_tasks())
loaded_data=storage.load_tasks()
print(loaded_data)