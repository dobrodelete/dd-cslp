from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import task_comment_crud
from app.schemas import TaskCommentCreate, TaskCommentUpdate, TaskCommentRead

router = APIRouter()


@router.post("/", response_model=TaskCommentRead)
async def create_task_comment(task_comment: TaskCommentCreate):
    return await task_comment_crud.create_task_comment(task_comment)


@router.get("/{task_comment_id}", response_model=TaskCommentRead)
async def get_task_comment(task_comment_id: int):
    task_comment = await task_comment_crud.get_task_comment(task_comment_id)
    if task_comment is None:
        raise HTTPException(status_code=404, detail="TaskComment not found")
    return task_comment


@router.get("/", response_model=List[TaskCommentRead])
async def get_task_comments(skip: int = 0, limit: int = 100):
    return await task_comment_crud.get_task_comments(skip, limit)


@router.put("/{task_comment_id}", response_model=TaskCommentRead)
async def update_task_comment(task_comment_id: int, task_comment: TaskCommentUpdate):
    task_comment.id = task_comment_id
    updated_task_comment = await task_comment_crud.update_task_comment(task_comment)
    if updated_task_comment is None:
        raise HTTPException(status_code=404, detail="TaskComment not found")
    return updated_task_comment


@router.delete("/{task_comment_id}", response_model=None)
async def delete_task_comment(task_comment_id: int):
    await task_comment_crud.delete_task_comment(task_comment_id)
