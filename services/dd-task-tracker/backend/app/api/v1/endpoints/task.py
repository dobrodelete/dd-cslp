from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import task_crud
from app.schemas import TaskCreate, TaskUpdate, TaskRead

router = APIRouter()


@router.post("/", response_model=TaskRead)
async def create_task(task: TaskCreate):
    return await task_crud.create_task(task)


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(task_id: int):
    task = await task_crud.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.get("/", response_model=List[TaskRead])
async def get_tasks(skip: int = 0, limit: int = 100):
    return await task_crud.get_tasks(skip, limit)


@router.put("/{task_id}", response_model=TaskRead)
async def update_task(task_id: int, task: TaskUpdate):
    task.id = task_id
    updated_task = await task_crud.update_task(task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/{task_id}", response_model=None)
async def delete_task(task_id: int):
    await task_crud.delete_task(task_id)
