from sqlalchemy import Integer, Text, Boolean, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


# User Model
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    tasks: Mapped[list["Task"]] = relationship(
        back_populates="user"
    )


# Task Model
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    user: Mapped["User"] = relationship(
        back_populates="tasks"
    )

    priority: Mapped[int] = mapped_column(
    Integer,
    nullable=False,
    server_default="1"
    )
