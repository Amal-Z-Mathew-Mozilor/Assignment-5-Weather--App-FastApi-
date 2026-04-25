from fastapi.routing import APIRouter

from fast_api.web.api import docs, monitoring
from fast_api.web.api.weather import views as weather_views
from fast_api.web.api.auth import views as auth_views
api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(auth_views.router)      # ✅ adds /auth/signup, /auth/login
api_router.include_router(weather_views.router)