from sqlalchemy import BigInteger, func, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class TeamMember(Base):
    __tablename__ = "team_members"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    team_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("teams.id", ondelete="CASCADE"))
    user_id: Mapped[BigInteger] = mapped_column(BigInteger)
    joined_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    team: Mapped["Team"] = relationship("Team", back_populates="members")
