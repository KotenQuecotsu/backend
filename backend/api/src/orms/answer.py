from typing import Any, Dict, List, Optional, Type, TypeVar
from pydantic import BaseModel


class AnswerORM(BaseModel):
    id:int
    answer:str
    student_id:int

class CreateAnswerORM(BaseModel):
    answer:str
    student_id:int