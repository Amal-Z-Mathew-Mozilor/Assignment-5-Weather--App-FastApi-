from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fast_api.db.dao.user_dao import UserDAO
from fast_api.db.models.user_model import User
from fast_api.services.jwt import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    dao: UserDAO = Depends(),
) -> User:
    email = decode_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = await dao.get_by_email(email)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user
