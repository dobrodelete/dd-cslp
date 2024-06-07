from sqlalchemy import BigInteger, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class UserSession(Base):
    __tablename__ = 'user_sessions'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("users.id"))
    session_token: Mapped[str] = mapped_column(unique=True, nullable=False)
    valid: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    expires_at: Mapped[DateTime] = mapped_column(DateTime)
    ip_address: Mapped[str] = mapped_column()
    user_agent: Mapped[str] = mapped_column()

    user: Mapped["User"] = relationship(back_populates="user_session")
