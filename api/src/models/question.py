from __future__ import annotations
from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from src.db.postgres import Base
from src.orms.question import QuestionORM


class Questions(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    question: Mapped[str] = mapped_column(String)
    answer: Mapped[str] = mapped_column(String)
    test_id: Mapped[int] = mapped_column(ForeignKey("tests.id"))

    def to_read_model(self):
        return QuestionORM(
            id=self.id,
            question=self.question,
            answer=self.answer,
            test_id=self.test_id,
        )