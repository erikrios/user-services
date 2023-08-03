from typing import List
from uuid import UUID

from models import User
from repository_exception import UnimplementedRepositoryException


class UserRepository:

    def insert(self, user: User):
        raise UnimplementedRepositoryException()

    def get_all(self) -> List[User]:
        raise UnimplementedRepositoryException()

    def get_by_id(self, user_id: UUID) -> User:
        raise UnimplementedRepositoryException()

    def update(self, user_id: UUID, new_user: User):
        raise UnimplementedRepositoryException()

    def delete(self, user_id: UUID):
        raise UnimplementedRepositoryException()
