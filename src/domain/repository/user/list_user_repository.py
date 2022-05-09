from abc import ABC, abstractmethod
from typing import List
from src.domain.entity.user import UserEntity


class ListUserRepositoryInterface(ABC):

    @abstractmethod
    def list_users(self) -> List[UserEntity]:
        raise Exception("Method not implemented: list_users")