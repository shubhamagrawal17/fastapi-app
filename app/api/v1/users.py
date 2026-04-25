from fastapi import APIRouter
from typing import List

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user(payload: UserCreate):
    return UserService.create_user(payload.name, payload.email)


@router.get("/", response_model=List[UserResponse])
def list_users():
    return UserService.get_users()
