from fastapi import APIRouter
from .category import router as category_router
from .comment import router as comment_router
from .like import router as like_router
from .media import router as media_router
from .page import router as page_router
from .post import router as post_router
from .tag import router as tag_router

router = APIRouter()
router.include_router(category_router, prefix="/categories", tags=["categories"])
router.include_router(comment_router, prefix="/comments", tags=["comments"])
router.include_router(like_router, prefix="/likes", tags=["likes"])
router.include_router(media_router, prefix="/media", tags=["media"])
router.include_router(page_router, prefix="/pages", tags=["pages"])
router.include_router(post_router, prefix="/posts", tags=["posts"])
router.include_router(tag_router, prefix="/tags", tags=["tags"])
