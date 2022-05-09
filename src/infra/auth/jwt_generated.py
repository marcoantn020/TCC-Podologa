from abc import abstractmethod
import time
import jwt
from decouple import config
from src.domain.contracts.token import TokenInterface

class JWTTokenGenerated(TokenInterface):

    def token_response(self, token: str):
        return token

    def signJWT(self, userID: str):
        payload = {
            "userID": userID,
            "expiry": time.time() + 600
        }
        token = jwt.encode(payload=payload, key=config("SECRET_KEY"), algorithm=config("ALGORITHM"))
        return self.token_response(token=token)

    def decodeJWT(self, token: str):
        try:
            decode_token = jwt.decode(token=token, key=config("SECRET_KEY"), algorithms=config("ALGORITHM"))
            return decode_token if decode_token['expires'] >= time.time() else None
        except:
            return {}