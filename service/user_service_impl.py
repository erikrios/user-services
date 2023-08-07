from typing import List
from uuid import UUID, uuid4

from httplayer.payload import CreateUserPayload, UpdateUserPayload
from models.models import User, Gender
from repository.repository_exception import NotFoundRepositoryException, UnimplementedRepositoryException
from repository.user_repository import UserRepository
from service.service_exception import UnimplementedServiceException, NotFoundServiceException, UnknownServiceException
from service.user_service import UserService


class UserServiceImpl(UserService):
    repo: UserRepository

    def __init__(self, _repo: UserRepository):
        self.repo = _repo

    def insert(self, user: CreateUserPayload) -> str:
        user_id = uuid4()
        add_user: User = User(user_id, user.full_name, user.age, user.gender)
        self.repo.insert(add_user)
        return str(user_id)

    def get_all(self) -> List[User]:
        return self.repo.get_all()

    def get_by_id(self, user_id: UUID) -> User:
        try:
            user = self.repo.get_by_id(user_id)
            return user
        except NotFoundRepositoryException as user_not_found_exception:
            raise NotFoundServiceException(str(user_not_found_exception))
        except UnimplementedRepositoryException:
            raise UnimplementedServiceException()
        except Exception as e:
            print(e)
            raise UnknownServiceException()

    def update(self, user_id: UUID, new_user: UpdateUserPayload):
        test: str
        if new_user.gender == "male":
            test = Gender.MALE
        else:
            test = Gender.FEMALE
        update_user: User = User(user_id, new_user.full_name, new_user.age,
                                 Gender.MALE if new_user.gender == "male" else Gender.FEMALE)
        try:
            self.repo.update(user_id, update_user)
        except NotFoundRepositoryException as user_not_found_exception:
            raise NotFoundServiceException(str(user_not_found_exception))
        except UnimplementedRepositoryException:
            raise UnimplementedServiceException()
        except Exception as e:
            print(e)
            raise UnknownServiceException()

    def delete(self, user_id: UUID):
        try:
            self.repo.delete(user_id)
        except NotFoundRepositoryException as user_not_found_exception:
            raise NotFoundServiceException(str(user_not_found_exception))
        except UnimplementedRepositoryException:
            raise UnimplementedServiceException()
        except Exception:
            raise UnknownServiceException()
