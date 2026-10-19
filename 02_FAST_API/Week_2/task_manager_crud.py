from sqlalchemy import Integer,Text,Boolean,create_engine,select
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
import os


db_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["PGUSER"],
    password=os.environ["PGPASSWORD"],
    host=os.environ["PGHOST"],
    port=int(os.environ["PGPORT"]),
    database=os.environ["PGDATABASE"],
)
engine=create_engine(db_url)


class Base(DeclarativeBase):
    pass



class Task(Base):
    __tablename__="tasks"

    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    title:Mapped[str]=mapped_column(Text,nullable=False)
    completed:Mapped[bool]=mapped_column(Boolean,nullable=False)





def create_task(task_title):
    with Session(engine) as session:
      try:
        task=Task(title=task_title,completed=False)
        session.add(task)
        session.commit()

        print("Task created")
        print(f"Task id :{task.id}")
        print(f"Task title :{task.title}")
        print(f"Task status :{task.completed}")
      finally:
        engine.dispose()  


def view_task(id):
    with Session(engine) as session:
      try:
        task=session.get(Task,id)
        
        if task is not None:
         print("Task found")
         print(f"Task id :{task.id}")
         print(f"Task title :{task.title}")
         print(f"Task status :{task.completed}")
        else:
           print("Task not found") 
      finally:
        engine.dispose()  




def view_tasks():
    with Session(engine) as session:
      try:
        statement=select(Task).order_by(Task.id)
        tasks=session.scalars(statement).all()      
        if tasks:
         for task in tasks:
          print("Task found")
          print(f"Task id :{task.id} |")
          print(f"Task title :{task.title} |")
          print(f"Task status :{task.completed} |")
        else:
           print("Task not found") 
      finally:
        engine.dispose()  

def update_task(id,title,status=False):
  with Session(engine) as session:
   try:
     task=session.get(Task,id)
     if task is not None:
       task.title=title
       task.completed=status
       session.commit()
       print("Task updated")
     else:
       print("Task not found")
   finally:
     engine.dispose()   




def delete_task(id):
  with Session(engine) as session:
    try:
      task=session.get(Task,id)
      if task is not None:
        session.delete(task)
        session.commit()
        print("Task deleted")
      else:
        print("Task not found")
    finally:
        engine.dispose()  



view_task(1)