from typing import List

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Role(Base):
    __tablename__ = "roles"
    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    description: Mapped[str] = mapped_column()

    users: Mapped[List["User"]] = relationship(secondary="user_role_association", back_populates="roles")
    permissions: Mapped[List["Permission"]] = relationship(secondary="role_permission_association", back_populates="roles")
