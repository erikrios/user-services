from typing import List
from uuid import UUID

from models import User
from payload import UpdateUserPayload, CreateUserPayload
from service_exception import UnimplementedServiceException


class UserService:

    def insert(self, user: CreateUserPayload) -> str:
        raise UnimplementedServiceException()

    def get_all(self) -> List[User]:
        raise UnimplementedServiceException()

    def get_by_id(self, user_id: UUID) -> User:
        raise UnimplementedServiceException()

    def update(self, user_id: UUID, new_user: UpdateUserPayload):
        raise UnimplementedServiceException()

    def delete(self, user_id: UUID):
        raise UnimplementedServiceException()
