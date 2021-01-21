from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi_utils.api_model import APIModel

from app.review.serializers.review_answer import ReviewAnswerResponse


class ReviewResponse(APIModel):
    """Review Response"""
    id: UUID
    text: Optional[str] = None
    reference_id: UUID
    creator_id: UUID
    rate: float
    review_answer: Optional[ReviewAnswerResponse] = None
    create_date: datetime
    update_date: datetime


class ReviewCreate(APIModel):
    """Review Create"""
    text: Optional[str] = None
    reference_id: UUID
    rate: float


class ReviewUpdate(APIModel):
    """Review Update"""
    text: Optional[str] = None
    rate: Optional[float] = None
