from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import ctf_event_crud
from app.schemas import CTFEventCreate, CTFEventRead, CTFEventUpdate, CTFEvents

router = APIRouter()


@router.post("/", response_model=CTFEventRead)
async def create_ctf_event(ctf_event_in: CTFEventCreate):
    ctf_event = await ctf_event_crud.create_ctf_event(ctf_event=ctf_event_in)
    return ctf_event


@router.get("/{ctf_event_id}", response_model=CTFEventRead)
async def get_ctf_event(ctf_event_id: int):
    ctf_event = await ctf_event_crud.get_ctf_event(ctf_event_id=ctf_event_id)
    if not ctf_event:
        raise HTTPException(status_code=404, detail="CTF Event not found")
    return ctf_event


@router.get("/", response_model=CTFEvents)
async def get_ctf_events(skip: int = 0, limit: int = 100):
    events = await ctf_event_crud.get_ctf_events(skip=skip, limit=limit)
    total = await ctf_event_crud.get_total()
    return CTFEvents(
        events=events,
        total=total
    )


@router.put("/{ctf_event_id}", response_model=CTFEventRead)
async def update_ctf_event(ctf_event_id: int, ctf_event_in: CTFEventUpdate):
    ctf_event = await ctf_event_crud.update_ctf_event(ctf_event=ctf_event_in)
    if not ctf_event:
        raise HTTPException(status_code=404, detail="CTF Event not found")
    return ctf_event


@router.delete("/{ctf_event_id}")
async def delete_ctf_event(ctf_event_id: int):
    await ctf_event_crud.delete_ctf_event(ctf_event_id=ctf_event_id)
    return {"message": "CTF Event deleted successfully"}
