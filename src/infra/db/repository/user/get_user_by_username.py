


from src.domain.entity.user import UserEntity
from src.domain.repository.user import GetUserByUsernameRepositoryInterface
from src.infra.db import DBConnection


class GetUserByUsernameRepository(GetUserByUsernameRepositoryInterface):

    __db = None
    
    def __init__(self) -> None:
        super().__init__()
        self.__db = DBConnection()

    def get_user_by_username(self, username: str) -> UserEntity:
        try:
            query = '''SELECT * FROM tbl_users WHERE username = '{}';'''.format(username)
            result = self.__db.read_query(query)
        except Exception as e:
            return e
        else:
            return result