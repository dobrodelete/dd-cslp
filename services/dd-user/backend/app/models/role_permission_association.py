from sqlalchemy import ForeignKey, Table, Column

from app.models import Base

role_permission_association = Table(
    "role_permission_association",
    Base.metadata,
    Column("role_id", ForeignKey("roles.id")),
    Column("permission_id", ForeignKey("permissions.id"))
)
