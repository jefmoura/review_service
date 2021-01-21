from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi_utils.api_model import APIModel


class ReviewAnswerResponse(APIModel):
    """Review Answer Response"""
    id: UUID
    text: str
    review_id: UUID
    creator_id: UUID
    create_date: datetime
    update_date: datetime


class ReviewAnswerCreate(APIModel):
    """Review Answer Create"""
    text: str


class ReviewAnswerUpdate(APIModel):
    """Review Answer Update"""
    text: Optional[str] = None
