from __future__ import annotations
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.postgres import Base
from src.orms.test import TestORM



class Tests(Base):
    __tablename__ = "tests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    creator_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    

    def to_read_model(self):
        return TestORM(
            id=self.id,
            creator_id=self.creator_id,
        )
