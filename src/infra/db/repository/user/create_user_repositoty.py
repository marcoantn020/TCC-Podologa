
from src.domain.repository.user import CreateUserRepositoryInterface
from src.infra.db import DBConnection


class CreateUserRepository(CreateUserRepositoryInterface):

    __db = None
    
    def __init__(self) -> None:
        super().__init__()
        self.__db = DBConnection()

    def create(self, name: str, username: str, password: str):
        try:
            query = '''
            INSERT INTO tbl_users 
            (name, username, password) 
            VALUES ('{}','{}','{}');'''.format(name, username, password)
            result = self.__db.write_query(query)
        except Exception as e:
            return e
        else:
            return result