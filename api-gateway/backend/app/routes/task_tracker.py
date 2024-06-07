import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter()

TASK_TRACKER_SERVICE_URL = "http://task-tracker-service:8000"


@router.get("/")
async def get_tasks():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TASK_TRACKER_SERVICE_URL}/tasks")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching tasks")
        return response.json()
