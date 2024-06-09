from __future__ import annotations
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.postgres import UserORM
from src.orms.user import UserORM

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(SqlEnum(str))
    hashed_password: Mapped[str] = mapped_column(String())
    
    def to_read_model(self):
        return UserORM(
            id=self.id,
            email=self.email,
            name=self.name,
            role=self.role,
        )