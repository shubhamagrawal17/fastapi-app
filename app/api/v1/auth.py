import os

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException

from app.core.security import create_access_token

load_dotenv()

router = APIRouter(prefix="/auth", tags=["Auth"])

USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")


@router.post("/login")
def login(data: dict):

    if (
        data.get("username") != USERNAME
        or data.get("password") != PASSWORD
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token({
        "sub": data["username"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
