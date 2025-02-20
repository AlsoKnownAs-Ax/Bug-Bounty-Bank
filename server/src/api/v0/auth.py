from fastapi import APIRouter, HTTPException, status
from pydantic import EmailStr
from src.core.deps import SessionDep
from src.modules.user.user_deps import UserServiceDep
from src.modules.auth.auth_schemas import GetUserRequest, LoginRequest, LoginResponse, RegisterRequest, RegisterResponse


router = APIRouter()


@router.post('/login', response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login_user(
    login_data: LoginRequest,
    user_service: UserServiceDep
) -> LoginResponse:
    """
    Login a user with the given user data.
    """
    user = user_service.get_user_by_email(login_data.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )
    
    if user.password != login_data.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid password"
        )
    
    return LoginResponse(user=user.model_dump())    

@router.post('/register', response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def register_user(
    register_data: RegisterRequest,
    user_service: UserServiceDep
) -> RegisterResponse:
    """
    Register a new user with the given user data.
    """
    existing_user = user_service.get_user_by_email(register_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User already exists"
        )
    
    new_user = user_service.create_user(register_data)
    if new_user:
        return RegisterResponse(user=new_user.model_dump())

#Flagged: Security issue: one can call the API with other emails and get the user data
@router.get('/current-user', response_model=LoginResponse, status_code=status.HTTP_200_OK)
def get_current_user(
    data: GetUserRequest,
    user_service: UserServiceDep
) -> LoginResponse:
    """
    Get the current user by email.
    """
    user = user_service.get_user_by_email(data.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )
    
    return LoginResponse(user=user.model_dump())
