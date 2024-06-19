from sqlalchemy import BigInteger, String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Hint(Base):
    __tablename__ = "hints"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    challenge_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("challenges.id", ondelete="CASCADE"))
    content: Mapped[str] = mapped_column(nullable=False)
    cost: Mapped[int] = mapped_column(nullable=False)

    challenge: Mapped["Challenge"] = relationship("Challenge", back_populates="hints")
