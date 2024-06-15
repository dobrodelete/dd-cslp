from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import ctf_event_registration_crud
from app.schemas import CTFEventRegistrationCreate, CTFEventRegistrationRead, CTFEventRegistrationUpdate

router = APIRouter()


@router.post("/", response_model=CTFEventRegistrationRead)
async def create_registration(registration_in: CTFEventRegistrationCreate):
    registration = await ctf_event_registration_crud.create_registration(registration=registration_in)
    return registration


@router.get("/{registration_id}", response_model=CTFEventRegistrationRead)
async def get_registration(registration_id: int):
    registration = await ctf_event_registration_crud.get_registration(registration_id=registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration


@router.get("/", response_model=List[CTFEventRegistrationRead])
async def get_registrations(skip: int = 0, limit: int = 100):
    return await ctf_event_registration_crud.get_registrations(skip=skip, limit=limit)


@router.put("/{registration_id}", response_model=CTFEventRegistrationRead)
async def update_registration(registration_in: CTFEventRegistrationUpdate):
    registration = await ctf_event_registration_crud.update_registration(registration=registration_in)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration


@router.delete("/{registration_id}")
async def delete_registration(registration_id: int):
    await ctf_event_registration_crud.delete_registration(registration_id=registration_id)
    return {"message": "Registration deleted successfully"}
