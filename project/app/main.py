from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI()


# The Depends function is a dependency that declares another dependency, get_settings.
@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
