from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

DB_URL = "postgresql+asyncpg://postgres:h6lld6m6n@localhost:5432/postgres"

engine = create_async_engine(DB_URL)
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


@asynccontextmanager
async def get_async_session():
    async with async_session_maker() as session:
        yield session
