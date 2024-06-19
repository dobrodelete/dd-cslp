from typing import List

from sqlalchemy import BigInteger, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Challenge(Base):
    __tablename__ = "challenges"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    ctf_event_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("ctf_events.id", ondelete="CASCADE"), nullable=True)
    category_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("categories.id", ondelete="CASCADE"))
    points: Mapped[int] = mapped_column(nullable=False)
    flag: Mapped[str] = mapped_column(nullable=False)

    ctf_event: Mapped["CTFEvent"] = relationship(
        "CTFEvent",
        back_populates="challenges"
    )
    category: Mapped["Category"] = relationship("Category", back_populates="challenges")

    hints: Mapped[List["Hint"]] = relationship(
        "Hint",
        back_populates="challenge",
        cascade="all, delete",
        passive_deletes=True,
    )
    submissions: Mapped[List["Submission"]] = relationship(
        "Submission",
        back_populates="challenge",
        cascade="all, delete",
        passive_deletes=True,
    )
    files: Mapped[List["File"]] = relationship(
        "File",
        back_populates="challenge",
        cascade="all, delete",
        passive_deletes=True,
    )
    links: Mapped[List["Link"]] = relationship(
        "Link",
        back_populates="challenge",
        cascade="all, delete",
        passive_deletes=True,
    )
    comments: Mapped[List["ChallengeComment"]] = relationship(
        "ChallengeComment",
        back_populates="challenge",
        cascade="all, delete",
        passive_deletes=True,
    )
    ratings: Mapped[List["ChallengeRating"]] = relationship(
        "ChallengeRating",
        back_populates="challenge"
    )
