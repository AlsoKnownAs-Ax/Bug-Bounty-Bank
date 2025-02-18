from datetime import datetime
from uuid import UUID, uuid4
from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default=uuid4, primary_key=True, index=True)
    email: EmailStr = Field(unique=True, index=True)
    password: str
    username: str
    first_name: str
    last_name: str
    ssn: str
    iban: str
    balance: float = 0.0
    admin_level: int = 0

    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.now, 
        nullable=False, 
        sa_column_kwargs={"onupdate": datetime.now}
    )