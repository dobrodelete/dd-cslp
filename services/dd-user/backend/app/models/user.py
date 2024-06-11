from typing import List

from sqlalchemy import BigInteger, LargeBinary, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True, index=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    password_hash: Mapped[LargeBinary] = mapped_column(LargeBinary)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    phone_number: Mapped[str] = mapped_column(unique=True, nullable=True)
    full_name: Mapped[str] = mapped_column()
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())

    roles: Mapped[List["Role"]] = relationship(
        secondary="user_role_association",
        back_populates="users",
        cascade="all, delete"
    )
    permissions: Mapped[List["Permission"]] = relationship(
        secondary="user_permission_association",
        back_populates="users",
        cascade="all, delete"
    )
    login_attempts: Mapped[List["LoginAttempts"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    password_changes: Mapped[List["PasswordChanges"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    user_access_log: Mapped[List["UserAccessLog"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    user_security: Mapped[List["UserSecurity"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    user_session: Mapped[List["UserSession"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    user_settings: Mapped[List["UserSettings"]] = relationship(back_populates="user", cascade="all, delete-orphan")
