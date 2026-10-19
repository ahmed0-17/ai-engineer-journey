import os
from sqlalchemy import Boolean, Integer, Text, create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


# 1. Database connection
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["PGUSER"],
    password=os.environ["PGPASSWORD"],
    host=os.environ["PGHOST"],
    port=int(os.environ["PGPORT"]),
    database=os.environ["PGDATABASE"],
)

engine = create_engine(database_url)


# 2. ORM base class
class Base(DeclarativeBase):
    pass


# 3. Existing tasks table ka ORM model
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    title: Mapped[str] = mapped_column(
        Text, nullable=False
    )
    completed: Mapped[bool] = mapped_column(
        Boolean, nullable=False
    )


# 4. Insert a new task
try:
    with Session(engine) as session:
        task = Task(
            title="Lerning Python",
            completed=False,
        )

        session.add(task)
        session.commit()

        print("Task inserted successfully!")
        print(f"Task ID: {task.id}")
        print(f"Task title: {task.title}")
        print(f"Completed: {task.completed}")

finally:
    engine.dispose()
