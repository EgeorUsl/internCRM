from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .base import Base


class Status(Base):
    __tablename__ = "status"

    status_name: Mapped[str] = mapped_column(String(255), unique=True,
                                             nullable=False)
