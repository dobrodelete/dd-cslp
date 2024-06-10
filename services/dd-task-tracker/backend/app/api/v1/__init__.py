from fastapi import FastAPI, APIRouter
from app.api.v1.endpoints import (
    project_router,
    task_router,
    task_assignment_router,
    task_comment_router,
    task_status_router,
)

api_router = APIRouter()

api_router.include_router(project_router, prefix="/projects", tags=["Projects"])
api_router.include_router(task_router, prefix="/tasks", tags=["Tasks"])
api_router.include_router(task_assignment_router, prefix="/task_assignments", tags=["TaskAssignments"])
api_router.include_router(task_comment_router, prefix="/task_comments", tags=["TaskComments"])
api_router.include_router(task_status_router, prefix="/task_statuses", tags=["TaskStatuses"])
