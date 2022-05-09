from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.infra.auth.jwt_generated import JWTTokenGenerated

class JWTBearer(HTTPBearer):
    def __init__(self, auto_Error : bool = True) -> None:
        super(JWTBearer, self).__init__(auto_error=auto_Error)
    
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=401, details="Invalid or Expired Token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=401, details="Invalid or Expired Token")

    def verify_jwt(self, jwtToken: str):
        isTokenValid: bool = False
        payload = JWTTokenGenerated().decodeJWT(token=jwtToken)
        if payload:
            isTokenValid = True
        return isTokenValid