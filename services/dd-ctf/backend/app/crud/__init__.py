from .announcement import AnnouncementCrud
from .base import CrudBase
from .category import CategoryCrud
from .challenge import ChallengeCrud
from .hint import HintCrud
from .submission import SubmissionCrud
from .team import TeamCrud
from .team_member import TeamMemberCrud

announcement_crud = AnnouncementCrud()
category_crud = CategoryCrud()
challenge_crud = ChallengeCrud()
hint_crud = HintCrud()
submission_crud = SubmissionCrud()
team_crud = TeamCrud()
team_member_crud = TeamMemberCrud()


__all__ = [attr for attr in locals().keys() if not attr.startswith("_")]
