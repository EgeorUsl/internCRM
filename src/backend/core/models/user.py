from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (Integer, String,
                        ForeignKey)
from sqlalchemy.sql.sqltypes import Boolean
from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm.decl_api import declarative_base


class user_group(Base):
    __tablename__ = "user_group"
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'),
                                         primary_key=True)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'groups.id'), primary_key=True)


class User(Base):
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(
        String(32), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    groups = relationship('Group', secondary=user_group,
                          backref='users')


class Group(Base):
    name: Mapped[str] = mapped_column(String(255), unique=True)
