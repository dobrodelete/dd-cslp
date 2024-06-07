from sqlalchemy import BigInteger, DateTime, func
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class BlockedIPs(Base):
    __tablename__ = 'blocked_ips'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    block: Mapped[bool] = mapped_column(default=True)
    ip_address_v4: Mapped[INET] = mapped_column(INET, unique=True, nullable=False)
    ip_address_v6: Mapped[INET] = mapped_column(INET, unique=True, nullable=True)
    block_reason: Mapped[str] = mapped_column(nullable=True)
    blocked_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())
