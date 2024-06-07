from typing import List
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Permission(Base):
    __tablename__ = "permissions"
    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    description: Mapped[str] = mapped_column(nullable=True)

    roles: Mapped[List["Role"]] = relationship(secondary="role_permission_association", back_populates="permissions")
    users: Mapped[List["User"]] = relationship(secondary="user_permission_association", back_populates="permissions")
