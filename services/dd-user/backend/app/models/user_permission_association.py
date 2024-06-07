from sqlalchemy import ForeignKey, Table, Column

from app.models import Base

user_permission_association = Table(
    "user_permission_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("permission_id", ForeignKey("permissions.id"))
)
