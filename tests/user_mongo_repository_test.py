import unittest
from uuid import uuid4

from models.models import User, Gender
from repository.user_mongo_repository import UserMongoRepository
from repository.repository_exception import NotFoundRepositoryException


class MyTestCase(unittest.TestCase):
    def test_insert(self):
        user_to_insert = User(uuid4(), "Erik Rio Setiawan", 5, Gender.MALE)
        repo = UserMongoRepository()
        repo.insert(user_to_insert)
        user = repo.get_by_id(user_to_insert.id)

        self.assertEqual(str(user_to_insert.id), str(user.id))
        self.assertEqual(user_to_insert.gender, user.gender)
        self.assertEqual(user_to_insert.age, user.age)
        self.assertEqual(user_to_insert.full_name, user.full_name)

    def test_get_all(self):
        user_to_insert = User(uuid4(), "Erik Rio Setiawan", 5, Gender.MALE)
        repo = UserMongoRepository()
        repo.insert(user_to_insert)
        users = repo.get_all()

        self.assertGreater(len(users), 0)

    def test_get_by_id(self):
        user_to_insert = User(uuid4(), "Erik Rio Setiawan", 5, Gender.MALE)
        repo = UserMongoRepository()
        repo.insert(user_to_insert)
        user = repo.get_by_id(user_to_insert.id)

        self.assertEqual(str(user_to_insert.id), str(user.id))
        self.assertEqual(user_to_insert.gender, user.gender)
        self.assertEqual(user_to_insert.age, user.age)
        self.assertEqual(user_to_insert.full_name, user.full_name)

    def test_update(self):
        user_to_insert = User(uuid4(), "Erik Rio Setiawan", 5, Gender.MALE)
        repo = UserMongoRepository()
        repo.insert(user_to_insert)

        user_to_insert.full_name = "Test New Name"

        repo.update(user_to_insert.id, user_to_insert)

        user = repo.get_by_id(user_to_insert.id)

        self.assertEqual(str(user_to_insert.id), str(user.id))
        self.assertEqual(user_to_insert.gender, user.gender)
        self.assertEqual(user_to_insert.age, user.age)
        self.assertEqual(user_to_insert.full_name, user.full_name)

    def test_delete(self):
        with self.assertRaises(NotFoundRepositoryException):
            user_to_insert = User(uuid4(), "Erik Rio Setiawan", 5, Gender.MALE)
            repo = UserMongoRepository()
            repo.insert(user_to_insert)
            repo.delete(user_to_insert.id)

            repo.get_by_id(user_to_insert.id)


if __name__ == '__main__':
    unittest.main()
