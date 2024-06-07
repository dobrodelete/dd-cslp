from typing import List

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)

    challenges: Mapped[List["Challenge"]] = relationship("Challenge", back_populates="category")
