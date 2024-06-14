from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UniqueConstraint
from .base import Base
from .candidate import Candidate


class Branch(Base):
    __tablename__ = "branches"

    branch_name: Mapped[str] = mapped_column(String(255), unique=True,
                                             nullable=False)
    # groups: Mapped[list] = mapped_column(String(255))
    # __table_args__ = (UniqueConstraint('branch_name', 'groups'),)
