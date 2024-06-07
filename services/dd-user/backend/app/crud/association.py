from sqlalchemy import insert, delete, select

from app.crud import CrudBase
from app.models import role_permission_association, user_permission_association, user_role_association


class AssociationCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def add_role_permission(self, role_id: int, permission_id: int):
        with self.insert_session_scope() as s:
            stmt = insert(role_permission_association).values(role_id=role_id, permission_id=permission_id)
            await s.execute(stmt)

    async def remove_role_permission(self, role_id: int, permission_id: int):
        with self.insert_session_scope() as s:
            stmt = delete(role_permission_association).where(
                (role_permission_association.c.role_id == role_id) &
                (role_permission_association.c.permission_id == permission_id)
            )
            await s.execute(stmt)

    async def add_user_permission(self, user_id: int, permission_id: int):
        with self.insert_session_scope() as s:
            stmt = insert(user_permission_association).values(user_id=user_id, permission_id=permission_id)
            await s.execute(stmt)

    async def remove_user_permission(self, user_id: int, permission_id: int):
        with self.insert_session_scope() as s:
            stmt = delete(user_permission_association).where(
                (user_permission_association.c.user_id == user_id) &
                (user_permission_association.c.permission_id == permission_id)
            )
            await s.execute(stmt)

    async def add_user_role(self, user_id: int, role_id: int):
        with self.insert_session_scope() as s:
            stmt = insert(user_role_association).values(user_id=user_id, role_id=role_id)
            await s.execute(stmt)

    async def remove_user_role(self, user_id: int, role_id: int):
        with self.insert_session_scope() as s:
            stmt = delete(user_role_association).where(
                (user_role_association.c.user_id == user_id) &
                (user_role_association.c.role_id == role_id)
            )
            await s.execute(stmt)

    async def get_user_permissions(self, user_id: int):
        with self.insert_session_scope() as s:
            stmt = select(user_permission_association.c.permission_id).where(
                user_permission_association.c.user_id == user_id)
            result = await s.execute(stmt)
            return result.scalars().all()

    async def get_role_permissions(self, role_id: int):
        stmt = select(role_permission_association.c.permission_id).where(
            role_permission_association.c.role_id == role_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_user_roles(self, user_id: int):
        stmt = select(user_role_association.c.role_id).where(user_role_association.c.user_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
