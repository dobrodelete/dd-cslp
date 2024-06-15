from sqlalchemy import BigInteger, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class ChallengeComment(Base):
    __tablename__ = "challenge_comments"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    challenge_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("challenges.id"))
    user_id: Mapped[BigInteger] = mapped_column(BigInteger)
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    challenge: Mapped["Challenge"] = relationship("Challenge", back_populates="comments")
    user: Mapped["User"] = relationship("User", back_populates="comments")
