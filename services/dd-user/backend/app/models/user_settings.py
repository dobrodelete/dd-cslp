from sqlalchemy import BigInteger, ForeignKey, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models import Base


class UserSettings(Base):
    __tablename__ = "user_settings"
    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("users.id"))
    setting_name: Mapped[str] = mapped_column()
    setting_value: Mapped[str] = mapped_column()
    last_updated: Mapped[DateTime] = mapped_column(DateTime)

    user: Mapped["User"] = relationship(back_populates="user_settings")
