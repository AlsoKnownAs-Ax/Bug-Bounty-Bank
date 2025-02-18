from pydantic import EmailStr
from sqlmodel import Session

from src.modules.auth.auth_schemas import LoginRequest
from src.modules.user.models.user import User


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_email(self, email: EmailStr) -> User:
        #FLAGGED: Security Issue
        statement = f"SELECT * FROM users WHERE email = '{email}'"
        user = self.session.exec(statement).first()
        return user
    
    def create_user(self, user: User) -> User:
        #Flagged: Unhashed passsword
        new_user = User.model_validate(user)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return user