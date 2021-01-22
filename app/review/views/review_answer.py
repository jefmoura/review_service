from uuid import UUID

from fastapi import HTTPException, status

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sdk_fastapi.views.viewset import ProtectedViewSet

from app.review.crud import CRUDReviewAnswer
from app.review.models import ReviewAnswer
from app.review.serializers.review_answer import ReviewAnswerCreate, ReviewAnswerUpdate, ReviewAnswerResponse

review_answer_router = InferringRouter()


@cbv(review_answer_router)
class ReviewAnswerViewSet(ProtectedViewSet):
    model = ReviewAnswer
    crud = CRUDReviewAnswer

    @review_answer_router.post("/review/{id}/answer")
    def create(self, id: UUID, review_answer: ReviewAnswerCreate) -> ReviewAnswerResponse:
        review_answer_orm = self.service.create_with_creator_and_id(
            creator_id=self.user.id, id=id, obj_in=review_answer)
        return ReviewAnswerResponse.from_orm(review_answer_orm)

    @review_answer_router.put("/review/{id}/answer/{answer_id}")
    def update(self, id: UUID, answer_id: UUID, review_answer: ReviewAnswerUpdate) -> ReviewAnswerResponse:
        review_answer_orm = self.service.get(id=answer_id)
        if not review_answer_orm:
            raise HTTPException(status_code=404, detail="ReviewAnswer not found")

        review_answer_orm = self.service.update(db_obj=review_answer_orm, obj_in=review_answer)
        return ReviewAnswerResponse.from_orm(review_answer_orm)

    @review_answer_router.delete("/review/{id}/answer/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete(self, id: UUID, answer_id: UUID):
        review_answer_orm = self.service.get(id=answer_id)
        if not review_answer_orm:
            raise HTTPException(status_code=404, detail="ReviewAnswer not found")

        _ = self.service.remove(id=answer_id)
