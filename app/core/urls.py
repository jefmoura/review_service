from fastapi import APIRouter

from app.review.views.review import review_router
from app.review.views.review_answer import review_answer_router
from app.review.views.review_event import review_event_router

api_router = APIRouter()

api_router.include_router(review_router, tags=["review"])
api_router.include_router(review_answer_router, tags=["review"])
api_router.include_router(review_event_router, tags=["review"])

