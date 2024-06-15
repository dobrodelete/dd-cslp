from typing import List

from sqlalchemy import BigInteger, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Challenge(Base):
    __tablename__ = "challenges"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    ctf_event_id: Mapped[BigInteger] = mapped_column(BigInteger, nullable=True)
    category_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("categories.id"))
    points: Mapped[int] = mapped_column(nullable=False)
    flag: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    ctf_event: Mapped["CTFEvent"] = relationship("CTFEvent", back_populates="challenges")
    category: Mapped["Category"] = relationship("Category", back_populates="challenges")
    hints: Mapped[List["Hint"]] = relationship("Hint", back_populates="challenge")
    submissions: Mapped[List["Submission"]] = relationship("Submission", back_populates="challenge")
    files: Mapped[List["File"]] = relationship("File", back_populates="challenge")
    links: Mapped[List["Link"]] = relationship("Link", back_populates="challenge")
    challenge_comments: Mapped[List["ChallengeComment"]] = relationship("ChallengeComment", back_populates="challenge")
    challenge_rating: Mapped[List["ChallengeRating"]] = relationship("ChallengeRating", back_populates="challenge")
