from fastapi import FastAPI

from app.api.router import api_router
from app.core.errors import register_exception_handlers


def create_app() -> FastAPI:
    application = FastAPI(
        title="Gestion de Pasajes Ecuador API",
        description="API para la gestion de pasajes en Ecuador.",
        version="0.1.0",
    )
    application.include_router(api_router)
    register_exception_handlers(application)
    return application


app = create_app()