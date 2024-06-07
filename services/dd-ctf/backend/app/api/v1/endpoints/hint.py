from typing import List
from fastapi import APIRouter, HTTPException
from app.crud import hint_crud
from app.schemas.hint import HintCreate, HintUpdate, HintRead

router = APIRouter()


@router.post("/", response_model=HintRead)
async def create_hint(hint: HintCreate):
    return await hint_crud.create_hint(hint)


@router.get("/{hint_id}", response_model=HintRead)
async def get_hint(hint_id: int):
    hint = await hint_crud.get_hint(hint_id)
    if hint is None:
        raise HTTPException(status_code=404, detail="Hint not found")
    return hint


@router.get("/", response_model=List[HintRead])
async def get_hints(skip: int = 0, limit: int = 100):
    return await hint_crud.get_hints(skip, limit)


@router.put("/{hint_id}", response_model=HintRead)
async def update_hint(hint: HintUpdate):
    updated_hint = await hint_crud.update_hint(hint)
    if updated_hint is None:
        raise HTTPException(status_code=404, detail="Hint not found")
    return updated_hint


@router.delete("/{hint_id}", response_model=HintRead)
async def delete_hint(hint_id: int):
    deleted_hint = await hint_crud.delete_hint(hint_id)
    if deleted_hint is None:
        raise HTTPException(status_code=404, detail="Hint not found")
    return deleted_hint
