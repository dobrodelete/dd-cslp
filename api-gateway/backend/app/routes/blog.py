import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter()

BLOG_SERVICE_URL = "http://blog-service:8000"


@router.get("/")
async def get_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BLOG_SERVICE_URL}/posts")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching posts")
        return response.json()
