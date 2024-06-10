from sqlalchemy import BigInteger, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class TaskAssignment(Base):
    __tablename__ = "task_assignments"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    task_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("tasks.id"))
    user_id: Mapped[BigInteger] = mapped_column(BigInteger)
    assigned_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    task: Mapped["Task"] = relationship("Task", back_populates="assignments")
