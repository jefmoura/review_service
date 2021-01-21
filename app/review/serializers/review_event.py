from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi_utils.api_model import APIModel

from app.review.models import ReviewEventType


class ReviewEventResponse(APIModel):
    """Review Event Response"""
    id: UUID
    text: Optional[str] = None
    type: ReviewEventType
    review_id: UUID
    creator_id: UUID
    create_date: datetime
    update_date: datetime


class ReviewEventCreate(APIModel):
    """Review Event Create"""
    text: Optional[str] = None
    type: ReviewEventType
