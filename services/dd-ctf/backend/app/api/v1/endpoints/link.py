from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.crud import link_crud
from app.schemas import LinkCreate, LinkRead, LinkUpdate

router = APIRouter()


@router.post("/", response_model=LinkRead)
async def create_link(link_in: LinkCreate):
    link = await link_crud.create_link(link=link_in)
    return link


@router.get("/{link_id}", response_model=LinkRead)
async def get_link(link_id: int):
    link = await link_crud.get_link(link_id=link_id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link


@router.get("/", response_model=List[LinkRead])
async def get_links(skip: int = 0, limit: int = 100):
    return await link_crud.get_links(skip=skip, limit=limit)


@router.put("/{link_id}", response_model=LinkRead)
async def update_link(link_in: LinkUpdate):
    link = await link_crud.update_link(link=link_in)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link


@router.delete("/{link_id}")
async def delete_link(link_id: int):
    await link_crud.delete_link(link_id=link_id)
    return {"message": "Link deleted successfully"}
