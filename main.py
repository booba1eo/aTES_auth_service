from fastapi import FastAPI

from app.core.orm import init_db
from app.core.settings import settings
# from app.routers.routers import router


app = FastAPI(title=settings.PROJECT_NAME)

# app.include_router(router)

@app.on_event("startup")
async def startup_event():
    init_db(app)
