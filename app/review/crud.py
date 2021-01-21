from typing import List
from uuid import UUID

from fastapi.encoders import jsonable_encoder

from app.db.crud import CRUDBase
from app.review.models import Review, ReviewAnswer, ReviewEvent, ReviewEventType
from app.review.serializers.review import ReviewCreate, ReviewUpdate
from app.review.serializers.review_answer import ReviewAnswerCreate, ReviewAnswerUpdate
from app.review.serializers.review_event import ReviewEventCreate


class CRUDReview(CRUDBase[Review, ReviewCreate, ReviewUpdate]):
    def list_by_reference_id(self, *, reference_id: UUID, skip: int = 0, limit: int = 100) -> List[Review]:
        return (
            self.db.query(self.model)
            .filter(self.model.reference_id == reference_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create_with_creator_id(self, *, creator_id: UUID, obj_in: ReviewCreate) -> Review:
        obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        db_obj = self.model(**obj_in_data, creator_id=creator_id)  # type: ignore
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj


class CRUDReviewAnswer(CRUDBase[ReviewAnswer, ReviewAnswerCreate, ReviewAnswerUpdate]):
    def create_with_creator_and_review_id(
            self,
            *,
            creator_id: UUID,
            review_id: UUID,
            obj_in: ReviewAnswerCreate
    ) -> ReviewAnswer:

        obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        db_obj = self.model(**obj_in_data, creator_id=creator_id, review_id=review_id)  # type: ignore
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj


class CRUDReviewEvent(CRUDBase[ReviewEvent, ReviewEventCreate, None]):
    def list_review_reports(self, *, review_id: UUID, skip: int = 0, limit: int = 100) -> List[ReviewEvent]:
        return (
            self.db.query(self.model)
                .filter(self.model.review_id == review_id, self.model.type == ReviewEventType.REPORT)
                .offset(skip)
                .limit(limit)
                .all()
        )

    def create_with_creator_and_review_id(
            self,
            *,
            creator_id: UUID,
            review_id: UUID,
            obj_in: ReviewEventCreate
    ) -> ReviewEvent:
        obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        db_obj = self.model(**obj_in_data, creator_id=creator_id, review_id=review_id)  # type: ignore
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
