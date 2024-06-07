from sqlalchemy import Column, BigInteger, ForeignKey, Table

from app.models import Base

post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", BigInteger, ForeignKey("posts.id", ondelete="CASCADE")),
    Column("tag_id", BigInteger, ForeignKey("tags.id", ondelete="CASCADE"))
)
