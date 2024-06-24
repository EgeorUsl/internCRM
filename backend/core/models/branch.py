from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer
from .base import Base


class Branch(Base):
    __tablename__ = "branches"

    branch_name: Mapped[str] = mapped_column(String(255), unique=True,
                                             nullable=False)
    groups = relationship("Group", backref="branch")


class Group(Base):
    __tablename__ = "groups"

    group_name: Mapped[str] = mapped_column(String(255),
                                            nullable=False)
    branch_id: Mapped[Branch] = mapped_column(Integer, ForeignKey(Branch.id))
