from sqlalchemy import BigInteger, ForeignKey, DateTime, String
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from app.enums import AccessStatus


class UserAccessLog(Base):
    __tablename__ = "user_access_log"
    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True, index=True)
    user_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("users.id"))
    timestamp: Mapped[DateTime] = mapped_column(DateTime)
    ip_address_v4: Mapped[INET] = mapped_column(INET)
    ip_address_v6: Mapped[INET] = mapped_column(INET)
    action: Mapped[str] = mapped_column()
    status: Mapped[AccessStatus] = mapped_column()
    user_agent: Mapped[str] = mapped_column()
    location: Mapped[str] = mapped_column(nullable=True)

    user: Mapped["User"] = relationship(back_populates="user_access_log")
