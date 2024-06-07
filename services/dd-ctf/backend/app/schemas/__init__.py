from .announcement import AnnouncementBase, AnnouncementCreate, AnnouncementRead, AnnouncementUpdate
from .category import CategoryBase, CategoryCreate, CategoryRead, CategoryUpdate
from .challenge import ChallengeBase, ChallengeCreate, ChallengeRead, ChallengeUpdate
from .hint import HintBase, HintCreate, HintRead, HintUpdate
from .submission import SubmissionBase, SubmissionCreate, SubmissionRead, SubmissionUpdate
from .team import TeamBase, TeamCreate, TeamRead, TeamUpdate
from .team_member import TeamMemberBase, TeamMemberCreate, TeamMemberRead, TeamMemberUpdate

ChallengeRead.model_rebuild()
TeamRead.model_rebuild()


__all__ = [attr for attr in locals().keys() if not attr.startswith("_")]
