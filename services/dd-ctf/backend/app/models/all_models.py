from typing import List

from sqlalchemy import func, DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import declared_attr, DeclarativeBase, mapped_column, Mapped, relationship


class Base(DeclarativeBase):
    __abstract__ = True

    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    def __str__(self) -> str:
        columns_str = ", ".join(
            [
                f"{column.name}={getattr(self, column.name)!r}"
                for column in self.__table__.columns
            ]
        )
        return f"{self.__class__.__name__}({columns_str})"

    def __repr__(self) -> str:
        return self.__str__()


class Announcement(Base):
    __tablename__ = "announcements"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)

    challenges: Mapped[List["Challenge"]] = relationship("Challenge", back_populates="category")


class Challenge(Base):
    __tablename__ = "challenges"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    category_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("categories.id"))
    points: Mapped[int] = mapped_column(nullable=False)
    flag: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    category: Mapped["Category"] = relationship("Category", back_populates="challenges")
    hints: Mapped[List["Hint"]] = relationship("Hint", back_populates="challenge")
    submissions: Mapped[List["Submission"]] = relationship("Submission", back_populates="challenge")


class Hint(Base):
    __tablename__ = "hints"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    challenge_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("challenges.id"))
    content: Mapped[str] = mapped_column(nullable=False)
    cost: Mapped[int] = mapped_column(nullable=False)

    challenge: Mapped["Challenge"] = relationship("Challenge", back_populates="hints")


class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    challenge_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("challenges.id"))
    user_id: Mapped[BigInteger] = mapped_column(BigInteger)
    submission_time: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    flag: Mapped[str] = mapped_column(nullable=False)
    correct: Mapped[bool] = mapped_column(nullable=False)

    challenge: Mapped["Challenge"] = relationship("Challenge", back_populates="submissions")


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    members: Mapped[List["TeamMember"]] = relationship("TeamMember", back_populates="team")


class TeamMember(Base):
    __tablename__ = "team_members"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    team_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("teams.id"))
    user_id: Mapped[BigInteger] = mapped_column(BigInteger)
    joined_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    team: Mapped["Team"] = relationship("Team", back_populates="members")
