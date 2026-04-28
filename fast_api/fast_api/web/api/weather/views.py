from fastapi import APIRouter, Depends, HTTPException
from fast_api.db.dao.weather_dao import WeatherDAO
from fast_api.db.dao.user_dao import UserDAO
from fast_api.web.api.weather.schema import WeatherResponse, SavedWeatherResponse
from fast_api.db.models.user_model import User
from fast_api.services.dependencies import get_current_user
from fast_api.services.weather import get_coordinates, get_weather
router = APIRouter()
@router.get("/fetch_weather", response_model=WeatherResponse)
async def fetchweather(city: str) -> WeatherResponse:
    c1 = await get_coordinates(city)
    if "results" not in c1 or len(c1["results"]) == 0:
        raise HTTPException(status_code=404, detail="City not found")
    loc = c1["results"][0]
    c2 = await get_weather(loc["latitude"], loc["longitude"])
    current = c2["current"]
    return {
        "city": loc["name"],
        "country": loc["country"],
        "latitude": loc["latitude"],
        "longitude": loc["longitude"],
        "temperature": current["temperature_2m"],
        "feels_like": current["apparent_temperature"],
        "humidity": current["relative_humidity_2m"],
        "wind": current.get("wind_speed_10m"),
        "time": current["time"],
    }
@router.post("/save")
async def save_weather(
    data: WeatherResponse,
    current_user: User = Depends(get_current_user),
    dao: WeatherDAO = Depends(),
) -> dict:
    await dao.save_weather(current_user.id, data.model_dump())
    return {"message": "Weather saved successfully"}
@router.get("/history", response_model=list[SavedWeatherResponse])
async def get_history(
    current_user: User = Depends(get_current_user),
    dao: WeatherDAO = Depends(),
) -> list[SavedWeatherResponse]:
    return await dao.get_user_records(current_user.id)