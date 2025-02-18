from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.configs.config import settings
from src.core.database import init_db
from src.api.api_router import router

app = FastAPI()

app.include_router(router, prefix=f"/api/{settings.API_VERSION}")


