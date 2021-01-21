from typing import Type, TypeVar

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.crud import CRUDBase, ModelType
from app.core.utils import get_db, get_jwt_user, UserData

CRUDType = TypeVar("CRUDType", bound=CRUDBase)


class GenericViewSet:
    session: Session = Depends(get_db)
    model: Type[ModelType]
    crud: Type[CRUDType]

    @property
    def service(self):
        return self.crud(self.model, self.session)


class ProtectedViewSet(GenericViewSet):
    user: UserData = Depends(get_jwt_user)
