
from fastapi import APIRouter, HTTPException
from src.application.controller.login import LoginController
from src.application.api.schemas.login import LoginInput, ResponseToken

router = APIRouter()
tag = "Login"

@router.post("/login", tags=[tag], status_code=200, response_model=ResponseToken)
def login(user: LoginInput):
    login_generate = LoginController.handle(user)
    if login_generate.statusCode == 400:
        raise HTTPException(status_code=login_generate.statusCode, detail=login_generate.body)
    return login_generate.body
