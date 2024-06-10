from .base import CrudBase
from .project import ProjectCrud
from .task import TaskCrud
from .task_assignment import TaskAssignmentCrud
from .task_comment import TaskCommentCrud
from .task_status import TaskStatusCrud

project_crud = ProjectCrud()
task_crud = TaskCrud()
task_assignment_crud = TaskAssignmentCrud()
task_comment_crud = TaskCommentCrud()
task_status_crud = TaskStatusCrud()

__all__ = [attr for attr in locals().keys() if not attr.startswith("_")]
