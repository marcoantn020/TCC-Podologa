


from typing import List
from src.infra.db import DBConnection
from src.domain.entity.user import UserEntity
from src.domain.repository.user import ListUserRepositoryInterface


class ListUserRepository(ListUserRepositoryInterface):

    __db = None
    def __init__(self) -> None:
        super().__init__()
        self.__db = DBConnection()

    def list_users(self) -> List[UserEntity]:
        try:
            query = '''SELECT * FROM tbl_users;'''
            result = self.__db.read_query(query)
        except Exception as e:
            return e
        else:
            return result