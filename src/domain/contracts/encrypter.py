from abc import ABC, abstractmethod


class EncrypterInterface(ABC):

    @abstractmethod
    def encrypter(value: str) -> str:
        raise Exception("Method not implemented: encrypter")

    @abstractmethod
    def decrypter(value: str, hash) -> bool:
        raise Exception("Method not implemented: decrypter")

