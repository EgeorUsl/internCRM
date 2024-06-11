from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .base import Base


class Branch(Base):
    __tablename__ = "branches"

    branch_name: Mapped[str] = mapped_column(String(255), unique=True,
                                             nullable=False)
    groups_list: Mapped[list] = mapped_column(String(255), nullable=False)
