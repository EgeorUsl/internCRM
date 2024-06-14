from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .base import Base
from .candidate import Candidate


class Status(Base):
    __tablename__ = "status"

    status_name: Mapped[str] = mapped_column(String(255), unique=True,
                                             nullable=False)
    # status_cand: Mapped['candidates'] = relationship(
    #     'candidates', back_populates="status")
