from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from .base import Base
from .cities import City
from .status import Status
from .branch import Branch, Group


class Intern(Base):
    __tablename__ = "interns"
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    studing_place: Mapped[str] = mapped_column(String(255), default="")
    education: Mapped[str] = mapped_column(String(255), nullable=False)
    status_id: Mapped[int] = mapped_column(Integer, ForeignKey(Status.id),
                                           default=1)
    city_id: Mapped[int] = mapped_column(Integer, ForeignKey(City.id))
    branch_id: Mapped[int] = mapped_column(Integer, ForeignKey(Branch.id))
    group_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Group.id), nullable=True)
    status = relationship("Status", backref="interns")
    city = relationship("City", backref="interns")
    branch = relationship("Branch", backref="interns")
    group = relationship("Group", backref="interns")
