from typing import Annotated
from fastapi import Depends
from sqlmodel import Session

from src.core.deps import SessionDep

from .user_service import UserService

def get_user_service(db: SessionDep) -> UserService:
    """Dependency to provide a UserService instance."""
    return UserService(db)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]