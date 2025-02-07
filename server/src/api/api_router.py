from fastapi import APIRouter, FastAPI
from contextlib import asynccontextmanager
from src.database import init_db
from src.api.v0.auth import router as auth_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth")

@router.get("/")
def health_check():
    return "bug bounty is online"