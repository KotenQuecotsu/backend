from typing import Any, Dict, List, Optional, Type, TypeVar
from pydantic import BaseModel


class UserORM(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    role: Role


class CreateUser(CreateUpdateDictModel):
    email: str
    first_name: str
    last_name: str
    role: Role
    password: str