from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas import TaskStatusCreate, TaskStatusUpdate, TaskStatusRead
from app.crud import task_status_crud

router = APIRouter()


@router.post("/", response_model=TaskStatusRead)
async def create_task_status(task_status: TaskStatusCreate):
    return await task_status_crud.create_task_status(task_status)


@router.get("/{task_status_id}", response_model=TaskStatusRead)
async def get_task_status(task_status_id: int):
    task_status = await task_status_crud.get_task_status(task_status_id)
    if task_status is None:
        raise HTTPException(status_code=404, detail="TaskStatus not found")
    return task_status


@router.get("/", response_model=List[TaskStatusRead])
async def get_task_statuses(skip: int = 0, limit: int = 100):
    return await task_status_crud.get_task_statuses(skip, limit)


@router.put("/{task_status_id}", response_model=TaskStatusRead)
async def update_task_status(task_status_id: int, task_status: TaskStatusUpdate):
    task_status.id = task_status_id
    updated_task_status = await task_status_crud.update_task_status(task_status)
    if updated_task_status is None:
        raise HTTPException(status_code=404, detail="TaskStatus not found")
    return updated_task_status


@router.delete("/{task_status_id}", response_model=None)
async def delete_task_status(task_status_id: int):
    await task_status_crud.delete_task_status(task_status_id)
