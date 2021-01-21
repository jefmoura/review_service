import jwt
import logging

from typing import Generator, List, Optional
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from pydantic import BaseModel

from app.core.config import settings
from app.db.session import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.AUTH_SERVICE_URL}/token/"
)

logger = logging.getLogger(__name__)


class RoleData(BaseModel):
    reference_id: Optional[UUID] = None
    scopes: List[str] = []


class UserData(BaseModel):
    id: Optional[UUID] = None
    roles: List[RoleData] = []


async def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_jwt_user(token: str = Depends(reusable_oauth2)) -> UserData:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    public_key = settings.JWT_PUBLIC_KEY_RSA
    if not public_key:
        logger.error('No public RSA key was set for JWT')
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    payload = jwt.decode(token, public_key, algorithms=['HS256', 'RS256'])
    user_id: UUID = UUID(payload.get('user_id', ''))
    if user_id == '':
        raise credentials_exception

    user_data = UserData(id=user_id, roles=payload.get("roles", []))

    return user_data
