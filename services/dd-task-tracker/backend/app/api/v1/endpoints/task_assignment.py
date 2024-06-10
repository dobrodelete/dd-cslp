from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import task_assignment_crud
from app.schemas import TaskAssignmentCreate, TaskAssignmentUpdate, TaskAssignmentRead

router = APIRouter()


@router.post("/", response_model=TaskAssignmentRead)
async def create_task_assignment(task_assignment: TaskAssignmentCreate):
    return await task_assignment_crud.create_task_assignment(task_assignment)


@router.get("/{task_assignment_id}", response_model=TaskAssignmentRead)
async def get_task_assignment(task_assignment_id: int):
    task_assignment = await task_assignment_crud.get_task_assignment(task_assignment_id)
    if task_assignment is None:
        raise HTTPException(status_code=404, detail="TaskAssignment not found")
    return task_assignment


@router.get("/", response_model=List[TaskAssignmentRead])
async def get_task_assignments(skip: int = 0, limit: int = 100):
    return await task_assignment_crud.get_task_assignments(skip, limit)


@router.put("/{task_assignment_id}", response_model=TaskAssignmentRead)
async def update_task_assignment(task_assignment_id: int, task_assignment: TaskAssignmentUpdate):
    task_assignment.id = task_assignment_id
    updated_task_assignment = await task_assignment_crud.update_task_assignment(task_assignment)
    if updated_task_assignment is None:
        raise HTTPException(status_code=404, detail="TaskAssignment not found")
    return updated_task_assignment


@router.delete("/{task_assignment_id}", response_model=None)
async def delete_task_assignment(task_assignment_id: int):
    await task_assignment_crud.delete_task_assignment(task_assignment_id)
