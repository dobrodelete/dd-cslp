from .announcement import AnnouncementCrud
from .base import CrudBase
from .category import CategoryCrud
from .challenge import ChallengeCrud
from .challenge_comment import ChallengeCommentCrud
from .challenge_rating import ChallengeRatingCrud
from .ctf_event import CTFEventCrud
from .ctf_event_registration import CTFEventRegistrationCrud
from .file import FileCrud
from .hint import HintCrud
from .link import LinkCrud
from .submission import SubmissionCrud
from .team import TeamCrud
from .team_member import TeamMemberCrud

announcement_crud = AnnouncementCrud()
category_crud = CategoryCrud()
challenge_crud = ChallengeCrud()
challenge_comment_crud = ChallengeCommentCrud()
challenge_rating_crud = ChallengeRatingCrud()
ctf_event_crud = CTFEventCrud()
ctf_event_registration_crud = CTFEventRegistrationCrud()
file_crud = FileCrud()
hint_crud = HintCrud()
link_crud = LinkCrud()
submission_crud = SubmissionCrud()
team_crud = TeamCrud()
team_member_crud = TeamMemberCrud()

__all__ = [attr for attr in locals().keys() if not attr.startswith("_")]
