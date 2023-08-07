from typing import Literal

from pydantic import BaseModel

from models.models import Gender


class CreateUserPayload(BaseModel):
    full_name: str
    age: int
    gender: Gender


class UpdateUserPayload(BaseModel):
    full_name: str
    age: int
    gender: Literal['male', 'female']
