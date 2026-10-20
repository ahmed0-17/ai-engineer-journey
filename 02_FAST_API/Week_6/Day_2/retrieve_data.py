import os
from sqlalchemy import Boolean, Integer, Text, create_engine, select
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


# 1. Database connection configuration
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["PGUSER"],
    password=os.environ["PGPASSWORD"],
    host=os.environ["PGHOST"],
    port=int(os.environ["PGPORT"]),
    database=os.environ["PGDATABASE"],
)

engine = create_engine(database_url)


# 2. Base class for ORM models
class Base(DeclarativeBase):
    pass


# 3. Map Python class to existing PostgreSQL table
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


# 4. Read records using a Session
try:
    with Session(engine) as session:
        statement = select(Task).order_by(Task.id)
        tasks = session.scalars(statement).all()

        for task in tasks:
            print(
                f"ID: {task.id} | "
                f"Title: {task.title} | "
                f"Completed: {task.completed}"
            )
finally:
    engine.dispose()
