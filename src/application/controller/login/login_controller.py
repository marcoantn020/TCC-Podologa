


from abc import abstractmethod
from src.domain.usecase.login import LoginUsecase
from src.infra.auth.jwt_generated import JWTTokenGenerated
from src.infra.db.repository.user import GetUserByUsernameRepository
from src.infra.helper.encrypter import Encrypter

class LoginController:

    @abstractmethod
    def handle(input: dict ):
        get_user_by_username_repository = GetUserByUsernameRepository()
        token = JWTTokenGenerated()
        encrypter = Encrypter()
        login = LoginUsecase(get_user_by_username_repository, token, encrypter)
        user = login.execute(
            username=input.username,
            password=input.password
        )
        return user