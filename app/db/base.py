# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.review.models import Review, ReviewAnswer, ReviewEvent  # noqa
