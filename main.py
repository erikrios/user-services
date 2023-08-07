import os
from typing import List
from uuid import UUID

from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse

from httplayer.http_exception import handle_exception
from httplayer.payload import CreateUserPayload, UpdateUserPayload
from models.models import User
from repository.user_mongo_repository import UserMongoRepository
from repository.user_repository import UserRepository
from service.user_service import UserService
from service.user_service_impl import UserServiceImpl

app = FastAPI()
open_app = FastAPI()
secured_app = FastAPI()

repo: UserRepository = UserMongoRepository()
service: UserService = UserServiceImpl(repo)


@secured_app.middleware("httplayer")
async def api_key_middleware(request: Request, call_next):
    if request.headers.get('API-KEY') != os.getenv("API_KEY"):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content={"detail": "Please provide correct API-Key"})
    else:
        return await call_next(request)


@open_app.get("/")
async def root():
    return {"message": "Hello, World!"}


@open_app.get("/ping")
async def ping():
    return {"status": "up"}


@secured_app.get("/users")
async def get_users():
    users: List[User] = service.get_all()
    return {
        "status": "success",
        "message": "successfully get users",
        "data": users
    }


@secured_app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserPayload):
    user_id: str = service.insert(user)
    return {
        "status": "success",
        "message": "successfully create users",
        "data": {
            "id": user_id
        }
    }


@secured_app.get("/users/{user_id}")
async def get_user(user_id: UUID):
    try:
        user: User = service.get_by_id(user_id)
        return {
            "status": "success",
            "message": "successfully get user",
            "data": {
                "user": user
            }
        }
    except Exception as e:
        handle_exception(e)


@secured_app.put("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(user_id: UUID, user: UpdateUserPayload):
    try:
        service.update(user_id, user)
    except Exception as e:
        handle_exception(e)


@secured_app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: UUID):
    try:
        service.delete(user_id)
    except Exception as e:
        handle_exception(e)


app.mount("/api/v1", secured_app)
app.mount("/", open_app)
