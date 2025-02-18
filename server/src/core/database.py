from collections.abc import Generator
from sqlmodel import create_engine, SQLModel, Session
from src.configs.config import settings

from src.modules.user.models.user import User

engine = create_engine(settings.DATABASE_URL, echo=settings.DATABASE_ECHO)

def init_db():
    SQLModel.metadata.create_all(engine)
    print("Available tables:", list(SQLModel.metadata.tables.keys()))


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def reset_database():
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)

SQLModel.metadata.create_all(engine)

