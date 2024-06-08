from __future__ import annotations
from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from src.db.postgres import Base
from src.orms.orms import AnswerORM


class Answers(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    answer: Mapped[str] = mapped_column(String)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def to_read_model(self):
        return AnswerORM(
            id=self.id,
            answer=self.answer,
            student_id=self.student_id,
        )