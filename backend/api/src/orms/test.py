from typing import Any, Dict, List, Optional, Type, TypeVar
from pydantic import BaseModel
from src.orms.question import AnswerORM


class TestORM(BaseModel):
    id: int
    creator_id:int
    

class CreateTest(BaseModel):
    creator_id: int

