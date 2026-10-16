import os
from sqlalchemy import create_engine, text
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

with engine.connect() as connection:
    result = connection.execute(text("SELECT version()"))
    print(result.scalar())

engine.dispose()