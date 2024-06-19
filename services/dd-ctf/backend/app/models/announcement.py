from sqlalchemy import BigInteger, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class Announcement(Base):
    __tablename__ = "announcements"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
