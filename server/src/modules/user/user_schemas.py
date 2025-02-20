from uuid import UUID
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: UUID
    email: str
    admin_level: int
    first_name: str
    last_name: str
    ssn: str
    balance: float
    iban: str