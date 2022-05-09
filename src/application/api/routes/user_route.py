
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from src.application.controller.user import ListUserController
from src.application.api.schemas.user import UserCreated, UserInput, UserOutput 
from src.application.controller.user import CreateUserController
from src.infra.auth.jwt_bearer import JWTBearer

router = APIRouter()
tag = "User"

@router.post("/user/create", tags=[tag], status_code=201, response_model=UserCreated)
def create_user(user: UserInput):
    new_user = CreateUserController.handle(user)
    if new_user.statusCode == 400:
        raise HTTPException(status_code=new_user.statusCode, detail=new_user.body)
    return new_user.body

@router.get("/user/list", tags=[tag], dependencies=[Depends(JWTBearer())], status_code=200, response_model=List[UserOutput])
def list():
    list_users = ListUserController.handle()
    if list_users.statusCode == 204:
        raise HTTPException(status_code=list_users.statusCode, detail=list_users.body)
    return list_users.body