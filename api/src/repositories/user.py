from src.models.user import User
from src.util.repository import SQLAlchemyRepository


class OperationUserRepository(SQLAlchemyRepository):
    model = User