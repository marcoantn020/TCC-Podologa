
from datetime import date
from email.policy import default
from pydantic import BaseModel, Field


class UserInput(BaseModel):
    name: str = Field(default=None)
    username: str = Field(default=None)
    password: str = Field(default=None)
    passwordConfirmation: str = Field(default=None)

    class Config:
        user_schema = {
            "user_demo": {
                "name": "john Doe",
                "username": "johnDoe",
                "password": "123456",
                "passwordConfirmation": "123456"
            }
        }

class UserOutput(BaseModel):
    id: int
    name: str
    username: str
    created_at: date
    updated_at: date

    class Config:
        user_schema = {
            "user_demo": {
                "id": 1,
                "name": "john Doe",
                "username": "johnDoe",
                "created_at": "2022-04-21 19:25:40",
                "updated_at": "2022-04-21 19:25:40"
            }
        }

class UserCreated(BaseModel):
    id: int   

    class Config:
        user_create_schema = {
            "user_create_demo": {
                "id" : 1
            }
        }