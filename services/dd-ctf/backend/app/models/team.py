from typing import List

from sqlalchemy import BigInteger, String, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    members: Mapped[List["TeamMember"]] = relationship("TeamMember", back_populates="team")
