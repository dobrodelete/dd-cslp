from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import project_crud
from app.schemas import ProjectCreate, ProjectUpdate, ProjectRead

router = APIRouter()


@router.post("/", response_model=ProjectRead)
async def create_project(project: ProjectCreate):
    return await project_crud.create_project(project)


@router.get("/{project_id}", response_model=ProjectRead)
async def get_project(project_id: int):
    project = await project_crud.get_project(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/", response_model=List[ProjectRead])
async def get_projects(skip: int = 0, limit: int = 100):
    return await project_crud.get_projects(skip, limit)


@router.put("/{project_id}", response_model=ProjectRead)
async def update_project(project_id: int, project: ProjectUpdate):
    project.id = project_id
    updated_project = await project_crud.update_project(project)
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project


@router.delete("/{project_id}", response_model=None)
async def delete_project(project_id: int):
    await project_crud.delete_project(project_id)
