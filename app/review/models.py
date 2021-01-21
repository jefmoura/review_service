import enum
import uuid

from datetime import datetime

from sqlalchemy import DateTime, Float, Text, Column, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM, UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class ReviewEventType(str, enum.Enum):
    LIKE = 'like'
    REPORT = 'report'


class Review(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    text = Column(Text, nullable=True)
    rate = Column(Float, nullable=False)
    reference_id = Column(UUID(as_uuid=True), nullable=False, doc="It's a course or provider id")
    review_answer = relationship("ReviewAnswer", uselist=False, back_populates="review")
    creator_id = Column(UUID(as_uuid=True), nullable=False)
    create_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=datetime.now)


class ReviewAnswer(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    text = Column(Text, nullable=False)
    review_id = Column(UUID(as_uuid=True), ForeignKey("review.id", ondelete="CASCADE"), nullable=False)
    review = relationship("Review", back_populates="review_answer")
    creator_id = Column(UUID(as_uuid=True), nullable=False)
    create_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=datetime.now)


class ReviewEvent(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    text = Column(Text, nullable=True)
    type = Column(ENUM(ReviewEventType), nullable=False)
    review_id = Column(UUID(as_uuid=True), ForeignKey("review.id", ondelete="CASCADE"), nullable=False)
    creator_id = Column(UUID(as_uuid=True), nullable=False)
    create_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=datetime.now)
