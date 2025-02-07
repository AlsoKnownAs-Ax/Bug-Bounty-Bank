from pydantic import BaseModel

from src.modules.user.user_schemas import UserResponse


class LoginResponse(BaseModel):
    token: str
    user: UserResponse
    
    class Config:
        orm_mode = True