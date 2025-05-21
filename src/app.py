from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .microservice.user_interface import router as user_interface_router


def create_app() -> FastAPI:
    app = FastAPI(title="Ecommerce Microservice", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(user_interface_router)
    return app
