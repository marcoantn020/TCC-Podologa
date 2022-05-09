from abc import ABC, abstractmethod


class CreateUserRepositoryInterface(ABC):

    @abstractmethod
    def create(self, name: str, username: str, password: str) -> None:
        raise Exception("Method not implemented: create")