from typing import Generic, Optional
from fastapi import Depends, HTTPException, Request, Response

from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models

from src.repositories.user import OperationUserRepository
from src.orms.user import CreateUser
from src.db.postgres import async_session_maker
from conf import SECRET_AUTH
from src.utils.auth import get_user_db
from src.models.user import User


class UserManager(Generic[models.UP, models.ID], IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH

    async def on_after_login(self, user: User, request: Optional[Request] = None, response: Optional[Response] = None):
        print(f"User {user.id} logged in.")

    async def create(
        self,
        user_create: CreateUser,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = user_create.model_dump()
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        created_user = await OperationUserRepository().add_one(user_dict)

        
        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)