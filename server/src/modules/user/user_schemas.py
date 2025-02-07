from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    email: str
    is_admin: bool
    first_name: str
    last_name: str
    ssn: str
    balance: float
    iban: str
