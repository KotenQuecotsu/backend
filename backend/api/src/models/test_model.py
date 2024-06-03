from __future__ import annotations


from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.postgres import Base
from src.orms.orms import *


class Tests(Base):
    __tablename__ = "tests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    creator_id: Mapped[str] = mapped_column(ForeignKey("professors.id"))
    

    def to_read_model(self):
        return TestORM(
            id=self.id,
            creator_id=self.creator_id,
        )

class Questions(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    question: Mapped[str] = mapped_column(String)
    answer: Mapped[str] = mapped_column(String)
    test_id: Mapped[int] = mapped_column(ForeignKey("tests.id"))

class Answers(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    answer: Mapped[str] = mapped_column(String)
    student_id: Mapped[int] = mapped_column(ForeignKey("tests.id"))