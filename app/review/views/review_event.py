from typing import List
from uuid import UUID

from fastapi import HTTPException, status

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from app.core.viewset import ProtectedViewSet

from app.review.crud import CRUDReviewEvent
from app.review.models import ReviewEvent
from app.review.serializers.review_event import ReviewEventCreate, ReviewEventResponse

review_event_router = InferringRouter()


@cbv(review_event_router)
class ReviewEventViewSet(ProtectedViewSet):
    model = ReviewEvent
    crud = CRUDReviewEvent

    @review_event_router.post("/review/{review_id}/event")
    def create(self, review_id: UUID, review_event: ReviewEventCreate) -> ReviewEventResponse:
        review_event_orm = self.service.create_with_creator_and_review_id(
            creator_id=self.user.id, review_id=review_id, obj_in=review_event)
        return ReviewEventResponse.from_orm(review_event_orm)

    @review_event_router.get("/review/{review_id}/report")
    def list_reports(self, review_id: UUID) -> List[ReviewEventResponse]:
        review_events_orm = self.service.list_review_reports(review_id=review_id)

        review_events: List[ReviewEventResponse] = list()
        for review_event_orm in review_events_orm:
            review_events.append(ReviewEventResponse.from_orm(review_event_orm))

        return review_events

    @review_event_router.delete("/review/{review_id}/event/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete(self, review_id: UUID, event_id: UUID):
        review_event_orm = self.service.get(id=event_id)
        if not review_event_orm:
            raise HTTPException(status_code=404, detail="ReviewEvent not found")

        _ = self.service.remove(id=event_id)
