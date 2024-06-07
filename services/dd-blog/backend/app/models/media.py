from typing import List, Optional

from sqlalchemy import BigInteger, DateTime, func, ForeignKey, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Media(Base):
    __tablename__ = "media"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String, nullable=False)
    post_id: Mapped[Optional[BigInteger]] = mapped_column(BigInteger, ForeignKey("posts.id"), nullable=True)
    page_id: Mapped[Optional[BigInteger]] = mapped_column(BigInteger, ForeignKey("pages.id"), nullable=True)
    uploaded_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    post: Mapped[Optional["Post"]] = relationship("Post", back_populates="media")
    page: Mapped[Optional["Page"]] = relationship("Page", back_populates="media")
