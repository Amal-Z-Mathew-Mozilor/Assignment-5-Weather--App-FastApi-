from pydantic import BaseModel
from datetime import datetime 
class WeatherResponse(BaseModel):
    city: str
    country: str
    latitude: float
    longitude: float
    temperature: float
    feels_like: float
    humidity: int
    wind: float | None
    time: str

class SavedWeatherResponse(BaseModel):
    id: int
    user_id: int
    city: str
    country: str
    temperature: float
    feels_like: float
    humidity: int
    wind: float | None
    time: datetime 

    class Config:
        from_attributes = True 