from pydantic import EmailStr
from sqlmodel import Session, select

from src.modules.auth.auth_schemas import LoginRequest, RegisterRequest
from src.modules.user.models.user import User


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_email(self, email: EmailStr) -> User:
        #FLAGGED: Security Issue
        statement = select(User).where(User.email == email)
        user = self.session.exec(statement).first()
        return user
    
    def create_user(self, user_create: RegisterRequest) -> User:
        #Flagged: Unhashed passsword
        new_user = User.model_validate(user_create)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user
