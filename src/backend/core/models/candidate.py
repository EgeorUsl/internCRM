
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Integer
from .base import Base


class Candidate(Base):
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    studing_place: Mapped[str] = mapped_column(
        String(255), default="")
    education: Mapped[str] = mapped_column(String(100), nullable=False)
    scores: Mapped[str] = mapped_column(Integer(), default=0, nullable=False)
    status: Mapped[str] = mapped_column(
        String(50), default="Begin_Testing", nullable=False)
    target_internship: Mapped[str] = mapped_column(Text,
                                                   default="")
    city: Mapped[str] = mapped_column(String(255), nullable=False)
    prefer_branch: Mapped[str] = mapped_column(String(255), nullable=False)
    future_branch: Mapped[str] = mapped_column(String(255), nullable=True)
    resume_filename: Mapped[str] = mapped_column(String(255), nullable=True)
    completed_tests: Mapped[int] = mapped_column(Integer, default=0)
