from sqlalchemy import BigInteger, ForeignKey, DateTime, LargeBinary, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class PasswordChanges(Base):
    __tablename__ = "password_changes"
    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("users.id"))
    old_password_hash: Mapped[LargeBinary] = mapped_column(LargeBinary)
    new_password_hash: Mapped[LargeBinary] = mapped_column(LargeBinary)
    change_time: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    user: Mapped["User"] = relationship(back_populates="password_changes")
