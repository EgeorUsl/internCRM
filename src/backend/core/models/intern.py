from core.models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Intern(Base):
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    studing_place: Mapped[str | None] = mapped_column(String(255), default="")
    education: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(
        String(50), default="working", nullable=False)
    city: Mapped[str] = mapped_column(String(255), nullable=False)
    branch: Mapped[str] = mapped_column(String(255), nullable=True)
    group: Mapped[str] = mapped_column(String(255), nullable=True)
