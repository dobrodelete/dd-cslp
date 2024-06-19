from typing import Optional

from sqlalchemy import BigInteger, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class File(Base):
    __tablename__ = "files"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    filename: Mapped[str] = mapped_column(nullable=False)
    filepath: Mapped[str] = mapped_column(nullable=False)
    challenge_id: Mapped[Optional[BigInteger]] = mapped_column(BigInteger, ForeignKey("challenges.id", ondelete="CASCADE"), nullable=True)

    challenge: Mapped[Optional["Challenge"]] = relationship(
        "Challenge",
        back_populates="files"
    )
