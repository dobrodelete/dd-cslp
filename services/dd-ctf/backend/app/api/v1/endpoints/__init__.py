from fastapi import APIRouter
from .announcement import router as announcement_router
from .category import router as category_router
from .challenge import router as challenge_router
from .hint import router as hint_router
from app.api.v1.endpoints.submission import router as submission_router
from app.api.v1.endpoints.team import router as team_router
from app.api.v1.endpoints.team_member import router as team_member_router

api_router = APIRouter()

api_router.include_router(announcement_router, prefix="/announcements", tags=["Announcements"])
api_router.include_router(category_router, prefix="/categories", tags=["Categories"])
api_router.include_router(challenge_router, prefix="/challenges", tags=["Challenges"])
api_router.include_router(hint_router, prefix="/hints", tags=["Hints"])
api_router.include_router(submission_router, prefix="/submissions", tags=["Submissions"])
api_router.include_router(team_router, prefix="/teams", tags=["Teams"])
api_router.include_router(team_member_router, prefix="/team_members", tags=["Team Members"])
