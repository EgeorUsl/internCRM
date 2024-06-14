from sqlalchemy import (String, ForeignKey, Integer,
                        TIMESTAMP, JSON, Boolean)
from core.models import Base
from datetime import datetime
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column


class Role(Base):
    __tablename__ = "roles"
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    permissions: Mapped[dict] = mapped_column(JSON)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    username: Mapped[str] = mapped_column(
        String(length=1024), nullable=False)
    registered_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, default=datetime.utcnow)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey(Role.id))
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False)
