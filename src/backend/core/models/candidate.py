from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Integer, ForeignKey
from .base import Base
# from .cities import City
# from .status import Status
# from .branch import Branch


class Candidate(Base):
    __tablename__ = "candidates"
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True,
                                       nullable=False)
    studing_place: Mapped[str] = mapped_column(
        String(255), default="")
    education: Mapped[str] = mapped_column(String(255), nullable=False)
    scores: Mapped[str] = mapped_column(
        Integer(), default=0, server_default="0", nullable=False)

    target_internship: Mapped[str] = mapped_column(Text)

    # status_id: Mapped[int] = mapped_column(
    #     Integer, ForeignKey(Status.id), default=1)
    #
    # city_id: Mapped[int] = mapped_column(
    #     Integer, ForeignKey(City.id), nullable=False)
    #
    # prefer_branch_id: Mapped[int] = mapped_column(
    #     Integer, ForeignKey(Branch.id), nullable=False)
    #
    # future_branch_id: Mapped[int] = mapped_column(
    #     Integer, ForeignKey(Branch.id))

    completed_tests: Mapped[int] = mapped_column(
        Integer, server_default="0", default=0)
