from sqlalchemy import BigInteger, String, func, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    challenge_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("challenges.id"))
    user_id: Mapped[BigInteger] = mapped_column(BigInteger)
    submission_time: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    flag: Mapped[str] = mapped_column(nullable=False)
    correct: Mapped[bool] = mapped_column(nullable=False)

    challenge: Mapped["Challenge"] = relationship("Challenge", back_populates="submissions")
