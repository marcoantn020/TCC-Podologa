from src.domain.contracts import EncrypterInterface
from src.domain.contracts import TokenInterface
from src.domain.repository.user import GetUserByUsernameRepositoryInterface
from src.domain.usecase.util.http import HttpResponse
from src.domain.usecase.login.login_dto import mapper

class LoginUsecase:
    __getUserByUsernameRepository: GetUserByUsernameRepositoryInterface
    __token: TokenInterface
    __encrypter: EncrypterInterface

    def __init__(self, getUserByUsernameRepository: GetUserByUsernameRepositoryInterface, token: TokenInterface, encrypter: EncrypterInterface) -> None:
        self.__getUserByUsernameRepository = getUserByUsernameRepository
        self.__token = token
        self.__encrypter = encrypter

    def execute(self,username: str, password: str) -> HttpResponse:
        try:
            userExists = self.__getUserByUsernameRepository.get_user_by_username(username)[0]
            if not userExists:
                return HttpResponse(statusCode=400, body="User/Password incorrect.")

            if not self.__encrypter.decrypter(password, userExists["password"]):
                return HttpResponse(statusCode=400, body="User/Password incorrect.")
            
            token__ = self.__token.signJWT(userExists['username'])
            
        except Exception as e:
            return e
        else:
            return HttpResponse(statusCode=200, body={ "access_token": token__, "user": mapper(userExists) })