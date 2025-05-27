from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...infrastructure.db.engine import SessionLocal
from ...infrastructure.repositories.product_repository import (
    SQLProductRepository,
)
from ...application_core.product.use_cases.find_product import FindProductUseCase
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all")
def get_all_products(db: Session = Depends(get_db)):
    repo = SQLProductRepository(db)
    use_case = FindProductUseCase(repo)
    result = use_case.execute()
    return result
