from typing import List
from uuid import UUID

from fastapi.encoders import jsonable_encoder

from models import User
from mongo_db import get_database
from repository_exception import NotFoundRepositoryException
from user_repository import UserRepository


class UserMongoRepository(UserRepository):
    def __init__(self):
        db = get_database()
        self.collection_name = db["users"]

    def insert(self, user: User):
        self.collection_name.insert_one(jsonable_encoder(user))

    def get_all(self) -> List[User]:
        users = self.collection_name.find()
        results: List[User] = []
        for user in users:
            res = User(user['id'], user['full_name'], user['age'], user['gender'])
            results.append(res)
        return results

    def get_by_id(self, user_id: UUID) -> User:
        user = self.collection_name.find_one({"id": str(user_id)})
        if user is not None:
            return User(user['id'], user['full_name'], user['age'], user['gender'])

        raise NotFoundRepositoryException("user with ID {0} not found.".format(user_id))

    def update(self, user_id: UUID, new_user: User):
        update_result = self.collection_name.update_one({"id": str(user_id)}, {
            "$set": {"full_name": new_user.full_name, "age": new_user.age, "gender": str(new_user.gender)}})
        if update_result.modified_count < 1:
            raise NotFoundRepositoryException("user with ID {0} not found.".format(user_id))

    def delete(self, user_id: UUID):
        deleted_result = self.collection_name.delete_one({"id": str(user_id)})
        if deleted_result.deleted_count < 1:
            raise NotFoundRepositoryException("user with ID {0} not found.".format(user_id))
