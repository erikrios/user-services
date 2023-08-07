from typing import List
from uuid import UUID

from models.models import User
from repository.repository_exception import NotFoundRepositoryException
from user_repository import UserRepository


class UserMemoryRepository(UserRepository):
    users: List[User]

    def __init__(self):
        self.users = []

    def insert(self, user: User):
        self.users.append(user)

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, user_id: UUID) -> User:
        for user in self.users:
            if user.id.int == user_id.int:
                return user

        raise NotFoundRepositoryException("user with ID {0} not found.".format(user_id))

    def update(self, user_id: UUID, new_user: User):
        user: User = self.get_by_id(user_id)

        user.gender = new_user.gender
        user.full_name = new_user.full_name
        user.age = new_user.age

    def delete(self, user_id: UUID):
        user: User = self.get_by_id(user_id)
        self.users.remove(user)
