from sqlalchemy import BigInteger, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class TaskComment(Base):
    __tablename__ = "task_comments"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    task_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("tasks.id"))
    author_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("users.id"))
    content: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    task: Mapped["Task"] = relationship("Task", back_populates="comments")
    author: Mapped["User"] = relationship("User")
