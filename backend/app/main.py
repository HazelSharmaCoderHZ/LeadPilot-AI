from fastapi import FastAPI
from app.api.routes.workflow import router as workflow_router

from app.api.v1.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

app.include_router(
    health_router,
    prefix=settings.API_V1_PREFIX,
)

app.include_router(workflow_router)

@app.get("/")
async def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }