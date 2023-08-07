from enum import Enum
from uuid import UUID


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"

    def __str__(self):
        if self.value == Gender.MALE:
            return "male"
        else:
            return "female"


class User:
    id: UUID
    full_name: str
    age: int
    gender: Gender

    def __init__(self, _id: UUID, _full_name: str, _age: int, _gender: Gender):
        self.id = _id
        self.full_name = _full_name
        self.age = _age
        self.gender = _gender

    def __str__(self):
        user = '''ID = {0}
        Full Name = {1}
        Age = {2}
        Gender = {3}
        '''.format(self.id, self.full_name, self.age, self.gender)
        return user
