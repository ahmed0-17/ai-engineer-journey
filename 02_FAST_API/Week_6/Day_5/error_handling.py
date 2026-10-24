import os
from sqlalchemy import create_engine,Text,Integer,Boolean
from sqlalchemy.orm import Session,mapped_column,Mapped,DeclarativeBase
from sqlalchemy.engine import URL

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


with Session(engine) as session:
    try:
        task = Task(title="Error Handling Test",completed=False)
        session.add(task)
        session.commit()

    except Exception:
        session.rollback()
        raise