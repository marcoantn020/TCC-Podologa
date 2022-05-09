

from src.domain.usecase.util import HttpResponse
from src.domain.repository.user import ListUserRepositoryInterface


class ListUserUsecase:
    __listUserRepository: ListUserRepositoryInterface

    def __init__(self, listUserRepository: ListUserRepositoryInterface) -> None:
        self.__listUserRepository = listUserRepository

    def execute(self) -> HttpResponse:
        try:
            response = self.__listUserRepository.list_users()
            if not response:
                return HttpResponse(statusCode=204, body=None)
        except Exception as e:
            return e
        else:
            return HttpResponse(statusCode=200, body=response)