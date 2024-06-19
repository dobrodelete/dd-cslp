from typing import Optional

from sqlalchemy import BigInteger, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Link(Base):
    __tablename__ = "links"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    challenge_id: Mapped[Optional[BigInteger]] = mapped_column(BigInteger, ForeignKey("challenges.id", ondelete="CASCADE"), nullable=True)

    challenge: Mapped[Optional["Challenge"]] = relationship("Challenge", back_populates="links")
