from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import TeamMember
from app.schemas import TeamMemberCreate, TeamMemberUpdate, TeamMemberRead


class TeamMemberCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_team_member(self, id: int) -> Optional[TeamMemberRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(TeamMember).where(TeamMember.id == id))
            team_membership: Optional[TeamMember] = result.scalar()
            return TeamMemberRead.model_validate(team_membership) if team_membership else None

    async def get_team_members(self, skip: int = 0, limit: int = 999) -> Optional[List[TeamMemberRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(TeamMember).offset(skip).limit(limit))
            team_memberships: Optional[List[TeamMember]] = result.scalars().all()
            return [TeamMemberRead.model_validate(team_membership) for team_membership in
                    team_memberships] if team_memberships else None

    async def create_team_member(self, team_membership: TeamMemberCreate) -> TeamMember:
        async with self.insert_session_scope() as s:
            db_team_membership = TeamMember(**team_membership.dict())
            s.add(db_team_membership)
            await s.flush()
            return db_team_membership

    async def update_team_member(self, team_membership: TeamMemberUpdate) -> Optional[TeamMemberRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(TeamMember)
                .where(TeamMember.id == team_membership.id)
                .values(**team_membership.dict(exclude_unset=True))
                .returning(TeamMember)
            )
            team_membership: Optional[TeamMember] = result.scalar()
            return TeamMemberRead.model_validate(team_membership) if team_membership else None

    async def delete_team_member(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(
                delete(TeamMember)
                .where(TeamMember.id == id)
            )
