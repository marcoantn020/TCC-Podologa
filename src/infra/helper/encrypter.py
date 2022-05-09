

import bcrypt
from src.domain.contracts import EncrypterInterface


class Encrypter(EncrypterInterface):

    def encrypter(self,value: str) -> str:
        return bcrypt.hashpw(value.encode('utf8'), bcrypt.gensalt(8)).decode("utf8")

    def decrypter(self, value: str, hash: str) -> bool:
        return bcrypt.checkpw(value.encode('utf8'), hash.encode("utf8"))