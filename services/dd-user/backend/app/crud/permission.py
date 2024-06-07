from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud.base import CrudBase
from app.models.permission import Permission
from app.schemas.permission import PermissionCreate, PermissionUpdate, PermissionRead


class PermissionCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_permission(self, id: int) -> Optional[PermissionRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Permission).where(Permission.id == id))
            permission: Optional[Permission] = result.scalar()
            return PermissionRead.model_validate(permission) if permission else None

    async def get_permission_roles(self, id: int, limit: int = 999) -> Optional[PermissionRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(Permission)
                .where(Permission.id == id)
                .limit(limit=limit)
                .options(Permission.roles)
            )
            permission: Optional[Permission] = result.scalar()
            return PermissionRead.model_validate(permission) if permission else None

    async def get_permission_users(self, id: int, limit: int = 999) -> Optional[PermissionRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(Permission)
                .where(Permission.id == id)
                .limit(limit=limit)
                .options(Permission.users)
            )
            permission: Optional[Permission] = result.scalar()
            return PermissionRead.model_validate(permission) if permission else None

    async def get_full_permission(self, id: int, limit: int = 999) -> Optional[PermissionRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(Permission)
                .where(Permission.id == id)
                .limit(limit=limit)
                .options(Permission.roles)
                .options(Permission.users)
            )
            permission: Optional[Permission] = result.scalar()
            return PermissionRead.model_validate(permission) if permission else None

    async def get_permissions(self, skip: int = 0, limit: int = 999) -> Optional[List[PermissionRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Permission).offset(skip).limit(limit))
            permissions: Optional[List[Permission]] = result.scalars().all()
            return [PermissionRead.model_validate(permission) for permission in permissions] if permissions else None

    async def get_full_permissions(self, skip: int = 0, limit: int = 999) -> Optional[List[PermissionRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(Permission)
                .offset(skip)
                .limit(limit)
                .options(Permission.roles)
                .options(Permission.users)
            )
            permissions: Optional[List[Permission]] = result.scalars().all()
            return [PermissionRead.model_validate(permission) for permission in permissions] if permissions else None

    async def create_permission(self, permission: PermissionCreate) -> Permission:
        async with self.insert_session_scope() as s:
            db_permission = Permission(name=permission.name, description=permission.description)
            s.add(db_permission)
            await s.flush()
            return db_permission

    async def update_permission(self, permission: PermissionUpdate) -> Optional[PermissionRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Permission)
                .where(Permission.id == permission.id)
                .values(name=permission.name, description=permission.description)
                .returning(Permission)
            )
            updated_permission: Optional[Permission] = result.scalar()
            return PermissionRead.model_validate(updated_permission) if updated_permission else None

    async def delete_permission(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(Permission).where(Permission.id == id))
