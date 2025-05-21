from fastapi import APIRouter
from .controllers.product_controller import router as product_controller

router = APIRouter()
router.include_router(product_controller, prefix="/product", tags=["product"])