import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter()

CTF_SERVICE_URL = "http://ctf-service:8000"


@router.get("/")
async def get_ctf_events():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{CTF_SERVICE_URL}/events")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching CTF events")
        return response.json()
