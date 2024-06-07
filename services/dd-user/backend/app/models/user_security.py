from sqlalchemy import BigInteger, ForeignKey, DateTime, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models import Base


class UserSecurity(Base):
    __tablename__ = "user_security"
    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("users.id"))
    last_login: Mapped[DateTime] = mapped_column(DateTime)
    login_attempts: Mapped[int] = mapped_column(default=0)
    last_failed_login: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    password_changed_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    password_reset_token: Mapped[str] = mapped_column(nullable=True)
    password_reset_token_expires_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    account_lock: Mapped[bool] = mapped_column(default=False)
    account_lock_until: Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    user: Mapped["User"] = relationship(back_populates="user_security")
