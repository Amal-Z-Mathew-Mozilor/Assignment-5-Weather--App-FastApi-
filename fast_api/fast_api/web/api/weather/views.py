from fastapi import APIRouter, Depends, HTTPException
import httpx
from fast_api.db.dao.weather_dao import WeatherDAO
from fast_api.db.dao.user_dao import UserDAO
from fast_api.web.api.weather.schema import WeatherResponse, SavedWeatherResponse
from fast_api.web.api.auth.jwt import get_current_user

router = APIRouter(prefix="/weather", tags=["Weather"])

async def get_coordinates(country: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={country}&count=1&language=en&format=json"
        )
        return response.json()

async def get_weather(latitude: float, longitude: float):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code,wind_speed_10m,apparent_temperature,relative_humidity_2m"
        )
        return response.json()

@router.get("/fetch_weather", response_model=WeatherResponse)
async def fetchweather(country: str):
    # no auth needed here — anyone can fetch weather
    c1 = await get_coordinates(country)
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
        "time": current["time"]
    }

@router.post("/save")
async def save_weather(
    data: WeatherResponse,
    current_email: str = Depends(get_current_user),  
    dao: WeatherDAO = Depends(),
    user_dao: UserDAO = Depends()
):
    user = await user_dao.get_by_email(current_email)
    await dao.save_weather(user.id, data.model_dump())
    return {"message": "Weather saved successfully"}

@router.get("/history", response_model=list[SavedWeatherResponse])
async def get_history(
    current_email: str = Depends(get_current_user),  
    dao: WeatherDAO = Depends(),
    user_dao: UserDAO = Depends()
):
    user = await user_dao.get_by_email(current_email)
    return await dao.get_user_records(user.id)