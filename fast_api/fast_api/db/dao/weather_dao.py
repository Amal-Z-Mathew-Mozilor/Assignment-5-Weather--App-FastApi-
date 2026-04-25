from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fast_api.db.dependencies import get_db_session
from fast_api.db.models import Weather
from datetime import datetime
class WeatherDAO:
    def __init__(self,session:AsyncSession=Depends(get_db_session)):
        self.session=session

    async def save_weather(self,user:int,data:dict):
        time_value = data.get("time")
        if isinstance(time_value, str):
           time_value = datetime.fromisoformat(time_value)

        record = Weather(
            user_id=user,
            city=data["city"],
            country=data["country"],
            temperature=data["temperature"],
            feels_like=data["feels_like"],
            humidity=data["humidity"],
            wind=data["wind"],
            time=time_value
        )
        self.session.add(record)
        await self.session.commit()
    async def get_user_records(self,user:int):
        result=await self.session.execute(select(Weather).where(Weather.user_id==user))
        return list(result.scalars().fetchall())

  
        
     