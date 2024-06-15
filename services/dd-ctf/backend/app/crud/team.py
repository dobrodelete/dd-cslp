from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import Team
from app.schemas import TeamCreate, TeamUpdate, TeamRead


class TeamCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_team(self, id: int) -> Optional[TeamRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Team).where(Team.id == id))
            team: Optional[Team] = result.scalar()
            return TeamRead.model_validate(team) if team else None

    async def get_teams(self, skip: int = 0, limit: int = 999) -> Optional[List[TeamRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Team).offset(skip).limit(limit))
            teams: Optional[List[Team]] = result.scalars().all()
            return [TeamRead.model_validate(team) for team in teams] if teams else None

    async def create_team(self, team: TeamCreate) -> Team:
        async with self.insert_session_scope() as s:
            db_team = Team(**team.dict())
            s.add(db_team)
            await s.flush()
            return db_team

    async def update_team(self, team: TeamUpdate) -> Optional[TeamRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Team)
                .where(Team.id == team.id)
                .values(**team.dict(exclude_unset=True))
                .returning(Team)
            )
            team: Optional[Team] = result.scalar()
            return TeamRead.model_validate(team) if team else None

    async def delete_team(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(
                delete(Team)
                .where(Team.id == id)
            )
