from abc import ABC, abstractmethod
from src.domain.entity.user import UserEntity


class GetUserByUsernameRepositoryInterface(ABC):

    @abstractmethod
    def get_user_by_username(username: str) -> UserEntity:
        raise Exception("Method not implemented: get_user_by_username")