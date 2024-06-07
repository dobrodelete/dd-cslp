from typing import List
from fastapi import APIRouter, HTTPException
from app.crud import submission_crud
from app.schemas import SubmissionCreate, SubmissionUpdate, SubmissionRead

router = APIRouter()


@router.post("/", response_model=SubmissionRead)
async def create_submission(submission: SubmissionCreate):
    return await submission_crud.create_submission(submission)


@router.get("/{submission_id}", response_model=SubmissionRead)
async def get_submission(submission_id: int):
    submission = await submission_crud.get_submission(submission_id)
    if submission is None:
        raise HTTPException(status_code=404, detail="Submission not found")
    return submission


@router.get("/", response_model=List[SubmissionRead])
async def get_submissions(skip: int = 0, limit: int = 100):
    return await submission_crud.get_submissions(skip, limit)


@router.put("/{submission_id}", response_model=SubmissionRead)
async def update_submission(submission: SubmissionUpdate):
    updated_submission = await submission_crud.update_submission(submission)
    if updated_submission is None:
        raise HTTPException(status_code=404, detail="Submission not found")
    return updated_submission


@router.delete("/{submission_id}", response_model=SubmissionRead)
async def delete_submission(submission_id: int):
    deleted_submission = await submission_crud.delete_submission(submission_id)
    if deleted_submission is None:
        raise HTTPException(status_code=404, detail="Submission not found")
    return deleted_submission
