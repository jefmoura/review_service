from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.service.config import settings
from app.service.urls import api_router

app = FastAPI(
    title=settings.PROJECT_NAME, version=settings.API_VERSION, debug=settings.API_DEBUG
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_VERSION_PREFIX)
