

from abc import abstractmethod
from src.domain.usecase.user import CreateUserUsecase

from src.infra.db.repository.user import CreateUserRepository
from src.infra.db.repository.user import GetUserByUsernameRepository
from src.infra.helper.encrypter import Encrypter


class CreateUserController:

    @abstractmethod
    def handle(input: dict ):
        create_user_repository = CreateUserRepository()
        get_userrepository = GetUserByUsernameRepository()
        encrypter = Encrypter()
        create_user_usecase = CreateUserUsecase(create_user_repository,get_userrepository, encrypter)
        user = create_user_usecase.execute(
            name=input.name,
            username=input.username,
            password=input.password,
            passwordConfirmation=input.passwordConfirmation
        )
        return user