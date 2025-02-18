from fastapi import APIRouter, HTTPException, status
from src.core.deps import SessionDep
from src.modules.user.user_deps import UserServiceDep
from src.modules.auth.auth_schemas import LoginRequest, LoginResponse, RegisterRequest, RegisterResponse


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
    
    return LoginResponse(user=user)    

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
        return RegisterResponse(user=new_user)

