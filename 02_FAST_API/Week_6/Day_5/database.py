import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase,Session


# Database URL
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["PGUSER"],
    password=os.environ["PGPASSWORD"],
    host=os.environ["PGHOST"],
    port=int(os.environ["PGPORT"]),
    database=os.environ["PGDATABASE"],
)


# Database Engine
engine = create_engine(database_url)


# Base class for all ORM models
class Base(DeclarativeBase):
    pass




def get_session():
    with Session(engine) as session:
        yield session