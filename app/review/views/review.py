from typing import List
from uuid import UUID

from fastapi import HTTPException, status

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from app.core.permissions import HasReferenceAccess
from app.core.viewset import GenericViewSet, ProtectedViewSet

from app.review.crud import CRUDReview
from app.review.models import Review
from app.review.serializers.review import ReviewCreate, ReviewUpdate, ReviewResponse

review_router = InferringRouter()


@cbv(review_router)
class ReviewViewSet(ProtectedViewSet):
    model = Review
    crud = CRUDReview
    permission_classes = (HasReferenceAccess, )

    @review_router.post("/review")
    def create(self, review: ReviewCreate) -> ReviewResponse:
        review_orm = self.service.create_with_creator_id(creator_id=self.user.id, obj_in=review)
        return ReviewResponse.from_orm(review_orm)

    @review_router.put("/review/{review_id}")
    def update(self, review_id: UUID, review: ReviewUpdate) -> ReviewResponse:
        review_orm = self.service.get(id=review_id)
        if not review_orm:
            raise HTTPException(status_code=404, detail="Review not found")

        review_orm = self.service.update(db_obj=review_orm, obj_in=review)
        return ReviewResponse.from_orm(review_orm)

    @review_router.delete("/review/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete(self, review_id: UUID):
        review_orm = self.service.get(id=review_id)
        if not review_orm:
            raise HTTPException(status_code=404, detail="Review not found")

        _ = self.service.remove(id=review_id)


@cbv(review_router)
class PublicReviewViewSet(GenericViewSet):
    model = Review
    crud = CRUDReview

    @review_router.get("/review/{review_id}")
    def get(self, review_id: UUID) -> ReviewResponse:
        review_orm = self.service.get(id=review_id)
        if not review_orm:
            raise HTTPException(status_code=404, detail="Review not found")
        return ReviewResponse.from_orm(review_orm)

    @review_router.get("/review")
    def list(self) -> List[ReviewResponse]:
        reviews_orm = self.service.list()

        reviews: List[ReviewResponse] = list()
        for review_orm in reviews_orm:
            reviews.append(ReviewResponse.from_orm(review_orm))

        return reviews
