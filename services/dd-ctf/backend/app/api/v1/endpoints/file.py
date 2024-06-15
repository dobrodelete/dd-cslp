from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import file_crud
from app.schemas import FileCreate, FileRead, FileUpdate

router = APIRouter()


@router.post("/", response_model=FileRead)
async def create_file(file_in: FileCreate):
    file = await file_crud.create_file(file=file_in)
    return file


@router.get("/{file_id}", response_model=FileRead)
async def get_file(file_id: int):
    file = await file_crud.get_file(file_id=file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return file


@router.get("/", response_model=List[FileRead])
async def get_files(skip: int = 0, limit: int = 100):
    return await file_crud.get_files(skip=skip, limit=limit)


@router.put("/{file_id}", response_model=FileRead)
async def update_file(file_in: FileUpdate):
    file = await file_crud.update_file(file=file_in)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return file


@router.delete("/{file_id}")
async def delete_file(file_id: int):
    await file_crud.delete_file(file_id=file_id)
    return {"message": "File deleted successfully"}
