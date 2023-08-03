from pydantic import BaseModel

from models import Gender


class CreateUserPayload(BaseModel):
    full_name: str
    age: int
    gender: Gender


class UpdateUserPayload(BaseModel):
    full_name: str
    age: int
    gender: Gender
