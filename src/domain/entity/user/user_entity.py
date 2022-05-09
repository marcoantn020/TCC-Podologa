from datetime import datetime


class UserEntity:
    __id: int
    __name: str
    __username: int
    __password: str
    __created_at: str
    __updated_at: int
    

    def __init__ (self, id: int, name: str, username: str, password: str) -> None:
        self.__id = id
        self.__name = name
        self.__username = username
        self.__password = password
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
    

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @property
    def updated_at(self) -> datetime:
        return self.__updated_at