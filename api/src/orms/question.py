from typing import Any, Dict, List, Optional, Type, TypeVar
from pydantic import BaseModel


class QuestionORM(BaseModel):
    id:int
    text:str
    answer:str
    test_id:int

class CreateQuestion(BaseModel):
    text:str
    answer:str
    test_id:str