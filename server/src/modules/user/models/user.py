from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import EmailStr
from sqlmodel import Field, SQLModel
import secrets

def generate_iban() -> str:
    """Generate a random IBAN-like string for testing purposes"""
    country_code = "NL"
    random_digits = ''.join(str(secrets.randbelow(10)) for _ in range(16))
    return f"{country_code}{random_digits}"

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    email: EmailStr = Field(unique=True, index=True)
    password: str
    first_name: str
    last_name: str
    ssn: str
    iban: str = Field(default_factory=generate_iban)
    balance: float = 0.0
    admin_level: int = 0

    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.now, 
        nullable=False, 
        sa_column_kwargs={"onupdate": datetime.now}
    )