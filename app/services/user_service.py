from typing import List
from app.models.user import User
from app.db.fake_db import DB


class UserService:

    @staticmethod
    def create_user(name: str, email: str) -> User:
        user = User(id=len(DB) + 1, name=name, email=email)
        DB.append(user)
        return user

    @staticmethod
    def get_users() -> List[User]:
        return DB
