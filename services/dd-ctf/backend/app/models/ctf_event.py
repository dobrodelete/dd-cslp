from typing import List

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class CTFEvent(Base):
    __tablename__ = "ctf_events"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    start_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    active: Mapped[bool] = mapped_column(default=True)

    challenges: Mapped[List["Challenge"]] = relationship("Challenge", back_populates="ctf_event")
