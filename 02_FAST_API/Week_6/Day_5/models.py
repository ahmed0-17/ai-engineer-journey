from sqlalchemy import Text, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


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