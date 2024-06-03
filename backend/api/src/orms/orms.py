from typing import Optional, List
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class TestORM(BaseModel):
    id: int
    creator_id:int

class QuestionORM(BaseModel):
    id:int
    text:str
    answer:str
    test_id:int

class AnswerORM(BaseModel):
    id:int
    answer:str
    student_id:int


