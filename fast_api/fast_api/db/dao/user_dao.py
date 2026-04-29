import bcrypt
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fast_api.db.dependencies import get_db_session
from fast_api.db.models.user_model import User
from fast_api.services.auth import hash_password, verify_password


class UserDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)) -> None:
        self.session = session

    async def create_user(self, email: str, password: str, username: str | None = None) -> User:
        hashed = hash_password(password)
        user = User(email=email, hashed_password=hashed, username=username)
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)
        return user

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalars().first()
