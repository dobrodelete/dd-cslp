from .base import CrudBase
from .category import CategoryCrud
from .comment import CommentCrud
from .like import LikeCrud
from .media import MediaCrud
from .page import PageCrud
from .post import PostCrud
from .tag import TagCrud

category_crud = CategoryCrud()
comment_crud = CommentCrud()
like_crud = LikeCrud()
media_crud = MediaCrud()
page_crud = PageCrud()
post_crud = PostCrud()
tag_crud = TagCrud()

__all__ = [attr for attr in locals().keys() if not attr.startswith("_")]
