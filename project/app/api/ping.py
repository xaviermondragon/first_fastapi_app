from fastapi import APIRouter, Depends

from app.config import get_settings, Settings

router = APIRouter()


# The Depends function is a dependency that declares another dependency, get_settings.
@router.get("/ping")
async def pong(settings:Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }