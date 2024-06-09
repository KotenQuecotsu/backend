from typing import Any, Dict, List, Optional, Type, TypeVar
from pydantic import BaseModel


class AnswerORM(BaseModel):
    id:int
    answer:str
    student_id:int

class CreateAnswer(BaseModel):
    answer:str
    student_id:int