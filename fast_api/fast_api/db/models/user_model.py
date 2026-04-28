# fast_api/db/models/user_model.py

from datetime import datetime

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from fast_api.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    username: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # Added timestamp
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )