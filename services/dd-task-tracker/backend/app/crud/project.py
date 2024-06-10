from typing import Optional, List
from sqlalchemy import select, update, delete
from app.crud import CrudBase
from app.models import Project
from app.schemas import ProjectCreate, ProjectUpdate, ProjectRead


class ProjectCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_project(self, id: int) -> Optional[ProjectRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Project).where(Project.id == id))
            project: Optional[Project] = result.scalar()
            return ProjectRead.model_validate(project) if project else None

    async def get_projects(self, skip: int = 0, limit: int = 100) -> Optional[List[ProjectRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Project).offset(skip).limit(limit))
            projects: Optional[List[Project]] = result.scalars().all()
            return [ProjectRead.model_validate(project) for project in projects] if projects else None

    async def create_project(self, project: ProjectCreate) -> Project:
        async with self.insert_session_scope() as s:
            db_project = Project(
                name=project.name,
                description=project.description,
                owner_id=project.owner_id
            )
            s.add(db_project)
            await s.flush()
            return db_project

    async def update_project(self, project: ProjectUpdate) -> Optional[ProjectRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Project)
                .where(Project.id == project.id)
                .values(
                    name=project.name,
                    description=project.description
                )
                .returning(Project)
            )
            updated_project: Optional[Project] = result.scalar()
            return ProjectRead.model_validate(updated_project) if updated_project else None

    async def delete_project(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(Project).where(Project.id == id))
