from typing import List

from sqlalchemy import BigInteger, DateTime, func, ForeignKey, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Page(Base):
    __tablename__ = "pages"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    author_id: Mapped[BigInteger] = mapped_column(BigInteger)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())
    published: Mapped[bool] = mapped_column(Boolean, default=False)

    media: Mapped[List["Media"]] = relationship("Media", back_populates="page")
