from sqlalchemy import ForeignKey, Column, Table

from app.models import Base

user_role_association = Table(
    "user_role_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("role_id", ForeignKey("roles.id"))
)
