from sqlalchemy import BigInteger, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class LoginAttempts(Base):
    __tablename__ = "login_attempts"
    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True, index=True)
    user_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("users.id"))
    attempt_time: Mapped[DateTime] = mapped_column(DateTime)
    ip_address_v4: Mapped[INET] = mapped_column(INET)
    ip_address_v6: Mapped[INET] = mapped_column(INET, nullable=True)
    user_agent: Mapped[str] = mapped_column()
    successful: Mapped[bool] = mapped_column()

    user: Mapped["User"] = relationship(back_populates="login_attempts")
