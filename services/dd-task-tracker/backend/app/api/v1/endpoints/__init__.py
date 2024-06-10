from .project import router as project_router
from .task import router as task_router
from .task_assignment import router as task_assignment_router
from .task_comment import router as task_comment_router
from .task_status import router as task_status_router

__all__ = [
    "project_router",
    "task_router",
    "task_assignment_router",
    "task_comment_router",
    "task_status_router",
]
