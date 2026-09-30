from manager import TaskManager
from validation import Validation
from app_logging import get_logger
manager = TaskManager()


def show_menu():
   print("-----------Main Menu-----------")
   print("1. Create Task ")
   print("2. Show Tasks ")
   print("3. Show Task ")
   print("4. Update Task ")
   print("5. Complete Task ")
   print("6. Delete Task ")
   print("7.  Exit ")

def create_task():
  title=input("Enter task title :")
  description=input("Enter task description :")
  priority=input("Enter task priority :")

  if Validation.validate_title(title) and Validation.validate_description(description) and Validation.validate_priority(priority):
    manager.create_task(title,description,priority)


def show_tasks():
    return manager.get_tasks()


def show_task():
   try:
     task_id = int(input("Enter task ID: "))
   except ValueError:
     get_logger.error("Invalid ID")
     return
   if Validation.validate_id(task_id):
    task=manager.get_task(task_id)
    if task:print(task)
    else:print("Task not found")


def update_task():
  try:
    task_id = int(input("Enter task ID: "))
  except ValueError:
    get_logger.error("Invalid ID")
  title=input("Enter New title :")
  description=input("Enter  new task description :")
  priority=input("Enter new task priority :")

  if Validation.validate_title(title) and Validation.validate_description(description) and Validation.validate_id(task_id) and Validation.validate_priority(priority):
    manager.update_task(task_id,title,description,priority)


def complete_task():
   try:
       task_id = int(input("Enter task ID: "))
   except ValueError:
       get_logger.error("Invalid ID")
   if Validation.validate_id(task_id):
     manager.complete_task(task_id)

def delete_task():
  try:
    task_id = int(input("Enter task ID: "))
  except ValueError:
    get_logger.error("Invalid ID")
  if Validation.validate_id(task_id):
     manager.delete_task(task_id)
       


def run():
 while True:

  show_menu()

  choice = input("Enter your choice: ")

  if choice=="1": create_task()
  elif choice=="2":print(show_tasks())
  elif choice=="3":show_task()
  elif choice=="4":update_task()
  elif choice=="5":complete_task()
  elif choice=="6":delete_task()
  elif choice=="7":  
    print("Goodbye!")
    break



run()  