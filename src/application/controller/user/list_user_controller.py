

from abc import abstractmethod
from src.domain.usecase.user import ListUserUsecase
from src.infra.db.repository.user import ListUserRepository


class ListUserController:

    @abstractmethod
    def handle():
        list_user_repository = ListUserRepository()
        list_user_usecase = ListUserUsecase(list_user_repository)
        users = list_user_usecase.execute()
        return users