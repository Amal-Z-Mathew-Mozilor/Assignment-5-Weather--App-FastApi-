from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fast_api.db.dependencies import get_db_session
from fast_api.db.models.weather_model import Weather
from datetime import datetime
class WeatherDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
    async def save_weather(self, user_id: int, data: dict) -> None:
        time_value = data.get("time")
        if isinstance(time_value, str):
            time_value = datetime.fromisoformat(time_value)
        record = Weather(
            user_id=user_id,
            city=data["city"],
            country=data["country"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            temperature=data["temperature"],
            feels_like=data["feels_like"],
            humidity=data["humidity"],
            wind=data["wind"],
            time=time_value,
        )
        self.session.add(record)
        await self.session.flush()
        await self.session.refresh(record)
    async def get_user_records(self, user_id: int) -> list[Weather]:
        result = await self.session.execute(
            select(Weather).where(Weather.user_id == user_id)
        )
        return list(result.scalars().fetchall())