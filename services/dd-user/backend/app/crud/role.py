from typing import Optional, List

from sqlalchemy import select, update

from app.crud.base import CrudBase
from app.models import Role
from app.schemas import RoleCreate, RoleUpdate, RoleRead


class RoleCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_role(self, id: int) -> Optional[RoleRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Role).where(Role.id == id))
            role: Optional[Role] = result.scalar()
            return RoleRead.model_validate(role) if role else None

    async def get_role_permissions(self, id: int, limit: int = 999) -> Optional[RoleRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(Role)
                .where(Role.id == id)
                .limit(limit=limit)
                .options(Role.permissions)
            )
            role: Optional[Role] = result.scalar()
            return RoleRead.model_validate(role) if role else None

    async def get_role_users(self, id: int, limit: int = 999) -> Optional[RoleRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(Role)
                .where(Role.id == id)
                .limit(limit=limit)
                .options(Role.users)
            )
            role: Optional[Role] = result.scalar()
            return RoleRead.model_validate(role) if role else None

    async def get_full_role(self, id: int, limit: int = 999) -> Optional[RoleRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(Role)
                .where(Role.id == id)
                .limit(limit=limit)
                .options(Role.permissions)
                .options(Role.users)
            )
            role: Optional[Role] = result.scalar()
            return RoleRead.model_validate(role) if role else None

    async def get_roles(self, skip: int = 0, limit: int = 999) -> Optional[List[RoleRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Role).offset(skip).limit(limit))
            roles: Optional[List[Role]] = result.scalars().all()
            return [RoleRead.model_validate(role) for role in roles] if roles else None

    async def get_full_roles(self, skip: int = 0, limit: int = 999) -> Optional[List[RoleRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(Role)
                .offset(skip)
                .limit(limit)
                .options(Role.permissions)
                .options(Role.users)
            )
            roles: Optional[List[Role]] = result.scalars().all()
            return [RoleRead.model_validate(role) for role in roles] if roles else None

    async def create_role(self, role: RoleCreate) -> Role:
        async with self.insert_session_scope() as s:
            db_role = Role(name=role.name, description=role.description)
            s.add(db_role)
            await s.flush()
            return db_role

    async def update_role(self, role: RoleUpdate) -> Optional[RoleRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Role)
                .where(Role.id == role.id)
                .values(name=role.name, description=role.description)
                .returning(Role)
            )
            role: Optional[Role] = result.scalar()
            return RoleRead.model_validate(role) if role else None

    async def delete_role(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.delete(Role).where(Role.id == id)
