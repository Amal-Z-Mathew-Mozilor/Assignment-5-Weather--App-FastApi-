from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from passlib.context import CryptContext
from fast_api.db.dependencies import get_db_session
from fast_api.db.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalars().first()

    async def create_user(self, email: str, password: str) -> User:
        hashed = pwd_context.hash(password)
        user = User(email=email, password=hashed)
        self.session.add(user)
        await self.session.commit()
        return user

    def verify_password(self, plain: str, hashed: str) -> bool:
        return pwd_context.verify(plain, hashed)