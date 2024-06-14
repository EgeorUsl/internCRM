from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey
from .base import Base
from .cities import City
from .status import Status


class Intern(Base):
    __tablename__ = "interns"
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    studing_place: Mapped[str] = mapped_column(String(255), default="")
    education: Mapped[str] = mapped_column(String(100), nullable=False)
    status_id: Mapped[int] = mapped_column(Integer, ForeignKey(Status.id))
    city_id: Mapped[int] = mapped_column(Integer, ForeignKey(City.id))
    branch: Mapped[str] = mapped_column(String(255), nullable=True)
    group: Mapped[str] = mapped_column(String(255), nullable=True)
