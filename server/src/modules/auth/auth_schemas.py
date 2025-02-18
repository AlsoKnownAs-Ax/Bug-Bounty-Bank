from pydantic import BaseModel

from src.modules.user.user_schemas import UserResponse

#Flagged: Issue auth tokens
class LoginResponse(BaseModel):
    # token: str
    user: UserResponse
    
    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterResponse(BaseModel):
    # token: str
    user: UserResponse
    
    class Config:
        from_attributes = True

class RegisterRequest(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    ssn: str
    iban: str