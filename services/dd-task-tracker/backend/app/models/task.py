from typing import List, Optional

from sqlalchemy import BigInteger, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    project_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("projects.id"))
    status_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("task_statuses.id"))
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())
    due_date: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)

    project: Mapped["Project"] = relationship("Project", back_populates="tasks")
    status: Mapped["TaskStatus"] = relationship("TaskStatus", back_populates="tasks")
    comments: Mapped[List["TaskComment"]] = relationship("TaskComment", back_populates="task")
    assignments: Mapped[List["TaskAssignment"]] = relationship("TaskAssignment", back_populates="task")
