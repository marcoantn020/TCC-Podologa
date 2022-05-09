
from src.domain.contracts import EncrypterInterface
from src.domain.usecase.util import HttpResponse
from src.domain.repository.user import CreateUserRepositoryInterface
from src.domain.repository.user import GetUserByUsernameRepositoryInterface


class CreateUserUsecase:
    __createUserRepository: CreateUserRepositoryInterface
    __getUserByUsernameRepository: GetUserByUsernameRepositoryInterface
    __encrypter: EncrypterInterface

    def __init__(self, createUserRepository: CreateUserRepositoryInterface, getUserByUsernameRepository: GetUserByUsernameRepositoryInterface, encrypter: EncrypterInterface) -> None:
        self.__createUserRepository = createUserRepository
        self.__getUserByUsernameRepository = getUserByUsernameRepository
        self.__encrypter = encrypter

    def execute(self, name: str, username: str, password: str, passwordConfirmation: str) -> HttpResponse:
        try:
            if password != passwordConfirmation:
                return HttpResponse(statusCode=400, body="passwords are not the same")
            
            userExists = self.__getUserByUsernameRepository.get_user_by_username(username)
            if userExists:
                return HttpResponse(statusCode=400, body="this user already exists")
                
            passwordHashed = self.__encrypter.encrypter(password)
            response = self.__createUserRepository.create(name, username, passwordHashed)
        except Exception as e:
            return e
        else:
            return HttpResponse(statusCode=401, body={"id": response})