from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .base import Base


class City(Base):
    __tablename__ = "cities"

    city_name: Mapped[str] = mapped_column(String(255), unique=True,
                                           nullable=False)
    # cand_city: Mapped['candidates'] = relationship(
    #     'candidates', back_populates="city")
