from fastapi import FastAPI
from .microservice.user_interface import router as user_interface_router

def create_app() -> FastAPI:
    app = FastAPI(title="Ecommerce Microservice", version="1.0.0")
    app.include_router(user_interface_router)
    return app
