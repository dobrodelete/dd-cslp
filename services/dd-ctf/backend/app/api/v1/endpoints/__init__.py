from fastapi import APIRouter
from .announcement import router as announcement_router
from .category import router as category_router
from .challenge import router as challenge_router
from .challenge_comment import router as challenge_comment_router
from .challenge_rating import router as challenge_rating_router
from .ctf_event import router as ctf_event_router
from .ctf_event_registration import router as ctf_event_registration_router
from .file import router as file_router
from .hint import router as hint_router
from .link import router as link_router
from .submission import router as submission_router
from .team import router as team_router
from .team_member import router as team_member_router

api_router = APIRouter()

api_router.include_router(announcement_router, prefix="/announcements", tags=["Announcements"])
api_router.include_router(category_router, prefix="/categories", tags=["Categories"])
api_router.include_router(challenge_router, prefix="/challenges", tags=["Challenges"])
api_router.include_router(challenge_comment_router, prefix="/challenge_comments", tags=["Challenge comments"])
api_router.include_router(challenge_rating_router, prefix="/challenge_rating", tags=["Challenge rating"])
api_router.include_router(ctf_event_router, prefix="/ctf_event", tags=["CTF event"])
api_router.include_router(ctf_event_registration_router, prefix="/ctf_event_registration", tags=["CTF event registration users"])
api_router.include_router(file_router, prefix="/file", tags=["File"])
api_router.include_router(hint_router, prefix="/hints", tags=["Hints"])
api_router.include_router(submission_router, prefix="/submissions", tags=["Submissions"])
api_router.include_router(link_router, prefix="/link", tags=["Link"])
api_router.include_router(team_router, prefix="/teams", tags=["Teams"])
api_router.include_router(team_member_router, prefix="/team_members", tags=["Team Members"])
