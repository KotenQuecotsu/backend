from fastapi import APIRouter, Depends
from src.orms.user import UserORM, CreateUser
from src.utils.users import fastapi_users, auth_backend

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserORM, CreateUser),
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
)