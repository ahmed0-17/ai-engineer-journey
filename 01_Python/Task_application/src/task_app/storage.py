import json
from storage import TaskManager



class Storage(TaskManager):

   def __init__(self):
    super().__init__(self.tasks)

   def save_tasks(self):
    with open("tasks.json","w") as info:
        data=json.dump(self.tasks,info,indent=4)
        info.write(data)

    def load_tasks():
      with open("tasks.json","r") as info:
        data=json.load(info)
        response=data.js
  

