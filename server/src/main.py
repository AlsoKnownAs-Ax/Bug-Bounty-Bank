from fastapi import FastAPI
from contextlib import asynccontextmanager

from fastapi.routing import APIRoute
from src.configs.config import settings
from src.core.database import init_db, reset_database
from src.api.api_router import router

def custom_generate_unique_id(route: APIRoute) -> str:
    tag = route.tags[0] if route.tags else "default"
    return f"{tag}-{route.name}"

@asynccontextmanager
async def lifespan(app: FastAPI):
    reset_database()
    init_db()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    lifespan=lifespan,
    openapi_url=f"/{settings.VERSION}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id
)


app.include_router(router, prefix=f"{settings.API_V0_STR}")
