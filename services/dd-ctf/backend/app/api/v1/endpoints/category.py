from typing import List, Optional

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.crud import category_crud
from app.schemas import CategoryCreate, CategoryUpdate, CategoryRead, Categories

router = APIRouter()


@router.post("/", response_model=Optional[CategoryRead])
async def create_category(category: CategoryCreate):
    try:
        category = await category_crud.create_category(category)
        return category
    except IntegrityError as e:
        raise HTTPException(status_code=405, detail="Category already exists")


@router.get("/{category_id}", response_model=Optional[CategoryRead])
async def get_category(category_id: int):
    category = await category_crud.get_category(category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("/", response_model=Categories)
async def get_categories(skip: int = 0, limit: int = 100):
    categories = await category_crud.get_categories(skip, limit)
    total = await category_crud.get_total()
    return Categories(
        categories=categories,
        total=total
    )


@router.get("/count/")
async def get_categories() -> int:
    total = await category_crud.get_total()
    return total


@router.put("/{category_id}", response_model=CategoryRead)
async def update_category(category: CategoryUpdate):
    updated_category = await category_crud.update_category(category)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category


@router.delete("/{category_id}")
async def delete_category(category_id: int):
    deleted_category = await category_crud.delete_category(category_id)
    if deleted_category is False:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category
