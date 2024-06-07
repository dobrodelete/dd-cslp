from sqlalchemy import BigInteger, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    post_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("posts.id"))
    author_id: Mapped[BigInteger] = mapped_column(BigInteger)
    content: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    post: Mapped["Post"] = relationship("Post", back_populates="comments")
