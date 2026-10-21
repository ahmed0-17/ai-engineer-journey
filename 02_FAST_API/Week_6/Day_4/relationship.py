import os

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Integer,
    String,
    create_engine,
    select,
)
from sqlalchemy.engine import URL
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    relationship,
)


# 1. Database connection
db_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["PGUSER"],
    password=os.environ["PGPASSWORD"],
    host=os.environ["PGHOST"],
    port=int(os.environ["PGPORT"]),
    database=os.environ["PGDATABASE"],
)

engine = create_engine(db_url)


# 2. Base class
class Base(DeclarativeBase):
    pass


# 3. User model
# Existing users table ko map karta hai
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    tasks: Mapped[list["Task"]] = relationship(
        back_populates="user"
    )


# 4. Task model
# Existing tasks table ko map karta hai
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    completed: Mapped[bool] = mapped_column(Boolean)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user: Mapped["User"] = relationship(
        back_populates="tasks"
    )


# 5. Fetch tasks with their user names
with Session(engine) as session:
    statement = select(Task).join(Task.user)

    tasks = session.scalars(statement).all()

    for task in tasks:
        print(
            f"Task ID: {task.id} | "
            f"Title: {task.title} | "
            f"Completed: {task.completed} | "
            f"User ID: {task.user_id} | "
            f"User Name: {task.user.name}"
        )
