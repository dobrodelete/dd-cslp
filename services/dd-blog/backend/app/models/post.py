from typing import List

from sqlalchemy import BigInteger, String, DateTime, Boolean, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    category_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey("categories.id"))
    author_id: Mapped[BigInteger] = mapped_column(BigInteger)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())
    published: Mapped[bool] = mapped_column(Boolean, default=False)

    category: Mapped["Category"] = relationship("Category", back_populates="posts")
    tags: Mapped[List["Tag"]] = relationship("Tag", secondary="post_tags", back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="post")
    likes: Mapped[List["Like"]] = relationship("Like", back_populates="post")
    media: Mapped[List["Media"]] = relationship("Media", back_populates="post")
