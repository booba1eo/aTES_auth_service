from fastapi import FastAPI

from app.core.orm import init_db
from app.core.settings import settings
from app.routers.routers import router


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=settings.OPENAPI_URL,
    servers=settings.PROJECT_SERVERS,
    root_path=settings.LOCAL_ROOT_PATH if settings.IS_LOCAL else settings.SERVER_ROOT_PATH,
    root_path_in_servers=False
)


app.include_router(router)


@app.on_event("startup")
async def startup_event():
    init_db(app)
