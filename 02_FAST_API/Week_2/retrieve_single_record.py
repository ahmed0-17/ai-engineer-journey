import os
from sqlalchemy import Boolean, Integer, Text, create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


# Database connection settings
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["PGUSER"],
    password=os.environ["PGPASSWORD"],
    host=os.environ["PGHOST"],
    port=int(os.environ["PGPORT"]),
    database=os.environ["PGDATABASE"],
)

engine = create_engine(database_url)


# Base class for ORM models
class Base(DeclarativeBase):
    pass


# Map the Python class to the existing database table
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, nullable=False)


# Read one task
try:
    with Session(engine) as session:
        task = session.get(Task, 5)

        if task is not None:
            print(f"ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Completed: {task.completed}")
        else:
            print("Task not found")

finally:
    engine.dispose()
