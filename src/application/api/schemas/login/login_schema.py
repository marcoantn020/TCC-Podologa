from pydantic import BaseModel, Field
from src.application.api.schemas.user import UserOutput


class LoginInput(BaseModel):
    username: str = Field(default=None)
    password: str = Field(default=None)

    class Config:
        login_schema = {
            "login_demo": {
                "username": "johnDoe",
                "password": "*********"
            }
        }

class ResponseToken(BaseModel):
    access_token: str
    user: UserOutput