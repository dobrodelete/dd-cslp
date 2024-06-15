from sqlalchemy import BigInteger, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class CTFEventRegistration(Base):
    __tablename__ = "ctf_event_registrations"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[BigInteger] = mapped_column(BigInteger, nullable=False)
    event_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("ctf_events.id"), nullable=False)
    registered_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    event: Mapped["CTFEvent"] = relationship("CTFEvent", back_populates="registrations")
