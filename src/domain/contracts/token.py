from abc import ABC, abstractmethod


class TokenInterface(ABC):

    @abstractmethod
    def signJWT(value: str):
        raise Exception("Method not implemented: signJWT")

    @abstractmethod
    def decodeJWT(value: str):
        raise Exception("Method not implemented: verify_access_token")