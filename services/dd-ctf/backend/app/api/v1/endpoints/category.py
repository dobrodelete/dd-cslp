from typing import List, Optional

from fastapi import APIRouter, HTTPException

from app.crud import category_crud
from app.schemas import CategoryCreate, CategoryUpdate, CategoryRead

router = APIRouter()


@router.post("/", response_model=CategoryRead)
async def create_category(category: CategoryCreate):
    return await category_crud.create_category(category)


@router.get("/{category_id}", response_model=Optional[CategoryRead])
async def get_category(category_id: int):
    category = await category_crud.get_category(category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("/", response_model=Optional[List[CategoryRead]])
async def get_categories(skip: int = 0, limit: int = 100):
    return await category_crud.get_categories(skip, limit)


@router.put("/{category_id}", response_model=CategoryRead)
async def update_category(category: CategoryUpdate):
    updated_category = await category_crud.update_category(category)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category


@router.delete("/{category_id}", response_model=CategoryRead)
async def delete_category(category_id: int):
    deleted_category = await category_crud.delete_category(category_id)
    if deleted_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category
