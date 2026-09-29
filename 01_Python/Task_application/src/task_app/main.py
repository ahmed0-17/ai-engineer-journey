from manager import TaskManager




manager=TaskManager()
tasks=manager.get_tasks()
print(tasks)
manager.create_task("Learn German", "with fluency" ,"High")
manager.delete_task(2)
manager.delete_task(1)
manager.create_task("Learn German", "with fluency" ,"High")








