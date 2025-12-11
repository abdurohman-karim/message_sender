from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.partners import router as partners_router
from app.db.session import engine
from app.db.base import Base  # важно: импорт, который подтянет модели


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.API_TITLE,
        version=settings.API_VERSION,
    )

    app.include_router(partners_router)

    @app.on_event("startup")
    def on_startup():
        # Для простоты: создавать таблицы автоматически
        Base.metadata.create_all(bind=engine)

    return app


app = create_app()
