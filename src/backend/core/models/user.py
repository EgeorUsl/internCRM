from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from .base import Base
from sqlalchemy.orm import relationship


class User(Base):
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(32), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    groups: Mapped[list["Group"]] = relationship('Group',
                                                 primaryjoin='User.id == Group.user_id',
                                                 back_populates='user')


class Group(Base):
    branch_name: Mapped[str] = mapped_column(String(255))
    group_name: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship('User',
                                        primaryjoin='User.id == Group.user_id',
                                        back_populates='groups')
