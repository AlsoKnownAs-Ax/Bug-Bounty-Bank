from fastapi import APIRouter, HTTPException, status
from src.modules.auth.auth_schemas import LoginResponse


router = APIRouter()


@router.post('/login', response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login():
    pass