from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import page_crud
from app.schemas import PageCreate, PageUpdate, PageRead

router = APIRouter()


@router.post("/", response_model=PageRead)
async def create_page(page: PageCreate):
    return await page_crud.create_page(page)


@router.get("/{page_id}", response_model=PageRead)
async def get_page(page_id: int):
    page = await page_crud.get_page(page_id)
    if page is None:
        raise HTTPException(status_code=404, detail="Page not found")
    return page


@router.get("/", response_model=List[PageRead])
async def get_pages(skip: int = 0, limit: int = 100):
    return await page_crud.get_pages(skip, limit)


@router.put("/{page_id}", response_model=PageRead)
async def update_page(page: PageUpdate):
    updated_page = await page_crud.update_page(page)
    if updated_page is None:
        raise HTTPException(status_code=404, detail="Page not found")
    return updated_page


@router.delete("/{page_id}", response_model=PageRead)
async def delete_page(page_id: int):
    deleted_page = await page_crud.delete_page(page_id)
    if deleted_page is None:
        raise HTTPException(status_code=404, detail="Page not found")
    return deleted_page
