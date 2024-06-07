from sqlalchemy import BigInteger, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Like(Base):
    __tablename__ = "likes"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    post_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("posts.id", ondelete="CASCADE"))
    user_id: Mapped[BigInteger] = mapped_column(BigInteger)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    post: Mapped["Post"] = relationship("Post", back_populates="likes")
