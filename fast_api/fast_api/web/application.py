from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fast_api.log import configure_logging
from fast_api.web.api.router import api_router
from fast_api.web.lifespan import lifespan_setup

APP_ROOT = Path(__file__).parent.parent


def get_app() -> FastAPI:
    configure_logging()
    app = FastAPI(
        title="fast_api",
        lifespan=lifespan_setup,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/api/openapi.json",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:8000",
            "http://127.0.0.1:8000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router=api_router, prefix="/api")
    app.mount("/static", StaticFiles(directory=APP_ROOT / "static"), name="static")
    app.mount("/", StaticFiles(directory=APP_ROOT / "static", html=True), name="root")

    return app
