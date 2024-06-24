from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, Integer, ForeignKey
from .base import Base
from core.models.branch import Branch
from core.models.cities import City
from core.models.status import Status


class Candidate(Base):
    __tablename__ = "candidates"
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    studing_place: Mapped[str] = mapped_column(
        String(255), nullable=True)
    education: Mapped[str] = mapped_column(String(255))
    scores: Mapped[str] = mapped_column(
        Integer(), server_default="0")
    target_internship: Mapped[str] = mapped_column(Text, nullable=True)
    status_id: Mapped[int] = mapped_column(
        ForeignKey(Status.id), default=1)
    city_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(City.id))
    prefer_branch_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Branch.id))
    completed_tests: Mapped[int] = mapped_column(
        Integer, server_default="0")
    status = relationship("Status", backref="candidates")
    city = relationship("City", backref="candidates")
    prefer_branch = relationship("Branch", backref="candidates")
