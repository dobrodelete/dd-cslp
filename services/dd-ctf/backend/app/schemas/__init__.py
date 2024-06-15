from .announcement import AnnouncementBase, AnnouncementCreate, AnnouncementRead, AnnouncementUpdate
from .category import CategoryBase, CategoryCreate, CategoryRead, CategoryUpdate
from .challenge import ChallengeBase, ChallengeCreate, ChallengeRead, ChallengeUpdate
from .challenge_comment import ChallengeCommentBase, ChallengeCommentCreate, ChallengeCommentRead, ChallengeCommentUpdate
from .challenge_rating import ChallengeRatingBase, ChallengeRatingCreate, ChallengeRatingRead, ChallengeRatingUpdate
from .ctf_event import CTFEventBase, CTFEventCreate, CTFEventRead, CTFEventUpdate
from .ctf_event_registration import CTFEventRegistrationBase, CTFEventRegistrationCreate, CTFEventRegistrationRead, \
    CTFEventRegistrationUpdate
from .file import FileBase, FileCreate, FileRead, FileUpdate
from .hint import HintBase, HintCreate, HintRead, HintUpdate
from .link import LinkBase, LinkCreate, LinkRead, LinkUpdate
from .submission import SubmissionBase, SubmissionCreate, SubmissionRead, SubmissionUpdate
from .team import TeamBase, TeamCreate, TeamRead, TeamUpdate
from .team_member import TeamMemberBase, TeamMemberCreate, TeamMemberRead, TeamMemberUpdate

ChallengeRead.model_rebuild()
TeamRead.model_rebuild()

__all__ = [attr for attr in locals().keys() if not attr.startswith("_")]
