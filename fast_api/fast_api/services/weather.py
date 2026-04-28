import httpx


async def get_coordinates(country: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={country}&count=1&language=en&format=json"
        )
        return response.json()


async def get_weather(latitude: float, longitude: float) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code,wind_speed_10m,apparent_temperature,relative_humidity_2m"
        )
        return response.json()
