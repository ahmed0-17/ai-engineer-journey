from sqlalchemy import Integer,DateTime, Text, Boolean, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from datetime import datetime, timezone


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )

    token_hash: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        index=True
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True)
    )

    revoked: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    user: Mapped["User"] = relationship(
    back_populates="refresh_tokens"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )




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

    email: Mapped[str] = mapped_column(
            String(255),
        unique=True,
        nullable=True
        )
    
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=True
        )

    refresh_tokens: Mapped[list["RefreshToken"]] = relationship(
    back_populates="user",
    cascade="all, delete-orphan"
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
